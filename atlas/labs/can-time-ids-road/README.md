# Time-based CAN IDS on ROAD: reproduction and masquerade boundary

_Run commands from the repository root. Data and the venv live under `.cache/` and are never committed._

Date: 2026-11-15. Atlas experiment that runs a faithful re-implementation of published ORNL detection code, checked against the pinned module, on real public data.

## Question

Do ORNL's four time-based CAN detectors (Blevins, Moriano et al., AutoSec 2021) reproduce their published fabrication-attack numbers on the public ROAD dataset, and where is their boundary? Specifically:

- **R0.** Does Binning at α=3.5 reproduce F1 0.9889 and Mean at α=0.444 (8/18) reproduce F1 0.9862 on the 16 fabrication logs?
- **Q1.** Can the same trained detectors see the 13 ROAD masquerade captures at all? (Not evaluated by the paper or notebook.)
- **Q2.** Is the Gaussian detector's poor F1 (0.26) caused by its "3 consecutive" sufficiency rule rather than by the Gaussian model? Swap rules: Gaussian with Mean's "3 of last 6", Mean with Gaussian's "3 consecutive".
- **Q3.** The notebook labels every target-ID frame inside the injection interval as an attack, including legitimate ECU frames. How many positives survive payload-based relabeling, and what happens to precision?

## Pin and code provenance

- Code: https://github.com/pmoriano/can-time-based-ids-benchmark at `e0c862d6c6cbb0d60ed2572a90dd483a3253ed0f` (HEAD, only branch), checkout at `.cache/src/can-time-ids-e0c862d/`, read only and never executed except for the equivalence check described below. GPL-3.0.
- Reader reconstruction with line citations: [deep-dives/can-time-ids/reconstruction.md](../../../deep-dives/can-time-ids/reconstruction.md).
- Detectors in `can_ids.py` are **Atlas-authored vectorised re-implementations** of `make_can_df`, `add_time_diff_per_aid_col`, `train`, `add_actual_attack_col`, `alert_by_mean_various_p` + `get_results_mean_various_p`, `alert_by_bin_various_p`, `y_threshold_gauss`, `add_gauss_val_col` + `get_results_gauss` (`code/helper_functions.py` @ e0c862d). They are not ORNL's code. `equivalence_check.py` imports the pinned `helper_functions.py` by explicit path (with `matplotlib.pyplot` stubbed, since the module only imports it) and compares outputs on small inputs, so the re-implementation is tied to the original, not just to my reading of it.
- Notebook not run. KDE detector skipped (over 5 h in the original run).
- Data: ROAD, Zenodo record 10462796, `road.zip`, md5 `cab184cfc2fe12c0834bc46188c0f330` (verified), CC BY 4.0. Verma et al., arXiv:2012.14600. Only `road/ambient/ambient_dyno_*.log`, `road/attacks/*.log`, the two `capture_metadata.json` files, `readme.md` and `data_table.csv` extracted.

This is not a synthetic input run: it is an offline replay of real dynamometer captures. See Limits.

## Predictions (written before any run)

### R0: reproduction

Prediction: **both pass** (F1 within ±0.002 of 0.9889 and 0.9862, each confusion-matrix cell within ±1% of `[[1525895,852],[514,61002]]` and `[[1525274,1473],[239,61277]]`). Parsing and labeling are deterministic, so I expect the test-set size (1,588,263 rows) and positives (61,516) to match **exactly**. Residual drift can come only from training: `EllipticEnvelope` is unseeded and library versions differ from the authors' unknown ones, which moves each µ slightly.

Wrong if: either F1 misses by more than 0.002, or the row or positive counts differ (that would mean my parser or the data differ from what the authors used, e.g. a different ROAD release).

### Q1: masquerade

