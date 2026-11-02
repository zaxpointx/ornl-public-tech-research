Short brief (RULES 21): built from an ORNL news story and an OSTI software record; no public code.

# URBAN-NET (URBAN-NET-TOOLKIT)

- Official page: https://www.ornl.gov/news/urban-net-infrastructure-modeling-tool-be-incorporated-eagle-i (ORNL news, 2022-08-04) [KNOWN: fetched 2026-10-29]
- OSTI: https://www.osti.gov/biblio/1467082 (software record "URBAN-NET-TOOLKIT", 2017-08-31, ORNL, USDOE) [KNOWN: OSTI API, accessed 2026-10-29]
- Repo / Docs: none public [KNOWN: discovery/stub-search-2026-10-24.md]
- License: UNKNOWN
- Status: unknown

## Walkthrough
URBAN-NET models how failures spread between different kinds of infrastructure: power, gas, communications, water and transport. [KNOWN: OSTI description; news story]
The problem: a hurricane that knocks out one gas plant can starve power plants, which drop substations, which cut off customers far from the storm. Agencies usually look at one system at a time and miss those knock-on effects. [KNOWN: news story's own example, paraphrased]
What goes in: data on infrastructure assets and how they connect. [KNOWN: OSTI says the toolkit includes tools for preprocessing data] Which datasets exactly is UNKNOWN.
What happens: it builds one combined network of dependencies and traces how a failure cascades through it. [KNOWN: news story, "entire infrastructure interdependency topology"]
What comes out: the downstream parts likely to fail, like substations hit by an upstream outage, and priorities for where to look or collect data during an event. [KNOWN: news story]
Where humans act: emergency planners and EAGLE-I users decide what to protect or fix first. [KNOWN: news says it feeds EAGLE-I, used by DOE's CESER office, FEMA and state and local agencies]
What it is not: not a public download, and not a real-time control system. [KNOWN: no public code; INFERRED: described as planning and awareness]
Example: the story's own case is a gas plant knocked out, leading to power plants, then substations, then customers. [KNOWN]
Unknown: the algorithms and data sources, and whether the EAGLE-I integration was finished.

## What it is (plain English, 2-4 sentences)
A decision-support toolkit for critical infrastructure operators that maps dependencies across systems and finds where cascading failures would hit. [KNOWN: OSTI 1467082] In 2022, ORNL said it would be folded into EAGLE-I, DOE's energy outage monitoring system. [KNOWN: news story]

## How it works (plain English, no jargon without definition)
1. Preprocess infrastructure data. [KNOWN: OSTI]
2. Combine the separate systems into one network of dependencies, covering FEMA's seven "community lifelines" (essential service categories such as energy, communications and transportation). [KNOWN: news story]
3. Trace cascades to find the components that need deeper analysis. [KNOWN: news story]
4. Report to EAGLE-I users for awareness and response planning. [KNOWN: news story, stated as planned]

## How the project is organized
No public repo, so layout, languages, build, contributors and releases are all [UNKNOWN] (RULES 21). Searched: the OSTI record links field, GitHub search and the github.com/ORNL repo list (discovery/stub-search-2026-10-24.md).

## Timeline
| Date | Event | Source | Tag |
|---|---|---|---|
| 2015 | started as an ORNL-funded LDRD project (internal research money) | news story | [KNOWN] |
| 2017-08-31 | OSTI software record 1467082 | https://www.osti.gov/biblio/1467082 | [KNOWN] |
| 2022-08-04 | news: being made available to users and incorporated into EAGLE-I | news story | [KNOWN] |

A 2016 IEEE BigData paper and a KDD 2019 paper showed up in a search but weren't refetched, so they're not listed. [UNKNOWN until fetched]

## Who uses it / why it matters
Planned users are EAGLE-I's community: DOE CESER, FEMA, and state and local agencies. [KNOWN: news story] Whether they use it now is UNKNOWN. It matters because cascading failures are how a local disaster becomes a regional one. [INFERRED from the story]

## Related projects
Filled by the connections pass, matching connections/map.md.
| Related item | Relationship | Source | Tag |
|---|---|---|---|
| EAGLE-I | planned integration (outside DOE system); map link 223 | https://www.ornl.gov/news/urban-net-infrastructure-modeling-tool-be-incorporated-eagle-i | [KNOWN] |
| ORNL LDRD | funding at the 2015 start; map link 224 | same story | [KNOWN] |
| [GridKit](gridkit.md) | related topic (grid and infrastructure); map link 86 | OSTI 1467082 | [INFERRED] |
| [LandScan](landscan.md), [Vivaldi](vivaldi.md), [Gauntlet](gauntlet.md) | related topic (geospatial); map link 87 | https://landscan.ornl.gov/ | [INFERRED] |

## What stands out
It's a clean example of ORNL's path from internal seed money (LDRD, 2015) to a sponsor's operational system (EAGLE-I, 2022), about seven years. [KNOWN dates; the "pattern" reading is interpretation]

## Ten questions (GOAL.md)
1. Problem and audience: cascading infrastructure failure, for emergency and energy agencies. [KNOWN]
2. Place in the tree: grid and critical infrastructure resilience. The division isn't named. [UNKNOWN]
3. Who pays: started with ORNL LDRD; EAGLE-I is funded by DOE CESER. [KNOWN: news] Current URBAN-NET funding is UNKNOWN.
4. Code: UNKNOWN.
5. Alive: last public sign is 2022. [KNOWN]
6. Outside users: EAGLE-I's users, as planned. [KNOWN]
7. Connections: downstream EAGLE-I. [KNOWN]
8. What it teaches: LDRD seeds projects that sponsors later adopt. [KNOWN for this case]
9. Student path: no code. The idea can be tried with networkx on public infrastructure maps. [INFERRED]
10. Still unknown: algorithms, data and integration status. Searched without result: a public repo.

## Known / Inferred / Unknown
- KNOWN: purpose, the LDRD start, the OSTI record and the EAGLE-I plan.
- INFERRED: the scale of its importance.
- UNKNOWN: code, data, method details and current use.

## Verification notes
Filled by the fact-check pass.

## Sources (URL, title, accessed date, what it supports)
- https://www.ornl.gov/news/urban-net-infrastructure-modeling-tool-be-incorporated-eagle-i, ORNL news, 2022-08-04, accessed 2026-10-29, supports the purpose, example, LDRD start and EAGLE-I
- https://www.osti.gov/biblio/1467082, OSTI "URBAN-NET-TOOLKIT", accessed 2026-10-29, supports the date, ORNL and description

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
- Re-read the 2022-08-04 ORNL story and OSTI 1467082 (2017-08-31, ORNL, USDOE, software). Verified: cross-infrastructure scope, the gas plant to substations example, FEMA's seven community lifelines, the three capabilities, EAGLE-I funded by CESER and used by CESER, FEMA and other agencies, the 2015 LDRD start and "nearly seven years" of development.
- Older papers are still left out: no primary source was fetched for them.
- Related-projects table checked against connections/map.md and its sources; rows match. (Map links 69, 84 and 86 got factual updates; see verification/log.md.)

### Second pass (2026-10-29)
- Reread: "KNOWN" on where humans act is a fair paraphrase of the story's user list; "nearly seven years" and the 2015 LDRD start match. No independent source for EAGLE-I completion, which stays UNKNOWN. No issues found.
