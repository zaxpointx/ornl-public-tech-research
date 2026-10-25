# MatRIS
- Official page: none found. The README is the documentation, and `docs/doxygen.cfg` configures API docs that are built locally. [KNOWN: repo tree]
- Repo: https://github.com/ORNL/MatRIS (default branch `main`). Its GitHub description is "MatRIS: A heterogenous Math library using IRIS run-time". [KNOWN: GitHub API]
- License: BSD 3-Clause, "Copyright (c) 2025, UT-Battelle, LLC". The GitHub API also says BSD-3-Clause. [KNOWN: LICENSE lines 1-3, GitHub API]
- Status: unknown (borderline, rule 14).
  - The last commit and push were 2025-10-23, exactly 12 months before access.
  - There are no GitHub releases or tags, but CHANGELOG states version "[1.0.0] - 2025-07-21". That is a stated version, not a tagged release. [KNOWN: git log, GitHub API, CHANGELOG.md]
  - I chose unknown over active because there has been no activity for a year, per rule 10. Status unknown was confirmed by editorial decision on 2026-10-24.
- Maturity: the README describes its GEMM demo as a "proof of concept", and the brief keeps that wording (rule 10). [KNOWN: README]
- Scope (rule 13): passes. ORNL owns the repo and UT-Battelle holds the copyright. OSTI 2441045 and 2439841 list ORNL as research org. [KNOWN: repo; OSTI check in the discovery pass] That's the repo plus OSTI, so I'm marking it CORROBORATED pending the fact-check pass.

## Plain-language walkthrough
- **What it is:** a C/C++ math library that does the standard heavy matrix operations scientific and AI codes depend on. It picks at run time whether each piece runs on a CPU, an NVIDIA GPU, an AMD GPU or other chips, using ORNL's IRIS runtime to schedule the work. [KNOWN: README]
- **Key terms:**
  - *BLAS* (Basic Linear Algebra Subprograms) and *LAPACK* (Linear Algebra PACKage) are decades-old standard sets of matrix routines. For example, GEMM is matrix multiply and GETRF is LU factorization, a step in solving systems of equations.
  - *Heterogeneous* means a machine with several kinds of processors.
  - A *runtime* is software that decides where and when tasks run while the program is running. [INFERRED: general definitions; KNOWN: the routine names from README and CHANGELOG]
- **The problem:** every chip vendor ships its own tuned BLAS (cuBLAS for NVIDIA, hipBLAS for AMD, plus OpenBLAS, CLBlast and others). Apps usually hard-code one at build time, so they can't move work to whatever processor is free. MatRIS sits in front of all of them and chooses per task while running. [KNOWN: README's problem statement, paraphrased]
- **What goes in:** an application's matrix call through MatRIS's API, such as `matris_core_dgemm(...)`, after `init_matris_blas` and an optional `set_matris_blas_target`. The vendor libraries must be installed and found through environment variables. [KNOWN: README API list and setup steps]
- **What happens:**
  1. MatRIS splits big matrices into tiles (`flat2tile`/`tile2flat` utilities).
  2. It turns the operation into a graph of tile tasks.
  3. A scheduling policy hands the tasks to IRIS, which places them on devices and calls the matching vendor kernel. [KNOWN: README tree, `src/policies/`, `src/algorithms/lapack/*_tiling.h`; INFERRED: the step order]
- **What comes out:** the result matrix, plus timing and performance metrics in the paper-style experiments. [KNOWN: README]
- **Where humans act:** a developer builds the vendor libraries, sets environment paths, picks targets or policies, and runs experiments. [KNOWN: README setup sections]
- **What it is not:** it isn't a new BLAS implementation of its own, and it isn't a Python library. [INFERRED: it wraps vendor kernels; the Python and notebooks are analysis tools]
- **What's unknown:** whether anyone outside the research group uses it, and why 1.0.0 has no git tag.
- **Example:** the README's demo runs one DGEMM or SGEMM (double- or single-precision matrix multiply) and lets the runtime send it to OpenBLAS, cuBLAS, CLBlast, Xilinx BLAS (an FPGA chip library) or hipBLAS. [KNOWN: README]

