"""Optimisation driver.

Runs ACO to generate candidate routes, then DE and GA to select the best route
set, and finally evaluates the objective-function score of:
    ACO+DE, ACO+AG and Dijkstra baselines.

The route selection result for ACO+AG is used as the "optimised" network
configuration (as in the thesis).  Results are cached to ``cache_*`` files so
the heavy ACO stage only needs to run once.
"""
import os
import numpy as np

from .data import load_topology
from .dijkstra import dijkstra_routes
from .aco import aco_generate_routes
from .de import de_aco
from .ga import ga_aco
from .objective import linkc5

_CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def build_app_blocks(mrotas, top):
    """Return {app_index: [lo_row, hi_row]} contiguous blocks in mrotas."""
    n = top.n
    app_of_row = mrotas[:, n + 6].astype(int)
    blocks = {}
    for r in range(mrotas.shape[0]):
        a = int(app_of_row[r])
        lo, hi = blocks.get(a, [r + 1, r + 1])
        blocks[a] = [lo, max(hi, r + 1)]
    return {a: [blocks[a][0], blocks[a][1]] for a in sorted(blocks)}


def run_optimization(aco_ants=100, aco_iters=100, de_iters=200, ga_iters=200,
                     node_pop=50, seed=42, force=False):
    top = load_topology()
    n = top.n

    # ---- Dijkstra baseline (FO should be ~120 on topology 1) ----
    mrotas_dj = dijkstra_routes(top)
    fodi = linkc5(np.arange(1, top.napp + 1), mrotas_dj, top, top.napp)

    # ---- ACO candidate routes ----
    cache_file = os.path.join(_CACHE, "cache_mrotas_aco.npy")
    if os.path.exists(cache_file) and not force:
        mrotas = np.load(cache_file)
        tm = mrotas.shape[0]
    else:
        mrotas, n_, tm = aco_generate_routes(top, nAnt=aco_ants, MaxIt=aco_iters,
                                             seed=seed)
        np.save(cache_file, mrotas)

    app_blocks = build_app_blocks(mrotas, top)
    # random per-app selection baseline
    rng = np.random.default_rng(1)
    rotas_sel = np.array([rng.integers(lo, hi + 1)
                          for lo, hi in app_blocks.values()])
    frnd = linkc5(rotas_sel, mrotas, top, tm)

    # ---- DE ----
    best_de, _, bc_de = de_aco(top, mrotas, tm, rotas_sel,
                               niter=de_iters, nPop=node_pop, pCR=0.2, seed=7,
                               app_blocks=app_blocks)
    # ---- GA ----
    best_ga, _, bc_ga = ga_aco(top, mrotas, tm, rotas_sel,
                               niter=ga_iters, nPop=node_pop, pc=0.9, pm=0.3,
                               seed=8, app_blocks=app_blocks)
    fo_de = linkc5(best_de["Position"], mrotas, top, tm)
    fo_ga = linkc5(best_ga["Position"], mrotas, top, tm)

    result = {
        "top": top,
        "mrotas_aco": mrotas,
        "mrotas_dj": mrotas_dj,
        "fo_dijkstra": fodi,
        "fo_random": frnd,
        "fo_de": fo_de,
        "fo_ga": fo_ga,
        "best_de": best_de["Position"],
        "best_ga": best_ga["Position"],
        "bestcost_de": bc_de,
        "bestcost_ga": bc_ga,
        "app_blocks": app_blocks,
    }
    return result


def routes_from_idx(mrotas, idx, n):
    """Convert a selection vector (1-based row indices) into per-app node routes."""
    idx = np.atleast_1d(np.asarray(idx))
    routes = {}
    for a, ri in enumerate(idx):
        row = mrotas[int(ri) - 1]
        routes[a + 1] = [int(x) for x in row[:n] if x != 0]
    return routes


def dijkstra_route_dict(mrotas_dj, n, napp):
    routes = {}
    for a in range(1, napp + 1):
        row = mrotas_dj[a - 1]
        routes[a] = [int(x) for x in row[:n] if x != 0]
    return routes