Prediction: recall ≤ 0.01 for both Mean (0.444, 3 of 6) and Binning (3.5) on **every** one of the 13 masquerade logs. FPR stays on the fabrication order (~1e-3). The few true positives sit within a few frames of the interval start or end. Reason: ROAD removed the legitimate target-ID frames during the attack, so the injected stream has the legitimate period and nothing in inter-arrival time changes. Gaussian (p=0.09, 3 consecutive) also ≤ 0.01.

Labels: every target-ID frame inside the metadata interval is positive (all of them are injected in these logs).

Wrong if: any masquerade log gives recall > 0.05 for Mean or Binning.

### Q2: sufficiency-rule swap

Reconstruction hypothesis: under flam delivery the target ID's gaps alternate δ, µ−δ; a two-sided test flags δ but not µ−δ, so "3 consecutive" is rarely met while "3 of 6" is.

My predictions, diverging in one place from the reconstruction:
- **Mean with 3 consecutive** at α=0.444: F1 ≤ 0.40 (point guess < 0.2), because alternating flags never form three in a row on the aid-sorted rows.
- **Gaussian with 3 of 6 at p=0.09**: F1 ≤ 0.83, **not** ≥ 0.85. Reason: any row meeting "3 consecutive" also meets "3 of last 6", so false positives with 3-of-6 are at least the published 3-consecutive count. From the published P 0.334 and R 0.213 that is about 26k false positives against 61.5k positives, so even at recall 1.0 precision is ≤ 0.70.
- **Gaussian with 3 of 6, best over its 18-value p sweep**: F1 ≥ 0.85 at some smaller p. This is the actual test of the sufficiency hypothesis.
- Supporting measure: in one 0xD0 fabrication capture, more than 80% of flagged in-interval target frames have both neighbours unflagged.

Wrong (hypothesis rejected, tail-shape explanation favoured) if: best Gaussian 3-of-6 F1 over the sweep stays below 0.5, or Mean 3-consecutive stays above 0.8.

### Q3: payload relabeling

Relabel the 13 targeted fabrication logs: positive only if `aid == injection_id`, in interval, and `data` matches `injection_data_str` with `X` as regex `.` (logic of the commented-out `get_injection_interval`, `helper_functions.py:L234-L237`). Fuzzing labels are already payload-based and stay unchanged.

Prediction: positives in those 13 logs fall to 40–60% of the current count (about one injected frame per legitimate one). At the published optima, precision falls below 0.65 for both Mean and Binning, because the windowed alerts also fire on the legitimate frames between injections; recall stays above 0.95. Side output: flam delay δ (gap from each payload-matched frame to the previous same-aid frame) has median well under 1 ms.

Wrong if: payload labels keep more than 75% of positives, or precision stays above 0.9.

## Resource caps

Planned: single process, BLAS threads 1, `ulimit -t 3600` (CPU seconds), `ulimit -u` left at the user default, wall-clock limit 3600 s enforced by a watchdog in `run.sh`, peak RSS measured with `/usr/bin/time -l`. macOS does not enforce `ulimit -v`, so memory is measured, not capped. Actual values are recorded below.

Actual: CPU `ulimit -t 3600`; `ulimit -u` set to the current user process count + 64, because macOS counts all of the user's processes and a flat 256 made `fork` fail on the first attempt (that attempt never started Python); a 3600 s wall clock per step via `perl -e 'alarm…'`; BLAS/OpenMP threads 1. Measured (`raw/*.time`): main run 43 s wall, peak RSS 3.6 GB; seed-1 R0 rerun 31 s, 3.7 GB; equivalence check 7 s, 0.2 GB.

## Setup and reproduce

