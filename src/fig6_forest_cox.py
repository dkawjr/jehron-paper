"""
Figure 6 (NEW) — Forest plot of the adjusted Cox proportional-hazards model.

A forest plot is the standard, high-impact way to present a multivariable model.
It replaces the dense Table 2 with an at-a-glance view of effect direction,
magnitude, and precision (95% CI), with the HR=1 line of no effect marked.
Source: data/table2_cox_model.csv (the final adjusted model).
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from nature_style import set_style, save, COL15, DATA


def main():
    set_style()
    df = pd.read_csv(DATA / "table2_cox_model.csv")
    # plot from bottom to top -> reverse so first row is on top
    df = df.iloc[::-1].reset_index(drop=True)

    fig, ax = plt.subplots(figsize=(COL15, COL15 * 0.5))
    y = np.arange(len(df))

    for i, row in df.iterrows():
        label = row["level"]
        if row["is_reference"] == 1:
            ax.plot(1.0, i, "|", color="#555555", markersize=8)
            ax.text(1.0, i + 0.28, "ref", ha="center", va="bottom",
                    fontsize=6, color="#555555")
        else:
            hr, lo, hi = row["hr"], row["ci_low"], row["ci_high"]
            sig = lo > 1 or hi < 1
            color = "#0072B2" if sig else "#888888"
            ax.plot([lo, hi], [i, i], color=color, lw=1.4, zorder=2)
            ax.plot(hr, i, "s", color=color, markersize=6, zorder=3)
            ax.text(ax.get_xlim()[1], i, f"  {hr:.2f} ({lo:.2f}–{hi:.2f})",
                    va="center", fontsize=6.5)

    ax.axvline(1.0, color="#999999", lw=0.75, ls="--", zorder=1)
    ax.set_yticks(y)
    ax.set_yticklabels(df["level"])
    ax.set_xscale("log")
    ax.set_xticks([0.25, 0.5, 1, 2, 4, 8])
    ax.set_xticklabels(["0.25", "0.5", "1", "2", "4", "8"])
    ax.set_xlim(0.2, 16)
    ax.set_xlabel("Adjusted hazard ratio (95% CI)")
    ax.set_ylim(-0.6, len(df) - 0.4)

    # group brackets on the left
    ax.tick_params(axis="y", length=0)
    ax.text(0.20, len(df) - 0.2, "← lower risk            higher risk →",
            transform=ax.get_yaxis_transform(), fontsize=6, color="#777777")

    ax.set_title("Adjusted Cox model: predictors of positive GI-PCR > 100 d post-HSCT",
                 fontsize=7.5, pad=8)
    fig.tight_layout()
    save(fig, "Figure6_forest_cox_model")


if __name__ == "__main__":
    main()
