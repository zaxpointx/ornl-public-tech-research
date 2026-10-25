# FIXS (Flexible Interface for X-in-the-loop Simulation)
- Official page: https://www.osti.gov/doecode/biblio/110562 (DOI 10.11578/dc.20230727.1)
- Repo: https://github.com/ORNL-Real-Sim/FIXS
- Docs: https://real-sim.readthedocs.io/en/latest/index.html, plus `doc/` in the repo
- License: MIT, copyright 2023 UT-Battelle, LLC [KNOWN: https://github.com/ORNL-Real-Sim/FIXS/blob/main/LICENSE]. The README says the `ProprietaryFiles` submodule is a separate private repository that the MIT license doesn't cover. [KNOWN: README] We didn't open or try to reach it.
- Status: very active [KNOWN: last push 2026-10-23; v0.9.0-alpha and v0.9.0-beta released 2026-10-12, GitHub API]


## Plain-language walkthrough
- **What it is:** a connector that makes traffic simulators, vehicle simulators and real hardware run as one test. [KNOWN: README]
- **The problem:** testing self-driving controllers in real traffic is costly and risky, but pure simulation misses real hardware effects.
- **What goes in:** a `config.yaml` naming the tools (such as SUMO, CarMaker, CARLA, VISSIM or Simulink) and how they connect. [KNOWN: README]
- **What happens:** FIXS passes vehicle states and commands between the tools each step. [KNOWN: `doc/FIXS_message_flow.md`]
- **What comes out:** a synchronized co-simulation, where a test vehicle drives among simulated traffic. [INFERRED]
- **Where humans act:** researchers write the config and controllers, and sometimes drive real hardware.
- **What it is not:** it's not a simulator itself. The private `ProprietaryFiles` part isn't open. [KNOWN: README]
- **What's unknown:** the leading ORNL division.
- **Example:** SUMO traffic, a Python speed controller and a Simulink vehicle model running together. The docs note a one-step command delay in this setup. [KNOWN: `doc/FIXS_message_flow.md`]

## What it is
FIXS is the "glue" layer of ORNL's Real-Sim project. It connects traffic simulators, vehicle simulators, 3D driving environments and real hardware, so they run together as one test. [KNOWN: README] "X-in-the-loop" (XIL) means swapping one part of a simulation for a real thing: a real controller board (hardware-in-the-loop), real software, or even a real car on a test track, while the rest stays virtual. [INFERRED: standard definition; the README uses XIL without defining it] The goal is to test connected and automated vehicles in realistic traffic without needing a real city full of cars. [KNOWN: README]

## How it works
- **Plug-and-play co-simulation:** you describe the setup in a `config.yaml` file, and FIXS handles the connections between tools behind the scenes. [KNOWN: README]
- **Supported tools:** SUMO and VISSIM (traffic), CarMaker (vehicle dynamics), CARLA (3D driving simulator), and dSPACE/MATLAB-Simulink (control and vehicle models). The README lists the versions it's developed against: CarMaker 13.1.3, CARLA 0.9.15, VISSIM 2022, SUMO 1.21, dSPACE/MATLAB 2024a. [KNOWN: README]
- **Message loop:** the traffic simulator sends vehicle states, a Python controller computes commands, a detailed Simulink vehicle model works out the physical response, and the results go back to the traffic simulator. The docs openly note that the current setup has a one-step delay in the speed command, because SUMO is serving two clients. [KNOWN: `doc/FIXS_message_flow.md`] That kind of honest timing note matters a lot in hardware testing. [INFERRED]

## How the project is organized
- Top level: `TrafficLayer/` (the core C++ interface), `CommonLib/` (shared code, including `fixs`, `xil`, `VirEnv` and a bundled `yaml-cpp`), and one folder per tool: `Carla/`, `CarMaker/`, `VISSIM/`, `VirtualEnvironment/`, `VirCarlaEnv/`. Also `standalone/`, `scripts/` (including release dispatch), `tests/` (24 test folders), `doc/` (Sphinx docs, tutorials, API) and `cmake/`. [KNOWN: repo tree]
- Languages: C++ 53%, Python 36.6%, plus PowerShell, MATLAB, Shell and Batch. Windows build scripts (`dispatch.bat`, PowerShell) suggest Windows is the main platform. [KNOWN: GitHub languages API, repo files; INFERRED: the platform]
- Build: CMake, with Python environment files (`pyproject.toml`, `uv.lock`, `environment.yml`). [KNOWN: repo]
- Contributors: about 10. [KNOWN: GitHub contributors API]
- Team: Real-Sim is led by ORNL with the University of Georgia and the University of Texas at Dallas, and the README lists the University of Georgia as primary maintainer. [KNOWN: README] (Staff contact details are left out on purpose.)
- Funding: DOE Vehicle Technologies Office, Energy Efficient Mobility Systems (EEMS) program, as one of EEMS's "core tools". DOE Annual Merit Review slides from 2021 to 2024 are linked in the README. [KNOWN: README]

## Who uses it / why it matters
Researchers testing automated-driving controllers against realistic traffic. A cyber angle: any co-simulation that wires real hardware to networked simulators depends on message timing and integrity, so it's a natural place to study attacks on connected-vehicle data. [INFERRED]

## Related projects
- Real-Twin (`real-twin`): same ORNL-Real-Sim GitHub org [KNOWN]. Real-Twin generates traffic scenarios, and FIXS runs live co-simulations. They're likely complementary [INFERRED: no code dependency checked].
- Both support SUMO and VISSIM. [KNOWN: both READMEs]

## Known / Inferred / Unknown
- KNOWN: purpose, supported tools and versions, message flow, layout, MIT license, private submodule exists, team, funding, DOI.
- INFERRED: XIL definition, Windows focus, cyber relevance.
- UNKNOWN: which ORNL division leads it, and what a "stable" release means versus the version tags.

## Sources (accessed 2026-10-24)
- https://github.com/ORNL-Real-Sim/FIXS (README, LICENSE, doc/FIXS_message_flow.md)
- https://api.github.com/repos/ORNL-Real-Sim/FIXS (plus /languages, /releases, /contributors)
- https://www.osti.gov/doecode/biblio/110562

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Sweeps 1 and 2 done. Verified against the GitHub API and the README/LICENSE (main, 2026-10-24) plus DOE CODE 110562.
- Verified: MIT, "Copyright (c) 2023 UT-Battelle, LLC", last push 2026-10-23, C++ 53.0% / Python 36.6%, homepage real-sim.readthedocs.io, and DOE CODE DOI 10.11578/dc.20230727.1 with VTO as sponsor.
- README: "Real-Sim Project Lead: Oak Ridge National Lab", team UGA and UT-Dallas, "Primary Maintainer: University of Georgia", and "It is part of the core tools of EEMS."
- ProprietaryFiles: "a separate private repository and is not covered by this license." It was not opened.
- Tool versions verified (README: "CM13.1.3, Carla 0.9.15, VISSIM 2022, SUMO 1.21, dSPACE/Matlab 2024a"). The one-step SUMO delay is verified in doc/FIXS_message_flow.md.
- Added: the repo has 9 releases, including a "stable" tag (2026-09-27) and v0.10.0-alpha (2026-09-23), so version numbering isn't linear. What "stable" means is UNKNOWN.
- The README lists ORNL PI names and emails. They're still kept out of the brief.
