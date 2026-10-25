# Zambeze
- Official page: the README and repo homepage point to https://docs.zambeze.org, which gave no response when I tried it on 2026-10-24 (logged in not-found.md). The Sphinx docs source is in the repo under `docs/`. [KNOWN: README, GitHub API homepage]
- Repo: https://github.com/ORNL/zambeze (default branch `main`) [KNOWN]
- Package: https://pypi.org/project/zambeze/. PyPI's latest is 0.1, while the repo's `pyproject.toml` says 0.2, which suggests 0.2 was never published. [KNOWN: PyPI JSON API, pyproject.toml; INFERRED: "never published"]
- License: MIT, "Copyright (c) 2022 Oak Ridge National Laboratory". [KNOWN: LICENSE lines 1-3]
- Status: unknown (rule 14). The last commit and last push were 2024-09-13, which is more than two years of quiet. It isn't archived. The releases are v0.0.1-devel (2023-01-25, marked pre-release) and v0.1-Yambeshe (2023-03-06). [KNOWN: git log, GitHub API] Quiet doesn't mean dead (rule 10).
- Scope (rule 13): passes. ORNL owns the repo and holds the copyright, and `pyproject.toml` lists ORNL as author. OSTI 2483434 (PEARC 2024) names ORNL as research org. [KNOWN: repo; https://www.osti.gov/biblio/2483434, research org ORNL, abstract names Zambeze] That's an in-repo source plus OSTI, so I'm marking it CORROBORATED pending Fact Checker.

## Plain-language walkthrough
- **What it is:** a Python system for running a science "campaign", a chain of tasks like moving data then processing it, across different computers, from big supercomputers to small "edge" machines near instruments. The README calls it "a distributed task orchestration system". [KNOWN: README]
- **The problem:** experiments often span facilities. Data comes off an instrument in one place, gets moved, and gets crunched somewhere else, and doing each step by hand is slow and error-prone. Zambeze lets you describe the steps once and have agents carry them out. [KNOWN: README purpose; INFERRED: the scenario] Scout's OSTI records tie it to cross-facility workflow research (PEARC 2024) and an OLCF report on DOE's Integrated Research Infrastructure (IRI). [KNOWN: catalog row]
- **Key terms:**
  - An *agent* is a background program running on each machine that waits for work.
  - A *message queue* (here RabbitMQ) is a post office that holds task messages until an agent picks them up.
  - A *DAG* (directed acyclic graph) is a to-do list where some steps must wait for others, with no loops. [KNOWN: `zambeze start`, `queue_rmq.py`, `campaign/dag.py`, compose.yaml; INFERRED: the definitions]
- **What goes in:** a short Python script that builds a `Campaign` out of activities, such as a `ShellActivity` (run a command) or a `TransferActivity` (move files). [KNOWN: `examples/imagemagick_files.py`, `src/zambeze/campaign/`]
- **What happens:**
  1. You start the agent with `zambeze start`.
  2. Your script dispatches the campaign.
  3. Activities become messages on the queue.
  4. Agents pick them up, check them, run them through plugins, and record state in a small SQL database. [KNOWN: README usage, `orchestration/` files, `db/zambeze_schema.sql`; INFERRED: the flow]
- **What comes out:** the task's results, such as files produced, plus logs and status records. [INFERRED]
- **Where humans act:** a scientist writes the campaign script, starts and stops agents, and sets up any Globus account for transfers. [KNOWN: README; `globus` test markers] We didn't set up or use any accounts.
- **What it is not:** it isn't a job scheduler like Slurm, which decides when jobs run on a cluster, and it isn't a data-transfer service itself. It drives tools like Globus or rsync. [INFERRED: from deps and test markers]
- **What's unknown:** whether it's still used, whether Flowcept or another tool took over its role, and why the docs site doesn't respond.
- **Example:** the README's demo has a shell activity run ImageMagick (an image tool) to turn a folder of images into an animated GIF. [KNOWN: README, the example's docstring]

## How it works
- **Messaging:** messages travel over RabbitMQ (through the `pika` library), and ZeroMQ (`pyzmq`) is also a dependency. Docker Compose files spin up a RabbitMQ broker and two agent containers for testing. [KNOWN: pyproject dependencies, `compose.yaml`, `deployment/README.md`]
- **Plugins:** each action type is a plugin with a message validator and a template generator. The shipped plugin module is `shell`. [KNOWN: `orchestration/plugin_modules/`]
- **Transfers:** `globus_sdk` is a dependency, and the tests have Globus-specific markers. Globus is a widely used research data-transfer service. [KNOWN: pyproject.toml]
- **Provenance hook:** if Flowcept is turned on in settings, the agent loads Flowcept's `ZambezeInterceptor` to record what ran. Provenance means a record of where results came from. [KNOWN: `src/zambeze/orchestration/agent/message_handler.py` lines 69-76, `deployment/compose-flowcept.yml`] That's code-level evidence for the Flowcept pairing Connector already mapped (link 114).

