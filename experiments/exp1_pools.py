#!/usr/bin/env python3
"""Exp1: generate the ACO candidate pools (one per topology x seed)."""
import os
import sys
import json
import time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sdn.topologies import get_all_instances
from sdn.aco import aco_generate_routes
from sdn.run_optimization import build_app_blocks

SEEDS = list(range(20))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(os.path.join(OUT, "pools"), exist_ok=True)

tops = get_all_instances()
for top in tops:
    for seed in SEEDS:
        f = os.path.join(OUT, "pools", f"pool_{top.name}_s{seed}.npy")
        if os.path.exists(f):
            print(f"skip {f} (exists)", flush=True)
            continue
        t0 = time.time()
        mrotas, n, tm = aco_generate_routes(top, nAnt=100, MaxIt=100, seed=seed)
        np.save(f, mrotas)
        print(f"{top.name} seed={seed}: {tm} routes in {time.time()-t0:.0f}s",
              flush=True)
print("POOLS DONE", flush=True)