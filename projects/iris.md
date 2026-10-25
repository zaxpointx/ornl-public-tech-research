# IRIS
- Official page: https://iris-programming.github.io [KNOWN: README]
- Repo: https://github.com/ORNL/iris
- Docs: Sphinx and Doxygen sources in `docs/` (published on the official page) [KNOWN: repo tree; INFERRED: that the site is built from these]
- License: BSD 3-Clause. Quote: "Copyright (c) 2021, UT-Battelle, LLC" [KNOWN: https://github.com/ORNL/iris/blob/main/LICENSE, line 3; GitHub API spdx BSD-3-Clause]. UT-Battelle is the contractor that manages ORNL for DOE.
- Status: active [KNOWN: release v3.0.1 on 2026-02-10 UTC, not archived, GitHub API]
- Scope (rule 13): ORNL is the repo owner (github.com/ORNL) and UT-Battelle holds the copyright. [KNOWN]

## Plain-language walkthrough
- **What it is:** a *runtime system*, a layer of software that sits under an application while it runs and decides where each piece of work goes. The README calls it "an intelligent runtime system for extremely heterogeneous architectures". [KNOWN: README]
- **The problem:** modern supercomputers mix CPUs, NVIDIA GPUs, AMD GPUs, Intel GPUs, FPGAs (reprogrammable chips) and phone-style DSPs. Each speaks its own programming system, such as CUDA for NVIDIA, HIP for AMD, Level Zero for Intel and OpenCL or OpenMP for many. Writing one program that uses all of them at once is hard. [KNOWN: README lists OpenMP, CUDA, HIP, Level Zero, OpenCL, Hexagon]
- **What goes in:** an application broken into *tasks* (units of work, such as "multiply these two matrices") with their data, plus device-specific *kernels* (the small functions that actually run on a chip). [KNOWN: tests such as `02_task_depend`, apps such as `saxpy`, `dgemm`]
- **What happens:** IRIS discovers which devices exist, tracks which tasks depend on which data, moves data between devices ahead of time, and uses a *scheduling policy* to pick a device for each task. [KNOWN: README]
- **What comes out:** the same results the application would compute, run across whatever hardware is present.
- **Where humans act:** developers split code into tasks, write or reuse kernels, and can pick or write a scheduling policy. [KNOWN: `apps/custom_policy`, `scheduling-policies/`]
- **What it is not:** it's not a compiler and not a job scheduler like Slurm that hands out whole machines to users. It works inside one application. [INFERRED: from the runtime design in `src/runtime/`]
- **What's unknown:** which ORNL group owns it (not stated in what I read) and which production codes use it.
- **Example:** `apps/vecadd` adds two vectors. With IRIS, the same task could run on a CUDA GPU on one machine and a HIP GPU on another, without rewriting the program around each vendor. [KNOWN: app exists; INFERRED: the portability point from the README's purpose]

## How it works
- **Device backends:** `src/runtime/` has one class per device type: `DeviceCUDA`, `DeviceHIP`, `DeviceLevelZero`, `DeviceOpenCL`, `DeviceOpenMP`, `DeviceHexagon` and `DeviceQIREE`. A *backend* is the code that talks to one kind of hardware. [KNOWN: file names]
- **Task graphs:** tasks and their data dependencies form a graph, and v3.0.0 added automatic dependency detection from data flow. [KNOWN: CHANGELOG 3.0.0 "Automatic dependency identification based on data flow analysis"]
- **Async streams:** v3.0.0 overlaps computation with data transfers using each device's multiple streams (queues of work a GPU can run at once). [KNOWN: CHANGELOG 3.0.0]
- **Policies:** `scheduling-policies/` includes `aiwc` and graph-prediction policies, including a GNN one. A GNN (graph neural network) is an AI model that works on graphs. [KNOWN: folder names; INFERRED: that these predict good device choices from the task graph]
- **Language support:** C and C++ core, a Fortran API, a Python package, initial Julia support (added in 3.0.0), plus some Rust. [KNOWN: `FortranAPI.f90`, `pyproject.toml`, `Project.toml`, CHANGELOG, languages API]
- **Quantum hook:** `DeviceQIREE` treats QIR-EE (a quantum program runner, see `qiree`) as one more device, and `apps/qiree_backend` and `apps/quantum` exist. [KNOWN: file names; INFERRED: how mature this path is, since some lines in DeviceQIREE.cpp are commented out]

## How the project is organized
- `src/runtime/` (the C++ core), `include/` (public headers), `apps/` (examples and benchmarks), `tests/` (numbered tests like `01_init_finalize`, `11_deadlock`), `scheduling-policies/`, `schema/`, `docs/` (Sphinx and Doxygen), `utils/`, plus CMake, `setup.py`/`pyproject.toml` and Julia build files. [KNOWN: repo tree]
- Languages: Jupyter notebooks are the largest by bytes (likely stored outputs), then C++, C, Python and shell. [KNOWN: GitHub languages API; INFERRED: why notebooks dominate]
- Contributors: 12 including anonymous commit authors, 9 GitHub accounts without them. Created 2020-02-14. Releases: v1.0.0, v1.0.1 and v2.0.0 all on 2023-06-02, v3.0.0 on 2025-05-30, v3.0.1 on 2026-02-10. [KNOWN: GitHub API]
- Versioning: the CHANGELOG uses its own BRANCH.TAG.BUILD scheme, not standard semantic versioning. [KNOWN: CHANGELOG]
- Citation: the README asks users to cite a 2021 IEEE HPEC paper, "IRIS: A Portable Runtime System Exploiting Multiple Heterogeneous Programming Systems". It also lists a Zenodo DOI, 10.5281/zenodo.15556123. [KNOWN: README]

## Who uses it / why it matters
It targets labs that must run on very mixed hardware, which is the direction DOE supercomputers are heading. [INFERRED] Named users beyond its own papers are [UNKNOWN]. For a security student, a runtime that loads backends at run time is a useful example of a big trusted layer: it uses `dlopen` (loading shared libraries while running), which matters when you think about what code a program will trust. [KNOWN: `dlfcn.h` include in DeviceQIREE.cpp; INFERRED: security framing]

## Related projects
- QIR-EE (`qiree`): IRIS has a QIR-EE device backend. [KNOWN: `src/runtime/DeviceQIREE.cpp`] That's a new candidate link for the connections pass.
- HeCBench (`hecbench`): both are ORNL heterogeneous-computing work. Any direct tie is [UNKNOWN].

## Known / Inferred / Unknown
- KNOWN: BSD-3 license with UT-Battelle copyright, purpose, supported programming systems, backends, 3.0.0 features, layout, releases, citation.
- INFERRED: it's not a compiler or job scheduler; what the policies predict; the maturity of the quantum path; why notebooks dominate the byte count.
- UNKNOWN: owning group, outside users, which supercomputers its CI runs on (signals work).

## Sources (accessed 2026-10-24)
- https://github.com/ORNL/iris (README.md, LICENSE, CHANGELOG.md, src/runtime/, apps/, tests/, scheduling-policies/, docs/)
- https://iris-programming.github.io
- https://api.github.com/repos/ORNL/iris (plus /languages, /releases, /contributors)

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Rechecked: BSD-3 with "Copyright (c) 2021, UT-Battelle, LLC" (LICENSE line 3), created 2020-02-14, v3.0.1 on 2026-02-10 and the release list, contributors 12 with anonymous / 9 accounts, languages (Jupyter largest, then C++ and C; Julia, Rust and Fortran present), `Project.toml` and `pyproject.toml` present, the README "intelligent runtime system for extremely heterogeneous architectures" quote, iris-programming.github.io resolves, `src/runtime/DeviceQIREE.cpp` exists. All verified.
- Second primary source: OSTI 3018176 ("Q-IRIS: The Evolution of the IRIS Task-Based Runtime...", 2026) comes back under an ORNL research-org filter. Rule 13 is CORROBORATED.
- Namesake guard: DOE CODE code-75005 "slaclab/new-iris" is a SLAC project and is [UNRELATED].
- No corrections needed.
