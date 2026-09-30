#!/usr/bin/env python3
"""Exp9: emit LaTeX tables with Portuguese headers -> results/tables/*_pt.tex."""
import os
import sys
import json
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sdn.stats_tools import mean_ci95

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "..", "results")
OUTT = os.path.join(RES, "tables")
os.makedirs(OUTT, exist_ok=True)


def load_sweep():
    rows = []
    with open(os.path.join(RES, "sweep.jsonl")) as fh:
        for line in fh:
            rows.append(json.loads(line))
    return pd.DataFrame(rows)


def main():
    df = load_sweep()
    st = lambda a, t, lf: df[(df.algo == a) & (df.topo == t) & (df.load == lf)]

    # ---------------- SRv6 ----------------
    with open(os.path.join(RES, "srv6_state.json")) as fh:
        sdf = pd.DataFrame(json.load(fh))
    lines = [r"\begin{tabular}{@{}lrrrrr@{}}", r"\toprule",
             r"Topologia & Regras OF & Máx/nó OF & Regras SRv6 & Máx SIDs & Redução\\",
             r"\midrule"]
    for topo in ["maia52", "waxman52", "gridcore", "germany50", "geant2012"]:
        row = sdf[(sdf.topo == topo) & (sdf.algo == "cspf")].iloc[0]
        lines.append(
            f"{topo} & {int(row['of_total_rules'])} & "
            f"{int(row['of_max_node_rules'])} & {int(row['srv6_total_rules'])} & "
            f"{int(row['max_segment_list'])} & {row['reduction_factor']:.1f}$\\times$\\\\")
    lines += [r"\bottomrule", r"\end{tabular}"]
    open(os.path.join(OUTT, "table_srv6_pt.tex"), "w").write("\n".join(lines) + "\n")

    # ---------------- tempos ----------------
    lines = [r"\begin{tabular}{@{}lrr@{}}", r"\toprule",
             r"Método & Tempo mediano (s) & Modelo\\", r"\midrule"]
    rt = {"Dijkstra": ("dijkstra", "determinístico"),
          "CSPF": ("cspf", "determinístico"),
          "ACO+AG": ("aco_ga", "estocástico"),
          "ACO+DE": ("aco_de", "estocástico"),
          "Q-learning": ("qlearn", "aprendizado"),
          "ILP-P (pool)": ("ilp_pool", "exato"),
          "ILP-L (MCF)": ("ilp_mcf", "exato")}
    for name, (algo, model) in rt.items():
        sub = df[df.algo == algo]
        if sub.empty:
            continue
        lines.append(f"{name} & {sub['time_s'].median():.1f} & {model}\\\\")
    lines += [r"\bottomrule", r"\end{tabular}"]
    open(os.path.join(OUTT, "table_time_pt.tex"), "w").write("\n".join(lines) + "\n")

    # ---------------- FO nominal ----------------
    lines = [r"\begin{tabular}{@{}lrrrrr@{}}", r"\toprule",
             r"Topologia & Dijkstra & CSPF & Q-learn & ACO+DE & ACO+AG\\",
             r"\midrule"]
    for topo in ["maia52", "waxman52", "gridcore", "germany50", "geant2012"]:
        vals = []
        empty = False
        for algo in ["dijkstra", "cspf", "qlearn", "aco_de", "aco_ga"]:
            sub = st(algo, topo, 1.0)
            if sub.empty:
                empty = True
                break
            if algo in ("dijkstra", "cspf"):
                vals.append(f"{sub.iloc[0]['fo_original']:.0f}")
            else:
                m, h = mean_ci95(sub["fo_original"])
                vals.append(f"{m:.0f}$\\pm${h:.0f}")
        if empty:
            continue
        lines.append(f"{topo} & " + " & ".join(vals) + r"\\")
    lines += [r"\bottomrule", r"\end{tabular}"]
    open(os.path.join(OUTT, "table_fo_pt.tex"), "w").write("\n".join(lines) + "\n")

    # ---------------- violações ----------------
    lines = [r"\begin{tabular}{@{}lrrrrr@{}}", r"\toprule",
             r"Carga & Dijkstra & CSPF & Q-learn & ACO+DE & ACO+AG\\",
             r"\midrule"]
    for lf in [1.0, 1.25, 1.5]:
        vals = []
        for algo in ["dijkstra", "cspf", "qlearn", "aco_de", "aco_ga"]:
            sub = st(algo, "maia52", lf)
            if sub["seed"].isna().all():
                vals.append(f"{int(sub.iloc[0]['overloaded_links'])}+"
                            f"{int(sub.iloc[0]['delay_violations'])}")
            else:
                viol = (sub["overloaded_links"] + sub["delay_violations"])
                m, h = mean_ci95(viol)
                vals.append(f"{m:.1f}$\\pm${h:.1f}")
        lines.append(f"{lf}$\\times$ & " + " & ".join(vals) + r"\\")
    lines += [r"\bottomrule", r"\end{tabular}"]
    open(os.path.join(OUTT, "table_viol_pt.tex"), "w").write("\n".join(lines) + "\n")

    print("TABLES PT DONE")


if __name__ == "__main__":
    main()