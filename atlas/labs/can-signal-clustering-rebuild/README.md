# Signal-clustering-similarity CAN masquerade detector: independent rebuild on ROAD

_Run commands from the repository root. Data, venv and parse cache live under `.cache/` and are never committed._

**Independent rebuild. This is not ORNL's code.** ORNL's implementation (DOE CODE 134139, "Using Signal Clustering Similarity for Detecting CAN Masquerade Attacks") is closed source. Everything here is my code, written from the method published in OSTI 1866690 (Moriano, Bridges, Iannacone, AutoSec 2022 at NDSS) and the reader's spec in [deep-dives/can-signal-clustering/artifact-study.md](../../../deep-dives/can-signal-clustering/artifact-study.md), whose inferred choices are treated as choices under test.

Date: 2026-11-15/16 (UTC). Pin: none (independent rebuild); method source OSTI 1866690, PDF md5 `27f8aa0e05691288e8f67734c151b31a` per the artifact study.

## Questions

- **R0.** Does the rebuild reproduce Table II (Mann-Whitney p for single, complete, average and Ward linkage; two-sided, one-sided `greater`, legacy half-two-sided) and Table III (Ward, 220 folds, one group test per fold)? Which of the sensitivity choices (A2 slow IDs, A3 per-pair element set, A4 distance) matter?
- **Q1.** Per masquerade capture, does the rebuild flag the 13 masquerades that the time-based IDS lab measured at recall 0 (Mean and Binning)?
- **Q2 (confound).** Does Ward significance persist for (a) pre-injection segments of the attack files and (b) length-matched benign crops from long ambient captures?
- **Q3.** Which targeted signals survive the global constant filter, and does detection persist with the target ID's signals excluded?

## Result in brief

The rebuild does not reproduce the paper. Under the reader's main choices, Ward is significant in 0 of 5 categories (paper 5 of 5), and 1 of 13 masquerade captures is flagged. The global constant filter drops every targeted field, because the idle capture freezes the wheel-speed and speedometer fields. Only the per-pair element-set variant gives Ward significance (3 of 5, two-sided), and it runs the wrong way: attack captures look *more* similar to benign ones than benign captures do to each other. That effect survives removing the target ID's signals entirely. Under the main choices, clean benign crops matched in length are flagged in 25% of category tests, against 0% for the real attacks. On ROAD's released signal files, then, this description of the method does not detect the masquerades the time-based IDS missed. The closed ORNL code may differ in choices the paper does not state.

## Prediction ordering (how a referee can check it)

Predictions are in [predictions.md](predictions.md), written once at 2026-11-16T02:54Z and made read-only (`chmod 444`) immediately. `raw/predictions.sha256` was written by the first command of the lab (02:54:07Z) and records the file's SHA-256 `bb2bc21c…a405a2`, its birth time and mtime. The extraction of `signal_extractions/`, venv creation, every script and every run came after that; `raw/run_log.txt` timestamps each run step, and the `.stdout`/`.time` files carry filesystem mtimes. Re-hash with `shasum -a 256 atlas/labs/can-signal-clustering-rebuild/predictions.md`. This README was started at 02:58Z, after the parse step (`prep`) but before any clustering, similarity or test was computed.

## Deviations from the pre-registered choices

D1 to D3 were written at 02:58 to 03:00Z, before the first clustering run (`r0`, 03:00:02Z in `raw/run_log.txt`). D4 and D5 carry their own timestamps.

