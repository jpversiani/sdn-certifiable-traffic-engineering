#!/usr/bin/env python3
"""Exp2: load-sweep experiment with statistical replication.

Algorithms: dijkstra, cspf, qlearn, aco_ga, aco_de, ilp_pool, ilp_mcf.
Design: 3 topologies x 5 load factors x 20 seeds (stochastic algorithms).
The ACO candidate pool is generated once per (topology, seed) at nominal
load and reused across the sweep (route diversity is load-independent;
the selection adapts to load).  All results are appended to
results/sweep.jsonl incrementally so partial progress is never lost.
"""
import os
import sys
import json
import time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sdn.topologies import get_all_instances as get_topologies
from sdn.metrics import evaluate_routes
from sdn.dijkstra import dijkstra_routes
from sdn.cspf import cspf_route
from sdn.qlearn import qlearn_route
from sdn.ga import ga_aco
from sdn.de import de_aco
from sdn.ilp import ilp_pool, ilp_link_mcf
from sdn.run_optimization import build_app_blocks, routes_from_idx
from sdn.loadmodel import loaded_topology, extend_pool, augment_pool_with_cspf

SEEDS = list(range(20))
LOADS = [0.5, 0.75, 1.0, 1.25, 1.5]
GA_ITERS, GA_POP = 300, 50
QL_EPISODES = 100
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(OUT, exist_ok=True)
JSONL = os.path.join(OUT, "sweep.jsonl")


def record(rec):
    with open(JSONL, "a") as fh:
        fh.write(json.dumps(rec) + "\n")


def _dijkstra_dict(top):
    """dijkstra_routes returns the mrotas matrix; convert to routes dict."""
    mr = dijkstra_routes(top)
    return {a: [int(x) for x in mr[a - 1][:top.n] if x != 0]
            for a in range(1, top.napp + 1)}


def run_deterministic(algo, fun, top, lf):
    t0 = time.perf_counter()
    routes = fun(top)
    ev = evaluate_routes(top, routes, 1.0)
    return {"algo": algo, "topo": top.name, "load": lf, "seed": None,
            **ev, "time_s": time.perf_counter() - t0}


def main():
    tops = get_topologies()
    done = set()
    if os.path.exists(JSONL):
        with open(JSONL) as fh:
            for line in fh:
                try:
                    r = json.loads(line)
                    done.add((r["algo"], r["topo"], r["load"], r["seed"]))
                except Exception:
                    pass

    for top in tops:
        for f in LOADS:
            tf = loaded_topology(top, f, seed=77)   # f<=1 scales; f>1 adds flows
            lf = round(f, 2)
            routes_cspf_ref = cspf_route(tf)        # constructive seed (shared)
            # ---------------- deterministic baselines ----------------
            for algo, fun in [("dijkstra", _dijkstra_dict),
                              ("cspf", cspf_route)]:
                if (algo, top.name, lf, None) not in done:
                    rec = run_deterministic(algo, fun, tf, lf)
                    record(rec); done.add((algo, top.name, lf, None))
                    print(f"[{rec['algo']} {top.name} f={lf}] "
                          f"FO={rec['fo_original']:.0f} feas={rec['feasible']} "
                          f"maxu={rec['max_util']:.2f}", flush=True)
            # ---------------- exact ILP (link MCF) ----------------
            if ("ilp_mcf", top.name, lf, None) not in done:
                t0 = time.perf_counter()
                res = ilp_link_mcf(tf, load_factor=1.0, time_limit=300)
                rec = {"algo": "ilp_mcf", "topo": top.name, "load": lf,
                       "seed": None, "status": res["status"],
                       "time_s": time.perf_counter() - t0}
                if res["status"] == "Optimal":
                    ev = evaluate_routes(tf, res["routes"], 1.0)
                    rec.update(ev)
                    rec["Z_exact"] = res["Z"]
                record(rec); done.add(("ilp_mcf", top.name, lf, None))
                print(f"[ilp_mcf {top.name} f={lf}] {res['status']} "
                      f"Z={res.get('Z')} t={rec['time_s']:.0f}s", flush=True)

            # ---------------- stochastic algorithms ----------------
            for seed in SEEDS:
                pool_file = os.path.join(OUT, "pools",
                                         f"pool_{top.name}_s{seed}.npy")
                if not os.path.exists(pool_file):
                    print(f"MISSING POOL {pool_file}", flush=True)
                    continue
                mrotas = np.load(pool_file)
                tm = mrotas.shape[0]
                # extend the pool with k-shortest routes for extra flows,
                # then augment with the CSPF constructive solution per flow
                mrotas = extend_pool(mrotas, top, tf)
                mrotas = augment_pool_with_cspf(mrotas, tf, routes_cspf_ref)
                tm = mrotas.shape[0]
                blocks = build_app_blocks(mrotas, top)
                rng = np.random.default_rng(1000 * seed + int(lf * 100))
                rotas_sel = np.array([rng.integers(lo, hi + 1)
                                      for lo, hi in blocks.values()])

                # ACO+GA
                if ("aco_ga", top.name, lf, seed) not in done:
                    t0 = time.perf_counter()
                    best, _, _ = ga_aco(tf, mrotas, tm, rotas_sel,
                                        niter=GA_ITERS, nPop=GA_POP,
                                        pc=0.9, pm=0.3, seed=seed,
                                        app_blocks=blocks)
                    routes = routes_from_idx(mrotas, best["Position"], tf.n)
                    ev = evaluate_routes(tf, routes, 1.0)
                    rec = {"algo": "aco_ga", "topo": top.name, "load": lf,
                           "seed": seed, **ev,
                           "time_s": time.perf_counter() - t0}
                    record(rec); done.add(("aco_ga", top.name, lf, seed))
                # ACO+DE
                if ("aco_de", top.name, lf, seed) not in done:
                    t0 = time.perf_counter()
                    best, _, _ = de_aco(tf, mrotas, tm, rotas_sel,
                                        niter=GA_ITERS, nPop=GA_POP,
                                        pCR=0.2, seed=seed,
                                        app_blocks=blocks)
                    routes = routes_from_idx(mrotas, best["Position"], tf.n)
                    ev = evaluate_routes(tf, routes, 1.0)
                    rec = {"algo": "aco_de", "topo": top.name, "load": lf,
                           "seed": seed, **ev,
                           "time_s": time.perf_counter() - t0}
                    record(rec); done.add(("aco_de", top.name, lf, seed))
                # Q-learning
                if ("qlearn", top.name, lf, seed) not in done:
                    t0 = time.perf_counter()
                    routes = qlearn_route(tf, seed=seed, episodes=QL_EPISODES)
                    ev = evaluate_routes(tf, routes, 1.0)
                    rec = {"algo": "qlearn", "topo": top.name, "load": lf,
                           "seed": seed, **ev,
                           "time_s": time.perf_counter() - t0}
                    record(rec); done.add(("qlearn", top.name, lf, seed))
                # ILP-P (pool optimum for this seed's pool)
                if ("ilp_pool", top.name, lf, seed) not in done:
                    t0 = time.perf_counter()
                    res = ilp_pool(tf, mrotas, tm, blocks, load_factor=1.0,
                                   time_limit=60)
                    rec = {"algo": "ilp_pool", "topo": top.name, "load": lf,
                           "seed": seed, "status": res["status"],
                           "fo_poolopt": res["fo"],
                           "time_s": time.perf_counter() - t0}
                    record(rec); done.add(("ilp_pool", top.name, lf, seed))
            print(f"== finished {top.name} load={lf} ==", flush=True)
    print("SWEEP DONE", flush=True)


if __name__ == "__main__":
    main()