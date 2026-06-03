"""
Figure 11 (NEW) — Study flow (CONSORT-style) diagram.

373 records reviewed -> 90 met inclusion criteria -> 41 positive GI-PCR
(47 detections) vs 49 negative. Only cohort totals are known, so the single
exclusion box is left aggregated rather than inventing sub-reasons.
"""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from nature_style import set_style, save, COL15


def box(ax, x, y, w, h, text, fc="#EaF1F8", ec="#0072B2"):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                 boxstyle="round,pad=0.012,rounding_size=0.02",
                 linewidth=1.0, edgecolor=ec, facecolor=fc, zorder=2))
    ax.text(x, y, text, ha="center", va="center", fontsize=7.2, zorder=3)


def arrow(ax, x1, y1, x2, y2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color="#555555", lw=1.0))


def main():
    set_style()
    fig, ax = plt.subplots(figsize=(COL15, COL15 * 0.85))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    cx = 0.40
    box(ax, cx, 0.90, 0.52, 0.12,
        "373 HSCT recipients with medical\nrecords reviewed (2020–2025)")
    box(ax, cx, 0.62, 0.52, 0.12,
        "90 patients met inclusion criteria\n(GI multiplex-PCR > 100 d post-HSCT)")
    # exclusion (to the side)
    box(ax, 0.82, 0.76, 0.34, 0.14,
        "283 excluded\n(did not meet inclusion\ncriteria / lost to follow-up\n< 100 d post-HSCT)",
        fc="#F5F5F5", ec="#999999")
    # outcomes
    box(ax, 0.20, 0.28, 0.34, 0.14,
        "41 (46%) positive GI-PCR\n47 pathogen detections",
        fc="#FBEDE4", ec="#D55E00")
    box(ax, 0.62, 0.28, 0.30, 0.12,
        "49 (54%) negative\nGI-PCR", fc="#F5F5F5", ec="#999999")

    arrow(ax, cx, 0.84, cx, 0.68)
    arrow(ax, cx, 0.78, 0.65, 0.76)          # to exclusion
    arrow(ax, cx, 0.56, cx, 0.46)            # down from included
    ax.plot([cx, cx], [0.40, 0.40], lw=0)    # spacer
    arrow(ax, cx, 0.44, 0.20, 0.35)          # to positive
    arrow(ax, cx, 0.44, 0.62, 0.34)          # to negative

    save(fig, "Figure11_consort_flow")


if __name__ == "__main__":
    main()