- **D1, grid span (A1).** The pre-registered span `[max first, min last]` over all IDs collapses on most attack captures: ID 1649 (0x671) is event-driven (2 to 16 frames in the 12 attack captures that contain it, 0.1 Hz in long captures), so the span shrinks to 0.05 to 0.15 s on `max_engine_coolant_temp` (1.00 to 1.05 s), `correlated_signal_attack_1`, `reverse_light_off_attack_1` and `_2` (`raw/prep_stats.json`, `span_max_first`/`span_min_last`). Rule used instead: IDs whose frame count divided by the capture duration is below 0.5 Hz are dropped from that file before the span is taken. On this data that drops ID 1649 in 23 of 25 files: it runs at 1.0 Hz in `highway_street_driving_diagnostics` (kept there) and is absent from `correlated_signal_attack_3`. It also drops IDs 631 and 930 (0.41 Hz) in `dyno_drive_benign_anomaly` (`raw/r0.json` `file_info.*.sporadic_dropped`). The span is then `[max first, min last]` over the remaining IDs, as pre-registered.
- **D2, environment.** `clusim==0.4` fails with current scipy (`'csr_matrix' object has no attribute 'tolist'` in `make_cielg`: newer scipy returns a sparse matrix from sparse/dense division). Pinned instead to scipy 1.9.3, numpy 1.23.5, pandas 1.5.3, python-igraph 0.9.9 (the 2024 ORNL environment pins python-igraph 0.9.9 and clusim 0.4).
- **D3, similarity caching.** `element_sim` recomputes both affinity matrices on every call. I compute clusim's `make_affinity_matrix` once per dendrogram and take `mean(cL1(A1, A2, alpha))`, which is what `element_sim_elscore` does with `r2 = r`. `run_r0.py` checks this against `clusim.sim.element_sim` on real pairs (`clusim_equivalence` in `raw/r0.json`).
- **D4, Q2/Q3 run in two element-set modes (written 2026-11-16T03:07:54Z, after R0 and the sensitivity runs, before any Q1 to Q3 run).** Under the pre-registered global intersection no Ward category is significant (R0 below), so a confound test in that mode can only measure the false-significance base rate. The only variant with Ward significance in 3 or more categories is A3 (per-pair element set), where the significance is two-sided and in the direction *attack more similar to benign than benign pairs are*. Q2 and Q3 are therefore run in both modes: `global` (pre-registered) and `pairwise` (A3). In pairwise mode the per-pair similarity depends only on the two items, so it is cached within a run; Q3 pairwise reuses A3 for the with-target numbers. The crops in `q2_pairwise_crops_s0` are the same draws as the first 4 replicates of `q2_global` (same seed and draw order). The predictions in predictions.md are scored as written against both modes; nothing in them is changed.
- **D5 (written 2026-11-16T03:24:10Z, after the pairwise full and pre-injection results).** Added one pairwise run of the injection-interval-only segments (`q2pi`), which the global run already had, to see whether the pairwise effect lives in the attack interval. Not pre-registered.

## Resource caps

Per run step (`run.sh`): wall clock 1800 s (`perl alarm` around the process, plus `signal.alarm(1800)` inside Python), CPU 1800 s (`ulimit -t`), processes limited to the user's current count + 16 (`ulimit -u`; macOS counts all of the user's processes), BLAS/OpenMP threads 1, memory 8 GiB through a watchdog thread on peak RSS that hard-exits with code 97. `setrlimit(RLIMIT_AS)` was attempted and refused by macOS (`raw/prep_stats.json` `guard`), so the watchdog is the only memory cap. No cap fired. Measured (`raw/*.time`): parse 29 s and 5.1 GB peak RSS (the 556 MB highway CSV); R0 9 s, 1.5 GB; A2+A4 12 s; A3 331 s, 1.5 GB; Q2 global 23 s, 2.0 GB; Q3 global 23 s; pairwise runs 270 to 791 s each, at most 2.4 GB. Three pairwise steps ran concurrently once (03:09:47Z), each under its own caps.

## Setup and reproduce

- macOS 26.6.2 arm64 (Apple M4, 32 GB). Python 3.10.20 via `uv venv --python 3.10 .cache/venv-clusim`; `uv pip install clusim==0.4 python-igraph==0.9.9 scipy==1.9.3 numpy==1.23.5 pandas==1.5.3` (full freeze in `raw/environment.txt`: clusim 0.4, igraph 0.9.9, networkx 3.4.2, numpy 1.23.5, pandas 1.5.3, scipy 1.9.3, texttable 1.7.3, mpmath 1.4.1). No network after the install.
- Data: ROAD (Zenodo 10462796, CC BY 4.0; Verma et al., arXiv:2012.14600), `road.zip` md5 `cab184cfc2fe12c0834bc46188c0f330` (re-checked, `raw/environment.txt`). Extracted only `road/signal_extractions/*` into `.cache/data/road/` (`unzip -q -n road.zip 'road/signal_extractions/*'`; the zip has no `__MACOSX` entries under that path). Listing with CRC32 in `raw/unzip-v-signal_extractions.txt`, SHA-256 of every file in `raw/sha256-signal_extractions.txt`.
- Run: `sh atlas/labs/can-signal-clustering-rebuild/run.sh env dups prep r0 r0check sens a3 q1 diag q2g q3g q2p q2pi q2pc0 q2pc1 q3p`, then `.cache/venv-clusim/bin/python -I atlas/labs/can-signal-clustering-rebuild/summarize.py atlas/labs/can-signal-clustering-rebuild/raw atlas/labs/can-signal-clustering-rebuild`. The order actually run, with timestamps and the two failed-and-fixed starts, is in `raw/run_log.txt`.
- Every script runs with `python -I`; each inserts only its own lab directory into `sys.path`. Data paths are arguments. The parse cache (`.cache/data/road/work-clusim/*.npz`, 1.2 GB, git-ignored) is regenerated by `prep`. Runs before 03:37:57Z used `.cache/work-clusim/`, which was moved there unchanged because that path is not git-ignored; `r0check` was rerun from the new path and matches (`raw/run_log.txt`).

