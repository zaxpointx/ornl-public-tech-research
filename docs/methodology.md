# Methodology

## Scope
The original project catalog covers public software, tools, datasets, and facility software released by ORNL. The in-progress [public research guide](public-research-guide.md) also covers selected publicly documented research, facilities, instruments, results and professional roles across the lab. The software catalog remains the master project list: a cataloged project must have a primary source naming ORNL as research organization, copyright holder, repository owner, or a named contributing lab. Related projects without that evidence appear in the connections map as outside projects. A research story or facility example is not automatically a new catalog entry.

## Sources
Allowed: ornl.gov, osti.gov (including DOE CODE), energy.gov, public GitHub/GitLab organizations, public papers, public documentation sites. Search snippets are never final evidence; the page itself is fetched. Primary sources are preferred over news.

Not allowed: logging in, bypassing access controls, anything marked restricted, CUI, export-controlled, or internal, and contacting lab staff.

## Pipeline
1. Discovery: candidates are added to `discovery/catalog.csv` with source URL, license, status, and owning unit when stated.
2. Reading: a brief is written in `projects/` from a fixed template, opening with a plain-language walkthrough and one concrete example.
3. Sweep 1: each claim is re-checked against its source plus a second primary source where possible, and logged in `verification/log.md`.
4. Sweep 2: every brief and map link in the batch is re-read, load-bearing sources are re-fetched, disconfirming evidence is sought, and overstatements are fixed. Only then is a brief marked verified.
5. Connections: links between projects are recorded in `connections/map.md`, each with its own tag and source.
6. Signals: public traces (commit history, release cadence, funding records, citations) are read in `signals/` to estimate activity and maturity.
7. Batch summary: `batches/` records what was researched, verified, still unknown, and next.

## Evidence rules
- Load-bearing claims (ownership, funding, maturity, dependencies, licenses) record URL, publisher, date, access date, and a short quote under 25 words.
- The source's maturity verb is kept (studied, prototyped, tested, deployed). Nothing is upgraded to "production" without a source.
- Two projects, tools, or people are never merged without binding evidence.
- Authorship shows participation, not ownership or leadership.

## Limits of OSINT
Public records show what a project chose to publish. They rarely show internal priorities, funding amounts per project, or who leads a team. Commit counts measure activity, not importance. Absence from search results is logged but is not proof that something does not exist.

## Privacy
The subject is research, not personal profiles. Since 2026-11-04, names may be included for a relevant professional role or authorship directly supported by an official public professional source, with an access date. Authorship is not leadership. Do not include personal contact details, personal histories or social-media investigation; do not contact staff. Older role-only files retain their original convention. See RULES.md item 22.
