# TASMANIAN
- Official page: https://ornl.github.io/TASMANIAN/ (documentation site, the repo's homepage field) [KNOWN: GitHub API, README]
- Repo: https://github.com/ORNL/TASMANIAN (default branch `master`)
- Docs: stable docs at https://ornl.github.io/TASMANIAN/stable/ and rolling docs at https://ornl.github.io/TASMANIAN/. There's also a separate PDF Math Manual, linked from the README, hosted on a developer's personal GitHub Pages site. [KNOWN: README]
- License: BSD 3-Clause, with copyright stated as "Copyright (c) 2017, Miroslav Stoyanov". The file adds a disclaimer that "UT-BATTELLE, LLC AND THE UNITED STATES GOVERNMENT MAKE NO REPRESENTATIONS" about the software. [KNOWN: https://github.com/ORNL/TASMANIAN/blob/master/LICENSE, lines 3 and 31] GitHub's API shows NOASSERTION, probably because of that extra paragraph. [KNOWN: API; INFERRED: the reason]
- Status: active [KNOWN: last commit 2026-10-19, release v8.2 on 2025-12-09 UTC, not archived, GitHub API]
- Scope (rule 13): ORNL is the repo owner (github.com/ORNL), and the LICENSE carries a UT-Battelle (ORNL's managing contractor) disclaimer. [KNOWN] The copyright line names an individual, not UT-Battelle. Why is [UNKNOWN]. A second source ties it to ORNL: the DOE CODE record (code-6305, OSTI 1231809, 2013) lists Oak Ridge National Laboratory as research org, so rule 13 is [CORROBORATED]. [KNOWN: https://www.osti.gov/biblio/1231809]

## Plain-language walkthrough
- **What it is:** a math toolkit whose name stands for "Toolkit for Adaptive Stochastic Modeling and Non-Intrusive ApproximatioN". It builds cheap stand-in models of expensive simulations, and it works out which input settings best explain observed data. [KNOWN: README]
- **The problem:** some simulations take hours per run and depend on many uncertain inputs (dozens of material constants, say). You can't run every combination. You need a smart, small set of runs that still captures how the output depends on the inputs. That field is called *uncertainty quantification* (UQ). [INFERRED: standard UQ motivation; the README describes "high dimensional integration and interpolation as well as parameter calibration"]
- **What goes in:** a function or simulation you can evaluate at chosen points, the number of inputs and their ranges, and, for calibration, measured data. [INFERRED: from the API description in the README]
- **What happens:** the Sparse Grids module picks a clever set of sample points (a *sparse grid*, which needs far fewer points than a full grid in many dimensions) and builds an approximation from the results, adding points where the function changes fast. The DREAM module then samples likely input values that match the data. [KNOWN: README]
- **What comes out:** a fast *surrogate model* (a cheap formula that mimics the slow simulation), integrals such as averages over uncertain inputs, and samples from the probability distribution of the inputs. [KNOWN: README describes integration, interpolation and sampling]
- **Where humans act:** a scientist chooses grid types and accuracy, runs the real simulation at the points Tasmanian asks for, and reads the results.
- **What it is not:** it doesn't simulate physics itself. It's "non-intrusive", meaning it treats your simulation as a black box and never changes its code. [KNOWN: the name; INFERRED: the black-box meaning]
- **What's unknown:** which ORNL group owns it, and which ORNL codes use it.
- **Example:** a model of a battery has 10 uncertain inputs and takes an hour per run. A full grid with 10 points per input would need 10 billion runs. A sparse grid might need a few thousand, giving a surrogate that answers in microseconds. DREAM then uses that surrogate to find which input values fit lab measurements. [INFERRED: an illustrative example; the numbers are arithmetic, not from a source]

## How it works
- **Five grid families:** Global (smooth polynomials over the whole range), Sequence (like Global with optimized data structures), Local polynomial (piecewise, for sharp local changes), Wavelet (local functions with better error estimates) and Fourier (for periodic, repeating functions). [KNOWN: README]
- **DREAM:** "DiffeRential Evolution Adaptive Metropolis", a variant of Markov Chain Monte Carlo (MCMC). MCMC is a way to draw samples from a probability distribution by taking a guided random walk. DREAM runs many walks ("chains") at once, which parallelizes well and handles distributions with several peaks. [KNOWN: README]
- **Bayesian inference:** DREAM's main use is updating beliefs about inputs given data, and it can use a sparse-grid surrogate in place of the slow model. [KNOWN: README]
- **GPU acceleration:** optional CUDA (NVIDIA), HIP (AMD), DPC++ (Intel) and MAGMA backends, all marked "(stable)" in the build options. [KNOWN: CMakeLists.txt lines 80 to 83; kernel files in `SparseGrids/`]
- **MPI add-ons:** `Addons/` has MPI helpers for building grids and running DREAM across many computers. [KNOWN: file names such as `tsgMPIConstructGrid.hpp`, `tsgMPISampleDream.hpp`]

## How the project is organized
- `SparseGrids/` (the core grids, plus CUDA, HIP and DPC++ kernels), `DREAM/` (the sampler and optimization), `Addons/` (MPI helpers, surrogate construction), `InterfaceTPL/` (wrappers for BLAS, a standard linear-algebra library, and for GPU libraries), `InterfacePython/`, `InterfaceMATLAB/`, `InterfaceSwig/` (generated bindings, used for Fortran), `Tasgrid/` (a command-line tool), `Testing/`, `Doxygen/`, `docker/`, `Config/`. [KNOWN: repo tree; INFERRED: the SWIG-for-Fortran role, from the Fortran byte count and the removed F90 module in CHANGELOG 8.2]
- Languages: C++ (about 69% by bytes), Python, Fortran, MATLAB and CMake, with a little CUDA. [KNOWN: GitHub languages API]
- Build: CMake on Linux, macOS and Windows, or plain GNU Make on Linux and macOS. It's also on PyPI as `Tasmanian`. [KNOWN: README] CI builds on Ubuntu, macOS and Windows. [KNOWN: `.github/workflows/`]
- Contributors: 12 including anonymous commit authors, 8 GitHub accounts without them. Created 2017-10-16. [KNOWN: GitHub API]
- Release cadence: about one a year, recently v7.9 (2022-10-26), v8.0 (2023-10-11), v8.1 (2024-10-21) and v8.2 (2025-12-09). The CHANGELOG already lists 8.3, which requires C++17. [KNOWN: GitHub API, CHANGELOG]

## Who uses it / why it matters
UQ underpins any claim that "the simulation says X, plus or minus Y". [INFERRED] Named users beyond its own papers are [UNKNOWN]; the README asks users to cite the Manual and related papers. The sampling ideas behind DREAM (MCMC) also show up in security, for example in probabilistic attack-graph analysis. [INFERRED: a general connection; not about Tasmanian specifically]

## Related projects
- IRIS (`iris`) and HeCBench (`hecbench`): other ORNL HPC libraries with CUDA and HIP backends. The connections pass found no source tying IRIS to Tasmanian. [KNOWN per map, map pass on IRIS]
- MAGMA: an outside GPU linear-algebra library from the University of Tennessee ("UTK Magma" in the build options). [KNOWN: CMakeLists.txt line 83]

## Known / Inferred / Unknown
- KNOWN: license text and its UT-Battelle disclaimer, purpose, grid types, DREAM, GPU and MPI options, layout, CI, releases.
- INFERRED: why GitHub shows NOASSERTION, the example numbers, the SWIG/Fortran role.
- UNKNOWN: owning group, why the copyright names an individual, users.

## Sources (accessed 2026-10-24)
- https://github.com/ORNL/TASMANIAN (README.md, LICENSE, CHANGELOG.md, CMakeLists.txt, SparseGrids/, DREAM/, Addons/, InterfaceTPL/, .github/workflows/)
- https://ornl.github.io/TASMANIAN/
- https://api.github.com/repos/ORNL/TASMANIAN (plus /languages, /releases, /contributors)

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Rechecked: the LICENSE (line 3 copyright to an individual, lines 30-31 UT-Battelle disclaimer), NOASSERTION, created 2017-10-16, last push 2026-10-19, 12 releases with v8.2 on 2025-12-09 and yearly cadence since 2021, contributors 12 with anonymous / 8 accounts, languages (C++ 69%, Python 14%, Fortran, MATLAB), the README name expansion and "high dimensional integration and interpolation" quote, DREAM section, and the CUDA, HIP, DPC++ and MAGMA options marked "(stable)" in CMakeLists.txt. All verified.
- Added: DOE CODE code-6305 / OSTI 1231809 lists ORNL as research org, so rule 13 is now CORROBORATED rather than resting on the GitHub org alone. Why the copyright names an individual is still UNKNOWN.
