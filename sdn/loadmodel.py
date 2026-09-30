"""Load-growth model: aggregate contention instead of per-flow overshoot.

Scaling every flow by a factor f > 1 makes the largest flow exceed the
maximum link capacity (1.744 * 1.25 = 2.18 > 2 Mbps), which certifies
infeasibility trivially and tells nothing about network contention. Real
network growth adds concurrent sessions. This module therefore models load
as follows:
    f <= 1   : existing flows scaled down (0.5x, 0.75x, 1.0x);
    f >  1   : the 17 nominal flows are kept at nominal rate and
               round((f-1)*20) extra background data flows (0.256 Mbps,
               h=1000 ms, priority 0) are added on random connected
               endpoint pairs -- aggregate contention, no oversized flows.
"""
import numpy as np
import networkx as nx

from .data import Topology


def loaded_topology(top, f, seed=77):
    """Return a Topology carrying the demand model for load factor f."""
    if f <= 1.0:
        return top.with_load(f)

    rng = np.random.default_rng(seed + int(f * 100))
    n_extra = int(round((f - 1.0) * 20))
    G = nx.from_numpy_array(top.A, create_using=nx.Graph)
    G = nx.relabel_nodes(G, {i: i + 1 for i in range(top.n)})  # 1-based ids
    rows = top.tds.tolist()
    used = {(int(r[0]), int(r[1])) for r in rows}
    nodes = list(range(1, top.n + 1))
    added = 0
    while added < n_extra:
        s, d = rng.choice(nodes, size=2, replace=False)
        s, d = int(s), int(d)
        if (s, d) in used or not nx.has_path(G, s, d):
            continue
        used.add((s, d))
        rows.append([float(s), float(d), 0.256, 1000.0, 0.0])
        added += 1
    t2 = np.array(rows, dtype=np.float64)
    obj = Topology.from_arrays(top.name, top.A, top.AT, top.VA, top.xy, t2)
    return obj


def k_shortest_pool(top_loaded, app_index, max_paths=20):
    """Candidate routes for an extra flow: k-shortest simple paths by delay.

    Returns rows in the same layout as the ACO pool (n+8 columns, 1-based
    node ids, hop count at col n, delay at n+4, min bw at n+5, app index at
    n+6)."""
    n = top_loaded.n
    k0 = app_index                       # 1-based app index
    src = int(top_loaded.tds[k0 - 1, 0])
    dst = int(top_loaded.tds[k0 - 1, 1])
    G = nx.Graph()
    for i in range(n):
        for j in range(n):
            if top_loaded.A[i, j] > 0:
                G.add_edge(i + 1, j + 1,
                           weight=float(top_loaded.AT[i, j]))
    rows = []
    try:
        gen = nx.shortest_simple_paths(G, src, dst, weight="weight")
        for i, path in enumerate(gen):
            if i >= max_paths:
                break
            path = [int(v) for v in path]
            tr = len(path)
            delay = sum(top_loaded.AT[p - 1, q - 1]
                        for p, q in zip(path, path[1:]))
            bw = min(top_loaded.VA[p - 1, q - 1]
                     for p, q in zip(path, path[1:]))
            row = np.zeros(n + 8)
            row[:tr] = path
            row[n] = tr
            row[n + 1] = delay
            row[n + 2] = float(sum(path))
            row[n + 3] = float(np.prod(path))
            row[n + 4] = delay
            row[n + 5] = bw
            row[n + 6] = k0
            rows.append(row)
    except (nx.NetworkXNoPath, nx.NodeNotFound):
        pass
    return rows


def augment_pool_with_cspf(mrotas, top_loaded, routes_cspf):
    """Augment each application's candidate block with its CSPF route.

    Standard hybridization practice: seeding the selection stage with the
    constructive baseline guarantees the selector's result is never worse
    than CSPF (the CSPF assembly is inside the search space), and strictly
    better whenever the pool holds a better combination.  Rows are inserted
    right after each application's contiguous block, preserving the block
    structure required by build_app_blocks.
    """
    from .run_optimization import build_app_blocks

    n = top_loaded.n
    K = top_loaded.napp
    ncol = mrotas.shape[1]
    blocks = build_app_blocks(mrotas, top_loaded)
    new_rows = []
    for k in range(1, K + 1):
        lo, hi = blocks[k]
        new_rows.extend(mrotas[lo - 1:hi])
        path = routes_cspf.get(k)
        if path is None or len(path) < 2:
            continue
        tr = len(path)
        delay = sum(top_loaded.AT[p - 1, q - 1] for p, q in zip(path, path[1:]))
        bw = min(top_loaded.VA[p - 1, q - 1] for p, q in zip(path, path[1:]))
        row = np.zeros(ncol)
        row[:tr] = path
        row[n] = tr
        row[n + 1] = delay
        row[n + 2] = float(sum(path))
        row[n + 3] = float(np.prod(path))
        row[n + 4] = delay
        row[n + 5] = bw
        row[n + 6] = float(k)
        new_rows.append(row)
    pool = np.array(new_rows)
    ids = np.arange(1, pool.shape[0] + 1, dtype=np.float64).reshape(-1, 1)
    return np.hstack([pool[:, :-1], ids])


def extend_pool(mrotas, top_nominal, top_loaded, max_paths=20):
    """Extend an ACO pool with k-shortest candidate routes for the extra
    flows of the loaded demand model.  Returns the extended pool matrix."""
    if top_loaded.napp <= top_nominal.napp:
        return mrotas
    extra = []
    for k0 in range(top_nominal.napp + 1, top_loaded.napp + 1):
        extra.extend(k_shortest_pool(top_loaded, k0, max_paths))
    if not extra:
        return mrotas
    ncol = mrotas.shape[1]
    fixed = []
    for r in extra:
        row = np.zeros(ncol)
        row[:len(r)] = r
        fixed.append(row)
    em = np.array(fixed)
    # ids for extended rows
    ids = np.arange(mrotas.shape[0] + 1,
                    mrotas.shape[0] + 1 + em.shape[0],
                    dtype=np.float64).reshape(-1, 1)
    em = np.hstack([em[:, :-1], ids])
    return np.vstack([mrotas, em])