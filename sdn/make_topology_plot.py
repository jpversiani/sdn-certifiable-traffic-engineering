import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sdn.data import load_topology
from sdn.run_optimization import run_optimization, routes_from_idx

FIG_DIR = 'paper/figures'
top = load_topology()
n = top.n
res = run_optimization(seed=42)
routes_opt = routes_from_idx(res['mrotas_aco'], res['best_ga'], n)
routes_dj = {a: [int(x) for x in res['mrotas_dj'][a-1][:n] if x != 0] for a in range(1, top.napp + 1)}

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5.2), dpi=300)
xy = top.xy

for ax, title, routes in [(ax1, '(a) Dijkstra Baseline (Congested Core)', routes_dj),
                          (ax2, '(b) ACO + GA (Load-Balanced Routes)', routes_opt)]:
    for i in range(top.n):
        for j in range(i + 1, top.n):
            if top.A[i, j] > 0:
                ax.plot([xy[i, 0], xy[j, 0]], [xy[i, 1], xy[j, 1]], color='#b0bec5', lw=1.2, zorder=1)
    
    colors = plt.cm.tab20(np.linspace(0, 1, len(routes)))
    for k, (a, rota) in enumerate(routes.items()):
        xs = [xy[x-1, 0] for x in rota]
        ys = [xy[x-1, 1] for x in rota]
        ax.plot(xs, ys, color=colors[k], lw=1.8, alpha=0.85, zorder=3)
    ax.scatter(xy[:, 0], xy[:, 1], color='#263238', s=24, zorder=4)
    for i in range(top.n):
        ax.text(xy[i, 0] + 0.12, xy[i, 1] + 0.12, str(i + 1), fontsize=6, color='#37474f')
    ax.set_title(title, fontsize=11, weight='bold')
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_aspect('equal')

plt.tight_layout()
fig.savefig(f'{FIG_DIR}/fig6_topology.png', dpi=300, bbox_inches='tight')
fig.savefig(f'{FIG_DIR}/fig6_topology.pdf', bbox_inches='tight')
plt.close(fig)
print('Fig 6 topology saved.')
