# SNS Data Workflow Manager (data_workflow)
- Official page / Docs: https://data-workflow.readthedocs.io [KNOWN: GitHub API homepage, README badge]
- Repo: https://github.com/neutrons/data_workflow
- License: BSD 3-Clause, copyright 2022 Oak Ridge National Laboratory [KNOWN: LICENSE file, https://github.com/neutrons/data_workflow/blob/next/LICENSE]
- Status: active, last push 2026-10-23, release 3.12.0 on 2026-10-19 [KNOWN: GitHub API]

## What it is (plain English, 2-4 sentences)
This is the behind-the-scenes plumbing that watches every experiment at ORNL's neutron facilities and automatically kicks off data processing when a run finishes [KNOWN: README describes it as the "SNS data workflow manager and reporting app"]. It also runs the status website, WebMon, where staff and users can check what each instrument is doing and whether automatic processing ("autoreduction") worked [KNOWN: docs glossary]. The glossary says it covers both SNS (the Spallation Neutron Source) and HFIR (the High Flux Isotope Reactor) [KNOWN: docs/glossary.rst]. The production site is https://monitor.sns.gov [KNOWN: docs/developer/index.rst].

## How it works (plain English, no jargon without definition)
- It's built from three Django apps (Django is a popular Python web framework) deployed together with Docker Compose [KNOWN: README, developer docs].
- **Workflow Manager:** the backend that moves each run through processing steps. It talks over ActiveMQ, a "message broker" that passes messages between programs so they don't need to call each other directly, using the STOMP messaging protocol [KNOWN: README].
- **DASMON listener:** DASMON is a service on each beamline that reports instrument readings ("PVs", process variables like temperature or motor position) and run metadata. The listener records those messages in a database [KNOWN: README, glossary].
- **WebMon:** the reporting website that reads that database and shows instrument and autoreduction status [KNOWN: README, glossary].
- Data lives in PostgreSQL 17+ (or MySQL), with optional stored procedures to speed up run-rate and error-rate queries [KNOWN: README].
- The actual number-crunching runs elsewhere. The `post_processing_agent` runs on dedicated "autoreducer" machines, and `livereduce` (a Mantid-project daemon) makes live plots during acquisition [KNOWN: docs/developer/index.rst]. Those reduction steps are where Mantid comes in [KNOWN: livereduce sits in the mantidproject org, and the post_processing_agent README has a Mantid settings section and says its predecessor was mantidproject/autoreduce].

## How the project is organized (repo structure, languages, build, maintainers/org unit, release cadence)
- Languages: about 70% Python, 16% JavaScript, 10% HTML and 3% CSS [KNOWN: GitHub languages API].
- `src/workflow_app`, `src/webmon_app` (the `reporting` module) and `src/dasmon_app` are the three apps. There are separate Dockerfiles for autoreducer, dasmon, oncat, webmon, webmonchow and workflow, plus `nginx/` (web server config), `config/`, `tests/` and `docs/` (Sphinx/ReadTheDocs, with user, developer and admin sections) [KNOWN: repo tree].
- Build: `pyproject.toml` with pixi for environments, and Docker Compose for deployment [KNOWN: repo root].
- Quality: CI on GitHub Actions, code coverage through Codecov, and an OpenSSF/CII Best Practices badge (project 5504) [KNOWN: README badges].
- Releases: frequent, about every 1 to 3 months in 2026. Recent ones are 3.10.0 (2026-07-16), 3.11.0 (2026-08-04) and 3.12.0 (2026-10-19), with release candidates [KNOWN: GitHub releases API]. The repo dates from 2012-08-15 [KNOWN].
- Contributors: about 35 per the GitHub API, counting anonymous ones [KNOWN].
- Org unit: the `neutrons` GitHub org, serving SNS and HFIR [KNOWN: docs]. The specific ORNL division isn't stated [UNKNOWN]. It's likely the Neutron Sciences Directorate, given what it serves [INFERRED].

## Who uses it / why it matters
- Instrument scientists and visiting researchers at SNS and HFIR, who use WebMon to check runs. The docs have separate guides for general users, guests and instrument scientists [KNOWN: docs/users file names].
- It turns a firehose of raw detector data into processed results automatically, so scientists get usable data minutes after a run instead of days [INFERRED: purpose of autoreduction].
- For a cyber student, it's a real example of a message-queue architecture with a public-facing monitoring site [INFERRED].

## Related projects
- Mantid, through livereduce and autoreduction [KNOWN: see above].
- ONCat, the neutron experiment data catalog at https://oncat.ornl.gov, has its own Dockerfile here [KNOWN: glossary and Dockerfile.oncat].
- SNAPRed and PyRS are from the same `neutrons` org [KNOWN: catalog].
- post_processing_agent and live_data_server are sibling repos not yet in the catalog [KNOWN: developer docs], and could be candidates for batch 3.

## Known / Inferred / Unknown
- [KNOWN] BSD-3, the three-app Django design, ActiveMQ/STOMP, PostgreSQL, serving SNS and HFIR, the monitor.sns.gov production site, frequent 2026 releases, about 35 contributors.
- [INFERRED] NScD ownership.
- [UNKNOWN] Exact owning group, and data volumes handled.

## Sources (URL, accessed date)
- https://github.com/neutrons/data_workflow (README.rst, LICENSE, docs/glossary.rst, docs/developer/index.rst, tree), accessed 2026-10-24
- https://api.github.com/repos/neutrons/data_workflow (+ /languages, /releases, /contributors), accessed 2026-10-24
- https://data-workflow.readthedocs.io, linked, not opened this pass

## Fact-check notes (ORNL Fact Checker, 2026-10-24)
- Corrected: Mantid link retagged KNOWN after reading https://github.com/neutrons/post_processing_agent README.
- Verified: BSD-3 copyright 2022 ORNL; created 2012-08-15; releases 3.10.0 (2026-07-16), 3.11.0 (2026-08-04), 3.12.0 (2026-10-19) with rc tags; Python 70.3 / JS 15.9 / HTML 9.7 / CSS 2.9; 35 contributor pages; README lists stomp, django, PostgreSQL 17+, MySQL option, ActiveMQ and badge 5504; glossary covers WebMon at SNS and HFIR and DASMON PVs; developer docs link monitor.sns.gov and the sibling repos; six Dockerfiles, nginx, pixi.lock confirmed.
- No DOE CODE record found for data_workflow. Owning division stays [UNKNOWN].
