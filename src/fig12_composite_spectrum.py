"""
Figure 12 (NEW) — Composite A: microbiologic spectrum and its timing.

a: overall pathogen frequency (the spectrum).
b: every detection by exact day, per pathogen (the timing).
c: normalized cumulative accrual by category (the early-cluster vs
   late-persistence summary).
One figure that carries the whole descriptive story.
"""
import matplotlib.pyplot as plt
from nature_style import set_style, save, COL2
from _panels import load_detections, draw_pathogen_bar, draw_dotstrip, draw_accrual


def main():
    set_style()
    df = load_detections()
    fig = plt.figure(figsize=(COL2, COL2 * 0.72))
    gs = fig.add_gridspec(2, 2, height_ratios=[1.7, 1.1],
                          width_ratios=[1.0, 1.5], hspace=0.5, wspace=0.45)

    ax_a = fig.add_subplot(gs[0, 0])
    draw_pathogen_bar(ax_a, df)

    ax_b = fig.add_subplot(gs[0, 1])
    draw_dotstrip(ax_b, df)

    ax_c = fig.add_subplot(gs[1, :])
    draw_accrual(ax_c, df, normalized=True)

    for ax, lab, x in ((ax_a, "a", -0.30), (ax_b, "b", -0.13), (ax_c, "c", -0.07)):
        ax.text(x, 1.03, lab, transform=ax.transAxes, fontsize=10,
                fontweight="bold", va="bottom", ha="right")

    save(fig, "Figure12_composite_spectrum")


if __name__ == "__main__":
    main()
