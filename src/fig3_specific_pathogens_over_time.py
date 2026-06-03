"""
Figure 3 — Specific pathogens over time.

Original: normalized lines per pathogen (11 series, hard to parse).
Improvement: stacked bars of absolute counts per standardized time bin, with
segments coloured by individual pathogen (shaded within category, so the
bacterial/viral/parasitic grouping is still legible). Makes E. coli's
persistence across all intervals immediately visible.
"""
import matplotlib.pyplot as plt
from nature_style import (set_style, save, COL15, PATHOGEN_COLORS,
                          PATHOGEN_ORDER, TIME_LABELS)
from _binning import load_binned


def main():
    set_style()
    df = load_binned()
    paths = [p for p in PATHOGEN_ORDER if p in df["pathogen"].unique()]
    tab = (df.groupby(["time_bin", "pathogen"], observed=False)
             .size().unstack(fill_value=0).reindex(columns=paths, fill_value=0))
    tab = tab.reindex(TIME_LABELS)

    fig, ax = plt.subplots(figsize=(COL15, COL15 * 0.62))
    bottom = [0] * len(tab)
    x = range(len(tab))
    for p in paths:
        vals = tab[p].values
        ax.bar(x, vals, bottom=bottom, color=PATHOGEN_COLORS[p],
               edgecolor="white", linewidth=0.5, width=0.7, label=p)
        bottom = [b + v for b, v in zip(bottom, vals)]

    totals = tab.sum(axis=1).values
    for i, t in enumerate(totals):
        ax.text(i, t + 0.4, f"n={int(t)}", ha="center", va="bottom",
                fontsize=6.5, color="#333333")

    ax.set_xticks(list(x))
    ax.set_xticklabels(TIME_LABELS)
    ax.set_xlabel("Days after HSCT")
    ax.set_ylabel("Positive detections")
    ax.set_ylim(0, max(totals) * 1.15)

    leg = ax.legend(title="Pathogen", loc="center left",
                    bbox_to_anchor=(1.01, 0.5), handlelength=1.0,
                    handleheight=1.0, borderpad=0.4, labelspacing=0.35)
    for txt in leg.get_texts():
        txt.set_fontstyle("italic")
    fig.tight_layout()
    save(fig, "Figure3_specific_pathogens_over_time")


if __name__ == "__main__":
    main()