| File | What it is |
|---|---|
| `scs.py` | the rebuild: parse, 10 Hz interpolation, constant filter, unit norm, Pearson, linkage, clusim affinity, MWU in three conventions, caps |
| `check_dups.py` → `raw/duplicate_check.json` | SHA-256 check of the `ambient/` duplicates |
| `prep.py` → `raw/prep_stats.json` | per-file, per-ID rates, spans, signal counts vs DBC |
| `run_r0.py` → `raw/r0.json`, `raw/r0_final_code.json`, `raw/sens.json`, `raw/a3.json` | Table II, Table III, Fig. 3 cut, Fig. 5 per-file FPR, target survival, A2/A4, A3 |
| `run_q.py` → `raw/q1.json`, `raw/q2_global.json`, `raw/q2_pairwise_{fixed,injection,crops_s0,crops_s1}.json`, `raw/q3_global.json`, `raw/q3_pairwise.json` | Q1 to Q3 |
| `diag_pairN.py` → `raw/diag_pairN.json` | similarity vs element-set size under A3 |
| `summarize.py` → `results_table2.csv`, `results_table3.csv`, `results_q1.csv`, `results_q2_q3.csv` | flat tables with the raw file and key of each number |

## Results

### Data checks

- **Duplicates, confirmed by SHA-256** (`raw/duplicate_check.json`): `ambient/` holds 29 CSVs; 17 are byte-identical to the same-named file in `attacks/` (the 13 masquerades and 4 accelerator captures). The other 12 are exactly the keys of `ambient/metadata.json`. Benign files were selected by those keys.
- **Signals.** All 25 files have 105 IDs and 664 signals (correlated_signal_attack_3 lacks ID 1649 (0x671): 104 IDs, 662 signals). For every ID in every file, the number of non-NaN `Signal_k` columns equals the DBC `SG_` count for that `BO_` (`signal_count_vs_dbc_mismatch` empty), which supports reading `Signal_k` as DBC `Unknown_(k-1)`. Under that reading and the DBC bit layout, the targeted fields are: 0x6E0 `Signal_1..4` (four 14-bit fields), 0xD0 `Signal_6` (bytes 5 and 6, max speedometer), 0xD0 `Signal_3` (byte 2 bit 3, the only bit where `0C` and `04` differ: reverse light), 0x4E7 `Signal_2` (byte 5, coolant). [INFERRED mapping]
- **The paper's 10 Hz premise does not hold for ROAD's signal files**: 40 to 42 IDs per file have median rates below 9.5 Hz, most at 1 or 2 Hz, some at 0.5 to 0.67 Hz (`ids_below_9_5hz`). ID 1649 is event-driven (D1).
- Three benign captures start with a partial bus: in `dyno_drive_extended_long` 53 IDs first appear at 71 to 98 s, in `extended_short` 22 IDs at 20 to 23 s, in `exercise_all_bits` 51 IDs at 141 to 142 s (ID 1649 not counted). The span rule trims those starts.

### R0: Table II and Table III do not reproduce

Main choices (global intersection). **N = 114 signals** survive the global filter (per-file non-constant counts 155 to 523, `raw/r0.json` `primary.file_info`). `clusim_equivalence`: cached affinity and `clusim.sim.element_sim` agree to all printed digits on 3 real pairs. `r0_final_code.json` (the final code, rerun) is identical to `r0.json` apart from timings.

