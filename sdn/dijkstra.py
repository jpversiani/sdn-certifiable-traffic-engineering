"""Dijkstra shortest-path routing.

Port of the MATLAB `dijkstra.m` (Joseph Kirk, 2015) used in the thesis,
called as ``dijkstra(A, xy)`` -- edge costs are the Euclidean point-to-point
distance between node coordinates (as the thesis does for route generation).
Also provides a variant that minimises hop count / delay as used for the
comparison baselines.
"""
import numpy as np
import heapq


def edge_weights_from_coords(A, xy):
    """Return dict {(i,j): euclidean_dist} for every adjacent pair."""
    n = A.shape[0]
    w = {}
    for i in range(n):
        for j in range(i + 1, n):
            if A[i, j] > 0:
                d = float(np.hypot(xy[i, 0] - xy[j, 0], xy[i, 1] - xy[j, 1]))
                w[(i, j)] = d
                w[(j, i)] = d
    return w


def dijkstra_paths(A, xy):
    """Return (costs, paths) for all-pairs shortest paths using Euclidean
    edge weights (mirrors ``[costs, paths] = dijkstra(A, xy)``)."""
    n = A.shape[0]
    adj = {i: [] for i in range(n)}
    for (i, j), d in edge_weights_from_coords(A, xy).items():
        adj[i].append((j, d))

    costs = np.zeros((n, n))
    paths = [[None] * n for _ in range(n)]
    for s in range(n):
        dist = [float("inf")] * n
        dist[s] = 0.0
        prev = [None] * n
        heap = [(0.0, s)]
        seen = [False] * n
        while heap:
            d, u = heapq.heappop(heap)
            if seen[u]:
                continue
            seen[u] = True
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    prev[v] = u
                    heapq.heappush(heap, (nd, v))
        costs[s] = dist
        for t in range(n):
            if t == s:
                paths[s][t] = [s]
            elif dist[t] < float("inf"):
                # reconstruct path s -> t
                seq = []
                cur = t
                while cur is not None:
                    seq.append(cur)
                    cur = prev[cur]
                paths[s][t] = list(reversed(seq))
            else:
                paths[s][t] = []
    # node ids 0-based internally
    return costs, paths


def dijkstra_routes(top):
    """Return matrix of routes (like mgrafos14dijkstra) using Euclidean
    shortest paths, plus per-route delay and min-bandwidth attributes.

    Returns
    -------
    mrotas : ndarray (K, n+8)  row layout identical to the MATLAB code
             cols 0..n-1 route nodes (padded with zeros),
             col n hop count, n+1 distance, n+2 sum(nodes), n+3 prod(nodes),
             n+4 total delay (ms), n+5 min bandwidth (Mbps), n+6 app index,
             last col route id.
    """
    A, xy, tds, n = top.A, top.xy, top.tds, top.n
    _, paths = dijkstra_paths(A, xy)
    K = tds.shape[0]
    mrotas = np.zeros((K, n + 8))
    for cf in range(K):
        orig = int(tds[cf, 0]) - 1
        dest = int(tds[cf, 1]) - 1
        rota = [p + 1 for p in paths[orig][dest]]  # 1-based node ids
        tr2 = len(rota)
        mrotas[cf, :tr2] = rota
        mrotas[cf, n] = tr2                    # hop count
        mrotas[cf, n + 1] = tr2 + 1            # distance placeholder
        mrotas[cf, n + 2] = sum(rota)
        mrotas[cf, n + 3] = _prod(rota)
        delays, bws = [], []
        for i in range(tr2 - 1):
            delays.append(top.AT[rota[i] - 1, rota[i + 1] - 1])
            bws.append(top.VA[rota[i] - 1, rota[i + 1] - 1])
        mrotas[cf, n + 4] = sum(delays)        # total delay
        mrotas[cf, n + 5] = min(bws) if bws else 0.0   # min bandwidth
        mrotas[cf, n + 6] = cf + 1             # app index
    return mrotas


def _prod(seq):
    p = 1.0
    for x in seq:
        p *= x
    return p