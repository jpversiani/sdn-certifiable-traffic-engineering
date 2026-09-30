"""Differential Evolution (DE) route selector.

Port of the MATLAB ``deaco311.m``.  Operates on integer vectors of length
``K`` where each entry selects one candidate route (row index into the ACO
route matrix ``mrotas``) for an application.  DE evolves the population to
maximise the objective function (linkc5).
"""
import numpy as np

from .objective import linkc5


def de_aco(top, mrotas, tm, rotas_sel, niter=200, nPop=50, pCR=0.2,
           beta_min=0.2, beta_max=0.8, seed=None, app_blocks=None):
    """Returns (BestSol, pop, BestCost, Tempoexec) mirroring deaco311.

    ``app_blocks`` maps each application index (1..K) to the [lo,hi] range of
    valid rows in ``mrotas`` for that application.  When provided, every
    selected route is forced to belong to its application's block (the
    intended semantics: AG/DE pick one candidate route per application).
    """
    rng = np.random.default_rng(seed)
    if seed is not None:
        np.random.seed(seed)
    K = top.napp
    VarMin = 1
    VarMax = tm
    tr_sel = np.array(rotas_sel, dtype=int)

    def clamp(pos):
        """Force each app's selection into its own block."""
        pos = np.asarray(pos, dtype=int).copy()
        if app_blocks is not None:
            for a in range(K):
                lo, hi = app_blocks[a + 1]
                pos[a] = int(np.clip(pos[a], lo, hi))
        return pos

    def CostFunction(rs):
        return linkc5(clamp(rs), mrotas, top, tm)

    # Initialisation
    pop = []
    BestCost_val = -np.inf
    for i in range(nPop):
        pos = rng.integers(VarMin, VarMax + 1, size=K)
        pos = clamp(pos)
        cost = CostFunction(pos)
        pop.append({"Position": pos, "Cost": cost})
        if cost > BestCost_val:
            BestCost_val = cost
            best = pop[-1]

    BestCost = np.zeros(niter)
    Tempoexec = np.zeros(niter)

    for it in range(niter):
        for i in range(nPop):
            x = pop[i]["Position"].astype(float)
            # indices a,b,c distinct from i
            pool = [p for p in range(nPop) if p != i]
            rng.shuffle(pool)
            a, b, c = pool[0], pool[1], pool[2]
            # Mutation (beta vector rounded, as in MATLAB)
            beta = rng.uniform(beta_min, beta_max, size=K)
            beta = np.round(beta)
            y = pop[a]["Position"] + beta * (pop[b]["Position"] - pop[c]["Position"])
            y = np.round(y)
            y = np.clip(y, VarMin, VarMax).astype(int)
            # Crossover (exponential-ish MATLAB style: j0 forced then rand<=pCR)
            z = np.empty(K, dtype=float)
            j0 = rng.integers(0, K)
            rnd = rng.random(K)
            for j in range(K):
                z[j] = y[j] if (j == j0 or rnd[j] <= pCR) else x[j]
            NewPos = clamp(z.astype(int))
            NewCost = CostFunction(NewPos)
            if NewCost > pop[i]["Cost"]:
                pop[i] = {"Position": NewPos, "Cost": NewCost}
                if pop[i]["Cost"] > BestCost_val:
                    best = pop[i]
                    BestCost_val = pop[i]["Cost"]
        BestCost[it] = BestCost_val
        # Tempoexec handled externally (wall-clock) in the driver
    BestSol = best
    return BestSol, pop, BestCost