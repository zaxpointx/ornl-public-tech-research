# ExaTN (Exascale Tensor Networks)
- Official page: none separate. The README is the docs and links the ExaTN paper (Frontiers in Applied Mathematics and Statistics, 2022): https://www.frontiersin.org/articles/10.3389/fams.2022.838601/full [KNOWN: README]
- Repo: https://github.com/ORNL-QCI/exatn (default branch `devel`). GitHub's description is "Hierarchical Tensor Networks at Exascale". [KNOWN: GitHub API]
  - The README's CI badges point to an ORNL-hosted GitLab. Per rule 16, I didn't follow them, because they go to an ORNL host that may need sign-in.
- License: BSD 3-Clause, "Copyright (c) 2017, UT-Battelle". The GitHub API also says BSD-3-Clause. [KNOWN: LICENSE lines 1-3, GitHub API]
- Status: unknown (rule 14).
  - The last commit was 2023-07-19 and the last push 2023-07-24 UTC. It isn't archived, and there are no releases or tags. [KNOWN: git log, GitHub API]
  - That's more than three years quiet. Quiet doesn't mean dead (rule 10).
- Scope (rule 13): CORROBORATED. UT-Battelle holds the copyright and DOE CODE code-45739 (2018-10-01) lists ORNL as research org. [KNOWN: LICENSE; https://www.osti.gov/doecode/biblio/45739 per the discovery pass]
  - Org unit: the repo sits in ORNL-QCI, the same GitHub org as QIR-EE and TNQVM. The org name suggests a quantum computing group, but no page I read names the division, so it stays [INFERRED].

## Plain-language walkthrough
- **What it is:** a C++ library (with Python bindings) for building and computing "tensor networks". These are a way to break a gigantic multi-dimensional array into many small connected pieces so you can work with it at all. It runs anywhere from a laptop to GPU supercomputers. [KNOWN: README]
- **Key terms:**
  - A *tensor* is a multi-dimensional array of numbers: a vector is 1-D, a matrix is 2-D, and tensors keep going.
  - A *tensor network* is a graph where each dot is a small tensor and each line is a shared index. *Contracting* the network means multiplying and summing along those lines to get the final answer.
  - The order you contract in can change the cost by orders of magnitude, so finding a good order is a big deal. [KNOWN: README's definitions of TensorNetwork and output tensor; INFERRED: the explanation and the cost point]
- **The problem:** the full state of a 50-qubit quantum computer, or of many interacting electrons, is too large to store directly. Tensor networks compress it, but contracting big networks still needs lots of memory and many GPUs working together. ExaTN handles that bookkeeping and the parallel execution. [KNOWN: README domain list; INFERRED: the qubit example]
- **What goes in:** tensors you declare with a name and shape, the network connecting them, and operators or expansions built from networks, all through C++ or Python calls. [KNOWN: README "Declarative API"]
- **What happens:**
  1. Declaring objects allocates nothing.
  2. When you call the executive API, ExaTN allocates storage.
  3. It builds a task graph of the tensor operations, optimizes it, and runs it with an executor, on CPU through BLAS or on NVIDIA GPUs through cuTensor/cuQuantum, optionally across nodes with MPI. [KNOWN: README "Executive API", `src/runtime/{graph,optimizer,executor}`, Dependencies; INFERRED: the order]
- **What comes out:** result tensors, such as an amplitude of a simulated quantum circuit or an energy from a many-body calculation. ExaTN also includes eigensolver, linear-solver and optimizer helpers. [KNOWN: `src/exatn/` file names; INFERRED: the examples]
- **Where humans act:** a physicist or quantum-software developer designs the network and chooses build options like GPU, BLAS and MPI. [KNOWN: README build options; INFERRED]
- **What it is not:** it isn't a quantum computer or a full circuit simulator by itself. TNQVM is the piece that turns XACC circuits into ExaTN networks. [KNOWN: map link 162; INFERRED: the division of labor]
- **What's unknown:** whether anyone still maintains it, and whether it builds against current CUDA and cuQuantum.
- **Example:** simulating a quantum circuit. Each gate becomes a small tensor, wires become shared indices, and contracting the network gives the probability of a particular output. The README lists "Quantum computing simulations" as a target. [KNOWN: README; INFERRED: the walkthrough]

## How it works
- **Two APIs:** the declarative API (`src/numerics`) is for describing objects. The executive API (`src/exatn/exatn_numerics.hpp`) does the actual computing. Tensors are stored column-major, so external data has to match. [KNOWN: README]
- **Runtime:** a tensor graph plus an execution state, a graph optimizer, and graph and node executors. The node executors are `talsh` (TAL-SH, a tensor algebra library) and `exatensor`, and there's a `cuquantum` path for NVIDIA's quantum-simulation library. [KNOWN: `src/runtime/` tree] It uses a plugin registry built on CppMicroServices, the same approach XACC uses. [KNOWN: `src/exatn/ServiceRegistry.*`, `tpls/cppmicroservices`, `manifest.json` files]
- **Extras:** a parser (ANTLR grammar), an RPC driver (`src/driver-rpc`), and Python bindings via pybind11. [KNOWN: tree, language stats]

## How the project is organized
- `src/` holds `exatn` (the top-level API and solvers), `numerics` (tensor, network, operator and expansion classes), `runtime`, `parser`, `driver-rpc`, `utils` and `scripts`. The other folders are `python/`, `tpls/` (ExaTensor, ANTLR, Boost, CppMicroServices, Eigen, GoogleTest, METIS and pybind11), `doc/`, `docker/` and `cmake/`. [KNOWN: repo tree]
- Languages: C++ about 94.8% by bytes, then CUDA, CMake, C, Python and ANTLR. [KNOWN: GitHub languages API]
- Build: CMake 3.9 or newer, GNU 8+ with C++14 and Fortran-2003. Optional: MPI (MPICH or OpenMPI families), BLAS (OpenBLAS, ATLAS, MKL and others), CUDA 11.2+, and cuTensor 1.6.2 / cuQuantum 22.11 or newer. [KNOWN: README Dependencies]
- CI: GitHub Actions `ci-linux.yml` plus a `.gitlab-ci.yml`. [KNOWN]
- History: 1,202 commits from 2018-11-01 to 2023-07-19, and 12 remote branches. Created 2018-10-03. 69 stars and 20 forks. [KNOWN: git log, GitHub API]
- Contributors: 12 including anonymous commit authors, but only 2 GitHub accounts. Most commit authors aren't linked to GitHub accounts. [KNOWN: GitHub API]

## Who uses it / why it matters
Tensor networks are one of the main ways classical supercomputers simulate quantum computers and hard physics problems. ExaTN was ORNL's attempt at a general, multi-GPU engine for them. [INFERRED] It's the back end behind TNQVM's tensor-network simulation for XACC. [KNOWN per map link 162] For usage evidence, see the usage section in `signals/exatn.md`.

## Related projects
- TNQVM (`tnqvm`, catalog row 69): can use ExaTN. [KNOWN per map]
- XACC (`xacc`): reaches ExaTN through TNQVM, and shares the plugin design. [KNOWN: tpls; INFERRED: the design overlap]
- QIR-EE (`qiree`): same GitHub org. [KNOWN]

## Known / Inferred / Unknown
- KNOWN: license, DOE CODE, dates, no releases, APIs, runtime pieces, dependencies, layout, counts.
- INFERRED: the tensor and contraction explanations, the circuit example, the org-unit meaning.
- UNKNOWN: maintenance, compatibility with current CUDA, any successor (none named).

## Sources (accessed 2026-10-24)
- https://github.com/ORNL-QCI/exatn (README.md, LICENSE, src/, tpls/, python/, .github/workflows/)
- https://api.github.com/repos/ORNL-QCI/exatn (plus /languages, /releases, /tags, /contributors)
- https://www.frontiersin.org/articles/10.3389/fams.2022.838601/full (linked, not reviewed in depth)
- https://www.osti.gov/doecode/biblio/45739 (per the discovery pass)

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Verified on a fresh clone of ORNL-QCI/exatn and public records: BSD 3-Clause "Copyright (c) 2017, UT-Battelle", last commit 2023-07-19, first 2018-11-01, 1,202 commits on `devel`, 12 remote branches, 0 tags, contributors 12 with anonymous and 2 accounts, `src/` and `tpls/` layouts, the runtime pieces including `executor/cuquantum`, both CI files, and README build requirements (CMake 3.9+, GNU 8+, C++14 and Fortran-2003, cuTensor 1.6.2/cuQuantum 22.11). DOE CODE code-45739 refetched from the OSTI API: "ExaTN", 2018-10-01, ORNL research org, contract AC05-00OR22725. Paper link resolves.
- No corrections. Note: the 12 contributor figure is GitHub's count by commit email; git log shows 11 distinct author names, so a couple of entries may be the same person under two emails. [INFERRED]
- Status unknown stands: not archived on GitHub, so rule 14 doesn't allow archived.
