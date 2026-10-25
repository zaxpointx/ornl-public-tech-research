# Xolotl
- Official page: none separate. The README and the GitHub wiki serve as the docs. [KNOWN: README; repo homepage field is empty, GitHub API]
- Repo: https://github.com/ORNL-Fusion/xolotl (default branch `stable`)
- Docs: wiki pages linked from the README, covering build configuration, running the code, the parameter file, PETSc options, benchmark problems and publications. [KNOWN: README links to https://github.com/ORNL-Fusion/xolotl/wiki]
- License: BSD-3-Clause, per the LICENSE file's first line. GitHub's API shows NOASSERTION. [KNOWN: https://github.com/ORNL-Fusion/xolotl/blob/stable/LICENSE]
- Copyright: shared among six institutions. The list starts with "Copyright 2012-2024 UT-Battelle, LLC" and also names the University of Tennessee and its research foundation, UChicago Argonne, University of Florida, Penn State and University of Michigan. [KNOWN: LICENSE lines 3 to 8]
- Status: active. The latest release is v3.4.0 (2026-09-03 UTC), the last push was 2026-10-21 UTC, and the repo isn't archived. [KNOWN: GitHub API]
- Scope (rule 13): UT-Battelle (ORNL's managing contractor) is a named copyright holder. [KNOWN: LICENSE] The GitHub org is "ORNL-Fusion". There's no OSTI software record (Scout's search came back empty), but OSTI 1513390, a 2018 journal article with ORNL as research org and ASCR as sponsor, calls it "Our cluster dynamics model, Xolotl". [KNOWN: https://www.osti.gov/biblio/1513390] Rule 13 is [CORROBORATED] by the copyright plus that record.

## Plain-language walkthrough
- **What it is:** a supercomputer simulation code that predicts how the inside of a metal wall changes over time when it's bombarded by particles. The README calls it "a continuum simulator under development within two DOE SciDAC programs". SciDAC is DOE's Scientific Discovery through Advanced Computing program. [KNOWN: README]
- **The problem:** in a fusion reactor like ITER, the *divertor* (the part of the wall that takes the hottest plasma exhaust) gets hit by helium and hydrogen. Those atoms burrow in and clump into bubbles that can crack or fuzz the surface. Fuel in fission reactors suffers similar damage from gas made inside it. Engineers need to know how fast that happens. [KNOWN: README names ITER divertors and fission fuel; INFERRED: the bubble and fuzz mechanism, from standard fusion-materials background]
- **What goes in:** a parameter file describing the material, temperature, the incoming particle flux, the grid and the time span, plus solver options. [KNOWN: README, wiki "Parameter File" and "PETSc Options" pages linked]
- **What happens:** the code tracks how many clusters of each size and type (for example, helium clumps of various sizes) sit at each depth in the material. Every time step, it computes how clusters drift (*advection*), spread out (*diffusion*) and merge or split (*reaction*). This is "advection-reaction-diffusion kinetic rate theory". [KNOWN: README; INFERRED: the cluster-counting explanation, from the network/cluster code structure]
- **What comes out:** HDF5 files (a standard scientific data format) holding concentrations over depth and time, which Python scripts in `analysis/` turn into plots such as retention and depth profiles. [KNOWN: HDF5 is a required dependency; `analysis/` has `psiRetention.py`, `psiDepthProfile.py` and an `HDF5utils` folder; INFERRED: that the outputs are HDF5]
- **Where humans act:** a researcher writes the parameter file, picks a benchmark or a new case, runs it on a cluster, and interprets the plots against experiments.
- **What it is not:** it's not a plasma simulator and doesn't model atoms one by one. It works with averaged concentrations (a "continuum" model). [KNOWN: "continuum" in the README; INFERRED: the contrast]
- **What's unknown:** which ORNL division leads it, and how its results are validated.
- **Example:** you set a tungsten wall at 1,000 K under a steady helium flux. Xolotl reports how much helium is trapped, and at what depths, after a set time. [INFERRED: an illustrative case; tungsten surface handlers like `W100MaterialHandler` exist in the code]

## How it works
- **Solver:** PETSc, a widely used library for solving huge systems of equations in parallel, does the time stepping. Kokkos, a library that lets one C++ code run on CPUs or GPUs, handles the hardware. The CUDA (NVIDIA GPU) or OpenMP (multicore CPU) backend is chosen at build time. [KNOWN: README dependencies; `CMake/BuildPETSc.cmake` lines 66 and 67]
- **Reaction networks:** each material system has its own network of cluster types and reactions. The code has PSI, Fe, Zr, Li, NE and Alloy networks. [KNOWN: `xolotl/core/include/xolotl/core/network/`] PSI most likely means plasma-surface interaction (the tungsten-wall case), Fe means iron, Zr means zirconium (fuel cladding), Li means lithium and NE means nuclear fuel. [INFERRED: from names plus the `W1xx`, `Fuel`, `AlphaZr` and `Fe` material handlers; NE's meaning is a guess]
- **Physics modules:** `core/src/` has separate folders for advection, diffusion, flux (incoming particles), material, temperature and modified reactions. [KNOWN: repo tree]
- **Uncertainty quantification:** `UQ/` has Bayesian inference scripts that use UQTk (a Sandia UQ toolkit) to fit model parameters to data. [KNOWN: `UQ/uqtkScripts/bayesianInference1D.py`; INFERRED: UQTk's origin, from the folder name]

## How the project is organized
- `xolotl/` is the main code, split into `core/` (physics and networks), `solver/`, `io/`, `options/`, `factory/`, `interface/`, `perf/`, `viz/` and `util/`. Other top-level folders: `xconv/` (a small converter tool), `test/`, `benchmarks/`, `tutorial/`, `analysis/` (Python plotting), `UQ/`, `CI/` (Docker image for Ubuntu 22) and `scripts/`. [KNOWN: repo tree]
- Languages: about 67% of bytes are Jupyter notebooks and about 30% are C++. The notebooks inflate the count, and the simulator itself is C++20. [KNOWN: GitHub languages API, README "C++20 compiler"; INFERRED: that notebooks are analysis or tutorial material]
- Build: CMake 3.13 or newer. It can build PETSc and its other dependencies for you with `-DXolotl_BUILD_PETSC=ON`. [KNOWN: README]
- CI: GitHub Actions with gcc and clang builds on Ubuntu, plus a macOS job. [KNOWN: `.github/workflows/ci-github-actions.yaml`]
- Contributors: 27 including anonymous commit authors, 9 GitHub accounts without them. The repo was created 2018-02-05, and the LICENSE dates go back to 2012, so earlier history likely lived elsewhere. [KNOWN: GitHub API; INFERRED: the earlier home; the README's SourceForge mailing list hints at it]
- Releases: 14 GitHub releases, from v2.0.0 (2021-09-22) to v3.4.0 (2026-09-03), about two a year lately. [KNOWN: GitHub API]

## Who uses it / why it matters
Fusion power depends on walls that survive years of bombardment, and testing that in real reactors is slow and costly. A simulator like this lets researchers screen materials and conditions first. [INFERRED] The wiki keeps a publications list. [KNOWN: README] The six-institution copyright shows multi-lab and university collaboration. [KNOWN: LICENSE]

## Related projects
- Kokkos and PETSc: outside libraries it depends on. Scout has Cabana/Kokkos queued. [KNOWN: README; Scout batch-07 notes]
- TASMANIAN (`tasmanian`): another UQ-flavored ORNL code, but I saw no direct tie. Xolotl's UQ scripts use UQTk, not Tasmanian. [INFERRED: from the `UQ/` folder]

## Known / Inferred / Unknown
- KNOWN: purpose, license, copyright holders, dependencies, layout, networks, CI, releases, counts.
- INFERRED: what each network abbreviation means, output format, the example, earlier history.
- UNKNOWN: OSTI software record, owning ORNL division, validation details.

## Sources (accessed 2026-10-24)
- https://github.com/ORNL-Fusion/xolotl (README.md, LICENSE, CMakeLists.txt, CMake/BuildPETSc.cmake, xolotl/core/, UQ/, analysis/, .github/workflows/)
- https://github.com/ORNL-Fusion/xolotl/wiki (linked from the README; not separately reviewed)
- https://api.github.com/repositories/120320792 (plus /languages, /releases, /contributors)

## Sweep 2 notes (ORNL Fact Checker, 2026-10-24)
- Rechecked against the GitHub API and raw files: the BSD-3 LICENSE with 6 copyright holders (UT-Battelle first), NOASSERTION, created 2018-02-05, last push 2026-10-21, 14 releases from v2.0.0 (2021-09-22) to v3.4.0 (2026-09-03), contributors 27 with anonymous / 9 accounts, languages Jupyter 66.9% and C++ 30.1%, the README quotes ("continuum simulator under development within two DOE SciDAC", ITER, fission fuel), C++20 (CMakeLists line 13), Kokkos >= 4.6 and PETSc in the README requirements. All verified.
- Corrected: ORNL as research org is no longer UNKNOWN. OSTI 1513390 (ORNL, ASCR) names Xolotl as "our cluster dynamics model", so rule 13 is CORROBORATED.
- Note: Kokkos comes in through PETSc and plsm per the README, not a direct find_package in the top CMakeLists. The brief's wording ("handles the hardware") stays INFERRED-safe.
