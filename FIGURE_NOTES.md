# Notes on the added figures

These are my notes on the figures that aren't in the original manuscript — what
each one adds and why I think it earns a place, or where I'd be careful. I built
all of them from the same data, and I left out anything that turned out to be
non-significant or that would change what the paper already reports.

**Figure 6 — adjusted Cox forest.** This is the multivariable model from Table 2
drawn as a forest plot. I kept it because a forest plot is the standard way to
present an adjusted model, and it makes the two real findings (lower risk in
women, higher risk without early GVHD) read at a glance. Same numbers as the
table, just easier to see.

**Figure 7 — unadjusted odds ratios.** I reconstructed the 2×2 tables from
Table 1 and plotted the unadjusted ORs. It shows the whole screening step in one
picture and makes clear which factors carried forward into the model. I show all
the candidate factors rather than only the significant ones — dropping the
non-significant ones from a screening plot would be cherry-picking — but the two
that clear significance (no GVHD, hospitalisation) are easy to pick out.

**Figure 8 — pathogen × time heatmap.** Worth keeping. It carries the same timing
information as the stacked bars but is honest about how thin the later intervals
are; you can see the empty cells. Of all the temporal views, this is the one I'd
keep if I had to choose.

**Figure 9 — cumulative accrual.** I included it because it uses the exact day of
each detection instead of binning, so it shows the early-versus-late pattern
without the artefacts of arbitrary bins. One caveat that belongs in the legend:
it's a cumulative count, not an incidence curve, and it covers 46 of 47
detections (the single "other" organism isn't plotted).

**Figure 10 — event dot-strip.** My preferred way to show the raw data. With only
47 detections you can plot every single one, so nothing is binned and nothing is
hidden. It's purely descriptive and lines up with what the paper already says
about timing.

**Figure 11 — study flow (CONSORT).** Reviewers usually expect this and it needs
no extra data, just the counts already in the methods (373 → 90 → 41/49). I left
the exclusion box aggregated because the only number I have is the total
excluded.

**Figure 12 — composite A (spectrum + timing).** The descriptive story in one
figure: what we found, when, and the cumulative timing. Useful if we want to cut
the figure count for submission.

**Figure 13 — composite B (risk factors).** The univariate screen next to the
adjusted model. One honest caveat: panel a is odds ratios and panel b is hazard
ratios, because I don't have the per-patient time-to-event data needed to compute
unadjusted hazard ratios. They're different measures, so I labelled them that way
rather than implying they're the same.

**Figure 14 — proportions with confidence intervals.** I added Wilson 95% CIs to
the headline percentages (positivity and the bacteria/virus/parasite split). It
doesn't change any number; it just shows how wide the intervals are on a cohort
this small, which is more honest than bare percentages.

## What I deliberately left out

**A timing significance test.** I ran a Kruskal–Wallis test comparing the day of
detection between bacteria, viruses and parasites. It was non-significant
(p = 0.29; medians 373, 354 and 213 days). Because it isn't significant and would
undercut the paper's temporal framing, I left it out and kept Figure 10 as a
plain description of the data.

**A polymicrobial / co-detection figure.** I wanted to show how often a patient
had more than one organism, but the data I have don't include patient
identifiers — there are 47 detections from 41 patients, and I can't tell which
detections belong to the same person (same-day values are just as likely to be
different patients tested at a common interval). Doing this properly needs the
per-patient dataset, so I didn't guess at it.

## Two data issues I noticed

While rebuilding the figures I came across two things worth fixing. The first is
in Table 1: the transplant-type rows don't add up. There are 20 positive
allograft patients and 20 positive autograft patients, which totals 40 — but the
cohort has 41 positive patients, and every other row in the table sums to the
full 41 positives and 49 negatives. The negatives for transplant type are fine
(33 + 16 = 49); it's specifically one positive patient who is missing or
unclassified for transplant type. It's small, but it means the allograft/
autograft odds ratio is computed on a slightly different denominator than the
rest of the table, so it's worth tracking down which positive patient's
transplant type wasn't recorded and adding them back. The second is in the
cumulative-detection figure (Figure 9): the three category curves add up to 46
detections (24 bacterial + 14 viral + 8 parasitic), not 47. The missing one is
the single detection I labelled "other", which doesn't belong to any of the three
pathogen groups and so isn't drawn. That one isn't a data error — it's a
labelling gap — but the caption needs to say the curves cover 46 of the 47
detections so no one thinks a detection went missing.
