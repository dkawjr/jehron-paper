"""
Figure 2 — Enteric pathogen burden over time, by category.

Original: normalized line/bar of each pathogen type as a proportion of its own
total (hard to read sample size).
Improvement: stacked bars of ABSOLUTE detection counts per standardized time
bin, coloured by category. This shows both (i) the declining total infection
burden over time and (ii) the shifting composition, without hiding the small
denominators. Counts are printed on each segment.
"""
import matplotlib.pyplot as plt
from nature_style import (set_style, save, COL1, CATEGORY_COLORS,
                          CATEGORY_ORDER, TIME_LABELS)
from _binning import load_binned


def main():
    set_style()
    df = load_binned()
    cats = [c for c in CATEGORY_ORDER if c in df["category"].unique()]
    tab = (df.groupby(["time_bin", "category"], observed=False)
             .size().unstack(fill_value=0).reindex(columns=cats, fill_value=0))
    tab = tab.reindex(TIME_LABELS)

    fig, ax = plt.subplots(figsize=(COL1, COL1 * 0.78))
    bottom = [0] * len(tab)
    x = range(len(tab))
    for cat in cats:
        vals = tab[cat].values
        ax.bar(x, vals, bottom=bottom, color=CATEGORY_COLORS[cat],
               edgecolor="white", linewidth=0.5, width=0.7, label=cat)
        for i, (v, b) in enumerate(zip(vals, bottom)):
            if v > 0:
                ax.text(i, b + v / 2, str(int(v)), ha="center", va="center",
                        fontsize=6.5, color="white", fontweight="bold")
        bottom = [b + v for b, v in zip(bottom, vals)]

    totals = tab.sum(axis=1).values
    for i, t in enumerate(totals):
        ax.text(i, t + 0.4, f"n={int(t)}", ha="center", va="bottom",
                fontsize=6.5, color="#333333")

    ax.set_xticks(list(x))
    ax.set_xticklabels(TIME_LABELS)
    ax.set_xlabel("Days after HSCT")
    ax.set_ylabel("Positive detections")
    ax.set_ylim(0, max(totals) * 1.18)
    ax.legend(title="Pathogen type", loc="upper right",
              handlelength=1.0, handleheight=1.0, borderpad=0.4)
    fig.tight_layout()
    save(fig, "Figure2_pathogen_category_over_time")


if __name__ == "__main__":
    main()
