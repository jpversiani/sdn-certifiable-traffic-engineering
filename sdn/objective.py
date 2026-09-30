"""Objective function (fitness) -- port of MATLAB ``linkc5.m``.

Given a vector ``rotas_sel`` selecting one candidate route (row index into
``mrotas``) for each application, compute the traffic-engineering fitness
``pfinal`` that the AG/DE metaheuristics maximise:

    FO = sum(priority_k * y_k)  +  3*sum(y_k)  +  2*(K - n_lb_over)
         + 1*(K - n_delay_over)

where
    y_k          = 1 if application k's route is established (all are)
    priority_k   = tds(k,5)
    n_lb_over    = # links whose aggregate demand exceeds link bandwidth
    n_delay_over = # routes whose end-to-end delay exceeds its max allowed

Node ids are 1-based (as in the MATLAB data / thesis).
"""
import numpy as np


def linkc5(rotas_sel, mrotas, top, tm):
    """rotas_sel : list/array of length K (row indices into mrotas, 1-based)."""
    rotas_sel = np.atleast_1d(np.asarray(rotas_sel, dtype=int))
    tds = top.tds
    VA = top.VA
    n = top.n
    K = tds.shape[0]

    idx = rotas_sel - 1                      # 0-based into mrotas
    sel = mrotas[idx]                        # (K, n+8)
    maxlen = int(sel[:, n].max()) + 1

    matlinks = np.zeros((K, maxlen))
    matlinks[:, :maxlen - 1] = sel[:, :maxlen - 1]

    # tags the flow demand of each app onto the last column of its row
    for ii in range(K):
        first = sel[ii, 0]
        last_node = sel[ii, int(sel[ii, n]) - 1]
        for jj in range(K):
            if (tds[jj, 0] == first) and (tds[jj, 1] == last_node):
                matlinks[ii, -1] = tds[jj, 2]
                break

    mo = sel[:, n] - 1                        # number of links per route
    nvl = int(mo.sum())

    vetlinks = np.zeros((nvl, 3))
    cl = 0
    for ii in range(K):
        n_links = int(mo[ii])
        for jj in range(n_links):
            vetlinks[cl, 0] = matlinks[ii, jj]
            vetlinks[cl, 1] = matlinks[ii, jj + 1]
            vetlinks[cl, 2] = matlinks[ii, -1]
            cl += 1

    # normalise link as (min,max)
    m1 = np.minimum(vetlinks[:, 0], vetlinks[:, 1])
    m2 = np.maximum(vetlinks[:, 0], vetlinks[:, 1])
    vetlinks[:, 0], vetlinks[:, 1] = m1, m2

    # sort by col0 then col1 (stable, like MATLAB's double sort)
    order = np.lexsort((vetlinks[:, 1], vetlinks[:, 0]))
    vetlinks2 = vetlinks[order]

    # aggregate repeated links (same pair) summing flow demand
    lines = []   # each: (u, v, total_flow, usage_count)
    for (u, v, fl) in vetlinks2:
        if lines and lines[-1][0] == u and lines[-1][1] == v:
            lv = lines[-1]
            lines[-1] = (u, v, lv[2] + fl, lv[3] + 1)
        else:
            lines.append((u, v, fl, 1))

    # check bandwidth per distinct link
    pneglargb = 0
    for (u, v, agg, _cnt) in lines:
        cap = VA[int(u) - 1, int(v) - 1]
        if cap - agg < 0:
            pneglargb += 1

    # --- vetpnt : which applications are established (all) ---
    vetpnt = np.zeros(K)
    for pnt in range(K):
        a = sel[pnt, n + 6]
        vetpnt[int(a) - 1] = 1

    # --- delay check per application route (delay stored at col n+4,
    #     MATLAB col n+5) ---
    pontnegat = 0
    for at in range(K):
        if mrotas[idx[at], n + 4] > tds[at, 3]:
            pontnegat += 1

    # --- priority contribution ---
    pontprior = vetpnt * tds[:, 4]
    sumpprior = pontprior.sum()

    pfinal = sumpprior + 3 * vetpnt.sum() + 2 * (K - pneglargb) + 1 * (K - pontnegat)
    return float(pfinal)


# convenience that only needs route indices (used by DE/GA)
def make_cost_function(mrotas, top, tm):
    def cf(rotas_sel):
        return linkc5(rotas_sel, mrotas, top, tm)
    return cf


def linkc5_debug(rotas_sel, mrotas, top, tm):
    """Same as linkc5 but returns (pfinal, details-dict) for analysis."""
    sel = mrotas[np.atleast_1d(np.asarray(rotas_sel)) - 1]
    tds = top.tds
    VA = top.VA
    n = top.n
    K = tds.shape[0]
    idx = np.atleast_1d(np.asarray(rotas_sel)) - 1
    maxlen = int(sel[:, n].max()) + 1
    matlinks = np.zeros((K, maxlen))
    matlinks[:, :maxlen - 1] = sel[:, :maxlen - 1]
    for ii in range(K):
        first = sel[ii, 0]
        last_node = sel[ii, int(sel[ii, n]) - 1]
        for jj in range(K):
            if (tds[jj, 0] == first) and (tds[jj, 1] == last_node):
                matlinks[ii, -1] = tds[jj, 2]
                break
    mo = sel[:, n] - 1
    nvl = int(mo.sum())
    vetlinks = np.zeros((nvl, 3))
    cl = 0
    for ii in range(K):
        nl = int(mo[ii])
        for jj in range(nl):
            vetlinks[cl, 0] = matlinks[ii, jj]
            vetlinks[cl, 1] = matlinks[ii, jj + 1]
            vetlinks[cl, 2] = matlinks[ii, -1]
            cl += 1
    m1 = np.minimum(vetlinks[:, 0], vetlinks[:, 1])
    m2 = np.maximum(vetlinks[:, 0], vetlinks[:, 1])
    vetlinks[:, 0], vetlinks[:, 1] = m1, m2
    order = np.lexsort((vetlinks[:, 1], vetlinks[:, 0]))
    vetlinks2 = vetlinks[order]
    lines = []
    for (u, v, fl) in vetlinks2:
        if lines and lines[-1][0] == u and lines[-1][1] == v:
            lv = lines[-1]
            lines[-1] = (u, v, lv[2] + fl, lv[3] + 1)
        else:
            lines.append((u, v, fl, 1))
    pneglargb = 0
    over_list = []
    for (u, v, agg, _c) in lines:
        cap = VA[int(u) - 1, int(v) - 1]
        if cap - agg < 0:
            pneglargb += 1
            over_list.append((int(u), int(v), round(float(agg), 3),
                              round(float(cap), 2)))
    return pneglargb, over_list, int(nvl), lines