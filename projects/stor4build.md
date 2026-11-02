# Stor4Build

- Official page: DOE CODE record https://www.osti.gov/doecode/biblio/170060 (DOI 10.11578/dc.20251112.1, 2025-11-11, ORNL and NREL, sponsor EERE Building Technologies Office) [KNOWN: DOE CODE, accessed 2026-10-24]
- Repo: https://github.com/Stor4Build/stor4build (a side org; qualifies under RULES 13 via the DOE CODE record and the UT-Battelle copyright) [KNOWN]
- Docs: README, `docs/` (notebook demo, control demo, Ubuntu setup note), PyPI page https://pypi.org/project/stor4build [KNOWN]
- License: BSD-3-Clause. Copyright is shared by UT-Battelle (ORNL), the Alliance for Energy Innovation and contributors. [KNOWN: `LICENSE.txt`] The Alliance runs NREL. [INFERRED: matches the DOE CODE co-lab]
- Status: active (v1.0.0 tag 2026-09-30, last push 2026-10-13) [KNOWN: GitHub, accessed 2026-10-24]

## Walkthrough
Stor4Build asks one question: if a building makes ice at night and melts it to cool itself in the afternoon, how much does that cut its peak power use? [KNOWN: README "About", paraphrased]
The problem: air conditioning drives summer peak demand, and peak power is the most expensive power for both utilities and building owners. Thermal energy storage (TES) moves the cooling work to cheaper, off-peak hours. [KNOWN: README says it studies shifting cooling loads and cutting peak demand]
What goes in: a standard DOE prototype building model (24 `.osm` files ship in `models/`, covering offices, schools, retail and so on), a weather file, and settings such as the tank size and when to discharge it. [KNOWN: `models/`, `weather/`, CLI options]
What happens: OpenStudio measures (small scripts that edit a building model) add an ice tank or a packaged ice-storage unit. EnergyPlus, DOE's building physics simulator, then runs the year hour by hour. [KNOWN: `measures/`, `run.py`]
What comes out: CSV results to compare against the no-storage baseline. [KNOWN: README; sample `output-*.csv` files]
Where humans act: picking the building, climate, tank size and control strategy, and reading the comparison. [INFERRED]
What it is not: not a controller for a real building, and not a hardware design tool. It's simulation only. [KNOWN: README describes modeling and simulation]
Example: `stor4build size-icetank` sizes an ice tank from the baseline model and a chosen discharge window (say noon to 6 pm), then the run shows how much afternoon chiller power drops. (The command is from the README; the noon-to-6 window matches the repo's `add_demo_noon_to_six` measure.)
Unknown: which outside studies have used it so far.

## What it is (plain English, 2-4 sentences)
A Python package, command line tool and small web API for testing building-integrated thermal energy storage in simulation. It wraps OpenStudio and EnergyPlus so a study can be rerun from JSON inputs and CSV outputs. [KNOWN: README "About"] ORNL and NREL built it for DOE's Building Technologies Office. [KNOWN: DOE CODE]

## How it works (plain English, no jargon without definition)
1. Pick a baseline: a DOE prototype building (`models/`, or `create_DOE_prototype_building` measure) and weather. [KNOWN]
2. Add storage: measures such as `add_central_ice_storage`, `add_packaged_ice_storage` and `add_pytank` change the model. The `pytank` path uses an EnergyPlus Python plugin (`plugins/thermaltank`) to model the tank. [KNOWN: `measures/`, `plugins/`]
3. Control: plugins in `plugins/controls` and `dynamic_charge_controls.py` decide when the tank charges and discharges. [KNOWN: file names]
4. Run: `run.py` finds the `openstudio` program on the computer and runs the workflow as a subprocess. It raises an error if OpenStudio isn't installed. [KNOWN: `src/stor4build/run.py` lines 9-26]
5. Compare: CSV outputs versus baseline. [KNOWN: README]
6. Optional web API: Flask (a small Python web framework) serves runs, but it needs a PostgreSQL/Timescale database of baseline models and weather, set through `FLASK_TIMESCALE_*` variables. The README says that setup "is not described here yet". [KNOWN: README "Web API", short quote]

## How the project is organized
- Layout: `src/stor4build/` (`cli/`, `api/`, `icetank.py`, `dxcoil.py`, `system.py`, `run.py`, `database.py`, `schema.py`), `measures/` (19 OpenStudio measures), `plugins/`, `models/` (24 prototypes), `weather/`, `schema/`, `examples/examples.json`, `regression_tests/` (golden CSV results to compare against), `tests/`, `docs/`. [KNOWN: repo tree]
- Languages and build: Python 3.8 or newer, packaged with Hatch. Dependencies include click, flask, scipy, pandas, marshmallow, matplotlib, psycopg2-binary and SecondaryCoolantProps (fluid properties for the chilled-water loop). OpenStudio measures are Ruby. [KNOWN: `pyproject.toml`; measures as OpenStudio requires]
- Outside tools needed: OpenStudio 3.11 (required as of 1.0.0), which supports EnergyPlus 25.2 and Python 3.12. CI runs on Ubuntu 24.04. [KNOWN: `docs/source/installation.md`; `.github/workflows/tests.yml`] (corrected in a fact-check pass, 2026-10-29)
- CI: `tests.yml` across Python 3.8-3.13, and `python-publish.yml` to PyPI. [KNOWN: `.github/workflows/`]
- Contributors: 3 accounts. 1 star, 1 fork, 8 open issues. [KNOWN: GitHub API, 2026-10-24]
- Coverage: a README table marks which prototypes work with each storage type, with some still "TBD". [KNOWN: README "Prototype Coverage"]
- Why it was built this way: UNKNOWN.

## Timeline
| Date | Event | Source | Tag |
|---|---|---|---|
| 2024-02-23 | earliest commit in history (repo itself created later, so history was imported) | git log; GitHub API | [KNOWN]; import [INFERRED] |
| 2024-09-10 | v0.1.0 tag | GitHub tags | [KNOWN] |
| 2025-10-20 | public GitHub repo created | GitHub API | [KNOWN] |
| 2025-11-11 | DOE CODE record, DOI 10.11578/dc.20251112.1 | https://www.osti.gov/doecode/biblio/170060 | [KNOWN] |
| 2025-11-16 | first PyPI release, 0.3.0 | https://pypi.org/project/stor4build/#history | [KNOWN] |
| 2026-09-30 / 2026-10-01 | v1.0.0 tag, then PyPI 1.0.0 | GitHub; PyPI | [KNOWN] |

Commits per year: 109 in 2024, 119 in 2025, 90 in 2026 so far, by committer date. By author date: 109, 136 and 114. [KNOWN: git log, fresh clone 2026-10-29] (corrected in a fact-check pass, 2026-10-29)

## Who uses it / why it matters
No outside users or citing papers found yet. [UNKNOWN; see verification/not-found.md] It just hit 1.0, so outside use may simply not have shown up. [INFERRED] It matters because TES is one of the cheaper ways to cut building peak demand, and a reproducible open tool lets anyone test it on standard buildings. [INFERRED from README "About"]

## Related projects
Filled by the connections pass, matching connections/map.md.
| Related item | Relationship | Source | Tag |
|---|---|---|---|
| OpenStudio / EnergyPlus | uses (outside DOE projects) | README; `run.py` | [KNOWN] |
| [EnergyPlus](energyplus.md) | uses (simulation engine); map link 59 | https://github.com/ORNL/Stor4Build README | [KNOWN] |
| NREL | co-developer (OSTI research orgs); map link 60 | OSTI record per map link 60 | [KNOWN] |

## What stands out
This is the most "product-shaped" brief in group two: tests, CI on six Python versions, regression baselines, PyPI releases and a 1.0. It also shows how a two-lab project stays mostly invisible until it goes public: about 20 months of history existed before the repo appeared.

## Ten questions (GOAL.md)
1. Problem and audience: testing building thermal storage for peak cutting, for building energy researchers and analysts. [KNOWN]
2. Place in the tree: buildings research, an ORNL and NREL joint tool. [KNOWN: DOE CODE]
3. Who pays: DOE EERE Building Technologies Office. [KNOWN: DOE CODE]
4. Code: Python and Hatch, plus Ruby OpenStudio measures, EnergyPlus plugins and Flask. [KNOWN]
5. Alive: yes, with steady commits and a v1.0.0 in September 2026. [KNOWN]
6. Outside users: none found. [UNKNOWN]
7. Connections: upstream OpenStudio, EnergyPlus and DOE prototype buildings; downstream UNKNOWN.
8. What it teaches: multi-lab tools can live in their own GitHub org. [KNOWN]
9. Student path: doable. `pip install stor4build` plus OpenStudio 3.11 (it has a Mac installer) should run the CLI. [INFERRED; not run here] Good first contributions would be the "TBD" coverage rows.
10. Still unknown: users and results from real studies. Searched without result: outside citations.

## Known / Inferred / Unknown
- KNOWN: the DOE CODE record, labs, sponsor, license, layout, CLI, CI, releases and dependencies.
- INFERRED: the imported history, the NREL operator reading and the Mac path.
- UNKNOWN: users and study results.

## Verification notes
Filled by the fact-check pass.

## Sources (URL, title, accessed date, what it supports)
- https://www.osti.gov/doecode/biblio/170060, DOE CODE "Stor4Build", accessed 2026-10-24, supports the DOI, labs and sponsor
- https://github.com/Stor4Build/stor4build, the repo, accessed 2026-10-28, supports the code, CI and docs facts
- https://pypi.org/project/stor4build/, PyPI release history, accessed 2026-10-24, supports release dates

## Quality gate
- [x] Every load-bearing claim has a source and a tag
- [x] Facts are kept apart from interpretation
- [x] ORNL relationship is not overstated, and maturity verbs match the source
- [x] Walkthrough, flow, timeline and unknowns are present
- [x] Ten questions answered or marked UNKNOWN
- [x] No copied text beyond short cited quotes; people by role only
- [ ] Two fact-check sweeps done
- [ ] INDEX, catalog, LAB-TREE and connections map updated

## Fact-check notes (2026-10-29)
- Re-checked against GitHub API, a fresh clone, DOE CODE 170060 and PyPI. Verified: BSD-3-Clause with the shared ORNL/UT-Battelle and Alliance copyright line; repo created 2025-10-20; last push 2026-10-13; earliest commit 2024-02-23; tags v0.1.0 (2024-09-10) through v1.0.0 (2026-09-30); PyPI first release 0.3.0 on 2025-11-16 and 1.0.0 on 2026-10-01 (UTC upload, evening of 2026-09-30 ET); 24 `.osm` models; 19 measures (plus a README); Python >=3.8; 3 contributors, 1 star, 1 fork, 8 open issues; DOE CODE ORNL and NREL research orgs, BTO sponsor, 2025-11-11.
- Corrected: yearly commit counts labelled as committer date, with author-date figures added.
- Map links 59 and 60 match the brief.

### Second pass (2026-10-29)
- Re-verified with new sources: the CI Python matrix (3.8 to 3.13) and Ubuntu 24.04 runner in tests.yml; OpenStudio and EnergyPlus versions from docs/source/installation.md (corrected: patch-level versions weren't stated, and the source was mislabelled; the docs also tie the plugin to Python 3.12). The commit-count label fix is in place.
