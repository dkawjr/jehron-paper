# Manuscript edits to make

This is my running list of things to fix in the manuscript text and tables. I
checked every number against the data behind the figures and had it
double-checked. I've grouped them roughly by how important they are. Quotes are
pulled from the current draft so they're easy to find.

## Numbers and statistics (fix these first)

1. **The male-sex hazard ratio in the abstract is impossible as written.**
   "*male sex (adjusted HR (aHR) 2.08, 95% CI 0.26–0.90)*" — an HR of 2.08 can't
   have a confidence interval that sits entirely below 1. That interval is the
   *female* estimate's. The clean, data-backed fix is to report it as **female
   sex aHR 0.48 (95% CI 0.26–0.90)**. If we want to keep the male framing, the
   point estimate is ~2.08 (it's just 1/0.48), but the matching CI (~1.11–3.85)
   has to be pulled straight from the SPSS output — it isn't something I can
   recompute from the figure data, so grab it from the model.

2. **The abstract's crude-analysis sentence points two factors the wrong way.**
   "*male sex, hospitalization at the time of testing, conditioning with
   chemotherapy plus total body irradiation, and absence of GVHD … was associated
   with increased likelihood of a positive GI PCR test.*" Hospitalization
   (51% of positives vs 73% of negatives) and chemo+TBI (12% vs 29%) were
   actually associated with *negative* results — which is what the Results
   section already says. So the abstract contradicts the body. Also, male sex was
   p = 0.057 in the crude analysis, so it's a trend, not a clear association.
   Reword so only absence of GVHD (and male sex, as a trend) sit on the
   "more positive" side, and move hospitalization and chemo+TBI to the
   "more negative" side.

3. **The bacteria/virus/parasite split is off.** Both the abstract and Results
   say "*bacteria (49%), viruses (33%), parasites (17%)*." The 47 detections
   actually give **bacteria 51%, viruses 30%, parasites 17%** (24, 14 and 8 of
   47). The old 49/33 looks like it came from an earlier, smaller data cut. One
   thing to decide while fixing this: there's a single "other" detection (2%), so
   the three main groups are 51/30/17 *of all 47* and don't sum to 100. Either
   state the n and acknowledge the one "other," or renormalize to the 46
   bacteria/virus/parasite detections (52/30/17) — just be explicit about which.

## Placeholders still in the draft

4. Methods: "*\*\*\* were entered stepwise, retaining variables…*" — fill in
   which variables were entered.
5. Methods: "*…IBM SPSS Statistics version 31 (IBM Corp, Armonk, NY) and \*\*\*.*"
   — either name the second program or delete "and \*\*\*."
6. Results: "*adjustments made for potential confounders/baseline
   characteristics?*" — finish this sentence and drop the stray "?".
7. Table 1, median age row: the IQRs are still "*(\*IQR)*" placeholders and the
   p-value cell is "X." Fill in the actual IQRs (and either give a p-value or
   mark it not tested).
8. Table 1, TBI row: "0 | 0 | X" — fill in or remove.

## The temporal story is overstated (important)

9. **"Almost exclusively early" isn't supported by the data.** The abstract says
   viral and parasitic infections "*occurred almost exclusively during the early
   post HSCT period (day 100 to 400)*" and the Results call out the parasites'
   "*most pronounced early peak*." When I actually test the timing, there's no
   difference: Kruskal–Wallis across the three groups p = 0.29; viruses vs
   bacteria p = 0.96 (basically identical timing); parasites vs bacteria p = 0.18.
   Before day 400 the proportions are bacteria 50%, viruses 50%, parasites 75% —
   viruses are no earlier than bacteria. The early skew is mostly just that most
   testing happens early. This needs to come down to plainly descriptive,
   hypothesis-generating wording — drop "almost exclusively" and "most pronounced
   peak."

10. **Two late viral detections contradict the "late = bacterial" claim.** The
    discussion says that beyond ~1000 days infection is "*increasingly driven by
    bacterial pathogens*," but of the four detections after day 1000, two are
    viral — sapovirus at day 1101 and norovirus at day 1222 (the other two are
    E. coli at 1329 and 1896). So the latest interval is split evenly between
    bacteria and viruses, not bacterial. Soften that claim.

11. **The "not beyond 1300 days" framing is arbitrary.** The Figure 3 caption
    says norovirus was "*not detected beyond 1300 days*," but the last norovirus
    is day 1222, and 1300 is only meaningful because E. coli happens to be the
    only thing past it. Better to just state the actual last-detection days.

12. **Pick one direction for the GVHD finding and stick with it.** The text
    flips between "GVHD is protective" and "absence of GVHD is a risk factor"
    (abstract, and discussion in two places). The model result is no-GVHD
    aHR 2.59, so I'd frame it consistently as absence of GVHD increasing risk.

## Wording / internal logic

13. **The Kaplan–Meier numbers are mislabeled.** "*lower cumulative probability
    of positive GI PCR results among patients with GVHD … reaching approximately
    50% vs 75% at 1000 days.*" Only 46% of patients were ever positive, so a
    *positivity* curve can't reach 75%. Those 50%/75% values are the
    event-free (staying-negative) probabilities. Make the text, the y-axis label,
    and the Figure 5 caption all say the same thing — either cumulative incidence
    of a positive (which would be roughly 25% vs 50%) or probability of remaining
    negative (50% vs 75%). I can't verify the exact numbers until the per-patient
    survival data are available to regenerate Figure 5.

14. "*patients without acute-phase GVHD had a higher hazard … compared to those
    **without** prior GVHD*" — the second "without" should be "with."

15. "*Chi-square analysis  clinical characteristics between patients…*" — missing
    a verb; should read "Chi-square analysis **compared** clinical
    characteristics."

16. Methods describes a stepwise model *and* a Cox model, but only the Cox model
    shows up in Table 2. Clarify whether a stepwise logistic step was actually
    run or whether that sentence (the one with the "\*\*\*") is leftover.

## Figure / text consistency

17. **The "100–600 day" statistic no longer matches the figures.** Results: "*Between
    100 and 600 days … bacteria (51%), viruses (29%), parasites (20%).*" Those
    numbers are correct for a 100–600 window, but the redrawn figures use
    100–400 / 400–700 / 700–1000 / >1000 bins, so nothing in the figures shows a
    100–600 bar anymore. Either re-anchor this sentence to the new bins or keep
    the original binning.

18. **Figure 2 and 3 captions don't match the redrawn figures.** They say each
    pathogen is shown "*as a proportion of the cumulative total*" over "100–700
    days," but the new figures show counts over the standardized bins. Use the
    captions in `FIGURE_CAPTIONS.md`.

19. **The figure-caption block is duplicated** — Figures 1–5 are listed twice,
    verbatim. Delete one copy.

20. **Figure 5 still needs data.** The KM figure and its numbers can't be
    reproduced or checked without the per-patient survival file (time, event,
    GVHD status). Either supply it so the figure can be generated, or pull the
    specific values until it can be verified.

## Typos and small fixes

21. "*is not biologically **unform***" → "uniform."
22. "*This study also **not evaluate** for pathogens*" → "did not evaluate."
23. Figure 1 caption: "*Cryptospordium parvum(13%)*" → "Cryptosporidium parvum
    (13%)" (spelling + missing space).
24. Abstract says "*Cryptosporidium species*" while the Results say
    "*Cryptosporidium parvum*." The data are genus-level only, so I'd use
    "Cryptosporidium species" everywhere.
25. "*GI PCR testing more than 100 after HSCT*" — add "days."

## Clarity / data hygiene

26. **Say which denominator each percentage uses.** The pathogen percentages are
    out of 47 detections (in 41 positive patients); the 46% positivity is 41/90
    patients. State this once so the two aren't confused — six patients had more
    than one organism, which is why the counts differ.

27. **Transplant type is short one positive patient.** In Table 1 the allograft
    and autograft positives add up to 40, but there are 41 positives, and every
    other row sums to 41/49. One positive patient isn't classified by transplant
    type — worth finding and adding back, since it affects the allograft odds
    ratio.
