"""
Figure 7 (NEW) — Forest plot of unadjusted odds ratios (Table 1 risk factors).

Turns the dense Table 1 into a visual: for each binary factor we reconstruct the
2x2 table (positive vs negative GI-PCR) and compute the unadjusted odds ratio
with a 95% CI (Woolf method; Haldane-Anscombe 0.5 correction for any zero cell).
Effect direction and precision are immediately readable; the OR=1 line marks no
association. This complements the adjusted Cox forest (Figure 6).
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from nature_style import set_style, save, COL15, DATA


def odds_ratio(a, b, c, d):
    """a=exp_pos, b=exp_neg, c=ref_pos, d=ref_neg. Returns OR, lo, hi."""
    if 0 in (a, b, c, d):
        a, b, c, d = a + 0.5, b + 0.5, c + 0.5, d + 0.5
    or_ = (a * d) / (b * c)
    se = np.sqrt(1 / a + 1 / b + 1 / c + 1 / d)
    lo = np.exp(np.log(or_) - 1.96 * se)
    hi = np.exp(np.log(or_) + 1.96 * se)
    return or_, lo, hi


def main():
    set_style()
    df = pd.read_csv(DATA / "table1_risk_factors.csv")
    res = []
    for _, r in df.iterrows():
        or_, lo, hi = odds_ratio(r.exp_pos, r.exp_neg, r.ref_pos, r.ref_neg)
        res.append((f"{r.exposed} vs {r.reference}", or_, lo, hi))
    res = pd.DataFrame(res, columns=["label", "or", "lo", "hi"])
    res = res.sort_values("or").reset_index(drop=True)

    fig, ax = plt.subplots(figsize=(COL15, COL15 * 0.62))
    for i, row in res.iterrows():
        sig = row.lo > 1 or row.hi < 1
        color = "#0072B2" if sig else "#888888"
        ax.plot([row.lo, row.hi], [i, i], color=color, lw=1.4, zorder=2)
        ax.plot(row["or"], i, "o", color=color, markersize=5, zorder=3)
        ax.text(20, i, f"{row['or']:.2f} ({row.lo:.2f}–{row.hi:.2f})",
                va="center", fontsize=6.3, ha="left")

    ax.axvline(1.0, color="#999999", lw=0.75, ls="--", zorder=1)
    ax.set_yticks(range(len(res)))
    ax.set_yticklabels(res["label"])
    ax.set_xscale("log")
    ax.set_xticks([0.1, 0.25, 0.5, 1, 2, 4, 8])
    ax.set_xticklabels(["0.1", "0.25", "0.5", "1", "2", "4", "8"])
    ax.set_xlim(0.08, 60)
    ax.set_xlabel("Unadjusted odds ratio for positive GI-PCR (95% CI)")
    ax.tick_params(axis="y", length=0)
    ax.set_title("Unadjusted associations with positive GI-PCR > 100 d post-HSCT",
                 fontsize=7.5, pad=8)
    fig.tight_layout()
    save(fig, "Figure7_forest_table1_unadjusted")


if __name__ == "__main__":
    main()
