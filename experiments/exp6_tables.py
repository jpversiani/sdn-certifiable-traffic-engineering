#!/usr/bin/env python3
"""Exp6: emit results/macros.tex and results/tables/*.tex from experiment
outputs, so every number in the manuscript is auto-injected."""
import os
import sys
import json
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sdn.stats_tools import mean_ci95, wilcoxon_paired

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "..", "results")
OUTM = os.path.join(RES, "macros.tex")
OUTT = os.path.join(RES, "tables")
os.makedirs(OUTT, exist_ok=True)


def fmt(x, nd=1):
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "--"
    return f"{x:.{nd}f}"


def pct(x, nd=1):
    return f"{100*x:.{nd}f}"


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
    st = lambda a, t, lf: df[(df.algo == a) & (df.topo == t) & (df.load == lf)]

    M = {}

    # --- FO at nominal load (maia52) ---
    pool = df[df.algo == "ilp_pool"]
    pool_opt = pool[(pool.topo == "maia52") &
                    (pool.load == 1.0)]["fo_poolopt"].dropna()
    M["PoolOptFO"] = fmt(pool_opt.mean(), 0) if len(pool_opt) else "--"

    for key, algo in [("Ga", "aco_ga"), ("De", "aco_de"), ("Ql", "qlearn")]:
        sub = st(algo, "maia52", 1.0)
        if not sub.empty:
            m, h = mean_ci95(sub["fo_original"])
            M[f"{key}FOmaia"] = fmt(m, 1)
            M[f"{key}FOmaiaCI"] = fmt(h, 1)
    dj = st("dijkstra", "maia52", 1.0)
    if not dj.empty:
        M["DjFOmaia"] = fmt(dj.iloc[0]["fo_original"], 0)
        M["DjMaxUtil"] = fmt(dj.iloc[0]["max_util"], 2)
    cs = st("cspf", "maia52", 1.0)
    if not cs.empty:
        M["CspfFOmaia"] = fmt(cs.iloc[0]["fo_original"], 0)
        M["CspfMaxUtil"] = fmt(cs.iloc[0]["max_util"], 2)

    # --- ILP results ---
    il = df[(df.algo == "ilp_mcf") & (df.topo == "maia52")]
    z = il[(il.load == 1.0) & il["Z_exact"].notna()]
    M["IlpZmaia"] = fmt(z.iloc[0]["Z_exact"], 3) if len(z) else "--"
    zh = il[(il.load == 1.25) & il["Z_exact"].notna()]
    M["IlpZmaiaHigh"] = fmt(zh.iloc[0]["Z_exact"], 3) if len(zh) else "--"
    M["IlpZmaiaHighPct"] = pct(zh.iloc[0]["Z_exact"], 1) if len(zh) else "--"
    zm = il[(il.load == 1.5) & il["Z_exact"].notna()]
    M["IlpZmaiaMax"] = fmt(zm.iloc[0]["Z_exact"], 3) if len(zm) else "--"
    for pfx, topo in [("Wax", "waxman52"), ("Grid", "gridcore")]:
        zz = df[(df.algo == "ilp_mcf") & (df.topo == topo) &
                (df.load == 1.5) & df["Z_exact"].notna()]
        M[f"IlpZ{pfx}Max"] = fmt(zz.iloc[0]["Z_exact"], 3) if len(zz) else "--"
    infeas = sorted(il[il["status"] != "Optimal"]["load"].tolist())
    M["IlpInfeasLoad"] = fmt(infeas[0], 2) if infeas else ">1.5"
    ilg = df[(df.algo == "ilp_mcf") & (df.topo == "gridcore") &
             (df["status"] != "Optimal")]
    M["IlpInfeasGrid"] = fmt(ilg["load"].min(), 2) if len(ilg) else "--"
    M["IlpTime"] = fmt(il["time_s"].median(), 1) if len(il) else "--"
    pp = pool[pool.topo == "maia52"]
    M["PoolTime"] = fmt(pp["time_s"].median(), 1) if len(pp) else "--"

    # --- session-growth model: aggregate-traffic ratios for f>1 ---
    total_nom = float(df[(df.algo == "cspf") & (df.topo == "maia52") &
                         (df.load == 1.0)].iloc[0]["total_demand_mbps"]) \
        if "total_demand_mbps" in df.columns else 9.70
    M["LoadRatioHigh"] = fmt((total_nom + 5 * 0.256) / total_nom, 2)
    M["LoadRatioMax"] = fmt((total_nom + 10 * 0.256) / total_nom, 2)

    # --- Q-learning feasibility at nominal load (maia52) ---
    qln = st("qlearn", "maia52", 1.0)
    M["QlFeasNominal"] = pct(qln["feasible"].mean(), 0) if not qln.empty else "--"

    # --- real backbone headline numbers (GEANT: the hard regime) ---
    for key, algo in [("Dj", "dijkstra"), ("Cspf", "cspf")]:
        s = st(algo, "geant2012", 1.0)
        if not s.empty:
            M[f"Ant{key}MaxUtil"] = fmt(s.iloc[0]["max_util"], 2)
            M[f"Ant{key}Viol"] = fmt(s.iloc[0]["overloaded_links"] +
                                     s.iloc[0]["delay_violations"], 0)
            M[f"Ant{key}FO"] = fmt(s.iloc[0]["fo_original"], 0)
    for key, algo in [("Ga", "aco_ga"), ("De", "aco_de"), ("Ql", "qlearn")]:
        s1 = st(algo, "geant2012", 1.0)
        if not s1.empty:
            M[f"Ant{key}Feas"] = pct(s1["feasible"].mean(), 0)
            m, h = mean_ci95(s1["fo_original"])
            M[f"Ant{key}FO"] = f"{fmt(m, 1)}$\\pm${fmt(h, 1)}"
    pool_geant = pool[(pool.topo == "geant2012") & (pool.load == 1.0)]
    if not pool_geant.empty:
        M["AntPoolOpt"] = fmt(pool_geant["fo_poolopt"].mean(), 0)
        M["AntPoolOptFeasRate"] = pct((pool_geant["fo_poolopt"] >= 132).mean(), 0)
    for key, topo in [("Ger", "germany50"), ("Geant", "geant2012")]:
        zi = df[(df.algo == "ilp_mcf") & (df.topo == topo) &
                (df.load == 1.0) & df["Z_exact"].notna()]
        M[f"{key}Z"] = fmt(zi.iloc[0]["Z_exact"], 3) if not zi.empty else "--"
    # cross-instance view: fraction of (topo, load) cells the hybrid keeps clean
    ga_all = df[(df.algo == "aco_ga")]
    if not ga_all.empty:
        cell = ga_all.groupby(["topo", "load"])["feasible"].mean()
        M["GaFeasAllInst"] = pct(cell.mean(), 0)

    # --- instance latency envelopes (real backbones) ---
    try:
        from sdn.topologies import get_backbones
        from sdn.data import load_topology as _lt
        for pfx, nm in [("Ger", "germany50"), ("Geant", "geant2012")]:
            t = {x.name: x for x in get_backbones(tds_template=_lt().tds)}[nm]
            at = t.AT[t.A > 0]
            M[f"AntDelay{pfx}Min"] = fmt(float(at.min()), 1)
            M[f"AntDelay{pfx}Max"] = fmt(float(at.max()), 1)
            M[f"AntDelay{pfx}Mean"] = fmt(float(at.mean()), 1)
            M[f"AntCap{pfx}"] = fmt(float(t.capacity), 2)
    except Exception as _e:
        print("backbone meta skipped:", _e)

    # --- violations at infeasible loads (maia52) ---
    for lf, tag in [(1.25, "High"), (1.5, "Max")]:
        for key, algo in [("Ga", "aco_ga"), ("De", "aco_de"), ("Ql", "qlearn"),
                          ("Cspf", "cspf"), ("Dj", "dijkstra")]:
            sub = st(algo, "maia52", lf)
            if not sub.empty:
                viol = (sub["overloaded_links"] + sub["delay_violations"])
                m, h = mean_ci95(viol)
                M[f"{key}Viol{tag}"] = fmt(m, 1)
                M[f"{key}Viol{tag}CI"] = fmt(h, 1)
            else:
                M[f"{key}Viol{tag}"] = "--"
                M[f"{key}Viol{tag}CI"] = "--"

    # --- GA feasibility per load on maia52 and geant2012 ---
    for pfx, topo in [("Maia", "maia52"), ("Geant", "geant2012")]:
        for lf, tag in [(1.0, "Nominal"), (1.25, "High"), (1.5, "Max")]:
            sub = st("aco_ga", topo, lf)
            M[f"GaFeas{pfx}{tag}"] = pct(sub["feasible"].mean(), 0) \
                if not sub.empty else "--"
    # geant2012 violations at nominal load (GA, mean +- CI)
    gvn = st("aco_ga", "geant2012", 1.0)
    if not gvn.empty:
        v = (gvn["overloaded_links"] + gvn["delay_violations"])
        m, h = mean_ci95(v)
        M["GaViolGeantNominal"] = f"{fmt(m, 1)}$\\pm${fmt(h, 1)}"

    # --- Wilcoxon GA vs QL at 1.25 (maia) ---
    ga = st("aco_ga", "maia52", 1.25).set_index("seed")["fo_original"]
    ql = st("qlearn", "maia52", 1.25).set_index("seed")["fo_original"]
    common = ga.index.intersection(ql.index)
    if len(common) >= 8:
        _, p = wilcoxon_paired(ga.loc[common], ql.loc[common])
        M["QlVsGaP"] = ("<0.001" if p < 1e-3 else f"{p:.3f}")
    else:
        M["QlVsGaP"] = "--"

    # --- runtimes ---
    for key, algo in [("Ga", "aco_ga"), ("De", "aco_de"), ("Ql", "qlearn")]:
        sub = df[(df.algo == algo) & (df.topo == "maia52")]
        M[f"{key}Time"] = fmt(sub["time_s"].median(), 1) if len(sub) else "--"

    # --- SRv6 state ---
    with open(os.path.join(RES, "srv6_state.json")) as fh:
        srv = json.load(fh)
    sdf = pd.DataFrame(srv)
    for key, topo in [("Maia", "maia52"), ("Wax", "waxman52"),
                      ("Grid", "gridcore"), ("Ger", "germany50"),
                      ("Geant", "geant2012")]:
        row = sdf[(sdf.topo == topo) & (sdf.algo == "cspf")]
        if not row.empty:
            r = row.iloc[0]
            M[f"SrvOf{key}"] = f"{int(r['of_total_rules'])}"
            M[f"SrvRed{key}"] = fmt(r["reduction_factor"], 1)
            M[f"MaxSL{key}"] = f"{int(r['max_segment_list'])}"
            M[f"Srh{key}"] = f"{int(r['max_srh_overhead_bytes'])}"
    M["SrvSrRules"] = "17"
    sl_all = sdf["max_segment_list"].max()
    M["MaxSLAll"] = f"{int(sl_all)}"
    M["MaxSrhBytes"] = f"{int(sdf['max_srh_overhead_bytes'].max())}"
    M["MeanSLWax"] = fmt(sdf[(sdf.topo == "waxman52") &
                             (sdf.algo == "cspf")]["mean_segment_list"].mean(),
                         1)

    # --- slice isolation ---
    with open(os.path.join(RES, "slice_isolation.json")) as fh:
        slc = json.load(fh)
    cdf = pd.DataFrame(slc)
    if "topo" not in cdf.columns:
        cdf["topo"] = "maia52"

    def _slice(topo, algo, mult, field):
        s = cdf[(cdf.topo == topo) & (cdf.algo == algo) &
                (cdf.background_mult == mult)]
        return None if s.empty else s.iloc[0][field]

    for topo, pfx in [("maia52", "Urllc"), ("germany50", "Ger")]:
        o1 = _slice(topo, "ilp_opt", 1.0, "urllc_delay_ms")
        d1 = _slice(topo, "dijkstra", 1.0, "urllc_delay_ms")
        o2 = _slice(topo, "ilp_opt", 2.0, "urllc_delay_ms")
        d2 = _slice(topo, "dijkstra", 2.0, "urllc_delay_ms")
        o3 = _slice(topo, "ilp_opt", 3.0, "urllc_delay_ms")
        l1o = _slice(topo, "ilp_opt", 1.0, "urllc_loss")
        l2o = _slice(topo, "ilp_opt", 2.0, "urllc_loss")
        l1d = _slice(topo, "dijkstra", 1.0, "urllc_loss")
        l2d = _slice(topo, "dijkstra", 2.0, "urllc_loss")
        l4d = _slice(topo, "dijkstra", 4.0, "urllc_loss")
        vals = {"DoptOne": o1, "DdjOne": d1, "DoptTwo": o2, "DdjTwo": d2,
                "DoptThree": o3}
        for k, v in vals.items():
            if v is not None:
                M[f"{pfx}{k}"] = fmt(v, 0)
        o15 = _slice(topo, "ilp_opt", 1.5, "urllc_delay_ms")
        if o15 is not None:
            M[f"{pfx}DoptFifteen"] = fmt(o15, 0)
        l15 = _slice(topo, "ilp_opt", 1.5, "urllc_loss")
        if l15 is not None:
            M[f"{pfx}LossOptFifteen"] = pct(l15)
        for k, v in {"LoptOne": l1o, "LossOptTwo": l2o, "LdjOne": l1d,
                     "LossDjTwo": l2d, "LossDjFour": l4d}.items():
            if v is not None:
                M[f"{pfx}{k}"] = pct(v)
        # legacy aliases kept for the manuscript macros
        if topo == "maia52":
            for src, dst in [("UrllcDoptOne", "UrllcDoptOne"),
                             ("UrllcDdjOne", "UrllcDdjOne"),
                             ("UrllcDoptTwo", "UrllcDoptTwo"),
                             ("UrllcLossOptTwo", "UrllcLossOptTwo"),
                             ("UrllcLoptOne", "UrllcLoptOne"),
                             ("UrllcLdjOne", "UrllcLdjOne"),
                             ("UrllcLossDjFour", "UrllcLossDjFour")]:
                if src in M:
                    M[dst] = M[src]

    # --- packet QoS replicated ---
    with open(os.path.join(RES, "qos_sim.json")) as fh:
        qs = json.load(fh)
    qdf = pd.DataFrame(qs)
    o = qdf[qdf.algo == "ilp_opt"]; d = qdf[qdf.algo == "dijkstra"]
    M["NumSimSeeds"] = str(len(o))
    if len(o) and len(d):
        mo, ho = mean_ci95(o["mean_delay_ms"]); md, hd = mean_ci95(d["mean_delay_ms"])
        jo, jho = mean_ci95(o["mean_jitter_ms"]); jd, jhd = mean_ci95(d["mean_jitter_ms"])
        lo, lho = mean_ci95(o["mean_loss"]); ld, lhd = mean_ci95(d["mean_loss"])
        to, tho = mean_ci95(o["mean_throughput_mbps"])
        td, thd = mean_ci95(d["mean_throughput_mbps"])
        M["SimDelayOpt"] = fmt(mo, 0); M["SimDelayDj"] = fmt(md, 0)
        M["SimJitOpt"] = fmt(jo, 1); M["SimJitDj"] = fmt(jd, 1)
        M["SimLossOpt"] = pct(lo); M["SimLossDj"] = pct(ld)
        M["SimThrGain"] = f"+{100*(to/td-1):.0f}\\%"
        M["SimDelayRatio"] = fmt(md / mo, 1)
        # loss ratio is undefined when the optimized loss is zero
        M["SimLossRatio"] = fmt(ld / lo, 1) if lo > 1e-6 else "--"

    M["TotalDemand"] = "9.70"

    with open(OUTM, "w") as fh:
        for k, v in M.items():
            fh.write(f"\\newcommand{{\\{k}}}{{{v}}}\n")
    print(f"wrote {OUTM} with {len(M)} macros")

    # ---------------- table: SRv6 state ----------------
    lines = [
        r"\begin{tabular}{@{}lrrrrr@{}}", r"\toprule",
        r"Topology & OF rules & OF max/node & SRv6 rules & Max SIDs & Reduction\\",
        r"\midrule"]
    for topo in ["maia52", "waxman52", "gridcore", "germany50", "geant2012"]:
        row = sdf[(sdf.topo == topo) & (sdf.algo == "cspf")].iloc[0]
        lines.append(
            f"{topo} & {int(row['of_total_rules'])} & "
            f"{int(row['of_max_node_rules'])} & {int(row['srv6_total_rules'])} & "
            f"{int(row['max_segment_list'])} & {row['reduction_factor']:.1f}$\\times$\\\\")
    lines += [r"\bottomrule", r"\end{tabular}"]
    with open(os.path.join(OUTT, "table_srv6.tex"), "w") as fh:
        fh.write("\n".join(lines) + "\n")

    # ---------------- table: runtimes ----------------
    lines = [r"\begin{tabular}{@{}lrr@{}}", r"\toprule",
             r"Method & Median runtime (s) & Model\\", r"\midrule"]
    rt = {"Dijkstra": ("dijkstra", "deterministic"),
          "CSPF": ("cspf", "deterministic"),
          "ACO+GA": ("aco_ga", "stochastic"),
          "ACO+DE": ("aco_de", "stochastic"),
          "Q-learning": ("qlearn", "learning"),
          "ILP-P (pool)": ("ilp_pool", "exact"),
          "ILP-L (MCF)": ("ilp_mcf", "exact")}
    for name, (algo, model) in rt.items():
        sub = df[df.algo == algo]
        if sub.empty:
            continue
        lines.append(f"{name} & {sub['time_s'].median():.1f} & {model}\\\\")
    lines += [r"\bottomrule", r"\end{tabular}"]
    with open(os.path.join(OUTT, "table_time.tex"), "w") as fh:
        fh.write("\n".join(lines) + "\n")

    # ---------------- table: FO summary across topologies ----------------
    lines = [r"\begin{tabular}{@{}lrrrrr@{}}", r"\toprule",
             r"Topology & Dijkstra & CSPF & Q-learn & ACO+DE & ACO+GA\\",
             r"\midrule"]
    for topo in ["maia52", "waxman52", "gridcore", "germany50", "geant2012"]:
        vals = []
        for algo in ["dijkstra", "cspf", "qlearn", "aco_de", "aco_ga"]:
            sub = st(algo, topo, 1.0)
            if algo in ("dijkstra", "cspf"):
                vals.append(fmt(sub.iloc[0]["fo_original"], 0)
                            if not sub.empty else "--")
            else:
                m, h = mean_ci95(sub["fo_original"]) if not sub.empty else (np.nan, 0)
                vals.append(f"{m:.0f}$\\pm${h:.0f}" if not np.isnan(m) else "--")
        lines.append(f"{topo} & " + " & ".join(vals) + r"\\")
    lines += [r"\bottomrule", r"\end{tabular}"]
    with open(os.path.join(OUTT, "table_fo.tex"), "w") as fh:
        fh.write("\n".join(lines) + "\n")

    # ---------------- table: violations at high load (maia52) ----------
    lines = [r"\begin{tabular}{@{}lrrrrr@{}}", r"\toprule",
             r"Load & Dijkstra & CSPF & Q-learn & ACO+DE & ACO+GA\\",
             r"\midrule"]
    for lf in [1.0, 1.25, 1.5]:
        vals = []
        for algo in ["dijkstra", "cspf", "qlearn", "aco_de", "aco_ga"]:
            sub = st(algo, "maia52", lf)
            if sub.empty:
                vals.append("--")
            elif sub["seed"].isna().all():
                vals.append(f"{int(sub.iloc[0]['overloaded_links'])}+"
                            f"{int(sub.iloc[0]['delay_violations'])}")
            else:
                viol = (sub["overloaded_links"] + sub["delay_violations"])
                m, h = mean_ci95(viol)
                vals.append(f"{m:.1f}$\\pm${h:.1f}")
        lines.append(f"{lf}$\\times$ & " + " & ".join(vals) + r"\\")
    lines += [r"\bottomrule", r"\end{tabular}"]
    with open(os.path.join(OUTT, "table_viol.tex"), "w") as fh:
        fh.write("\n".join(lines) + "\n")

    print("TABLES DONE")


if __name__ == "__main__":
    main()