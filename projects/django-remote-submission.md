# Django Remote Submission (DRS)
- Official page / Docs: https://django-remote-submission.readthedocs.org (README link) [KNOWN: README]
- Repo: https://github.com/ornl-ndav/django-remote-submission [KNOWN]
- Package: https://pypi.org/project/django-remote-submission/ (latest 2.1.0, uploaded 2018-05-18) [KNOWN: PyPI JSON API]
- Paper: JOSS, DOI 10.21105/joss.00366, plus a Zenodo archive DOI 10.5281/zenodo.848749 [KNOWN: README badges]
- License: ISC, "Copyright (c) 2017, Oak Ridge National Laboratory" [KNOWN: LICENSE]
- Status: unknown. Not archived, but the last push was 2021-11-18 and the last release 2018. [KNOWN: GitHub API, PyPI] It's dormant in practice. [INFERRED]
- ORNL relationship: KNOWN. The license names ORNL as copyright holder, and the paper's only listed affiliation is ORNL. [KNOWN: LICENSE, paper.md] That passes rule 13 even though `ornl-ndav` is a side org.
- Years visible in public sources: 2016 to 2021
- Last checked: 2026-10-24

## Walkthrough (plain language)
- **What it is:** a plug-in for Django (a Python web framework) that lets a website start a long job on another computer over SSH, stream the job's log back live, and collect the result files. [KNOWN: README features]
- **Key terms:**
  - **SSH:** the standard encrypted way to log into and run commands on a remote Linux machine.
  - **Celery and Redis:** Celery runs slow tasks in the background so the website doesn't freeze. Redis is the message broker that passes "do this task" notes from the website to the Celery workers. [KNOWN: paper.md]
  - **WebSockets (Django Channels):** a connection that stays open so the server can push updates to your browser without you hitting refresh. [KNOWN: paper.md, README]
- **The problem:** the paper's case is the Liquids Reflectometer instrument at SNS. Fitting data is slow and scientists didn't want to install software or write scripts, so a web page needed a way to run the fitting on a cluster and show progress. [KNOWN: paper.md "Practical case"]
- **What goes in:** a Server record (host, port), a Job record (the script to run and an interpreter), and SSH credentials as a password or key. [KNOWN: README quickstart; `models.py` classes Interpreter, Server, Job]
- **What happens:**
  1. The website calls the `submit_job_to_server` task. [KNOWN: `tasks.py`]
  2. Celery picks it up through Redis. [KNOWN: paper.md]
  3. A wrapper (`wrapper/remote.py` over SSH with paramiko, or `local.py`) copies the script over and runs it. [KNOWN: tree, `setup.py` requires paramiko]
  4. Standard output and error are saved as Log rows and pushed live over WebSockets. [KNOWN: README; `models.py` Log]
  5. When it finishes, the files that changed come back as Result rows. [KNOWN: README; `models.py` Result]
  6. The job status moves through initial, submitted, then success or failure. [KNOWN: README; `models.py` STATUS]