Table II, Ward, p-values (`results_table2.csv`):

| Attack | Paper | two-sided | greater | legacy half | median benign pairs / attack-benign |
|---|---|---|---|---|---|
| Correlated signal | 0.000 | 0.692 | 0.346 | 0.346 | 0.8832 / 0.8800 |
| Max speedometer | 0.000 | 0.573 | 0.287 | 0.287 | 0.8832 / 0.8802 |
| Max coolant | 0.008 | 0.809 | 0.601 | 0.404 | 0.8832 / 0.8846 |
| Reverse light on | 0.004 | 0.199 | 0.099 | 0.099 | 0.8832 / 0.8777 |
| Reverse light off | 0.000 | 0.908 | 0.549 | 0.454 | 0.8832 / 0.8789 |

Detected at 0.05, by linkage (two-sided / greater): Ward 0/0 (paper 5), complete 1/0 (paper 4; the one is correlated, p 0.0019, with attack *more* similar), single 0/0 (paper 3), average 0/0 (paper 3). No convention matches any paper cell.

Sensitivity, Ward (two-sided p; `greater` in brackets where below 0.05; full grid in `results_table2.csv`):

| Variant | N | Corr. | Speedo | Coolant | Rev on | Rev off | Ward detected |
|---|---|---|---|---|---|---|---|
| Main (global, rows-Euclidean) | 114 | 0.69 | 0.57 | 0.81 | 0.20 | 0.91 | 0 |
| A2 drop IDs < 9.5 Hz | 76 | 0.041 | 0.62 | 0.63 | 0.83 | 0.18 | 1 (attack more similar) |
| A4 condensed 2(1-r) | 114 | 0.025 | 0.074 | 0.18 | 0.16 | 0.26 | 1 (attack more similar) |
| A3 per-pair element set | 128 to 407 | **0.0054** | **0.0053** | 0.116 | **0.0043** | 0.20 | 3 two-sided, 0 `greater` |

In every Ward cell that reaches 0.05 in any variant, the attack-vs-benign similarities are **higher** than the benign-pair similarities, so the one-sided `greater` test (benign more self-similar, the direction a detector needs) is never significant (A3 `greater` p 0.899 to 0.998). A3 legacy-half values (0.0027, 0.0026, 0.058, 0.0022, 0.10) are the closest any variant gets to Table II's pattern, and they match it in no cell.

Table III, Ward, 220 folds, group test (`results_table3.csv`):

| Variant, convention | FP of 220 (FPR) | TP corr / speedo / coolant / rev on / rev off | Paper |
|---|---|---|---|
| Main, two-sided | 29 (13.18%) | 8 / 1 / 0 / 15 / 2 | FPR 13.64% stated; FP 30 and TP 220 / 220 / 204 / 205 / 220 back-solved from Table III P/R [INFERRED, artifact study] |
| Main, greater | 23 (10.45%) | 15 / 5 / 0 / 41 / 4 | |
| Main, legacy half | 50 (22.73%) | 15 / 5 / 0 / 41 / 4 | |
| A3, legacy half (direction-free) | 74 (33.64%) | 199 / 194 / 33 / 211 / 36 | |
| A3, greater | 35 (15.91%) | 0 / 0 / 0 / 0 / 0 | |

The main run's two-sided FPR (13.18%) lands within one fold of the paper's 13.64%, and its highest per-file FPR is `dyno_drive_benign_anomaly` at 27.3%, the paper's Fig. 5 value for that file; `dyno_reverse` is 5.5% (paper 20%). Recall is 0 to 7%, so the FPR agreement says only that benign-vs-benign false alarms run at roughly the paper's rate, not that detection reproduces. The per-file reading (each held-out file alone) gives FPR 12.0% two-sided.

Fig. 3 analogue (Ward on rows of the 25×25 similarity matrix, cut at 4 clusters, `primary.linkages.ward.fig3`): two clusters hold 9 benign files and no attack; the other two hold all 13 attacks plus `dyno_drive_winter` (48 s), `dyno_reverse` (51 s) and `dyno_idle_radio_infotainment`. The paper's cut has 11 benign plus 2 attacks on one side and `dyno reverse` with 11 attacks on the other. Both cuts put the short reverse capture with the attacks.

