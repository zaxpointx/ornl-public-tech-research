# Mind the Gap
- Repo: https://github.com/ORNL/mind_the_gap [KNOWN]
- DOE CODE: code-152916, "ORNL/mind_the_gap", DOI 10.11578/dc.20250320.1. Research org ORNL, sponsor the National Geospatial-Intelligence Agency. [KNOWN: OSTI API record code-152916, accessed 2026-10-24]
- Docs: README only (the dependencies include Sphinx, but no docs folder is published) [KNOWN: tree, pyproject.toml]
- License: UT-Battelle open source license, "Copyright © 2025, UT-Battelle, LLC". GitHub shows NOASSERTION. [KNOWN: LICENSE.txt, GitHub API]
- Status: unknown (rule 14 has no "active-ish"; not archived, but main has been quiet since April 2025). v1.0.0 in pyproject.toml, last commit on main 2025-04-09, last push 2025-08-05 (other branches). [KNOWN: git log, GitHub API]
- ORNL relationship: KNOWN. It's in the main ORNL GitHub org, with UT-Battelle copyright and an OSTI record naming ORNL. [KNOWN]
- Years visible in public sources: 2022 to 2025
- Last checked: 2026-10-24

## Walkthrough (plain language)
- **What it is:** a Python algorithm that finds holes in building-footprint maps, meaning places where buildings are missing from the data, not from the ground. [KNOWN: README, OSTI description]
- **Key terms:**
  - **Building footprint:** the outline of a building as seen from above, usually traced from satellite images by people or by machine learning.
  - **Imagery tile:** satellite images come in square tiles. If a tile is missing or cloudy, every building in that square goes missing too, which leaves a rectangular hole. [KNOWN: README "rectangular-shaped gaps caused by missing imagery tiles"; INFERRED: the cloud example]
  - **Centroid:** the center point of a shape. The tool can work on centroids alone. [KNOWN: README]
  - **AOI:** area of interest, the boundary you're checking. [KNOWN: README]
  - **GeoPandas:** a Python library for map data in tables. [KNOWN: README, pyproject.toml]
- **The problem:** big footprint datasets cover whole countries, and missing tiles create holes that look like empty land. Population or energy models built on them would undercount. [KNOWN: README purpose; INFERRED: the downstream harm]
- **What goes in:** building footprints or their centroids, plus the AOI boundary. [KNOWN: README "Inputs"]
- **What happens:**
  1. Points get dropped into thin north-south and east-west strips (`into_the_bins`).
  2. In each strip the tool looks for long empty stretches, which are candidate gap lines (`find_lat_gaps`, `find_lon_gaps`).
  3. It keeps places where horizontal and vertical gap lines cross, because a real missing tile leaves both (`find_intersections`, `intersection_filter`).
  4. It groups crossing lines into clusters (`find_clusters`, which walks connected gaps with an inner `take_a_walk` helper).
  5. It wraps each cluster in a polygon using an "alpha shape", a tight outline around a set of points (`generate_alpha_polygons`).
  [KNOWN: function names in `mind_the_gap/mind_the_gap.py`; INFERRED: the plain-English reading of each step]
  - `chainage.py` puts evenly spaced points along the boundary so the edge of the area doesn't read as a gap. [KNOWN: module docstring; INFERRED: why]
  - `auto_tune.py` builds a grid over the area (`make_grid`), runs the detector with different settings, and scores each run (`fit_check`), with a parallel option, so you don't have to guess the parameters. [KNOWN: method names in `auto_tune.py`; INFERRED: the plain reading of the scoring]
- **What comes out:** gap polygons as a GeoDataFrame, a map-data table. [KNOWN: README "Outputs"]
- **Where humans act:** an analyst picks the area, optionally tunes the settings, and decides what to do about each gap, such as re-running detection or using other imagery. [INFERRED]
- **What it is not:** it doesn't detect buildings or fill gaps. It only flags where data is missing. [KNOWN: README; INFERRED: "doesn't fill"]
- **What's unknown:** which footprint dataset it was built for. The test data includes a Slovakia boundary, which suggests country-scale testing. [KNOWN: `tests/data/slovakia_bound.gpkg`; UNKNOWN: the production dataset]
- **Example:** run it over a country's footprints, and a square of farmland with no buildings in one strip gets flagged where a whole imagery tile was skipped. [INFERRED from the README purpose]

## What it is (plain English, 2-4 sentences)
A quality-control tool for building maps. It looks for the rectangular blank spots that missing satellite tiles leave behind, and it can tune itself to the dataset. [KNOWN: README]

## How it works (plain English, no jargon without definition)
See the walkthrough steps. Dependencies: geopandas, shapely, libpysal (spatial statistics), numba (a compiler that speeds up Python loops), rtree (spatial indexing), plus psycopg2 and geoalchemy for reading from a PostGIS database. [KNOWN: pyproject.toml; INFERRED: what each is for]

