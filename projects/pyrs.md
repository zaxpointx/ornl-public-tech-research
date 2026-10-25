# PyRS (pyRS)
- Official docs: https://neutrons-pyrs.readthedocs.io/en/latest/index.html (GitHub homepage field). The repo also has a `docs/` folder with user, developer and planning notes. [KNOWN: GitHub API, tree]
- Repo: https://github.com/neutrons/PyRS (default branch `next`). GitHub's description is "Reduction and visualization software for Stress Residual (HB2B)". [KNOWN: GitHub API]
- License: GPL-3.0, per the LICENSE file and the GitHub API. It's the standard GPL text with no project copyright holder named. [KNOWN: LICENSE, GitHub API]
- Status: active (rule 14). The last commit was 2026-10-21 10:11 ET, and the last push was 2026-10-23 09:44 UTC. Not archived. [KNOWN: git log, GitHub API]
  - Releases: the GitHub Releases list has v1.8.0 (2026-02-03) as the newest, and the git tags go to v1.8.1 (2026-03-13). [KNOWN: GitHub API, git tags]
- Scope (rule 13): CORROBORATED.
  - OSTI 17315105, "pyRS 2.0: software for the calibration, reduction and analysis of neutron engineering diffraction data", is a Journal of Applied Crystallography article (publication date 2026-10-01, DOI 10.1107/S1600576726007855).
  - It lists "Research Org.: Oak Ridge National Laboratory (ORNL)" with sponsor USDOE. [KNOWN: https://www.osti.gov/api/v1/records/17315105, accessed 2026-10-24]
  - `pyproject.toml` describes it as reduction of data "measured at the HFIR HB2B instrument". HFIR, ORNL's High Flux Isotope Reactor, is named in that file only by acronym. [KNOWN: pyproject.toml line 3]
- Org unit: the `neutrons` GitHub org. [INFERRED: the SNS/HFIR software group]

## Plain-language walkthrough
- **What it is:** a Python program with a graphical interface that turns neutron measurements from HB2B (also called HIDRA, the High Intensity Diffractometer for Residual Stress Analysis) into maps of the hidden stress inside metal parts. [KNOWN: description, OSTI abstract]
- **Key terms:**
  - *Residual stress* is force locked inside a part after welding, 3D printing or machining. It can make parts warp or crack later.
  - Neutrons pass deep into metal, so diffraction can measure tiny changes in the spacing between atoms (*strain*) without cutting the part open. Stress is then calculated from strain.
  - *Peak fitting* means fitting a curve to each bump in the diffraction pattern to find its exact position.
  - *Texture* is the preferred direction the grains in a metal point. [KNOWN: OSTI abstract mentions residual stress and texture analysis; INFERRED: the explanations]
- **The problem:** engineers need reliable, non-destructive stress maps of real components. The OSTI abstract says accurate reduction software "is essential for maximizing instrument capabilities". [KNOWN: OSTI abstract]
- **What goes in:** a NeXus file (the standard neutron data format) from an HB2B run. [KNOWN: README workflow step 1]
- **What happens:** the README lays out the steps:
  1. Split the run into sub-scans and create a "project file".
  2. Make powder diffraction patterns and add them.
  3. Fit the peaks in the GUI.
  4. Write a summary CSV.
  - Going back a step deletes later results, so a project file never mixes old patterns with new fits. [KNOWN: README "Data reduction workflow"]
- **What comes out:** the project file (HDF5-based) with patterns and fits, CSV summaries of peaks, strain and stress, and plots in the strain/stress viewer. [KNOWN: README, `pyrs/projectfile/`, `interface/strainstressviewer/`, sample CSVs in `docs/planning/`]
- **Where humans act:** an instrument scientist or user calibrates the detector, picks peaks and fit settings, and checks the results in the GUI. [KNOWN: `interface/detector_calibration`, `peak_fitting`, `texture_fitting`]
- **What it is not:** it isn't the generic Mantid framework (it uses Mantid's fitting), and it isn't for other instruments. [KNOWN: `calibration/mantid_peakfit_calibration.py`, `peaks/mantid_fit_peak.py`; INFERRED]
- **What's unknown:** whether the "pyRS 2.0" in the 2026 paper matches the v1.8.x tags, since the repo's versions don't say 2.0 yet. [UNKNOWN]
- **Example:** a 3D-printed metal column is scanned on HB2B, and PyRS turns the scans into a stress map. An ORNL OSTI record from 2026 covers neutron residual stress in additively manufactured columns, but I didn't confirm it used PyRS. [KNOWN: OSTI search list; UNKNOWN: the tie]