- **What comes out:** the job's status, a live log and the returned files, available through the Django admin, a REST API and WebSockets. [KNOWN: `admin.py`, `serializers.py`, `consumers.py`]
- **Where humans act:** a scientist clicks "fit" in a web interface. A developer wires DRS into that site and sets up the servers. [KNOWN: paper.md; INFERRED: the developer's role]
- **What it is not:** it isn't a batch scheduler like Slurm. It runs a script over SSH, which can then hand off to a cluster. It also isn't part of the SNS autoreduction pipeline in our neutron deep dive. [KNOWN: features; INFERRED: the pipeline relationship, since no code link was found]
- **What's unknown:** whether the reflectivity fitting site still uses it.
- **Example:** a reflectometry user sets up a REFL1D fit in the web page. DRS sends the fit to a cluster, the user watches the log scroll by live, and the fitted curves come back to the page. [KNOWN: paper.md]

## What it is (plain English, 2-4 sentences)
A small, reusable piece of a website that turns "run this script on that server" into a tracked job with live logs and saved results. It was built for a neutron instrument's web-based data fitting and released as a general Django package with a short peer-reviewed software paper. [KNOWN: README, paper.md]

## How it works (plain English, no jargon without definition)
See the walkthrough steps above. There are also `copy_job_to_server` (copy without running), plus `copy_key_to_server` and `delete_key_from_server`, which install or remove an SSH public key on the remote machine so later jobs can log in without a password. [KNOWN: `tasks.py` lines 324-423; HISTORY 2.1.0]

## How the project is organized
- Language: Python (Django app). Tests use pytest and tox, and CI was on Travis CI with Codecov badges. [KNOWN: `pytest.ini`, `tox.ini`, README badges] Travis badges like these often stopped working after Travis's 2021 changes. [INFERRED, not checked]
- Layout: `django_remote_submission/` (models, tasks, consumers, routing, serializers, views, wrapper), `example/` (a demo Django project with a Redis config), `tests/`, `docs/`, and `paper.md` with `paper.bib` for the JOSS paper. [KNOWN: tree]
- Dependencies: Django 2.0, Celery 4.1 or newer, Channels 2.1.1 or newer, paramiko. Version 2.0 dropped Python 2. [KNOWN: `setup.py`, HISTORY]
- Has CONTRIBUTING.rst, AUTHORS.rst and codemeta.json (machine-readable software metadata). [KNOWN: tree]
- Contributors: 7 including anonymous authors, 5 accounts. 20 stars, 5 forks, 2 open issues. [KNOWN: GitHub API, 2026-10-24]
- Why they chose Celery and Channels over alternatives: [UNKNOWN; not stated]

## Timeline
| Date | Event | Source | Tag |
|---|---|---|---|
| 2016-09-27 | Repo created | GitHub API | KNOWN |
| 2016 to 2017 | 70 then 148 commits | git log | KNOWN |
| 2017 | JOSS paper and Zenodo DOI | README badges | KNOWN |
| 2017-11-13 | v1.2 adds REST API filtering | HISTORY.rst | KNOWN |
| 2018-04-19 | v2.0.0 moves to Channels 2.0, Python 3 only | HISTORY.rst | KNOWN |
| 2018-05-18 | v2.1.0, last PyPI release | HISTORY.rst, PyPI | KNOWN |
| 2020-06-12 | Last commit: "Remove old py2 compatibiity" | git log | KNOWN |
| 2021-11-18 | Last push | GitHub API | KNOWN |

## Who uses it / why it matters
- The SNS Liquids Reflectometer fitting web interface, per the paper. [KNOWN: paper.md] Current use is [UNKNOWN].
- It's on PyPI, so anyone can install it. Download counts weren't checked. [KNOWN; UNKNOWN]

## Related projects
Filled by the connections pass, matching connections/map.md.
| Related item | Relationship (uses, extends, shares data, same facility, related topic, unknown) | Source | Tag |
|---|---|---|---|
| SNS Liquids Reflectometer | same facility (its practical case) | map link 199; https://doi.org/10.21105/joss.00366 | KNOWN |
| live-data-server | related topic (both Django web tools; no code link) | map link 200 | INFERRED |
| data-workflow and neutrons group | unknown (no shared code or contributors found) | map link 38 | UNKNOWN |

## What stands out
- It shows the neutron facilities building web tools so scientists don't have to install software. That's the same instinct as WebMon and live-data-server in the SNS deep dive, just for analysis instead of reduction. [INFERRED]
- The code handles passwords and installs SSH keys on remote machines, which makes it a compact real-world case study in credential handling for a security student. [KNOWN: `tasks.py`; INFERRED: the teaching value]

## Ten questions (GOAL.md)
1. **Problem and for whom:** running slow remote jobs from a web page with live logs. It was built for SNS reflectometry users. [KNOWN: paper.md]
2. **Where in the tree:** ORNL, then neutron sciences (SNS), then the Liquids Reflectometer's analysis web tools. [KNOWN: paper.md] The `ndav` org name probably means neutron data analysis and visualization. [INFERRED, not stated]
3. **Who pays:** OSTI 1394387 ("Django Remote Submission") lists only USDOE as sponsor. The related "Web interface for reflectivity fitting" record (OSTI 1470800) lists USDOE and the Office of Science, Basic Energy Sciences. [KNOWN: OSTI API, 2026-10-24] The paper's acknowledgment says the work used HFIR and SNS, "a DOE Office of Science User Facility". [KNOWN: paper.md] That makes BES likely for DRS too, but no record says so. [INFERRED]
4. **Organized how:** a Python Django app with Celery, Redis, Channels and paramiko, plus tests, docs and an example project. [KNOWN]
5. **Alive?** It's dormant, with bursts in 2016-17, a last release in 2018 and a last commit in 2020. [KNOWN]
6. **Outside users:** JOSS citations weren't checked. 20 stars and 5 forks. [KNOWN; UNKNOWN]
7. **Connections:** upstream are Django, Celery, Redis, Channels and REFL1D (the fitting code). Downstream is the reflectivity fitting web interface. [KNOWN: paper.md]
8. **What it teaches about ORNL:** facility teams sometimes package a one-off tool for general use and publish a short software paper so it gets credit and citations. [KNOWN: JOSS paper; INFERRED: the lesson]
9. **Student angle:** a strong read for a security student, covering SSH automation, key management, message brokers and WebSockets in a small codebase with tests and a CONTRIBUTING file. To run it you'd need Python, Redis and a test SSH server you own. Contributing would mostly mean modernizing it for current Django and Channels, and there's no sign anyone is reviewing PRs. [KNOWN: tree; INFERRED]
10. **Unknown and searched without result:** current use and JOSS citations (not checked). The OSTI search found 1394387 and 1470800.

## Known / Inferred / Unknown
- [KNOWN] purpose, design, dependencies, history, license, paper, SNS use case.
- [INFERRED] dormancy, the meaning of `ndav`, the link to the SNS web-tool pattern.
- [UNKNOWN] the specific funding office, current use, citations.

## Verification notes
_Filled by the fact-check pass._

## Sources (accessed 2026-10-24)
- https://github.com/ornl-ndav/django-remote-submission (README.rst, LICENSE, HISTORY.rst, paper.md, codemeta.json, setup.py, `django_remote_submission/models.py`, `tasks.py`, tree)
- https://api.github.com/repos/ornl-ndav/django-remote-submission (and /contributors)
- https://pypi.org/pypi/django-remote-submission/json
- https://www.osti.gov/api/v1/records?q="Django Remote Submission" (records 1394387, 1470800)
- https://doi.org/10.21105/joss.00366 (named in the README; not fetched)

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Verified: ISC license, repo created 2016-09-27, last push 2021-11-18, last commit 2020-06-12, last PyPI release 2.1.0 on 2018-05-18, the paper's Liquids Reflectometer case at SNS, OSTI 1394387 (USDOE only, the JOSS DOI) and 1470800 (USDOE plus BES). No corrections.
