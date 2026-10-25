# TNQVM (Tensor Network Quantum Virtual Machine)
- Official docs: none of its own. The README points to the XACC docs at https://xacc.readthedocs.io. [KNOWN: README]
- Repo: https://github.com/ORNL-QCI/tnqvm (default branch `master`). GitHub's description is "Tensor Network QPU Simulator for Eclipse XACC". [KNOWN: GitHub API]
- License: BSD 3-Clause per the README ("TNQVM is licensed - BSD 3-Clause"). There's no LICENSE file in the repo, and the GitHub API license is null. Source headers carry "Copyright (c) 2019, UT-Battelle". [KNOWN: README, repo file list, `CMakeLists.txt` lines 1-3; this wording follows the editorial decision recorded in the catalog row]
- Status: unknown (rule 14). The last commit and push were 2025-03-05 (commit at 15:50 ET). There are no releases or tags, and the repo isn't archived. The `VERSION` file says 0.1.9. More than a year with no push and no tagged release counts as unknown under the team's status convention. Quiet doesn't mean dead (rule 10). [KNOWN: git log, GitHub API, VERSION]
- Scope (rule 13): CORROBORATED. UT-Battelle holds the copyright in the source headers. OSTI 2583844 (a 2022 journal article on TNQVM at exascale) and OSTI 2251617 (a PEPS plugin record, 2023) list ORNL as research org. [KNOWN: CMakeLists.txt; OSTI API records 2583844 (journal article, 2022-10-21) and 2251617 (conference paper, 2023-11-01), re-fetched in the fact-check pass 2026-10-24]
- Org unit: ORNL-QCI GitHub org, same as ExaTN and QIR-EE. [INFERRED: a quantum computing group, no division named]

## Plain-language walkthrough
- **What it is:** a plug-in that lets XACC, ORNL's quantum programming framework, run quantum programs on an ordinary classical computer by simulating them with tensor networks. [KNOWN: README]
- **Key terms:**
  - In XACC, an *Accelerator* is any back end that can run a quantum circuit: real quantum hardware or a simulator. TNQVM is one of those.
  - A *visitor* is a piece of code that walks through a circuit gate by gate and does something with each gate. Here it turns each gate into tensor operations.
  - An *MPS* (matrix product state) is a tensor-network shape that chains one small tensor per qubit. It's cheap when qubits aren't very entangled.
  - *MPO* and *density matrix* (DM) variants can also model noise. [KNOWN: visitor folder names `exatn-mps`, `exatn-mpo`, `exatn-dm`; INFERRED: the explanations]
- **The problem:** a full simulation of n qubits needs memory that doubles with every qubit, so around 50 qubits it's out of reach. Tensor networks compress circuits that don't have too much entanglement, so researchers can check quantum algorithms and compilers at sizes where brute force fails. The 2018 PLOS ONE paper cited in the README is about "validating quantum-classical programming models with tensor network simulations". [KNOWN: README citation title; INFERRED: the memory explanation]
- **What goes in:** a quantum circuit written with XACC, in C++ or Python, plus a choice of visitor (for example `exatn`, `exatn-mps` or `exatn-gen`). [KNOWN: README code samples]
- **What happens:**
  1. XACC hands the compiled circuit to TNQVM.
  2. The chosen visitor converts the gates into a tensor network.
  3. A back end contracts it: ExaTN for the `exatn*` visitors, or the ITensor library for the older `itensor` path.
  4. With `exatn-mps` and an MPI-enabled ExaTN, the work can spread across several nodes. [KNOWN: README "MPI Execution", `tnqvm/visitors/`]
- **What comes out:** measurement results, bitstring counts, expectation values or amplitudes, returned through XACC like any other back end. [INFERRED: from XACC's Accelerator interface and the examples' names]
- **Where humans act:** a quantum-software researcher writes the circuit, picks the visitor, and builds XACC, then ExaTN (optional), then TNQVM. [KNOWN: README install steps]
- **What it is not:** it isn't a quantum computer, and it isn't a general tensor library. That's ExaTN. It's also not a standalone app: XACC has to be installed. [KNOWN: README; INFERRED: the division of labor]
- **What's unknown:** whether it builds against current XACC and ExaTN, since XACC and ExaTN are both quiet too (see their briefs), and whether anyone maintains it.
- **Example:** `examples/sycamore/` contains programs that compute amplitudes of circuits shaped like Google's Sycamore supremacy experiment, plus a parser for circuit files in qFlex format. [KNOWN: folder and file names; INFERRED: the Sycamore meaning]