## How it works
- Modules:
  - `core/` handles the reduction engine.
  - `calibration/` handles detector calibration.
  - `peaks/` has fit engines with a fit factory.
  - `projectfile/` handles saving.
  - `dataobjects/` and `utilities/` are support code.
  - `interface/` holds the Qt GUI panels: manual reduction, combine runs, detector calibration, peak fitting, texture fitting, and the strain/stress viewer. [KNOWN: tree]
- The OSTI abstract lists the 2.0 upgrades: a calibration GUI with diagnostics, real-time reduction of live neutron event data, a new texture module, and better quality control. [KNOWN: OSTI abstract]

## How the project is organized
- Top level: `pyrs/`, `scripts/` (calibration and plotting scripts), `tests/`, `docs/` (user, developer, planning, `ground_truths.md`), `example/`, `pyproject.toml` and `pixi.lock`. [KNOWN: tree]
- Languages: Python 99.9%. Requires Python 3.12 or newer per `pyproject.toml`. The README's Pixi section still says 3.11, so the docs are slightly out of date. [KNOWN: GitHub languages API, pyproject.toml line 5, README; INFERRED: the out-of-date reading]
- Dependencies: Mantid and Mantid Workbench 6.16.x from the `mantid-ornl` conda channels, and PyQt. [KNOWN: pyproject.toml, README]
- CI: GitHub Actions (test and deploy, lockfile updates, a Grype security scan) and Codecov. [KNOWN: `.github/workflows/`]
- AI-assisted development: the repo includes a `CLAUDE.md` file of instructions for an AI coding assistant, and Copilot setup steps. The file says the project "is designed for scientists who may be new to software engineering". [KNOWN: `CLAUDE.md`, `.github/workflows/copilot-setup-steps.yml`]
- History: 3,332 commits, the first on 2018-03-19. By year there are 235 in 2018, 893 in 2019, 1,392 in 2020, 95 in 2021, 193 in 2022, 157 in 2023, 113 in 2024, 83 in 2025 and 171 in 2026 so far. 6 stars and 10 forks. [KNOWN: git log, GitHub API]
- Contributors: 33 including anonymous commit authors, 19 GitHub accounts. [KNOWN: GitHub API]

## Who uses it / why it matters
Residual stress is a big deal for welded and 3D-printed parts in energy, aerospace and defense. HB2B is one of the few places that measures it deep inside thick metal. PyRS is the software side of that capability. [INFERRED] The 2026 uptick in commits lines up with the 2.0 paper. [KNOWN: commit counts, OSTI date; INFERRED: the link] Usage evidence goes in `signals/pyrs.md` once it exists.

## Related projects
- Mantid (`mantid`): the fitting and data framework underneath. [KNOWN: pyproject.toml]
- SNAPRed (`snapred`): a sibling reduction tool for SNAP at SNS, with the same org and the same Pixi and Mantid setup. [KNOWN]
- Live data server (`live-data-server`): that brief notes an `hb2b` data type, which hints that HB2B results get posted there. [KNOWN per live-data-server brief; INFERRED: the tie]
- AM tools (`additivefoam`, `3dthesis`, `finch`): they predict the thermal history that creates residual stress, and PyRS measures it. No code tie. [INFERRED]

## Known / Inferred / Unknown
- KNOWN: license, OSTI record and abstract, dates, releases and tags, workflow steps, modules, dependencies, CI, AI-assistant files, counts.
- INFERRED: the physics explanations, the docs mismatch, the commit-paper link, the AM and live-data ties.
- UNKNOWN: how "pyRS 2.0" maps to repo versions, outside users.

## Sources (accessed 2026-10-24)
- https://github.com/neutrons/PyRS (README.rst, LICENSE, pyproject.toml, CLAUDE.md, pyrs/, docs/, .github/workflows/)
- https://api.github.com/repos/neutrons/PyRS (plus /languages, /releases, /contributors with and without anon=1)
- https://www.osti.gov/api/v1/records/17315105 (title, research org, abstract)
- https://neutrons-pyrs.readthedocs.io/en/latest/index.html (linked, not read in depth)
