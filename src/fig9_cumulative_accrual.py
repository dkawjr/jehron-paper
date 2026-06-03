"""
Figure 9 (NEW) — Cumulative accrual of detections over time, by category.

A step plot of the cumulative number of detections versus days after HSCT, one
line per pathogen category. Uses the exact event days (no binning), so it shows
the timing differences directly: parasitic and viral curves plateau early while
the bacterial curve keeps climbing. A rug at the bottom marks individual events.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from nature_style import (set_style, save, COL15, CATEGORY_COLORS,
                          CATEGORY_ORDER, DATA)


def main():
    set_style()
    df = pd.read_csv(DATA / "positive_detections.csv").sort_values("day_post_sct")
    cats = [c for c in CATEGORY_ORDER if c in df["category"].unique()
            and c != "Other"]

    fig, ax = plt.subplots(figsize=(COL15, COL15 * 0.6))
    for cat in cats:
        d = np.sort(df.loc[df["category"] == cat, "day_post_sct"].values)
        x = np.concatenate([[0], d, [df["day_post_sct"].max()]])
        y = np.concatenate([[0], np.arange(1, len(d) + 1), [len(d)]])
        ax.step(x, y, where="post", color=CATEGORY_COLORS[cat], lw=1.6,
                label=f"{cat} (n={len(d)})")
        # rug of individual events
        ax.plot(d, np.full_like(d, -0.6, dtype=float), "|",
                color=CATEGORY_COLORS[cat], markersize=4, alpha=0.7)

    ax.set_xlabel("Days after HSCT")
    ax.set_ylabel("Cumulative detections")
    ax.set_xlim(0, df["day_post_sct"].max() * 1.02)
    ax.set_ylim(-1.2, None)
    ax.axvline(400, color="#CCCCCC", lw=0.75, ls=":", zorder=0)
    ax.text(400, ax.get_ylim()[1], " 400 d", fontsize=6, color="#999999",
            va="top", ha="left")
    ax.legend(loc="lower right")
    fig.tight_layout()
    save(fig, "Figure9_cumulative_accrual")


if __name__ == "__main__":
    main()
