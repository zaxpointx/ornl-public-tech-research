# Hydropower Fleet Intelligence (HydroFleetIntel, HFI)
- Repo: https://github.com/ORNL/HydroFleetIntel [KNOWN]
- DOE CODE: code-123550, DOI 10.11578/dc.20240307.4. Research org ORNL, sponsor DOE EERE Water Power Technologies Office (WPTO). [KNOWN: OSTI API record code-123550, accessed 2026-10-24]
- Docs: README only [KNOWN]
- License: UT-Battelle open source license, "Hydropower Fleet Intelligence, Version 1.0", copyright 2024. GitHub shows NOASSERTION. [KNOWN: LICENSE.md, GitHub API]
- Status: unknown. 8 commits over 2024-03-07 to 2024-03-12, nothing since. [KNOWN: git log] The README says "Submitted issues and pull requests are not actively monitored or reviewed." [KNOWN: README] It's a published snapshot, not a maintained project. [INFERRED]
- ORNL relationship: KNOWN (main ORNL org, UT-Battelle copyright, OSTI names ORNL)
- Years visible in public sources: 2024
- Last checked: 2026-10-24

## Walkthrough (plain language)
- **What it is:** a web dashboard that pulls together information about hydropower plants so you can see how old their parts are, how they've broken down and what maintenance has been done. [KNOWN: OSTI description; README]
- **Key terms:**
  - **Fleet:** all the plants an owner runs, looked at as a group.
  - **Nameplate data:** the basic specs stamped on a generator, such as its capacity.
  - **Taxonomy:** a family tree of parts. This one splits a hydropower facility into numbered pieces, for example "1. Headwater/Reservoir", then "1.1 Siltation and Dredging Devices". There are 222 rows. [KNOWN: `public/HFI_taxonomy_2.csv`]
  - **GADS:** the event files the maintenance code reads are labeled GADS. That's probably NERC's Generating Availability Data System, the North American grid's outage-reporting database. [KNOWN: file label in the code; INFERRED: the expansion]
  - **API:** the back-end web addresses the dashboard calls to get data. [KNOWN: `api/views.py`]
- **The problem:** many US hydropower plants are old, and the data about their parts, failures and maintenance is scattered. Owners and analysts need one place to judge age, reliability and cost. [KNOWN: OSTI description; INFERRED: the "old plants" context, which no source in this pass gave]
- **What goes in:** a facility list, generator nameplate data, sensor time series, event history and maintenance records. The public copy ships only a synthetic (made-up) facility list and nameplate data. [KNOWN: README "synthetic dataset"]
- **What happens:**
  1. The Next.js front end shows the part taxonomy as levels you click through. [KNOWN: `components/Taxonomy.tsx`, `components/Levels`]
  2. Each click calls the Flask API: `get_facilities`, `get_part_information`, `get_viz_data`, `get_event_history`, `get_maintenance_hist` and `maintenance_mileage`. [KNOWN: `api/views.py`]
  3. The API answers with charts and tables (chart.js, react-table). [KNOWN: package.json]
  4. `maintenance_mileage` estimates how much use a part has had since its last maintenance. [KNOWN: route name; INFERRED: what it computes]
- **What comes out:** an interactive page of facility info, part details, sensor charts and event and maintenance history. [KNOWN: README, OSTI]
- **Where humans act:** an asset manager or analyst browses the dashboard. Someone with real plant data would have to load it, since the public copy has only fake data. [KNOWN: README; INFERRED: the roles]
- **What it is not:** it isn't a control system for dams or turbines and doesn't connect to plant equipment. It only reads data files. [KNOWN: the code reads files; INFERRED: "not a control system"]
- **What's unknown:** who uses it with real data. Most analysis functions need datasets that aren't public. [KNOWN: README; UNKNOWN: users]
- **Example:** pick a facility, click down to "2. Dam/Weir" and then "2.1 Spillways", and see that part's synthetic sensor chart and event history. [KNOWN: taxonomy rows; INFERRED: the click path]

## What it is (plain English, 2-4 sentences)
A dashboard prototype for looking across a fleet of hydropower plants part by part, from reservoir to generator, combining age, failure events, maintenance and sensor data. The public release runs on fake data so anyone can try the interface. [KNOWN: README, OSTI]

## How it works (plain English, no jargon without definition)
Two programs talk to each other. A Flask (Python) server in `api/` reads data files and answers requests. A Next.js (React and TypeScript) web page in `pages/` and `components/` draws the interface. Docker Compose can start both at once as containers named `hfi-backend` and `hfi-frontend`. [KNOWN: tree, `docker-compose.yml`, README]

