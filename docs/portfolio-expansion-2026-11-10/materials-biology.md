# Materials, chemistry, and biology: four systems worth understanding

Independent public-source research, accessed 2026-11-10. This extends the [existing guide](../public-research-guide.md), [autonomous-science account](../autonomous-science.md), and [coverage matrix](../coverage-matrix.md). It neither adds catalog entries nor claims a complete directorate survey. [KNOWN] means the cited primary source states it; [INFERRED] marks our interpretation; [UNKNOWN] preserves a missing answer. The companion [JSON index](materials-biology.json) is a retrieval aid, not a replacement for the source ledger below.

## Sweep 1: discoveries and mechanisms

### MB1. Nylon-selective enzymes: specificity is not industrial throughput

**What it does.** [KNOWN: M01] ORNL-associated research characterized enzymes that distinguish nylon-6,6 from nylon-6. The 2025 paper reports nearly 40% activity among 95 candidates and up to twentyfold higher product titers for one nylon type versus the other, but yield remained below 1%. These are experimental enzyme findings, not an operating recycling plant.

**Inputs -> method -> outputs.** [KNOWN: M02] The public 2024 preprint describes a sequence-diversity panel, protein structure predictions, measured reaction products, and follow-up structural analysis. Mass spectrometry distinguishes products rather than merely reporting disappearing substrate. Its analysis warns that residual small cyclic compounds can make apparent bulk-polymer conversion look better than it is. This preprint is explicitly not the final peer-reviewed version.

**Why the connection matters.** [KNOWN: M03] ORNL's account connects synthetic biology, computational modeling, chemical analysis, and structural characterization. [INFERRED: M01–M03] The interesting engineering boundary is a chain of measurements: a model proposes a candidate, a physical assay establishes activity, product identity establishes selectivity, and overall yield determines whether the result is useful. A good prediction at one boundary cannot substitute for the next.

**Local opportunity.** [LOCAL proposal] Build a product-analysis notebook using published or synthetic assay tables. Keep selectivity ratios, total conversion, replicates, and detection thresholds separate. Test a counterexample where a highly selective candidate still has negligible conversion. This reproduces an analysis principle, not enzyme function or a wet-lab result. [KNOWN: M02] The preprint names public structures 9CXR and 9DYS; their underlying files and reuse conditions were not retrieved here. [UNKNOWN] Final-paper supplemental data completeness, assay-analysis code, independent scale-up economics, and real mixed-waste performance.

### MB2. MIJAMP: human-auditable biological pattern discovery

**What it does.** [KNOWN: M04, M05] MIJAMP turns sequencing-derived methylation information into candidate bacterial DNA patterns. Its distinguishing design is interactive refinement: a scientist can question a discovered pattern against the whole dataset instead of accepting a black-box output.

**Inputs -> method -> outputs.** [KNOWN: M04] The published workflow accepts modification calls and a reference genome, preprocesses aligned data, discovers candidate patterns, then lets a human refine or reject them against genome-wide evidence. Accepted patterns are removed from the unexplained pool before the next search, and final patterns are saved in a table. Separate query and diagnostic tools assess specific patterns and how much of the data the inferred pattern set explains. The paper compares two bacterial datasets with another tool; agreement on a control does not establish general accuracy on all organisms. It explicitly excludes non-motif-based methylation such as eukaryotic CpG islands.

**Public artifacts and limits.** [KNOWN: M04, M06] The paper links a public GitLab repository and its `testData` directory; the public landing page describes Python scripts. No repository contents or test data were downloaded. [UNKNOWN] Code license, pinned revision, dependency compatibility, and reproducible runtime on this workstation. [INFERRED: M04] This is an example of scientific review embedded inside computation, complementing the Atlas's autonomous-science story without establishing shared software.

**Local opportunity.** [LOCAL proposal] Use invented strings and marked positions to build an explainability exercise: display candidate-pattern coverage, unexplained observations, and a record of human accept/reject decisions. Compare an overbroad pattern with a narrower one. This is a toy data-analysis exercise, not a guide to modifying organisms or a replication of MIJAMP's biological conclusions.

### MB3. AtomAI: microscopy pixels become structures that models can use

**What it does.** [KNOWN: M07] AtomAI's 2022 publication describes a bridge from microscopy images and spectra to descriptors, atomic species/positions, and first-principles modeling. [KNOWN: M08] The repository explicitly credits development at ORNL; a side-organization name alone is not our evidence of that connection.

**Inputs -> method -> outputs.** [KNOWN: M08, M09] A segmentation model takes images and labeled masks during training, and predicts neural-network output plus detected coordinates for new images. Image/spectrum models learn a correspondence between local image patches and spectra through a reduced representation. Ensembles offer multiple predictions; disagreement can be inspected rather than hidden in one result. The public API distinguishes image tensors from mask tensors and makes image-to-spectrum dimensions explicit. These are software interfaces, not proof of accurate results for an arbitrary new microscope.

**What is technically useful.** [INFERRED: M07–M09] Converting pixels into atom/defect coordinates creates an intermediate artifact that can be checked before downstream simulation. A plausible image segmentation can still misplace atoms, so downstream physical predictions need their own checks. This provides a concrete way to deepen the existing microscope-autonomy chapter without claiming AtomAI powers a particular INTERSECT deployment.

