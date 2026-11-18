# Signal Clustering Similarity CAN Masquerade Detector: artifact study

Lead id: `can-signal-clustering-masquerade` (closed-source code, DOE CODE 134139). Data: `road-can-dataset`. Neighbours: [can-time-ids reconstruction](../can-time-ids/reconstruction.md) and [lab](../../atlas/labs/can-time-ids-road/README.md), whose Q1 found the timing detectors had recall 0 on all 13 masquerades.
Reader pass, 2026-11-15. This is an artifact study. **ORNL's code for this detector is not public.** DOE CODE lists it as closed source with no repository link. Everything below comes from the paper, its OSTI and DOE CODE records, the ROAD zip listing and readme, and one *different*, later, public ORNL repository that implements a windowed variant. Anything the experimenter builds is an **independent rebuild of the published method, not ORNL's code**. Wherever the paper is silent, the implementation details stay [UNKNOWN] or are marked [INFERRED] as my recommendation. They are never ORNL's design.

## Pin and sources

| Item | Value | Tag |
|---|---|---|
| Software record | DOE CODE 134139, "Using Signal Clustering Similarity for Detecting CAN Masquerade Attacks". `open_source: false`, `project_type: CS`, no repository link, licenses empty. Site ownership ORNL; research org ORNL; one developer with ORNL affiliation; sponsor USDOE (AC05-00OR22725). Released 2024-07-10, DOI 10.11578/dc.20240710.1. The archived file is named `90000299-signal-clustering-detection zip file.zip`. | [KNOWN: https://www.osti.gov/doecodeapi/services/search/134139, accessed 2026-11-15] |
| What the record says the code does | "cluster these time series using agglomerative hierarchical clustering from benign and attack datasets ... using the CluSim method", then "provide and probability score for an intrusion" (record `description`) | [KNOWN, same source] |
| Paper | Moriano, Bridges, Iannacone (ORNL CSMD and CRID), "Detecting CAN Masquerade Attacks with Signal Clustering Similarity", AutoSec 2022 workshop at NDSS, 24 April 2022, DOI 10.14722/autosec.2022.23028, 8 pp. | [KNOWN: OSTI 1866690 full text via https://www.osti.gov/servlets/purl/1866690, PDF md5 `27f8aa0e05691288e8f67734c151b31a`, accessed 2026-11-15] |
| OSTI record | OSTI 1866690, research org ORNL, sponsor USDOE, three ORNL authors, conference "NDSS 2022" | [KNOWN: https://www.osti.gov/api/v1/records/1866690, accessed 2026-11-15] |
| arXiv versions | arXiv:2201.02665. **v2 (11 Mar 2022) matches the OSTI/AutoSec text word for word**, apart from the arXiv stamp. v1 (7 Jan 2022) has the same method and the same p-values (in Figs 3 to 7 insets), but lacks Table II, the Fig. 3 heatmap analysis, §IV-F detection evaluation, Table III and Fig. 5. | [KNOWN: word diff of pdftotext output of https://arxiv.org/pdf/2201.02665v1 and v2 against the OSTI PDF, accessed 2026-11-15] |
| Later public ORNL code (windowed variant, **not** this detector) | `pmoriano/benchmarking-unsupervised-online-IDS-masquerade-attacks`, HEAD `695a24e89dcbeee4b3eb9ef34484e4c731e4bb59` (2024-08-23, "Update README.md"), MIT License, DOE CODE 141444 (site ORNL, LDRD sponsor). Checkout at `.cache/src/bench-online-695a24e/`, read only, nothing executed. | [KNOWN: `git log`, `LICENSE`, `discovery/snapshots/doecode-2026-11-11.json` code_id 141444, accessed 2026-11-15] |
| CluSim library | `clusim` on PyPI, latest 0.4 (wheel uploaded 2020-05-13), MIT, https://github.com/Hoosier-Clusters/clusim. The paper cites Gates and Ahn, JOSS 4(35):1264 (2019) [25], and Gates et al., Sci. Rep. 9 (2019) [23] | [KNOWN: https://pypi.org/pypi/clusim/json; source files read from GitHub master, accessed 2026-11-15] |
| Dataset | ROAD `road.zip` in `.cache/data/road/` (md5 verified by the previous lab). Listed with `unzip -l` / `-v` and headers read through `unzip -p ... \| head -1`. Nothing extracted. | [KNOWN] |
| Related later paper | OSTI 3009491, Marfo, Moriano, Tosh, Moore, "Detecting Masquerade Attacks in Controller Area Networks Using Graph Machine Learning", IEEE TIFS 20 (2025) 13127-13142, DOI 10.1109/TIFS.2025.3636019 | [KNOWN: https://www.osti.gov/api/v1/records/3009491 and its purl full text, accessed 2026-11-15] |

Citation form: `p.N §X` for the OSTI PDF (8 pages). Code citations use `path:Lx-Ly @ 695a24e` and refer to the later windowed repository only.

## What it is, in one paragraph

This is a **forensic, whole-capture** detector, not an online IDS. The paper says it "is not a real-time detector" (p.7 §V, "Not real-time detection"). It turns every signal-translated CAN capture into one dendrogram. To do that it resamples all signals to a common 10 Hz grid, computes the Pearson correlation matrix between signals, and runs agglomerative hierarchical clustering (AHC) on that matrix. It then compares dendrograms pairwise with CluSim's element-centric similarity (r = −5.0, α = 0.9). Benign-vs-benign similarities form one distribution, and attack-vs-benign similarities form another. A Mann-Whitney U test at 0.05 decides whether they differ. [KNOWN: p.2 §III; p.4 §III-D1 to D5] The evaluation used ROAD's 12 ambient and 13 masquerade signal captures. With Ward linkage all five masquerade attack types were significant, and a 220-fold hold-out experiment gave recall 92.7 to 100% at an overall false positive rate of 13.64% (p.5 Table II; p.6 Table III, §IV-F). The paper calls the tool "a proof of concept" (abstract, p.1). The maturity verb is **tested** on one vehicle's recorded data. No deployment is claimed, and the paper names "no baseline comparison" as a limitation (p.7 §V). [KNOWN]

## Lineage: how the three ORNL artifacts relate

1. **2022 forensic detector (this study).** Whole-file dendrograms and a file-level hypothesis test. Closed-source code (DOE CODE 134139, registered 2024). [KNOWN]
2. **2024 online benchmark (public, MIT, DOE CODE 141444).** Sliding-window correlation matrices compared with a single training dendrogram. Its README says that "the method that relies on detecting changes at the hierarchical structure of clusters of time series produces the best results at the expense of higher computational overhead" (`README.md:L3 @ 695a24e`). It shares the CluSim call pattern, the Ward linkage and r = −5. Whether its code was derived from the closed 2022 code is [UNKNOWN]. That shared calls imply shared code is [INFERRED] only, and authorship proves participation, not ownership.
3. **2025 TIFS graph-ML paper (OSTI 3009491).** A *different* method: message-sequence graphs with shallow graph embeddings plus statistical time-series features, run over sliding windows. Its related-work section cites the 2022 paper as prior work: "Moriano et al. [4] focused on detecting masquerade attacks ... Using hierarchical clustering". It also cites the 2024 benchmark [12]. Its baseline is "a baseline that uses graph-based features only" (abstract), not the clustering detector. [KNOWN: TIFS full text, related-work §II-B and refs [4], [12], accessed 2026-11-15] It neither extends nor formally replaces the clustering method. It is a parallel line of work. [INFERRED from the method description and baseline choice]

## Inputs (what the paper states)

- **Signals.** A capture is translated into a set of N signal time series, S = {X1, ..., XN} (p.2 §III). §III-C says "The ROAD dataset provides translated CAN time series following a similar schema used by Hanselmann et al." (p.3). Separately, the introduction says the work leverages ORNL's CAN-D signal reverse-engineering capability (p.1 §I), and §V assumes a high-fidelity translation "such as CAN-D" is available (p.7). The paper does not say whether it used ROAD's released translation as shipped. [KNOWN statements; source of the translation actually used UNKNOWN; corrected by referee 2026-11-15] The paper says the masquerade files hold "time series from hundreds of IDs that have a few to dozens of signals each" (p.3 §III-C). It does **not** list which signals or IDs it kept, or how many there were (N). [KNOWN statement; N UNKNOWN]
- **Alignment.** "We modified the time series to have the same frequency by linearly interpolating them in common timestamps. We chose a baseline frequency of 10 Hz because it is the lowest frequency in the IDs in this dataset" (p.4 §III-D1). [KNOWN]
- **Filtering and scaling.** "we also discarded any constant time series and normalized each remaining series to the unit norm" (p.4 §III-D1). [KNOWN] Unit-norm scaling cannot change a Pearson correlation, so it has no effect on the method as described. [INFERRED: Pearson is scale-invariant]
- **Window length and stride.** **None.** There is one dendrogram per whole file: "For each file, a hierarchical clustering dendrogram is produced" (p.5 Fig. 3 caption), and "Once each dendrogram has been computed for each file" (p.4 §III-D4). The forensic unit is the capture. [KNOWN] The "by window" part of the round question is therefore an extension beyond the paper. The 2024 public code (below) is the only ORNL-published reference for a windowed version.
- **Attack content inside the file.** The masquerade files contain benign driving before and after the injection interval (e.g. `max_engine_coolant_temp_attack_masquerade`: interval 19.98 to 24.17 s of a 25.88 s capture). The whole file, benign stretches included, is clustered. [KNOWN: `signal_extractions/attacks/metadata.json`; paper p.4 §III-D4 builds per-file dendrograms]

## The clustering

- **Input matrix.** "These pairwise correlations populate a correlation matrix, which is used as the input for AHC" (p.4 §III-D3). [KNOWN] How a correlation matrix becomes a dissimilarity for AHC (1−r, 1−|r|, √(2(1−r)), or rows as feature vectors with Euclidean distance) is **not stated**. [UNKNOWN]
- **Linkages studied.** Single, complete, average and Ward (p.3 §III-A; p.4 §III-D3). Ward is the best and is used for the detection evaluation (p.6 §IV-F). [KNOWN]
- **Dendrogram cut.** **None.** The full dendrogram is compared; it is not cut at a level. CluSim's hierarchical mode weights every level, and r sets how much each level counts (p.3 §III-B; p.8 App. B). [KNOWN]
- **File-level meta-clustering (Fig. 3 only).** The file-by-file similarity heatmap is itself clustered: "We used Euclidean distance on these similarities with Ward linkage" (p.5 Fig. 3 caption). This treats rows of a similarity matrix as feature vectors. [KNOWN]

## The CluSim similarity

- **Measure.** CluSim's element-centric similarity, as described in App. B (p.8). Clusterings become a bipartite element-cluster graph, with edges weighted by hierarchy level. That graph is projected onto the elements. Each element gets a personalized PageRank with restart probability 1−α. Elements are compared with a corrected L1 between their stationary distributions, and the score is the mean over elements, in [0, 1] (p.3 §III-B; p.8 App. B). [KNOWN]
- **Parameters.** "We parametrized the clustering similarity method by letting r = −5.0 and α = 0.9" (p.3 §III-B). r = −5 was chosen "to capture differences at higher levels of the dendrograms", meaning coarse groups of correlated signals (p.5 §IV). App. B states that larger r gives more weight to lower levels (p.8). [KNOWN]
- **Inconsistency.** App. B says "We used r = 5.0 and α = 0.9 in Figure 2" (p.8). The main text uses −5.0 throughout. Fig. 2 is only a toy illustration (0.82 and 0.76), so this does not affect results. Whether it is a sign typo is [UNKNOWN].
- **Function names.** The paper names "the opensource CluSim method" and its parameters, **not** functions. [KNOWN] The clusim functions that implement the App. B description are `clusim.clustering.Clustering().from_scipy_linkage(Z, dist_rescaled=...)` and `clusim.sim.element_sim(c1, c2, alpha=0.9, r=1., r2=None, rescale_path_type='max', ppr_implementation='prpack')`. `element_sim` returns `np.mean(elementScores)` of `cL1` = 1 − (1/2α)·Σ\|x−y\|. [KNOWN: clusim `clusim/clusimelement.py` `element_sim`, `element_sim_elscore`, `cL1`; `clusim/clustering.py` `from_scipy_linkage`, GitHub master, accessed 2026-11-15] That ORNL's 2022 code called exactly these is [INFERRED]. The 2024 ORNL code calls exactly these, with `dist_rescaled=True`, `r=-5`, `alpha=0.9` (`code/helpers.py:L575-L580 @ 695a24e`). [KNOWN for 2024 code]
- **Element identity trap.** `from_scipy_linkage` labels elements by integer leaf index 0..N−1 (`elm2clu_dict = {v:[v] for v in range(linkage_matrix.shape[0] + 1)}`, clusim `clustering.py`). Two dendrograms are therefore comparable only if row i means the same signal in both. In clusim 0.4, mismatched element sets raise `ClusteringSimilarityError`. The `differing_elements` option was added later: the GitHub history for `clusimelement.py` shows commit `2736a23bcd` "nonidentical" dated 2025-01-14, after the 0.4 release of 2020-05-13. [KNOWN: GitHub commits API for that path, PyPI release metadata, accessed 2026-11-15] The paper does not say how it made signal sets identical across files after dropping constant series per file. [UNKNOWN]

## Baseline distributions, scoring and the decision

- **Benign distribution (Table II experiment).** All C(12,2) = 66 pairwise similarities among the 12 benign files (p.4 §III-D4). [KNOWN]
- **Attack distribution.** Similarities between each file of one attack category and each of the 12 benign files (p.4 §III-D4). That gives 36 values for a 3-file category and 12 for coolant. The count is [INFERRED arithmetic].
- **Test.** "We used the Mann-Whitney U test ... and set the significance level to 0.05 to test the null hypothesis that the distribution underlying benign conditions is the same as the distribution underlying attack conditions" (p.4 §III-D5). It is described as "a test of difference in location" (p.4). One-sided or two-sided is **not stated**. [UNKNOWN]
  - **Library default hazard.** In scipy up to 1.6, `mannwhitneyu(x, y)` with the default `alternative=None` "computes p-value half the size of the 'two-sided' p-value" (scipy 1.5.3 docs). [KNOWN: https://docs.scipy.org/doc/scipy-1.5.3/reference/generated/scipy.stats.mannwhitneyu.html, accessed 2026-11-15] The 2024 ORNL code calls `mannwhitneyu(a, b)[1]` with no `alternative` (`code/helpers.py:L234 @ 695a24e`) under pinned `scipy=1.5.3` (`environment.yaml:L130`). If the 2022 code did the same, Table II's p-values are half two-sided values. That is [INFERRED], and it has to be tested.
- **Threshold.** The decision threshold is p < 0.05, fixed in advance, not tuned (p.4 §III-D5; p.6 §IV-F). [KNOWN] The DOE CODE record's "probability score" is not defined in the paper. The 2024 code's distribution detector uses `1 - p` as its score (`code/helpers.py:L234`). Whether the closed code does likewise is [UNKNOWN].
- **Detection evaluation (§IV-F, p.6).** Of the 12 benign files, 3 are held out "for testing purposes (along with all attack files)", and the remaining 9 are used "for computing the similarity distribution from benign files". All C(12,9) = 220 splits are run. Settings: Ward, r = −5.0, α = 0.9, significance 0.05. Metrics are "micro-averaged". [KNOWN] **How one test unit is scored is not stated** (one file or a group of files, and which similarities form its sample). [UNKNOWN] The reported numbers pin it down (next section).

## Reported numbers for R0

### Table II, Mann-Whitney p-values (p.5), benign 66 pairs vs attack-vs-benign

| Attack | Single | Complete | Average | Ward |
|---|---|---|---|---|
| Correlated signal | 0.005 | 0.002 | 0.123 | 0.000 |
| Max speedometer | 0.003 | 0.017 | 0.007 | 0.000 |
| Max engine coolant | 0.251 | 0.065 | 0.006 | 0.008 |
| Reverse light on | 0.378 | 0.007 | 0.057 | 0.004 |
| Reverse light off | 0.039 | 0.004 | 0.004 | 0.000 |

Detected at 0.05: Ward 5 of 5, complete 4, single 3, average 3 (p.5 §IV). [KNOWN] The same p-values appear in the v1 figure insets (arXiv v1 Figs 3 to 7). [CORROBORATED: two versions of the same paper, which are not independent sources]

### Table III, classification with Ward (p.6), in percent

| Attack | Precision | Recall | F1 |
|---|---|---|---|
| Correlated | 88.00 | 100.00 | 93.62 |
| Max speedometer | 88.00 | 100.00 | 93.62 |
| Max engine coolant | 87.18 | 92.73 | 89.87 |
| Reverse light on | 87.23 | 93.18 | 90.11 |
| Reverse light off | 88.00 | 100.00 | 93.62 |

Overall FPR is 13.64%, independent of the attack scenario (p.6 §IV-F). Fig. 5 (p.6): every benign file's FPR is at or below 20%, except `Benign dyno drive benign anomaly` at 27%. `Benign dyno reverse` is at 20%. [KNOWN]

**Back-solved counts** [INFERRED arithmetic; it fits every row exactly]. Under the reading "one group-level test per fold", FP = 30 and TN = 190 out of 220 benign tests (30/220 = 13.64%). TP for correlated, max speedometer and reverse light off is 220/220, giving precision 220/250 = 88.00%. Coolant is TP 204, FN 16 (204/220 = 92.73%; 204/234 = 87.18%). Reverse light on is TP 205, FN 15 (205/220 = 93.18%; 205/235 = 87.23%).
- The other reading, "each of 3 held-out benign files tested alone" (FP 90 of 660), reproduces the FPR. But it predicts coolant precision 204/(204+90) = 69.4%, not 87.18%. That only works if a single benign file were tested for coolant.
- **Recommendation:** per fold, run one benign test with the 3 held-out files' similarities to the 9 training files (27 values) against the 36 training pairs. Run one attack test per category with its files' similarities to the 9 training files (27 values, or 9 for coolant) against the same 36. [INFERRED]
- Fig. 5's per-file rates fit 55 folds per file: 11/55 = 20%, and 15/55 = 27.3%. Averaging over files gives 3·30/(12·55) = 13.64%, consistent with the group reading. [INFERRED]

### Other checkable outputs

- Fig. 3 (p.5): Ward meta-clustering of the 25 files gives four main clusters. The first two hold 11 of 12 benign files (all but `dyno reverse`) and two attack files, `correlated masquerade 3` and `reverse light on 3`. The last two hold the other 11 attack files plus `dyno reverse`. [KNOWN]
- Fig. 4 (p.5), correlated attack: similarity axes span about 0.7 to 0.95. With Ward, benign and attack mass sits around 0.80 to 0.95. [KNOWN, read off the figure axes; only approximate]
- Table I (p.4): 10 dyno ambient files (108.2 min), 2 road ambient files (70.6 min), 13 masquerade files used. Durations are whole-capture lengths, and they match the metadata `elapsed_sec` sums: 6,493 s dyno, 4,234 s road, 78 s correlated. [KNOWN, with the arithmetic checked against `signal_extractions/*/metadata.json`]

## ROAD `signal_extractions/` layout vs what the paper needs

All facts in this section come from `unzip -l`, `unzip -v`, the readme, the metadata JSON and CSV header lines of `road.zip`, read 2026-11-15. [KNOWN]

- **Folders.** `road/signal_extractions/{ambient,attacks,DBC}/`. `DBC/anonymized.dbc` (30,785 B) has 105 `BO_` messages and 664 `SG_` signals, all named `Unknown_k`.
- **`attacks/` holds exactly 17 CSVs**: the **13 masquerades** the paper uses, plus 4 accelerator captures, which the paper does not use. There are **no fabrication-attack CSVs**. The masquerades are:
  - `correlated_signal_attack_{1,2,3}_masquerade` (target 0x6E0, `595945450000FFFF`)
  - `max_speedometer_attack_{1,2,3}_masquerade` (0xD0, byte 5 = FF)
  - `max_engine_coolant_temp_attack_masquerade` (0x4E7, byte 5 = FF)
  - `reverse_light_on_attack_{1,2,3}_masquerade` (0xD0, byte 2 = 0C)
  - `reverse_light_off_attack_{1,2,3}_masquerade` (0xD0, byte 2 = 04)
  - `attacks/metadata.json` gives `injection_id`, `injection_data_str` and `injection_interval` for each. The 4 accelerator files have null injection fields.
- **Trap: `ambient/` holds 29 CSVs, not 12.** Besides the 12 real ambient captures, it holds copies of all 17 attack CSVs. Their CRC32s are identical to the files in `attacks/`. `ambient/metadata.json` lists only the 12 ambient captures. **Select benign files by `ambient/metadata.json` keys, never by globbing `ambient/*.csv`.**
- **The 12 benign files** are the 10 `ambient_dyno_*` and 2 `ambient_highway_street_driving_*` captures (`_long` at 3,764 s and `_diagnostics` at 470 s). They match the paper's 10 + 2 (p.4 Table I).
- **CSV schema.** All 46 CSVs have the same 25-column header: `Label,Time,ID,Signal_1_of_ID,...,Signal_22_of_ID`. The column order is Label, Time, ID, whereas the readme says `Label ID Time`.
  - Each row is one frame. `ID` is the decimal arbitration ID. Signal columns hold that ID's decoded values, with NaN beyond its signal count.
  - A signal's identity is therefore the pair (ID, k). The readme says "a single `ID` can contain dozens of signals"; the header caps it at 22.
  - Whether `Signal_k` maps to the k-th `SG_` of that `BO_` in the DBC is [INFERRED]. For example, 0x6E0 has four 14-bit signals `Unknown_0..3`, consistent with the four wheel speeds the paper names. The experimenter should check the non-NaN count per ID against the DBC.
- **Labels.** `Label` is per frame. The paper does not use it, because it labels whole files. Accelerator files are all `Label = 0` (readme).
- **File sizes.** The largest benign CSV is `ambient_highway_street_driving_long.csv` at 556 MB, and the 12 benign CSVs total about 1.52 GB uncompressed. The 13 masquerade CSVs total about 98 MB. [KNOWN from the listing; totals are arithmetic]

## Build spec for an independent rebuild (all [INFERRED] unless marked)

This spec reconstructs the *published method*. It is not ORNL's implementation.

1. **File sets.** Benign: the 12 keys of `signal_extractions/ambient/metadata.json`. Attack: the 13 `*_masquerade.csv` in `signal_extractions/attacks/`. Exclude accelerator. [KNOWN selection, p.4 Table I and §III-C]
2. **Parse.** Stream with `usecols`, and give `Label` and `ID` integer dtypes. For each ID, keep the `Signal_k` columns that are not all-NaN. Signal key = `f"{ID}_{k}"`, the same naming pattern as `code/helpers.py:L63 @ 695a24e`.
3. **Resample.** For each signal, take its (Time, value) pairs from rows of its ID and linearly interpolate (`np.interp`) onto a 10 Hz grid, as the paper states (p.4 §III-D1). Grid span: `[max first-timestamp, min last-timestamp]` over the retained signals of that file (my choice; the span is UNKNOWN). Record how many seconds this trims.
   - Measure each ID's median rate first. The paper says 10 Hz "is the lowest frequency in the IDs in this dataset". If slower IDs exist, keep them (still interpolated) in the primary run. As a sensitivity run, drop IDs below 9.5 Hz.
4. **Filter.** Drop signals that are constant on the grid. Scale to unit L2 norm (stated, but it does not affect Pearson).
5. **Common element set.** Use the **global intersection** of non-constant signals across all 25 files, in a fixed sorted order. The paper builds one dendrogram per file and then compares pairs (p.4 §III-D4), which needs one fixed element set across files. clusim 0.4 needs identical element indices.
   - Sensitivity run: per-pair intersection, as the 2024 code does (`code/helpers.py:L617-L619 @ 695a24e`).
   - **Report which signals of IDs 0xD0, 0x6E0 and 0x4E7 survive.** A reverse-light bit that is constant in any ambient file would be dropped globally, and the reverse-light attacks could then only be detected through side effects.
6. **Correlation.** Pearson correlation N×N (`DataFrame.corr()`).
7. **AHC.** Primary: `scipy.cluster.hierarchy.linkage(C, method=m)` on the N×N correlation matrix C, with its rows treated as observation vectors (Euclidean). This is what scipy does with a 2-D array: "a collection of m observation vectors in n dimensions may be passed as an m by n array", and for `ward(X)` the metric is Euclidean (scipy 1.5.3 docs, accessed 2026-11-15).
   - It is also exactly what the 2024 ORNL code does, `ward(corr_matrix)` on a square DataFrame (`code/helpers.py:L539-L556`), and it mirrors the paper's Fig. 3 "Euclidean distance on these similarities".
   - Alternative: condensed `pdist`-style distance d = 2(1−r), which the 2024 DBSCAN path uses (`code/helpers.py:L384-L386`), or √(2(1−r)).
   - Run m ∈ {single, complete, average, ward}.
8. **CluSim.** Pin `clusim==0.4` (it needs `python-igraph`, and the 2024 env pins `python-igraph==0.9.9`, `environment.yaml`). Build with `Clustering().from_scipy_linkage(Z, dist_rescaled=True)`, then `clusim.sim.element_sim(c1, c2, alpha=0.9, r=-5.0)`, leaving the `rescale_path_type='max'` default. `dist_rescaled=True` matches the 2024 code; the paper is silent. Similarity is the raw `element_sim` output, in [0, 1]. Do **not** take 1 − sim; that is the 2024 code's anomaly score.
9. **Table II run.** Benign sample: the 66 benign pairs. Attack sample: each category file × the 12 benign files. Mann-Whitney U at 0.05. Report three p-values for every cell: two-sided, one-sided `alternative='greater'` (benign more similar than attack), and the legacy "None" value (half the two-sided p). Then say which matches Table II.
10. **Table III run.** Ward only. 220 combinations of 9 training benign files.
    - Training sample: the 36 pairs among the 9.
    - Benign test: the 27 similarities of the 3 held-out files to the 9 training files. It counts as FP if p < 0.05.
    - Attack test per category: the n_files × 9 similarities to the training files. It counts as TP if p < 0.05.
    - Expected: FP 30, TN 190; TP 220/220/204/205/220.
    - Also compute the per-file reading (each held-out file alone, 9 similarities) and report both.
11. **Per-file FPR (Fig. 5).** For each benign file, compute the share of its 55 held-out folds that test positive.
12. **Logging.** Record N per file and the global N; the dropped signals; the grid span trimmed; wall time and peak RSS; `pip freeze`; and the md5 of `road.zip`.

**Cost estimate** [INFERRED]: parsing the 1.6 GB of benign CSVs dominates, and streaming one file at a time keeps peak memory in the low GB. The 3,764 s file at 10 Hz is about 37.6k × N floats. Pearson and linkage on N in the hundreds take seconds. `element_sim` on a few hundred elements is sub-second per pair. Table II is about 66 + 156 pairs per linkage, so 4 × 222 pairs in all. Table III reuses one 12×12 similarity matrix plus the 13×12 attack matrix. **All 220 folds need no new CluSim calls**, only resampling of a 25×25 (strictly 12×12 plus 13×12) precomputed similarity matrix.

## The later windowed variant (public; reference only, not the 2022 detector)

These facts are [KNOWN] at `695a24e` unless marked.

- **Entry point.** `code/streaming-detector-AHC-ROAD.py:L9-L92`. It trains on **one** ambient capture, `training_captures[-1]` from an `os.listdir` order (`:L31`; `helpers.py:L22-L30`), at `freq=100`. It tests every non-accelerator attack capture in parallel processes (`:L79-L92`).
- **Preprocessing is not in the repo.** `helpers.py:L19-L20` inserts an absolute path into `sys.path` and imports `signal_based_preprocess_functions`, which the repo does not contain. The function is called with `min_hz_msgs=freq` and a heuristic-labeled DBC path that is also not shipped (`:L44-L56`).
  - It reads raw captures through its own DBC, not ROAD's `signal_extractions/` CSVs. [KNOWN: paths at `:L24`, `:L47`]
  - That `min_hz_msgs` drops IDs below `freq` Hz is [INFERRED] from the parameter name.
- **Per window.** Drop constant columns, apply **min-max** normalization (not unit norm), partition by `window` samples with stride `offset` (`:L59-L89`), compute Pearson (`:L92-L105`), intersect signal names with training (`:L617`), run Ward on each correlation matrix (`:L619`, `:L539-L556`), and score `1 - element_sim(..., r=-5)` (`:L621`, `:L575-L580`).
- **Window labels.** A window is positive if it overlaps the injection interval (`:L624-L631`). An empty correlation matrix scores 0 (`:L634-L642`).
- **Sweep.** `window ∈ {50, 100, ..., 400}` samples, which is 0.5 to 4 s at 100 Hz, and `offset ∈ {10, 20, ..., window}` (`:L663-L664`). Results are written as JSON to an absolute path (`:L674`).
- **Environment.** `environment.yaml` pins Python 3.8.12, scipy 1.5.3, numpy 1.20.3, pandas 1.4.1, scikit-learn 0.23.2 and `clusim==0.4`.
- **History.** 24 commits from 2023-08-08 to 2024-08-23, two authors. Merge messages name an ORNL-hosted remote (`bf3e3db`, `b8c8096`). [KNOWN: `git log`] No tests or CI. [KNOWN: tree listing]
- **Use for this round.** The windowed variant gives an ORNL-published parameter range for a "by window" extension (0.5 to 4 s windows), plus the `1 - sim` score convention. Its results are in arXiv:2406.13778, which this pass did not read. [UNKNOWN numbers]

## Ambiguities and recommended choices

| # | Ambiguity | Paper evidence | Recommendation [INFERRED] | Why |
|---|---|---|---|---|
| A1 | Resampling grid span | "linearly interpolating them in common timestamps" (p.4 §III-D1) | `[max first, min last]` per file, at 10 Hz | No extrapolation; the trim is usually under 1 s for IDs at 10 Hz or faster |
| A2 | IDs slower than 10 Hz | "10 Hz ... lowest frequency in the IDs" (p.4) | Measure the rates; keep all IDs in the primary run, drop those below 9.5 Hz in a sensitivity run | The paper's premise may not hold for every ROAD ID |
| A3 | Element set across files | Per-file dendrograms (p.4 §III-D4); constants dropped per file | Global intersection, sorted; per-pair intersection as sensitivity | clusim 0.4 needs identical elements, and one dendrogram per file implies a fixed set |
| A4 | Correlation → AHC input | "correlation matrix ... used as the input for AHC" (p.4 §III-D3) | Rows of C as vectors with Euclidean distance (scipy default for a 2-D array); 2(1−r) as alternative | Matches ORNL's 2024 code and the Fig. 3 convention |
| A5 | `dist_rescaled`, `rescale_path_type` | Not mentioned | `True`, `'max'` | 2024 code; clusim default |
| A6 | r sign | −5.0 in text, 5.0 in App. B for Fig. 2 | −5.0 | Used for all results; the rationale (coarse levels) is stated on p.5 |
| A7 | MWU sidedness | "difference in location" (p.4) | Report two-sided, one-sided and legacy half; keep whichever reproduces Table II | The scipy ≤1.6 default halves p, and the 2024 code relies on that default |
| A8 | Test unit in §IV-F | Not stated | Group test per fold (27 vs 36; 9 for coolant) | The only reading that reproduces all 5 rows of Table III with one FP count |
| A9 | NaN correlations | Not mentioned | Cannot arise after constants are dropped; assert it | Defensive |
| A10 | Whole file vs injection interval | Whole file (Fig. 3 caption) | Whole file for R0; interval-only and pre-injection-only as extensions | Separates attack signal from capture-context effects |

## What stands out (interpretation, kept apart from the facts)

1. **Capture length and driving context are confounded with attack status.**
   - The 13 attack files run 17 to 88 s. The benign files run 47 to 3,764 s, two of them under 52 s.
   - Correlation matrices from short captures are noisier and narrower in driving regime. On that basis alone they should look *less similar* to long benign captures.
   - The one benign file that clusters with the attacks in Fig. 3 is `dyno reverse`, at 51 s and in reverse only. The highest-FPR benign file is `benign anomaly`.
   - This pattern is what a length or regime confound would predict. It does not prove one. [INFERRED]
2. **The 13.64% FPR is large for a forensic tool.** It means about 1 in 7 groups of three clean captures is flagged. The paper reports it plainly and does not compare against a baseline (p.7 §V). [KNOWN numbers; the framing is mine]
3. **The coolant masquerade lasts 4.2 s of a 25.9 s file.** At a 10 Hz whole-file correlation, about 84% of its samples are benign driving. That still gives Ward p = 0.008, which fits point 1: much of what separates it may be context rather than the injection. [INFERRED]

## Experiment questions this artifact study sets up

- **R0.** Do Table II's Ward column and Table III's counts (FP 30 of 220; TP 220/220/204/205/220) reproduce under the spec? Which MWU sidedness matches?
- **Q-confound (most informative).** Re-run the Table II Ward test with the attack files replaced by (a) only their pre-injection segment and (b) random benign crops matched in length to the attack files (17 to 88 s), taken from the long ambient captures.
  - *Falsifiable expectation:* if (a) or (b) is also significant at 0.05 with p values comparable to Table II, the method detects short or out-of-regime captures, not masquerades.
  - If both are non-significant while the full files are significant, the attack signal is real.
- **Q-window.** Using the 2024 parameter range (0.5 to 4 s windows), where does a windowed version of this spec separate injection-interval windows from pre-injection windows, by attack? This is the round's "by window" question. It is an extension, not a reproduction.
- **Q-signal.** After the global intersection, do the targeted signals (0x6E0 `Unknown_0..3`; the 0xD0 byte-5 and byte-2 fields; the 0x4E7 byte-5 field) survive? If a target signal is dropped, does detection still occur?

## Known / Inferred / Unknown summary

- **KNOWN**:
  - The pipeline steps: 10 Hz linear interpolation, constant-drop, unit norm, Pearson, AHC with four linkages, CluSim r = −5 and α = 0.9, MWU at 0.05.
  - The file sets: 12 benign, 13 masquerade.
  - All Table II and III numbers and the 13.64% FPR.
  - Code closed (DOE CODE CS, no repo).
  - ROAD signal layout, including the duplicated attack CSVs in `ambient/`.
  - The 2024 public windowed variant's exact calls.
  - The TIFS paper is a different method that cites this one.
- **INFERRED**:
  - The clusim function names used in 2022.
  - The correlation-to-distance choice.
  - The group-level test unit, from back-solving Table III.
  - That MWU p-values may be one-sided halves.
  - The global element set.
  - The length/regime confound.
- **UNKNOWN**:
  - N and which signals were kept.
  - Grid span and the handling of IDs below 10 Hz.
  - How element sets were matched across files.
  - The distance definition, `dist_rescaled` and MWU sidedness.
  - The meaning of the DOE CODE "probability score".
  - Whether the closed 2024-registered code differs from the 2022 paper's pipeline.
  - The windowed variant's numbers (arXiv:2406.13778, not read).
  - Runtime of the original.

## Sources (all accessed 2026-11-15)

- DOE CODE 134139 API record: https://www.osti.gov/doecodeapi/services/search/134139. Supports closed source, ORNL site and research org, release date, description.
- OSTI 1866690 record https://www.osti.gov/api/v1/records/1866690 and full text https://www.osti.gov/servlets/purl/1866690. Supports all method and result claims cited by page.
- arXiv:2201.02665 v1 and v2 PDFs, https://arxiv.org/abs/2201.02665. Supports the version comparison.
- OSTI 3009491 record https://www.osti.gov/api/v1/records/3009491 and full text https://www.osti.gov/servlets/purl/3009491. Supports the lineage section.
- `pmoriano/benchmarking-unsupervised-online-IDS-masquerade-attacks` @ `695a24e89dcbeee4b3eb9ef34484e4c731e4bb59`, https://github.com/pmoriano/benchmarking-unsupervised-online-IDS-masquerade-attacks, cloned read-only. DOE CODE 141444 per `discovery/snapshots/doecode-2026-11-11.json`. Supports the windowed-variant section and the code-convention inferences.
- clusim: https://pypi.org/pypi/clusim/json; `clusim/clusimelement.py` and `clusim/clustering.py` at GitHub master; GitHub commits API for `clusim/clusimelement.py`. Supports function signatures, the element-identity requirement, and the `differing_elements` date.
- scipy 1.5.3 docs for `mannwhitneyu` and `cluster.hierarchy.ward`. Supports the legacy p-value halving and the observation-vector semantics.
- `.cache/data/road/road.zip`: `unzip -l`, `unzip -v` (CRC32), `road/readme.md`, `road/signal_extractions/{ambient,attacks}/metadata.json`, `road/signal_extractions/DBC/anonymized.dbc`, and the header line of each of the 46 signal CSVs. Supports the layout section. ROAD is CC BY 4.0 (Zenodo 10462796); attribute it in any write-up.