## How the project is organized
- Languages: TypeScript and JavaScript (Next.js 13, React 18, Chakra UI for styling) and Python (Flask with CORS, conda environment `hfi_env.yml`). [KNOWN: package.json, hfi_env.yml]
- Layout: `api/` (`views.py`, `classes/`, `functions/`, `data/`), `components/`, `pages/`, `public/` (the taxonomy CSV), `part_level_tables/` (an Excel "sufficiency matrix" template plus an R script that generates link tables), `run.py`, and two Dockerfiles. [KNOWN: tree]
- Install: two methods, Docker Desktop or local Node 20.11 or newer with conda. The README is written for VS Code users. [KNOWN: README]
- Tests: none found. CI: none. Releases: none on GitHub. CONTRIBUTING: none, and the README says PRs aren't reviewed. [KNOWN: tree, README]
- Contributors: 2 including anonymous authors, 1 account. 0 stars, 0 forks. [KNOWN: GitHub API, 2026-10-24]
- Why Flask plus Next.js, or why the sufficiency-matrix approach: [UNKNOWN; not stated]

## Timeline
| Date | Event | Source | Tag |
|---|---|---|---|
| 2024-03-07 | 6 commits; OSTI code-123550 DOI dated the same day | git log, OSTI | KNOWN |
| 2024-03-12 | 2 final commits | git log | KNOWN |

## Who uses it / why it matters
- It's aimed at hydropower asset managers and WPTO-funded analysts. [INFERRED from the sponsor and description] No public users found. [UNKNOWN]

## Related projects
Filled by the connections pass, matching connections/map.md.
| Related item | Relationship (uses, extends, shares data, same facility, related topic, unknown) | Source | Tag |
|---|---|---|---|
| GridKit | related topic (grid/energy; no code or people link) | map link 49 | UNKNOWN |
| Grid solver group (PETSc, Ipopt, HiOp, SUNDIALS) | unknown; none of them used, own Flask/Next.js stack | map link 196; https://github.com/ORNL/HydroFleetIntel | KNOWN |
| DOE EERE Water Power Technologies Office | sponsor | map link 202; https://www.osti.gov/api/v1/records/code-123550 | KNOWN |

## What stands out
- The part taxonomy is the most reusable piece. A 222-row breakdown of a hydropower plant is a teaching tool even without the app. [KNOWN: CSV; INFERRED: the value]
- Publishing with synthetic data is a neat way to share a tool when the real plant data can't be shared. [KNOWN: README; INFERRED]
- It's another case where the public repo appears the same day as its DOE CODE record, which looks like a release-and-done snapshot. [KNOWN: dates; INFERRED]

## Ten questions (GOAL.md)
1. **Problem and for whom:** one view of hydropower plant parts, age, reliability and cost, for plant owners and analysts. [KNOWN: OSTI]
2. **Where in the tree:** ORNL, then water power research, funded by DOE EERE WPTO. [KNOWN: OSTI; INFERRED: the program placement]
3. **Who pays:** EERE's Water Power Technologies Office. [KNOWN: code-123550]
4. **Organized how:** a Flask API plus a Next.js front end, Docker Compose, conda, and an R helper script. [KNOWN]
5. **Alive?** No. It was 8 commits over six days in March 2024, and the README says issues aren't monitored. [KNOWN]
6. **Outside users:** none found. 0 stars and 0 forks. [KNOWN]
7. **Connections:** upstream are probably NERC GADS event data and plant records. [INFERRED] Downstream: unknown.
8. **What it teaches about ORNL:** applied energy offices fund practical tools, and some code is released as a finished snapshot with fake data rather than as a living project. [INFERRED]
9. **Student angle:** a good full-stack example to run locally with Docker. You can read how a React page calls a Python API. Contributing isn't realistic because PRs aren't reviewed, but forking and loading your own made-up data is. [KNOWN: README; INFERRED]
10. **Unknown and searched without result:** a paper or report on HFI (not searched in this pass), real deployments, what "sufficiency matrix" scores mean.

## Known / Inferred / Unknown
- [KNOWN] sponsor, stack, endpoints, synthetic data, taxonomy, history, README disclaimer.
- [INFERRED] the GADS expansion, the purpose of `maintenance_mileage`, the snapshot nature.
- [UNKNOWN] users, real data, a paper.

## Verification notes
_Filled by the fact-check pass._

## Sources (accessed 2026-10-24)
- https://github.com/ORNL/HydroFleetIntel (README.md, LICENSE.md, package.json, hfi_env.yml, docker-compose.yml, `api/views.py`, `public/HFI_taxonomy_2.csv`, tree)
- https://api.github.com/repos/ORNL/HydroFleetIntel (and /contributors)
- https://www.osti.gov/api/v1/records/code-123550

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Verified: code-123550 (WPTO sponsor, ORNL, DOI, 2024-03-07), 8 commits (6 on 2024-03-07, 2 on 2024-03-12), the README's synthetic-data and no-review lines, 0 stars and 0 forks. The README names a staff contact; the brief correctly leaves it out. No corrections.
