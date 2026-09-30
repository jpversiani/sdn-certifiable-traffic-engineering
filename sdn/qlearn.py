"""Tabular Q-learning routing baseline (learning-based reference).

Implements the canonical "per-flow sequential Q-learning" routing used as an
accessible proxy for the DRL-TE literature (Xu et al. 2018; Almasan et al.
2022): each flow learns a node-level routing policy with a state space equal
to the network nodes and action space equal to the neighbour set, trained
sequentially in priority order against the load left by previously routed
flows.  It captures the same *decision structure* as a DQN (state->action
value estimation from reward samples) without the neural approximation, and
therefore exposes the same qualitative weaknesses: no hard-constraint
guarantee and training cost per scenario.
"""
import heapq
import numpy as np


def _neighbors(top, u):
    return [int(v) + 1 for v in np.flatnonzero(top.A[u - 1] > 0)]


def qlearn_route(top, seed=0, episodes=200, alpha=0.2, gamma=0.9,
                 epsilon=0.15, order_by_priority=True):
    """Train-and-route all flows sequentially; returns routes dict."""
    rng = np.random.default_rng(seed)
    tds = top.tds
    K = tds.shape[0]
    n = top.n

    order = list(range(K))
    if order_by_priority:
        order.sort(key=lambda k: (tds[k, 4], tds[k, 2]), reverse=True)

    residual = top.VA.copy()
    routes = {}

    for k in order:
        src, dst = int(tds[k, 0]), int(tds[k, 1])
        flow = tds[k, 2]
        max_d = tds[k, 3]
        Q = np.zeros((n + 1, n + 1))
        base = {u: _neighbors(top, u) for u in range(1, n + 1)}

        for _ep in range(episodes):
            u = src
            visited = {u}
            traj = []
            while u != dst and len(visited) <= n:
                nb = base[u]
                if rng.random() < epsilon:
                    a = nb[rng.integers(len(nb))]
                else:
                    a = nb[int(np.argmax(Q[u, nb]))]
                # step reward: delay cost + capacity-violation penalty
                cap = residual[u - 1, a - 1]
                delay = top.AT[u - 1, a - 1]
                pen = 0.0 if cap >= flow else 50.0
                r = -(delay / 100.0) - pen
                traj.append((u, a))
                visited.add(a)
                # bootstrap from best action at next state
                if a == dst:
                    target = r + 10.0
                else:
                    target = r + gamma * np.max(Q[a, base[a]])
                Q[u, a] += alpha * (target - Q[u, a])
                u = a
            # end-of-episode shaping: penalize paths that violate the SLA
            if u == dst:
                path = [src]
                for (uu, aa) in traj:
                    if path[-1] == uu:
                        path.append(aa)
                total_d = sum(top.AT[p - 1, q - 1]
                              for p, q in zip(path, path[1:]))
                if total_d > max_d:
                    for (uu, aa) in traj:
                        Q[uu, aa] -= 0.5

        # greedy rollout with capacity pruning
        path = _greedy_path(Q, top, src, dst, flow, residual)
        if path is None:
            # fall back to unconstrained greedy on Q (honest failure mode)
            path = _greedy_path(Q, top, src, dst, flow, None)
        routes[k + 1] = path
        for p, q in zip(path, path[1:]):
            residual[p - 1, q - 1] -= flow
            residual[q - 1, p - 1] -= flow

    return routes


def _greedy_path(Q, top, src, dst, flow, residual):
    n = top.n
    dist = {i: float("inf") for i in range(1, n + 1)}
    prev = {i: None for i in range(1, n + 1)}
    dist[src] = 0.0
    pq = [(0.0, src)]
    pops = 0
    max_pops = 8 * n + 64          # hard safety bound against any hang
    while pq and pops < max_pops:
        pops += 1
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        if u == dst:
            break
        for v in _neighbors(top, u):
            if residual is not None and residual[u - 1, v - 1] < flow:
                continue
            # Dijkstra requires non-negative weights: Q can be positive near
            # the destination (terminal bonus), so clamp the derived cost.
            edge_cost = max(1e-3, -Q[u, v] + 0.01)
            if dist[u] + edge_cost < dist[v]:
                dist[v] = dist[u] + edge_cost
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    if dist[dst] == float("inf"):
        return None
    path, cur = [], dst
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    return list(reversed(path))