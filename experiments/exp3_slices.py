#!/usr/bin/env python3
"""Exp3: slice-isolation experiment (URLLC stability vs background load).

Compares the certified-optimal routing (ILP-MCF at nominal load) against
Dijkstra routing.  URLLC flows (apps 8, 9, 13, 15) stay at nominal rate while
the background slices (mMTC data + eMBB video) are progressively amplified.
Packet-level simpy simulation reports URLLC delay, jitter and loss as a
function of background multiplier -- measuring whether the optimizer's
hard-capacity routing provides logical slice isolation.
"""
import os
import sys
import json
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sdn.data import load_topology
from sdn.ilp import ilp_link_mcf
from sdn.dijkstra import dijkstra_routes
from sdn.netsim import simulate_network

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(OUT, exist_ok=True)
URLLC = [8, 9, 13, 15]
MULTS = [1.0, 1.5, 2.0, 3.0, 4.0]


def scaled_routes(top, routes, mult):
    """Copy of the demand table with background slices scaled by mult."""
    t2 = top.tds.copy()
    for k in range(1, top.napp + 1):
        if k not in URLLC:            # background = eMBB + mMTC
            t2[k - 1, 2] = top.tds[k - 1, 2] * mult
    top2 = top.with_load(1.0)
    top2.tds = t2
    return top2


def main():
    import os
    from sdn.topologies import get_all_instances
    sel = os.environ.get("DSH_SLICE_TOPOS", "maia52").split(",")
    sel = [s.strip() for s in sel if s.strip()]
    insts = {t.name: t for t in get_all_instances()}

    out = []
    for name in sel:
        top = insts[name]
        print(f"=== {name} ===", flush=True)

        # certified-optimal routing at nominal load
        res = ilp_link_mcf(top, load_factor=1.0, time_limit=300)
        if res["status"] != "Optimal":
            print(f"{name}: ILP infeasible at nominal load -- skip", flush=True)
            continue
        routes_opt = {int(k): [int(x) for x in v]
                      for k, v in res["routes"].items()}
        mr = dijkstra_routes(top)
        routes_dj = {a: [int(x) for x in mr[a - 1][:top.n] if x != 0]
                     for a in range(1, top.napp + 1)}

        for mult in MULTS:
            for algo, routes in [("ilp_opt", routes_opt), ("dijkstra", routes_dj)]:
                t2 = scaled_routes(top, routes, mult)
                r = simulate_network(t2, routes, duration=5.0,
                                     max_queue_pkts=80, seed=7)
                d = np.mean([r[a]["mean_delay_ms"] for a in URLLC])
                j = np.mean([r[a]["jitter_ms"] for a in URLLC])
                l = float(np.mean([r[a]["loss"] for a in URLLC]))
                thr = float(np.mean([r[a]["throughput_mbps"] for a in URLLC]))
                rec = {"topo": name, "algo": algo,
                       "background_mult": mult,
                       "urllc_delay_ms": d, "urllc_jitter_ms": j,
                       "urllc_loss": l, "urllc_throughput_mbps": thr}
                out.append(rec)
                print(json.dumps(rec), flush=True)
    with open(os.path.join(OUT, "slice_isolation.json"), "w") as fh:
        json.dump(out, fh, indent=1)
    print("SLICES DONE", flush=True)


if __name__ == "__main__":
    main()