**Public artifacts.** [KNOWN: M08, M10] Public examples, tests, pretrained-model directory, and MIT license are visible. Inspected revision: `93c88817a577686d6b8a84ab954872ca5cab7fcc`. No upstream model was installed or executed. [LOCAL proposal] Make synthetic lattice images with known missing sites, add noise, and measure coordinate error and missed/false detections. Treat a classical detector as a baseline before any neural model. [UNKNOWN] Which trained weights match a given experimental modality, calibration of uncertainty, and transfer accuracy under instrument drift.

### MB4. HydraGNN: shared structural learning without pretending all labels agree

**What it does.** [KNOWN: M11] A 2025 preprint describes shared graph-message-passing layers with distinct prediction heads for dataset-specific outputs. Rather than forcing incompatible scientific labels into one output definition, it keeps a shared representation and separates their targets. It reports training on over 24 million structures from five datasets and tests on Perlmutter, Aurora, and Frontier. This is a reported pretraining/scaling study, not evidence that a local model will reproduce its scientific accuracy.

**Inputs -> method -> outputs.** [KNOWN: M12] The HydraGNN Predictive GFM 2026 data record describes preprocessed atomistic datasets, model parameters, and hyperparameter-search outputs. It explicitly distinguishes original total energies from energies realigned by subtracting a composition-based linear prediction. [INFERRED: M11, M12] Units, energy references, and source identity are part of the learning problem, not clerical metadata: merging them incorrectly can make apparent training improvement scientifically meaningless.

**A newly concrete reuse path.** [KNOWN: M13] ORNL's separate fine-tuning repository provides preprocessing, adaptation of output heads, ensemble fine-tuning, and benchmark/evaluation scripts. Its README points to the GFM release through OLCF Data Constellation/Globus. Its README states HydraGNN v5.0 as a prerequisite; actual installation compatibility remains untested. Public metadata was read; files or weights were not downloaded, and no login was attempted. [KNOWN: M14] HydraGNN core has BSD-3-Clause licensing. [UNKNOWN] A separate license was not established for the fine-tuning repository or every dataset/weight; do not assume the core license automatically covers them.

[KNOWN: M11–M13] The 2025 paper and 2026 released artifacts are different stages; their dataset populations and model checkpoints must not be treated as identical.

**Local opportunity.** [LOCAL proposal] Construct two synthetic structure-label datasets with a known reference offset. Compare a pooled regressor, source-specific heads, and explicit reference alignment on a held-out structure split. This tests a design question before considering pretrained models or HPC. [UNKNOWN] Workstation memory needs, independently reproduced transfer benchmarks, and precise compatibility between the inspected core head and fine-tuning repository. Existing catalog connection: [HydraGNN brief](../../projects/hydragnn.md).

## Connections and priorities

| Connection | Evidence boundary | Useful next investigation |
|---|---|---|
| Enzyme selectivity and materials modeling both depend on what was actually measured | [INFERRED: M01, M12] comparison of label/assay definitions, not shared implementation | Preserve product identity and energy-reference conventions as first-class metadata |
| MIJAMP interactive refinement and AtomAI intermediate coordinates make errors inspectable | [INFERRED: M04, M09] common design principle, not a software dependency | Evaluate failure cases and retain rejected candidates/intermediates |
| AtomAI structural descriptors and HydraGNN atomistic graphs are potentially complementary | [INFERRED: M07, M11] plausible data boundary only; no reviewed source establishes an adapter | Inspect coordinate/species/cell/unit requirements before connecting them |
| Nylon biology and polymer/materials science are directly connected within one publication | [KNOWN: M01–M03] measured chemistry and structure evidence, not a general integrated ORNL platform | Read final supplementary assay tables and compare them with the preprint |

[EDITORIAL] First follow-up priority is the small AtomAI-style synthetic-coordinate benchmark, because it offers known ground truth without facility access or external datasets. Second is a multi-source label-alignment experiment inspired by HydraGNN. Nylon work is a strong scientific deep-dive target; its low-yield limitation should remain prominent. MIJAMP adds biosciences coverage through an auditable analytic workflow, without turning Atlas into a laboratory engineering manual.

## Source ledger

All accessed 2026-11-10. Quotes are brief verification locators, not copied explanatory text. Dates are source publication dates unless marked unknown. Dynamic repository heads are observations on access date, not release guarantees.

