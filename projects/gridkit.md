# GridKit
- Official page: https://gridkit.readthedocs.io/en/latest/ [KNOWN: README]
- Repo: https://github.com/ORNL/GridKit (default branch `develop`) [KNOWN: GitHub API]
- License: a custom UT-Battelle permissive (BSD-like) license, "Copyright (c) 2025, UT-Battelle." GitHub reports NOASSERTION. A NOTICE file carries the standard DOE/UT-Battelle disclaimer. [KNOWN: LICENSE line 1, NOTICE, GitHub API]
- Trademark: the README writes GridKit™. [KNOWN]
- Status: active. The last commit was 2026-10-23. Releases are v0.0.7 (2023-07-18 UTC), v0.1.0 (2025-04-14 UTC) and v0.2.0 (2026-10-01 UTC), and the CHANGELOG already has an unreleased "v.03" section. [KNOWN: git log, GitHub releases API, CHANGELOG.md] It's still pre-1.0, so interfaces may change. [INFERRED: version numbers]
- Scope (rule 13): CORROBORATED. ORNL owns the repo, UT-Battelle holds the copyright, and DOE CODE code-152622 (2025-03-14) lists ORNL as research org. [KNOWN: GitHub, LICENSE; https://www.osti.gov/doecode/biblio/152622 per Scout]
  - An older same-named OSTI software record isn't cited here, per the lead's ruling. [rule 10: no merging without binding evidence]
- Rewrite note: this replaces the batch 01 brief, adding the rule 12 walkthrough, both contributor counts, and no named individuals. The old version is kept at `<local scratch copy>` for Fact Checker.

## Plain-language walkthrough
- **What it is:** a C++ toolkit for building computer models of a power grid and simulating how it behaves, both in steady state and during disturbances like a fault on a line. [KNOWN: README]
- **The problem:** grid studies need many kinds of models (generators, loads, lines, inverters for solar and batteries) and many kinds of math (steady-state solves, time simulation, optimization). Most tools lock you into one. GridKit wants one framework that can hold "multiple families of models" and plug in different solvers. [KNOWN: README, short quote; INFERRED: the framing]
- **Key terms:**
  - *Power flow* is the steady-state snapshot of voltages and flows on every line.
  - *Phasor dynamics* simulates the grid over seconds using averaged sine-wave quantities. It's the standard way to ask "does the grid stay stable after this fault?"
  - *EMT* (electromagnetic transients) is a much finer, waveform-level simulation, needed for fast power electronics.
  - *DAE* means differential-algebraic equations, the type of math these simulations boil down to. [KNOWN: model folder names, README "differential and algebraic equations"; INFERRED: the definitions]
- **What goes in:** a grid case described in JSON, giving buses, branches, generators with their controls (exciters, governors), and loads. [KNOWN: `GridKit/Model/PhasorDynamics/ComponentDataJSONParser.hpp`, `INPUT_FORMAT.md`, CHANGELOG v0.2 "Added JSON parsing"] Test cases range from toy and two-area systems to IEEE 39-bus, WECC 240-bus, Hawaii, and synthetic ACTIVSg grids of up to 10,000 buses. [KNOWN: `cases/PhasorDynamics/`]
- **What happens:**
  1. GridKit builds the equations for every component and connects them through buses and ports.
  2. It hands the whole system to a solver: SUNDIALS for time simulation, Ipopt for optimization, or ReSolve (another ORNL library) for GPU linear solves.
  3. It steps through time, applying events such as faults or switching a branch out. [KNOWN: README dependencies, `GridKit/Solver/{SteadyState,Dynamic,Optimization}`, CHANGELOG v.03 events; INFERRED: the step order]
- **What comes out:** voltages, angles and machine states over time for the variables you choose to monitor. [KNOWN: `VariableMonitor*.hpp`; INFERRED: the output type]
- **Where humans act:** an engineer writes or converts the case file, chooses the solver and events, and reads the results. [INFERRED]
- **What it is not:** it isn't an optimizer for running the whole grid the way ExaGO is, and it isn't connected to any real utility. It's a modeling and simulation library tested on public benchmark cases. [INFERRED; Connector's link 150 found no code link to ExaGO]
- **What's unknown:** who uses it outside ORNL, and how close the EMT side is to working. The examples README calls the EMT examples "architecture skeletons". [KNOWN: examples/README.md]
- **Example:** load the IEEE 39-bus case, put a fault on one bus for a fraction of a second, then clear it, and watch whether the generators swing back into step. [KNOWN: `cases/PhasorDynamics/IEEE39`, `Bus::setFault` in CHANGELOG v.03; INFERRED: the scenario]

