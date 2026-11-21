Short brief, public code (dormant). Independent research, not affiliated with ORNL. People by role only. Last checked: 2026-11-21.

# Stucco (cyber intelligence knowledge graph)

- Official page: https://www.ornl.gov/projects/stucco/ [1]
- Project site: https://stucco.github.io/ [2]
- Repos: https://github.com/stucco (29 repositories) [3]
- Final report: https://info.ornl.gov/sites/publications/Files/Pub104227.pdf ("Stucco System", prepared by ORNL for the DHS S&T Cyber Security Division, dated 2018-06-01) [4]
- License: Mixed. Most repos carry a non-standard license file (GitHub reports NOASSERTION); the `ui` repo is MIT. [KNOWN: GitHub API, 3]
- Status: unknown (no commits to any repo after 2019-11-27; none flagged archived) [KNOWN: GitHub API, 3]
- ORNL relationship (RULES 13): KNOWN: the ORNL project page describes it [1]; the 2018 report says it was prepared by ORNL [4]. Partners named in the report: PNNL, Stanford University and REN-ISAC [4].
- Years visible in public sources: 2012 (first repo) to 2019 (last commit)

## Walkthrough (plain language)
- **What it is:** A platform that gathers security context from many sources and stores it as a knowledge graph, so an analyst can look up everything related to an alert in one place. [KNOWN: 1, 2]
- **The problem:** An IDS alert on its own says little. Analysts hand-search logs, flows, blacklists, vulnerability feeds, vendor blogs and news to work out whether it matters. [KNOWN: 1]
- **What goes in:** Structured feeds (vulnerability lists, blacklists, logs) and unstructured text (blogs, advisories). [KNOWN: 2, 4]
- **What happens:** Collectors fetch documents. A real-time pipeline (RT) pulls them off RabbitMQ queues, extracts cyber entities and relationships from text, shapes them as STIX 1.2 subgraphs and merges them into the graph. [KNOWN: 2, 4]
- **What comes out:** A searchable graph plus a web UI and API. [KNOWN: 2]
- **Where humans act:** Analysts query the graph and decide what is a false positive. [KNOWN: 1]
- **What it is not:** Not an IDS and not a live threat-feed service. [INFERRED from 1, 2]
- **Example:** An alert names a software version. A graph search returns known vulnerabilities for that version, write-ups that mention it, and internal hosts running it. (Illustrative, built from the report's relationship types, 4.)
- **Unknown:** Whether anyone still runs it, and who funded which years beyond the DHS S&T report.

## How it works
1. Collectors schedule and gather structured and unstructured documents. [KNOWN: 2]
2. A document service stores raw text over an HTTP API. [KNOWN: 2]
3. RT pipeline: entity extraction, then relation extraction (the report says it uses SVMs and feature models), then graph alignment. [KNOWN: 4]
4. Storage: the project site names Titan, a distributed graph database. [KNOWN: 2] Any later database change is UNKNOWN here; later repos were not re-read.
5. UI and API for analysts. [KNOWN: 2]

## Outside-in signals
- 29 public repos, the first created 2012-10-05, last push 2019-11-27. [KNOWN: GitHub API, 3]
- The most-starred repo is `auto-labeled-corpus` (97 stars), a labeled corpus of cyber security text. [KNOWN: 3] Stars suggest it is the piece outsiders still reuse. [INFERRED from stars only]
- `entity-extractor`: 38 commits from 2014-01 to 2016-05 under 4 author names. [KNOWN: GitHub API]
- A DHS S&T archive page lists STUCCO among its network-measurement projects. [KNOWN-from-search-result: https://www.dhs.gov/archive/science-and-technology/anms; not re-fetched]

## What stands out (interpretation)
The labeled corpus outlived the platform. For a student, that is the reusable part: training data for pulling CVEs, product names and versions out of text.

## Related
- [Situ](../../../projects/situ.md): same era and research area (analyst tools). [INFERRED]
- [ORCA](orca.md) and [NV](nessus-visualization.md): the same 2010s analyst-tooling line; see the [lineage deep dive](../deep-dives/analyst-tools-lineage.md). [INFERRED]

## Known / Inferred / Unknown
- KNOWN: Purpose, components, STIX alignment, partners, open-source release.
- INFERRED: That it is dormant (from commit dates, not a statement).
- UNKNOWN: Funding after 2018, deployments, why work stopped.

## Sources (accessed 2026-11-21 unless noted)
1. https://www.ornl.gov/projects/stucco/ (ORNL project page); supports: purpose
2. https://stucco.github.io/ (Stucco project page); supports: components, RabbitMQ, Titan
3. https://github.com/stucco (GitHub org, read through the API); supports: repo list, dates, licenses
4. https://info.ornl.gov/sites/publications/Files/Pub104227.pdf (Stucco System, ORNL report for DHS S&T, 2018-06-01); supports: pipeline, STIX 1.2, partners

## Verification
Sweep 1 done on 2026-11-21: each load-bearing source above was fetched that day unless it is marked as seen in a search result. Sweep 2 (an independent re-read) has not been done, so this brief is not yet promoted to `discovery/catalog.csv`. See the [cyber atlas verification notes](../verification.md).
