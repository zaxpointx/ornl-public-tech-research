# adamantine
- Official page: https://adamantine-sim.github.io/adamantine/ (project site, the repo's homepage field) [KNOWN: GitHub API, README]
- Repo: https://github.com/adamantine-sim/adamantine (default branch `master`)
- Docs: the project site above. Tutorials are in a separate repo, https://github.com/adamantine-sim/adamantine-tutorials [KNOWN: README]
- License: Apache License 2.0 with LLVM Exceptions. Quote: "adamantine is under the Apache License v2.0 with LLVM Exceptions" [KNOWN: https://github.com/adamantine-sim/adamantine/blob/master/LICENSE, line 2]. It was relicensed from 3-clause BSD in release 1.1. [KNOWN: CHANGELOG 1.1, PR 346] GitHub's API shows NOASSERTION, and `CITATION.cff` still says "BSD-3-Clause", which looks stale. [KNOWN: both files; INFERRED: stale]
- Status: active [KNOWN: last push 2026-10-21 UTC, not archived, GitHub API]
- Scope (rule 13): the OSTI record for the JOSS paper lists ORNL as the research org. [KNOWN: https://www.osti.gov/biblio/2472702, research_orgs "Oak Ridge National Laboratory (ORNL), Oak Ridge, TN (United States)"] The repo itself sits in a project org (`adamantine-sim`), not under github.com/ORNL, and the README doesn't name ORNL. [KNOWN: README]

## Plain-language walkthrough
- **What it is:** a simulator for 3D metal and plastic printing (*additive manufacturing*, AM: building an object layer by layer). The README calls it "a thermomechanical code for additive manufacturing". *Thermomechanical* means it tracks both heat and the forces and bending that heat causes. [KNOWN: README]
- **The problem:** when a printer melts material with a laser, electron beam or hot nozzle, the part heats and cools unevenly. That can warp it or leave hidden stress. Printing test parts to find out is slow and costly, so engineers simulate first. [INFERRED: standard AM motivation; the README describes simulating the "thermomechanical evolution" during manufacturing]
- **What goes in:** an input file describing the part's geometry, material properties, the heat source and the *scan path* (the route the laser or nozzle takes). Optionally, real sensor data from the print, such as thermocouples or infrared cameras. [KNOWN: `applications/input.info`, `input_scan_path.txt`; OSTI 2472702 abstract]
- **What happens:** it solves the heat equation with the *finite element method* (splitting the part into many small cells and solving on each), refining the mesh where things change fast. It can add elastic and plastic deformation on top. Material can be powder, liquid or solid. [KNOWN: OSTI 2472702 abstract, README]
- **What comes out:** temperatures over time, stress (von Mises stress, a single number engineers use to judge if metal will yield), and cooling rates and temperature gradients at the melting point, written to files for visualization. [KNOWN: CHANGELOG 1.1]
- **Where humans act:** engineers write the input, supply sensor data if they have it, and read the results to adjust the print.
- **What it is not:** it doesn't control a printer, and it isn't a CAD tool for designing parts. [INFERRED: no printer-control or design code in `source/`]
- **What's unknown:** which ORNL group or facility runs it, and who uses it outside the paper authors.
- **Example:** you simulate a laser printing a metal block along a given scan path. Midway through, you feed in infrared camera readings from the real print. The *Ensemble Kalman filter* (a statistics method that runs many slightly different simulations and nudges them toward the measurements) corrects the simulation so it better matches that specific print. [KNOWN: README names the Ensemble Kalman filter; OSTI abstract names thermocouples and IR cameras]

## How it works
- **Built on big math libraries:** deal.II (finite elements), p4est (mesh splitting across computers), ArborX (fast geometric search), Trilinos (solvers) and Kokkos (one code that runs on CPUs or GPUs). [KNOWN: README; OSTI 2472702 abstract]
- **Heat sources:** separate models for a Gaussian beam, a Goldak model (a standard welding heat shape), an electron beam and a simple cube. [KNOWN: `source/*HeatSource.cc` file names]
- **Data assimilation:** `DataAssimilator.cc` and `ExperimentalData.hh` handle merging sensor data into the run. *Data assimilation* means correcting a running model with real measurements, the same idea weather forecasting uses. [KNOWN: file names, README]
- **CPU and GPU versions:** many files come in `Host` (CPU) and `Dev` (device or GPU) variants, which is how Kokkos code is usually split. [KNOWN: file names; INFERRED: the Kokkos reading]
- **Parallel runs:** release 1.1 added MPI (the standard way to split one simulation across many computers) for mechanical simulations without adaptivity. [KNOWN: CHANGELOG 1.1]

## How the project is organized
- `source/` (the physics and solver code), `applications/` (the `adamantine` program, example inputs and an activation visualizer), `tests/`, `doc/` (Doxygen), `ci/` (a Dockerfile and Jenkins-style `continuous.groovy` and `nightly.groovy` pipelines), `cmake/`, plus a Nix build (`flake.nix`, `NIX.md`). [KNOWN: repo tree]
- Languages: almost all C++ (about 95% by bytes), with CMake, Python, Nix and Docker. [KNOWN: GitHub languages API]
- Contributors: 11 including anonymous commit authors, 10 GitHub accounts without them. The repo was created 2016-06-30. GitHub releases: v1.0 (2024-10-01) and v1.1 (published 2026-01-23). [KNOWN: GitHub API] The CHANGELOG dates release 1.1 to 2025-01-23, a year earlier than the GitHub release object. [KNOWN: CHANGELOG] The 2026 date is [CORROBORATED]: the v1.1 tag and release were created 2026-01-23, the `release/1.1` branch commits run from 2026-01-12 to 2026-01-23, and the CHANGELOG itself was last edited on master on 2026-01-23. [KNOWN: GitHub releases API; https://github.com/adamantine-sim/adamantine/commits/release/1.1.atom; commits/master/CHANGELOG.md.atom] So the CHANGELOG's 2025 is very likely a year typo. [INFERRED]
- Paper: "Adamantine 1.0: A Thermomechanical Simulator for Additive Manufacturing", Journal of Open Source Software, 2024, DOI 10.21105/joss.07017. [KNOWN: CITATION.cff, OSTI 2472702]
- Funding: OSTI lists DOE LDRD and DOE's Office of Energy Efficiency and Renewable Energy (EERE) as sponsors. [KNOWN: OSTI 2472702 sponsor_orgs]

## Who uses it / why it matters
The paper says it's especially suited to fused filament fabrication (plastic-style nozzle printing), directed energy deposition and powder bed fusion. [KNOWN: OSTI 2472702 abstract] Named users beyond the authors are [UNKNOWN]. The interesting idea for a cyber student is the "digital twin" pattern: a simulation that keeps correcting itself with live sensor data from one specific physical process. [INFERRED: framing; the source doesn't use the term "digital twin"]

## Related projects
- 3DThesis (`3dthesis`), AdditiveFOAM (`additivefoam`), Myna (`myna`) and ExaCA (in the map as an outside project): all are AM simulation codes in our catalog or map. Direct code ties are [UNKNOWN]. I didn't check dependency files for them.
- Trilinos and Kokkos: outside libraries adamantine depends on. [KNOWN: README]

## Known / Inferred / Unknown
- KNOWN: ORNL as research org (OSTI), license and relicense, purpose, physics features, dependencies, layout, paper, sponsors, release objects.
- INFERRED: that CITATION.cff's license is stale; that it doesn't control printers; the Kokkos Host/Dev reading.
- UNKNOWN: owning group, outside users.

## Sources (accessed 2026-10-24)
- https://github.com/adamantine-sim/adamantine (README.md, LICENSE, CHANGELOG.md, CITATION.cff, source/, applications/, ci/)
- https://adamantine-sim.github.io/adamantine/
- https://www.osti.gov/biblio/2472702 (via https://www.osti.gov/api/v1/records?osti_id=2472702)
- https://api.github.com/repos/adamantine-sim/adamantine (plus /languages, /releases, /contributors)

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Rechecked license (LICENSE line 2, PR 346 "Relicense to apache 2.0 with the llvm exception"), CITATION.cff still BSD-3, OSTI 2472702 research org and sponsors, README quotes, contributors 10 accounts / 11 with anonymous, releases v1.0 2024-10-01 and v1.1 2026-01-23, project site and tutorials repo (both 200). All verified.
- Corrected: the 1.1 release date is no longer UNKNOWN. Release branch and CHANGELOG commit dates confirm 2026-01-23, so the CHANGELOG's 2025 is tagged as an INFERRED typo.
- Scope (rule 13) holds on OSTI 2472702. No ORNL affiliation is implied in the brief.

## GOAL.md questions (added 2026-10-24)
- **Who pays (Q3):** OSTI 2472702 lists DOE LDRD (the lab's internal research-and-development fund) and EERE. [KNOWN, above]
- **Where in the tree (Q2):** ORNL, then additive manufacturing, on the 3D-printing ladder (part-scale thermal and mechanical simulation). It lives in its own GitHub org, not an ORNL one. [KNOWN: repo owner]
- **What it teaches about ORNL (Q8):** LDRD seed money can grow a code into a standalone project with its own org, releases and a paper, and the license can change partway (BSD-3 to Apache with LLVM exceptions). [KNOWN: sponsors, CHANGELOG; INFERRED: the growth story]
- **Student angle (Q9):** it has a CONTRIBUTING.md and a separate tutorials repo. [KNOWN] You'd need C++, deal.II (a finite-element library) and some heat-transfer basics, so it's steep. [INFERRED]
- **Searched without result (Q10):** see this brief's unknowns.
