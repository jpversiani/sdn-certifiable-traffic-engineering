#!/usr/bin/env python3
"""Exp8: regenerates the paper figures with Portuguese labels -> figures/pt/."""
import os
import sys
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sdn.stats_tools import mean_ci95
from sdn.topologies import get_all_instances as get_topologies
from sdn.empirical_data import APPLICATIONS_DATA

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "..", "results")
FIG = os.path.join(BASE, "..", "paper", "figures", "pt")
os.makedirs(FIG, exist_ok=True)

ALGOS = ["dijkstra", "cspf", "qlearn", "aco_de", "aco_ga", "ilp_mcf"]
LABELS = {"dijkstra": "Dijkstra", "cspf": "CSPF", "qlearn": "Q-learning",
          "aco_de": "ACO+DE", "aco_ga": "ACO+GA", "ilp_mcf": "ILP (exato)"}
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


def bench_dataframe():
    df = pd.DataFrame(APPLICATIONS_DATA, columns=[
        "app_id", "type", "orig", "dest", "target_thr_kbps", "opt_thr_kbps",
        "dj_thr_kbps", "opt_loss_pct", "dj_loss_pct", "target_delay_s",
        "opt_delay_s", "dj_delay_s", "opt_jitter_s", "dj_jitter_s"])
    return df


