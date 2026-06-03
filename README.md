# Late-Phase Enteric Infections after HSCT — Figures

Publication-quality (Nature-style) figures and the code that generates them for
the manuscript *"Risk Factors and Microbiologic Spectrum of Late Phase Enteric
Infections after Hematopoietic Stem Cell Transplant."*

Every figure is generated **programmatically from the underlying data** so they
are fully reproducible, restyleable, and editable as vector PDFs.

---

## Quick start

```bash
# 1. install dependencies (Python 3.9+)
pip install -r requirements.txt

# 2. (re)build the clean data tables from the original workbook
python src/extract_data.py

# 3. build every figure into figures/  (PDF + 600-dpi PNG)
python src/make_all.py
```

> On Windows you may need to type `py` instead of `python`.

Each figure is also a standalone script (e.g. `python src/fig1_pathogen_distribution.py`).

---

## What's in here

```
hsct-enteric-figures/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/Revised_Figures_and_Tables.xlsx   # original source workbook
│   ├── positive_detections.csv               # 47 positive GI-PCRs: day, pathogen, category
│   ├── table1_risk_factors.csv               # reconstructed 2x2 counts (Table 1)
│   └── table2_cox_model.csv                   # adjusted Cox HRs (Table 2)
├── src/
│   ├── nature_style.py        # shared styling: palette, fonts, sizes, save()
│   ├── extract_data.py        # workbook -> tidy CSVs
│   ├── _binning.py            # standardized time bins
│   ├── fig1 ... fig9 .py      # one script per figure
│   └── make_all.py            # build everything
└── figures/                   # output (PDF + PNG)
```

Outputs are saved as **both** vector `.pdf` (for journal submission / Illustrator
editing) and 600-dpi `.png` (for slides and quick viewing). Text is embedded as
editable TrueType (`pdf.fonttype = 42`).

---

## The figures

### Polished versions of the existing figures

| # | File | What changed |
|---|------|--------------|
| **1** | `Figure1_pathogen_distribution` | Horizontal bar chart sorted by frequency, coloured by pathogen **type** — replaces the pie/percent display. Bars encode magnitude accurately; *n* and % labelled. |
| **2** | `Figure2_pathogen_category_over_time` | Stacked bars of **absolute counts** per time bin by category. Shows both the declining infection burden and the shifting composition without hiding small denominators. |
| **3** | `Figure3_specific_pathogens_over_time` | Stacked bars of individual pathogens over time, shaded within category. Makes *E. coli*'s persistence into late intervals obvious. |
| **4** | `Figure4_relative_contribution` | Clean 100%-stacked composition per time bin, with the per-bin denominator (*n*) annotated so the reader isn't misled by sparse intervals. |
| **5** | `Figure5_kaplan_meier` | **Script is ready but needs data — see below.** |

### New visualizations (all derivable from the data already provided)

| # | File | Why it helps |
|---|------|--------------|
| **6** | `Figure6_forest_cox_model` | **Forest plot of the adjusted Cox model** (Table 2). The standard, at-a-glance way to present a multivariable model in a high-impact journal. |
| **7** | `Figure7_forest_table1_unadjusted` | **Forest plot of unadjusted odds ratios** (Table 1). Turns a dense table into a visual ranking of risk factors with 95% CIs. |
| **8** | `Figure8_pathogen_time_heatmap` | Compact **pathogen × time heatmap** — an elegant matrix alternative to the stacked bars. |
| **9** | `Figure9_cumulative_accrual` | **Cumulative accrual step plot** using exact event days (no binning). Directly shows parasites/viruses plateauing early while bacteria keep accruing. |

---

## Figure 5 (Kaplan–Meier) — action needed

The original Figure 5 in the workbook is a **pasted Stata screenshot**, and the
per-patient survival data are **not** in any of the provided files, so it cannot
be reproduced from what we have.

`src/fig5_kaplan_meier.py` is written and ready. It computes the KM estimator,
the log-rank test, and the number-at-risk table (numpy/scipy only). To produce
the figure, drop a one-row-per-patient file at:

```
data/kaplan_meier_patients.csv
```

with these columns:

| column | meaning |
|--------|---------|
| `time`  | days from HSCT day 100 to first positive GI-PCR **or** to censoring |
| `event` | `1` = positive GI-PCR (event), `0` = censored |
| `gvhd`  | GVHD status: `1`/`0` or `"GVHD"`/`"No GVHD"` |

Then run `python src/fig5_kaplan_meier.py`. (If the file is missing, the script
writes an example layout to `data/kaplan_meier_patients_TEMPLATE.csv` you can
copy from.)

---

## Notes for the authors

- **Standardized time bins.** The workbook used different time bins across
  figures (and contained an unresolved note debating them). All temporal figures
  now use one consistent scheme: **100–400, 400–700, 700–1000, >1000 days.**
  The later 300-day bins each held only 1–2 detections, so collapsing the tail
  into `>1000` avoids visually overweighting near-empty intervals. Bins are
  left-inclusive (`[100, 400)`, etc.); change `TIME_BINS` in `nature_style.py`
  to use a different scheme.

- **Possible abstract typo.** The abstract reports *"male sex (aHR 2.08, 95% CI
  0.26–0.90)"* — the CI does not contain 2.08 and matches the **female**
  estimate. The adjusted model is **Female HR 0.48 (0.26–0.90)**, equivalently
  **Male HR ≈ 2.08** relative to a female reference. Figure 6 shows it correctly;
  worth fixing in the text.

- **Counts are computed from the raw 47 detections**, which reproduce the
  manuscript's headline numbers exactly (E. coli 36%, norovirus 21%,
  Cryptosporidium 13%). A couple of the workbook's pre-summarized per-bin counts
  differ by one from the raw data (internal rounding/binning inconsistencies in
  the spreadsheet); the figures here are recomputed from source for consistency.

## Further analyses possible if the per-patient line-level dataset is shared

The provided files only contain the 47 positive detections plus summary tables.
With the full per-patient dataset (the one behind Tables 1–2), these would be
straightforward, high-value additions:

- Figure 5 Kaplan–Meier (as above), plus KM stratified by sex.
- A combined / multivariable forest with all candidate covariates.
- Time-to-event by pathogen category (competing-risks / cumulative incidence).
- A patient-level "swimmer" or CONSORT-style flow (373 reviewed → 90 included).
