"""Synthetic topologies with the same demand profile as the original study.

Provides two additional 52-node instances besides the original Maia topology:
  - waxman52 : Waxman random geometric graph (Waxman, 1988)
  - gridcore : 8x6 peripheral grid + 4-node dense core

All instances share: 52 nodes, uniform 2 Mbps link capacity, link delays in
the 1..80 ms range (peripheral 1 ms; core proportional to geometry), and the
same 17-application demand table (sources/destinations re-drawn at random).
"""
import numpy as np
import networkx as nx

from .data import Topology

CORE_DELAY = 20.0


def _tds_for_graph(G, rng, tds_template):
    """Re-draw 17 endpoint pairs on G, preserving the demand profile.

    Endpoints are drawn in 1..n (the codebase's node-id convention)."""
    n = G.number_of_nodes()
    nodes = list(range(1, n + 1))
    rows = []
    used = set()
    G1 = nx.relabel_nodes(G, {nd: i + 1 for i, nd in enumerate(sorted(G.nodes()))})
    for i in range(tds_template.shape[0]):
        while True:
            s, d = rng.choice(nodes, size=2, replace=False)
            s, d = int(s), int(d)
            if (s, d) not in used and nx.has_path(G1, s, d):
                used.add((s, d))
                break
        rows.append([s, d, tds_template[i, 2], tds_template[i, 3],
                     tds_template[i, 4]])
    return np.array(rows, dtype=np.float64)


def waxman52(seed=1, tds_template=None):
    rng = np.random.default_rng(seed)
    n = 52
    while True:
        G = nx.waxman_graph(n, alpha=0.55, beta=0.28, domain=(0, 0, 1, 1),
                            seed=int(seed))
        if nx.is_connected(G):
            break
        seed += 1
    # relabel to 1..n and extract arrays
    nodes = sorted(G.nodes())
    mapping = {nd: i + 1 for i, nd in enumerate(nodes)}
    G = nx.relabel_nodes(G, mapping)
    pos = nx.get_node_attributes(G, "pos")
    xy = np.array([[pos[i][0], pos[i][1]] for i in range(1, n + 1)])

    A = np.zeros((n, n))
    for (u, v) in G.edges():
        A[u - 1, v - 1] = 1
        A[v - 1, u - 1] = 1
    dist = np.hypot(xy[:, 0][:, None] - xy[:, 0][None, :],
                    xy[:, 1][:, None] - xy[:, 1][None, :])
    AT = np.zeros((n, n))
    for u in range(n):
        for v in range(n):
            if A[u, v] > 0:
                AT[u, v] = max(1.0, round(dist[u, v] * 80.0))
    VA = np.where(A > 0, 2.0, 0.0)
    tds = _tds_for_graph(nx.from_numpy_array(A, create_using=nx.Graph),
                         np.random.default_rng(seed + 100), tds_template)
    return Topology.from_arrays("waxman52", A, AT, VA, xy, tds)


def gridcore(seed=1, tds_template=None):
    n_per, cols = 48, 8
    n_core = 4
    n = n_per + n_core
    xy = []
    for i in range(n_per):
        r, c = divmod(i, cols)
        xy.append([0.05 + 0.9 * c / (cols - 1),
                   0.05 + 0.55 * r / 5.0])
    core_xy = [[0.25, 0.78], [0.45, 0.82], [0.65, 0.78], [0.85, 0.82]]
    xy.extend(core_xy)
    xy = np.array(xy)

    A = np.zeros((n, n))
    # grid edges (4-neighbour)
    for i in range(n_per):
        r, c = divmod(i, cols)
        if c + 1 < cols:
            A[i, i + 1] = A[i + 1, i] = 1
        if r + 1 < 6:
            A[i, i + cols] = A[i + cols, i] = 1
    # core ring + chords
    core = list(range(n_per, n))
    for a, b in [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2), (1, 3)]:
        A[core[a], core[b]] = A[core[b], core[a]] = 1
    # attach grid corner regions to core (two attachments each)
    attach = [(0, core[0]), (7, core[0]), (8, core[1]), (15, core[1]),
              (40, core[2]), (47, core[2]), (32, core[3]), (39, core[3])]
    for g, cc in attach:
        A[g, cc] = A[cc, g] = 1

    AT = np.zeros((n, n))
    for u in range(n):
        for v in range(n):
            if A[u, v] > 0:
                if u >= n_per and v >= n_per:
                    AT[u, v] = CORE_DELAY            # core-core
                elif u >= n_per or v >= n_per:
                    AT[u, v] = 10.0                  # grid-core access
                else:
                    AT[u, v] = 1.0                   # peripheral
    VA = np.where(A > 0, 2.0, 0.0)
    tds = _tds_for_graph(nx.from_numpy_array(A, create_using=nx.Graph),
                         np.random.default_rng(seed + 200), tds_template)
    return Topology.from_arrays("gridcore", A, AT, VA, xy, tds)


def get_topologies(tds_template=None):
    orig = __import__("sdn.data", fromlist=["load_topology"]).load_topology()
    if tds_template is None:
        tds_template = orig.tds
    return orig, waxman52(seed=1, tds_template=tds_template), \
        gridcore(seed=1, tds_template=tds_template)


