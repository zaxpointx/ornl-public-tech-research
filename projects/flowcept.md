# Flowcept
- Official page: https://flowcept.org (project site, linked from the README) [KNOWN: README]
- Repo: https://github.com/ORNL/flowcept
- Docs: https://flowcept.readthedocs.io/ (built from `docs/` in the repo)
- License: MIT. Quote: "Copyright (c) 2022 Oak Ridge National Laboratory" [KNOWN: https://github.com/ORNL/flowcept/blob/main/LICENSE, line 3; GitHub API spdx MIT]
- Status: active [KNOWN: last push 2026-08-12 UTC, release v1.0.3 on 2026-07-20 UTC, not archived, GitHub API]
- Scope (rule 13): ORNL is the copyright holder and the repo owner. [KNOWN: LICENSE, github.com/ORNL]

## Plain-language walkthrough
- **What it is:** a Python library and service that records the history of a computing job while it runs: what ran, which data went in and came out, where, how long it took and what resources it used. That history is called *provenance*. The README calls it a "lightweight runtime provenance data management and data observability system". [KNOWN: README]
- **The problem:** big science and AI jobs spread across many machines (laptops, cloud, supercomputers) and many steps. Afterward it's hard to answer "which data and settings produced this model?" Flowcept keeps that record automatically. [KNOWN: README "hard to inspect after the fact"]
- **What goes in:** events from your code (you mark functions with a decorator, a tag above a Python function) or from tools you already use, such as PyTorch, Dask, MLflow and TensorBoard, through "adapters" that watch them without code changes. [KNOWN: README, docs/architecture.rst]
- **What happens:** records are buffered in memory and streamed through a message queue (Redis by default; RabbitMQ, Kafka or Mofka are options) to "Provenance Keeper" services that store them. [KNOWN: docs/architecture.rst]
- **What comes out:** stored provenance in a JSONL file, LMDB or MongoDB, plus a web UI, reports ("workflow cards") and a query API. [KNOWN: README]
- **Where humans act:** scientists add decorators or turn on adapters, pick a storage setup, then browse the UI or ask questions. An optional "Flowcept Agent" lets people query the records in plain language through an LLM (large language model, the kind of AI behind chatbots). [KNOWN: README]
- **What it is not:** it doesn't schedule or run your workflow; it watches and records one. [INFERRED: the docs describe capture, storage and querying only, with no scheduler]
- **What's unknown:** which ORNL group owns it, and how widely it's used outside its own papers (the connections-pass signals work may answer the second).
- **Example:** the README quickstart marks two tiny functions, `add_one` and `double`, with `@flowcept_task`. Running it with no database writes a local JSONL record of each call's inputs, outputs and timing, then prints a summary card. [KNOWN: README Quickstart]

## How it works
- **Provenance model:** records follow W3C PROV, a web standard for describing where data came from, extended for workflow, ML and agent runs. [KNOWN: README, docs/architecture.rst]
- **Two ways to capture:** passive adapters that watch outside services, and direct code hooks like decorators. [KNOWN: docs/architecture.rst "Capture Mechanisms"]
- **Publish-subscribe hub:** a message queue sits between the job and storage. The job "publishes" records and keepers "subscribe" to them, so a slow database doesn't slow the science job. The docs say buffering is meant "To minimize interference with HPC applications". [KNOWN: docs/architecture.rst, quote under 25 words]
- **Storage tiers:** JSONL for small demos, LMDB (a fast file-based key-value store) for file-only runs, and MongoDB (a document database) for querying and the UI. [KNOWN: README]
- **Agent layer:** `src/flowcept/agents/` holds LLM chat, query tools and an MCP folder. MCP (Model Context Protocol) is a standard way for AI assistants to call tools. [KNOWN: repo tree; INFERRED: the MCP folder's purpose from its name and the README's "MCP agents" mention]

## How the project is organized
- `src/flowcept/` has `flowceptor/` (adapters, consumers, telemetry capture), `instrumentation/` (decorators and hooks), `commons/` (data access, buffers, settings), `flowcept_api/` (the controller and database API), `webservice/`, `report/` and `agents/`. `ui/` is a separate TypeScript web app built with Vite and tested with Playwright. `deployment/` holds Docker Compose files for each broker and database. `docs/`, `examples/`, `notebooks/` and `tests/` round it out. [KNOWN: repo tree]
- Languages: Python (about 74%) and TypeScript (about 21%), plus notebooks. [KNOWN: GitHub languages API, by bytes]
- Build: Python 3.11+, packaged with Hatch, published on PyPI as `flowcept`. [KNOWN: pyproject.toml, README PyPI badge]
- CI: GitHub Actions run tests across databases, brokers (Kafka, RabbitMQ), offline mode, Python 3.13, containers, LLM tests and UI checks, and publish releases. [KNOWN: .github/workflows file names]
- Contributors: 19 including anonymous commit authors, 11 GitHub accounts without them. Created 2022-11-10. Releases come often, for example v0.10.8 and v0.10.9 the same day (2026-06-11), then v1.0.1 to v1.0.3 in July 2026. [KNOWN: GitHub API]
- Owning division or group: not stated in what I read. [UNKNOWN]

## Who uses it / why it matters
The project says it targets ML training, agent workflows, HPC jobs and edge-to-cloud-to-HPC pipelines. [KNOWN: README] Its docs list publications. I didn't read them, so named users are [UNKNOWN]. For a security student, provenance is close to audit logging: a trustworthy record of who ran what on which data. That's the same idea behind forensic timelines and software supply-chain records. [INFERRED]

## Related projects
- DataFed (`datafed`): map link 19 already ties them. [KNOWN per map; not re-read by me]
- HydraGNN (`hydragnn`): both are ORNL AI and HPC tools. Any direct use is [UNKNOWN].

## Known / Inferred / Unknown
- KNOWN: MIT license with ORNL copyright, purpose, capture and streaming design, storage options, layout, languages, CI coverage, release history.
- INFERRED: it doesn't schedule workflows; the MCP folder's role; the security relevance.
- UNKNOWN: owning group, outside users, which supercomputers it has run on (not checked; that's signals work).

## Sources (accessed 2026-10-24)
- https://github.com/ORNL/flowcept (README.md, LICENSE, pyproject.toml, docs/architecture.rst, .github/workflows/, src/)
- https://flowcept.readthedocs.io/
- https://api.github.com/repos/ORNL/flowcept (plus /languages, /releases, /contributors)

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Rechecked against the GitHub API and raw files: MIT with "Copyright (c) 2022 Oak Ridge National Laboratory" (LICENSE line 3), created 2022-11-10, last push 2026-08-12, v1.0.3 on 2026-07-20, the same-day v0.10.8/v0.10.9 releases, contributors 19 with anonymous / 11 accounts, languages Python 74.3% and TypeScript 20.6%, the README "lightweight runtime provenance data management and data observability system" quote. flowcept.org, the readthedocs site and the repo all resolve. All verified.
- Second primary source: ORNL's FY2025 LDRD report (OSTI 3025007) describes FlowCept as the part of an LDRD project that captures "runtime provenance, metadata, and references to large data objects", alongside Zambeze. Rule 13 is CORROBORATED.
- No corrections needed.
