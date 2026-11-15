# Time-Based CAN IDS Benchmark: code reconstruction

Lead ids: `can-time-ids-benchmark` (code), `road-can-dataset` (data). Catalog context: [projects/can-d.md](../../projects/can-d.md).
Reader pass, 2026-11-15. Everything here comes from reading the code, the saved notebook outputs and the two public papers. Nothing in the checkout was executed.

## Pin and sources

| Item | Value | Tag |
|---|---|---|
| Repo | https://github.com/pmoriano/can-time-based-ids-benchmark | [KNOWN] |
| Pinned commit | `e0c862d6c6cbb0d60ed2572a90dd483a3253ed0f`, committed 2022-01-18 09:16 -0500, "Update notebook folder name". This is HEAD and the only branch | [KNOWN: `git log --all`, accessed 2026-11-15] |
| Local checkout | `.cache/src/can-time-ids-e0c862d/` (untrusted, read only) | [KNOWN] |
| License | GPL-3.0 full text, `LICENSE` added in 502bd3d | [KNOWN: LICENSE @ e0c862d] |
| DOE CODE | code_id 69319: site_ownership_code ORNL, developer affiliation ORNL, research_organizations empty, GPL-3.0, release 2022-01-17, DOI 10.11578/dc.20220112.2 (record page JSON export link, re-fetched by referee 2026-11-15) | [KNOWN] |
| Companion paper | Blevins, Moriano, Bridges, Verma, Iannacone, Hollifield, "Time-Based CAN Intrusion Detection Benchmark", AutoSec 2021 workshop (NDSS), arXiv:2101.05781v1, 14 Jan 2021, https://arxiv.org/abs/2101.05781 | [KNOWN: PDF fetched 2026-11-15] |
| Dataset | ROAD, Zenodo record 10462796 (DOI 10.5281/zenodo.10462795), `road.zip`, 556,718,276 bytes, md5 `cab184cfc2fe12c0834bc46188c0f330`, CC BY 4.0, publication date 2020-12-28 | [KNOWN: Zenodo API https://zenodo.org/api/records/10462796, accessed 2026-11-15] |
| Dataset paper | Verma et al., ROAD, arXiv:2012.14600v3 (7 Feb 2024; PLOS ONE version) | [KNOWN: PDF fetched 2026-11-15] |

Citation form: `path:Lx-Ly @ e0c862d`. For the notebook, line numbers are raw JSON lines in `notebook/time-base-detector.ipynb`, and the cell index is given too.

## What it is, in one paragraph

The repository is one Jupyter notebook plus one helper module. The notebook trains four per-arbitration-ID timing detectors on the 10 ROAD dynamometer ambient logs. It then scores the 16 ROAD fabrication-attack logs (fuzzing plus five flam-delivery targeted-ID attacks), sweeps a threshold for each detector and plots precision-recall curves, which are the paper's Table II and Fig. 2. **It does not evaluate masquerade or accelerator captures.** The notebook says those are out of scope (markdown cell 15, `notebook/time-base-detector.ipynb:L1518-L1520 @ e0c862d`), and the paper says so too: masquerade and accelerator attacks "do not alter timing characteristics and are thus out of scope" (arXiv:2101.05781 §II-A). [KNOWN]

## Repo layout and engineering checklist

- **Layout**: `README.md`; `LICENSE`; `.gitignore`; `code/helper_functions.py` (902 lines, 45 functions); `notebook/time-base-detector.ipynb` (85 cells, outputs saved); `figs/*.pdf` (10 figure PDFs that match the paper's figures). [KNOWN: `ls`, `grep -c "def "` @ e0c862d]
- **Language and dependencies**: Python. Imports are numpy, pandas, matplotlib, scikit-learn (`EllipticEnvelope`, `confusion_matrix`, `precision_recall_fscore_support`, `auc`), scipy (`stats.gaussian_kde`, `stats.norm`, `integrate.quad`) and tqdm, plus stdlib json, pickle, bisect and re (`code/helper_functions.py:L1-L26`, notebook cell 0 `:L8-L31 @ e0c862d`). There is no requirements file, setup.py or environment file, so **no versions are pinned**. [KNOWN]
  - Version evidence: the notebook kernelspec says Python 3.8.8 (notebook metadata), but a saved traceback shows `env/lib/python3.6/site-packages/pandas` (`:L2075 @ e0c862d`). The saved outputs therefore came from at least two environments. [KNOWN]
  - The repr `scipy.stats.kde.gaussian_kde` in the output of cell 60 points to scipy older than about 1.8, before the module became `_kde`. [INFERRED]
- **Build**: none. The README tells users to create `data/` in the repo and "dump the content of the ROAD dataset in there". It links https://0xsam.com/road/, not Zenodo (`README.md:L5 @ e0c862d`). [KNOWN]
- **Tests**: none. There is no test folder and no test functions. [KNOWN]
- **CI**: none. There is no `.github/` or any CI config. [KNOWN: `ls -a`]
- **Releases**: no tags and no GitHub releases. There are 7 commits, all on 2022-01-17 and 2022-01-18. The first commit (4ec6b7c) adds all code and figures; the rest touch the README or LICENSE, or rename `notebooks/` to `notebook/`. Two author spellings appear for one person. [KNOWN: `git log --stat`]
- **Contribution path**: no CONTRIBUTING file, code of conduct or issue templates. [KNOWN]
- **Data and reproducibility**: no data or pickles are shipped. `.gitignore` excludes `*.pkl`, `*.log`, `data*/`, `/exploratory` and `*.zip` (`.gitignore:L1-L11 @ e0c862d`). The notebook depends on pickles it only loads, which the repo does not contain (see the hidden-state section). [KNOWN]
- **Deployment statement**: the paper says the Binning detector was implemented as an OBD-II plug-in prototype on a Raspberry Pi 3B+ with a CANBerry Dual 2.1 board, with a demo video. The prototype code is **not** in this repo. [KNOWN: arXiv §III-A; repo contents]
- **Why it was built this way**: [UNKNOWN] beyond the paper's stated motivation, which is to benchmark simple time-based detectors on real flam attacks.

## Data flow

1. **Parse** (`make_can_df`, `code/helper_functions.py:L96-L115 @ e0c862d`). `pd.read_fwf` reads candump lines `(ts) can0 ID#DATA`. It keeps time, aid and data, and **drops the first and last line of every log** (`skiprows=1, skipfooter=1`). It parses hex aids, zero-pads the data to 16 hex characters, re-zeroes time to the earliest remaining row and **keeps only `aid <= 0x700`**. That filter also removes ROAD's `0xFFF` "filler" frames. [KNOWN code; the filler interaction is INFERRED from the ROAD paper §4.2]
2. **Feature** (`add_time_diff_per_aid_col`, `:L192-L205`). The frame is sorted by `(aid, time)`. `time_diffs` is the gap from the previous frame with the same aid, and the first frame of each aid is dropped. The order stays aid-major, not time order. This is the only feature: the per-aid inter-arrival time. [KNOWN]
3. **Train** (`train`, `:L289-L311`). For each aid, `EllipticEnvelope(contamination=0.0001, support_fraction=0.999)` removes outliers from the 1-D inter-arrival times. The stored values are `mu`, `std`, `scipy.stats.gaussian_kde(time_diffs)` and `norm(mu, std)`. No `random_state` is set, so the MCD subset search is not seeded. `train_no_preprocessing` (`:L313-L335`) is the same without the outlier step. [KNOWN]
   - Training data comes from cell 6 (`:L252-L271`): every file in `data/ambient` whose name contains `dyno`, which is 10 logs and 13,300,759 rows after differencing. The cell is **commented out**, yet its saved output is present. Cell 8 writes `aggregated_training_data.csv` and cell 10 reads it back (`:L420-L427`). Training covers 105 aids (cell 12 `:L1480-L1497`, output "105/105"). [KNOWN]
4. **Test set** (cell 17, `:L1569-L1584`): every file in `data/attacks` whose name contains neither `masquerade`, `accelerator` nor `metadata`, which gives 16 logs. The `attacks` folder held 34 entries in total, per tqdm `0/34` in cell 57, meaning 33 captures plus `capture_metadata.json`. [KNOWN]
5. **Labels** (cells 21 and 27, `:L1784-L1812`, `:L1974-L1996`; `add_actual_attack_col`, `:L255-L265`). The injection interval is read straight from `capture_metadata.json["<capture>"]["injection_interval"]`. A payload-based interval finder (`get_injection_interval`, `:L224-L252`) exists but is commented out in the notebook. A frame is labelled an attack when it falls inside the interval **and** `aid == injection_id`. For fuzzing, where `injection_id == "XXX"`, the condition is instead `data == injection_data_str` by exact string match. [KNOWN]
6. **Score, sweep and save**. The `get_results_*` functions apply a detector to every test frame, aggregate one confusion matrix across all 16 files, compute precision, recall, F1 and FPR, and pickle the results to `os.path.dirname(os.getcwd())`, which is `data/` (`:L591-L619`, `:L653-L676`, `:L706-L735`, `:L801-L827`). [KNOWN]
7. **Plot**. Cell 79 (`:L6248-L6281`) computes PR-AUC with `sklearn.metrics.auc` over the swept (recall, precision) points and draws a hard-coded baseline of 0.039. [KNOWN]

## The four detectors, exactly as coded

Notation: `x` is a frame's inter-arrival time for its aid. `mu` and `std` come from training after outlier removal.

| Detector | Step 1 (per frame) | Step 2 (sufficiency) | Swept threshold | Paper optimum (code agrees) | Code |
|---|---|---|---|---|---|
| **Mean** | `x <= p*mu` | alert if at least 3 of the last 6 frames (in df row order) are flagged: `rolling(6).sum() >= 3` | `p in linspace(0,1,19)` = i/18, i=0..18 | p=0.444 (8/18): F1 0.9862, P 0.9765, R 0.9961, FPR 0.00096; CM `[[1525274,1473],[239,61277]]` | `alert_by_mean_various_p` `:L391-L396`; `get_results_mean_various_p` `:L591-L619`; output `:L2922`, `:L2964` |
| **Binning** | none (no step 2) | for each aid separately, alert if the sum of the **last 6 inter-arrival gaps** is at most `p*mu` | `p in linspace(1,10,19)` = 1, 1.5, ..., 10 | p=3.5: F1 0.9889, P 0.9862, R 0.9916, FPR 0.00056; CM `[[1525895,852],[514,61002]]` | `alert_by_bin_various_p` `:L524-L538`; `get_results_binning_various_p` `:L801-L827`; output `:L3069`, `:L3114` |
| **Gaussian** | two-sided "p-value" of `x` under `norm(mu,std)` is at most p | alert if 3 **consecutive** frames are flagged: `rolling(3).sum() == 3` | {0.001..0.009} ∪ {0.01..0.09} (18 values) | p=0.09: F1 0.2600 (P 0.334, R 0.213) | `y_threshold_gauss` `:L366-L380`, `alert_by_gauss` `:L444-L449`, `get_results_gauss` `:L706-L735`; output `:L4123` |
| **KDE** | the same p-value under `gaussian_kde` (Scott bandwidth, the scipy default) | 3 consecutive, as for Gaussian | {0, 0.001..0.009, 0.01..0.09} (19 values) | p=0.09: F1 0.2779 (P 0.367, R 0.224) | `y_threshold_kde` `:L348-L363`, `alert_by_kde` `:L420-L425`, `get_results_kde` `:L653-L676`; output `:L6166` |

All of the above is [KNOWN] from the code and saved outputs.

How the p-value is computed (`:L355-L363`, `:L374-L380`). The density is evaluated on a 1000-point grid over `[mu-5std, mu+5std]`. For each grid point it sums the densities of all points at or below that point's density, times the step `10*std/1000`. That is a Riemann approximation of paper Eq. 1, `P_f({t: f(t) <= f(x)})`. The threshold `y` is the largest density whose approximate tail mass is at most p, and a frame is flagged when `f(x) <= y`. Probability mass outside ±5σ is ignored, and anything out there has near-zero density, so it is always flagged. The test is two-sided, so a frame can be flagged for arriving too late as well as too early. [KNOWN code; the interpretation is INFERRED]

PR-AUC from saved output (`:L6229-L6232`): Mean 0.6905, Binning 0.8218, Gaussian 0.0899, KDE 0.1388. These match the paper's Table II **"Without Outliers"** column exactly (69.05, 82.18, 8.99, 13.88). [KNOWN]

Positives: 61,516 attack frames out of 1,588,263 (`:L4186`), matching the paper §II-A2. [KNOWN]

## Paper claims vs what the code computes

1. **Binning window is off by one between the text and the code.** The paper says it labels a frame malicious "when the last six frames arrived in less than αiµ seconds" (§II-B2), and its latency analysis "stores the previous five message times" (§II-C). That is 6 frames and 5 gaps. The code sums `rolling(6)` of `time_diffs`, which is 6 gaps spanning 7 frames (`:L534`). The saved sweep supports the code's version: F1 falls off a cliff between p=5.5 (0.957) and p=6.0 (0.122) (`:L3073-L3074`). That is where a 6-gap sum of about 6µ crosses the threshold. With 5 gaps the cliff would sit near 5. [KNOWN code and output; that the cliff confirms 6 gaps is INFERRED]
2. **The "with outliers" column is not reproducible from the notebook as shipped.** Cell 82 (`:L6313-L6357`) only *loads* `results_*_no_pretraining.pkl`. No cell builds a training dictionary with `train_no_preprocessing`, and no cell calls any `get_results_*_no_pretraining` function (grep over the notebook returns nothing). The helper functions exist (`:L622-L650`, `:L679-L703`, `:L738-L767`, `:L829-L855`) but are never wired up. [KNOWN]
   - Cell 82's comment `# Without outliers` sits above the `no_pretraining` loads. Those files are actually the *with outliers* results. The panel order (a = no_pretraining) still matches the paper's Fig. 2 (a) "with outliers". This is a comment mislabel, not a result error. [KNOWN code; INFERRED reading]
3. **Labels count legitimate target-ID frames as attacks.** For every non-fuzzing capture, `add_actual_attack_col` labels *all* frames of the target aid inside the interval as attacks (`:L260-L261`). The payload is ignored. Under flam delivery, each injected frame follows a legitimate one, so roughly half of the "attack" frames are real ECU frames. A rough check: 0xD0 at about 100 Hz (paper Fig. 1, µ≈0.010 s) over the 9 captures that target 0xD0 (about 252 s of intervals, from the saved interval list at `:L1837` onward) gives about 25k legitimate plus about 25k injected frames. 0x6E0 at a similar rate over about 55 s adds roughly 5.5k plus 5.5k. Together with the coolant and fuzzing captures this lands near the observed 61,516, which is consistent with legitimate and injected frames both being counted. [KNOWN code; the about-2x composition is INFERRED arithmetic for the experimenter to verify] The ROAD paper itself suggests labelling with injection ID, **data** and intervals (arXiv:2012.14600 App. 6.2). Neither paper states which labelling convention was used. [UNKNOWN]
4. **The paper's alerts-per-minute figure looks miscalculated.** The paper estimates "0.014 × 1.6/12.3M = 1,821 alerts per minute" from 1 − precision. But 1 − precision is the fraction of *alerts* that are false, not of messages. The notebook's own confusion matrix at Binning p=3.5 has 852 false positives in total (`:L3114`), which over about 12.3 minutes is **about 69 false alerts per minute** (about 5,000 total alerts per minute). The paper's qualitative point, that the false alarm volume is still too high, survives, but the number does not follow from the data. [KNOWN numbers; INFERRED that it is an error]
5. **The paper's explanation for Gaussian/KDE failure vs the code's sufficiency rule.** The paper attributes the poor Gaussian and KDE results to their tails being "insufficient to characterize" the timing (§IV), and notes that flam attacks make the attack inter-arrival times bimodal. In the code, Mean and Gaussian/KDE differ in **two** ways at once: the comparison statistic, and the sufficiency rule (3 of 6 vs 3 consecutive). Under flam delivery the target aid's gaps alternate between δ (injected right after legitimate) and µ−δ. A two-sided test flags δ but usually not µ−δ, so "3 consecutive" is rarely met inside an attack, while "3 of 6" is met easily. My hypothesis is that the sufficiency rule, not the distribution choice, drives most of the gap. This is testable (see experiment question 2). [INFERRED]
6. **Thresholds.** Mean: the paper says i/18 for i=1..18, the code also includes 0 (F1 nan). Binning: the paper says (2+i)/2 for i=1..18, i.e. 1.5..10, and the code also includes 1. These match up to an extra endpoint. [KNOWN]
7. **Durations.** The paper says the test set was "~12.3 minutes"; the Table I fabrication durations sum to 11.6 minutes. This is a minor inconsistency. [KNOWN arithmetic]

## Hard-coded values and hazards

- **Paths.** The notebook `chdir`s to `dirname(cwd)+"/data/ambient"`, then `"/data/attacks"` (cells 2 and 16), so it must start from `notebook/`. Results pickles go to `data/`, and figures to `../../figs/` (cells 46 and 48). Saved outputs reveal the authors' local path. [KNOWN]
- **Magic numbers.** Outlier contamination 0.0001 and support fraction 0.999. Aid cap 0x700. Mean window 3 of 6. Binning n=6. Gaussian/KDE 3 consecutive. Grid ±5σ with 1000 steps. Optima hard-coded in the plotting cells (0.4444444444444444, 3.5, 0.09). Baseline 0.039. [KNOWN: cells 50, 54, 63, 77, 79]
- **Hidden state and execution order.** Execution counts are non-monotonic (for example cell 32 is 18, cell 17 is 21, cell 57 is 29, cell 69 is 42) and file listing orders differ between runs (cell 17 vs cell 57). The saved outputs therefore come from several kernel sessions. The final KDE and Gaussian numbers depend on `training_dict.pkl` and `df_aggregation_final.pkl`, which were loaded rather than recomputed (cells 69 and 73). [KNOWN]
- **`os.listdir` order coupling.** `df_aggregation[count]` and `attack_metadata[count]` are aligned only by running the same `listdir` loop repeatedly (cells 17, 21 and 27). Order is stable within one process on one filesystem, but not guaranteed by spec. A new driver should key by file name. [INFERRED risk]
- **Value-to-row alignment.** `add_kde_val_col` and `add_gauss_val_col` concatenate per-aid arrays in `df.aid.unique()` order (`:L273`, `:L284`). That is correct only because the frame is sorted aid-major. Calling `add_time_diff_per_aid_col(order_by_time=True)` would silently misalign the scores. [KNOWN code; INFERRED hazard]
- **Windows cross aid boundaries.** Mean, Gaussian and KDE apply `rolling` to the whole aid-sorted frame, so the first 2–5 frames of each aid share a window with the previous aid. Binning filters per aid first (`:L533`). With about 105 aids and 16 files the effect is small. [INFERRED]
- **Unseen aids raise KeyError.** `d[row.aid]` (`:L387`, `:L273`) has no guard. Each test file showed 104–105 aids, no more than training's 105, so this never triggered. How ROAD fuzzing frames (which cycle IDs, per arXiv:2012.14600 §4.1.1) fit within the trained aid set is [UNKNOWN] without the data.
- **numpy 2 / modern pandas breakage risk.** `np.where(...)[0] != []` (`:L360`) relies on old elementwise-comparison behaviour. `df.count()[0]` (`:L404`) relies on positional `[]` (that function is unused). `y_threshold_gauss` calls `np.max` on a possibly empty array (`:L379`). [INFERRED]
- **Dead or broken code.** The J1939 functions (`:L117-L170`, `:L338-L345`, `:L541-L556`, `:L858-L885`) are unused. `print_details` references an undefined `name` (`:L895`). `get_results_mean` and `get_results_mean_various_p` both write `results_mean_final.pkl`, and both binning variants write `results_binning_final.pkl`, so they overwrite each other. `get_results_kde` initialises its result dictionary from its own `pvals_kde` but loops over the `pvals` argument (`:L659-L665`). [KNOWN]
- **Cost.** Saved tqdm timings: training 25 s; Gaussian thresholds 7 m 45 s (`:L3774`); KDE thresholds 1 h 39 m (`:L6037`); KDE scoring 3 h 37 m (`:L5543`). The code's own comments estimate Mean at about 35 s per threshold and Binning at about 10 s. [KNOWN]

## ROAD layout as the code expects it

- `data/ambient/`: 12 ambient logs. Training uses the 10 with `dyno` in the name: `ambient_dyno_{exercise_all_bits, reverse, drive_basic_short, drive_basic_long, drive_radio_infotainment, drive_winter, drive_extended_short, drive_extended_long, idle_radio_infotainment, drive_benign_anomaly}.log` (cell 3 output, `:L66-L75`). [KNOWN]
- `data/attacks/`: 33 attack logs plus `capture_metadata.json`, whose keys are the log names without `.log`. Each entry has `injection_id` (hex or `XXX`), `injection_data_str` (hex with `X` wildcards), and `injection_interval` [start, end] in elapsed seconds. [KNOWN: code; ROAD App. 6.2]
- The 16 fabrication logs used: `correlated_signal_attack_{1,2,3}` (target 0x6E0), `reverse_light_off_attack_{1,2,3}`, `reverse_light_on_attack_{1,2,3}`, `max_speedometer_attack_{1,2,3}` (all 0xD0), `max_engine_coolant_temp_attack` (0x4E7), `fuzzing_attack_{1,2,3}` (`XXX`) (cell 21 output). [KNOWN]
- The 13 masquerade logs are the targeted-ID captures above "with the ambient frames of the target ID removed during the attack period" (ROAD §3 and §4.1.2). Their exact file names, presumably containing `masquerade`, are not printed anywhere in the notebook. [INFERRED from the filter string; exact names UNKNOWN]
- The internal folder structure of `road.zip` (whether it matches `ambient/` and `attacks/` under one root) is not listed by the Zenodo API. [UNKNOWN; the experimenter should run `unzip -l` first]
- Timestamp accuracy is 100 µs (Kvaser Leaf Light V2). IDs and payload bytes are obfuscated consistently across logs (ROAD §4.2–4.3). [KNOWN]

## Known / Inferred / Unknown summary

- **KNOWN**: detector definitions and thresholds; training and test file sets; labelling rule; saved numbers matching Table II "without outliers"; no tests, CI, releases or pinned dependencies; masquerade excluded; the with-outliers column is not wired in the notebook.
- **INFERRED**: the binning 6-vs-5-gap mismatch, as read from the F1 cliff; about half of the positives being legitimate frames; the alerts-per-minute miscalculation; the sufficiency rule rather than the distribution choice explaining the Gaussian/KDE failure; library version ranges.
- **UNKNOWN**: the exact `road.zip` paths and masquerade file names; fuzzing `injection_data_str` and how many fuzzing frames are labelled; how fuzzing IDs relate to the trained aid set; flam injection delay δ; whether the labelling convention was a deliberate choice; the OBD-II prototype's code.

## Experiment design (for the experimenter)

**Important reframing.** No published result on ROAD *masquerade* attacks exists for this code. The paper and notebook both exclude them, and ROAD's own paper predicts frequency methods "will almost certainly fail" on them (§4.1.2). So the plan has two parts. First, reproduce a published fabrication result to validate the pipeline. Second, run the same trained detectors on the masquerade captures as a *new* boundary measurement.

### Smallest reproducing run

Target: the **Binning detector at p=3.5** reproduces CM `[[1525895, 852],[514, 61002]]` and F1 0.9889. Also, cheaply, the **Mean detector at p=0.444** reproduces CM `[[1525274,1473],[239,61277]]` and F1 0.9862. Both come from the notebook outputs at `:L2964` and `:L3114` and match paper §III. Skip KDE, which takes over 5 hours. Gaussian is optional (about 8 minutes of thresholds).

Steps:
1. Unzip `road.zip` into a fresh directory outside the checkout.
2. Write a new driver script outside the checkout, sorting file names rather than using bare `listdir`. Either import `helper_functions.py` by path, or re-implement the six functions it needs: `make_can_df`, `add_time_diff_per_aid_col`, `train`, `add_actual_attack_col`, `alert_by_mean_various_p` and `alert_by_bin_various_p` (about 80 lines). Re-implementing avoids the module's pickle side effects. Do not run the notebook.
3. Training: parse the 10 `ambient_dyno_*` logs, add time diffs, concatenate, and run `train()` per aid.
4. Test: parse the 16 fabrication logs, label them from `capture_metadata.json`, and run Binning (n=6, p=3.5) and Mean (p=0.444, 3 of 6). Report the aggregate confusion matrices.
5. Pass criterion: F1 within ±0.002 and each confusion-matrix cell within ±1%. Exact equality is not expected, because `EllipticEnvelope` is unseeded (`:L298`), which shifts µ slightly, and the original run's library versions are unknown.

**Files needed from road.zip** (verify names with `unzip -l` first):
- The 10 `ambient/ambient_dyno_*.log` files listed above.
- The 16 fabrication logs listed above, in `attacks/`.
- `attacks/capture_metadata.json`.
- For the boundary tests: the 13 masquerade logs, `*masquerade*.log`.
- Not needed: the 2 road ambient logs, the 4 accelerator logs and the signal-translation CSVs.

**venv dependencies** (no pins exist upstream; these are my suggested period-appropriate pins [INFERRED]): Python 3.9, `numpy==1.23.5`, `pandas==1.5.3`, `scipy==1.9.3` (any version from 1.7 on works for `gaussian_kde` and `norm`), `scikit-learn==1.1.3`, `tqdm`. Add `matplotlib==3.6.x` only for figures. Avoid numpy 2 and pandas 2 (see hazards). No Jupyter is needed.

**Memory and time estimate** [INFERRED from saved row counts and timings]:
- Parsing: `read_fwf` with `skipfooter` forces the slow Python engine. About 14.9M raw lines (13.3M ambient plus 1.6M test) will likely take 10–30 minutes.
- Memory: peak about 3–5 GB, while the largest ambient log (about 4.1M rows with a string data column) is in memory. The concatenated training frame (time, aid, time_diffs) is about 0.3 GB. You can drop the data column before concatenating, since the notebook keeps only time, aid and time_diffs.
- Compute: training about 30 s; Binning at one threshold about 10 s; Mean at one threshold about 35 s (row-wise `apply`).
- Totals: about 30–45 minutes on an 8 GB laptop, with 16 GB comfortable. The masquerade pass adds roughly 5 minutes. Disk: 557 MB zip; unzipped size [UNKNOWN], likely a few GB.

### Failure-boundary questions (each with a falsifiable prediction)

**Q1. Can the timing detectors see a masquerade at all?** Run the trained Mean (p=0.444, 3 of 6) and Binning (p=3.5) on the 13 masquerade logs. Label every frame of the target aid inside the interval; here they are all injected, because the legitimate ones were removed.
*Prediction:* recall at most 0.01 on every masquerade capture. The FPR stays at the fabrication-run level (on the order of 1e-3), and any true positives cluster within one or two frames of the interval start or end, where one gap stretches to µ+δ or shrinks to µ−δ. *Falsified if* any masquerade capture gives recall above 0.05 for either detector.
Secondary check: for the two-sided Gaussian (p=0.09, 3 consecutive) on 0xD0, where σ≈0.001 s, also predict recall at most 0.01. A late-gap test could in principle catch the boundary stretch, but cannot meet "3 consecutive".

**Q2. Is the Gaussian/KDE failure caused by the sufficiency rule, not the distribution?** On the 16 fabrication logs, swap the sufficiency rules. Run Gaussian (p=0.09) with Mean's "3 of last 6", and Mean (p=0.444) with Gaussian's "3 consecutive".
*Prediction:* Gaussian with 3 of 6 reaches F1 of at least 0.85, up from 0.26. Mean with 3 consecutive drops to F1 of at most 0.40, down from 0.986. The reason is that flam delivery produces alternating δ / (µ−δ) gaps, which "3 consecutive" cannot match. *Falsified if* Gaussian with 3 of 6 stays below 0.5 F1. That outcome would support the paper's tail-shape explanation instead.
Cheap supporting measurement: in one 0xD0 fabrication capture, compute the per-frame Gaussian flags inside the interval and report the fraction of flagged frames whose immediate neighbours are unflagged. The prediction is above 0.8.

**Q3. How much do the published numbers depend on the labelling convention?** Relabel the 13 targeted-ID fabrication captures using payload as well. Mark as positive only frames whose data matches `injection_data_str`, with `X` turned into a regex `.` (the commented-out `get_injection_interval` logic, `:L234-L237`). Re-score Mean and Binning.
*Prediction:* positives fall to 40–60% of the current count for those captures, consistent with about one injected frame per legitimate one. Precision at the published optima falls below 0.65, because the windowed alerts also cover the legitimate frames between injections, while recall stays above 0.95. *Falsified if* payload labels keep more than 75% of the original positives, or precision stays above 0.9.
Side output: measure the flam delay δ directly, as the gap from each payload-matched frame to the preceding same-aid frame. Report the median and 99th percentile. This also parameterises Q1.

**Optional Q4 (periodicity).** Group the false positives of Mean and Binning on the fabrication run by aid, against each aid's training coefficient of variation (std/mu after outlier removal). *Prediction:* more than half of all false positives come from the aids in the top quartile of CV, i.e. the least periodic IDs. *Falsified if* false positives are spread proportionally to frame counts.

### What the experimenter should log

The pinned SHA; the `road.zip` md5 (expected `cab184cfc2fe12c0834bc46188c0f330`); `unzip -l` output; `pip freeze`; the per-file and aggregate confusion matrices; wall time and peak RSS. Note that ROAD is CC BY 4.0, so attribute it in any write-up.

## Sources

- Repo @ e0c862d, cloned 2026-11-15: https://github.com/pmoriano/can-time-based-ids-benchmark. Supports all code claims.
- Blevins et al., "Time-Based CAN Intrusion Detection Benchmark", arXiv:2101.05781v1, AutoSec 2021, https://arxiv.org/abs/2101.05781, accessed 2026-11-15. Supports the detector definitions, Table II, the optima, the plug-in claims and the masquerade exclusion.
- Verma et al., ROAD, arXiv:2012.14600v3, https://arxiv.org/abs/2012.14600, accessed 2026-11-15. Supports the dataset composition, masquerade construction, fuzzing payload, obfuscation and metadata fields.
- Zenodo record API, https://zenodo.org/api/records/10462796, accessed 2026-11-15. Supports the file size, md5, license and date.
- discovery/leads.csv rows `can-time-ids-benchmark` and `road-can-dataset`. Supports the DOE CODE 69319 attribution (re-fetched by the 2026-11-15 referee).
