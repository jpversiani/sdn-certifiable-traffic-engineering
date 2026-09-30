#!/usr/bin/env python3
"""Exact Multi-Commodity QoS Routing ILP benchmark using SciPy / HiGHS solver.
Evaluates:
1. Theoretical Global Optimum (ILP with Min-Max Link Utilization).
2. Optimality Gap of ACO+GA and CSPF against the exact ILP solution.
3. Flow arrival order sensitivity of sequential greedy CSPF.
4. Load scaling sweep comparing ILP vs. ACO+GA vs. CSPF vs. Dijkstra.
"""

import os
import heapq
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import milp, LinearConstraint, Bounds

from sdn.data import load_topology
from sdn.run_optimization import run_optimization, routes_from_idx
from sdn.cspf import cspf_route

FIG_DIR = 'paper/figures'
os.makedirs(FIG_DIR, exist_ok=True)

class ExactILPSolver:
    def __init__(self, top):
        self.top = top
        self.n = top.n
        self.K = top.napp
        self.tds = top.tds
        self.A = top.A
        self.AT = top.AT
        self.VA = top.VA

        # Enumerate directed edges
        self.edges = []
        for i in range(self.n):
            for j in range(self.n):
                if self.A[i, j] > 0:
                    self.edges.append((i, j))
        self.E = len(self.edges)
        self.edge_idx = {(i, j): idx for idx, (i, j) in enumerate(self.edges)}

        # Undirected edges
        self.undirected_edges = set()
        for (u, v) in self.edges:
            self.undirected_edges.add(tuple(sorted([u, v])))

    def solve_mlu(self, scale=1.0):
        """Solves the exact ILP to minimize Maximum Link Utilization (theta)."""
        tds = self.tds.copy()
        tds[:, 2] *= scale
        n_vars = self.K * self.E + 1
        theta_idx = n_vars - 1

        rows, lhs, rhs = [], [], []

        # 1. Flow conservation for each commodity k and node v
        for k in range(self.K):
            src = int(tds[k, 0]) - 1
            dst = int(tds[k, 1]) - 1
            for v in range(self.n):
                row = np.zeros(n_vars)
                for j in range(self.n):
                    if (v, j) in self.edge_idx:
                        row[k * self.E + self.edge_idx[(v, j)]] += 1
                    if (j, v) in self.edge_idx:
                        row[k * self.E + self.edge_idx[(j, v)]] -= 1
                val = 1.0 if v == src else (-1.0 if v == dst else 0.0)
                rows.append(row); lhs.append(val); rhs.append(val)

        # 2. Delay bound constraints
        for k in range(self.K):
            row = np.zeros(n_vars)
            max_d = tds[k, 3]
            for e_idx, (i, j) in enumerate(self.edges):
                row[k * self.E + e_idx] = self.AT[i, j]
            rows.append(row); lhs.append(0.0); rhs.append(max_d)

        # 3. Min-Max Link capacity constraints: load(u,v) - cap * theta <= 0
        for (u, v) in self.undirected_edges:
            row = np.zeros(n_vars)
            cap = self.VA[u, v]
            e1 = self.edge_idx.get((u, v), None)
            e2 = self.edge_idx.get((v, u), None)
            for k in range(self.K):
                fl = tds[k, 2]
                if e1 is not None: row[k * self.E + e1] += fl
                if e2 is not None: row[k * self.E + e2] += fl
            row[theta_idx] = -cap
            rows.append(row); lhs.append(-np.inf); rhs.append(0.0)

        A_mat = np.array(rows)
        constraints = LinearConstraint(A_mat, lhs, rhs)
        integrality = np.zeros(n_vars)
        integrality[:self.K * self.E] = 1 # binary flow vars
        integrality[theta_idx] = 0        # continuous theta

        bounds = Bounds(np.zeros(n_vars), [1.0] * (self.K * self.E) + [10.0])
        c = np.zeros(n_vars)
        c[theta_idx] = 1.0

        res = milp(c=c, integrality=integrality, bounds=bounds, constraints=constraints)
        if res.success:
            return float(res.x[theta_idx])
        return float('nan')


def run_cspf_order_experiment(top, num_trials=100, seed=42):
    """Evaluates how sensitive greedy sequential CSPF is to flow arrival order."""
    n = top.n
    tds = top.tds
    K = tds.shape[0]
    VA = top.VA
    AT = top.AT
    A = top.A
    rng = np.random.default_rng(seed)

    overloads_list = []
    max_u_list = []

    for trial in range(num_trials):
        order = list(range(K))
        rng.shuffle(order)
        residual_cap = VA.copy()
        routes = {}

        for k in order:
            src, dst, flow = int(tds[k, 0]), int(tds[k, 1]), tds[k, 2]
            dist = {i: float('inf') for i in range(1, n + 1)}
            prev = {i: None for i in range(1, n + 1)}
            dist[src] = 0
            pq = [(0, src)]

            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]: continue
                if u == dst: break
                for v in range(1, n + 1):
                    if A[u - 1, v - 1] > 0 and residual_cap[u - 1, v - 1] >= flow:
                        cost = AT[u - 1, v - 1] if AT[u - 1, v - 1] > 0 else 1.0
                        if dist[u] + cost < dist[v]:
                            dist[v] = dist[u] + cost
                            prev[v] = u
                            heapq.heappush(pq, (dist[v], v))

            if dist[dst] < float('inf'):
                path = []
                curr = dst
                while curr is not None:
                    path.append(curr)
                    curr = prev[curr]
                path.reverse()
                routes[k + 1] = path
                for i in range(len(path) - 1):
                    u, v = path[i], path[i + 1]
                    residual_cap[u - 1, v - 1] -= flow
                    residual_cap[v - 1, u - 1] -= flow
            else:
                # Fallback to shortest unpruned path
                pq_fb = [(0, src)]
                dist_fb = {i: float('inf') for i in range(1, n + 1)}
                prev_fb = {i: None for i in range(1, n + 1)}
                dist_fb[src] = 0
                while pq_fb:
                    d, u = heapq.heappop(pq_fb)
                    if d > dist_fb[u]: continue
                    if u == dst: break
                    for v in range(1, n + 1):
                        if A[u - 1, v - 1] > 0:
                            cost = AT[u - 1, v - 1] if AT[u - 1, v - 1] > 0 else 1.0
                            if dist_fb[u] + cost < dist_fb[v]:
                                dist_fb[v] = dist_fb[u] + cost
                                prev_fb[v] = u
                                heapq.heappush(pq_fb, (dist_fb[v], v))
                path = []
                curr = dst
                while curr is not None:
                    path.append(curr)
                    curr = prev_fb[curr]
                path.reverse()
                routes[k + 1] = path

        loads = {}
        for a in range(1, K + 1):
            p = routes[a]
            fl = tds[a-1, 2]
            for i in range(len(p)-1):
                e = tuple(sorted([p[i], p[i+1]]))
                loads[e] = loads.get(e, 0.0) + fl
        overloads = sum(1 for (u, v), load in loads.items() if VA[u-1, v-1] < load)
        max_u = max(load / VA[u-1, v-1] for (u, v), load in loads.items())
        overloads_list.append(overloads)
        max_u_list.append(max_u)

    return overloads_list, max_u_list


