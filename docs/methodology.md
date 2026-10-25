# Methodology

## Scope
Public software, tools, datasets, and facility software released by ORNL. A project is cataloged only if a primary source names ORNL as research organization, copyright holder, repository owner, or a named contributing lab. Related projects without that evidence appear in the connections map as outside projects.

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
The subject is projects, not people. Names, emails, and handles of individuals are removed or replaced with role labels in this public copy. Published citations are kept as bibliographic references.
