# TRANSFORM (TRANsient Simulation Framework of Reconfigurable Models)

- Repo: https://github.com/ORNL-Modelica/TRANSFORM-Library (side org; qualifies via DOE CODE code-5745 and the UT-Battelle copyright) [KNOWN]
- Official record: DOE CODE https://www.osti.gov/doecode/biblio/5745 (2017-09-26, ORNL, USDOE); the README's citation gives doi 10.11578/dc.20171025.2022 [KNOWN: catalog row; README "Citation"]
- Docs: README, the in-library `UsersGuide` package, and a separate training repo, TRANSFORM-Training [KNOWN]
- License: Apache-2.0, copyright 2017 UT-Battelle [KNOWN: README "License"]
- Status: active (last push 2026-10-14) [KNOWN: GitHub API via catalog]

## Walkthrough
TRANSFORM is a library of building blocks (pipes, pumps, heat exchangers, reactor cores, control systems) for simulating how a whole power plant behaves over time. [KNOWN: README; package names]
The problem: when a pump trips or power changes, heat and fluid move through a plant in seconds to hours, and designers need to know whether temperatures stay safe. Building that model from scratch for each new reactor design is slow. [INFERRED: standard background for system thermal-hydraulics]
What goes in: a plant model assembled from TRANSFORM components, plus their settings (sizes, materials, the fluid, such as water, molten salt, sodium or CO2). [KNOWN: `Media`, `Fluid`, `HeatExchangers` packages and the example folders]
What happens: Modelica, an equation-based modeling language, turns the connected components into one big set of equations, and a tool solves them through time. [KNOWN: README says it's Modelica based; Modelica definition is standard]
What comes out: temperatures, pressures, flows and power over time. [INFERRED]
Where humans act: an engineer builds the model and judges the transient. [INFERRED]
What it is not: not a neutron transport or fuel chemistry code. The `Nuclear` package has reactor kinetics (simple equations for how power rises and falls), not full core physics. [KNOWN: `Nuclear/ReactorKinetics`; INFERRED scope]
Example: the `Examples/MoltenSaltReactor` models simulate a molten-salt plant; a user could cut pump flow and watch the core outlet temperature rise. (The folder exists; the scenario is illustrative.)
The catch: the README lists Dymola, a paid commercial Modelica tool, as its only requirement. [KNOWN: README "Requirements"] Whether free OpenModelica can run it is UNKNOWN, and the README doesn't mention it.

## What it is (plain English, 2-4 sentences)
An open Modelica library for modeling thermal-hydraulic energy systems and other multi-physics systems. [KNOWN: README] It ships ready-made examples for pressurized water reactors, small modular reactors, molten salt and sodium fast reactors, supercritical CO2 cycles, and a test facility called CIET. [KNOWN: `TRANSFORM/Examples/` folder names, fresh clone 2026-10-29]

## How it works (plain English, no jargon without definition)
1. Pick components from packages such as `Fluid`, `HeatExchangers`, `HeatAndMassTransfer`, `Electrical`, `Controls` and `Nuclear`. [KNOWN]
2. Choose a medium (fluid properties) from `Media`. [KNOWN]
3. Connect them graphically or in code into a plant model. [INFERRED: how Modelica tools work]
4. Simulate in Dymola. [KNOWN: README]
5. Check the library itself by running the `runAll_*.mos` unit test scripts. [KNOWN: README]

## How the project is organized
- Layout: `TRANSFORM/` with about 18 packages (Blocks, Controls, Electrical, Examples, Fluid, HeatAndMassTransfer, HeatExchangers, Math, Media, Nuclear, PeriodicTable, UsersGuide, Utilities and more), plus `LICENSE.txt` and `README.md`. [KNOWN: repo tree]
- `Nuclear/` subpackages: ClosureRelations, CoreSubchannels, DoseCalculations, FuelModels, PowerProfiles, ReactorKinetics. [KNOWN]
- Language and tools: Modelica, with Dymola required. [KNOWN] Sibling repos in the same org: TRANSFORM-Training, TRANSFORM-Julia and ModelicaPy. [KNOWN: catalog row]
- Contributors: 17 distinct author names on the default branch (18 across all branches; 20 if name+email pairs are counted separately). [KNOWN: git shortlog on a fresh clone, 2026-10-29]
- Releases: 4 GitHub releases. [KNOWN: GitHub API releases endpoint, 2026-10-29]
- Tests: `.mos` scripts run inside Dymola. No CI. [KNOWN: README; INFERRED no CI, since `.github/` holds only issue templates]
- Why Modelica and Dymola: UNKNOWN.

## Timeline
| Date | Event | Source | Tag |
|---|---|---|---|
| 2017-07-26 | repo created | GitHub API (catalog) | [KNOWN] |
| 2017-09-26 | DOE CODE record code-5745 | DOE CODE | [KNOWN] |
| 2018-2020 | busiest years, 373, 187 and 169 commits | git log, author dates | [KNOWN] |
| 2022-2026 | slower but steady, 8 to 29 commits a year | git log | [KNOWN] |
| 2026-09-30 | latest commit on default branch (author and committer date) | git log, fresh clone | [KNOWN] |
| 2026-10-14 | latest push (pushed_at; can include branch or tag pushes) | GitHub API | [KNOWN] |

## Who uses it / why it matters
UNKNOWN from sources read. Molten salt use was seen only in a search summary. [INFERRED, not fetched] It matters because the advanced reactor designs ORNL works on need fast plant-level transient models before anything gets built. [INFERRED]

## Related projects
Filled by the connections pass, matching connections/map.md.
| Related item | Relationship | Source | Tag |
|---|---|---|---|
| Dymola | required runtime (outside, commercial); map link 215 | https://github.com/ORNL-Modelica/TRANSFORM-Library README | [KNOWN] |
| OpenModelica | compatibility not stated in the docs; map link 215 | README | [UNKNOWN] |
| DOE CODE code-5745 | ORNL research org, USDOE sponsor; map link 215 | https://www.osti.gov/api/v1/records/code-5745 ; https://www.osti.gov/doecode/biblio/5745 | [KNOWN] |

## What stands out
The code is open, but the practical door is a paid tool, so "open" here means readable and modifiable, not free to run. For Cayden's Mac goal that makes it one to read, not run, unless OpenModelica turns out to work.

## Ten questions (GOAL.md)
1. Problem and audience: plant-level transient thermal-hydraulics, for reactor and energy-system engineers. [KNOWN/INFERRED]
2. Place in the tree: nuclear energy systems modeling; the owning division is UNKNOWN.
3. Who pays: USDOE per DOE CODE, program UNKNOWN.
4. Code: Modelica in about 18 packages. [KNOWN]
5. Alive: yes, slow but steady through 2026. [KNOWN]
6. Outside users: UNKNOWN.
7. Connections: Dymola (runtime), and the sibling training and Julia repos. [KNOWN]
8. What it teaches: ORNL open-sources modeling libraries even when the runtime is commercial. [KNOWN for this case]
9. Student path: read the Examples folders to learn plant layouts. Running them needs Dymola, or an untested try with OpenModelica. [KNOWN/UNKNOWN]
10. Still unknown: OpenModelica compatibility and users. Searched without result: a README mention of a free runtime.

## Known / Inferred / Unknown
- KNOWN: license, DOE CODE record, packages, examples, the Dymola requirement and history.
- INFERRED: outputs and significance.
- UNKNOWN: free-tool compatibility, users and funding program.

## Verification notes
Filled by the fact-check pass.

## Sources (URL, title, accessed date, what it supports)
- https://github.com/ORNL-Modelica/TRANSFORM-Library, repo, cloned 2026-10-29, supports README, layout and history
- https://www.osti.gov/doecode/biblio/5745, DOE CODE record, accessed 2026-10-28 (discovery pass), supports ORNL, USDOE and the date

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
First-pass fact check against a fresh clone (commit history read 2026-10-29), the GitHub API, and the DOE CODE page for code-5745.
- Verified: Apache-2.0 and the 2017 UT-Battelle copyright (README); README "Requirements" names Dymola only; `runAll_*.mos` test scripts; DOE CODE record (release date 2017-09-26, ORNL research org, USDOE sponsor, DOI 10.11578/dc.20171025.2022); repo created 2017-07-26; last push 2026-10-14 UTC; package list and `Nuclear/` subpackages; example folders; `.github/` holds only issue templates; yearly commit counts 2018-2020 (373, 187, 169) and 2022-2026 (8 to 29), by author date, default branch.
- Commit count spot check (Rule 17): default branch 915 commits, all branches 960, fresh clone 2026-10-29. Yearly counts use author dates.
- Corrected: contributor count now says which way it is counted; added the 2026-09-30 last commit date next to the push date (they differ); filled an empty source tag on the examples list; noted 4 GitHub releases.
- OpenModelica stays UNKNOWN. The only mention in the repo is a link to OpenModelica's general Modelica course list inside `UsersGuide/Resources.mo`; that is not a statement of support.
- Side note: DOE CODE points its license link to `LICENSE.md`, while the repo file is `LICENSE.txt`. The license text itself matches (Apache-2.0).
- Nothing restricted or non-public found.

### Second pass (2026-10-29)
Skeptical reread; first-pass fixes confirmed in place and reading cleanly.
- License Apache-2.0: re-checked through the GitHub API license field, not just the README. Verified.
- DOI 10.11578/dc.20171025.2022: resolves through doi.org. Verified.
- "4 GitHub releases": cross-checked against the clone's tags (v0.1-beta to v0.4-beta, plus a `Before_MSL_4.0` tag). Verified.
- Dymola as the only stated requirement, and OpenModelica UNKNOWN: README re-read. Verified.
- Timeline: first commit 2017-08-14 comes after the repo's 2017-07-26 creation date; consistent. Last commit 2026-09-30 (author and committer). Verified.
- No corrections in this pass.
