"""
Figure 10 (NEW) — Every enteric detection by exact day post-HSCT.

A purely descriptive display: one dot per detection (n=47), one row per
pathogen, coloured by category. With a sample this small the honest approach is
to show every data point rather than bin it. This is consistent with the paper's
descriptive temporal findings and makes no inferential claim.

(An earlier draft added a median/IQR panel with a Kruskal-Wallis test of timing
differences between categories; that test was non-significant (p=0.29) and is
deliberately omitted so nothing here alters the paper's reported results.)
"""
import matplotlib.pyplot as plt
from nature_style import set_style, save, COL2, CATEGORY_COLORS
from _panels import load_detections, draw_dotstrip


def main():
    set_style()
    df = load_detections()
    fig, ax = plt.subplots(figsize=(COL2, COL2 * 0.42))
    draw_dotstrip(ax, df)

    handles = [plt.Line2D([0], [0], marker="o", linestyle="", markersize=6,
                          markerfacecolor=c, markeredgecolor="white",
                          label=k)
               for k, c in CATEGORY_COLORS.items()]
    ax.legend(handles=handles, title="Pathogen type", loc="center left",
              bbox_to_anchor=(1.01, 0.5), handletextpad=0.3, borderpad=0.4)
    fig.tight_layout()
    save(fig, "Figure10_event_dotstrip")


if __name__ == "__main__":
    main()