def generate_benchmark_plot():
    top = load_topology()
    solver = ExactILPSolver(top)
    res_opt = run_optimization(seed=42)
    routes_opt = routes_from_idx(res_opt['mrotas_aco'], res_opt['best_ga'], top.n)
    routes_dj = {a: [int(x) for x in res_opt['mrotas_dj'][a-1][:top.n] if x != 0] for a in range(1, top.napp + 1)}
    routes_cspf = cspf_route(top)

    scales = np.linspace(0.6, 1.4, 9)
    ilp_mlu = []
    opt_mlu = []
    cspf_mlu = []
    dj_mlu = []

    def get_mlu(routes, scale):
        tds = top.tds.copy()
        tds[:, 2] *= scale
        loads = {}
        for a in range(1, top.napp + 1):
            p = routes[a]
            fl = tds[a-1, 2]
            for i in range(len(p)-1):
                e = tuple(sorted([p[i], p[i+1]]))
                loads[e] = loads.get(e, 0.0) + fl
        return max(load / top.VA[u-1, v-1] for (u, v), load in loads.items())

    print('Computing exact ILP MLU across traffic load scaling...')
    for s in scales:
        ilp_val = solver.solve_mlu(s)
        ilp_mlu.append(ilp_val * 100)
        opt_mlu.append(get_mlu(routes_opt, s) * 100)
        cspf_mlu.append(get_mlu(routes_cspf, s) * 100)
        dj_mlu.append(get_mlu(routes_dj, s) * 100)

    # 100 order experiment
    ov_list, mu_list = run_cspf_order_experiment(top, num_trials=100)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.3), dpi=300)

    # Panel (a): Exact ILP vs Heuristics
    ax1.plot(scales * 100, ilp_mlu, 'k-', lw=2.4, label='Exact Global Optimum (ILP / HiGHS)')
    ax1.plot(scales * 100, opt_mlu, 'g-o', lw=1.8, label='Proposed Hybrid (ACO + GA)')
    ax1.plot(scales * 100, cspf_mlu, 'y-^', color='#f57c00', lw=1.8, label='Sequential CSPF (Greedy)')
    ax1.plot(scales * 100, dj_mlu, 'r-s', lw=1.8, label='Shortest Path (Dijkstra)')
    ax1.axhline(100, color='blue', ls='--', lw=1.2, label='Physical Link Capacity (100%)')
    ax1.set_xlabel('Offered Traffic Demand (% of Nominal Load)')
    ax1.set_ylabel('Maximum Link Utilization (%)')
    ax1.set_title('(a) Optimality Gap vs. Exact ILP (HiGHS)')
    ax1.grid(True, ls=':', alpha=0.6)
    ax1.legend(fontsize=8, loc='upper left')

    # Panel (b): CSPF arrival order vulnerability
    ax2.hist(np.array(mu_list) * 100, bins=12, color='#f57c00', alpha=0.8, edgecolor='black')
    ax2.axvline(100, color='blue', ls='--', lw=1.5, label='Capacity Threshold (100%)')
    ax2.axvline(np.mean(mu_list) * 100, color='red', ls='-', lw=1.8, label=f'CSPF Mean ({np.mean(mu_list)*100:.1f}%)')
    ax2.axvline(opt_mlu[4], color='green', ls='-', lw=2.0, label='ACO+GA Deterministic (100%)')
    ax2.set_xlabel('Worst-Case Link Utilization (%)')
    ax2.set_ylabel('Frequency (100 Random Arrival Orders)')
    ax2.set_title('(b) CSPF Vulnerability to Flow Arrival Order')
    ax2.grid(True, ls=':', alpha=0.6)
    ax2.legend(fontsize=8, loc='upper right')

    plt.tight_layout()
    fig.savefig(f'{FIG_DIR}/fig7_ilp_benchmark.png', dpi=300, bbox_inches='tight')
    fig.savefig(f'{FIG_DIR}/fig7_ilp_benchmark.pdf', bbox_inches='tight')
    plt.close(fig)
    print('Fig 7 ILP benchmark saved successfully!')

if __name__ == '__main__':
    generate_benchmark_plot()
