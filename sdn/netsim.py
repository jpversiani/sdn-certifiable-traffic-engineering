"""Discrete-event network simulator (simpy) that reproduces the SDN / D-ITG
emulation of the thesis: packets of 512 bytes are injected per application
at a constant rate; they traverse the computed route, being queued at each
link whose capacity (from ``top.VA``, shared per undirected pair -- same
convention as the optimizer) and one-way delay (AT matrix) model the core.

Measurement conventions (documented in the paper):
    - throughput  : delivered goodput = received packets x bits / window
    - end-to-end delay (atraso fim-a-fim): mean over delivered packets
    - jitter      : mean absolute consecutive-delay variation (RFC 3550
                    style); NOT the D-ITG estimator
    - packet loss : admission drops only (bounded FIFO); packets still in
                    flight at the end of the window are neither delivered
                    nor counted as lost

The routes themselves come from the optimisation stage (see run_optimization.py)
and are passed as a dict {app_index: list_of_nodes}.
"""
import simpy
import numpy as np

PACKET_BYTES = 512
BITS_PER_PACKET = PACKET_BYTES * 8


def pkt_rate_mbps(flow_mbps):
    return flow_mbps * 1e6 / BITS_PER_PACKET


class Link:
    """A directed link: capacity (Mbps) and one-way propagation delay (ms).

    Transmission is modelled as a serial resource of capacity 1 so the link
    bandwidth is respected: when the aggregate offered load exceeds the link
    capacity the packets queue, producing queuing delay (jitter) and, if the
    queue exceeds ``max_queue``, packet drops (loss).
    """
    __slots__ = ("cap_bps", "delay_s", "tx", "buffer", "in_queue")

    def __init__(self, env, cap_mbps, delay_ms):
        self.cap_bps = cap_mbps * 1e6
        self.delay_s = delay_ms / 1000.0
        self.tx = simpy.Resource(env, capacity=1)   # serialises transmission
        self.buffer = simpy.Store(env)
        self.in_queue = 0


class Packet:
    __slots__ = ("flow_id", "created", "app_id")

    def __init__(self, app_id, created, ensemble=0):
        self.app_id = app_id
        self.created = created


class SDNNetwork:
    def __init__(self, env, top, routes, max_queue_pkts=80):
        """
        routes: dict {app_index(int,1-based): list of 1-based node ids}

        Convention alignment with the optimizer (sdn.ilp / sdn.metrics):
        the capacity of an undirected pair {u,v} is shared by both
        directions (aggregate offered load of both directions must fit the
        single capacity), and per-link capacity is read from ``top.VA``
        (not hard-coded).
        """
        self.env = env
        self.top = top
        self.routes = routes
        self.max_queue = max_queue_pkts
        # one link (shared serial resource) per undirected pair, 1-based
        self.links = {}
        for flow in routes.items():
            for u, v in zip(flow[1], flow[1][1:]):
                key = (min(u, v), max(u, v))
                if key not in self.links:
                    cap = float(top.VA[key[0] - 1, key[1] - 1])
                    self.links[key] = Link(env, cap_mbps=cap,
                                           delay_ms=float(top.AT[u - 1, v - 1]))
        # measurement recorders per application
        self.recv_time = {a: [] for a in routes}
        self.sent_count = {a: 0 for a in routes}
        self.recv_count = {a: 0 for a in routes}
        self.drop_count = {a: 0 for a in routes}
        self.packet = simpy.Resource(env, capacity=1)

    # ------------- traffic generators -------------
    def start_apps(self):
        tds = self.top.tds
        for a in range(1, self.top.napp + 1):
            flow = tds[a - 1, 2]
            self.env.process(self._app_flow(a, flow))

    def _app_flow(self, app_id, flow_mbps):
        rate = pkt_rate_mbps(flow_mbps)
        interval = 1.0 / rate
        route = self.routes[app_id]
        c = 0
        while True:
            yield self.env.timeout(max(interval, 1e-9))
            c += 1
            self.sent_count[app_id] += 1
            pkt = Packet(app_id, self.env.now, ensemble=0)
            self.env.process(self._route_packet(pkt, route, app_id))

    def _route_packet(self, pkt, route, app_id):
        # enqueue at each successive link along the route
        for u, v in zip(route[:-1], route[1:]):
            key = (min(u, v), max(u, v))
            link = self.links[key]
            # bounded FIFO buffer: drop on admission if full (loss)
            if link.in_queue >= self.max_queue:
                self.drop_count[app_id] += 1
                return
            link.in_queue += 1
            req = link.tx.request()
            yield req
            # the packet leaves the buffer and occupies the wire
            link.in_queue -= 1
            try:
                yield self.env.timeout(BITS_PER_PACKET / link.cap_bps)  # serial.
            finally:
                link.tx.release(req)
            yield self.env.timeout(link.delay_s)                    # propagation
        # reached destination after traversing all links of the route
        self.recv_count[app_id] += 1
        self.recv_time[app_id].append(self.env.now - pkt.created)

    # ------------- metrics -------------
    def results(self):
        out = {}
        tds = self.top.tds
        for a in self.routes:
            sent = self.sent_count[a]
            recv = self.recv_count[a]
            drop = self.drop_count[a]
            delays = np.array(self.recv_time[a])
            # loss counts ONLY admission drops; packets still in flight at
            # the end of the window are neither lost nor delivered
            loss = drop / sent if sent else 0.0
            # delivered goodput actually measured over the window (Mbps)
            thr = recv * BITS_PER_PACKET / self.env.now / 1e6 \
                if self.env.now > 0 else 0.0
            if delays.size >= 2:
                mean_delay = float(delays.mean())
                # jitter = mean absolute consecutive-delay variation
                # (RFC 3550-style); documented, NOT the D-ITG estimator
                jitter = float(np.abs(np.diff(delays)).mean())
            else:
                mean_delay = float(delays.mean()) if delays.size else 0.0
                jitter = 0.0
            out[a] = {
                "sent": sent,
                "recv": recv,
                "drop": drop,
                "loss": loss,
                "throughput_mbps": thr,
                "mean_delay_s": mean_delay,
                "mean_delay_ms": mean_delay * 1000.0,
                "jitter_ms": jitter * 1000.0,
            }
        return out


def simulate_network(top, routes, duration=5.0, max_queue_pkts=80, seed=0):
    """Run a simpy simulation and return per-app metrics for the given routes."""
    np.random.seed(seed)
    env = simpy.Environment()
    net = SDNNetwork(env, top, routes, max_queue_pkts=max_queue_pkts)
    net.start_apps()
    env.run(until=duration)
    return net.results()