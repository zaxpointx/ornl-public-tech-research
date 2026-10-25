# Real-Twin
- Official page: https://www.osti.gov/doecode/biblio/147051 (DOI 10.11578/dc.20250602.3)
- Repo: https://github.com/ORNL-Real-Sim/Real-Twin
- Docs: https://real-twin.readthedocs.io/en/latest/
- License: GPL-3.0 [KNOWN: https://github.com/ORNL-Real-Sim/Real-Twin/blob/main/LICENSE]
- Status: active [KNOWN: last push 2026-10-08, GitHub API]


## Plain-language walkthrough
- **What it is:** a Python tool that builds a traffic "digital twin", meaning a simulated copy of a real road network. [KNOWN: README]
- **The problem:** setting up a realistic traffic simulation by hand for a real area takes a lot of manual work.
- **What goes in:** real-world network and traffic data plus a config, for SUMO, VISSIM or AIMSUN. [KNOWN: README supported simulators; INFERRED: input types]
- **What happens:** staged functions in `func_lib` install the simulator, generate the network and demand, calibrate it and visualize it (stages `_a_` to `_h_`). [KNOWN: repo layout]
- **What comes out:** a calibrated simulation scenario ready to run. [INFERRED]
- **Where humans act:** engineers pick the area and data and check the calibration.
- **What it is not:** it isn't a traffic simulator itself. It drives existing ones. [KNOWN: README]
- **What's unknown:** which ORNL group runs it. (Release history is now known, see "How the project is organized".)
- **Example:** `pip install realtwin`, then building a SUMO model of a corridor for testing signal timing. [KNOWN: pip name; INFERRED: the use case]

## What it is
Real-Twin builds traffic simulations from real-world data, so researchers can test things like self-driving cars on a virtual copy of real streets before trying them for real. [KNOWN: README and repo description] A "digital twin" is a simulation kept close enough to the real system that you can experiment on it. Its main selling point is that it's "platform-agnostic": one workflow produces matching scenarios for three different traffic simulators. [KNOWN: README]

## How it works
- **Microscopic traffic simulation** models every single vehicle and its decisions (speeding up, changing lanes, stopping at lights), rather than treating traffic as an average flow. Real-Twin supports three such simulators: SUMO (free and open source), VISSIM and AIMSUN (both commercial). [KNOWN: README for the three names; INFERRED: the open versus commercial status]
- **Workflow:** you write a YAML config file, check which simulators are installed, build a "matchup table" from a SUMO road network, add traffic demand and signal-timing data, generate an "abstract scenario" (independent of any simulator), then generate the concrete scenarios for each simulator. [KNOWN: README quick example]
- **Calibration** means tuning the simulation until its outputs match real measured traffic. Real-Twin automates part of it. [KNOWN: README]
- **Autonomous vehicles (AVs):** it includes a scenario database and pipeline for AV studies, with connected vehicles (CAVs) and EVs planned. [KNOWN: README]

## How the project is organized
- `realtwin/func_lib/` has one folder per pipeline stage, named in order: `_a_install_simulator`, `_b_load_inputs`, `_c_abstract_scenario`, `_d_concrete_scenario`, `_e_simulation`, `_f_calibration`, `_g_analyzer`, `_h_vis`. That's a neat, readable map of the whole workflow. [KNOWN: repo tree]
- Also: `realtwin/autonomous_veh`, `data_lib` and `util_lib`; `datasets/`, including `chattanooga` and `Nolen` examples; `docs/` (Sphinx/Read the Docs); `tests/`; and tutorials as a `.py`, `.md` and Jupyter notebook. [KNOWN: repo tree]
- Language: Python 97.4%. It's installed with `pip install realtwin`, and `pyproject.toml` says version 0.1.2. [KNOWN: GitHub languages API, README, pyproject.toml]
- Releases: v0.0.9.dev3 (2025-06-02), v0.1.0 (2025-06-05), v0.1.1 (2026-03-13), v0.1.2 (2026-05-12) [KNOWN: GitHub releases API, rechecked 2026-10-24]. PyPI also has realtwin 0.1.2 [KNOWN: https://pypi.org/pypi/realtwin/json]. The CHANGELOG is dated, with the latest entry 2026-02-19, and says test coverage went from 22% to 38% in October 2025, with 90% as the goal. [KNOWN: CHANGELOG.md]
- Contributors: about 9. [KNOWN: GitHub contributors API]
- Funding: DOE Vehicle Technologies Office, Energy Efficient Mobility Systems program, project EEMS114. [KNOWN: README; OSTI DOE CODE 147051 lists VTO as sponsor and ORNL as research org]

## Who uses it / why it matters
Transportation researchers who want reproducible comparisons. Running the same scenario in SUMO, VISSIM and AIMSUN shows whether a result comes from the technology or from quirks of one simulator. [KNOWN: README for cross-validation; INFERRED: the framing] The Chattanooga dataset suggests it's tested on real Tennessee roads. [INFERRED: from the folder name]

## Related projects
- Gauntlet (`gauntlet`): another ORNL buildings/transport geospatial tool. [INFERRED: same domain, no code link]
- FIXS (`fixs`, formerly Real-Sim): same ORNL-Real-Sim GitHub org [KNOWN: https://github.com/ORNL-Real-Sim/FIXS]. FIXS links traffic simulators to vehicle and hardware-in-the-loop tests, while Real-Twin builds the scenarios. They're likely complementary [INFERRED: no code dependency checked].

## Known / Inferred / Unknown
- KNOWN: purpose, three simulators, pipeline stages, GPL-3.0, Python, version 0.1.2, funding, DOI.
- KNOWN: FIXS sits in the same ORNL-Real-Sim GitHub org.
- INFERRED: SUMO's open-source status, the Chattanooga test site, that Real-Twin and FIXS work together.
- UNKNOWN: which ORNL group runs it.

## Sources (accessed 2026-10-24)
- https://github.com/ORNL-Real-Sim/Real-Twin (README, LICENSE, CHANGELOG.md, CITATION.cff, pyproject.toml)
- https://api.github.com/repos/ORNL-Real-Sim/Real-Twin
- https://www.osti.gov/doecode/biblio/147051
- https://real-twin.readthedocs.io/en/latest/

## Fact-check notes (ORNL Fact Checker, 2026-10-24)
- Corrected: releases recheck worked. There are four GitHub releases, and PyPI versions run 0.0.9.dev2 to 0.1.2.
- Verified: func_lib _a to _h stages; datasets include chattanooga and Nolen; README platform-agnostic, SUMO/VISSIM/AIMSUN, calibration, AV/CAV/EV, pip install, VTO EEMS funding; CHANGELOG 22% to 38% coverage and 90% goal; version 0.1.2; Python 97.4%; GPL-3.0; OSTI code-147051 ORNL research org, VTO sponsor, DOI 10.11578/dc.20250602.3; FIXS in the same org (its description says it's part of the EEMS Real-Sim project).

## Sweep 2 notes (ORNL Fact Checker, 2026-10-24)
- Re-fetched the GitHub API (GPL-3.0, last push 2026-10-08, 4 releases, 9 contributor pages), README and OSTI code-147051. No contradictions.
- Corrected: the walkthrough still said release history was unknown because an API call failed. That was stale after sweep 1, so it is fixed.
- Corrected: "the Real-Sim family" split into KNOWN same org and INFERRED working together, matching map link 79.
- Load-bearing quotes: funding, README "Acknowledgement": "supported by the US Department of Energy, Vehicle Technologies Office, Energy Efficient Mobility Systems (EEMS) program, under project Real-Twin (EEMS114)". Simulators, OSTI code-147051 (Software, 2025-06-02, ORNL research org, VTO sponsor): "supports SUMO, VISSIM, and AIMSUN". The README and OSTI name the same three simulators, but the OSTI text copies the README, so this stays KNOWN rather than CORROBORATED.
- Walkthrough present. No maturity upgrades.