**Which choices matter.** The element-set rule matters most: it alone moves Ward from 0 to 3 significant categories, and it sets the direction. The slow-ID and distance choices each move single cells across 0.05, always in the "attack more similar" direction. Sidedness decides whether anything counts at all: no variant has a significant `greater` cell for Ward. No combination tested reproduces Table II or Table III.

Why A3 runs the "wrong" way (`raw/diag_pairN.json`): with a per-pair element set, similarity falls as the pair's element set grows (Spearman ρ = −0.30 over the 222 pairs, p = 6.5e-6; ρ = −0.41 among the 66 benign pairs), and attack-benign pairs have smaller sets (median 186) than benign pairs (median 245.5), because short captures have fewer non-constant signals. That accounts for part of the effect. It is not the whole story: with pre-injection segments in place of the attack files, the median pair element set over all 222 pairs falls to 177, against 189 for full files (`raw/q2_pairwise_fixed.json` `pre_injection.meta`), and those segments are not significant (Q2). [INFERRED from the correlations]

### Q1: per-file masquerade detection (`raw/q1.json`, `results_q1.csv`)

Each attack file's 12 similarities to the benign files vs the 66 benign pairs, Ward:

| Variant | Files significant, `greater` | Files significant, two-sided | Which |
|---|---|---|---|
| Main (global) | **1 of 13** | 1 | `max_speedometer_attack_3` (greater p 0.017) |
| A2 | 0 | 1 | `reverse_light_off_attack_3`, attack more similar |
| A4 | 0 | 0 | |
| A3 per-pair | 0 | 5 | correlated 2, speedo 1 and 2, reverse on 2 and 3; all attack more similar |

Per attack, main run, `greater` p: correlated 0.46 / 0.22 / 0.55; speedometer 0.94 / 0.31 / 0.017; coolant 0.60; reverse off 0.16 / 0.48 / 0.90; reverse on 0.22 / 0.15 / 0.24. So the rebuild does **not** recover what the time-based IDS missed. Under the main choices it flags one masquerade capture of 13 at the file level, and none of the 0x6E0 or 0x4E7 ones.

### Q2: confound (`raw/q2_global.json`, `raw/q2_pairwise_*.json`, `results_q2_q3.csv`)

Ward category tests, p (two-sided; `greater` in brackets):

| Test | Mode | Corr. | Speedo | Coolant | Rev on | Rev off |
|---|---|---|---|---|---|---|
| Full files | global (N 114) | 0.69 (0.35) | 0.57 (0.29) | 0.81 (0.60) | 0.20 (0.099) | 0.91 (0.55) |
| (a) Pre-injection only | global (N 107) | **0.012 (0.006)** | 0.46 (0.23) | 0.83 (0.42) | 0.069 (**0.035**) | **0.008 (0.004)** |
| Injection interval only | global (N 100) | 0.40 | 0.20 | 0.26 | 0.30 | 0.22 |
| Full files | pairwise | **0.0054** | **0.0053** | 0.116 | **0.0043** | 0.20 |
| (a) Pre-injection only | pairwise | 0.68 | 0.48 | 0.63 | 0.105 | 0.85 |
| Injection interval only | pairwise | 0.74 | **0.017** | 0.60 | **0.041** | 0.42 |

Pre-injection segments have 30 to 407 points on the 10 Hz grid, about 3 to 41 s (correlated_signal_attack_3 has only 30). Every significant pairwise cell has the attack side more similar.

(b) Benign crops matched in length to each of the 13 attack files, from the 10 benign captures of 300 s or more, parent excluded from both samples:

| Mode | Replicates | Crops | Per-crop significant, `greater` / two-sided | Category tests significant, `greater` / two-sided |
|---|---|---|---|---|
| global | 20 (seed 0) | 260 | 23.5% / 23.1% | 29% / 25% of 100 |
| pairwise | 8 (4 each, seeds 0 and 1) | 104 | 2.9% / 13.5% | 5% / 15% of 40 |

Pooled in `results_q2_crops_pooled.csv`. Nominal is 5%. In global mode, clean benign crops reach significance at about five times the nominal rate, mostly in the detector's direction (only 2 of the 25 two-sided hits have the crop more similar), while the real attack files reach it in 0 of 5 categories. In pairwise mode clean crops reach two-sided significance in 15% of category tests (5 of the 6 hits with the crop more similar, the same direction as the attack effect), against 3 of 5 categories (60%) for the real attack files. In global mode the pre-injection segments, which contain no injected frame, are significant in 3 of 5 categories (`greater`) while the full attack files are not. Under the pre-registered choices the test therefore flags short clean captures more often than masquerades. In pairwise mode the full-file effect vanishes in the pre-injection segments and partly reappears in the injection interval (speedometer, reverse light on). That is consistent with something in the attack period, though in the "attack more similar" direction; Q3 shows it is not the targeted fields.

