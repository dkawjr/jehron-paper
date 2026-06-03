"""
Figure 5 — Time to first positive GI-PCR by GVHD status (Kaplan-Meier).

IMPORTANT
---------
The original Figure 5 in the workbook is a pasted Stata screenshot, and the
per-patient survival data are NOT in the provided files. This script is ready
to generate a publication-quality KM figure the moment a per-patient dataset
is supplied as:

    data/kaplan_meier_patients.csv

with columns:
    time   -- days from HSCT day 100 to first positive GI-PCR OR to censoring
    event  -- 1 = positive GI-PCR (event), 0 = censored
    gvhd   -- GVHD status: 1/0, or "GVHD"/"No GVHD"

If that file is absent, this script writes a template and exits cleanly.

The KM estimator, log-rank test, and number-at-risk table are implemented with
numpy/scipy only (no extra dependencies). The plot shows the cumulative
incidence of a positive GI-PCR (1 - survival), matching the manuscript's intent.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from nature_style import set_style, save, COL1, DATA

GROUP_COLORS = {"GVHD": "#0072B2", "No GVHD": "#D55E00"}
PATIENTS = DATA / "kaplan_meier_patients.csv"            # real data goes here
TEMPLATE = DATA / "kaplan_meier_patients_TEMPLATE.csv"   # example layout only


def write_template():
    pd.DataFrame({"time": [350, 900, 600], "event": [1, 0, 1],
                  "gvhd": ["No GVHD", "GVHD", "GVHD"]}).to_csv(TEMPLATE, index=False)
    print("  [Figure 5] data/kaplan_meier_patients.csv not found.")
    print(f"  -> Wrote an example layout to {TEMPLATE.name}.")
    print("     Provide the real per-patient data (one row per patient) as")
    print("     data/kaplan_meier_patients.csv and re-run this script.")


def km_estimate(time, event):
    """Return step points (t, survival) starting at (0, 1.0)."""
    order = np.argsort(time)
    time, event = time[order], event[order]
    uniq = np.unique(time[event == 1])
    ts, surv = [0.0], [1.0]
    s = 1.0
    for t in uniq:
        at_risk = np.sum(time >= t)
        d = np.sum((time == t) & (event == 1))
        if at_risk > 0:
            s *= (1 - d / at_risk)
        ts.append(t)
        surv.append(s)
    return np.array(ts), np.array(surv)


def logrank(time, event, group):
    """Two-group log-rank test -> chi2, p."""
    groups = np.unique(group)
    g1 = group == groups[0]
    times = np.unique(time[event == 1])
    O1 = E1 = V = 0.0
    for t in times:
        at_risk = time >= t
        n = at_risk.sum()
        n1 = (at_risk & g1).sum()
        d = ((time == t) & (event == 1)).sum()
        d1 = ((time == t) & (event == 1) & g1).sum()
        if n > 1:
            E1 += d * n1 / n
            V += d * (n1 / n) * (1 - n1 / n) * (n - d) / (n - 1)
        O1 += d1
    chi2 = (O1 - E1) ** 2 / V if V > 0 else 0.0
    p = stats.chi2.sf(chi2, df=1)
    return chi2, p


def main():
    set_style()
    if not PATIENTS.exists():
        write_template()
        return
    df = pd.read_csv(PATIENTS)
    if len(df) < 5:
        print("  [Figure 5] need real per-patient data (>=5 rows). Skipping.")
        return

    # normalize gvhd labels
    df["gvhd"] = df["gvhd"].map(lambda v: "GVHD" if str(v) in ("1", "GVHD", "Yes")
                                else "No GVHD")
    time = df["time"].to_numpy(float)
    event = df["event"].to_numpy(int)
    group = df["gvhd"].to_numpy(str)

    fig, ax = plt.subplots(figsize=(COL1, COL1 * 0.85))
    risk_times = np.linspace(0, time.max(), 6)
    risk_rows = {}
    for g in ["GVHD", "No GVHD"]:
        m = group == g
        t, s = km_estimate(time[m], event[m])
        ci = 1 - s   # cumulative incidence
        ax.step(t, ci, where="post", color=GROUP_COLORS[g], lw=1.5,
                label=f"{g} (n={m.sum()})")
        risk_rows[g] = [int(np.sum(time[m] >= rt)) for rt in risk_times]

    _, p = logrank(time, event, group)
    ptxt = "log-rank p < 0.001" if p < 0.001 else f"log-rank p = {p:.3f}"
    ax.text(0.03, 0.95, ptxt, transform=ax.transAxes, va="top", fontsize=7)

    ax.set_xlabel("Days after HSCT")
    ax.set_ylabel("Cumulative incidence of positive GI-PCR")
    ax.set_ylim(0, 1)
    ax.set_xlim(0, time.max())
    ax.legend(loc="lower right")

    # number-at-risk table beneath the axes
    ytab = -0.20
    ax.text(0, ytab + 0.05, "No. at risk", transform=ax.transAxes,
            fontsize=6.5, fontweight="bold")
    for j, g in enumerate(["GVHD", "No GVHD"]):
        ax.text(-0.02, ytab - j * 0.06, g, transform=ax.transAxes,
                fontsize=6.5, ha="right", color=GROUP_COLORS[g])
        for rt, val in zip(risk_times, risk_rows[g]):
            xfrac = rt / time.max()
            ax.text(xfrac, ytab - j * 0.06, str(val), transform=ax.transAxes,
                    fontsize=6.5, ha="center", color=GROUP_COLORS[g])

    fig.tight_layout()
    save(fig, "Figure5_kaplan_meier")


if __name__ == "__main__":
    main()
