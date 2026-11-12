# Independent referee: materials and biology packet

Review date: **2026-11-10**. Reviewed the full `materials-biology.md`, its fourteen-entry source ledger and companion `materials-biology.json`. This is an independent source spot-check and claim-boundary review, not a scientific replication or a second execution of every original search. No shared files were edited.

## Judgment

**No blocking factual error found in the checked core claims.** The packet preserves the important negative result in the nylon work, supports AtomAI's ORNL attribution with explicit text rather than an organization-name inference, and correctly describes the HydraGNN energy-reference transformation. All four local opportunities are explicitly proposals. The packet does not claim an installation, downloaded weights, enzyme replication or executed synthetic benchmark.

## Primary-source checks

All sources below accessed 2026-11-10. Sources were fetched directly through public extraction; raw pinned license files were also retrieved independently. Excerpts are short locators.

| Checked claim | Source / locator | Verdict and limitation |
|---|---|---|
| Nylon candidate count, activity fraction, specificity and yield | [Final ORNL journal record](https://impact.ornl.gov/en/publications/identification-and-characterization-of-substrate-and-product-sele/), Chem Catalysis 5(8), article 101418, published 2025-08-21, Abstract; excerpt: “yield was still less than 1%” | **Verified.** Abstract states 95 enzymes, nearly 40% active, up to twentyfold higher product titers for nylon-6,6 versus nylon-6, and below-1% yield. The packet appropriately avoids industrial-throughput claims. No final supplementary table independently inspected in this referee pass. |
| AtomAI ORNL connection | [Public README](https://github.com/pycroscopy/atomai), What is AtomAI; excerpt: “at Oak Ridge National Lab” | **Verified.** Explicit development attribution exists. No inference from the pycroscopy organization name is needed. Historical development attribution does not establish present ownership of every application. |
| AtomAI segmentation input/output contract | [Model API](https://atomai.readthedocs.io/en/latest/atomai_models.html), Segmentor example and `fit` parameters; excerpt: “nn_output, coordinates” | **Verified.** Documentation distinguishes image tensors and mask targets, with binary/multiclass differences; prediction exposes network output and coordinates. README also documents ImSpec image/spectrum dimensions and ensembles. This verifies the documented interface, not empirical accuracy or compatibility on this workstation. |
| HydraGNN reference alignment | [OSTI dataset 2562660](https://www.osti.gov/biblio/2562660), release 2026-05-06, description of `datasets_ADIOS2_format`; excerpt: “subtract such prediction from the original value” | **Verified.** Dataset v1 preserves original energies; v2 subtracts a linear-regression prediction based on chemical composition. This is stronger than a generic normalization statement. No energy files were fetched or transformed locally. |
| 2025 HydraGNN multi-task scale | [arXiv 2506.21788](https://arxiv.org/abs/2506.21788), submitted 2025-06-26, Abstract; excerpt: “over 24 million structures from five datasets” | **Verified as reported.** Shared message-passing and dataset-specific heads, plus Perlmutter/Aurora/Frontier tests, are explicitly described. Independent scaling validation remains outside this review. |
| Fine-tuning reuse and prerequisite | [Fine-tuning README](https://github.com/ORNL/HydraGNN_GFM_FineTuning4Materials), Overview and Installation; excerpt: “HydraGNN v5.0” | **Verified with clarification below.** Repository names preprocessing, output-head adaptation, ensemble fine-tuning, evaluation and the GFM 2026 artifact. Required version is stated, although tested compatibility of arbitrary inspected heads remains unknown. |
| AtomAI license | [Pinned MIT license](https://github.com/pycroscopy/atomai/blob/93c88817a577686d6b8a84ab954872ca5cab7fcc/LICENSE), first line; excerpt: “MIT License” | **Verified by raw file fetch.** Does not license independently obtained microscope data or automatically establish every pretrained artifact's terms. |
| HydraGNN core license | [Pinned core license](https://github.com/ORNL/HydraGNN/blob/d49d934403f0cc3276750004c8dfbf3a502a10f1/LICENSE), first line; excerpt: “BSD 3-Clause License” | **Verified by raw file fetch.** Packet correctly refrains from automatically assigning this to all companion datasets, weights and repositories. |

## Nonblocking clarification for the editor

[KNOWN] The fine-tuning README explicitly asks for HydraGNN **v5.0**, and the 2026 dataset record likewise names v5.0 as its producing code. The packet's unknown about compatibility of the inspected core head and fine-tuning head is defensible because neither was run, but can be made more precise: the stated prerequisite is known; actual installation/runtime compatibility remains untested.

[KNOWN] The 2025 paper and the 2026 release are different stages. The first reports over 24 million structures from five datasets; the latter describes 544+ million structures from sixteen datasets and a subsequent ensemble/hyperparameter-search release [the two primary sources above]. The packet already dates them separately. [EDITORIAL] An explicit sentence separating stages would help prevent later retrieval from merging their scale claims or assuming the same checkpoint population. No claim that the packet's existing numbers are wrong is made.

## Scope and checks not repeated

The MIJAMP section, preprint/final separation, inference-labeled connection table, and JSON entries were read for internal consistency. The JSON marks local opportunities as proposals and does not add catalog entries. MIJAMP's paper/repository mechanics, the nylon preprint's structural IDs, AtomAI's 2022 paper date, and every original retrieval failure were **not independently re-fetched** here. They remain covered by the packet author's stated sweep, not newly certified by this referee report.

A direct Python retrieval of the AtomAI hosted API returned **HTTP 403** during this pass; the public extraction tool successfully returned its model documentation. Both pinned raw GitHub license fetches succeeded. No login, restricted source, artifact installation, data download, outside-repository change or experiment was performed.

## Proposed versus executed boundary

[KNOWN, packet inspection] The enzyme assay-table exercise, invented-pattern exercise, synthetic lattice-coordinate benchmark and source-label alignment test are all labeled local proposals. Statements of published experimental results are attributed to their source, and the packet explicitly says no upstream software was run. [INFERRED] The most useful next small execution remains a known-ground-truth synthetic coordinate benchmark or label-alignment test, but this review supplies no benchmark result and does not endorse fabricated data as evidence of real enzyme, microscope or foundation-model performance.

**Review result:** checked claims verified within the stated source sample, two nonblocking clarity improvements identified, no mandatory factual repair found.
