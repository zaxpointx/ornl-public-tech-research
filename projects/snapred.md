# SNAPRed
- Official docs: https://snapred.readthedocs.io/en/latest/ (Read the Docs). The front page notes "This project is under active development." [KNOWN: README, docs index]
- Repo: https://github.com/neutrons/SNAPRed (default branch `next`). GitHub's description is "A desktop application for Lifecycle Managment of data collected from the SNAP instrument." [KNOWN: GitHub API]
- License: GPL-3.0, per the LICENSE file and the GitHub API. The file is the standard GPL text and doesn't name a project copyright holder. [KNOWN: LICENSE, GitHub API]
- Status: active (rule 14).
  - The last commit was 2026-10-19 10:48 ET, and it isn't archived. [KNOWN: git log, GitHub API]
  - GitHub Releases stop at v2.0.0 (2025-09-16). The git tags go further: v2.3.0 and v2.3.1 were both tagged 2026-04-07, and there's an experimental `v2.4.0exp1-cycle-aware-calib` tag. [KNOWN: GitHub API, git tags]
- Scope (rule 13): CORROBORATED.
  - OSTI 3012509, "SNAPRed: Reduction of multidimensional neutron time-of-flight diffraction data", is a SoftwareX journal article (2025-12-08, DOI 10.1016/j.softx.2025.102464).
  - It lists "Research Org.: Oak Ridge National Laboratory (ORNL)" and its sponsor is DOE Office of Science, Basic Energy Sciences, Scientific User Facilities.
  - Its abstract describes SNAP as a diffractometer "at the Spallation Neutron Source operated by Oak Ridge National Laboratory". [KNOWN: https://www.osti.gov/api/v1/records/3012509, accessed 2026-10-24]
  - This replaces the catalog's earlier "OSTI: no hits" note. The record exists and turned up on a fresh search.
- Org unit: the `neutrons` GitHub org, which is the same org as Mantid-related ORNL tools in the catalog. [INFERRED: the SNS/HFIR software group; no division named]

## Plain-language walkthrough
- **What it is:** a Python desktop program for scientists using SNAP, a neutron diffraction instrument at ORNL's Spallation Neutron Source (SNS). It turns raw detector data into clean diffraction patterns and manages the calibration steps that make the patterns trustworthy. [KNOWN: description, OSTI abstract]
- **Key terms:**
  - *Neutron diffraction* means firing neutrons at a material and recording where they bounce. The pattern reveals how the atoms are arranged.
  - *Time-of-flight* means telling neutron energies apart by how long each one takes to arrive.
  - *Data reduction* is the cleanup that turns millions of raw detector "events" into a usable pattern.
  - *Calibration* means measuring known reference samples so you can correct for exactly how the detectors sit.
  - A *vanadium* run is a standard reference measurement used to normalize the data. [KNOWN: OSTI abstract mentions detection events and reduction, recipe names such as `GenerateFocussedVanadiumRecipe`, `PixelDiffCalRecipe`; INFERRED: the explanations]
- **The problem:** SNAP's detectors can be moved and reconfigured between experiments, so the right calibration depends on the instrument's "state". The datasets are also huge. The OSTI abstract says SNAPRed orchestrates reduction "while automatically managing the variable neutron instrumentation configuration". [KNOWN: OSTI abstract; `StateIdLookupService.py`]
- **What goes in:** raw SNAP event data for a run, plus calibrant and vanadium runs, crystallographic info about the reference samples, and pixel grouping and masking choices. [KNOWN: service and recipe names such as `CalibrantSampleService`, `CrystallographicInfoService`, `GroupingService`; OSTI abstract on grouping and masking]
- **What happens:**
  1. The program works out which instrument state the run belongs to.
  2. It loads the matching calibration, or helps the user make one (pixel-level, then group-level "diffraction calibration").
  3. It normalizes with vanadium.
  4. It reduces the run into focused diffraction patterns.
  - The heavy math runs through Mantid, the big neutron-data framework. [KNOWN: recipe and service names, Mantid dependency in `pyproject.toml`; INFERRED: the order]
- **What comes out:** reduced diffraction patterns plus saved calibration and normalization records with metadata, and calibration quality metrics. [KNOWN: `GenerateCalibrationMetricsWorkspaceRecipe`, `WriteWorkspaceMetadata`; INFERRED]
- **Where humans act:** an instrument scientist or visiting user works through GUI workflows (`ui/` with handler, model, presenter and plotting folders) to approve calibrations and pick settings. [KNOWN: tree; INFERRED: who]
- **What it is not:** it isn't Mantid (it depends on it), and it isn't a general tool for every instrument. It's built around SNAP's settings in `application.yml`. [KNOWN: docs usage page]
- **What's unknown:** why GitHub Releases stopped at v2.0.0 while tags kept going.
- **Example:** a high-pressure study on SNAP. Several OSTI records from 2025-2026 on high-pressure materials (such as cerium and pyrazine) come up alongside it in searches, though I didn't check whether they used SNAPRed. [KNOWN: OSTI search list; UNKNOWN: the tie]

## How it works
- The backend uses a kitchen metaphor:
  - "Recipes" (`backend/recipe/`) are single processing steps.
  - "Services" (`backend/service/`) put them together, with a `SousChef` service doing prep.
  - "FetchGroceries" loads the input data.
  - `dao/` (data access) handles saving and loading. [KNOWN: file names; INFERRED: the roles]
- The GUI follows a model-view-presenter layout. [KNOWN: `ui/model`, `ui/presenter`, `ui/handler`; INFERRED: the pattern name]
- The docs say the test data lives in a separate repo pulled in as a git submodule with Git LFS. That repo is on an ORNL-hosted GitLab, which I didn't follow (rule 16). [KNOWN: docs usage page]

## How the project is organized
- Top level: `src/snapred/` (backend, ui, meta, resources), `tests/`, `docs/` (Sphinx), `pyproject.toml` (hatchling build with versioningit), and `pixi.lock` (Pixi, a conda-style environment manager). [KNOWN: tree]
- Languages: Python 100%. Requires Python 3.10 or newer. [KNOWN: GitHub languages API, pyproject.toml]
- Dependencies: Mantid and Mantid Workbench 6.16 or newer, from ORNL-specific conda channels (`mantid-ornl`) for QA and production builds. [KNOWN: pyproject.toml lines 144-149 and 285-304]
- CI: GitHub Actions (unittest, docs, package, automerge), Codecov coverage, and an OpenSSF (CII) Best Practices badge. [KNOWN: workflows, README badges]
- History: 889 commits, the first on 2022-12-19 UTC. Created 2023-04-04. By year there are 4 in 2022, 281 in 2023, 412 in 2024, 156 in 2025 and 36 in 2026. 2 stars and 4 forks. [KNOWN: git log, GitHub API]
- Contributors: 20 including anonymous commit authors, 14 GitHub accounts. [KNOWN: GitHub API]

## Who uses it / why it matters
Facility users get beam time for only a few days, so turning raw data into results quickly and correctly is the bottleneck. SNAPRed is how SNAP tries to make that self-service. [INFERRED] Having a SoftwareX paper means it's presented as finished enough to cite. [KNOWN: OSTI record; INFERRED] Usage evidence goes in `signals/snapred.md` once it exists.

## Related projects
- Mantid (`mantid`): the computing engine underneath. [KNOWN: pyproject.toml]
- PyRS (`pyrs`): a sibling reduction tool for a different instrument (HB2B at HFIR), in the same org with the same Pixi and Mantid setup. [KNOWN: both repos]
- Post-processing agent and data-workflow (`post-processing-agent`, `data-workflow`): other `neutrons` org tools in the catalog. A direct tie isn't shown. [UNKNOWN]

## Known / Inferred / Unknown
- KNOWN: license, OSTI record and abstract, sponsor, dates, tags vs. releases, layout, dependencies, CI, counts.
- INFERRED: the physics explanations, the processing order, the kitchen-metaphor roles, the org unit.
- UNKNOWN: why GitHub Releases lag the tags, and who uses it beyond SNAP staff and users.

## Sources (accessed 2026-10-24)
- https://github.com/neutrons/SNAPRed (README.md, LICENSE, pyproject.toml, src/snapred/, docs/source/index.rst and usage.rst, .github/workflows/)
- https://api.github.com/repos/neutrons/SNAPRed (plus /languages, /releases, /contributors with and without anon=1)
- https://www.osti.gov/api/v1/records/3012509 (title, research org, sponsor, abstract)
- https://snapred.readthedocs.io/en/latest/ (linked docs, front page)

## GOAL.md questions (added 2026-10-24)
- **Who pays (Q3):** DOE Office of Science, Basic Energy Sciences, Scientific User Facilities. [KNOWN: OSTI 3012509]
- **Where in the tree (Q2):** ORNL, then the Spallation Neutron Source (a user facility), then the SNAP instrument. [KNOWN: OSTI abstract] It belongs with the SNS neutron data pipeline deep dive. [INFERRED]
- **What it teaches about ORNL (Q8):** user facilities build instrument-specific apps on top of a shared engine (Mantid) and ship them through the lab's own conda channels with QA and production builds. That's an in-house release pipeline. [KNOWN: pyproject.toml channels; INFERRED: the pattern]
- **Student angle (Q9):** there's no CONTRIBUTING file and no good-first-issue labels (15 open issues and PRs). The Sphinx docs do have a developer section covering architecture, implementation notes and deploy. [KNOWN: tree, GitHub API, accessed 2026-10-24] It's a good read for a Python student: clean layering, a GUI built on model-view-presenter, and unit tests in CI. Real contributions would need Mantid and test data hosted off GitHub. [INFERRED; docs usage page]
- **Searched without result (Q10):** why GitHub Releases stop at v2.0.0, and outside users.

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Verified on a fresh clone of neutrons/SNAPRed and public records: GPL-3.0 LICENSE, default branch `next`, last commit 2026-10-19 10:48 ET, 889 commits, first 2022-12-19, tags through v2.3.1 plus `v2.4.0exp1-cycle-aware-calib`, four workflows, Python 3.10+, contributors 20 with anonymous and 14 accounts. OSTI 3012509 refetched: title, 2025-12-08, DOI 10.1016/j.softx.2025.102464, ORNL research org, BES Scientific User Facilities sponsor. Docs link resolves.
- No corrections. Per-year counts differ by one commit at the 2023 and 2026 edges depending on time zone (my clone gives 282 and 35), which doesn't change anything.