### Q3: targeted signals (`raw/r0.json` `primary.target_survival`, `raw/q3_global.json`, `raw/q3_pairwise.json`)

Global constant filter, all 25 files: **every targeted field is dropped.**

| Signal | Constant in | In global set |
|---|---|---|
| 0x6E0 `Signal_1..4` (correlated) | `dyno_idle_radio_infotainment` (wheels stopped) | no |
| 0xD0 `Signal_6` (speedometer) | `dyno_idle_radio_infotainment` | no |
| 0xD0 `Signal_3` (reverse light) | 7 files: `dyno_drive_winter`, `dyno_idle_radio_infotainment`, correlated 1 to 3, coolant, speedometer 2 | no |
| 0x4E7 `Signal_2` (coolant) | 4 files: correlated 3, reverse off 1 to 3 | no |

Only 0xD0 `Signal_1` and `Signal_5` survive from the three target IDs. So under the main choices the method never sees the injected values. Its inputs can carry an attack only through side effects on other signals. (With only the 12 benign files and the coolant capture, 0x4E7 `Signal_2` does survive, N 133, and the coolant test is still not significant: two-sided 0.15.)

Excluding all signals of the attack's target ID, Ward, two-sided p:

| Target ID (categories) | Global with / without | Pairwise with (A3) / without |
|---|---|---|
| 0x6E0 (correlated) | 0.38 / 0.38 | 0.0054 / **0.0016** |
| 0xD0 (speedo; rev on; rev off) | 0.27, 0.96, 0.84 / 0.50, 0.39, 0.73 | 0.0053, 0.0043, 0.20 / **0.0035, 0.0068**, 0.35 |
| 0x4E7 (coolant) | 0.15 / 0.20 | 0.116 / 0.113 |

In pairwise mode, removing the target ID's signals leaves all three significant categories significant (correlated gets stronger), and the direction stays "attack more similar". Whatever the pairwise test responds to, it is not the injected fields.

## Observations vs prediction

Scored against [predictions.md](predictions.md) as written (SHA-256 in `raw/predictions.sha256`).

| Prediction | Observed | Verdict |
|---|---|---|
| R0: Ward significant in all 5 categories, two-sided and `greater` | 0 of 5 under the main choices; best variant (A3) 3 of 5 two-sided, 0 of 5 `greater` | **wrong** (the "wrong if fewer than 4 of 5" condition fired) |
| R0: at most 2 of 5 Ward cells round to the paper's value | 0 of 5 in every variant | confirmed |
| R0: legacy half-two-sided matches best (about 40% confidence) | no convention matches any cell; legacy half in A3 is nearest in pattern | not supported |
| R0: at most one of the complete/single/average detection counts matches | 0 of 3 (1/0/0 vs 4/3/3) | confirmed |
| R0: Table III FPR between 5% and 25% | 13.18% two-sided, 10.45% `greater`, 22.7% legacy half | confirmed |
| R0: recall at least 90% for correlated, speedometer, reverse off | 0.5% to 7% | **wrong** |
| R0: exact FP = 30 unlikely (under 20%) | 29 | consistent (not 30, but within one fold) |
| R0: slow IDs exist | 40 to 42 IDs per file below 9.5 Hz, down to 0.5 Hz | confirmed |
| R0: "None of A2/A3 flips a Ward category from significant to non-significant" | no Ward category is significant under the main choices, so the prediction could not be tested; A3 flips the other way, turning 3 categories significant (two-sided) | **not testable as written**; the element-set rule is the choice that matters, which the prediction did not anticipate |
| Q1: at least 10 of 13 files significant (`greater`), including all 0xD0 ones | 1 of 13 (main); 0 of 13 `greater` in every variant other than main | **wrong** |
| Q1: correlated_signal_attack_3 and reverse_light_on_attack_3 least significant | main `greater` p 0.547 and 0.238; least significant are max_speedometer_attack_1 (0.937) and reverse_light_off_attack_3 (0.90) | **wrong** (row added by referee 2026-11-15) |
| Q2(a): pre-injection significant in at least 4 of 5 categories | global 3 of 5 `greater`, 2 of 5 two-sided; pairwise 0 of 5 | **wrong** on the count; the direction of the idea holds in global mode only |
| Q2(b): crops significant in at least 3 of 5 categories in most replicates; per-crop rate above 30% | global: 5 of 20 replicates; per-crop 23.5%. Pairwise: 0 of 8 replicates; per-crop 2.9% (`greater`), 13.5% two-sided | **wrong** on both thresholds in both modes; global 23.5% is still about 5 times nominal |
| Q2 conclusion: the whole-file test mostly detects short or out-of-regime captures | global: yes in the sense that clean short captures and pre-injection segments flag more often than attacks; pairwise: the effect is absent before injection | partly supported (global); not supported (pairwise) |
| Q3: 0x6E0 and speedometer fields survive the global filter | dropped, both by the idle capture | **wrong** |
| Q3: reverse-light and coolant fields dropped | dropped | confirmed |
| Q3: excluding the target ID keeps significance in at least 4 of 5 | global: nothing significant either way; pairwise: all 3 significant categories stay significant | **wrong** as written (3 of 5 pairwise, 0 of 5 global). The stated failure condition ("removes 2 or more") did not fire: all 3 significant pairwise categories stay significant |

