#!/usr/bin/env python3
"""Exp7: packet-level QoS with replication (5 sim seeds) for CI reporting."""
import os
import sys
import json
import time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sdn.data import load_topology
from sdn.ilp import ilp_link_mcf
from sdn.dijkstra import dijkstra_routes
from sdn.netsim import simulate_network

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(OUT, exist_ok=True)


def main():
    top = load_topology()
    res = ilp_link_mcf(top, load_factor=1.0, time_limit=300)
    routes_opt = {int(k): [int(x) for x in v]
                  for k, v in res["routes"].items()}
    mr = dijkstra_routes(top)
    routes_dj = {a: [int(x) for x in mr[a - 1][:top.n] if x != 0]
                 for a in range(1, top.napp + 1)}

    out = []
    for seed in range(1, 6):
        for algo, routes in [("ilp_opt", routes_opt), ("dijkstra", routes_dj)]:
            t0 = time.time()
            r = simulate_network(top, routes, duration=5.0,
                                 max_queue_pkts=80, seed=seed)
            m = {
                "algo": algo, "seed": seed,
                "mean_throughput_mbps": float(np.mean(
                    [r[a]["throughput_mbps"] for a in r])),
                "mean_delay_ms": float(np.mean(
                    [r[a]["mean_delay_ms"] for a in r])),
                "mean_jitter_ms": float(np.mean(
                    [r[a]["jitter_ms"] for a in r])),
                "mean_loss": float(np.mean([r[a]["loss"] for a in r])),
                "sim_time_s": time.time() - t0,
            }
            out.append(m)
            print(json.dumps(m), flush=True)
    with open(os.path.join(OUT, "qos_sim.json"), "w") as fh:
        json.dump(out, fh, indent=1)
    print("QOSSIM DONE", flush=True)


if __name__ == "__main__":
    main()