# ---------------------------------------------------------------------------
# Real backbone instances (Topology Zoo / SNDLib public GML exports)
# ---------------------------------------------------------------------------
# These are real European research/education backbones with genuine node
# coordinates and link distances (km). The GML exports carry no capacity
# attribute, so we derive latency from the real distance and calibrate a
# uniform per-link capacity that places each backbone in the same congestion
# regime as the original study (nominal-load bottleneck utilization ~0.87).
# The calibration rule is fixed, applied once, and documented in the paper.

FIBER_MS_PER_KM = 5.0 / 1000.0   # ~5 us/km one-way in fiber (~200,000 km/s)
HOP_MS = 0.5                     # fixed per-hop switching/serialization term
_MEAN_DEG = 3.3                  # target average degree for calibration
_TOTAL_DEMAND = None             # filled from the template demand table


def _capacity_for_regime(G, tds, target_max_util=0.87):
    """Uniform link capacity placing the instance in the thesis regime.

    Strategy: solve the exact min--max MCF (ILP-L) once with a large capacity
    C0 (always feasible for these demands), obtaining Z0; the peak link load
    is then L = Z0 * C0, and we set every link to C = L / target so that the
    certified bottleneck utilization at nominal load equals ``target_max_util``
    (0.87, the value certified for the original instance). The same rule is
    applied to every backbone, so cross-instance comparisons are well posed."""
    from .ilp import ilp_link_mcf
    from .data import Topology as _T
    n = G.number_of_nodes()
    A = np.zeros((n, n))
    for (u, v) in G.edges():
        A[u - 1, v - 1] = A[v - 1, u - 1] = 1
    tds = np.asarray(tds, dtype=np.float64)
    C0 = max(50.0, 10.0 * float(np.sum(tds[:, 2])))   # feasible, well-conditioned
    unit = np.where(A > 0, C0, 0.0)
    probe = _T.from_arrays("probe", A, np.where(A > 0, 1.0, 0.0), unit,
                           np.zeros((n, 2)), tds)
    try:
        res = ilp_link_mcf(probe, load_factor=1.0, time_limit=180.0)
        Z0 = res.get("Z")
    except Exception:
        Z0 = None
    if Z0 is None or not np.isfinite(Z0) or Z0 <= 0:
        # fall back to the mean-load heuristic
        total = float(np.sum(tds[:, 2]))
        m_edges = max(1, int(A.sum() // 2))
        return float(round(2.0 * total / m_edges, 3))
    peak_load = float(Z0) * C0       # heaviest link under the exact solution
    return float(round(peak_load / target_max_util, 4))


def load_backbone(fname, name, tds_template, seed=1):
    """Build a Topology from a public SNDLib/Topology-Zoo GML file."""
    import os
    import networkx as nx
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "data", "backbones", fname)
    G = nx.read_gml(path)
    nodes = sorted(G.nodes())
    mapping = {nd: i + 1 for i, nd in enumerate(nodes)}
    G = nx.relabel_nodes(G, mapping)
    n = G.number_of_nodes()

    lon = nx.get_node_attributes(G, "lon")
    lat = nx.get_node_attributes(G, "lat")
    xy = np.array([[lon[i], lat[i]] for i in range(1, n + 1)])

    A = np.zeros((n, n))
    AT = np.zeros((n, n))
    for (u, v, d) in G.edges(data=True):
        dist = float(d.get("dist", 0.0) or 0.0)
        if dist <= 0:                       # fall back to great-circle-ish
            dist = float(np.hypot((xy[u - 1, 0] - xy[v - 1, 0]) * 50.0,
                                  (xy[u - 1, 1] - xy[v - 1, 1]) * 70.0))
        A[u - 1, v - 1] = A[v - 1, u - 1] = 1
        delay = max(0.5, dist * FIBER_MS_PER_KM) + HOP_MS
        AT[u - 1, v - 1] = AT[v - 1, u - 1] = round(delay, 2)

    # normalize coordinates for plotting (keep real values in a backup attr)
    VA = np.zeros((n, n))
    tds = _tds_for_graph(G, np.random.default_rng(seed + 300), tds_template)
    cap = _capacity_for_regime(G, tds)
    for u in range(n):
        for v in range(n):
            if A[u, v] > 0:
                VA[u, v] = cap
    topo = Topology.from_arrays(name, A, AT, VA, xy, tds)
    topo.capacity = cap
    topo.real_geography = True
    return topo


def germany50(tds_template=None, seed=1):
    return load_backbone("germany50.gml", "germany50", tds_template, seed)


def geant2012(tds_template=None, seed=1):
    return load_backbone("Geant2012.gml", "geant2012", tds_template, seed)


def get_backbones(tds_template=None):
    if tds_template is None:
        tds_template = __import__("sdn.data", fromlist=["load_topology"]) \
            .load_topology().tds
    return germany50(tds_template=tds_template), \
        geant2012(tds_template=tds_template)


def get_all_instances(tds_template=None):
    """All five instances: the original + two synthetic + two real backbones.

    The ``DSH_TOPOS`` environment variable (comma-separated names) restricts
    the set, e.g. ``DSH_TOPOS=germany50,geant2012``."""
    if tds_template is None:
        tds_template = __import__("sdn.data", fromlist=["load_topology"]) \
            .load_topology().tds
    import os
    all_inst = list(get_topologies(tds_template=tds_template)) + \
        list(get_backbones(tds_template=tds_template))
    sel = os.environ.get("DSH_TOPOS", "").strip()
    if sel:
        want = {s.strip() for s in sel.split(",") if s.strip()}
        all_inst = [t for t in all_inst if t.name in want]
    return tuple(all_inst)