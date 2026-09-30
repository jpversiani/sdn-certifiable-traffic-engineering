#!/usr/bin/env python3
"""Generates all publication-quality figures for the IEEE paper."""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from sdn.data import load_topology
from sdn.run_optimization import run_optimization, routes_from_idx
from sdn.empirical_data import get_empirical_dataframe
from sdn.cspf import cspf_route

FIG_DIR = 'paper/figures'
os.makedirs(FIG_DIR, exist_ok=True)

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.titlesize': 13,
    'font.family': 'sans-serif',
})

def plot_architecture():
    fig, ax = plt.subplots(figsize=(8.5, 4.2), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)

    box_app = dict(boxstyle='round,pad=0.5', facecolor='#e3f2fd', edgecolor='#1976d2', lw=1.5)
    box_opt = dict(boxstyle='round,pad=0.6', facecolor='#e8f5e9', edgecolor='#388e3c', lw=1.5)
    box_sdn = dict(boxstyle='round,pad=0.5', facecolor='#fff3e0', edgecolor='#f57c00', lw=1.5)
    box_data = dict(boxstyle='round,pad=0.5', facecolor='#f3e5f5', edgecolor='#7b1fa2', lw=1.5)

    ax.text(1.8, 4.8, 'QoS Application Demands\n- Bandwidth ($\\lambda_k$)\n- Max Delay ($h_k$)\n- Priority ($\\delta_k$)',
            ha='center', va='center', bbox=box_app, weight='bold')

    ax.text(5.5, 4.8, 'Stage 1: Route Exploration\nAnt Colony Optimization (ACO)\n- Diverse Candidate Route Pool $R_k$\n- Pheromone & Heuristic Balance',
            ha='center', va='center', bbox=box_opt)

    ax.text(5.5, 2.5, 'Stage 2: Combinatorial Selection\nGenetic Algorithm (GA) / DE\n- Objective Function $FO$ Max\n- Bandwidth & Delay Constraints',
            ha='center', va='center', bbox=box_opt, weight='bold')

    ax.text(1.8, 1.8, 'SDN Control Plane\nFloodlight Controller\n- Global Topology View\n- OpenFlow FlowMod Gen',
            ha='center', va='center', bbox=box_sdn)

    ax.text(8.8, 2.5, 'SDN Data Plane\nMininet / Open vSwitch\n- 52 Switches / Mesh\n- Queues & Flow Tables\n- D-ITG Traffic Injection',
            ha='center', va='center', bbox=box_data)

    arrow_props = dict(arrowstyle='->', lw=1.8, color='#37474f')
    ax.annotate('', xy=(3.6, 4.8), xytext=(2.9, 4.8), arrowprops=arrow_props)
    ax.annotate('', xy=(5.5, 3.4), xytext=(5.5, 4.0), arrowprops=arrow_props)
    ax.annotate('', xy=(3.0, 2.0), xytext=(4.0, 2.3), arrowprops=arrow_props)
    ax.annotate('', xy=(7.4, 2.5), xytext=(6.9, 2.5), arrowprops=arrow_props)
    ax.annotate('', xy=(7.4, 2.0), xytext=(2.9, 1.8), arrowprops=dict(arrowstyle='->', lw=1.8, color='#d32f2f', ls='--'))

    ax.text(5.0, 1.3, 'OpenFlow Southbound API (Flow Rules)', color='#d32f2f', weight='bold', ha='center', fontsize=9)
    plt.tight_layout()
    fig.savefig(f'{FIG_DIR}/fig1_architecture.png', dpi=300, bbox_inches='tight')
    fig.savefig(f'{FIG_DIR}/fig1_architecture.pdf', bbox_inches='tight')
    plt.close(fig)
    print('Fig 1 saved.')

