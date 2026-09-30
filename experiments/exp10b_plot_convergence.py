#!/usr/bin/env python3
"""Exp10b: plot FO convergence curves (EN -> figures/, PT -> figures/pt/).

View spans the full objective range (like the original thesis figure) so the
rise is visible in context, and contrasts the pool-AUGMENTED selector
(paper protocol) against the UN-augmented one (constructive-seeding ablation).
"""
import os
import sys
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sdn.stats_tools import mean_ci95

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "..", "results")

with open(os.path.join(RES, "convergence.json")) as fh:
    conv = json.load(fh)
with open(os.path.join(RES, "convergence_noaugment.json")) as fh:
    conv_na = json.load(fh)

TOPO = "maia52"


def mean_band(curves):
    arr = np.array(curves)
    gens = np.arange(1, arr.shape[1] + 1)
    means = arr.mean(axis=0)
    lows, highs = [], []
    for g in range(arr.shape[1]):
        m, h = mean_ci95(arr[:, g])
        lows.append(m - h)
        highs.append(m + h)
    return gens, means, np.array(lows), np.array(highs)


def render(lang):
    L = {
        "en": dict(title="Objective-function convergence -- maia52 "
                         "(nominal load, 20 seeds)",
                   xlabel="Generation",
                   ylabel="Best objective function (FO)",
                   ga="ACO + GA (augmented pool)",
                   de="ACO + DE (augmented pool)",
                   na="ACO + GA (no pool augmentation)",
                   pool="Certified pool optimum (ILP-P)",
                   djk="Dijkstra"),
        "pt": dict(title="Convergência da função objetivo -- maia52 "
                         "(carga nominal, 20 seeds)",
                   xlabel="Geração",
                   ylabel="Melhor função objetivo (FO)",
                   ga="ACO + AG (pool ampliado)",
                   de="ACO + DE (pool ampliado)",
                   na="ACO + AG (sem ampliação do pool)",
                   pool="Ótimo do pool certificado (ILP-P)",
                   djk="Dijkstra"),
    }[lang]
    fig, ax = plt.subplots(figsize=(7, 4.6))

    g, m, lo, hi = mean_band(conv[TOPO]["ga"])
    ax.plot(g, m, "-", color="#d62728", lw=2.2, label=L["ga"])
    ax.fill_between(g, lo, hi, color="#d62728", alpha=0.12)

    g, m, lo, hi = mean_band(conv[TOPO]["de"])
    ax.plot(g, m, "--", color="#2ca02c", lw=2.0, label=L["de"])
    ax.fill_between(g, lo, hi, color="#2ca02c", alpha=0.10)

    g, m, lo, hi = mean_band(conv_na[TOPO]["ga"])
    ax.plot(g, m, ":", color="#666666", lw=1.9, label=L["na"])
    ax.fill_between(g, lo, hi, color="#666666", alpha=0.10)

    ax.axhline(132, color="black", ls=":", lw=1.4, label=L["pool"])
    ax.axhline(120, color="black", ls="-.", lw=1.4, label=L["djk"])

    ax.set_xlabel(L["xlabel"], fontsize=10)
    ax.set_ylabel(L["ylabel"], fontsize=10)
    ax.set_title(L["title"], fontsize=10)
    ax.set_xlim(1, 300)
    ax.set_ylim(112.5, 133.2)          # full span, thesis-figure style
    ax.set_xticks([0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300])
    ax.grid(alpha=0.35, ls=":")
    ax.legend(fontsize=8, loc="lower right")
    plt.tight_layout()
    outdir = os.path.join(BASE, "..", "paper", "figures",
                          "" if lang == "en" else "pt")
    fig.savefig(os.path.join(outdir, "fig2_convergence.png"), dpi=130)
    plt.close(fig)
    print(f"saved {outdir} fig2_convergence.png ({lang})")


render("en")
render("pt")
print("CONVERGENCE PLOTS DONE")