## How the project is organized
- `src/zambeze/` contains:
  - `campaign/` for the user-facing Campaign, activities and DAG.
  - `orchestration/` for the agent, queue, executor, plugins, monitor and messages.
  - `db/`, plus `cli.py` and `cli_agent.py`.
- The other folders are `examples/`, `tests/`, `docs/` (Sphinx), and `deployment/` (Dockerfile and compose files). [KNOWN: repo tree]
- Languages: Python about 99.8% by bytes. [KNOWN: GitHub languages API]
- Build: hatchling (a Python packaging tool), Python 3.10 or newer, and two command-line entry points, `zambeze` and `zambeze-agent`. [KNOWN: pyproject.toml]
- CI: GitHub Actions `checks.yml`, `tests.yml` and `integration-tests.yml`. [KNOWN]
- Contributors: 11 including anonymous commit authors, 8 GitHub accounts without them. 1,061 commits since 2022-04-14. 10 stars and 2 forks. [KNOWN: GitHub API, git log]
  - Correction for the catalog: Scout's row says "2 contributors". The API's contributor pages give 8 and 11. [KNOWN]

## Who uses it / why it matters
It's an early ORNL attempt at the "connect instruments and supercomputers" problem that DOE's IRI effort targets. [INFERRED from the OSTI titles in the catalog row] For usage evidence, see Connector's section in `signals/zambeze.md`.

## Related projects
- Flowcept (`flowcept`): an optional provenance integration in the code. [KNOWN]
- Globus and RabbitMQ: outside dependencies.

## Known / Inferred / Unknown
- KNOWN: license, owner, releases, dates, dependencies, layout, the Flowcept hook, counts.
- INFERRED: the cross-facility scenario, that 0.2 was never published, the comparisons to Slurm and Globus.
- UNKNOWN: current use, any successor, the status of the docs site.

## Sources (accessed 2026-10-24)
- https://github.com/ORNL/zambeze (README.md, LICENSE, pyproject.toml, compose.yaml, deployment/, src/zambeze/, examples/imagemagick_files.py, .github/workflows/)
- https://api.github.com/repos/ORNL/zambeze (plus /languages, /releases, /contributors)
- https://pypi.org/pypi/zambeze/json
- https://www.osti.gov/biblio/2483434 and https://www.osti.gov/biblio/2477506 (per Scout's catalog row)

## Sweep 2 notes (ORNL Fact Checker, 2026-10-24)
- Verified on a fresh clone and the public feeds: MIT LICENSE "Copyright (c) 2022 Oak Ridge National Laboratory", pyproject version 0.2 with ORNL as author, PyPI latest 0.1 (releases 0.1 and 0.1.dev0), last main commit 2024-09-13, contributors 11 with anonymous and 8 accounts, Flowcept hook (setting check, import and `ZambezeInterceptor()`).
- Corrected: the Flowcept hook path is `src/zambeze/orchestration/agent/message_handler.py`, lines 69-76, not lines 70-77 of a top-level file. The rule 13 citation now points at OSTI 2483434 directly; its abstract names Zambeze and ORNL is research org, so CORROBORATED holds.
- OSTI 2477506 (OLCF ACE FY24) doesn't name Zambeze in its abstract, so it supports only a general cross-facility context, not the project tie.
- docs.zambeze.org non-response is left as logged. I didn't retry other paths (rule 16).

## Batch 09 note: does current Flowcept still support Zambeze? (accessed 2026-10-24)
- **Short answer:** not the way Zambeze's code expects. [KNOWN]
- **What Zambeze needs:** `message_handler.py` lines 69-76 import `ZambezeInterceptor` and `FlowceptConsumerAPI` from `flowcept`. [KNOWN]
- **What current Flowcept has:** at its default-branch HEAD (`main`, c000b10, 2026-07-20 UTC), neither of those names exists anywhere in the source. [KNOWN: repo search]
- **What's left behind:**
  - A settings kind called "zambeze" (`commons/vocabulary.py` line 15), with special handling in `commons/settings_factory.py` line 45.
  - A comment in `resources/sample_settings.yaml`.
  - `flowceptor/adapters/brokers/mqtt_interceptor.py`, whose docstrings still say "Zambeze interceptor" even though the class is now a generic MQTT broker interceptor. [KNOWN]
- **What that means:** turning on Flowcept in Zambeze with current Flowcept would most likely fail at the import. The leftover names look like traces of the old integration, not working support. [INFERRED: I didn't run it] This matches Fact Checker's finding for link 114.