- macOS 26.6.2 arm64 (Apple M4, 32 GB), Python 3.10.20 via `uv venv --python 3.10 .cache/venv-can-ids`, numpy 1.23.5, pandas 1.5.3, scipy 1.9.3, scikit-learn 1.1.3, tqdm 4.66.5 (full freeze in `raw/environment.txt`). No network after the package install.
- Data: `unzip road.zip 'road/ambient/ambient_dyno_*.log' 'road/ambient/capture_metadata.json' 'road/attacks/*' road/readme.md road/data_table.csv` into `.cache/data/road/` (listing in `raw/unzip-l-extracted.txt`). Every extracted log has 3-character aids and 16-character payloads in every line, which is why the fast `read_csv` parser can match `read_fwf` exactly.
- Run: `sh atlas/labs/can-time-ids-road/run.sh`, then `.cache/venv-can-ids/bin/python -I atlas/labs/can-time-ids-road/summarize.py atlas/labs/can-time-ids-road/raw atlas/labs/can-time-ids-road/results.csv`. Diagnostic: `.cache/venv-can-ids/bin/python -I atlas/labs/can-time-ids-road/diag_gauss_runs.py .cache/data/road/road atlas/labs/can-time-ids-road/raw/training_seed0.csv max_speedometer_attack_1 atlas/labs/can-time-ids-road/raw/diag_gauss_max_speedometer_attack_1.json`.
- All scripts run with `python -I`. Only `equivalence_check.py` touches the checkout, by loading `code/helper_functions.py` from an explicit path.

| File | What it is |
|---|---|
| `can_ids.py` | Atlas re-implementation of the detectors, with line citations |
| `equivalence_check.py` → `raw/equivalence.json` | re-implementation vs pinned `helper_functions.py` |
| `run_experiment.py` → `raw/r0_seed{0,1}.json`, `raw/q1.json`, `raw/q2.json`, `raw/q3.json`, `raw/training_seed{0,1}.csv`, `raw/run_log_seed0.json` | R0, Q1, Q2, Q3 |
| `diag_gauss_runs.py` → `raw/diag_gauss_max_speedometer_attack_1.json` | why Gaussian + 3 consecutive misses |
| `summarize.py` → `results.csv` | one row per claim, with the raw JSON key it came from |

## Results

### Equivalence (`raw/equivalence.json`)

On three attack logs, the re-implementation and the pinned module give identical row counts, aids, times, time diffs, payloads and labels (max abs difference 0.0). With the same global seed, `train` gives identical µ and σ for all 105 aids of `ambient_dyno_reverse`. Mean (α=0.444, 3 of 6) and Binning (α=3.5) confusion matrices on `max_engine_coolant_temp_attack` are identical, and Gaussian thresholds for 5 aids × 18 p values are identical.

### R0: reproduced exactly

| Detector | Published CM (notebook output) | This run, seeds 0 and 1 | F1 |
|---|---|---|---|
| Mean α=8/18, 3 of 6 | `[[1525274,1473],[239,61277]]` | `[[1525274,1473],[239,61277]]` | 0.9862 |
| Binning α=3.5 | `[[1525895,852],[514,61002]]` | `[[1525895,852],[514,61002]]` | 0.9889 |
| Gaussian p=0.09, 3 consecutive | `[[1500721,26026],[48436,13080]]` (notebook :L4119-L4120), F1 0.2600 | `[[1500707,26040],[48436,13080]]` P 0.3344 R 0.2126 | 0.2599 |

Training rows 13,300,759 and 105 aids; test rows 1,588,263; positives 61,516; no unseen aids in any test log. All match the notebook exactly. The full Mean and Binning sweeps are in `raw/r0_seed0.json`, including the Binning F1 cliff from 0.957 at α=5.5 to 0.122 at α=6.0. Seeds 0 and 1 give bit-identical µ for every aid (`training_seed*.csv`): with `support_fraction=0.999` the MCD fit does not depend on its random start here, so the "unseeded" risk in the reconstruction did not materialise.

### Q1: Mean and Binning are blind to masquerade (`raw/q1.json`)

