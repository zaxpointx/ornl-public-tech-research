# ExaGO (Exascale Grid Optimization toolkit)
- Official page: no separate website. The README, the `docs/web/` pages and a PDF manual (`docs/manual/manual.pdf`) serve as the docs. [KNOWN: README]
- Repo: https://github.com/ORNL/ExaGO (default branch `develop`). It replaces the archived https://github.com/pnnl/ExaGO, whose README says development "has moved to the new repository". [KNOWN: GitHub API; the catalog row]
- License: a custom UT-Battelle open-source license, a BSD-like grant. The conditions are to keep notices, mark your changes, not use the names for endorsement, and include a fixed DOE contract acknowledgment. It also has a disclaimer, and GitHub reports NOASSERTION. The earlier v1.6.0 license is kept as `LICENSE-1.6.0`. [KNOWN: LICENSE, repo tree, GitHub API]
- Copyright: "Copyright (c) 2026, UT-Battelle." It also carries "Copyright (c) 2020-2025, Battelle Memorial Institute" for the reused ExaGO v1.6.0 code. Battelle Memorial Institute operates PNNL. [KNOWN: LICENSE lines 1-5; INFERRED: the PNNL operator link, general knowledge]
- Trademark: the README writes ExaGO™. [KNOWN]
- Status: active. v2.1.0 came out 2026-10-09 UTC and v2.0.0 on 2026-05-21 UTC. The last commit was 2026-10-19 ET (2026-10-20 00:05 UTC), and CMake says version 2.1.0. [KNOWN: GitHub releases, git log, CMakeLists.txt line 9]
- Scope (rule 13): CORROBORATED. ORNL owns the repo, UT-Battelle holds the copyright, and DOE CODE code-176348 "ExaGO v2" lists ORNL as research org. [KNOWN: GitHub, LICENSE, OSTI check in the discovery pass]

