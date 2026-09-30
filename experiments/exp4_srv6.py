#!/usr/bin/env python3
"""Exp4: data-plane state accounting (OpenFlow vs SRv6) on all topologies.

Uses two routing philosophies (shortest-path Dijkstra and the certified
optimal routing) to show the state reduction is structural, i.e. independent
of which routing algorithm produced the paths.
"""
import os
import sys
import json
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sdn.topologies import get_all_instances as get_topologies
from sdn.dijkstra import dijkstra_routes
from sdn.cspf import cspf_route
from sdn.srv6_state import state_counts
from sdn.ilp import ilp_link_mcf

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(OUT, exist_ok=True)


def main():
    rows = []
    tops = get_topologies()
    for top in tops:
        mr = dijkstra_routes(top)
        r_dj = {a: [int(x) for x in mr[a - 1][:top.n] if x != 0]
                for a in range(1, top.napp + 1)}
        r_cspf = cspf_route(top)
        res = ilp_link_mcf(top, load_factor=1.0, time_limit=300)
        r_opt = None
        if res["status"] == "Optimal":
            r_opt = {int(k): [int(x) for x in v]
                     for k, v in res["routes"].items()}
        for algo, routes in [("dijkstra", r_dj), ("cspf", r_cspf),
                             ("ilp_opt", r_opt)]:
            if routes is None:
                continue
            sc = state_counts(top, routes)
            rows.append({"topo": top.name, "algo": algo, **sc})
            print(f"{top.name:10s} {algo:9s} OF={sc['of_total_rules']:4d} "
                  f"(max/node={sc['of_max_node_rules']:3d}) "
                  f"SRv6={sc['srv6_total_rules']:3d} "
                  f"reduction={sc['reduction_factor']:.1f}x "
                  f"maxSL={sc['max_segment_list']}", flush=True)
    with open(os.path.join(OUT, "srv6_state.json"), "w") as fh:
        json.dump(rows, fh, indent=1)
    print("SRV6 DONE", flush=True)


if __name__ == "__main__":
    main()