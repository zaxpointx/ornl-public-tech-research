# HydraGNN
- Official page: none separate from the repo [KNOWN: GitHub API shows empty homepage, https://api.github.com/repos/ORNL/HydraGNN]
- Repo: https://github.com/ORNL/HydraGNN
- Docs: README, USER_MANUAL.md and a GitHub wiki (https://github.com/ORNL/HydraGNN/wiki/Install)
- License: BSD 3-Clause, copyright 2021 Oak Ridge National Laboratory [KNOWN: LICENSE file, https://github.com/ORNL/HydraGNN/blob/main/LICENSE]
- Status: active, last push 2026-10-24 [KNOWN: GitHub API]

## What it is (plain English, 2-4 sentences)
HydraGNN is a Python toolkit for training graph neural networks (GNNs) that predict properties of molecules and materials [KNOWN: README]. A *graph* here means atoms as dots (nodes) joined by lines (edges) for bonds or nearby neighbors, and a GNN is a type of AI model that learns from that shape directly. "Multi-headed" means one model has several output "heads", so it can predict several things at once, like a molecule's energy and the forces on each atom [KNOWN: README capabilities list]. It's built to train on supercomputers, not just one GPU [KNOWN: README].

## How it works (plain English, no jargon without definition)
- You describe the model and data in a config file. The code turns raw chemistry data (for example the QM9 or Open Catalyst datasets) into graphs, trains a GNN on them, and reports how accurate the predictions are [INFERRED: from the config, preprocess, train and postprocess folders and the examples directory].
- The type of GNN layer is a setting you can swap, not hard-coded [KNOWN: README says convolutional layers are a hyperparameter]. Some of the layer options are "equivariant", which means that if you rotate a molecule in space, the model's predictions rotate with it the right way. Physics works like that, so these models tend to learn more reliably [KNOWN: README lists EGNN, PaiNN, MACE, DimeNet; explanation is general background, INFERRED].
- To scale up, it spreads training across many GPUs using PyTorch's distributed tools (DDP, FSDP) and Microsoft's DeepSpeed [KNOWN: README]. DDP copies the model onto every GPU and splits the data between them. FSDP also splits the model itself, so bigger models fit in memory.
- It can also act as a *machine-learned interatomic potential*. That's a fast AI stand-in for expensive quantum-chemistry calculations of how atoms push and pull on each other [KNOWN: README capability; definition INFERRED general background].
- Newer features include constraint-aware training for power-grid "optimal power flow" problems, which is a sign the tool is being used outside chemistry too [KNOWN: README; examples/opf and examples/opflearn folders].

## How the project is organized (repo structure, languages, build, maintainers/org unit, release cadence)
- Languages: about 87% Python and 13% shell scripts [KNOWN: https://api.github.com/repos/ORNL/HydraGNN/languages].
- `hydragnn/` is the package itself, with subfolders for `models`, `train`, `preprocess`, `postprocess`, `distributed`, `config`, `data`, `domain_losses`, `third_party` and `utils` [KNOWN: repo tree].
- `examples/` holds about 35 ready-made dataset setups (QM9, MD17, Open Catalyst 2020/2022/2025, Open Materials 2024, ZINC and more) [KNOWN: repo tree].
- `scripts/hpc/olcf/frontier/` holds install scripts for Frontier, ORNL's supercomputer, which uses AMD GPUs and therefore ROCm, AMD's GPU software stack [KNOWN: repo tree has install-rocm64/71/72 scripts; Frontier nodes use AMD MI250X GPUs per https://docs.olcf.ornl.gov/systems/frontier_user_guide.html, accessed 2026-10-24].
- Build: a standard Python package using `pyproject.toml`, plus `install_dependencies.sh`. It supports Python 3.11 to 3.14 and depends on PyTorch and PyTorch Geometric [KNOWN: README].
- Tests run with pytest (`tests/`, `pytest.ini`) [KNOWN: repo tree].
- Contributors: about 22 listed by the GitHub API, counting anonymous ones [KNOWN: /contributors?anon=1 pagination, accessed 2026-10-24].
- Releases: v2.0.0 (2023-01-20), v3.0 (2023-11-10), v4.0 (2025-08-15) and v5.0 (2026-04-14). That's roughly one major release a year [KNOWN: GitHub releases API]. The repo was created 2021-05-28 [KNOWN: GitHub API].
- Org unit: [UNKNOWN]. Nothing in the repo names an ORNL division.
- Software DOI on DOE CODE/OSTI: 10.11578/dc.20211019.2, plus 10.11578/dc.20260512.1 for v5.0 [KNOWN: CITATION.cff]. DOE CODE also has records for v3.0 (code-121354) and v4.0 (code-164024); all list ORNL as research org, and the v5.0 record (code-180990) also lists AMD [KNOWN: https://www.osti.gov/api/v1/records?q=HydraGNN&product_type=Software, accessed 2026-10-24].

## Who uses it / why it matters
- It's for scientists who want to screen huge numbers of molecules or materials (for batteries, catalysts, carbon capture and so on) with AI instead of slow simulations [INFERRED: from example datasets such as open_direct_air_capture_2023 and open_catalyst].
- 127 stars and 48 forks [KNOWN: GitHub API counts]. Stars aren't users: the connections-pass signals work found every OpenAlex citing paper that mentions it has ORNL authors, and its 2 GitHub dependents are PyPI mirror repos, so visible use is mostly in-house [INFERRED; see signals/hydragnn.md].
- Specific outside users: [UNKNOWN].

## Related projects
- It runs on OLCF Frontier, see olcf-user-docs [INFERRED: Frontier install scripts].
- It overlaps with GridKit and the power-grid domain through its optimal power flow examples [INFERRED: examples/opf, no stated link].
- It uses ADIOS as an optional feature for data I/O [KNOWN: README mentions "HPO, ADIOS, etc." under optional extras].

## Known / Inferred / Unknown
- [KNOWN] BSD-3 license, Python/PyTorch, multi-GPU training, about 35 example datasets, Frontier scripts, 4 major releases.
- [INFERRED] Used for AI-driven materials and chemistry screening, and is spreading into grid optimization.
- [UNKNOWN] Owning ORNL division, named outside users, and the papers that describe it, which weren't pulled this pass.

## Sources (URL, accessed date)
- https://github.com/ORNL/HydraGNN (README, LICENSE, CITATION.cff, repo tree), accessed 2026-10-24
- https://api.github.com/repos/ORNL/HydraGNN (+ /languages, /releases, /contributors), accessed 2026-10-24
- https://github.com/ORNL/HydraGNN/wiki/Install, linked from the README, not opened this pass

## Fact-check notes (2026-10-24)
- Corrected: example dataset count about 40 -> about 35 (35 folders in examples/).
- Corrected: package subfolder list was incomplete; added data, domain_losses, third_party.
- Retagged: Frontier uses AMD GPUs, INFERRED -> KNOWN (OLCF Frontier user guide).
- Added: DOE CODE records for v3.0, v4.0 and v5.0 confirm ORNL as research org; v5.0 also lists AMD.
- Verified against GitHub API, README, LICENSE, CITATION.cff: license, languages, releases, contributors, created date, stars/forks, Python 3.11-3.14, DDP/FSDP/DeepSpeed, equivariant layers, interatomic potentials, OPF training, ADIOS extra.
- No restricted content or implied ORNL affiliation found. No verbatim copying beyond short phrases.