def main():
    df = load_sweep()
    loads = sorted(df["load"].unique())
    det = df[df["algo"].isin(["dijkstra", "cspf", "ilp_mcf"])]
    pools = df[df["algo"] == "ilp_pool"]

    # ---- fig6: violações ----
    for topo in ["maia52", "gridcore", "waxman52", "germany50", "geant2012"]:
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
        plt.xlabel("Fator de carga"); plt.ylabel("Violações de SLA (enlaces + fluxos)")
        plt.title(f"Violações de restrição versus carga -- {topo}")
        plt.xticks(loads); plt.grid(alpha=0.3); plt.legend(fontsize=8)
        plt.tight_layout()
        plt.savefig(f"{FIG}/fig6_violations_{topo}.png", dpi=130)
        plt.close()

    # ---- fig7: utilização máxima ----
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
    zi = sub[["load", "Z_exact"]].dropna()
    if not zi.empty:
        plt.plot(zi["load"], zi["Z_exact"], "k--*", ms=9, lw=1.6,
                 label="ILP min-max (exato)")
    plt.axhline(1.0, color="red", ls=":", lw=1)
    plt.text(0.52, 1.02, "limite de capacidade", color="red", fontsize=8)
    plt.xlabel("Fator de carga"); plt.ylabel("Utilização máxima dos enlaces")
    plt.title("Qualidade de balanceamento versus carga -- maia52")
    plt.xticks(loads); plt.grid(alpha=0.3); plt.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig(f"{FIG}/fig7_maxutil_maia52.png", dpi=130)
    plt.close()

    # ---- fig8: certificação de otimalidade ----
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
                    label=f"Ótimo do pool (ILP) = {po['fo_poolopt'].mean():.0f}")
    plt.xticks(range(5), ["Dijkstra", "CSPF", "Q-learn", "ACO+DE", "ACO+GA"])
    plt.ylabel("Função objetivo FO"); plt.grid(alpha=0.3, axis="y")
    plt.title("Certificação de otimalidade -- maia52, carga nominal (20 seeds)")
    plt.legend(fontsize=8, loc="lower right")
    plt.tight_layout()
    plt.savefig(f"{FIG}/fig8_optimality.png", dpi=130)
    plt.close()

    # ---- fig9: estado SRv6 ----
    with open(os.path.join(RES, "srv6_state.json")) as fh:
        srv = json.load(fh)
    srvdf = pd.DataFrame(srv)
    topos3 = ["maia52", "waxman52", "gridcore", "germany50", "geant2012"]
    x = np.arange(len(topos3)); w = 0.36
    fig, ax = plt.subplots(figsize=(7, 4.6))
    of = [srvdf[(srvdf.topo == t) & (srvdf.algo == "cspf")]["of_total_rules"]
          .iloc[0] for t in topos3]
    sr = [srvdf[(srvdf.topo == t) & (srvdf.algo == "cspf")]["srv6_total_rules"]
          .iloc[0] for t in topos3]
    ax.bar(x - w / 2, of, w, label="OpenFlow (regras por fluxo)",
           color="#1f77b4")
    ax.bar(x + w / 2, sr, w, label="SRv6 (regras só no headend)",
           color="#d62728")
    for xi, (o, s) in enumerate(zip(of, sr)):
        ax.text(xi - w / 2, o + 1, str(o), ha="center", fontsize=9)
        ax.text(xi + w / 2, s + 1, str(s), ha="center", fontsize=9)
        ax.text(xi, max(o, s) + 7, f"{o/s:.1f}x", ha="center", fontsize=10,
                fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(topos3)
    ax.set_ylabel("Total de regras no plano de dados (17 fluxos)")
    ax.set_title("Estado de encaminhamento medido: OpenFlow versus SRv6")
    ax.grid(alpha=0.3, axis="y"); ax.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig(f"{FIG}/fig9_srv6_state.png", dpi=130)
    plt.close()

    # ---- fig10: isolamento de fatias (por topologia) ----
    with open(os.path.join(RES, "slice_isolation.json")) as fh:
        sl = json.load(fh)
    sdf = pd.DataFrame(sl)
    if "topo" not in sdf.columns:
        sdf["topo"] = "maia52"
    for st_name in [t for t in ["maia52", "germany50"] if t in set(sdf.topo)]:
        sub_all = sdf[sdf.topo == st_name]
        fig, axes = plt.subplots(1, 3, figsize=(12, 3.8))
        for ax, (col, name) in zip(axes, [
                ("urllc_delay_ms", "Atraso URLLC (ms)"),
                ("urllc_loss", "Perda URLLC"),
                ("urllc_jitter_ms", "Jitter URLLC (ms)")]):
            for algo, sty in [("ilp_opt", "-o"), ("dijkstra", "--s")]:
                sub = sub_all[sub_all.algo == algo].sort_values("background_mult")
                ax.plot(sub["background_mult"], sub[col], sty, ms=4, lw=1.8,
                        label="Otimizada (ILP)" if algo == "ilp_opt"
                        else "Dijkstra")
            if col == "urllc_delay_ms":
                ax.axhline(150, color="red", ls=":", lw=1)
                ax.text(3.1, 158, "SLA 150 ms", color="red", fontsize=8)
            ax.set_xlabel("Multiplicador do tráfego de fundo (eMBB+mMTC)")
            ax.set_title(name, fontsize=10)
            ax.grid(alpha=0.3); ax.legend(fontsize=7)
        fig.suptitle(f"Isolamento da fatia URLLC -- {st_name}", fontsize=11)
        plt.tight_layout()
        suffix = "" if st_name == "maia52" else f"_{st_name}"
        plt.savefig(f"{FIG}/fig10{suffix}_slice_isolation.png", dpi=130)
        plt.close()

    # ---- fig11: topologias ----
    tops = get_topologies()
    fig, axes = plt.subplots(1, len(tops), figsize=(3.6 * len(tops), 3.9))
    for ax, t in zip(axes, tops):
        xy = t.xy
        for i in range(t.n):
            for j in range(i + 1, t.n):
                if t.A[i, j] > 0:
                    ax.plot([xy[i, 0], xy[j, 0]], [xy[i, 1], xy[j, 1]],
                            color="0.8", lw=0.7, zorder=1)
        ax.scatter(xy[:, 0], xy[:, 1], s=10, c="k", zorder=2)
        ax.set_title(f"{t.name} ({t.n} nós, {int(t.A.sum()//2)} enlaces)",
                     fontsize=10)
        ax.set_xticks([]); ax.set_yticks([]); ax.set_aspect("equal")
    plt.tight_layout()
    plt.savefig(f"{FIG}/fig11_topologies.png", dpi=130)
    plt.close()

    # ---- fig3: bancada Mininet/D-ITG (dados empíricos) ----
    bdf = bench_dataframe()
    apps = bdf["app_id"].values
    fig, axs = plt.subplots(2, 2, figsize=(11, 7.5), dpi=300)
    bw = 0.38
    x = np.arange(len(apps))
    lab_o, lab_d, lab_n = "Otimizada (ACO+AG)", "Baseline (Dijkstra)", "Demanda nominal"

    ax = axs[0, 0]
    ax.bar(x - bw/2, bdf["opt_thr_kbps"], width=bw, label=lab_o, color="#2e7d32", alpha=0.9)
    ax.bar(x + bw/2, bdf["dj_thr_kbps"], width=bw, label=lab_d, color="#c62828", alpha=0.9)
    ax.plot(x, bdf["target_thr_kbps"], color="black", ls="--", lw=1.2,
            label=lab_n, marker="o", markersize=3)
    ax.set_xticks(x); ax.set_xticklabels(apps, fontsize=8)
    ax.set_xlabel("Identificador da aplicação"); ax.set_ylabel("Vazão (kbps)")
    ax.set_title("(a) Vazão recebida em Mininet/D-ITG")
    ax.legend(loc="upper right", fontsize=8); ax.grid(True, ls=":", alpha=0.5)

    ax = axs[0, 1]
    ax.bar(x - bw/2, bdf["opt_loss_pct"], width=bw, label=lab_o, color="#2e7d32", alpha=0.9)
    ax.bar(x + bw/2, bdf["dj_loss_pct"], width=bw, label=lab_d, color="#c62828", alpha=0.9)
    ax.set_xticks(x); ax.set_xticklabels(apps, fontsize=8)
    ax.set_xlabel("Identificador da aplicação"); ax.set_ylabel("Perda de pacotes (%)")
    ax.set_title("(b) Perda de pacotes em Mininet/D-ITG")
    ax.legend(loc="upper right", fontsize=8); ax.grid(True, ls=":", alpha=0.5)

    ax = axs[1, 0]
    ax.bar(x - bw/2, bdf["opt_delay_s"] * 1000.0, width=bw, label=lab_o, color="#2e7d32", alpha=0.9)
    ax.bar(x + bw/2, bdf["dj_delay_s"] * 1000.0, width=bw, label=lab_d, color="#c62828", alpha=0.9)
    ax.set_yscale("log")
    ax.set_xticks(x); ax.set_xticklabels(apps, fontsize=8)
    ax.set_xlabel("Identificador da aplicação"); ax.set_ylabel("Atraso fim-a-fim (ms, escala log)")
    ax.set_title("(c) Atraso fim-a-fim (impacto do bufferbloat em Mininet)")
    ax.legend(loc="upper right", fontsize=8); ax.grid(True, ls=":", alpha=0.5)

    ax = axs[1, 1]
    ax.bar(x - bw/2, bdf["opt_jitter_s"] * 1000.0, width=bw, label=lab_o, color="#2e7d32", alpha=0.9)
    ax.bar(x + bw/2, bdf["dj_jitter_s"] * 1000.0, width=bw, label=lab_d, color="#c62828", alpha=0.9)
    ax.set_xticks(x); ax.set_xticklabels(apps, fontsize=8)
    ax.set_xlabel("Identificador da aplicação"); ax.set_ylabel("Jitter (ms)")
    ax.set_title("(d) Jitter em Mininet/D-ITG")
    ax.legend(loc="upper right", fontsize=8); ax.grid(True, ls=":", alpha=0.5)

    plt.tight_layout()
    fig.savefig(f"{FIG}/fig3_mininet_results.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

    print("FIGURES PT DONE")


if __name__ == "__main__":
    main()