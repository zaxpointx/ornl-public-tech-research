# Predictions (write-once)

Written 2026-11-16T02:54Z (UTC), before the ROAD `signal_extractions/` folder was extracted, before the venv existed and before any script was written or run. This file is never edited after creation. Its SHA-256 and mtime are recorded in `raw/predictions.sha256` by the first command of the lab, before extraction. Any later design change goes in the README under "Deviations", not here.

Everything run in this lab is an **independent rebuild** of the method published in OSTI 1866690 (Moriano, Bridges, Iannacone, AutoSec 2022). ORNL's code (DOE CODE 134139) is closed; nothing here is ORNL's code. Spec: `deep-dives/can-signal-clustering/artifact-study.md`, whose inferred choices I treat as choices under test.

## Main choices (pre-registered)

10 Hz linear interpolation on `[max first, min last]` per file; all IDs kept; constant-on-grid signals dropped; unit-norm scaling; **global intersection** of non-constant signals over the 25 files (12 benign by `ambient/metadata.json` keys, 13 masquerades), sorted; Pearson matrix C; `scipy.cluster.hierarchy.linkage(C, method)` with rows of C as observation vectors (Euclidean); `clusim.Clustering().from_scipy_linkage(Z, dist_rescaled=True)`; `element_sim(alpha=0.9, r=-5.0)`; Mann-Whitney U with benign as x.

## R0: Table II and Table III

- Ward, Table II: **all 5 categories significant at 0.05** under two-sided and one-sided `greater`. Exact p-values will not match the paper's 3 decimals in most cells (I expect at most 2 of 5 Ward cells to round to the paper's value under any sidedness), because N, grid span and distance are unknown.
- Sidedness: if any of the three p conventions matches the paper's cells best, it will be the legacy half-two-sided (= one-sided in the observed direction), but I give this low confidence (about 40%).
- Other linkages: the paper's detection counts (complete 4, single 3, average 3) will **not** all reproduce; I predict at most one of those three counts matches exactly.
- Table III (Ward, 220 folds, group test): FPR between 5% and 25% (paper 13.64%); recall at least 90% for correlated, max speedometer and reverse light off. Exact FP = 30 of 220: under 20% likely.
- Sensitivity (A2 drop IDs below 9.5 Hz, A3 per-pair intersection, A4 condensed distance 2(1-r)): ROAD has IDs slower than 9.5 Hz (so the paper's "10 Hz is the lowest" premise is false for some IDs). None of A2/A3 flips a Ward category from significant to non-significant; A4 may change the non-Ward linkages most.

Wrong if: fewer than 4 of 5 Ward categories are significant two-sided; or Table III FPR is outside 5-25%; or no slow IDs exist.

## Q1: masquerades per attack

Per-file test (one attack file's 12 similarities to the benign files vs the 66 benign pairs, Ward, one-sided `greater`): **at least 10 of 13 masquerade files significant at 0.05**, including all three 0xD0 categories, which the time-based IDS missed at recall 0. Per-file, I expect `correlated_signal_attack_3` and `reverse_light_on_attack_3` to be the least significant (the paper's Fig. 3 puts them with the benign files).

Wrong if: fewer than 8 of 13 files are significant.

## Q2: confound (decides masquerade vs short/out-of-regime capture)

Design: (a) each attack file cut to its pre-injection segment `[start, injection_interval[0])`; (b) benign crops of lengths matched to the 13 attack files, taken at seeded random offsets from benign captures long enough to hold them, with the parent file excluded from both the baseline (55 pairs among the other 11) and the crop's comparison set (11 values). The element set is re-derived as the global intersection over all files in that test. Ward, same MWU.

- (a) Pre-injection segments: **significant in at least 4 of 5 categories** (two-sided and `greater`).
- (b) Length-matched benign crops: **significant in at least 3 of 5 matched categories** in the majority of seeded replicates; over all crops, the per-crop significance rate is above 30% (far above the nominal 5%).
- Conclusion I expect: the whole-file Table II test mostly detects short / out-of-regime captures, not the injection.

Wrong if: (a) is significant in at most 1 of 5 and (b) has a per-crop significance rate at or below 10% while the full files are significant. That would mean the method does detect the masquerade content.

## Q3: targeted signals

- Survive the global constant filter: the four 0x6E0 signals (wheel speeds vary in every capture) and the 0xD0 field written by max speedometer (byte 5). **Dropped**: the 0xD0 reverse-light field (byte 2) and the 0x4E7 coolant field (byte 5), because they are constant in at least one benign or short capture.
- Excluding all signals of the attack's target ID (0xD0 for speedometer and reverse light, 0x6E0 for correlated, 0x4E7 for coolant) leaves Ward significance in **at least 4 of 5 categories**.

Wrong if: the reverse-light or coolant field survives the global filter, or excluding the target-ID signals removes significance in 2 or more categories.