## How it works
- **Model families:**
  - `PowerFlow`: steady state.
  - `PhasorDynamics`: buses, branches, loads, exciters, governors, converters, controllers and signal nodes.
  - `PowerElectronics`: microgrid examples.
  - `EMT`: early.
  - `Experimental`: dynamic-constrained optimization. [KNOWN: `GridKit/Model/`, examples/README.md]
- **Automatic differentiation:** optional Enzyme support computes the derivatives solvers need straight from the code, so they don't have to be written by hand. The README calls it experimental and warns some Enzyme versions break the build. [KNOWN: README, CHANGELOG v0.2]
- **Optional features:** OpenMP and threads, ZeroMQ (a messaging library, possibly for co-simulation), and address and undefined-behavior sanitizers for catching memory bugs. [KNOWN: CMake options; INFERRED: the ZeroMQ purpose]

## How the project is organized
- `GridKit/` is the core library (Model, Solver, LinearAlgebra, AutomaticDifferentiation, MemoryUtilities, Utilities, Testing). The other folders are `application/` (a phasor-dynamics app), `cases/`, `examples/` (which double as integration tests), `tests/`, `docs/`, `buildsystem/`, `cmake/`, and `third-party/` (git submodules for magic-enum and nlohmann-json). [KNOWN: repo tree, examples/README.md]
- Languages: C++ about 96.9% by bytes, then CMake, Python and Dockerfile. [KNOWN: GitHub languages API]
- Build: CMake 3.13 or newer and a C++20 compiler. Every solver dependency is optional and off by default. Tested on Linux and Mac. [KNOWN: README, CMakeLists.txt]
- CI: GitHub Actions `pre_commit.yaml` and `spack_default_build.yaml`. [KNOWN]
- Contributors: 22 including anonymous commit authors, 17 GitHub accounts without them. Repo created 2023-07-18. 27 stars and 11 forks. [KNOWN: GitHub API] The README credits outside contributors from universities and industry. Per team convention, names aren't listed here.

## Who uses it / why it matters
As grids add solar, wind and batteries, they behave faster and less predictably. A flexible simulator that can mix detailed and averaged models helps researchers test whether a future grid stays stable. [INFERRED] For usage evidence, see Connector's section in `signals/gridkit.md`.

## Related projects
- ReSolve (`resolve`, catalog stub): an optional GPU linear-solver dependency. [KNOWN: README]
- ExaGO (`exago`): same field, no code link (Connector link 150). [KNOWN per map]
- SUNDIALS (LLNL) and Ipopt (COIN-OR): outside dependencies.

## Known / Inferred / Unknown
- KNOWN: license, DOE CODE, releases, dependencies, model families, cases, layout, CI, counts.
- INFERRED: the physics definitions, step order, the ZeroMQ purpose, the significance.
- UNKNOWN: outside adoption, EMT maturity, roadmap to 1.0.

## Sources (accessed 2026-10-24)
- https://github.com/ORNL/GridKit (README.md, LICENSE, NOTICE, CHANGELOG.md, CMakeLists.txt, GridKit/, cases/, examples/README.md, .github/workflows/)
- https://api.github.com/repos/ORNL/GridKit (plus /languages, /releases, /contributors)
- https://gridkit.readthedocs.io/en/latest/ (linked)
- https://www.osti.gov/doecode/biblio/152622 (per Scout)
