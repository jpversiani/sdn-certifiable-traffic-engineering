"""Exact optimization baselines via MILP (HiGHS through PuLP).

ILP-P  : path-selection formulation over the ACO candidate pool. It computes
         the *exact optimum of the thesis objective function* restricted to
         the same search space explored by the GA/DE, thereby certifying the
         optimality gap of the metaheuristics.

ILP-L  : link-based multi-commodity flow formulation of the REVISED model
         (hard capacity + hard delay constraints, min-max utilization
         objective). It provides the true reference optimum of the revised
         model and, crucially, *certifies infeasibility* at high loads where
         greedy methods still return constraint-violating routes.
"""
import numpy as np
import pulp

from .metrics import fo_original_from_routes, link_aggregate, route_delay


def _solve(problem, time_limit=120.0, msg=False):
    solver = pulp.getSolver("HiGHS", msg=msg,
                            timeLimit=time_limit) if _supports_time() else \
             pulp.getSolver("HiGHS", msg=msg)
    return problem.solve(solver)


def _supports_time():
    return True  # HiGHS wrapper in PuLP 4 accepts timeLimit


def _status(stats):
    s = getattr(stats, "status_str", None)
    return str(s) if s else str(stats.status)


# ---------------------------------------------------------------------------
# ILP-P: exact selection over the candidate pool (original thesis FO)
# ---------------------------------------------------------------------------
def ilp_pool(top, mrotas, tm, app_blocks, load_factor=1.0, time_limit=60.0):
    """Exact max of the thesis FO over the candidate pool.

    Returns dict(status, fo, selection(list of 1-based rows), time).
    """
    n = top.n
    K = top.napp
    tds = top.tds
    mu = top.VA
    c = top.AT

    prob = pulp.LpProblem("ilp_pool", pulp.LpMaximize)

    # x[r] = 1 if route r is selected (r: 1-based row into mrotas)
    routes_of_app = {k: list(range(app_blocks[k][0], app_blocks[k][1] + 1))
                     for k in range(1, K + 1)}
    x = {}
    for k, rows in routes_of_app.items():
        for r in rows:
            x[r] = prob.add_variable(f"x_{r}", lowBound=0, upBound=1,
                                     cat="Binary")

    # each application selects exactly one candidate route
    for k, rows in routes_of_app.items():
        prob.addConstraint(pulp.lpSum(x[r] for r in rows) == 1,
                           name=f"pick_{k}")

    # precompute per-route data
    def route_nodes(r):
        row = mrotas[r - 1]
        m = int(row[n])
        return [int(v) for v in row[:m]]

    route_links = {r: [(min(u, v), max(u, v))
                       for u, v in zip(route_nodes(r), route_nodes(r)[1:])]
                   for r in x}
    route_delay_ = {r: route_delay(top, route_nodes(r)) for r in x}

    # --- FO structure (all connections established) ---
    # FO = sum(delta_k) + 3K + 2(K - n_over) + (K - n_delayviol)
    #     = const - 2*sum(u_l) - sum(v_k), maximize == minimize penalties
    const = tds[:, 4].sum() + 3 * K + 2 * K + K
    u = {}   # 1 if link l overloaded under selection
    links = sorted({l for r in x for l in route_links[r]})
    for li, l in enumerate(links):
        u[l] = prob.add_variable(f"u_{li}", lowBound=0, upBound=1,
                                 cat="Binary")
    v = {}   # 1 if flow k violates its delay budget
    for k in range(1, K + 1):
        v[k] = prob.add_variable(f"v_{k}", lowBound=0, upBound=1, cat="Binary")

    # capacity coupling: sum_k lam_k * a_{l,k} <= mu_l + M * u_l
    Mbig = float(tds[:, 2].sum()) * 2.0 + 1.0
    for l in links:
        expr = pulp.lpSum(
            tds[k - 1, 2] * load_factor * x[r]
            for k, rows in routes_of_app.items() for r in rows
            if l in route_links[r])
        cap = float(mu[l[0] - 1, l[1] - 1])
        prob.addConstraint(expr <= cap + Mbig * u[l], name=f"cap_{l}")

    # delay coupling: sum_c a_{k,c} <= h_k + M2 * v_k
    M2 = float(np.max(c)) * (n + 1) + 1.0
    for k in range(1, K + 1):
        expr = pulp.lpSum(route_delay_[r] * x[r] for r in routes_of_app[k])
        prob.addConstraint(expr <= tds[k - 1, 3] + M2 * v[k],
                           name=f"del_{k}")

    prob.objective = const - 2 * pulp.lpSum(u.values()) \
                     - pulp.lpSum(v.values())

    stats = _solve(prob, time_limit)
    status = _status(stats)
    if status != "Optimal":
        return {"status": status, "fo": None, "selection": None,
                "time": stats.time}
    sel = sorted((r for r, var in x.items() if var.value() > 0.5))
    return {"status": "Optimal", "fo": pulp.value(prob.objective),
            "selection": sel, "time": stats.time}


