# Myna
- Official page / Docs: https://ornl-mdf.github.io/Myna/ [KNOWN: GitHub API homepage]. The README also links ornl-mdf.github.io/myna-docs/ [KNOWN: README; the two links differ, which is minor].
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
- Paper: "Myna: Connecting powder bed fusion build data to simulation tools for digital twin applications", Computational Materials Science, https://doi.org/10.1016/j.commatsci.2025.114094 [KNOWN: CITATION.bib; paper not read].
- Org unit: the ORNL-MDF GitHub org [KNOWN]. The README ties it to "ORNL MDF" [KNOWN].
- The repo includes an AGENTS.md file for AI coding agents [KNOWN: repo root]. It's a small sign of how the team works.

## Who uses it / why it matters
- Metal 3D-printing researchers who want to predict defects and material properties of a specific printed part instead of a generic one [INFERRED: purpose plus the example cases].
- Matters for aerospace and energy parts made by additive manufacturing [INFERRED: general context].

## Related projects
- Wraps AdditiveFOAM, which is in the catalog [KNOWN: application/additivefoam].
- Wraps 3DThesis, which is in the catalog [KNOWN: application/thesis; matching it to the 3dthesis row is INFERRED].
- ExaCA and adamantine are likely other ORNL codes not yet in the catalog [INFERRED].
- Uses Peregrine, the ORNL MDF monitoring tool [KNOWN: README].

## Known / Inferred / Unknown
- [KNOWN] BSD-3, Python, config/run/sync workflow, the wrapped tools, Peregrine origin, two releases, and the paper.
- [INFERRED] The target users, and ExaCA/adamantine being ORNL codes.
- [UNKNOWN] Whether Peregrine itself is public, and how widely Myna is used outside ORNL.

## Sources (URL, accessed date)
- https://github.com/ORNL-MDF/Myna (README, ARCHITECTURE.md, CHANGELOG.md, CITATION.bib, LICENSE.md, application readme), accessed 2026-10-24
- https://api.github.com/repos/ORNL-MDF/Myna (+ /languages, /releases, /contributors), accessed 2026-10-24

## Fact-check notes (ORNL Fact Checker, 2026-10-24)
- Corrected: MDF retagged KNOWN via the ornl.gov facility page.
- Added: DOE CODE record code-141169 (Myna, ORNL) via the OSTI records API.
- Verified: BSD-3 copyright 2024 ORNL; releases 1.0.0 (2024-08-19) and 1.1.0 (2025-04-09); created 2024-02-23; Python 99.0%; 9 contributor pages; Python 3.10+ and not on PyPI; config/run/sync in ARCHITECTURE.md; application folders (adamantine, additivefoam, bnpy, cubit, deer, exaca, openfoam, rve, thesis); CHANGELOG database types and 3.9 baseline; seven-author CITATION.bib; 21 example cases; AGENTS.md present.
