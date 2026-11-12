# MATEY

- Official page: none separate; the README is the documentation. [KNOWN: GitHub API `homepage` empty]
- Repo: https://github.com/ORNL/MATEY (default branch `main`, HEAD `631a4139295d4f51e573d474cff7d6586f3aa310`). GitHub description: "Scalable open-source codebase for developing spatiotemporal foundation models for multiscale multiphysics systems". [KNOWN: GitHub API, accessed 2026-11-11]
- Docs: README (install, Slurm launch, adding a dataset, publications); example YAML configs and Slurm scripts in `examples/`. [KNOWN: https://github.com/ORNL/MATEY/blob/631a4139295d4f51e573d474cff7d6586f3aa310/README.md]
- License: MIT, "Copyright (c) 2026, UT-Battelle, LLC"; source files carry `SPDX-License-Identifier: MIT` and `SPDX-FileCopyrightText: 2026 UT-Battelle, LLC`. [KNOWN: https://github.com/ORNL/MATEY/blob/631a4139295d4f51e573d474cff7d6586f3aa310/LICENSE#L1-L3; `matey/models/ringX_attn.py` L1-L3]
- Status: active (rule 14). Created on GitHub 2025-06-30; v1.0.0 tagged 2026-01-26; last push 2026-09-17; not archived. [KNOWN: GitHub API, git tags]
- ORNL relationship: CORROBORATED. Main github.com/ORNL org; UT-Battelle copyright; DOE CODE code-173753 "MATEY" (2026-01-26) lists research org "Oak Ridge National Laboratory (ORNL)", contract AC05-00OR22725, nine ORNL authors, and links the GitHub repo; the MATEY journal paper (OSTI 3365777) lists ORNL as research org. [KNOWN: https://www.osti.gov/doecode/biblio/173753; OSTI API code-173753 and 3365777]
- Origin: the README says the codebase "was originally seeded (Jan 2024) from" PolymathicAI's multiple_physics_pretraining (MPP) at commit 67ffa35 and "has since been substantially rewritten". The first git commit is that snapshot. MPP is MIT-licensed. [KNOWN: https://github.com/ORNL/MATEY/blob/631a4139295d4f51e573d474cff7d6586f3aa310/README.md#L79; git log 856c13f; GitHub API for PolymathicAI/multiple_physics_pretraining]
- Years visible in public sources: 2024 (seed and first ORNL work) to 2026
- Last checked: 2026-11-11

## Walkthrough (plain language)
- **What it is:** a PyTorch codebase for training transformer models that predict how a physical field (fluid flow, plasma edge, turbulence) evolves over time, meant to be pre-trained on many kinds of simulations and then fine-tuned. [KNOWN: README L3; OSTI 3365777 abstract]
- **The problem:** a vision transformer cuts a field into patches ("tokens"). Fine detail needs small patches, and small patches over a big 3D grid make sequences far too long to train. MATEY's answers are adaptive tokenization (refine only where the field is complex) and splitting long sequences across many GPUs. [KNOWN: OSTI 3365777 and 3367073 abstracts]
- **Key terms:**
  - *Foundation model*: one model pre-trained on broad data and then adapted to new tasks.
  - *Token / patch*: a small block of the grid turned into one vector the transformer reads.
  - *Spatiotemporal attention*: attention over both space and time; MATEY offers variants that mix them jointly or separately ("decoupled"). [KNOWN: OSTI 3365777]
  - *Sequence parallelism*: splitting one long token sequence across GPUs so each holds part of it. [INFERRED: definition]
- **What goes in:** simulation snapshots in HDF5, NetCDF, Zarr, Exodus, binary or graph form, read by a dataset class, plus a YAML config choosing model type, patch sizes, refinement, and parallel layout. [KNOWN: `matey/data_utils/*.py`; README L39-L59]
- **What happens:** the model reads a short history of states, normalizes each sample, patches it (optionally refining high-variance patches), runs space and time attention blocks, and decodes a predicted next state; training runs under PyTorch DDP or FSDP launched by Slurm. [KNOWN: `models/vit.py` L132-L162; `train.py` L197-L205]
- **What comes out:** trained checkpoints, loss logs, and predictions; `matey/postprocess/` and `matey/trustworthiness/` hold plotting and turbulence-statistics scripts. [KNOWN: tree]
- **Where humans act:** the researcher writes a dataset loader, registers it, edits a YAML config and a Slurm script, and picks pre-training or fine-tuning. [KNOWN: README L39-L70]
- **What it is not:** not a pip-installable package on PyPI (a different "matey" project owns that name), not a pretrained-model download, and not a general LLM. [KNOWN: https://pypi.org/pypi/matey/json is an unrelated database tool; no weights in repo]
- **What's unknown:** which pretrained checkpoints exist and whether any are public; how much of the MPP seed code remains.
- **Example:** `examples/config/Demo_JHUTDB_TT.yaml` trains the "turbt" (Turbulence Transformer) model, 192-dim embedding, 12 blocks, with a three-level hierarchy and sequence-parallel groups of 16 GPUs, on Johns Hopkins turbulence data. [KNOWN: https://github.com/ORNL/MATEY/blob/631a4139295d4f51e573d474cff7d6586f3aa310/examples/config/Demo_JHUTDB_TT.yaml#L33-L59]

## What it is (plain English, 2-4 sentences)
MATEY ("multiscale adaptive transformer models") is ORNL's research framework for spatiotemporal surrogate and foundation models of physical systems. It packages several transformer backbones (ViT, sViT, AViT, TurbT), adaptive and hierarchical tokenization, structured and graph inputs, 42 registered dataset names, and DDP/FSDP plus RingX sequence parallelism for Frontier-scale training. Its papers report the model, a plasma-edge surrogate, and turbulence runs on Frontier. [KNOWN: tree; OSTI 3365777, 3364707, 3367073]

## How it works (plain English, no jargon without definition)
1. **Data loading.** Each dataset family has a loader class (PDEBench, The Well, BLASTNet, Johns Hopkins turbulence, SOLPS-ITER, XGC, Gkeyll, BubbleML, MeshGraphNets airfoil, miniWeather colliding thermals, liquid-metal MHD and others), registered by name in `DSET_NAME_TO_OBJECT`. A `MixedDataset` and `MultisetBatchSampler` mix several datasets in one run. [KNOWN: https://github.com/ORNL/MATEY/blob/631a4139295d4f51e573d474cff7d6586f3aa310/matey/data_utils/datasets.py#L32-L97; `mixed_dset_batchsampler.py`] Data are not shipped; configs point to cluster paths. Two MATEY datasets are public on Zenodo (colliding thermals, liquid-metal MHD, CC-BY-4.0). [KNOWN: example configs; Zenodo 19889470 and 19857523 descriptions name the MATEY study]
2. **Normalize and tokenize.** Each sample is normalized, then cut into patches by "tokenizer heads" (`hMLP_stem` for grids, `GraphhMLP_stem` for graphs). Several patch sizes can be configured per head. [KNOWN: `models/basemodel.py` L31-L95; `spatial_modules.py` L213, L349]
3. **Adaptive refinement.** Patches are scored by variance; either the top `refine_ratio` fraction or every patch above `gammaref` times the maximum variance is re-tokenized at a finer patch size and merged back into the sequence. [KNOWN: https://github.com/ORNL/MATEY/blob/631a4139295d4f51e573d474cff7d6586f3aa310/matey/data_utils/shared_utils.py#L106-L127; `models/vit.py` L157-L160; `basemodel.py` L351-L536] The paper calls these "two novel adaptive tokenization schemes". [KNOWN: OSTI 3365777 abstract]
4. **Backbone.** Choose by `model_type`: `vit_all2all` (full spatiotemporal attention), `svit` (space then time, each all-to-all), `avit` (axial spatial plus temporal attention, the MPP-style design), or `turbt` (hierarchical Turbulence Transformer that filters the field into coarser levels). [KNOWN: `models/avit.py` L43-L60, `svit.py` L46-L56, `turbt.py` L50-L90; config comments in Demo_JHUTDB_TT.yaml L33-L38] The paper found fully decoupled axial attention "less efficient and expressive". [KNOWN: OSTI 3365777 abstract]
5. **Optional conditioning.** Lead-time MLP (predict further ahead), conditional inputs, super-resolution ratio. [KNOWN: `basemodel.py` L31, L89-L90; `time_modules.py`]
6. **Decode and loss.** `hMLP_output` maps tokens back to fields; outputs are de-normalized. [KNOWN: `vit.py` L233-L248]
7. **Parallel training.** `setup_dist` reads Slurm variables and starts `torch.distributed` with backend "nccl" (RCCL on AMD); the model is wrapped in FSDP (`use_orig_params=True`, size-based auto-wrap) or DDP. Ranks are grouped into sequence-parallel groups (`sp_groupsize`); each sample's 3D domain is split into blocks across the group, and attention runs through `ringX_attn_func`, a ring-style parallel attention built on flash-attention kernels. [KNOWN: https://github.com/ORNL/MATEY/blob/631a4139295d4f51e573d474cff7d6586f3aa310/matey/utils/distributed_utils.py#L27-L58 and #L120-L170; https://github.com/ORNL/MATEY/blob/631a4139295d4f51e573d474cff7d6586f3aa310/matey/train.py#L197-L205; `models/attention_modules.py` L13, L71-L83; `models/ringX_attn.py` L7, L265, L376]
8. **Launch.** Example Slurm scripts run 8 ranks per node with `--gpu-bind=closest`, set per-job MIOpen caches on node-local NVMe, and source a shared ROCm 6.3.1 Conda environment on Frontier. [KNOWN: https://github.com/ORNL/MATEY/blob/631a4139295d4f51e573d474cff7d6586f3aa310/examples/submit_batch.sh#L33-L42; README L6-L13]

## How the project is organized
From templates/engineering-checklist.md, at commit 631a413.
- **Repo layout:** `matey/models/` (backbones, attention, RingX), `matey/data_utils/` (11 format-specific loader modules plus shared utilities), `matey/utils/` (distributed, training, logging, visualization, XGC/SOLPS plotting), `matey/trustworthiness/` (turbulence descriptors and metrics), `matey/postprocess/` (plot scripts and notebooks), `matey/train.py` (902-line `Trainer`), `matey/inference.py`; `examples/` (23 YAML configs, 8 Slurm scripts, 3 Python entry points); `third_party/XGC_reader` (git submodule to an outside XGC reader repo); `tests/` holds only `.gitkeep`. 108 tracked files. [KNOWN: tree, `.gitmodules`]
- **Languages and dependencies:** Python 3.10 to 3.14 per pyproject (README option 2 still says Python 3.9); einops, h5py, timm, zarr, netcdf4, mpi4py, wandb, `flash-attn` (Python below 3.12), `adan-pytorch`, `dadaptation`, Sandia's `exodusii` from GitHub. PyTorch itself is not pinned in pyproject. [KNOWN: https://github.com/ORNL/MATEY/blob/631a4139295d4f51e573d474cff7d6586f3aa310/pyproject.toml#L1-L36; README L14-L18; INFERRED: torch comes from the environment]
- **Build:** Poetry (`pyproject.toml` + `poetry.lock`), plus `requirements.txt` and `setup.py`. [KNOWN: README L20-L28]
- **Tests:** none (empty `tests/`). [KNOWN]
- **CI:** none (no `.github/workflows`). [KNOWN]
- **Target machines:** Frontier is the only machine with a ready environment and job scripts (Slurm scripts with an OLCF allocation, ROCm, MIOpen, `-C nvme`; the allocation ID is left out under rule 16). The IPDPS paper reports runs "up to 1.1 EFLOPS on 32,768 AMD GPUs" on Frontier. [KNOWN: README L6-L13; submit_batch.sh L2, L9, L33; OSTI 3367073 abstract] The MLST paper's sponsor list includes NERSC, so some work also used NERSC resources; two example inference scripts carry an `--on_perlmutter` flag. [KNOWN: OSTI 3365777 sponsor field; `examples/basic_inference.py` L19; INFERRED: resource use]
- **Docs:** README only; config comments explain options. [KNOWN]
- **Releases:** one tag, v1.0.0 (2026-01-26), commit "Add MIT license headers and finalize v1.0.0", same date as DOE CODE. pyproject still says version 0.1.0. [KNOWN: git log, pyproject L3]
- **Contribution path:** no CONTRIBUTING file; development is by pull requests (53 PRs, 4 open) with review. [KNOWN: GitHub search API; merge commit 631a413 "Merge pull request #57"]
- **Data and reproducibility:** configs and scripts reference cluster paths; two datasets on Zenodo; branch `paper-matey-solps2025` holds paper-specific code. No pretrained weights published in the repo. [KNOWN: configs; Zenodo; `git branch -r`]
- **Deployment statements:** papers use "propose", "assess", "demonstrate", "perform scaling and science runs". No production claim. [KNOWN: OSTI abstracts]
- **Why it was built this way:** partly stated. Adaptive tokenization addresses "extremely long, computationally prohibitive token sequences"; RingX exists because ring attention's point-to-point pattern "fails to fully exploit" HPC networks. [KNOWN: OSTI 3365777 and 3005443 abstracts] Why FSDP plus custom sequence parallelism rather than another framework is [UNKNOWN].

## Timeline
| Date | Event | Source | Tag |
|---|---|---|---|
| 2023-10-07 | Author date of the seed commit (snapshot of PolymathicAI MPP, commit 67ffa35) | git log 856c13f; README L79 | [KNOWN] |
| 2024-01-24 | Squashed commit: "2D adpative tokenization; add MW and MHD cases; sts transformer" | git log e30068e | [KNOWN] |
| 2024-12 | NeurIPS 2024 ML4PS workshop paper; arXiv 2412.20601 | OSTI 3002823; arXiv | [KNOWN] |
| 2025-06-30 | GitHub repo created | GitHub API | [KNOWN] |
| 2025-07-01 | Squashed commit adding turbulence transformer, RingX, package restructure | git log 8287288 | [KNOWN] |
| 2025-11 | RingX paper at SC25 (ORNL; same RingX name as MATEY's module) | OSTI 3005443 | [KNOWN] |
| 2026-01-26 | v1.0.0 tag; DOE CODE code-173753 | git tags; OSTI | [KNOWN] |
| 2026-05 | MLST journal paper; Nuclear Fusion plasma-edge paper; IPDPS 2026 turbulence paper | OSTI 3365777, 3364707, 3367073 | [KNOWN] |
| 2026-09-17 | Last push: merge of fusion-related work into main (PR #57) | git log 631a413 | [KNOWN] |

## Who uses it / why it matters
Outside use is not visible: no GitHub dependents, no PyPI/conda/Spack package. The MLST paper has six citing works in OpenAlex, four with ORNL authors and two outside-only (University of Michigan; one with no institution listed). [KNOWN: GitHub dependents page; registries; OpenAlex 2026-11-11] It matters as ORNL's public example of a physics foundation-model codebase engineered for Frontier, including a published exascale run. [KNOWN: OSTI 3367073; INFERRED: significance]

## Related projects
| Related item | Relationship | Source | Tag |
|---|---|---|---|
| HydraGNN (`hydragnn`) | shares code: MATEY's `parse_slurm_nodelist` is marked "from" a pinned HydraGNN file | https://github.com/ORNL/MATEY/blob/631a4139295d4f51e573d474cff7d6586f3aa310/matey/utils/distributed_utils.py#L239-L240 | [KNOWN] (one helper function, not architecture) |
| Frontier (OLCF) | same facility: main target machine | README L6-L13; OSTI 3367073 | [KNOWN] |
| PolymathicAI multiple_physics_pretraining (outside) | seed codebase | README L79; git log 856c13f | [KNOWN] |
| RingX (ORNL SC25 paper) | MATEY ships a `ringX_attn` module; IPDPS paper names "a novel RingX sequence parallelism approach" | OSTI 3005443, 3367073; `models/ringX_attn.py` | [KNOWN] name and module; identical code [UNKNOWN] |
| XGC_reader (outside GitHub repo) | submodule for XGC fusion data | `.gitmodules` | [KNOWN] |
| flash-attention, Sandia exodusii (outside) | dependencies | pyproject | [KNOWN] |
| Microsoft Aurora model (outside) | position-encoding code marked "adopted from" its repo | `matey/models/positionbias_modules.py` L24 | [KNOWN] |
| Other ORNL foundation-model work (for example ORBIT) | no reference found in repo or papers read | grep of repo | [UNKNOWN] |

## What stands out
- Development is concentrated: 171 commits, top three authors 58%, 27% and 11%; 141 of them in 2026. Several large changes landed as squashed commits, so history understates earlier work. [KNOWN: git log; INFERRED: understatement]
- The README credits ORNL staff and named summer interns from UIUC, Georgia Tech, UC Irvine and Vanderbilt, an internship-to-codebase pipeline visible in public. [KNOWN: README L81-L95; people by role here]
- No tests and no CI in a codebase used for an exascale paper. Correctness is checked in papers and post-processing scripts, not in the repo. [KNOWN: tree; INFERRED: where checking happens]
- Funding on the MLST record mixes LDRD, ASCR SciDAC, BES user facilities and NERSC; the DOE CODE record lists ORNL itself as sponsor. [KNOWN: OSTI 3365777, code-173753]

### Reusable ideas [INFERRED]
- Variance-based patch refinement is a cheap, model-agnostic way to spend tokens where the field is busy; it needs only `unfold` and `topk`.
- A name-to-class dataset registry plus per-family base classes keeps dozens of heterogeneous scientific formats behind one interface.
- Splitting a 3D domain into blocks across a sequence-parallel group (choosing the factorization with `closest_factors`) maps the physics decomposition onto the attention decomposition.
- Putting MIOpen kernel caches on node-local NVMe per job avoids shared-filesystem contention on AMD systems; a small operational trick worth copying.
- Swappable backbones behind one `BaseModel` make architecture comparisons (joint vs decoupled attention) a config change.

## Ten questions (GOAL.md)
1. **What problem does it solve, and for whom?** Training transformer surrogates and foundation models for multiscale physics without impossible sequence lengths, for computational scientists. [KNOWN: OSTI 3365777]
2. **Where does it sit in the tree?** ORNL AI for science, HPC; runs on OLCF Frontier. Org unit not stated. [KNOWN: README, OSTI; UNKNOWN: org unit]
3. **Who pays for it?** MLST paper: LDRD, ASCR SciDAC, BES SUF, NERSC; DOE CODE: ORNL. [KNOWN: OSTI 3365777, code-173753]
4. **How is the code organized?** Python package `matey/` with models, data, utils, trainer; YAML configs and Slurm scripts; Poetry build. [KNOWN]
5. **Is it alive?** Yes: commits rose from 28 (2025) to 141 (2026), seven authors in 2026, PRs merged as recently as 2026-09-17. [KNOWN: git log]
6. **Who outside ORNL uses or cites it?** Two outside citing works for the MLST paper; no package dependents. [KNOWN: OpenAlex]
7. **What does it connect to?** PyTorch, flash-attention, MPP seed, XGC and SOLPS fusion data, HydraGNN (one helper), Frontier. [KNOWN]
8. **What does it teach about how ORNL works?** Research code grows by squashed merges and interns, gets a DOE CODE record at v1.0, and is paired with papers across fusion, turbulence and ML venues. [KNOWN: git log, OSTI; INFERRED: the pattern]
9. **Could a student learn from it?** Partly: the model code is readable, but running it needs a GPU cluster, data downloads and editing cluster paths. [INFERRED from configs and scripts]
10. **What is still unknown?** Pretrained weights, how much MPP code remains, exact RingX code lineage, outside users. Searches logged in verification/not-found.md.

## Known / Inferred / Unknown
- KNOWN: ownership, license, seed origin, model variants, adaptive tokenization method, parallelism stack, Frontier scripts, datasets registry, papers and funding, history counts.
- INFERRED: significance, reading of squashed history, torch from environment, NERSC resource use, reusable ideas.
- UNKNOWN: org unit, weights, outside users, relation to other ORNL foundation models, RingX code identity.

## Verification notes
Sweep 1 (discovery and reading pass, 2026-11-11): fresh `--filter=blob:none` clone at 631a413; read README, LICENSE, pyproject, models, data registry, distributed utils, trainer setup, configs, Slurm scripts; OSTI API records code-173753, 3365777, 3364707, 3367073, 3002823, 3005443; Zenodo dataset records; arXiv 2412.20601 title. Code read, not run. Sweep 2 not done.

Sweep 2 (fact-check pass, 2026-11-11, by the coordinator, independent of the discovery researcher): Re-fetched at 631a413: LICENSE (MIT, 2026 UT-Battelle); README L79 (seed statement); `matey/data_utils/shared_utils.py` L106-L127 (variance-based patch refinement). OSTI API: code-173753 (ORNL research org; sponsor field names ORNL); 3365777 sponsors (NERSC, LDRD, ASCR SciDAC, BES SUF); the 3367073 abstract (1.1 EFLOPS on 32,768 AMD GPUs). Commit spot check on an independent clone: 171 commits; per year 1/1/28/141, an exact match. Correction: removed an OLCF allocation ID quoted from a job script in this brief and in the signals file (rule 16 keeps out infrastructure identifiers). Not re-checked: FSDP and sequence-parallel line ranges, the dataset registry count.

## Sources (URL, title, accessed date, what it supports)
All accessed 2026-11-11.
- https://github.com/ORNL/MATEY and https://api.github.com/repos/ORNL/MATEY (metadata)
- https://github.com/ORNL/MATEY/blob/631a4139295d4f51e573d474cff7d6586f3aa310/README.md (purpose, Frontier env, seed origin, publications, contributors)
- https://github.com/ORNL/MATEY/blob/631a4139295d4f51e573d474cff7d6586f3aa310/LICENSE#L1-L3
- https://github.com/ORNL/MATEY/blob/631a4139295d4f51e573d474cff7d6586f3aa310/matey/data_utils/shared_utils.py#L106-L127 (variance refinement)
- https://github.com/ORNL/MATEY/blob/631a4139295d4f51e573d474cff7d6586f3aa310/matey/data_utils/datasets.py#L32-L97 (dataset registry)
- https://github.com/ORNL/MATEY/blob/631a4139295d4f51e573d474cff7d6586f3aa310/matey/utils/distributed_utils.py#L27-L58, #L120-L170, #L239-L240 (dist setup, sequence parallel, HydraGNN-derived helper)
- https://github.com/ORNL/MATEY/blob/631a4139295d4f51e573d474cff7d6586f3aa310/matey/train.py#L197-L205 (FSDP/DDP)
- https://github.com/ORNL/MATEY/blob/631a4139295d4f51e573d474cff7d6586f3aa310/matey/models/ringX_attn.py (RingX attention)
- https://github.com/ORNL/MATEY/blob/631a4139295d4f51e573d474cff7d6586f3aa310/examples/submit_batch.sh#L33-L42 (Frontier launch)
- https://github.com/ORNL/MATEY/blob/631a4139295d4f51e573d474cff7d6586f3aa310/examples/config/Demo_JHUTDB_TT.yaml#L33-L59 (TurbT config)
- https://www.osti.gov/doecode/biblio/173753 and https://www.osti.gov/api/v1/records/code-173753 (DOE CODE)
- https://www.osti.gov/biblio/3365777 (MLST paper), https://www.osti.gov/biblio/3364707 (Nuclear Fusion), https://www.osti.gov/biblio/3367073 (IPDPS), https://www.osti.gov/biblio/3002823 (NeurIPS workshop), https://www.osti.gov/biblio/3005443 (RingX)
- https://arxiv.org/abs/2412.20601 (MATEY preprint, title confirmed)
- https://zenodo.org/records/19889470 and https://zenodo.org/records/19857523 (MATEY datasets)
- https://github.com/PolymathicAI/multiple_physics_pretraining (seed repo, MIT)
- https://api.openalex.org/works/doi:10.1088/2632-2153/ae67d1 (citations)

## Quality gate
- [x] Every load-bearing claim has a source and a tag
- [x] Facts are kept apart from interpretation
- [x] ORNL relationship is not overstated, and maturity verbs match the source (RULES item 10)
- [x] Walkthrough, flow, timeline and unknowns are present
- [x] Ten questions answered or marked UNKNOWN
- [x] No copied text beyond short cited quotes; people by role only
- [x] Two fact-check sweeps done (RULES item 11): Sweep 1 and Sweep 2 both 2026-11-11
- [x] INDEX, catalog, LAB-TREE and connections map updated (batch 13) (coordinator)
