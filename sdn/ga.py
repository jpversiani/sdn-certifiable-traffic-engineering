"""Genetic Algorithm (GA) route selector.

Port of the MATLAB ``agaco811.m`` with its helpers (RouletteWheelSelection,
Crossover2, Mutate2).  Maximises the objective function (linkc5) over
integer vectors of route indices (one per application).
"""
import numpy as np

from .objective import linkc5


def roulette_selection(P, rng):
    r = rng.random()
    c = np.cumsum(P)
    idx = np.flatnonzero(r <= c)
    return int(idx[0]) if idx.size else int(P.size - 1)


def crossover2(x1, x2, gamma, VarMin, VarMax, rng):
    alpha = rng.uniform(-gamma, 1 + gamma, size=np.asarray(x1).shape)
    y1 = alpha * np.asarray(x1, float) + (1 - alpha) * np.asarray(x2, float)
    y2 = alpha * np.asarray(x2, float) + (1 - alpha) * np.asarray(x1, float)
    return (np.clip(np.round(y1), VarMin, VarMax).astype(int),
            np.clip(np.round(y2), VarMin, VarMax).astype(int))


def mutate2(x, mu, VarMin, VarMax, rng):
    nVar = np.asarray(x).size
    j = rng.integers(0, nVar)              # MATLAB randsample(nVar,1)
    sigma = 0.1 * (VarMax - VarMin)
    y = np.asarray(x, float).copy()
    y[j] = x[j] + sigma * rng.standard_normal()
    return np.clip(np.round(y), VarMin, VarMax).astype(int)


def ga_aco(top, mrotas, tm, rotas_sel, niter=200, nPop=50, pc=0.8, pm=0.3,
           beta=8.0, gamma=0.4, metodo_sorteio=1, seed=None, app_blocks=None):
    """Returns (BestSol, pop, BestCost) mirroring agaco811.

    ``app_blocks`` maps each application index (1..K) to the [lo,hi] range of
    valid rows in ``mrotas`` for that application (intended semantics: pick
    one candidate route per application).
    """
    rng = np.random.default_rng(seed)
    if seed is not None:
        np.random.seed(seed)
    K = top.napp
    VarMin = 1
    VarMax = tm
    tr_sel = np.array(rotas_sel, dtype=int)

    def clamp(pos):
        pos = np.asarray(pos, dtype=int).copy()
        if app_blocks is not None:
            for a in range(K):
                lo, hi = app_blocks[a + 1]
                pos[a] = int(np.clip(pos[a], lo, hi))
        return pos

    def CostFunction(rs):
        return linkc5(clamp(rs), mrotas, top, tm)

    nc = 2 * round(pc * nPop / 2)
    nm = round(pm * nPop)

    # Initialisation
    pop = []
    for i in range(nPop):
        pos = rng.integers(VarMin, VarMax + 1, size=K)
        pos = clamp(pos)
        pop.append({"Position": pos, "Cost": CostFunction(pos)})
    Costs = np.array([p["Cost"] for p in pop])
    order = np.argsort(Costs)[::-1]        # descending (maximise)
    pop = [pop[i] for i in order]
    BestSol = pop[0]
    WorstCost = pop[-1]["Cost"]
    BestCost = np.zeros(niter)

    for it in range(niter):
        Costs = np.array([p["Cost"] for p in pop])
        # selection probabilities (roleta)
        if metodo_sorteio == 1:
            P = np.exp(-beta * Costs / WorstCost)
            P = P / P.sum()
        # Crossover
        popc = []
        for k in range(nc // 2):
            i1 = roulette_selection(P, rng)
            i2 = roulette_selection(P, rng)
            p1, p2 = pop[i1]["Position"], pop[i2]["Position"]
            c1, c2 = crossover2(p1, p2, gamma, VarMin, VarMax, rng)
            popc.append({"Position": clamp(c1), "Cost": CostFunction(c1)})
            popc.append({"Position": clamp(c2), "Cost": CostFunction(c2)})
        # Mutation
        popm = []
        for k in range(nm):
            i = rng.integers(0, nPop)
            p = pop[i]["Position"]
            m = mutate2(p, 0.1, VarMin, VarMax, rng)
            popm.append({"Position": clamp(m), "Cost": CostFunction(m)})
        # Merge, sort desc, truncate
        merged = pop + popc + popm
        Costs = np.array([p["Cost"] for p in merged])
        order = np.argsort(Costs)[::-1]
        merged = [merged[i] for i in order]
        WorstCost = max(WorstCost, merged[-1]["Cost"])
        pop = merged[:nPop]
        BestSol = pop[0]
        BestCost[it] = BestSol["Cost"]
    return BestSol, pop, BestCost