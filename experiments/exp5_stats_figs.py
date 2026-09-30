#!/usr/bin/env python3
"""Exp5: aggregate sweep results, statistical tests and paper figures."""
import os
import sys
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sdn.stats_tools import mean_ci95, wilcoxon_paired

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "..", "results")
FIG = os.path.join(BASE, "..", "paper", "figures")
os.makedirs(FIG, exist_ok=True)

ALGOS = ["dijkstra", "cspf", "qlearn", "aco_de", "aco_ga", "ilp_mcf"]
LABELS = {"dijkstra": "Dijkstra", "cspf": "CSPF", "qlearn": "Q-learning",
          "aco_de": "ACO+DE", "aco_ga": "ACO+GA", "ilp_mcf": "ILP (exact)"}
COLORS = {"dijkstra": "#999999", "cspf": "#1f77b4", "qlearn": "#9467bd",
          "aco_de": "#2ca02c", "aco_ga": "#d62728", "ilp_mcf": "black"}


def load_sweep():
    rows = []
    with open(os.path.join(RES, "sweep.jsonl")) as fh:
        for line in fh:
            try:
                rows.append(json.loads(line))
            except Exception:
                pass
    return pd.DataFrame(rows)


def main():
    df = load_sweep()
    df.to_csv(os.path.join(RES, "sweep.csv"), index=False)
    stoch = df[df["algo"].isin(["aco_ga", "aco_de", "qlearn"])]
    det = df[df["algo"].isin(["dijkstra", "cspf", "ilp_mcf"])]
    pools = df[df["algo"] == "ilp_pool"]

    topos = ["maia52", "gridcore", "waxman52", "germany50", "geant2012"]
    loads = sorted(df["load"].unique())

    # ---------------- summary table (mean over seeds / topo) --------------
    summary = []
    for topo in topos:
        for lf in loads:
            row = {"topo": topo, "load": lf}
            for algo in ALGOS:
                sub = df[(df.algo == algo) & (df.topo == topo) &
                         (df.load == lf)]
                if sub.empty:
                    continue
                if algo == "ilp_mcf":
                    r = sub.iloc[0]
                    row[f"{algo}_status"] = r["status"]
                    row[f"{algo}_maxu"] = r.get("Z_exact", np.nan)
                    row[f"{algo}_fo"] = r.get("fo_original", np.nan)
                elif sub["seed"].notna().any():
                    m, h = mean_ci95(sub["fo_original"])
                    mu, muh = mean_ci95(sub["max_util"])
                    row[f"{algo}_fo"] = m
                    row[f"{algo}_fo_ci"] = h
                    row[f"{algo}_maxu"] = mu
                    row[f"{algo}_maxu_ci"] = muh
                    row[f"{algo}_feas"] = float(sub["feasible"].mean())
                    row[f"{algo}_viol"] = float(
                        (sub["overloaded_links"] + sub["delay_violations"]
                         ).mean())
            summary.append(row)
    sm = pd.DataFrame(summary)
    sm.to_csv(os.path.join(RES, "summary.csv"), index=False)
    print(sm.to_string(index=False), flush=True)

    # ---------------- Wilcoxon paired tests ----------------
    tests = []
    for topo in topos:
        for lf in loads:
            ga = df[(df.algo == "aco_ga") & (df.topo == topo) &
                    (df.load == lf)].set_index("seed")["fo_original"]
            de = df[(df.algo == "aco_de") & (df.topo == topo) &
                    (df.load == lf)].set_index("seed")["fo_original"]
            ql = df[(df.algo == "qlearn") & (df.topo == topo) &
                    (df.load == lf)].set_index("seed")["fo_original"]
            common = ga.index.intersection(de.index)
            if len(common) >= 8:
                s, p = wilcoxon_paired(ga.loc[common], de.loc[common])
                tests.append({"topo": topo, "load": lf,
                              "pair": "aco_ga_vs_aco_de",
                              "mean_ga": ga.loc[common].mean(),
                              "mean_de": de.loc[common].mean(), "p": p})
            common = ga.index.intersection(ql.index)
            if len(common) >= 8:
                s, p = wilcoxon_paired(ga.loc[common], ql.loc[common])
                tests.append({"topo": topo, "load": lf,
                              "pair": "aco_ga_vs_qlearn",
                              "mean_ga": ga.loc[common].mean(),
                              "mean_ql": ql.loc[common].mean(), "p": p})
    pd.DataFrame(tests).to_csv(os.path.join(RES, "wilcoxon.csv"), index=False)

    # ---------------- Figure: load sweep violations ----------------
    for topo in topos:
        plt.figure(figsize=(7, 4.6))
        for algo in ["cspf", "qlearn", "aco_de", "aco_ga"]:
            xs, ys, es = [], [], []
            for lf in loads:
                sub = df[(df.algo == algo) & (df.topo == topo) &
                         (df.load == lf)]
                if sub.empty or sub["seed"].isna().all():
                    continue
                v = (sub["overloaded_links"] + sub["delay_violations"]).values
                m, h = mean_ci95(v)
                xs.append(lf); ys.append(m); es.append(h)
            if xs:
                plt.errorbar(xs, ys, yerr=es, marker="o", ms=4, lw=1.8,
                             label=LABELS[algo], color=COLORS[algo])
        # ILP feasibility certificate
        for lf in loads:
            sub = det[(det.algo == "ilp_mcf") & (det.topo == topo) &
                      (det.load == lf)]
            if not sub.empty and sub.iloc[0]["status"] != "Optimal":
                plt.axvspan(lf - 0.06, lf + 0.06, color="black", alpha=0.12)
        plt.xlabel("Load factor"); plt.ylabel("SLA violations (links+flows)")
        plt.title(f"Constraint violations vs load -- {topo}")
        plt.xticks(loads); plt.grid(alpha=0.3); plt.legend(fontsize=8)
        plt.tight_layout()
        plt.savefig(f"{FIG}/fig6_violations_{topo}.png", dpi=130)
        plt.close()

    # ---------------- Figure: max utilization sweep ----------------
    plt.figure(figsize=(7, 4.6))
    mk = {"cspf": "o", "qlearn": "s", "aco_de": "^", "aco_ga": "D"}
    for algo in ["cspf", "qlearn", "aco_de", "aco_ga"]:
        xs, ys, es = [], [], []
        for lf in loads:
            sub = df[(df.algo == algo) & (df.topo == "maia52") &
                     (df.load == lf)]
            if sub.empty or sub["seed"].isna().all():
                continue
            m, h = mean_ci95(sub["max_util"])
            xs.append(lf); ys.append(m); es.append(h)
        if xs:
            plt.errorbar(xs, ys, yerr=es, marker=mk[algo], ms=4, lw=1.8,
                         label=LABELS[algo], color=COLORS[algo])
    sub = det[(det.algo == "ilp_mcf") & (det.topo == "maia52")]
    if not sub.empty:
        zi = sub[["load", "Z_exact"]].dropna()
        if not zi.empty:
            plt.plot(zi["load"], zi["Z_exact"], "k--*", ms=9, lw=1.6,
                     label="ILP min-max (exact)")
    plt.axhline(1.0, color="red", ls=":", lw=1)
    plt.text(0.52, 1.02, "capacity limit", color="red", fontsize=8)
    plt.xlabel("Load factor"); plt.ylabel("Maximum link utilization")
    plt.title("Load balancing quality vs load -- maia52")
    plt.xticks(loads); plt.grid(alpha=0.3); plt.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig(f"{FIG}/fig7_maxutil_maia52.png", dpi=130)
    plt.close()

    # ---------------- Figure: optimality certification ----------------
    plt.figure(figsize=(7, 4.6))
    lf = 1.0
    for i, algo in enumerate(["dijkstra", "cspf", "qlearn", "aco_de",
                              "aco_ga"]):
        sub = df[(df.algo == algo) & (df.topo == "maia52") & (df.load == lf)]
        if sub.empty:
            continue
        if sub["seed"].notna().any():
            m, h = mean_ci95(sub["fo_original"])
            plt.errorbar(i, m, yerr=h, fmt="o", ms=8, color=COLORS[algo],
                         capsize=4, label=LABELS[algo])
        else:
            plt.plot(i, sub.iloc[0]["fo_original"], "s", ms=9,
                     color=COLORS[algo], label=LABELS[algo])
    po = pools[(pools.topo == "maia52") & (pools.load == lf)]
    if not po.empty:
        plt.axhline(po["fo_poolopt"].mean(), color="black", ls="--", lw=1.4,
                    label=f"Pool optimum (ILP) = {po['fo_poolopt'].mean():.0f}")
    plt.xticks(range(5), ["Dijkstra", "CSPF", "Q-learn", "ACO+DE", "ACO+GA"])
    plt.ylabel("Objective function FO"); plt.grid(alpha=0.3, axis="y")
    plt.title("Optimality certification -- maia52, nominal load (20 seeds)")
    plt.legend(fontsize=8, loc="lower right")
    plt.tight_layout()
    plt.savefig(f"{FIG}/fig8_optimality.png", dpi=130)
    plt.close()

    # ---------------- Figure: SRv6 state ----------------
    with open(os.path.join(RES, "srv6_state.json")) as fh:
        srv = json.load(fh)
    srvdf = pd.DataFrame(srv)
    topos3 = ["maia52", "waxman52", "gridcore", "germany50", "geant2012"]
    x = np.arange(len(topos3)); w = 0.36
    fig, ax = plt.subplots(figsize=(8, 4.6))
    of = [srvdf[(srvdf.topo == t) & (srvdf.algo == "cspf")]["of_total_rules"]
          .iloc[0] for t in topos3]
    sr = [srvdf[(srvdf.topo == t) & (srvdf.algo == "cspf")]["srv6_total_rules"]
          .iloc[0] for t in topos3]
    ax.bar(x - w / 2, of, w, label="OpenFlow (per-flow rules)",
           color="#1f77b4")
    ax.bar(x + w / 2, sr, w, label="SRv6 (headend rules only)",
           color="#d62728")
    for xi, (o, s) in enumerate(zip(of, sr)):
        ax.text(xi - w / 2, o + 1, str(o), ha="center", fontsize=9)
        ax.text(xi + w / 2, s + 1, str(s), ha="center", fontsize=9)
        ax.text(xi, max(o, s) + 7, f"{o/s:.1f}x", ha="center", fontsize=10,
                fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(topos3)
    ax.set_ylabel("Total data-plane rules (17 flows)")
    ax.set_title("Measured forwarding state: OpenFlow vs SRv6")
    ax.grid(alpha=0.3, axis="y"); ax.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig(f"{FIG}/fig9_srv6_state.png", dpi=130)
    plt.close()

    # ---------------- Figure: slice isolation (per topology) ----------------
    with open(os.path.join(RES, "slice_isolation.json")) as fh:
        sl = json.load(fh)
    sdf = pd.DataFrame(sl)
    if "topo" not in sdf.columns:
        sdf["topo"] = "maia52"
    slice_topos = [t for t in ["maia52", "germany50"] if t in set(sdf.topo)]
    for ti, st_name in enumerate(slice_topos):
        sub_all = sdf[sdf.topo == st_name]
        fig, axes = plt.subplots(1, 3, figsize=(12, 3.8))
        for ax, (col, name) in zip(axes, [
                ("urllc_delay_ms", "URLLC delay (ms)"),
                ("urllc_loss", "URLLC loss"),
                ("urllc_jitter_ms", "URLLC jitter (ms)")]):
            for algo, sty in [("ilp_opt", "-o"), ("dijkstra", "--s")]:
                sub = sub_all[sub_all.algo == algo].sort_values("background_mult")
                ax.plot(sub["background_mult"], sub[col], sty, ms=4, lw=1.8,
                        label="Optimized (ILP)" if algo == "ilp_opt"
                        else "Dijkstra")
            if col == "urllc_delay_ms":
                ax.axhline(150, color="red", ls=":", lw=1)
                ax.text(3.1, 158, "SLA 150 ms", color="red", fontsize=8)
            ax.set_xlabel("Background (eMBB+mMTC) multiplier")
            ax.set_title(name, fontsize=10)
            ax.grid(alpha=0.3); ax.legend(fontsize=7)
        fig.suptitle(f"URLLC slice isolation -- {st_name}", fontsize=11)
        plt.tight_layout()
        suffix = "" if st_name == "maia52" else f"_{st_name}"
        plt.savefig(f"{FIG}/fig10{suffix}_slice_isolation.png", dpi=130)
        plt.close()

    # ---------------- Figure: topologies ----------------
    from sdn.topologies import get_all_instances
    tops = get_all_instances()
    fig, axes = plt.subplots(1, len(tops), figsize=(3.6 * len(tops), 3.9))
    for ax, t in zip(axes, tops):
        xy = t.xy
        for i in range(t.n):
            for j in range(i + 1, t.n):
                if t.A[i, j] > 0:
                    ax.plot([xy[i, 0], xy[j, 0]], [xy[i, 1], xy[j, 1]],
                            color="0.8", lw=0.7, zorder=1)
        ax.scatter(xy[:, 0], xy[:, 1], s=10, c="k", zorder=2)
        tag = " (real)" if getattr(t, "real_geography", False) else ""
        ax.set_title(f"{t.name}{tag} ({t.n} nodes, {int(t.A.sum()//2)} links)",
                     fontsize=9)
        ax.set_xticks([]); ax.set_yticks([]); ax.set_aspect("equal")
    plt.tight_layout()
    plt.savefig(f"{FIG}/fig11_topologies.png", dpi=130)
    plt.close()

    print("STATS+FIGS DONE", flush=True)


if __name__ == "__main__":
    main()