| ID | Primary source and date | Short excerpt and locator | Supports / limits |
|---|---|---|---|
| M01 | [ORNL record: Identification and characterization of substrate- and product-selective nylon hydrolases](https://impact.ornl.gov/en/publications/identification-and-characterization-of-substrate-and-product-sele/), 2025-08-21 | “yield was still less than 1%”, Abstract | Final journal abstract, candidate count/selectivity/low yield; no process economics |
| M02 | [Drufva et al. public preprint](https://pmc.ncbi.nlm.nih.gov/articles/PMC11601465/), 2024-11-14 | “This is a preprint”; “PDB ID: 9CXR”, heading and Structural analysis | Detailed methods/measurement caveats; not final peer-reviewed text |
| M03 | [ORNL enzyme account](https://www.ornl.gov/news/synthetic-biology-ai-driven-analysis-reveal-new-polymer-targeting-enzymes/), 2025-06-27 | “38 new enzymes”, Results and Impact | Cross-disciplinary workflow; institution's report, not independent replication |
| M04 | [Tidwell et al., Discovering methylated DNA motifs ... with MIJAMP](https://pmc.ncbi.nlm.nih.gov/articles/PMC12320774/), 2025-07-23 | “human-driven refinement strategy”, Abstract | Workflow, comparison and limits; one later web refetch hit browser check, public extraction succeeded |
| M05 | [ORNL MIJAMP software record](https://impact.ornl.gov/en/publications/mijamp/), Published 2024 | “user-defined motif”, Abstract | ORNL software/functional attribution; record date differs from 2025 paper |
| M06 | [Public MIJAMP repository landing page](https://code.ornl.gov/alexander-public/mijamp), created 2024-06-16 | “lightweight scripts written in Python 3”, Project information | Landing page only; no inferred code license or deployment |
| M07 | [ORNL AtomAI publication record](https://impact.ornl.gov/en/publications/atomai-framework-for-deep-learning-analysis-of-image-and-spectros/), Published December 2022 | “types and positions of atomic species”, Abstract | Published representation bridge and scientific scope |
| M08 | [AtomAI public repository](https://github.com/pycroscopy/atomai), date unknown | “It was developed by Maxim Ziatdinov at Oak Ridge National Lab.”, What is AtomAI | ORNL attribution, interfaces and public example/test surfaces |
| M09 | [AtomAI model API](https://atomai.readthedocs.io/en/latest/atomai_models.html), date unknown | “nn_output, coordinates”, Segmentor example | Precise input/output boundary; hosted docs can drift |
| M10 | [AtomAI pinned license](https://github.com/pycroscopy/atomai/blob/93c88817a577686d6b8a84ab954872ca5cab7fcc/LICENSE), date unknown | “MIT License”, first line | License only; no execution claim |
| M11 | [Multi-task parallelism ... atomistic modeling data](https://arxiv.org/abs/2506.21788), 2025-06-26 | “multiple decoding heads”, Abstract | Preprint mechanism and reported scale; not independent validation |
| M12 | [HydraGNN_Predictive_GFM_2026 dataset](https://www.osti.gov/biblio/2562660), 2026-05-06 | “values of the energy that have been realigned”, Description | Released artifact description and energy-reference distinction; no files fetched |
| M13 | [HydraGNN fine-tuning repository](https://github.com/ORNL/HydraGNN_GFM_FineTuning4Materials), date unknown | “task-specific output heads”, Overview | Reuse pipeline; separate license not established |
| M14 | [HydraGNN core pinned license](https://github.com/ORNL/HydraGNN/blob/d49d934403f0cc3276750004c8dfbf3a502a10f1/LICENSE), date unknown | “BSD 3-Clause License”, first line | Core license only; not inherited by all companion artifacts |

## Sweep 2: verification, corrections, and stopping boundary

[KNOWN: source checks] Re-read all four sections and connection rows against the fetched primary material. Reopened the ORNL final nylon abstract and retained the <1% qualification instead of repeating a success-story implication of near-term industrial recycling. Separated the 2024 preprint from the 2025 journal record. Reopened the MIJAMP software record and distinguished its 2024 date from the 2025 paper. Re-fetched pinned AtomAI and HydraGNN licenses; MIT and BSD-3-Clause were literally present. The GitHub public API reported AtomAI revision above and HydraGNN `d49d934403f0cc3276750004c8dfbf3a502a10f1`; fine-tuning repo head was `f3fe10ebdb2886d1199611d5644ec69e52bd78a2`. Repository ownership is not evidence of joint team structure or operational deployment.

[KNOWN: retrieval limits] ScienceDirect direct opening returned HTTP 403; its public extraction returned bibliographic material, so final quantitative claims use the directly fetched ORNL journal abstract instead. OSTI full manuscript `https://www.osti.gov/servlets/purl/3002770` returned HTTP 502 in this browser route. The OSTI GFM landing page timed out in browser retrieval; public text extraction succeeded. These are retrieval observations, not evidence that an artifact is absent. No restricted source, login, or endpoint discovery was used.

[UNKNOWN / bounded search] Queries on 2026-11-10 included `"MIJAMP" github ORNL methylated DNA motifs`, `"Identification and characterization of substrate- and product-selective nylon hydrolases" data`, and `"HydraGNN" materials multi fidelity 2025 ORNL paper`. No reviewed source established an AtomAI-to-HydraGNN adapter or a common production platform spanning all four systems. No final supplemental-data/code completeness judgment is made. Further broad searches will add examples; the highest-value next step is targeted artifact inspection and one small, explicitly local numerical test.

[STATUS] Research packet complete within this four-system boundary. No upstream software run, new catalog entry, completed scientific replication, or exhaustive biosciences/materials coverage is claimed.