| Detector | Recall on each of the 13 masquerade logs | Aggregate FPR | TPs |
|---|---|---|---|
| Mean α=0.444, 3 of 6 | 0.0000 on all 13 | 9.2e-4 | 0 of 30,731 |
| Binning α=3.5 | 0.0000 on all 13 | 5.4e-4 | 0 of 30,731 |
| Gaussian p=0.09, 3 consecutive | 0.000 to 0.833; above 0.01 on 6 of 13 | 1.77e-2 | 1,258, precision 0.047 |

In-interval target-aid gap medians match the trained µ for 0xD0 (e.g. 0.01000 vs µ 0.01000). The clear exception is the coolant masquerade (0x4E7: median 0.1139 s in the interval vs µ 0.1001), where the injector runs about 14% slower than the ECU. For 0x6E0 the in-interval median matches µ (0.01001–0.01004), so its Gaussian hits must come from the spread of the injected gaps rather than the period; that spread was not measured. Gaussian's two-sided test catches some of this: 35 of 42 frames on coolant, 27% and 20% on correlated_signal 1 and 2. Few of its hits fall within 5 frames of the interval edges overall (15 of 1,258, `tp_within5_of_edge`), so most are not boundary effects; the coolant log is the exception, with 9 of its 35 hits near the edges. Mean and Binning only fire on "too fast", so they cannot see a slower stream at all. Gaussian's per-log precision is 0.00–0.32, so this is a real signal and not yet a usable detector.

### Q2: the sufficiency rule drives most of the Gaussian gap, by a different mechanism than predicted (`raw/q2.json`, `raw/diag_gauss_max_speedometer_attack_1.json`)

| Variant | Best F1 over its sweep | At the published p/α |
|---|---|---|
| Gaussian, 3 consecutive (published) | 0.2599 (p=0.09) | 0.2599 |
| Gaussian, 3 of 6 | **0.9157** (p=0.007; P 0.847, R 0.997) | p=0.09: 0.5805 (P 0.409, FP 88,764) |
| Mean, 3 of 6 (published) | 0.9862 (α=0.444) | 0.9862 |
| Mean, 3 consecutive | 0.8069 (α=0.944) | α=0.444: **0.0432** (R 0.022) |

Isolated-flag share among flagged in-interval target frames (9 captures on 0xD0): Mean 0.88–0.998, Gaussian **0.09–0.32**.

The diagnostic shows why. For 0xD0, the trained σ/µ is 0.149, and p=0.09 flags |z| ≥ 1.70. Flam frames arrive about 0.2µ after each legitimate frame. Every injected frame is flagged (rate 1.00); legitimate frames inside the attack are flagged only 39% of the time, because their gaps (0.54–1.15µ) straddle the band edge at 0.745µ. Flag runs inside the interval are mostly length 1 (547) or length 3 (937; injected, legitimate, injected). "3 consecutive" therefore fires once per length-3 run (937 of the 962 alerts on 4,888 in-interval frames; the 7 longer runs add 25). Over all 16 logs at the same p, "3 of 6" recalls 0.999 of positives. So the mechanism is not a strict flagged/unflagged alternation. It is that "3 consecutive" needs a legitimate frame's gap to fall outside the band, and then still alerts on only one frame per length-3 run.

### Q3: half of the published positives are legitimate frames (`raw/q3.json`)

- Payload labels keep exactly 50.00% of positives in **every** one of the 13 targeted logs (61,462 → 30,731). For every log, the number of dropped positives equals the line-count difference between the fabrication log and its `_masquerade` twin (e.g. 2,444 for max_speedometer_attack_1), i.e. exactly the legitimate frames ROAD removed. This is an independent cross-check on the relabeling. Fuzzing keeps its 54 exact-payload positives.
- At the published optima with payload labels, all 16 logs: Mean P 0.4875, R 0.9936, F1 0.6541; Binning P 0.4921, R 0.9888, F1 0.6572 (vs 0.986 and 0.989). The windowed alert covers the legitimate frames between injections, so they become false positives.
- Flam delay δ (payload frame minus previous same-aid frame): median 2.0 ms on 0xD0 (µ 10.0 ms), p99 3.1 ms; 2.0–3.0 ms on 0x6E0; 25.6 ms on 0x4E7 (µ 100 ms). So δ ≈ 0.2–0.3µ.

