#!/usr/bin/env python3
"""Exp10: record best-FO convergence curves (per generation) of ACO+GA and
ACO+DE at nominal load, 20 seeds, on all topologies -- the classic
thesis figure upgraded with statistical replication."""
import os
import sys
import json
import time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sdn.topologies import get_topologies
from sdn.ga import ga_aco
from sdn.de import de_aco
from sdn.run_optimization import build_app_blocks
from sdn.loadmodel import loaded_topology, extend_pool, augment_pool_with_cspf
from sdn.cspf import cspf_route

SEEDS = list(range(20))
ITERS, POP = 300, 50
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(OUT, exist_ok=True)


def main():
    tops = get_topologies()
    out = {}
    for top in tops:
        tf = loaded_topology(top, 1.0)          # nominal (same demand model)
        cs = cspf_route(tf)                     # constructive seed (paper protocol)
        curves = {"ga": [], "de": []}
        for seed in SEEDS:
            pool_file = os.path.join(OUT, "pools",
                                     f"pool_{top.name}_s{seed}.npy")
            mrotas = np.load(pool_file)
            mrotas = extend_pool(mrotas, top, tf)
            mrotas = augment_pool_with_cspf(mrotas, tf, cs)
            tm = mrotas.shape[0]
            blocks = build_app_blocks(mrotas, tf)
            rng = np.random.default_rng(1000 * seed + 100)
            rs = np.array([rng.integers(lo, hi + 1)
                           for lo, hi in blocks.values()])
            t0 = time.time()
            _, _, bc_ga = ga_aco(tf, mrotas, tm, rs, niter=ITERS, nPop=POP,
                                 pc=0.9, pm=0.3, seed=seed,
                                 app_blocks=blocks)
            _, _, bc_de = de_aco(tf, mrotas, tm, rs, niter=ITERS, nPop=POP,
                                 pCR=0.2, seed=seed, app_blocks=blocks)
            curves["ga"].append([float(x) for x in bc_ga])
            curves["de"].append([float(x) for x in bc_de])
            print(f"{top.name} seed={seed} done ({time.time()-t0:.0f}s) "
                  f"GA={bc_ga[-1]:.0f} DE={bc_de[-1]:.0f}", flush=True)
        out[top.name] = curves
    meta = {
        "protocol": "ACO pool (100x100, per-seed) + k-shortest extras + "
                    "CSPF pool augmentation; GA 300x50 pc=0.9; DE 300x50 pCR=0.2",
        "seeds": SEEDS, "iterations": ITERS, "population": POP,
        "pool_augmentation": True, "load": 1.0,
        "note": "convergence_noaugment.json holds the ablation without "
                "augmentation (GA only)",
    }
    with open(os.path.join(OUT, "convergence_meta.json"), "w") as fh:
        json.dump(meta, fh, indent=1)
    # never silently overwrite: archive any previous version first
    target = os.path.join(OUT, "convergence.json")
    if os.path.exists(target):
        import shutil
        archive = os.path.join(OUT, "archive")
        os.makedirs(archive, exist_ok=True)
        stamp = time.strftime("%Y%m%d_%H%M%S")
        shutil.copy(target,
                    os.path.join(archive, f"convergence_{stamp}.json"))
    with open(target, "w") as fh:
        json.dump(out, fh)
    print("CONVERGENCE DONE", flush=True)


if __name__ == "__main__":
    main()