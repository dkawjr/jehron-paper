"""
make_all.py — regenerate every figure from scratch.

Usage:
    py src/extract_data.py     # once, to (re)build data/*.csv from the workbook
    py src/make_all.py         # build all figures into figures/
"""
import importlib

MODULES = [
    "fig1_pathogen_distribution",
    "fig2_pathogen_category_over_time",
    "fig3_specific_pathogens_over_time",
    "fig4_relative_contribution",
    "fig5_kaplan_meier",
    "fig6_forest_cox",
    "fig7_forest_table1",
    "fig8_pathogen_heatmap",
    "fig9_cumulative_accrual",
]


def main():
    for name in MODULES:
        print(f"[{name}]")
        mod = importlib.import_module(name)
        try:
            mod.main()
        except Exception as e:  # keep going so one failure doesn't stop the rest
            print(f"  !! {name} failed: {e}")
    print("\nAll done. See the figures/ folder.")


if __name__ == "__main__":
    main()