## How the project is organized
- Language: Python 3.10 or newer, packaged with Poetry, plus a Dockerfile and requirements.txt. [KNOWN: pyproject.toml, tree]
- Layout: `mind_the_gap/` (`mind_the_gap.py`, `chainage.py`, `auto_tune.py`) and `tests/` (pytest, with reference `.gpkg` map files). [KNOWN: tree]
- Tests: a GitHub Actions workflow (`testing.yml`) runs on Ubuntu with Python 3.10. [KNOWN: `.github/workflows/testing.yml`]
- Branches: a branch named for preparing a PyPI release exists, but there's no PyPI package that we checked. [KNOWN: branch list; UNKNOWN: PyPI]
- Contributors: 6 including anonymous authors, 1 account, and 5 distinct git author emails. 8 stars, 1 fork, 4 open issues. [KNOWN: GitHub API, git log]
- No CONTRIBUTING file. [KNOWN: tree]
- Why binning and alpha shapes rather than other methods: [UNKNOWN; not stated]

## Timeline
| Date | Event | Source | Tag |
|---|---|---|---|
| 2022-10-11 | Earliest commits in the history (renames to snake_case) | git log | KNOWN |
| 2022 to 2025 | 21, 126, 194, then 72 commits per year | git log | KNOWN |
| 2025-03-20 | Public GitHub repo created; OSTI code-152916 dated the same day | GitHub API, OSTI | KNOWN |
| 2025-04-09 | Last commit on main (boundary chainage feature merged) | git log | KNOWN |
| 2025-08-05 | Last push (another branch) | GitHub API | KNOWN |

The history starts more than two years before the public repo existed, so the code was probably developed somewhere private and published with its history. [INFERRED from the dates; we don't speculate about where (rule 16)]

## Who uses it / why it matters
- Builders of footprint datasets, and anyone using them for population, energy or disaster models. [INFERRED] No public users found. [UNKNOWN]

## Related projects
Filled by the connections pass, matching connections/map.md.
| Related item | Relationship (uses, extends, shares data, same facility, related topic, unknown) | Source | Tag |
|---|---|---|---|
| Vivaldi | related topic (ML on building datasets; different contributors) | map link 48 | INFERRED |
| National Geospatial-Intelligence Agency | sponsor | map link 201; https://www.osti.gov/api/v1/records/code-152916 | KNOWN |

## What stands out
- It's a small, honest tool about data quality. Building maps have blind spots, and someone wrote code just to find them. [INFERRED]
- The sponsor is a defense mapping agency, not DOE. That shows ORNL's geospatial group works for other federal agencies. We note the public sponsor field only and don't guess at the agency's uses (rule 16). [KNOWN: OSTI; INFERRED: the lesson]
- The public repo and the software record carry the same date, so publishing went through the DOE CODE release path in one step. [KNOWN: dates; INFERRED: the process]

## Ten questions (GOAL.md)
1. **Problem and for whom:** finding missing-tile holes in building-footprint datasets, for the people who build or use those datasets. [KNOWN: README]
2. **Where in the tree:** ORNL, then geospatial science (with Gauntlet, Vivaldi, LandScan and USA Structures as neighbors). [KNOWN: ORNL org and OSTI; INFERRED: the neighborhood]
3. **Who pays:** the National Geospatial-Intelligence Agency, per code-152916. [KNOWN]
4. **Organized how:** one Python package with three modules, Poetry, a Dockerfile, pytest, and tests in GitHub Actions. [KNOWN]
5. **Alive?** It was busy in 2023-24, the main branch has been quiet since April 2025, and it's at v1.0.0. [KNOWN]
6. **Outside users:** none found. 8 stars and 1 fork. [KNOWN; UNKNOWN]
7. **Connections:** upstream are footprint datasets. Downstream would be models that use them. Neighbors are the ORNL building tools. [INFERRED]
8. **What it teaches about ORNL:** the geospatial group takes work from non-DOE agencies, and data quality gets its own software. [KNOWN: sponsor; INFERRED]
9. **Student angle:** very readable. The core algorithm is one 941-line file (`mind_the_gap.py`), with two small helpers (`auto_tune.py`, `chainage.py`) and clear function names, plus real tests and CI. You'd need Python and GeoPandas, and you could make your own test data from free OpenStreetMap buildings. [KNOWN: tree; INFERRED: the OpenStreetMap idea] There's no CONTRIBUTING file, and GitHub shows 4 open issues and pull requests combined.
10. **Unknown and searched without result:** a paper describing it (OSTI search "mind the gap building footprint" found only the code record), PyPI release, outside users.

## Known / Inferred / Unknown
- [KNOWN] purpose, inputs and outputs, module layout, sponsor, license, history, CI.
- [INFERRED] the plain reading of each algorithm step, pre-publication history, the neighborhood.
- [UNKNOWN] the production dataset, users, paper.

## Verification notes
_Filled by the fact-check pass._

## Sources (accessed 2026-10-24)
- https://github.com/ORNL/mind_the_gap (README.md, LICENSE.txt, pyproject.toml, `mind_the_gap/*.py`, `.github/workflows/testing.yml`, `tests/data/`)
- https://api.github.com/repos/ORNL/mind_the_gap (and /contributors)
- https://www.osti.gov/api/v1/records/code-152916

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Verified: code-152916 (NGA sponsor, ORNL, DOI, 2025-03-20), repo created the same day, last main commit 2025-04-09, last push 2025-08-05, stars/forks, UT-Battelle license, testing.yml CI.
- Corrected: status set to unknown (a rule 14 value); the "single file" line now names the two helper modules; open count noted as issues plus PRs.
