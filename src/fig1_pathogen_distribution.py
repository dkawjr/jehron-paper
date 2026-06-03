"""
Figure 1 — Distribution of pathogens among positive GI-PCR tests.

Original: pie/bar of pathogen percentages.
Improvement: horizontal bar chart sorted by frequency, coloured by pathogen
category, with n and % labels. Bars encode magnitude far more accurately than
a pie, and the category colouring conveys the bacterial/viral/parasitic split
in the same view.
"""
import pandas as pd
import matplotlib.pyplot as plt
from nature_style import (set_style, save, COL1, PATHOGEN_COLORS,
                          CATEGORY_COLORS, DATA)


def main():
    set_style()
    df = pd.read_csv(DATA / "positive_detections.csv")
    n_total = len(df)

    counts = (df.groupby(["pathogen", "category"])
                .size().reset_index(name="n")
                .sort_values("n", ascending=True))   # ascending -> largest on top in barh
    counts["pct"] = 100 * counts["n"] / n_total
    colors = [PATHOGEN_COLORS.get(p, "#999999") for p in counts["pathogen"]]

    fig, ax = plt.subplots(figsize=(COL1, COL1 * 0.95))
    y = range(len(counts))
    ax.barh(y, counts["n"], color=colors, edgecolor="white", linewidth=0.4, height=0.78)

    ax.set_yticks(list(y))
    ax.set_yticklabels(counts["pathogen"], fontstyle="italic")
    ax.set_xlabel(f"Detections (n = {n_total})")
    ax.set_xlim(0, counts["n"].max() * 1.18)

    for i, (n, pct) in enumerate(zip(counts["n"], counts["pct"])):
        ax.text(n + counts["n"].max() * 0.02, i, f"{n} ({pct:.0f}%)",
                va="center", ha="left", fontsize=6.5, color="#222222")

    # category legend
    handles = [plt.Rectangle((0, 0), 1, 1, color=c) for c in CATEGORY_COLORS.values()]
    ax.legend(handles, CATEGORY_COLORS.keys(), title="Pathogen type",
              loc="lower right", handlelength=1.0, handleheight=1.0,
              borderpad=0.4, labelspacing=0.3)

    ax.tick_params(axis="y", length=0)
    fig.tight_layout()
    save(fig, "Figure1_pathogen_distribution")


if __name__ == "__main__":
    main()
