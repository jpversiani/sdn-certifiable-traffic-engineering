#!/usr/bin/env python3
"""Runner: optimizes the routes (ACO+AG / ACO+DE vs Dijkstra), simulates both
network configurations with simpy and prints/saves a comparison report plus
plots.  Reproduces the thesis headline figures on topology 1."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from sdn.data import load_topology
from sdn.run_optimization import run_optimization, routes_from_idx
from sdn.netsim import simulate_network

OUT = "output"
os.makedirs(OUT, exist_ok=True)

# --------------------------------------------------------------------------
def format_pct(x):
    return f"{100*x:.1f}%"


def main():
    res = run_optimization(aco_ants=100, aco_iters=100,
                           de_iters=200, ga_iters=200, node_pop=50, seed=42)
    top = res["top"]
    n = top.n
    napp = top.napp

    print("=" * 72)
    print("OBJECTIVE-FUNCTION (fitness) SCORES  -- thesis optimum = 132")
    print("=" * 72)
    print(f"  Dijkstra             : {res['fo_dijkstra']:6.1f}   (thesis: 120)")
    print(f"  random baseline      : {res['fo_random']:6.1f}")
    print(f"  ACO + DE (300x60)    : {res['fo_de']:6.1f}   (thesis: 132)")
    print(f"  ACO + AG (300x60)    : {res['fo_ga']:6.1f}   (thesis: 132)")

    # ---------------- network simulation (optimised vs dijkstra) --------
    routes_opt = routes_from_idx(res["mrotas_aco"], res["best_ga"], n)
    routes_dj = {a: [int(x) for x in res["mrotas_dj"][a-1][:n] if x != 0]
                 for a in range(1, napp + 1)}

    DURATION = 5.0
    res_opt = simulate_network(top, routes_opt, duration=DURATION,
                               max_queue_pkts=80, seed=0)
    res_dj = simulate_network(top, routes_dj, duration=DURATION,
                              max_queue_pkts=80, seed=0)

    # aggregate metrics
    def agg(r):
        loss = np.mean([r[a]["loss"] for a in r])
        delay = np.mean([r[a]["mean_delay_ms"] for a in r])
        jitter = np.mean([r[a]["jitter_ms"] for a in r])
        thr = np.mean([r[a]["throughput_mbps"] for a in r])
        return dict(loss=loss, delay=delay, jitter=jitter, thr=thr)

    ao, ad = agg(res_opt), agg(res_dj)
    print("\n" + "=" * 72)
    print("SDN NETWORK SIMULATION  (simpy) -- optimised (ACO+AG) vs Dijkstra")
    print("=" * 72)
    header = (f"{'metric':<22}{'optimised':>12}{'dijkstra':>12}"
              f"{'ratio (opt/dj)':>16}")
    print(header)
    rows = [
        ("throughput (Mbps)", ao["thr"], ad["thr"], ao["thr"] / ad["thr"]),
        ("e2e delay (ms)", ao["delay"], ad["delay"], ao["delay"] / ad["delay"]),
        ("jitter (ms)", ao["jitter"], ad["jitter"], ao["jitter"] / ad["jitter"]),
        ("packet loss", ao["loss"], ad["loss"], ao["loss"] / ad["loss"]),
    ]
    for name, vo, vd, ratio in rows:
        if name == "packet loss":
            print(f"{name:<22}{format_pct(vo):>12}{format_pct(vd):>12}"
                  f"{ratio:>16.2f}x")
        else:
            print(f"{name:<22}{vo:>12.4f}{vd:>12.4f}{ratio:>15.2f}x")

    # save per-app table
    import csv
    with open(os.path.join(OUT, "per_application_results.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["app", "orig", "dest", "flow_mbps", "max_delay_ms",
                    "opt_loss", "dj_loss", "opt_delay_ms", "dj_delay_ms",
                    "opt_jitter_ms", "dj_jitter_ms",
                    "opt_throughput_mbps", "dj_throughput_mbps"])
        for a in range(1, napp + 1):
            t = top.tds[a-1]
            w.writerow([a, int(t[0]), int(t[1]), t[2], t[3],
                        res_opt[a]["loss"], res_dj[a]["loss"],
                        res_opt[a]["mean_delay_ms"], res_dj[a]["mean_delay_ms"],
                        res_opt[a]["jitter_ms"], res_dj[a]["jitter_ms"],
                        res_opt[a]["throughput_mbps"], res_dj[a]["throughput_mbps"]])

    # ---------------- plots ----------------
    plot_convergence(res, OUT)
    plot_network(top, routes_opt, routes_dj, OUT)
    plot_metrics(res_opt, res_dj, OUT)
    plot_link_load(top, res["mrotas_aco"], res["best_ga"], res["mrotas_dj"],
                   OUT)
    print(f"\nPlots + CSV written to {OUT}/")


def plot_convergence(res, out):
    plt.figure(figsize=(7, 5))
    its = np.arange(1, len(res["bestcost_de"]) + 1)
    plt.plot(its, res["bestcost_de"], "--b", lw=2, label="ACO + DE")
    plt.plot(its, res["bestcost_ga"], "r", lw=2, label="ACO + AG")
    plt.axhline(res["fo_dijkstra"], color="k", ls="-.", lw=2,
                label=f"Dijkstra ({res['fo_dijkstra']:.0f})")
    plt.axhline(132, color="g", ls=":", lw=1.5, label="Óptimo FO = 132")
    plt.xlabel("Iteração"); plt.ylabel("Melhor valor função objetivo")
    plt.title("Convergencia ACO+DE vs ACO+AG vs Dijkstra")
    plt.grid(True); plt.legend()
    plt.tight_layout(); plt.savefig(f"{out}/convergence.png", dpi=110)


def plot_network(top, routes_opt, routes_dj, out):
    xy = top.xy
    fig, ax = plt.subplots(1, 2, figsize=(13, 5.5))
    for axi, (title, routes) in zip(
            ax, [("Red Optimizada (ACO+AG)", routes_opt),
                 ("Red Dijkstra", routes_dj)]):
        for i in range(top.n):
            for j in range(i + 1, top.n):
                if top.A[i, j] > 0:
                    axi.plot([xy[i, 0], xy[j, 0]], [xy[i, 1], xy[j, 1]],
                             color="0.85", lw=1, zorder=1)
        colors = plt.cm.tab20(np.linspace(0, 1, len(routes)))
        for k, (a, rota) in enumerate(routes.items()):
            xs = [xy[x-1, 0] for x in rota]
            ys = [xy[x-1, 1] for x in rota]
            axi.plot(xs, ys, color=colors[k], lw=1.6, alpha=0.85, zorder=3)
        axi.scatter(xy[:, 0], xy[:, 1], color="k", s=18, zorder=4)
        axi.set_title(title); axi.set_xticks([]); axi.set_yticks([])
        axi.set_aspect("equal")
    plt.tight_layout(); plt.savefig(f"{out}/network_routes.png", dpi=110)


def plot_metrics(res_opt, res_dj, out):
    apps = sorted(res_opt.keys())
    labels = [f"{a}" for a in apps]
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    mets = [
        ("throughput_mbps", "Vazão (Mbps)"),
        ("mean_delay_ms", "Atraso fim-a-fim (ms)"),
        ("jitter_ms", "Jitter (ms)"),
        ("loss", "Perda de paquetes"),
    ]
    for ax, (key, label) in zip(axes.flat, mets):
        vo = [res_opt[a][key] for a in apps]
        vd = [res_dj[a][key] for a in apps]
        x = np.arange(len(apps)); w = 0.38
        ax.bar(x - w/2, vo, w, label="Optimizada", color="tab:blue")
        ax.bar(x + w/2, vd, w, label="Dijkstra", color="tab:orange")
        ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=7)
        ax.set_title(label); ax.legend(fontsize=7)
        if key == "loss":
            ax.set_ylim(0, 1)
    plt.tight_layout(); plt.savefig(f"{out}/metric_bars.png", dpi=110)


def plot_link_load(top, mrotas_aco, best_ga, mrotas_dj, out):
    """Per-link aggregate offered load for the optimised vs dijkstra routes."""
    n = top.n

    def loads(routes_idx):
        agg = {}
        for ri in np.atleast_1d(routes_idx):
            row = mrotas_aco[int(ri)-1]
            rota = [int(x) for x in row[:n] if x != 0]
            for u, v in zip(rota, rota[1:]):
                key = (min(u, v), max(u, v))
                agg[key] = agg.get(key, 0.0) + 0.0  # count distinct links
        return agg

    def offered(routes_idx, tds):
        agg = {}
        for app, ri in enumerate(np.atleast_1d(routes_idx)):
            row = mrotas_aco[int(ri)-1]
            rota = [int(x) for x in row[:n] if x != 0]
            flow = tds[app, 2]
            for u, v in zip(rota, rota[1:]):
                key = (min(u, v), max(u, v))
                agg[key] = agg.get(key, 0.0) + flow
        return agg

    tds = top.tds
    lo = offered(best_ga, tds)
    # dijkstra offered load
    ld = {}
    for a in range(top.napp):
        row = mrotas_dj[a]
        rota = [int(x) for x in row[:n] if x != 0]
        flow = tds[a, 2]
        for u, v in zip(rota, rota[1:]):
            key = (min(u, v), max(u, v))
            ld[key] = ld.get(key, 0.0) + flow

    links = sorted(set(lo) | set(ld))
    cap = 2.0
    over_opt = sum(1 for k in links if lo.get(k, 0) > cap + 1e-6)
    over_dj = sum(1 for k in links if ld.get(k, 0) > cap + 1e-6)

    fig, ax = plt.subplots(figsize=(12, 5))
    labels = [f"{u}-{v}" for u, v in links]
    x = np.arange(len(links)); w = 0.38
    ax.bar(x - w/2, [lo.get(k, 0) for k in links], w, label="Optimizada",
           color="tab:blue")
    ax.bar(x + w/2, [ld.get(k, 0) for k in links], w, label="Dijkstra",
           color="tab:orange")
    ax.axhline(cap, color="r", ls="--", label="Capacidade enlace (2 Mbps)")
    ax.set_xticks(x); ax.set_xticklabels(labels, rotation=90, fontsize=6)
    ax.set_ylabel("Vazão oferecida (Mbps)")
    ax.set_title(f"Uso da largura de banda por enlace\n"
                 f"enlaces sobre capacidade: optimizada={over_opt}, "
                 f"Dijkstra={over_dj}")
    ax.legend(fontsize=8)
    plt.tight_layout(); plt.savefig(f"{out}/link_load.png", dpi=110)


if __name__ == "__main__":
    main()