## Observations vs prediction

| Prediction | Observed | Verdict |
|---|---|---|
| R0 Mean and Binning within ±0.002 F1 and ±1% per cell; rows and positives exact | every cell identical, both seeds; Gaussian near-identical (TP/FN equal, 26,040 vs notebook 26,026 FP, F1 0.25995 vs 0.25998) | confirmed, more strongly than predicted |
| Q1 Mean, Binning recall ≤ 0.01 on every masquerade log; FPR ~1e-3 | recall 0 on all 13; FPR 9e-4 and 5e-4 | confirmed |
| Q1 TPs cluster at interval edges | there were no TPs to cluster | moot |
| Q1 Gaussian ≤ 0.01 | above 0.01 on 6 of 13, up to 0.83 on coolant (precision ≤ 0.32) | **wrong**: the two-sided test sees a slower injector (0x4E7) and some 0x6E0 frames |
| Q2 Mean 3 consecutive at α=0.444 ≤ 0.40 (guess < 0.2) | 0.043 | confirmed; but at α=0.944 it reaches 0.807, so the swap is threshold-dependent |
| Q2 Gaussian 3 of 6 at p=0.09 ≤ 0.83 (subset bound; reconstruction said ≥ 0.85) | 0.58 | my bound confirmed; reconstruction's p=0.09 figure wrong |
| Q2 Gaussian 3 of 6, best over sweep ≥ 0.85 | 0.916 at p=0.007 | confirmed: hypothesis supported |
| Q2 > 80% of Gaussian flags isolated | 9–32% (Mean: 88–99.8%) | **wrong**: mechanism is band-straddling legitimate gaps, not alternation |
| Q3 payload labels keep 40–60% | exactly 50% in all 13 | confirmed |
| Q3 precision < 0.65, recall > 0.95 | P 0.49, R 0.99 | confirmed |
| Q3 δ median well under 1 ms | about 2 ms (0.2µ) on 0xD0 and 0x6E0; 25.6 ms on 0x4E7 | **wrong** |

## Limits

- Real data, but offline replay of one vehicle's dynamometer captures, in batch, on a laptop. It says nothing about ORNL's Raspberry Pi 3B+ OBD-II plug-in (whose code is not public), live bus timing, latency, or other vehicles.
- The detectors are my re-implementation. They are tied to the pinned code by exact equivalence on small inputs and by exact reproduction of the published matrices, but the full-scale run did not execute ORNL's functions.
- Train and test come from the same car and capture campaign. ROAD IDs and payloads are obfuscated, so signal semantics are not checked.
- Q1 labels assume every in-interval target frame in a masquerade log is injected, which follows ROAD's construction (and the line-count match in Q3), not ground truth per frame.
- Q2 tests one alternative rule per detector. It does not show that 3 of 6 is optimal, and it does not separate tail shape from rule for KDE, which was skipped.
- Q3 shows the published F1 depends on an unstated labelling convention. It does not show the paper is wrong: "every frame of an attacked stream" is a defensible unit. Payload labels have their own blind spot, since a legitimate frame that happens to match the pattern would count as an attack (none did here, by the line-count match).
- The "with outliers" column of Table II and the PR-AUC values were not recomputed.

## Next

The two-sided Gaussian caught most of the coolant masquerade, where the injector runs about 14% slower than the ECU, and part of the correlated-signal ones. Can a deliberately one-sided "too slow / period drift" test on the target aid (for example, Binning's 6-gap sum checked against an upper bound) detect those masquerades at FPR ≤ 1e-3 on the same data, and does it stay blind on the 0xD0 masquerades, whose period matches?