def plot_convergence(res):
    fig, ax = plt.subplots(figsize=(6.5, 3.8), dpi=300)
    iters_ga = np.arange(1, len(res['bestcost_ga']) + 1)
    iters_de = np.arange(1, len(res['bestcost_de']) + 1)

    ax.plot(iters_ga, res['bestcost_ga'], label='ACO + GA', color='#1565c0', lw=2.2)
    ax.plot(iters_de, res['bestcost_de'], label='ACO + DE', color='#e65100', lw=2.0, ls='--')
    ax.axhline(132, color='#2e7d32', ls=':', lw=1.8, label='Theoretical Global Optimum (FO = 132)')
    ax.axhline(120, color='#c62828', ls='-.', lw=1.8, label='Shortest Path Baseline (Dijkstra = 120)')

    ax.set_xlabel('Generation / Iteration')
    ax.set_ylabel('Objective Function Value (Fitness)')
    ax.set_title('Metaheuristic Optimization Convergence on 52-Node Topology')
    ax.grid(True, ls=':', alpha=0.6)
    ax.legend(loc='lower right', frameon=True)
    ax.set_ylim(110, 134)
    plt.tight_layout()
    fig.savefig(f'{FIG_DIR}/fig2_convergence.png', dpi=300, bbox_inches='tight')
    fig.savefig(f'{FIG_DIR}/fig2_convergence.pdf', bbox_inches='tight')
    plt.close(fig)
    print('Fig 2 saved.')

def plot_empirical_results():
    df = get_empirical_dataframe()
    apps = df['app_id'].values

    fig, axs = plt.subplots(2, 2, figsize=(11, 7.5), dpi=300)
    bar_width = 0.38
    x = np.arange(len(apps))

    # (a) Throughput
    ax = axs[0, 0]
    ax.bar(x - bar_width/2, df['opt_thr_kbps'], width=bar_width, label='Optimized (ACO+AG)', color='#2e7d32', alpha=0.9)
    ax.bar(x + bar_width/2, df['dj_thr_kbps'], width=bar_width, label='Baseline (Dijkstra)', color='#c62828', alpha=0.9)
    ax.plot(x, df['target_thr_kbps'], color='black', ls='--', lw=1.2, label='Nominal Demand', marker='o', markersize=3)
    ax.set_xticks(x)
    ax.set_xticklabels(apps, fontsize=8)
    ax.set_xlabel('Application ID')
    ax.set_ylabel('Throughput (kbps)')
    ax.set_title('(a) Received Throughput in Mininet/D-ITG')
    ax.legend(loc='upper right', fontsize=8)
    ax.grid(True, ls=':', alpha=0.5)

    # (b) Packet Loss (%)
    ax = axs[0, 1]
    ax.bar(x - bar_width/2, df['opt_loss_pct'], width=bar_width, label='Optimized (ACO+AG)', color='#2e7d32', alpha=0.9)
    ax.bar(x + bar_width/2, df['dj_loss_pct'], width=bar_width, label='Baseline (Dijkstra)', color='#c62828', alpha=0.9)
    ax.set_xticks(x)
    ax.set_xticklabels(apps, fontsize=8)
    ax.set_xlabel('Application ID')
    ax.set_ylabel('Packet Loss Ratio (%)')
    ax.set_title('(b) Packet Loss Ratio in Mininet/D-ITG')
    ax.legend(loc='upper right', fontsize=8)
    ax.grid(True, ls=':', alpha=0.5)

    # (c) End-to-End Delay
    ax = axs[1, 0]
    ax.bar(x - bar_width/2, df['opt_delay_s'] * 1000.0, width=bar_width, label='Optimized (ACO+AG)', color='#2e7d32', alpha=0.9)
    ax.bar(x + bar_width/2, df['dj_delay_s'] * 1000.0, width=bar_width, label='Baseline (Dijkstra)', color='#c62828', alpha=0.9)
    ax.set_yscale('log')
    ax.set_xticks(x)
    ax.set_xticklabels(apps, fontsize=8)
    ax.set_xlabel('Application ID')
    ax.set_ylabel('End-to-End Delay (ms, log scale)')
    ax.set_title('(c) End-to-End Delay (Mininet Bufferbloat Impact)')
    ax.legend(loc='upper right', fontsize=8)
    ax.grid(True, ls=':', alpha=0.5)

    # (d) Jitter (ms)
    ax = axs[1, 1]
    ax.bar(x - bar_width/2, df['opt_jitter_s'] * 1000.0, width=bar_width, label='Optimized (ACO+AG)', color='#2e7d32', alpha=0.9)
    ax.bar(x + bar_width/2, df['dj_jitter_s'] * 1000.0, width=bar_width, label='Baseline (Dijkstra)', color='#c62828', alpha=0.9)
    ax.set_xticks(x)
    ax.set_xticklabels(apps, fontsize=8)
    ax.set_xlabel('Application ID')
    ax.set_ylabel('Jitter (ms)')
    ax.set_title('(d) Jitter Performance in Mininet/D-ITG')
    ax.legend(loc='upper right', fontsize=8)
    ax.grid(True, ls=':', alpha=0.5)

    plt.tight_layout()
    fig.savefig(f'{FIG_DIR}/fig3_mininet_results.png', dpi=300, bbox_inches='tight')
    fig.savefig(f'{FIG_DIR}/fig3_mininet_results.pdf', bbox_inches='tight')
    plt.close(fig)
    print('Fig 3 saved.')

