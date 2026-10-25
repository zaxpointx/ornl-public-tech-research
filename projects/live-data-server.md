# Live Data Server
- Official page: https://livedata-ornl.readthedocs.io/en/latest/ (developer docs)
- Repo: https://github.com/neutrons/live_data_server (default branch `next`)
- Docs: the Read the Docs site above, from `docs/` in the repo
- License: BSD 3-Clause. Quote: "Copyright (c) 2024, OAK RIDGE NATIONAL LABORATORY" [KNOWN: https://github.com/neutrons/live_data_server/blob/next/LICENSE, line 3]
- Status: active [KNOWN: last push 2026-10-21 UTC, release v1.5.0 on 2026-02-03 UTC, GitHub API]

## Plain-language walkthrough
- **What it is:** a small website that stores plots of neutron experiment data and shows them in a browser. The repo describes it as a "Data server for data plots." [KNOWN: README]
- **The problem:** scientists want to see a run's plots, during or right after the experiment, without logging into the analysis computers.
- **What goes in:** other programs upload a ready-made HTML plot for an instrument and run number. Uploads need credentials. [KNOWN: `upload_plot_data` and `check_credentials` in `src/apps/plots/views.py`]
- **What happens:** it saves the plot in a Postgres database, tagged with instrument, run number and an expiration date. [KNOWN: `models.py`]
- **What comes out:** a web page per instrument and run, under `/plots/`. [KNOWN: `src/config/urls.py`]
- **Where humans act:** scientists view the plots. Admins deploy it and set its secrets.
- **What it is not:** it doesn't make the plots or reduce data. It only stores and serves what it's given. [INFERRED: there's no plotting or reduction code in `src/`]
- **What's unknown:** who exactly uploads to it. Where it's deployed is out of scope under rule 16, which bars mapping infrastructure, and we won't look for it.
- **Example:** after a run on an instrument (the list includes SNS and HFIR names like `arcs` and `hb2b`), a reduction job uploads an HTML plot for that run number. A scientist then opens the run's page in a browser, and the plot stays up for 3 years by default before expiring. [KNOWN: `src/config/instruments.py`, settings.py "expiration time for live plots to 3 years if not set"; INFERRED: that a reduction job is the uploader]

## How it works
- **Django:** it's built with Django, a Python web framework. Django gives you database tables ("models"), web addresses ("URLs") and an admin page out of the box. [KNOWN: `manage.py`, `django.urls` imports]
- **Data model:** there are tables for instruments, data runs (a run groups related plots) and the plot data itself. Only HTML plots are supported. [KNOWN: `models.py`, `DATA_TYPES = {"html": 1}`]
- **Deployment:** it runs in Docker containers next to a Postgres database. The README documents environment variables for database settings and a secret key. [KNOWN: README "Setup for Local Development"] The docs also cover serving it through Apache. [KNOWN: `docs/developer/service_through_apache.rst`]

## How the project is organized
- `src/config/` holds the settings, URLs and instrument list. `src/apps/plots/` holds the one app (models, views, upload handling, tests, migrations). There's also `deploy/` (Docker Compose files), `docs/` (Sphinx on Read the Docs), `scripts/`, `tests/`, and `pixi` and `pyproject` environment files. [KNOWN: repo tree]
- Languages: HTML (about 48%) and Python (about 45%). [KNOWN: GitHub languages API]
- Contributors: about 14. Created 2016-05-27. Releases include 1.3/1.4 (2024-11-22) and v1.5/v1.5.0 (2026-02-03). [KNOWN: GitHub API]

## Who uses it / why it matters
It's the "show me my plot" step at the end of the neutron data pipeline. [INFERRED] It's a good small, readable example of a Django service with authenticated uploads, which is useful for studying web-app security basics. [INFERRED]

## Related projects
- data-workflow (`data-workflow`): Connector's map link 91 ties the two. [KNOWN per Connector; not re-read by me]
- post-processing-agent (`post-processing-agent`): the likely uploader of live plots. [INFERRED: no upload call checked in the agent's code]
- Mantid (`mantid`): makes the data that ends up plotted. [INFERRED]

## Known / Inferred / Unknown
- KNOWN: BSD-3 license with ORNL copyright, Django and Postgres design, HTML-only plots, 3-year default expiry, instrument list, layout, stats.
- INFERRED: who uploads, the pipeline role.
- UNKNOWN: owning group. Production URL: out of scope (rule 16), not researched.

## Sources (accessed 2026-10-24)
- https://github.com/neutrons/live_data_server (README.md, LICENSE, src/, docs/)
- https://livedata-ornl.readthedocs.io/en/latest/
- https://api.github.com/repos/neutrons/live_data_server (plus /languages, /releases, /contributors)

## Sweep 2 notes (ORNL Fact Checker, 2026-10-24)
- Sweeps 1 and 2 done against the GitHub API and raw files on `next`.
- Verified:
  - BSD-3 with "Copyright (c) 2024, OAK RIDGE NATIONAL LABORATORY", created 2016-05-27, last push 2026-10-21, HTML 47.7% / Python 45.2%, contributors 14.
  - Releases v1.1 to 1.4 (2024-11-22) and v1.5/v1.5.0 (2026-02-03).
  - README "Data server for data plots.", `check_credentials` and `upload_plot_data` in views.py, `DATA_TYPES = {"html": 1}`, the 3-year expiry comment in settings.py, `arcs` and `hb2b` in instruments.py, and that the Apache doc and the RTD site resolve.
- Corrected: I reworded the production-URL item. Per rule 16 it's out of scope, not an open question.
- The README's local-dev example has placeholder credentials. They're not copied here and they're not relevant.