## How it works
- `tnqvm/base/Gates.hpp` defines the gate tensors. `tnqvm/visitors/` holds one folder per back end (`exatn`, `exatn-mps`, `exatn-mpo`, `exatn-dm`, `exatn-gen`, `itensor`). Each folder has an `Activator.cpp` and a `manifest.json`, which is how CppMicroServices (the plug-in loader XACC and ExaTN also use) finds them. [KNOWN: tree; per the xacc and exatn briefs]
- The ExaTN path is optional at build time (`-DEXATN_DIR`), and MPI is optional (`-DTNQVM_MPI_ENABLED=TRUE`). [KNOWN: README]

## How the project is organized
- Top level: `tnqvm/` (base, visitors, utils, tests), `examples/` (base_api, mpi, multiple_visitors, exatn_gen, sycamore, plos_one_experiments), `python/`, `cmake/` (including a `spack` folder), `docker/ci/ubuntu1804`, `tools/wheels`, `scripts/`, `setup.py` and `Dockerfile`. 484 tracked files. [KNOWN: tree, git ls-files]
- Languages: C++ about 96.8% by bytes, CMake 1.9%, then small amounts of Makefile, Python, C, Shell and Dockerfile. [KNOWN: GitHub languages API]
- CI: a GitHub Actions `build.yml` (Linux), plus a `.gitlab-ci.yml` for a non-public pipeline, which is out of scope (rule 16) and wasn't followed. [KNOWN: repo files]
- History: 636 commits on `master`, from 2016-11-11 to 2025-03-05. By year there's 1 in 2016, 115 in 2017, 55 in 2018, 52 in 2019, 247 in 2020, 137 in 2021, 25 in 2022, 0 in 2023, 2 in 2024 and 2 in 2025. The 2020-2021 peak lines up with the ExaTN integration era. Created 2016-11-08. 48 stars and 11 forks. [KNOWN: git log, GitHub API; INFERRED: the era link]
- Contributors: 11 including anonymous commit authors, 5 GitHub accounts. [KNOWN: GitHub API]

## Who uses it / why it matters
It was XACC's tensor-network simulator, and the bridge between XACC and ExaTN. Together the three were ORNL's quantum software stack for simulating circuits on supercomputers; the README mentions "Summit-like architectures". [KNOWN: README; INFERRED: the stack framing] The few commits in 2024-2025 are small compatibility fixes, which suggests light upkeep rather than active development. [KNOWN: commit messages; INFERRED] Usage evidence goes in `signals/tnqvm.md` once it exists.

## Related projects
- XACC (`xacc`): TNQVM is an Accelerator plug-in for it. [KNOWN: README, map]
- ExaTN (`exatn`): optional tensor back end. [KNOWN: README, map link 83]
- QIR-EE (`qiree`): same GitHub org. [KNOWN]
- ITensor (outside library): the older MPS back end. [KNOWN: `visitors/itensor`]

## Known / Inferred / Unknown
- KNOWN: license wording and its missing file, copyright header, dates, no tags, VERSION, visitors, build flags, layout, counts, citation.
- INFERRED: the term explanations, the Sycamore meaning, the era link, the upkeep reading.
- UNKNOWN: maintenance, whether it builds with current dependencies, users, any successor (none named).

## Sources (accessed 2026-10-24)
- https://github.com/ORNL-QCI/tnqvm (README.md, CMakeLists.txt, VERSION, tnqvm/, examples/, .github/workflows/build.yml)
- https://api.github.com/repos/ORNL-QCI/tnqvm (plus /languages, /releases, /tags, /contributors with and without anon=1)
- https://doi.org/10.1371/journal.pone.0206704 (PLOS ONE 2018, cited in the README, not read)
- OSTI 2583844 and 2251617 (per the catalog row)

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Verified on a fresh clone of ORNL-QCI/tnqvm and public records: no LICENSE file, README "BSD 3-Clause" line, UT-Battelle 2019 header in CMakeLists.txt, VERSION 0.1.9, no tags, `build.yml` and `.gitlab-ci.yml` present, 636 commits on `master` with the stated per-year counts, first 2016-11-11, last 2025-03-05 15:50 ET, contributors 11 with anonymous and 5 accounts, README "Summit-like architectures". OSTI 2583844 and 2251617 both list ORNL as research org.
- Clarified: the rule 13 OSTI sources are now re-fetched, and 2251617 is a conference paper, not a software record. No facts changed.