def plot_link_loads(top, routes_opt, routes_dj, routes_cspf):
    K = top.tds.shape[0]
    VA = top.VA

    def get_loads(routes):
        loads = {}
        for a in range(1, K + 1):
            p = routes[a]
            fl = top.tds[a-1, 2]
            for i in range(len(p)-1):
                e = tuple(sorted([p[i], p[i+1]]))
                loads[e] = loads.get(e, 0.0) + fl
        return loads

    l_opt = get_loads(routes_opt)
    l_dj = get_loads(routes_dj)
    l_cs = get_loads(routes_cspf)

    edges = sorted(list(set(list(l_opt.keys()) + list(l_dj.keys()) + list(l_cs.keys()))))
    edges.sort(key=lambda e: l_dj.get(e, 0.0), reverse=True)
    top_edges = edges[:16]

    fig, ax = plt.subplots(figsize=(10, 4.2), dpi=300)
    x = np.arange(len(top_edges))
    w = 0.28

    v_dj = [l_dj.get(e, 0.0) for e in top_edges]
    v_cs = [l_cs.get(e, 0.0) for e in top_edges]
    v_opt = [l_opt.get(e, 0.0) for e in top_edges]

    ax.bar(x - w, v_dj, width=w, label='Dijkstra (Shortest Path)', color='#c62828', alpha=0.85)
    ax.bar(x, v_cs, width=w, label='CSPF (Sequential)', color='#f57c00', alpha=0.85)
    ax.bar(x + w, v_opt, width=w, label='ACO + GA (Optimized)', color='#2e7d32', alpha=0.85)

    ax.axhline(2.0, color='blue', ls='--', lw=1.8, label='Nominal Link Capacity (2.0 Mbps)')
    ax.set_xticks(x)
    labels = [f'{e[0]}-{e[1]}' for e in top_edges]
    ax.set_xticklabels(labels, rotation=45, fontsize=8)
    ax.set_xlabel('Network Links (Source Switch - Target Switch)')
    ax.set_ylabel('Aggregate Offered Load (Mbps)')
    ax.set_title('Offered Load Distribution on the Most Congested Links')
    ax.legend(loc='upper right')
    ax.grid(True, ls=':', alpha=0.5)

    plt.tight_layout()
    fig.savefig(f'{FIG_DIR}/fig4_link_utilization.png', dpi=300, bbox_inches='tight')
    fig.savefig(f'{FIG_DIR}/fig4_link_utilization.pdf', bbox_inches='tight')
    plt.close(fig)
    print('Fig 4 saved.')