## Plain-language walkthrough
- **What it is:** software that works out the cheapest safe way to run an electric power grid, sized for supercomputers with GPUs. It's written in C/C++ with Python bindings. [KNOWN: README]
- **The problem:** grid operators have to decide how much each power plant should generate so that demand is met, wires don't overload, and voltages stay in safe ranges, all at minimum cost. That's called *optimal power flow* (OPF). Real grids have thousands of buses, meaning connection points. Operators also want plans that survive a line or plant failing and handle uncertain wind and solar output, which multiplies the problem size. [KNOWN: README's problem list; INFERRED: the explanation]
- **Key terms:**
  - *AC OPF* uses the full alternating-current physics, which is accurate but nonlinear and hard to solve.
  - *Contingency* or *security-constrained* means the plan must still work if any one listed component fails.
  - *Stochastic* means planning across several possible scenarios, like different wind forecasts.
  - *Multi-period* means planning over a sequence of time steps, respecting how fast plants can ramp up or down. [KNOWN: README; INFERRED: the definitions]
- **What goes in:** a grid model file in MATPOWER format (`.m`, a common power-systems case format), plus optional contingency lists and scenario files and an options file or command-line flags. [KNOWN: `datafiles/` such as `case118.m`, `case118.cont` and `10_scenarios_ACTIVSg200.csv`; README "Options"]
- **What happens:**
  1. ExaGO reads the network.
  2. It builds the optimization problem for the chosen application.
  3. It hands the problem to a solver: Ipopt (a widely used interior-point optimizer) or HiOp (an LLNL HPC optimizer, an outside dependency per rule 13).
  4. Large stochastic and contingency runs can be spread across many processes with MPI. [KNOWN: README, solver table; INFERRED: the step order]
- **What comes out:** a generation and voltage plan for each plant and bus, plus cost and line flows, which can be fed to a visualizer. [INFERRED from `src/ps/psoutput.cpp`, viz docs]
- **Where humans act:** an engineer prepares cases, picks the application and solver, and reads the results. The new AgentiGrid tool puts a large language model (LLM) in the loop, but a human still writes the goal. [KNOWN: agentigrid README]
- **What it is not:** it isn't a real-time grid control system or connected to any utility. It's an offline research toolkit that runs on test cases. [INFERRED: only synthetic and benchmark cases ship, such as ACTIVSg (synthetic Texas A&M grids) and IEEE-style case39/118/300]
- **What's unknown:** who uses v2 outside ORNL, and how far the GPU path is validated on Frontier beyond the config doc.
- **Example:** run OPFLOW on `case118.m` to get the cheapest generator settings for a 118-bus test grid, then run SCOPFLOW with `case118.cont` so the plan survives listed outages. [KNOWN: these files exist in `datafiles/`; INFERRED: that pairing]

## How it works
- **Applications** (each a separate executable in `applications/`):
  - OPFLOW: AC OPF on CPU or GPU.
  - TCOPFLOW: multi-period.
  - SCOPFLOW: security-constrained.
  - SOPFLOW: stochastic, optionally also security-constrained.
  - PFLOW: plain power flow.
  - DCOPFLOW: also present. [KNOWN: README; `applications/*_main.cpp`] DCOPFLOW has a main file but isn't in the README list. It likely uses the simplified "DC" approximation. [INFERRED from the name]
- **Solvers:** Ipopt supports all four OPF applications. HiOp supports OPFLOW, SCOPFLOW and SOPFLOW, and SCOPFLOW and SOPFLOW with HiOp still need Ipopt for the base problem. [KNOWN: README table and note]
- **Math backbone:** built on PETSc, a parallel scientific-computing library; v2.1 requires PETSc 3.25 or newer and ROCm 6.4 or newer, AMD's GPU stack. [KNOWN: CHANGELOG 2.1]
- **Front ends:**
  - A Python launcher app (`launcher/`).
  - "ChatGrid", a visualization front end built with React, PostgreSQL and LangChain (`viz/`). [KNOWN: README]
  - AgentiGrid, labeled "experimental", an LLM-driven loop added in 2.1. It edits grid inputs, reruns solvers and checks results against a goal written in plain English. [KNOWN: CHANGELOG 2.1, agentigrid README] I didn't run it and didn't use any LLM service credentials.

## How the project is organized
- Core code: `src/` (`ps` for the power-system data model, `opflow`, `pflow`, `scopflow`, `sopflow`, `tcopflow`, `contingencylist`, `utils`), `include/` and `applications/`.
- Python bindings and front ends: `interfaces/python`, `launcher/`, `viz/` and `agentigrid/`.
- Inputs, docs and tutorials: `datafiles/` (test grids), `docs/`, `tutorials/` (Jupyter demos) and `references/`.
- Build and test: `buildsystem/` (bash and Spack scripts, Spack being an HPC package manager), `performance_analysis/`, `tests/` and `tpl/` (bundled pybind11, spdlog, toml11 and Spack files). [KNOWN: repo tree, README]
- Languages: Python about 48.5% and C++ about 41.4% by bytes, then HTML, Shell, C and CMake. [KNOWN: GitHub languages API] The Python share is high because of the newer AgentiGrid, launcher and viz code. [INFERRED]
- Build: CMake 3.18 or newer. CI uses GitHub Actions (`pre_commit.yaml`, `spack_cpu_build.yaml` and `file_naming.yaml`), and the README also mentions GitLab CI. [KNOWN] The README offers prebuilt binaries only to developers "with access". We didn't look for them (rule 1).
- History: git history starts 2019-04-26, carried over from the PNNL repo. The ORNL repo was created 2026-01-08. There are 1,207 commits and 3 tags, of which two are releases. [KNOWN: git log, GitHub API]
- Contributors: 38 including anonymous commit authors, 22 GitHub accounts without them. 17 stars and 11 forks. [KNOWN: GitHub API]

## Who uses it / why it matters
Power-grid planning with lots of renewables and failure scenarios gets huge fast. ExaGO aims those problems at GPU supercomputers, and the README links a configuration doc for ORNL's Frontier. [KNOWN: README; INFERRED: the significance] For usage evidence, see the usage section in `signals/exago.md`.

## Related projects
- GridKit (`gridkit`, in our catalog): another ORNL power-grid code. [INFERRED: same domain; I didn't find a direct dependency, so this is for the connections pass to check]
- HiOp (LLNL) and PETSc: outside dependencies (rule 13).
- pnnl/ExaGO: the archived predecessor.

## Known / Inferred / Unknown
- KNOWN: license and copyrights, move from PNNL, DOE CODE, releases, applications, solver table, dependencies, layout, counts.
- INFERRED: the definitions, what DCOPFLOW means, the "offline research" framing, any GridKit relation.
- UNKNOWN: outside adoption, Frontier performance results, why development moved to ORNL.

## Sources (accessed 2026-10-24)
- https://github.com/ORNL/ExaGO (README.md, LICENSE, CHANGELOG.md, CMakeLists.txt, src/, applications/, agentigrid/README.md, viz/, datafiles/, .github/workflows/)
- https://api.github.com/repos/ORNL/ExaGO (plus /languages, /releases, /tags, /contributors)
- https://github.com/pnnl/ExaGO (archived; per the catalog row)
- https://www.osti.gov/doecode/biblio/176348 (per the catalog row)

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Verified: LICENSE (UT-Battelle 2026, plus the Battelle 2020-2025 notice for v1.6.0 code), DOE CODE code-176348 "ExaGO v2" with ORNL as research org (OSTI API, 2026-03-02), pnnl/ExaGO archived (GitHub API), releases v2.1.0 2026-10-09 and v2.0.0 2026-05-21, contributors 38 with anonymous, languages Python 48.5% and C++ 41.4%.
- Corrected: the last commit time zone. The develop feed shows 2026-10-20 00:05 UTC, which is 2026-10-19 ET, so both are now stated.
- AgentiGrid: the "experimental" label comes from CHANGELOG 2.1 ("Add AgentiGrid experimental agentic AI user interface"). The agentigrid README describes the LLM loop but doesn't use the word. The KNOWN tag holds because CHANGELOG is cited. Not run.
- Rule 13 CORROBORATED holds (ORNL repo owner and UT-Battelle LICENSE, plus OSTI code-176348).