# ---------------------------------------------------------------------------
# ILP-L: link-based MCF, revised model (hard constraints, min-max util)
# ---------------------------------------------------------------------------
def ilp_link_mcf(top, load_factor=1.0, time_limit=300.0, eps=1e-3, msg=False):
    """Exact solution of the revised model (lexicographic two-phase).

    Phase 1: minimize the bottleneck utilization Z alone. This is the value
    certified as the exact min--max lower bound of the instance.
    Phase 2: fix Z <= Z1 + tol and minimize the total route delay as a
    deterministic tie-break, returning the routes of the lexicographic
    optimum. (The historical eps-weighted single objective is NOT used:
    a weighted sum does not certify the minimum of Z.)

    Returns dict(status, Z (phase-1 certified value), Z_final, routes
    {app: nodes}, time, phase1_status).
    """
    n = top.n
    K = top.napp
    tds = top.tds
    mu = top.VA
    c = top.AT
    A = top.A

    # directed link list
    dlinks = [(i + 1, j + 1) for i in range(n) for j in range(n)
              if A[i, j] > 0]

    prob = pulp.LpProblem("ilp_mcf", pulp.LpMinimize)
    x = {}
    for k in range(1, K + 1):
        for (i, j) in dlinks:
            x[(k, i, j)] = prob.add_variable(f"x_{k}_{i}_{j}",
                                             lowBound=0, upBound=1,
                                             cat="Binary")
    Z = prob.add_variable("Z", lowBound=0)

    # flow conservation
    for k in range(1, K + 1):
        src, dst = int(tds[k - 1, 0]), int(tds[k - 1, 1])
        for i in range(1, n + 1):
            inflow = pulp.lpSum(x[(k, j, i)] for (j, ii) in dlinks
                                if ii == i)
            outflow = pulp.lpSum(x[(k, i, j)] for (ii, j) in dlinks
                                 if ii == i)
            if i == src:
                prob.addConstraint(outflow - inflow == 1,
                                   name=f"src_{k}_{i}")
            elif i == dst:
                prob.addConstraint(inflow - outflow == 1,
                                   name=f"dst_{k}_{i}")
            else:
                prob.addConstraint(inflow - outflow == 0,
                                   name=f"con_{k}_{i}")

    # hard capacity (shared per undirected pair, both directions) +
    # max-utilization definition
    und = {}
    for (i, j) in dlinks:
        key = (min(i, j), max(i, j))
        und.setdefault(key, []).append((i, j))
    for (u, v), dirs in und.items():
        cap = float(mu[u - 1, v - 1])
        expr = pulp.lpSum(tds[k - 1, 2] * load_factor * x[(k, i, j)]
                          for k in range(1, K + 1) for (i, j) in dirs)
        prob.addConstraint(expr <= cap, name=f"cap_{u}_{v}")
        prob.addConstraint(expr - cap * Z <= 0, name=f"util_{u}_{v}")

    # hard delay per commodity
    for k in range(1, K + 1):
        expr = pulp.lpSum(c[i - 1, j - 1] * x[(k, i, j)] for (i, j) in dlinks)
        prob.addConstraint(expr <= tds[k - 1, 3], name=f"del_{k}")

    total_delay = pulp.lpSum(c[i - 1, j - 1] * x[(k, i, j)]
                             for k in range(1, K + 1) for (i, j) in dlinks)

    import time as _time
    t0 = _time.perf_counter()
    # ---- phase 1: certify the minimum bottleneck utilization ----
    prob.objective = Z
    stats = _solve(prob, time_limit, msg=msg)
    status1 = _status(stats)
    out = {"status": status1, "Z": None, "Z_final": None, "routes": None,
           "time": 0.0, "phase1_status": status1}
    if status1 != "Optimal":
        out["time"] = _time.perf_counter() - t0
        return out
    Z1 = float(pulp.value(Z))
    out["Z"] = Z1

    # ---- phase 2: delay tie-break with Z pinned to the certified optimum ----
    tol = max(1e-6, 1e-6 * abs(Z1))
    prob.addConstraint(Z <= Z1 + tol, name="Z_lexicographic_pin")
    prob.objective = total_delay
    stats = _solve(prob, max(30.0, time_limit * 0.5), msg=msg)
    status2 = _status(stats)
    out["status"] = status2 if status2 == "Optimal" else status1
    out["time"] = _time.perf_counter() - t0
    if status2 != "Optimal":
        out["Z_final"] = Z1
        return out
    out["Z_final"] = float(pulp.value(Z))
    routes = {}
    for k in range(1, K + 1):
        src = int(tds[k - 1, 0])
        # walk along chosen arcs from src
        succ = {}
        for (i, j) in dlinks:
            if x[(k, i, j)].value() and x[(k, i, j)].value() > 0.5:
                succ.setdefault(i, []).append(j)
        path = [src]
        cur = src
        guard = 0
        while cur != int(tds[k - 1, 1]) and guard < n + 2:
            nxt = succ.get(cur, [])
            if not nxt:
                break
            cur = nxt[0]
            path.append(cur)
            guard += 1
        routes[k] = path
    out["routes"] = routes
    return out