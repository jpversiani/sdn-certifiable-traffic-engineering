"""Revised evaluation model (FOv2) and metrics.

Addresses the reviewer-identified weaknesses of the original scoring function:
  (1) capacity and delay become HARD constraints (feasibility is a gate, not a
      soft penalty mixed with an inconsistent link/app count);
  (2) load balancing enters as an explicit min-max utilization objective;
  (3) the original thesis FO (linkc5) is reproduced here for continuity from
      a routes dict, so all algorithms are scored on both models.
"""
import numpy as np


def fo_original_from_routes(top, routes):
    """Faithful recomputation of the thesis objective (linkc5) from a
    routes dict {app(1-based): [nodes(1-based)]}.

    FO = sum(delta_k) + 3*K + 2*(K - n_overloaded_links) + (K - n_delay_viol)
    (all connections established -> every y_k = 1)."""
    tds = top.tds
    K = tds.shape[0]
    overloaded = _overloaded_links(top, routes)
    n_over = len(overloaded)
    n_delayviol = len(_delay_violations(top, routes))
    return float(tds[:, 4].sum() + 3 * K + 2 * (K - n_over) + (K - n_delayviol))


def link_aggregate(top, routes, load_factor=1.0):
    """Aggregate offered load per undirected link {(u,v): sum of flows}."""
    tds = top.tds
    agg = {}
    for k in range(1, tds.shape[0] + 1):
        rota = routes[k]
        lam = tds[k - 1, 2] * load_factor
        for u, v in zip(rota, rota[1:]):
            key = (min(u, v), max(u, v))
            agg[key] = agg.get(key, 0.0) + lam
    return agg


def _overloaded_links(top, routes, load_factor=1.0):
    agg = link_aggregate(top, routes, load_factor)
    over = []
    for (u, v), load in agg.items():
        cap = top.VA[u - 1, v - 1]
        if load > cap + 1e-9:
            over.append((u, v, load, cap))
    return over


def _delay_violations(top, routes, load_factor=1.0):
    tds = top.tds
    viol = []
    for k in range(1, tds.shape[0] + 1):
        rota = routes[k]
        delay = sum(top.AT[u - 1, v - 1] for u, v in zip(rota, rota[1:]))
        if delay > tds[k - 1, 3] + 1e-9:
            viol.append((k, delay, tds[k - 1, 3]))
    return viol


def route_delay(top, rota):
    return sum(top.AT[u - 1, v - 1] for u, v in zip(rota, rota[1:]))


def evaluate_routes(top, routes, load_factor=1.0):
    """Full revised-model evaluation of a routing solution.

    Returns dict with:
      fo_original        : thesis scoring function (continuity metric)
      feasible           : bool -- hard capacity AND delay constraints all met
      max_util           : maximum per-link utilization (load/capacity)
      overloaded_links   : count of links with aggregate > capacity
      delay_violations   : count of flows whose route delay exceeds h_k
      mean_delay_ms      : mean route delay over all flows
      mean_util          : mean per-link utilization over used links
      used_links         : number of distinct links carrying traffic
      solve_quality      : 'feasible' | 'capacity_violation' | 'delay_violation'
    """
    agg = link_aggregate(top, routes, load_factor)
    utils = []
    overloaded = 0
    for (u, v), load in agg.items():
        cap = top.VA[u - 1, v - 1]
        utils.append(load / cap)
        if load > cap + 1e-9:
            overloaded += 1
    max_util = max(utils) if utils else 0.0
    mean_util = float(np.mean(utils)) if utils else 0.0

    viol = _delay_violations(top, routes, load_factor)
    delays = [route_delay(top, routes[k]) for k in sorted(routes)]

    feasible = (overloaded == 0) and (len(viol) == 0)
    if overloaded > 0:
        quality = "capacity_violation"
    elif len(viol) > 0:
        quality = "delay_violation"
    else:
        quality = "feasible"

    return {
        "fo_original": fo_original_from_routes(top, routes),
        "feasible": feasible,
        "max_util": float(max_util),
        "mean_util": mean_util,
        "overloaded_links": overloaded,
        "delay_violations": len(viol),
        "mean_delay_ms": float(np.mean(delays)) if delays else 0.0,
        "used_links": len(agg),
        "quality": quality,
    }