def plot_load_scaling(top, routes_opt, routes_dj, routes_cspf):
    factors = np.linspace(0.6, 1.6, 11)
    
    def eval_scale(routes, factor):
        tds = top.tds.copy()
        tds[:, 2] *= factor
        VA = top.VA
        K = tds.shape[0]
        loads = {}
        for a in range(1, K + 1):
            p = routes[a]
            fl = tds[a-1, 2]
            for i in range(len(p)-1):
                e = tuple(sorted([p[i], p[i+1]]))
                loads[e] = loads.get(e, 0.0) + fl
        overloads = sum(1 for (u, v), load in loads.items() if VA[u-1, v-1] < load)
        max_u = max(load / VA[u-1, v-1] for (u, v), load in loads.items())
        fo = sum(tds[:, 4]) + 3*K + 2*(K - overloads) + 1*K
        return fo, overloads, max_u

    dj_ov, dj_mu = [], []
    cs_ov, cs_mu = [], []
    op_ov, op_mu = [], []

    for f in factors:
        _, o1, m1 = eval_scale(routes_dj, f)
        _, o2, m2 = eval_scale(routes_cspf, f)
        _, o3, m3 = eval_scale(routes_opt, f)
        dj_ov.append(o1); dj_mu.append(m1)
        cs_ov.append(o2); cs_mu.append(m2)
        op_ov.append(o3); op_mu.append(m3)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.0), dpi=300)

    ax1.plot(factors * 100, dj_ov, marker='s', color='#c62828', lw=2, label='Dijkstra')
    ax1.plot(factors * 100, cs_ov, marker='^', color='#f57c00', lw=2, label='CSPF')
    ax1.plot(factors * 100, op_ov, marker='o', color='#2e7d32', lw=2, label='ACO + GA')
    ax1.set_xlabel('Offered Traffic Demand (% of Nominal Load)')
    ax1.set_ylabel('Number of Congested Links (> 100% capacity)')
    ax1.set_title('(a) Link Overload Count vs Traffic Load')
    ax1.grid(True, ls=':', alpha=0.5)
    ax1.legend()

    ax2.plot(factors * 100, np.array(dj_mu) * 100, marker='s', color='#c62828', lw=2, label='Dijkstra')
    ax2.plot(factors * 100, np.array(cs_mu) * 100, marker='^', color='#f57c00', lw=2, label='CSPF')
    ax2.plot(factors * 100, np.array(op_mu) * 100, marker='o', color='#2e7d32', lw=2, label='ACO + GA')
    ax2.axhline(100, color='blue', ls='--', lw=1.5, label='100% Link Capacity')
    ax2.set_xlabel('Offered Traffic Demand (% of Nominal Load)')
    ax2.set_ylabel('Maximum Link Utilization (%)')
    ax2.set_title('(b) Worst-Case Link Utilization')
    ax2.grid(True, ls=':', alpha=0.5)
    ax2.legend()

    plt.tight_layout()
    fig.savefig(f'{FIG_DIR}/fig5_load_stress.png', dpi=300, bbox_inches='tight')
    fig.savefig(f'{FIG_DIR}/fig5_load_stress.pdf', bbox_inches='tight')
    plt.close(fig)
    print('Fig 5 saved.')

def main():
    top = load_topology()
    n = top.n
    print('Running optimization for publication plots...')
    res = run_optimization(aco_ants=100, aco_iters=100, de_iters=300, ga_iters=300, seed=42)
    routes_opt = routes_from_idx(res['mrotas_aco'], res['best_ga'], n)
    routes_dj = {a: [int(x) for x in res['mrotas_dj'][a-1][:n] if x != 0] for a in range(1, top.napp + 1)}
    routes_cspf = cspf_route(top)

    plot_architecture()
    plot_convergence(res)
    plot_empirical_results()
    plot_link_loads(top, routes_opt, routes_dj, routes_cspf)
    plot_load_scaling(top, routes_opt, routes_dj, routes_cspf)
    print('All publication figures generated successfully!')

if __name__ == '__main__':
    main()
