"""
Figure 4 — Relative contribution of each pathogen category over time.

Original: 100% stacked composition by time interval.
Improvement: clean 100% stacked bars with within-bin percentages labelled and
the per-bin denominator (n) annotated above each bar, so the reader is not
misled by intervals built on very few detections.
"""
import matplotlib.pyplot as plt
from nature_style import (set_style, save, COL15, CATEGORY_COLORS,
                          CATEGORY_ORDER, TIME_LABELS)
from _binning import load_binned


def main():
    set_style()
    df = load_binned()
    cats = [c for c in CATEGORY_ORDER if c in df["category"].unique()]
    counts = (df.groupby(["time_bin", "category"], observed=False)
                .size().unstack(fill_value=0).reindex(columns=cats, fill_value=0))
    counts = counts.reindex(TIME_LABELS)
    totals = counts.sum(axis=1)
    pct = counts.div(totals.replace(0, 1), axis=0) * 100

    fig, ax = plt.subplots(figsize=(COL15, COL15 * 0.6))
    bottom = [0] * len(pct)
    x = range(len(pct))
    for cat in cats:
        vals = pct[cat].values
        ax.bar(x, vals, bottom=bottom, color=CATEGORY_COLORS[cat],
               edgecolor="white", linewidth=0.5, width=0.7, label=cat)
        for i, (v, b) in enumerate(zip(vals, bottom)):
            if v >= 8:
                ax.text(i, b + v / 2, f"{v:.0f}", ha="center", va="center",
                        fontsize=6.5, color="white", fontweight="bold")
        bottom = [b + v for b, v in zip(bottom, vals)]

    for i, t in enumerate(totals.values):
        ax.text(i, 101.5, f"n={int(t)}", ha="center", va="bottom",
                fontsize=6.5, color="#333333")

    ax.set_xticks(list(x))
    ax.set_xticklabels(TIME_LABELS)
    ax.set_xlabel("Days after HSCT")
    ax.set_ylabel("Share of detections (%)")
    ax.set_ylim(0, 100)
    ax.legend(title="Pathogen type", loc="center left",
              bbox_to_anchor=(1.01, 0.5), handlelength=1.0,
              handleheight=1.0, borderpad=0.4, labelspacing=0.35)
    fig.tight_layout()
    save(fig, "Figure4_relative_contribution")


if __name__ == "__main__":
    main()
