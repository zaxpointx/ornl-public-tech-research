# ReSolve (Re::Solve)
- Official docs: https://resolve.readthedocs.io/en/latest/ (linked from the README). [KNOWN: README]
- Repo: https://github.com/ORNL/ReSolve (default branch `develop`). GitHub's description is "Library of GPU-resident linear solvers". [KNOWN: GitHub API]
- License: a custom permissive UT-Battelle LLC and Battelle Memorial Institute license, "Copyright (c) 2023, UT-Battelle, LLC and Battelle Memorial Institute." It requires an acknowledgment naming both DOE contracts. [KNOWN: LICENSE lines 1-34]
  - The README badge and the DOE CODE record both call it BSD 3-clause, and the README says "BSD-style". The GitHub API says NOASSERTION. Recorded as stated: the LICENSE text is BSD-like but is not the standard BSD-3 wording. [KNOWN: README, DOE CODE, GitHub API; INFERRED: the comparison]
- Status: active (rule 14). Release v0.99.4 came out 2026-09-25, the last commit on `develop` was 2026-10-06 15:41 ET, and the last push was 2026-10-18 20:16 UTC (4:16 PM ET). Not archived. [KNOWN: GitHub API, git log]
- Scope (rule 13): CORROBORATED. DOE CODE code-114681 (released 2023-10-16, DOI 10.11578/dc.20231013.1) lists "Research Org.: Oak Ridge National Laboratory (ORNL), Oak Ridge, TN" and developer affiliations of PNNL and ORNL. The repo sits in the ORNL GitHub org. [KNOWN: https://www.osti.gov/doecode/biblio/114681, accessed 2026-10-24]
  - Org unit: not stated on any page I read. [UNKNOWN]

## Plain-language walkthrough
- **What it is:** a C++ library of *linear solvers* that keep their work on the GPU. It runs on NVIDIA GPUs (CUDA), AMD GPUs (HIP/ROCm), or plain CPUs. [KNOWN: README]
- **Key terms:**
  - A *linear system* is a big set of equations written as A·x = b. A is a matrix of known numbers, b is a known vector, and you're solving for x.
  - *Sparse* means most entries of A are zero, so only the nonzeros are stored.
  - A *direct* solver factors A into simpler pieces (LU factorization, which splits A into a lower- and an upper-triangular matrix) and solves exactly.
  - An *iterative* solver (here FGMRES) starts with a guess and improves it step by step.
  - *Refactorization* means reusing the factoring pattern when only the numbers in A change, not where the nonzeros sit. That's much cheaper than starting over. [INFERRED: standard definitions; KNOWN: solver names from `resolve/` file names]
- **The problem:** power-grid optimization and simulation codes solve thousands of nearly identical sparse systems in a row. If each solve copies data between CPU and GPU, the copying becomes the bottleneck. ReSolve keeps the matrices on the GPU and reuses factorizations across solves. [KNOWN: README says the examples "emulate nonlinear solver calling the linear solver repeatedly"; INFERRED: the bottleneck explanation]
- **What goes in:** a sparse matrix (in COO, CSR or CSC storage formats) and a right-hand-side vector, from a calling program, or from test matrix files for the examples. The README points to power-grid test matrices (ACTIVSg10k) in a public NREL repo. [KNOWN: `resolve/matrix/`, README]
- **What happens:**
  1. A first factorization runs on the CPU with KLU from SuiteSparse.
  2. Later solves refactor on the GPU with cuSOLVER, cuDSS or rocSOLVER.
  3. Optionally, FGMRES (plain or with randomized sketching) cleans up the answer. [KNOWN: `examples/kluRefactor.cpp`, `gpuRefactor.cpp`, `LinSolverDirect*`, `LinSolverIterative*RandFGMRES*`; INFERRED: the typical order]
- **What comes out:** the solution vector x, plus residual and error information for checking accuracy. [INFERRED from examples]
- **Where humans act:** a developer of a bigger simulation or optimizer links ReSolve through CMake (`find_package(ReSolve)`) and chooses the solver combination and GPU back end at build time. [KNOWN: README "To use the Re::Solve library in your own project"]
- **What it is not:** it isn't a grid simulator or an optimizer itself. It's the math engine that tools like GridKit can plug in. It also isn't at a 1.0 release yet: the tags are v0.99.x. [KNOWN: tags, GridKit CMake; INFERRED]
- **What's unknown:** who uses it in production-style runs. That's for the usage section in signals.
- **Example:** an optimal power flow run on a 10,000-bus test grid solves similar systems over and over as the optimizer adjusts generator settings. ReSolve factors the first one, then refactors the rest on the GPU. [KNOWN: README test matrices; INFERRED: the walkthrough]

## How it works
- **Solver classes:** `LinSolverDirect*` holds the direct solvers (KLU, LUSOL, cuSOLVER GLU/Rf, cuDSS, rocSOLVER Rf, plus CPU, cuSPARSE and rocSPARSE ILU0 preconditioners). `LinSolverIterative*` holds FGMRES and randomized FGMRES. `SystemSolver` wraps a chosen combination behind one interface. [KNOWN: `resolve/` tree]
- **Hardware back ends:** `resolve/cpu`, `resolve/cuda` and `resolve/hip` each have memory helpers and kernels, so the same code runs on each device type. [KNOWN: tree]
- **HyKKT:** a sub-package for the special block systems (KKT systems) that come out of optimization problems like optimal power flow. Its own README says it is "currently experimental, but is actively in development" and not fully integrated. [KNOWN: `resolve/hykkt/README.md`]

## How the project is organized
- Top level: `resolve/` (the library: matrix, vector, random, workspace, utilities, lusol, hykkt, and the device folders), `examples/` (including `experimental/`), `tests/` (unit and functionality), `docs/` (Sphinx and Doxygen), `buildsystem/`, `cmake/` and `scripts/`. [KNOWN: repo tree]
- Languages: C++ about 72.3% by bytes, Fortran 14.2% (the bundled LUSOL), CMake 3.9%, HIP 3.1%, CUDA 2.8%, and small amounts of Shell and Python. [KNOWN: GitHub languages API; INFERRED: that the Fortran is LUSOL]
- Build: CMake 3.22 or newer. Optional: SuiteSparse 5.0+ (KLU, AMD, COLAMD), CUDA 11.4+, and HIP/ROCm 6.4+. It has CMake presets, including a "cluster" preset. [KNOWN: README]
- CI: GitHub Actions for documentation, pre-commit, and a Spack CPU build. Workflows named "ORNL Ascent Mirror", "ORNL Crusher Mirror" and a PNNL mirror push to non-public pipelines, which are out of scope (rule 16). [KNOWN: `.github/workflows/` file names]
- Releases: v0.99.1 (2023-12-20), v0.99.2 (2025-11-05), v0.99.3 (2026-08-19) and v0.99.4 (2026-09-25). The CHANGELOG also has unreleased notes after 0.99.4 and a HyKKT section. [KNOWN: GitHub API, CHANGELOG]
- History: 283 commits on `develop`. The first commit is 2023-05-02 UTC, and by year there are 142 in 2023, 29 in 2024, 66 in 2025 and 46 in 2026 so far. The repo was created 2023-07-19. It has 85 stars and 14 forks. [KNOWN: git log, GitHub API]
- Contributors: 19 including anonymous commit authors, 15 GitHub accounts. [KNOWN: GitHub API]
- Funding: the README credits the Exascale Computing Project (ECP). DOE CODE lists USDOE as sponsor, under contract AC05-00OR22725. [KNOWN: README, DOE CODE]

## Who uses it / why it matters
GPU supercomputers like Frontier are fast at math but slow at moving data back and forth. Sparse solvers that stay on the GPU are one of the hard missing pieces for grid and optimization codes. [INFERRED] GridKit has an off-by-default `GridKit_ENABLE_RESOLVE` build option. [KNOWN: GridKit CMakeLists.txt line 37] For real-world usage evidence, see the usage section of `signals/resolve.md` once it exists.

## Related projects
- GridKit (`gridkit`): optional ReSolve support. [KNOWN: GridKit CMakeLists.txt]
- ExaGO (`exago`): same grid-optimization area. No ReSolve reference turned up in its top-level CMake. [INFERRED: possible link, not shown]
- PNNL co-development: the license and the DOE CODE affiliations show PNNL as a co-developer. [KNOWN]

## Known / Inferred / Unknown
- KNOWN: license text and its disagreement with the badges, DOE CODE record, releases, dates, solver list, build needs, layout, counts, ECP credit, GridKit option.
- INFERRED: the solver explanations, the bottleneck story, the OPF example, the Fortran-is-LUSOL point.
- UNKNOWN: org unit, real-world users beyond GridKit's optional hook, timing of a 1.0 release.

## Sources (accessed 2026-10-24)
- https://github.com/ORNL/ReSolve (README.md, LICENSE, CHANGELOG.md, resolve/, resolve/hykkt/README.md, examples/, .github/workflows/)
- https://api.github.com/repos/ORNL/ReSolve (plus /languages, /releases, /tags, /contributors with and without anon=1)
- https://www.osti.gov/doecode/biblio/114681 ("Research Org.: Oak Ridge National Laboratory (ORNL), Oak Ridge, TN (United States)")
- https://resolve.readthedocs.io/en/latest/ (linked from the README, not read in depth)
- https://github.com/ORNL/GridKit (CMakeLists.txt line 37)

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Verified on a fresh clone of ORNL/ReSolve and public records: LICENSE copyright line, README BSD-3 badge and "BSD-style" wording, CMake 3.22, SuiteSparse 5.0+ and ROCm 6.4+, ECP acknowledgment, HyKKT "experimental" wording, tags v0.99.1 to v0.99.4, last `develop` commit 2026-10-06 15:41 ET, 283 commits (142/29/66/46 for 2023-2026), first commit 2023-05-02, the six workflow files, contributors 19 with anonymous and 15 accounts. DOE CODE code-114681 refetched from the OSTI API: "ReSolve", 2023-10-16, DOI 10.11578/dc.20231013.1, ORNL research org, USDOE sponsor, contract AC05-00OR22725. Docs link resolves.
- No corrections. The mirror workflows were checked by file name only, per rule 16.

## GOAL.md questions (added 2026-10-24)
- **Who pays (Q3):** the README credits the Exascale Computing Project, and DOE CODE lists USDOE. [KNOWN, above]
- **Where in the tree (Q2):** ORNL, then the power grid and math libraries, as a solver used by grid tools (an optional GridKit hookup). [KNOWN, above]
- **What it teaches about ORNL (Q8):** it's a two-lab project (ORNL and PNNL) with CI wired to each lab's own machines. That shows how code is tested on hardware outsiders can't see, and we only note that those pipelines exist. [KNOWN: workflows; INFERRED]
- **Student angle (Q9):** it has a CONTRIBUTING.md. [KNOWN: tree] You'd need C++, linear algebra, and some GPU (CUDA or HIP) basics. [INFERRED]
- **Searched without result (Q10):** any ExaGO reference to ReSolve (logged in not-found).
