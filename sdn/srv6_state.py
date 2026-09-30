"""Data-plane state accounting: OpenFlow per-flow rules vs SRv6.

Measures, for a given routing solution, the per-node rule footprint under
both programming paradigms plus the SRH encapsulation overhead, making the
state-reduction claim of the SRv6 section an empirical result on each
topology instead of an asymptotic assertion.
"""
import numpy as np


def state_counts(top, routes):
    """Return dict with OpenFlow and SRv6 state metrics for ``routes``.

    OpenFlow model: every flow needs a match-action rule at every transit
    node (each node on the path except the ingress), matching the flow's
    5-tuple and rewriting/forwarding to the next hop.

    SRv6 model: exactly one rule per flow at its headend (encapsulation with
    the segment list); transit nodes execute the flow-agnostic End function
    and hold no per-flow state.
    """
    tds = top.tds
    K = tds.shape[0]
    of_rules = {v: 0 for v in range(1, top.n + 1)}
    headend_rules = {v: 0 for v in range(1, top.n + 1)}
    seg_lens = []
    srh_bytes = []

    for k in range(1, K + 1):
        rota = routes[k]
        for v in rota[1:-1]:          # transit nodes (excluding headend)
            of_rules[v] += 1
        headend_rules[rota[0]] += 1
        m = len(rota)
        seg_lens.append(m - 1)        # SIDs for downstream nodes
        # SRH overhead: outer IPv6 (40 B) + SRH fixed (8 B) + 16 B per SID
        srh_bytes.append(40 + 8 + 16 * (m - 1))

    of_total = sum(of_rules.values())
    of_max_node = max(of_rules.values())
    sr_total = sum(headend_rules.values())

    return {
        "of_total_rules": of_total,
        "of_max_node_rules": of_max_node,
        "of_mean_node_rules": float(np.mean(list(of_rules.values()))),
        "srv6_total_rules": sr_total,
        "srv6_max_node_rules": max(headend_rules.values()),
        "srv6_transit_rules": 0,
        "max_segment_list": max(seg_lens) if seg_lens else 0,
        "mean_segment_list": float(np.mean(seg_lens)) if seg_lens else 0.0,
        "max_srh_overhead_bytes": max(srh_bytes) if srh_bytes else 0,
        "mean_srh_overhead_bytes": float(np.mean(srh_bytes)) if srh_bytes else 0.0,
        "reduction_factor": of_total / sr_total if sr_total else float("inf"),
    }