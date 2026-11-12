# Myna
- Official page / Docs: https://ornl-mdf.github.io/Myna/ [KNOWN: GitHub API homepage]. The README shows the text ornl-mdf.github.io/myna-docs/ but its link goes to /Myna/, and a separate getting-started link uses the myna-docs address; that address returned 404 on 2026-10-29, so /Myna/ is the working docs site. [KNOWN: README lines 9 and 30; HTTP check] (corrected in a fact-check pass, 2026-10-29)
- Repo: https://github.com/ORNL-MDF/Myna
- License: BSD 3-Clause, copyright 2024 Oak Ridge National Laboratory [KNOWN: LICENSE.md, https://github.com/ORNL-MDF/Myna/blob/main/LICENSE.md]
- Status: active, last push 2026-10-13 [KNOWN: GitHub API]. The README warns that ongoing development may change directory layouts and outputs [KNOWN].

## What it is (plain English, 2-4 sentences)
Myna is a Python tool that connects real 3D-printing build records to computer simulations of that print [KNOWN: README, ARCHITECTURE.md]. It targets metal "powder bed fusion" printing, where a laser melts thin layers of metal powder one at a time [KNOWN: paper title in CITATION.bib names powder bed fusion; process description is general background]. Myna reads what actually happened during a build from a database and automatically sets up and runs a chain of simulations, for example temperature, then melt pool shape, then the metal's microscopic grain structure. The goal is "digital twins", virtual copies of a real printed part [KNOWN: paper title "...for digital twin applications"].

## How it works (plain English, no jargon without definition)
- You write a workflow input file (YAML, a simple config format) listing the steps you want [KNOWN: ARCHITECTURE.md].
- `myna config` pulls the needed metadata (build, part, layer) out of the build database and creates a folder for each simulation case. `myna run` executes each step, and `myna sync` pushes results back into the database [KNOWN: ARCHITECTURE.md].
- Each step calls an outside simulation code through a wrapper with three stages: configure, execute and postprocess [KNOWN: src/myna/application/readme.md]. Wrapped tools include AdditiveFOAM, OpenFOAM, ExaCA (grain-growth simulation), adamantine, 3DThesis ("thesis"), Cubit (meshing) and others [KNOWN: application folder names; ExaCA gloss INFERRED].
- It was first built around the database format of Peregrine, ORNL MDF's software for monitoring powder bed prints [KNOWN: README]. Version 1.1.0 added the MynaJSON, PeregrineHDF5 and AMBench2022 database types [KNOWN: CHANGELOG]. MDF is ORNL's Manufacturing Demonstration Facility [KNOWN: https://www.ornl.gov/facility/mdf, accessed 2026-10-24].

## How the project is organized (repo structure, languages, build, maintainers/org unit, release cadence)
- Languages: about 99% Python [KNOWN: GitHub languages API]. Requires Python 3.10 or newer [KNOWN: README]. The 1.1.0 changelog mentions a 3.9 baseline, so the minimum version has moved up since [KNOWN: CHANGELOG].
- `src/myna/` has `core` (workflow engine, components, file types, metadata), `application` (tool wrappers), `database` (database readers), `cli` and packaged material data. The repo also has `tests/` (pytest), `examples/cases/` (about 20 runnable cases such as melt_pool_geometry_part and microstructure_region), `examples/databases/` and `docs/` (MkDocs) [KNOWN: repo tree, ARCHITECTURE.md].
- Build: `pyproject.toml` plus a `uv.lock` lockfile, using uv (a fast Python package manager) or pip. It isn't on PyPI yet [KNOWN: README].
- Releases: 1.0.0 (2024-08-19) and 1.1.0 (2025-04-09) [KNOWN: GitHub releases API]. The repo was created 2024-02-23 [KNOWN].
- Contributors: about 9 per the GitHub API, counting anonymous ones [KNOWN]. The paper has seven authors [KNOWN: CITATION.bib].
- Paper: "Myna: Connecting powder bed fusion build data to simulation tools for digital twin applications", Computational Materials Science, https://doi.org/10.1016/j.commatsci.2025.114094. [KNOWN: [manuscript](https://www.osti.gov/pages/servlets/purl/3002570), accessed 2026-11-07; details Y01 in ../docs/public-research-sources.md]
- Org unit: the ORNL-MDF GitHub org [KNOWN]. The README ties it to "ORNL MDF" [KNOWN].
- The repo includes an AGENTS.md file for AI coding agents [KNOWN: repo root]. It's a small sign of how the team works.

## Who uses it / why it matters
**Research update, 2026-11-07:** The 2025 paper uses Myna v1.1 and the public Peregrine v2023-10 dataset for 54 3DThesis, 78 AdditiveFOAM and three ExaCA simulations. The authors manually chose regions, then compared simulated grain structure with electron backscatter diffraction measurements. Their simulated trends differed from the limited variation observed in the measured parts; a proposed two-phase explanation needs further testing. The paper credits Gerald Knapp, Samuel Reeve, John Coleman, Matthew Rolchigo, Benjamin Stump, Stephen DeWitt and Alex Plotkowski as authors, not necessarily current project leads. [KNOWN: Y01; accessed 2026-11-07]
- Metal 3D-printing researchers who want to predict defects and material properties of a specific printed part instead of a generic one [INFERRED: purpose plus the example cases].
- Matters for aerospace and energy parts made by additive manufacturing [INFERRED: general context].

## Related projects
- Wraps AdditiveFOAM, which is in the catalog [KNOWN: application/additivefoam].
- Wraps 3DThesis, which is in the catalog [KNOWN: application/thesis; matching it to the 3dthesis row is INFERRED].
- ExaCA is an LLNL-hosted external project in the map; adamantine has its own [catalog brief](adamantine.md) supported by an ORNL publication record. Both have Myna wrappers, but adamantine was not identified as part of the particular 2025 Myna experiment. [KNOWN: Y01, X06; project briefs]
- Uses Peregrine, the ORNL MDF monitoring tool [KNOWN: README].

## Known / Inferred / Unknown
- [KNOWN] BSD-3, Python, config/run/sync workflow, the wrapped tools, Peregrine origin, two releases, and the paper.
- [INFERRED] The target users. The earlier inference that ExaCA was an ORNL catalog code is superseded: its DOE CODE record lists LLNL; adamantine is in the ORNL catalog on its publication record. [KNOWN: X06; adamantine brief]
- [UNKNOWN] Whether Peregrine itself is public, and how widely Myna is used outside ORNL.

## Sources (URL, accessed date)
- https://github.com/ORNL-MDF/Myna (README, ARCHITECTURE.md, CHANGELOG.md, CITATION.bib, LICENSE.md, application readme), accessed 2026-10-24
- https://api.github.com/repos/ORNL-MDF/Myna (+ /languages, /releases, /contributors), accessed 2026-10-24

## Fact-check notes (2026-10-24)
- Corrected: MDF retagged KNOWN via the ornl.gov facility page.
- Added: DOE CODE record code-141169 (Myna, ORNL) via the OSTI records API.
- Verified: BSD-3 copyright 2024 ORNL; releases 1.0.0 (2024-08-19) and 1.1.0 (2025-04-09); created 2024-02-23; Python 99.0%; 9 contributor pages; Python 3.10+ and not on PyPI; config/run/sync in ARCHITECTURE.md; application folders (adamantine, additivefoam, bnpy, cubit, deer, exaca, openfoam, rve, thesis); CHANGELOG database types and 3.9 baseline; seven-author CITATION.bib; 21 example cases; AGENTS.md present.

## GOAL.md questions (added 2026-10-24)
- **Who pays (Q3):** DOE CODE code-141169 lists the Office of Science, and other Myna records add EERE and Nuclear Energy once each (see `signals/myna.md`). [KNOWN: OSTI API]
- **Where in the tree (Q2):** ORNL, then additive manufacturing, then the Manufacturing Demonstration Facility (ORNL-MDF org, Peregrine database). It sits at the top of the 3D-printing ladder and drives 3DThesis, AdditiveFOAM, ExaCA and others. [KNOWN per map; INFERRED: the ladder framing]
- **What it teaches about ORNL (Q8):** when several labs' physics codes exist, someone builds the glue that runs them in sequence on real build data, and that glue is where a facility's data meets the simulations. [INFERRED]
- **Student angle (Q9):** it has a CONTRIBUTING.md and docs deployed from CI. [KNOWN: tree, `.github/workflows/`] It's Python workflow code, the most approachable entry into the ladder for a Python student. [INFERRED]
- **Searched without result (Q10):** see this brief's unknowns and `verification/not-found.md`.

### Second pass (2026-10-29)
Skeptical reread of the riskiest claims against sources not leaned on before (a fresh clone, GitHub API, live pages). Earlier 2026-10-24 fixes checked and still hold.
- License BSD-3, 2024 ORNL: fresh clone and GitHub API. Verified.
- Releases 1.0.0 (2024-08-19) and 1.1.0 (2025-04-09): API publish dates and clone tags. Verified.
- "About 9 contributors per the GitHub API": API returns 9 (accounts, incl. anonymous). Git history shows 13 distinct author names on the default branch because some people commit under more than one name. Verified, with the method noted.
- Docs links: corrected. The myna-docs address now returns 404; the README's main docs link actually points to /Myna/, which works.
- Commit spot check (Rule 17): default branch `main` 477 commits, all branches 540; first commit 2023-05-11, before the 2024-02-23 repo creation, so history was imported; last commit 2026-10-28 (author and committer).
