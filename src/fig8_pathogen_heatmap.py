"""
Figure 8 (NEW) — Pathogen x time heatmap.

An elegant, compact alternative to the stacked bars: a matrix of detection
counts (pathogen rows, time-bin columns), pathogens grouped by category and
ordered by frequency. Sequential shading + cell annotations make temporal
patterns (e.g. E. coli persisting late; parasites confined early) pop out.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from nature_style import (set_style, save, COL1, PATHOGEN_ORDER, TIME_LABELS,
                          CATEGORY_COLORS)
from _binning import load_binned

PATH_CATEGORY = {
    "E. coli": "Bacteria", "C. difficile": "Bacteria", "Yersinia": "Bacteria",
    "Salmonella": "Bacteria", "Norovirus": "Virus", "Adenovirus": "Virus",
    "Rotavirus": "Virus", "Sapovirus": "Virus", "Cryptosporidium": "Parasite",
    "Giardia": "Parasite", "Other": "Other",
}


def main():
    set_style()
    df = load_binned()
    paths = [p for p in PATHOGEN_ORDER if p in df["pathogen"].unique()]
    tab = (df.groupby(["pathogen", "time_bin"], observed=False)
             .size().unstack(fill_value=0)
             .reindex(index=paths, columns=TIME_LABELS, fill_value=0))
    M = tab.values

    cmap = LinearSegmentedColormap.from_list("blues", ["#FFFFFF", "#08306B"])
    fig, ax = plt.subplots(figsize=(COL1, COL1 * 1.05))
    im = ax.imshow(M, cmap=cmap, aspect="auto", vmin=0, vmax=M.max())

    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            v = M[i, j]
            if v > 0:
                ax.text(j, i, str(int(v)), ha="center", va="center",
                        fontsize=6.5,
                        color="white" if v > M.max() * 0.55 else "#222222")

    ax.set_xticks(range(len(TIME_LABELS)))
    ax.set_xticklabels(TIME_LABELS, rotation=0)
    ax.set_yticks(range(len(paths)))
    ax.set_yticklabels(paths, fontstyle="italic")
    ax.set_xlabel("Days after HSCT")

    # colour the y-tick labels by category
    for tick, p in zip(ax.get_yticklabels(), paths):
        tick.set_color(CATEGORY_COLORS[PATH_CATEGORY[p]])

    ax.tick_params(length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)

    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label("Detections", fontsize=7)
    cbar.outline.set_linewidth(0.5)
    cbar.ax.tick_params(labelsize=6, length=2)

    fig.tight_layout()
    save(fig, "Figure8_pathogen_time_heatmap")


if __name__ == "__main__":
    main()
