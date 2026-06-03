"""
Figure 14 (NEW) — Positivity and pathogen composition with Wilson 95% CIs.

Point estimates with proper interval estimates make the uncertainty explicit on
this small cohort, instead of presenting bare percentages. Top row: overall
positivity (41/90). Lower rows: share of each pathogen category among the 47
detections, each with a Wilson 95% CI.
"""
import matplotlib.pyplot as plt
from nature_style import set_style, save, COL15, CATEGORY_COLORS, CATEGORY_ORDER
from _panels import load_detections
from _stats import wilson_ci


def main():
    set_style()
    df = load_detections()
    n_det = len(df)

    rows = [("Any positive GI-PCR", 41, 90, "#333333")]
    for cat in CATEGORY_ORDER:
        k = int((df["category"] == cat).sum())
        if k == 0:
            continue
        rows.append((f"{cat} (of detections)", k, n_det, CATEGORY_COLORS[cat]))

    fig, ax = plt.subplots(figsize=(COL15, COL15 * 0.5))
    for i, (label, k, n, color) in enumerate(rows):
        y = len(rows) - 1 - i
        p, lo, hi = wilson_ci(k, n)
        ax.plot([lo * 100, hi * 100], [y, y], color=color, lw=1.6, zorder=2)
        ax.plot(p * 100, y, "o", color=color, markersize=6,
                markeredgecolor="white", markeredgewidth=0.6, zorder=3)
        ax.text(102, y, f"{p*100:.0f}% ({lo*100:.0f}–{hi*100:.0f})  {k}/{n}",
                va="center", fontsize=6.5)

    ax.axhline(len(rows) - 1.5, color="#DDDDDD", lw=0.6)
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([r[0] for r in rows][::-1])
    ax.set_xlim(0, 100)
    ax.set_xlabel("Percentage (Wilson 95% CI)")
    ax.tick_params(axis="y", length=0)
    ax.set_xlim(0, 140)
    ax.set_xticks([0, 20, 40, 60, 80, 100])
    save(fig, "Figure14_wilson_proportions")


if __name__ == "__main__":
    main()
