"""
Figure 13 (NEW) — Composite B: risk factors for late positive GI-PCR.

a: unadjusted odds ratios for all candidate factors (the screen; exploratory).
b: adjusted Cox hazard ratios for the retained variables (the model).
Standard univariate -> multivariable forest pairing.

NOTE: panel a shows ORs (cross-sectional) and panel b shows HRs (time-to-event)
because the per-patient time-to-event data needed for unadjusted HRs were not
available; the two panels are therefore different estimands, labelled as such.
"""
import pandas as pd
import matplotlib.pyplot as plt
from nature_style import set_style, save, COL2, DATA
from _panels import draw_forest
from _stats import odds_ratio


def main():
    set_style()
    # panel a: unadjusted ORs
    t1 = pd.read_csv(DATA / "table1_risk_factors.csv")
    or_rows = []
    for _, r in t1.iterrows():
        est, lo, hi = odds_ratio(r.exp_pos, r.exp_neg, r.ref_pos, r.ref_neg)
        or_rows.append({"label": f"{r.exposed} vs {r.reference}",
                        "est": est, "lo": lo, "hi": hi})
    or_rows.sort(key=lambda d: d["est"])

    # panel b: adjusted Cox HRs
    t2 = pd.read_csv(DATA / "table2_cox_model.csv")
    cox_rows = []
    for _, r in t2.iterrows():
        cox_rows.append({"label": r.level, "est": r.hr,
                         "lo": r.ci_low, "hi": r.ci_high,
                         "is_ref": bool(r.is_reference)})

    fig = plt.figure(figsize=(COL2, COL2 * 0.55))
    gs = fig.add_gridspec(1, 2, width_ratios=[1, 1], wspace=0.75)

    ax_a = fig.add_subplot(gs[0])
    ax_a.set_xlim(0.08, 60)
    ax_a.set_xticks([0.1, 0.5, 1, 2, 8])
    ax_a.set_xticklabels(["0.1", "0.5", "1", "2", "8"])
    draw_forest(ax_a, or_rows,
                "Unadjusted odds ratio (95% CI)")
    ax_a.set_title("Unadjusted association", fontsize=7.5, pad=6)

    ax_b = fig.add_subplot(gs[1])
    ax_b.set_xlim(0.2, 16)
    ax_b.set_xticks([0.25, 0.5, 1, 2, 4, 8])
    ax_b.set_xticklabels(["0.25", "0.5", "1", "2", "4", "8"])
    draw_forest(ax_b, cox_rows,
                "Adjusted hazard ratio (95% CI)")
    ax_b.set_title("Adjusted Cox model", fontsize=7.5, pad=6)

    for ax, lab in ((ax_a, "a"), (ax_b, "b")):
        ax.text(-0.45, 1.04, lab, transform=ax.transAxes, fontsize=10,
                fontweight="bold", va="bottom", ha="right")

    save(fig, "Figure13_composite_riskfactors")


if __name__ == "__main__":
    main()
