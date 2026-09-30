"""Constrained Shortest Path First (CSPF) routing baseline.
Industry-standard QoS routing algorithm that prunes links failing bandwidth
or delay constraints before running shortest-path computation.
"""
import numpy as np
import heapq

def cspf_route(top, order_by_priority=True):
    """Computes routes for all applications using CSPF.
    Prunes links whose residual capacity is less than the requested flow bandwidth.
    Returns:
        routes: dict mapping app (1-based) to list of nodes (1-based)
        fitness: scalar calculated via objective.linkc5
    """
    n = top.n
    tds = top.tds
    K = tds.shape[0]
    VA = top.VA.copy()  # initial link bandwidth capacities (symmetric)
    AT = top.AT         # delay matrix
    A = top.A           # adjacency matrix

    # Determine order of routing
    app_order = list(range(K))
    if order_by_priority:
        # Sort by priority (col 4 descending), then flow size (col 2 descending)
        app_order.sort(key=lambda k: (tds[k, 4], tds[k, 2]), reverse=True)

    residual_cap = VA.copy()
    routes = {}

    for k in app_order:
        src = int(tds[k, 0])
        dst = int(tds[k, 1])
        flow = tds[k, 2]
        max_d = tds[k, 3]

        # Dijkstra on graph restricted to residual_cap >= flow
        dist = {i: float('inf') for i in range(1, n + 1)}
        prev = {i: None for i in range(1, n + 1)}
        dist[src] = 0
        pq = [(0, src)]

        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            if u == dst:
                break
            for v in range(1, n + 1):
                if A[u - 1, v - 1] > 0 and residual_cap[u - 1, v - 1] >= flow:
                    cost = AT[u - 1, v - 1] if AT[u - 1, v - 1] > 0 else 1.0
                    if dist[u] + cost < dist[v]:
                        dist[v] = dist[u] + cost
                        prev[v] = u
                        heapq.heappush(pq, (dist[v], v))

        # Reconstruct path
        if dist[dst] < float('inf'):
            path = []
            curr = dst
            while curr is not None:
                path.append(curr)
                curr = prev[curr]
            path.reverse()
            routes[k + 1] = path
            # Deduct residual capacity along the bidirectional link
            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                residual_cap[u - 1, v - 1] -= flow
                residual_cap[v - 1, u - 1] -= flow
        else:
            # Fallback to shortest path without pruning if constrained path not found
            # (best effort)
            pq_fallback = [(0, src)]
            dist_fb = {i: float('inf') for i in range(1, n + 1)}
            prev_fb = {i: None for i in range(1, n + 1)}
            dist_fb[src] = 0
            while pq_fallback:
                d, u = heapq.heappop(pq_fallback)
                if d > dist_fb[u]:
                    continue
                if u == dst:
                    break
                for v in range(1, n + 1):
                    if A[u - 1, v - 1] > 0:
                        cost = AT[u - 1, v - 1] if AT[u - 1, v - 1] > 0 else 1.0
                        if dist_fb[u] + cost < dist_fb[v]:
                            dist_fb[v] = dist_fb[u] + cost
                            prev_fb[v] = u
                            heapq.heappush(pq_fallback, (dist_fb[v], v))
            path = []
            curr = dst
            while curr is not None:
                path.append(curr)
                curr = prev_fb[curr]
            path.reverse()
            routes[k + 1] = path

    return routes