## Limits

- **This is my rebuild, not ORNL's code.** The closed DOE CODE 134139 implementation may differ in any of the unstated choices: grid span, slow-ID handling, element-set matching, distance, `dist_rescaled`, sidedness, how constant signals were handled across files, or the signal translation itself. A failed reproduction here means "the published description plus these choices does not give Table II on ROAD's public `signal_extractions/`". It does not show the paper's numbers are wrong.
- **The paper's own inputs may differ.** It says "The ROAD dataset provides translated CAN time series following a similar schema used by Hanselmann et al." (p.3 §III-C), and elsewhere that it builds on ORNL's CAN-D decoder (p.1 §I; p.7 §V). It does not say whether it used ROAD's released signal files as shipped. If ORNL ran its own translation of the raw logs, its signal set (and so N) would differ from ROAD's released CSVs. Its exact N is not stated.
- **Search is bounded.** I tested the reader's main choices and the three listed sensitivity variants (A2, A3, A4) one at a time, plus three MWU conventions. I did not test combinations (for example A2 with A3), `dist_rescaled=False`, r = +5, other grid spans, or unions with fill values. A different combination might reproduce the paper.
- **Mann-Whitney on pairwise similarities assumes independent observations**, and they are not: each file appears in 11 benign pairs. That plausibly inflates false positives (23% for clean crops in global mode). [INFERRED] The paper's test has the same structure.
- **Offline replay of one vehicle's recorded captures**, in batch, on a laptop. Nothing here says anything about a live bus, other vehicles, ORNL's deployment, or the closed tool's runtime. The paper itself calls the method forensic, not real-time, and a proof of concept.
- **Crops come from both dyno and road captures** of 300 s or more; attack captures are all dyno. Crops are matched in length, not in driving activity.
- **Q3 field mapping** (`Signal_k` = DBC `Unknown_(k-1)`, byte positions from the DBC bit layout) is inferred, supported by exact per-ID signal-count agreement with the DBC. "Exclude the target ID" removes all of that ID's signals, which is broader than the targeted field.
- Pairwise crop replicates are 8 (104 crops), against 20 in global mode, because of the 30-minute run cap. Pairwise rates are therefore rough (6 two-sided category hits in 40).

## Next

Under the main choices the method does not separate masquerades from clean captures on ROAD, and the only variant that does separate them runs in the "attack more similar" direction, which persists when the injected IDs are removed. The most useful next question is narrow: **does any single coherent set of preprocessing choices reproduce Table II's Ward column with benign pairs more self-similar than attack-benign pairs?** The obvious candidates are a union element set with constant signals kept as zero-correlation leaves, and ROAD's raw logs re-translated through the DBC at the paper's 10 Hz. If none does within a bounded grid, record the method as not reproduced by this rebuild from its public description, and move to the 2024 public windowed code (DOE CODE 141444), which can be run as shipped once its missing preprocessing module is accounted for.
