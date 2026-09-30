"""Ant Colony Optimisation (AntNet) route generator.

Port of the MATLAB ``mgrafos14g.m`` from the thesis.  For every application
in ``tds`` a colony of ``nAnt`` ants builds source->destination paths driven
by a pheromone matrix ``tau`` and a heuristic ``eta``; loops are removed and
the collected routes (with per-route delay and min bandwidth) are returned.

Route-row layout (identical to the MATLAB code; Python 0-based indices,
n = number of nodes = 52):
    cols 0..n-1  : node ids (1-based), padded with 0
    col n        : hop count (route length)
    col n+1      : "distancia" (MATLAB n+2)
    col n+2      : sum of node ids along route
    col n+3      : product of node ids along route
    col n+4      : (MATLAB n+5) total one-way delay of the route (ms)
    col n+5      : (MATLAB n+6) min link bandwidth along the route (Mbps)
    col n+6      : (MATLAB n+7) application index (cf, 1-based)
    col n+7      : route id (assigned at the end)
"""
import numpy as np

from .dijkstra import dijkstra_paths


def roulette_wheel(P):
    """MATLAB Roleta(P): return first index where random r <= cumsum(P)."""
    r = np.random.rand()
    c = P.cumsum()
    idx = np.flatnonzero(r <= c)
    return int(idx[0]) if idx.size else int(P.size - 1)


def _remove_loops(rota):
    """MATLAB 'RetirarLoops': collapse repeated nodes to a simple path."""
    i = 0
    out = []
    n = len(rota)
    while i < n:
        node = rota[i]
        out.append(node)
        # find last occurrence of this node
        last = n - 1 - rota[::-1].index(node)
        i = last + 1
    return out


def _trim(rota, dest):
    # keep only until dest is first reached (paths loop until dest)
    idx = rota.index(dest) + 1
    return rota[:idx]


def _prod(seq):
    p = 1.0
    for x in seq:
        p *= x
    return p


def func_distancia(rota, D):
    """Sum of link costs along rota (uses the D=adjacency matrix)."""
    total = 0.0
    for i in range(len(rota) - 1):
        total += D[rota[i] - 1, rota[i + 1] - 1]
    return total


def aco_generate_routes(top, nAnt=50, MaxIt=200, beta=1.0, alpha=1.0,
                        rho=0.05, seed=None, progress=False):
    """Port of ``mgrafos14g``.

    Returns (mrotas, n, tm) where mrotas has shape (K, n+8) and each row is a
    candidate route for the corresponding application.  nAnt distinct-ish
    routes are kept per application (the MATLAB code picks distinct routes via
    the sort/unique mechanism; we return the distinct set).
    """
    if seed is not None:
        np.random.seed(seed)
    n = top.n
    tds = top.tds
    napp = tds.shape[0]
    mrotas = []

    for cf in range(napp):
        orig = int(tds[cf, 0]) - 1          # 0-based
        dest = int(tds[cf, 1]) - 1          # 0-based

        Q = 1.0
        Q1 = 0.5 / 32.0
        # tau0 = 10*Q/(n*mean(D))
        D = top.D
        tau0 = 10.0 * Q / (n * (D.mean() if D.mean() > 0 else 1.0))
        tau = tau0 * top.A.copy()

        eta = np.where(D > 0, 1.0 / np.where(D > 0, D, 1.0), 0.0)
        eta = np.nan_to_num(eta)
        eta[np.isinf(eta)] = 0.0

        best_distance = float("inf")

        for _it in range(MaxIt):
            vet_rotas = []            # routes built by this iteration's ants
            for _j in range(nAnt):
                atual = orig
                rota = [orig + 1]            # route kept 1-based
                # forward walk until destination reached
                guard = 0
                while atual != dest and guard < 200 * n:
                    P = (np.power(tau[atual, :], alpha) *
                         np.power(eta[atual, :], beta))
                    s = P.sum()
                    if s <= 0:
                        break
                    P = P / s
                    ds = roulette_wheel(P)   # 0-based next node
                    atual = ds
                    rota.append(atual + 1)   # store 1-based
                    guard += 1
                # if destination never reached, skip this ant's walk
                if atual != dest:
                    continue
                rota = _remove_loops(rota)
                rota = _trim(rota, dest + 1)  # trim to first dest (1-based)
                if not rota or rota[-1] != dest + 1:
                    continue
                distancia = func_distancia(rota, D)
                if distancia < best_distance:
                    best_distance = distancia
                tr2 = len(rota)

                # vetvazao / vetatraso along the route
                vv, vat = [], []
                for i in range(tr2 - 1):
                    vv.append(top.VA[rota[i] - 1, rota[i + 1] - 1])
                    vat.append(top.AT[rota[i] - 1, rota[i + 1] - 1])
                row = np.zeros(n + 8)
                row[:tr2] = rota
                row[n] = tr2                      # hop count
                row[n + 1] = distancia            # distance
                row[n + 2] = float(sum(rota))     # sum of node ids
                row[n + 3] = float(_prod(rota))   # product of node ids
                row[n + 4] = float(sum(vat))      # total delay (MATLAB n+5)
                row[n + 5] = float(min(vv)) if vv else 0.0   # min bw (n+6)
                row[n + 6] = cf + 1               # app index (MATLAB n+7)
                vet_rotas.append(row)

                # backward walk: pheromone deposit proportional to bandwidth
                for m in range(tr2 - 1):
                    i = rota[m]
                    j = rota[m + 1]
                    tau[i - 1, j - 1] += (10.0 * Q1 * tds[cf, 2] *
                                          (min(vv) if vv else 0.0))

            # evaporation
            tau = (1.0 - rho) * tau

        # --- select the distinct routes (MATLAB sort/unique block) ---
        if not vet_rotas:
            raise RuntimeError(f"ACO produced no valid route for app {cf+1}")
        arr = np.array(vet_rotas)                 # (nAnt, n+8)
        # unique by (sum_nodes, prod_nodes) exactly as the MATLAB code,
        # which sorts columns (n+3,n+4) 1-based == Python cols (n+2,n+3)
        key = arr[:, [n + 2, n + 3]]
        order = np.lexsort((key[:, 1], key[:, 0]))
        sorted_rows = arr[order]
        distinct = []
        prev = None
        for r in sorted_rows:
            k = (r[n + 2], r[n + 3])
            if prev is None or k != prev:
                distinct.append(r)
            prev = k
        # sort the distinct routes by delay (col n+4, MATLAB col n+5),
        # as the MATLAB code does via sort(VetRSel(:,n+2)) placeholder;
        # we keep the delay-minimising order.
        distinct.sort(key=lambda r: r[n + 4])
        mrotas.append(distinct)

    # flatten: block per application but keep app grouping via col n+6
    rows = [r for app in mrotas for r in app]
    mrotas_matrix = np.array(rows)
    tm = mrotas_matrix.shape[0]
    # append route id as last column
    ids = np.arange(1, tm + 1, dtype=np.float64).reshape(-1, 1)
    mrotas_matrix = np.hstack([mrotas_matrix, ids])
    return mrotas_matrix, n, tm