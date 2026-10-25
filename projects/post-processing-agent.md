# Post Processing Agent
- Official page: https://github.com/neutrons/post_processing_agent (no separate docs site found)
- Repo: https://github.com/neutrons/post_processing_agent
- Docs: `README.md` and `README_developer.md` in the repo
- License: MIT. The license file reads "Copyright (c) 2022 NScD" [KNOWN: https://github.com/neutrons/post_processing_agent/blob/main/LICENSE.rst, top line]. ORNL ownership: the Calvera processor's header says "@copyright: 2023 Oak Ridge National Laboratory" [KNOWN: `postprocessing/processors/calvera_processor.py`, file docstring]. That NScD means ORNL's Neutron Sciences Directorate is [INFERRED].
- Status: active [KNOWN: last push 2026-10-21 UTC, release v4.6.0 on 2026-10-16 UTC, GitHub API]

## Plain-language walkthrough
- **What it is:** a background service that does the cleanup work automatically each time a neutron experiment finishes a "run" (one recorded block of measurement).
- **The problem:** neutron instruments at ORNL's SNS and HFIR facilities produce raw event files. Scientists need those files listed in a catalog and turned into usable results ("reduced"), and doing that by hand for every run doesn't scale.
- **What goes in:** a message saying "this run's raw data is ready", sent through a message broker called ActiveMQ.
- **What happens:** the agent picks up the message, runs the right job (catalog the raw file, run that instrument's reduction script, catalog the reduced output, or write a reduction script), and enforces time and memory limits.
- **What comes out:** reduced data files, catalog entries, and "complete" or "error" messages sent back to the broker.
- **Where humans act:** instrument staff write or tune each instrument's reduction script and set up the config. Scientists look at the results.
- **What it is not:** it isn't the reduction math itself (that's Mantid), and it isn't the web dashboard (that's data-workflow).
- **What's unknown:** which team owns it. How many servers run it is out of scope under rule 16, and we won't look for it.
- **Example:** a run finishes on an instrument. A "data ready" message lands in that instrument's reduction queue, the agent runs its script under a 60-minute default limit, and then a "reduced data ready" message triggers cataloging. [KNOWN: queue design and the 60-minute default in `README_developer.md` and `README.md`; INFERRED: the step order as one story]

## What it is
This is the new version of the automated reduction and cataloging agent. The README points to `mantidproject/autoreduce` for the old version. [KNOWN: README.md opening lines] The repo was created in 2014. [KNOWN: GitHub API created_at 2014-05-16]

## How it works
- **Message queues:** a message broker is a post office for programs. Senders drop messages into named queues, and listeners pick them up. The agent is an ActiveMQ client that subscribes to one queue per task. [KNOWN: README_developer.md "Tasks and queues"] There are four tasks: catalog raw data, reduce data, catalog reduced data, and create a reduction script. [KNOWN: README_developer.md, quote: "There are four tasks handled by the Post Processing Agent"]
- **Per-instrument queues:** queues can be split per instrument, so one busy instrument doesn't hold up the others. The agent also finds new instrument queues without restarting. [KNOWN: README_developer.md "Per-instrument queues"]
- **Safety limits:** it kills a task that goes over its time limit or memory share. The README's example config sets 60 minutes (`task_time_limit_minutes`) and 70% of system memory (`system_mem_limit_perc`). [KNOWN: README.md "Task time and memory limits"; INFERRED: that these are the shipped defaults]
- **Heartbeats:** it sends regular "I'm alive" messages so monitoring can tell it's running. [KNOWN: README_developer.md `heart_beat` setting]
- **Processors:** the code has plug-in processors for ONCat (the neutron data catalog), reduction, reduction-script creation, Calvera and INTERSECT. [KNOWN: `postprocessing/processors/` file names] What Calvera and INTERSECT are isn't explained in the repo. [UNKNOWN]

## How the project is organized
- `postprocessing/` holds the core: the queue consumer (`Consumer.py`, `queueProcessor.py`), the job runner (`PostProcessAdmin.py`) and `processors/`. Alongside it are `configuration/` (example configs), `systemd/` (a Linux service file, `autoreduce-queue-processor.service`), `SPECS/` and `rpmbuild.sh` (packaging as a Red Hat RPM), a `Dockerfile`, `tests/` and `scripts/`. [KNOWN: repo tree]
- Languages: about 97% Python. [KNOWN: GitHub languages API, Python 264,303 of 271,647 bytes]
- Contributors: about 18. [KNOWN: GitHub contributors API last page] Releases: 21 on GitHub, the latest six running v4.1.0 (2025-09-18) to v4.6.0 (2026-10-16). [KNOWN: GitHub releases API]

## Who uses it / why it matters
It's part of the automatic pipeline behind SNS and HFIR, so users can get reduced data soon after a run. [KNOWN: the catalog row and repo describe automated reduction for these facilities; INFERRED: the user benefit] For a security student, it's a clean real example of an event-driven system built on message queues and service accounts. [INFERRED]

## Related projects
- data-workflow (`data-workflow`): the workflow manager and dashboard that route runs. The README says the workflow manager can route each instrument's runs to its own queue. [KNOWN: README_developer.md]
- Mantid (`mantid`): reduction scripts run under Mantid's Python. [KNOWN: README.md "Mantid settings", `scripts/mantidpython.py`]
- ONCat (`oncat`): the catalog target. [KNOWN: processor names] We didn't touch ONCat itself, since it needs credentials.
- live-data-server (`live-data-server`): same org, and both feed data-workflow. [INFERRED]

## Known / Inferred / Unknown
- KNOWN: MIT license, ORNL copyright line in code, the four tasks and queues, limits, layout, stats.
- INFERRED: NScD meaning, the user benefit, the security angle.
- UNKNOWN: what Calvera and INTERSECT are, and the owning group. Deployment size is out of scope (rule 16).

## Sources (accessed 2026-10-24)
- https://github.com/neutrons/post_processing_agent (README.md, README_developer.md, LICENSE.rst, postprocessing/processors/calvera_processor.py)
- https://api.github.com/repos/neutrons/post_processing_agent (plus /languages, /releases, /contributors)

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Sweeps 1 and 2 done against the GitHub API and raw files on `main`.
- Verified:
  - MIT "Copyright (c) 2022 NScD", "@copyright: 2023 Oak Ridge National Laboratory" in calvera_processor.py, created 2014-05-16, last push 2026-10-21, contributors 18.
  - The README opening and the autoreduce pointer, plus "There are four tasks handled by the Post Processing Agent".
  - Per-instrument queues are "picked up without a restart", the `heart_beat` setting, the processor file list, and `systemd/autoreduce-queue-processor.service`.
- Corrected:
  - Python went from 96% to 97%.
  - The release range now notes there are 21 releases.
  - The 60 min / 70% figures are now the README's example config, with "defaults" INFERRED.
  - Deployment size was reworded as out of scope (rule 16).
- Note: the heartbeat topic name in README_developer.md is a public repo detail. It isn't repeated here, and we don't use it to map anything.