## How it works
- **Operations:** CHANGELOG 1.0.0 lists GEMM, TRSM (triangular solve), GETRF, POTRF (Cholesky factorization), GESV and POSV (solvers built on those). The tests also cover SYRK and eigenvalue cases. [KNOWN: CHANGELOG, `tests/`]
- **Policies:** `PolicyBlockCycle.cpp`, `PolicyLAVA.cpp` and `policy_gemm.cpp` decide how tiles map to devices. "Block cyclic" is the classic round-robin tile layout. LAVA is undefined in the repo. [KNOWN: files; UNKNOWN: what LAVA stands for]
- **Kernels:** `src/kernels/blas` has backends for cuBLAS, hipBLAS, clBlast and openBLAS. There are also host-to-CUDA, HIP and OpenCL bridges, an OpenMP path, and a `dsp/fft` folder. [KNOWN: tree]
- **Comparisons:** container recipes cover other task runtimes (StarPU, PaRSEC, QUARK, OmpSs-2, Chameleon, MAGMA), which suggests benchmarking against them. [KNOWN: `containers/*.def` names; INFERRED: the purpose]

## How the project is organized
- `src/` contains `algorithms` (blas, lapack, math), `kernels`, `policies` and `utils`. The other folders are `tests/` (about 30 C and C++ drivers), `containers/` (Apptainer definitions plus CUDA 12.5/12.6 and ROCm install scripts), `utils/` (with `deffe` notebooks and scripts), `docs/` and `irishxg.idl`. [KNOWN: repo tree] The README's directory diagram is older than the current tree; for example, it doesn't show `policies/`. [KNOWN: README vs tree]
- Languages: Jupyter Notebook about 82.7% by bytes, then C 8.0%, C++ 7.5%, Python, CMake and a little CUDA. [KNOWN: GitHub languages API] The notebook share comes from performance-exploration notebooks in `utils/deffe`, so the library itself is C and C++. [INFERRED]
- Build: CMake, which links `iris` from `$IRIS/lib`, with options such as `IRIS_ASYNC_STREAMING`. Also included are a `run.sh` and a `Makefile.apptainer`. [KNOWN: CMakeLists.txt, src/CMakeLists.txt] I found no CI workflows. [KNOWN: no `.github/workflows`]
- History: 565 commits starting 2022-03-01, before the repo was created on 2023-11-08, so the history was likely imported. [KNOWN: git log, GitHub API; INFERRED: imported]
- Contributors: 8 including anonymous commit authors, 5 GitHub accounts without them. 1 star and 0 forks. [KNOWN: GitHub API]

## Who uses it / why it matters
It's a research testbed showing that IRIS can pick vendor math libraries per task at run time, which matters as lab machines mix GPU vendors. [INFERRED] For usage evidence, see the usage section in `signals/matris.md`.

## Related projects
- IRIS (`iris`): a required runtime dependency. [KNOWN: CMake, README]
- HeCBench: no link found.
- The unrelated namesake HPC-AI-Team/MatRIS stays [UNRELATED] (per the catalog row).

## Known / Inferred / Unknown
- KNOWN: license, owner, CHANGELOG 1.0.0, operations, backends, layout, no tags or CI, counts.
- INFERRED: tiling flow, the purpose of the benchmark containers, imported history.
- UNKNOWN: what LAVA means, outside use, why there's no tag.

## Sources (accessed 2026-10-24)
- https://github.com/ORNL/MatRIS (README.md, LICENSE, CHANGELOG.md, CMakeLists.txt, src/, tests/, containers/, utils/)
- https://api.github.com/repos/ORNL/MatRIS (plus /languages, /tags, /contributors)
- https://www.osti.gov/biblio/2441045 and https://www.osti.gov/biblio/2439841 (per the catalog row)

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Verified on a full fresh clone of ORNL/MatRIS and refetches: LICENSE "Copyright (c) 2025, UT-Battelle, LLC", BSD-3 in the API, last commit 2025-10-23 (11:17 ET), 0 tags and 0 releases, CHANGELOG "[1.0.0] - 2025-07-21", README "proof of concept", and contributors 8 with anonymous and 5 accounts. The brief's 5 is right; an earlier report said 2.
- IRIS dependency verified: `src/CMakeLists.txt` lines 7-10 put `$ENV{IRIS}/lib` on the link path with `iris` as a link library, linked at line 27.
- Rule 13 CORROBORATED: OSTI 2441045 and 2439841 are both ORNL-research-org conference records titled "MatRIS: ...". Together with the UT-Battelle LICENSE and the ORNL repo owner, that's two independent sources.
- Status is left as unknown pending an editorial decision; the facts above don't settle it. No corrections.
