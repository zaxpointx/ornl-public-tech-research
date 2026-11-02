# OLCF User Documentation
- Official page: https://docs.olcf.ornl.gov (rendered site, linked from the README) [KNOWN: README]
- Repo: https://github.com/olcf/olcf-user-docs [KNOWN]
- Docs: the repo is the docs, written in reStructuredText and built with Sphinx [KNOWN: `conf.py`]
- License: none stated. GitHub's API returns no license, and the Sphinx config sets the copyright line to the current year and "OLCF" [KNOWN: GitHub API, `conf.py` line 31, accessed 2026-10-24]
- Status: active. Last push 2026-10-23, with commits every year since 2019 [KNOWN: GitHub API, git log]
- Scope (rule 13): the `olcf` org is a side org, so it needs other proof. The README names the Oak Ridge Leadership Computing Facility, links the rendered site on an ornl.gov host, and gives OLCF User Assistance as the contact. That counts as ORNL credited in the README. [KNOWN: README] No OSTI record exists, which is expected since this is documentation, not a code record. [KNOWN: catalog note]

## Plain-language walkthrough
- **What it is:** the source files for the public manual for OLCF's supercomputers and services. Edits here become the docs website after a build. [KNOWN: README]
- **Key terms:**
  - **reStructuredText (`.rst`):** a plain-text markup language, like Markdown with more features, used by a lot of Python and HPC docs.
  - **Sphinx:** the tool that turns `.rst` files into a website. [KNOWN: `conf.py`, contributing guide]
  - **Docs-as-code:** keeping a manual in Git so changes go through issues and pull requests like software. [INFERRED from the README's issue and PR workflow]
- **The problem:** thousands of researchers need accurate, current instructions for accounts, connecting, compiling, running jobs, moving data and using software on machines that change often. [INFERRED from the top-level folders]
- **What goes in:** text edits from staff and outside contributors, as pull requests. [KNOWN: README "Just send us a Pull Request"]
- **What happens:** a contributor forks, edits the `.rst`, builds locally with `make html` or `sphinx-build`, previews in a browser and opens a PR. [KNOWN: `contributing/index.rst`] How the merged docs get published to the live site isn't shown in the repo. There's no CI workflow folder in it. [KNOWN: tree; UNKNOWN: the publish step]
- **What comes out:** the docs website, with sections for accounts, connecting, systems, software, data, services, training, quantum computing and support. [KNOWN: top-level folders, `index.rst`]
- **Where humans act:** facility staff write and review. The README offers issues for suggestions and PRs for changes from anyone. [KNOWN: README; INFERRED: staff as reviewers]
- **What it is not:** it isn't software, and it isn't the OLCF test harness. We read it as a document about how a facility explains itself, not as a map of systems (rule 16).
- **What's unknown:** the publish pipeline, and who reviews outside PRs.
- **Example:** someone who's new to Frontier opens the Frontier user guide (`systems/frontier_user_guide.rst`), which is one file in this repo. [KNOWN: file exists]

## How it works
- One `.rst` file or folder per topic. `systems/` holds one user guide per machine, including Frontier, Summit, Andes and several smaller or test systems. [KNOWN: `systems/` file names] We list the file names only and didn't extract system details from them.
- `software/` covers compilers, Python, containers on Frontier, Spack environments, profiling, debugging, visualization and workflows. [KNOWN: folder names]
- `services_and_applications/` covers web services like Jupyter, myOLCF, Slate and an inference service. [KNOWN: folder names]
- There's also an AI and computing testbed area (`ace_testbed/`), quantum computing access (`quantum/`) and training, including GPU hackathons and a training archive. [KNOWN: folder names]
- Theme: `sphinx_rtd_theme` (the Read the Docs look), plus `sphinx_design` and `sphinx_copybutton`. The contributing guide pins Sphinx 7.4.7. [KNOWN: `conf.py`, `contributing/index.rst`]

## How the project is organized
- Languages and build: reStructuredText plus a Sphinx `conf.py`, `Makefile` and `make.bat`. Images live in `images/` and `_static/`. [KNOWN: tree]
- History: 2,877 commits from 2019-06-19 to 2026-10-22 [KNOWN: git log]. Commits per year: 2019: 336, 2020: 288, 2021: 271, 2022: 515, 2023: 422, 2024: 411, 2025: 324, 2026: 310 (to 2026-10-22). [KNOWN: git log] The peak in 2022-23 lines up with Frontier's debut and opening. [INFERRED; dates from the test harness timing notes]
- Contributors: 145 distinct author emails in git, and the GitHub API's first page is full at 100 entries including anonymous authors, 66 of them accounts. [KNOWN: git log, GitHub API page 1; the full API count is higher than 100]
- Default branch `master`. 67 stars, 124 forks, 8 open issues. [KNOWN: GitHub API, 2026-10-24]
- Org unit: OLCF User Assistance is the named contact. [KNOWN: README]

## Who uses it / why it matters
- OLCF users. It's the front door for anyone given time on the machines. [INFERRED from the content]
- 124 forks is unusual for a docs repo, which suggests many people have proposed edits or copied the layout. [KNOWN: count; INFERRED: why]

## Related projects
Filled by the connections pass, matching connections/map.md.
| Related item | Relationship (uses, extends, shares data, same facility, related topic, unknown) | Source | Tag |
|---|---|---|---|
| OLCF Test Harness | same facility | map links 43, 181; https://github.com/olcf/olcf-test-harness | KNOWN |
| DataFed | same facility (services hosted in OLCF) | map links 51, 128 | CORROBORATED |
| Flowcept | same facility (OLCF acknowledgment) | map link 8 | KNOWN |
| HydraGNN | same facility (Frontier scripts, Constellation) | map links 9, 26 | KNOWN |
| ExaTN | same facility (Summit build notes) | map link 10 | KNOWN |
| ExaGO | same facility (Frontier build scripts) | map link 170 | KNOWN |
| HeCBench | related topic (links OLCF training material) | map link 155 | KNOWN |

## Timeline
| Date | Event | Source | Tag |
|---|---|---|---|
| 2019-06-19 | First commit | git log | KNOWN |
| 2019 to 2021 | About 270 to 340 commits a year | git log | KNOWN |
| 2022 | Peak year, 515 commits | git log | KNOWN |
| 2022 to 2023 | Frontier debuts and opens to users (likely cause of the peak) | test harness timing notes | INFERRED |
| 2026-10-22 | Latest commit seen | git log | KNOWN |

## What stands out
- It's the only project in the catalog where the main thing being built is writing, not code, and it's still updated most weeks seven years in. [KNOWN: history; INFERRED: the comparison]
- With no license file, it's public to read but not clearly reusable. That's an odd gap for a repo that invites outside edits. [KNOWN: no LICENSE; INFERRED]

## Known / Inferred / Unknown
- [KNOWN] purpose, Sphinx build, folder layout, contribution steps, commit history, contact.
- [INFERRED] the activity peak around Frontier, and the forks pointing to outside edits.
- [UNKNOWN] the license, the publish pipeline, and how outside PRs are reviewed.

## Verification notes
_Filled by the fact-check pass._

## Sources (accessed 2026-10-24)
- https://github.com/olcf/olcf-user-docs (README.md, conf.py, contributing/index.rst, tree)
- https://api.github.com/repos/olcf/olcf-user-docs (and /contributors)
- https://docs.olcf.ornl.gov (named in the README; not crawled)

## GOAL.md questions (added 2026-10-24)
- **Problem and for whom (Q1):** clear instructions for researchers using OLCF machines. [INFERRED]
- **Where in the tree (Q2):** ORNL, then computing, then OLCF, then User Assistance. [KNOWN: README contact]
- **Who pays (Q3):** no record. [UNKNOWN] OLCF itself is a DOE Office of Science user facility (see the olcf-test-harness brief), but nothing ties funding to the docs. [INFERRED, not to be stated as fact]
- **Organized how (Q4):** see above. It's reStructuredText and Sphinx, one folder per topic.
- **Alive? (Q5):** yes, with steady commits every year since 2019 and a peak in 2022-23. [KNOWN]
- **Outside users (Q6):** 124 forks and 66+ contributing accounts. Whether the contributors are outside the lab isn't checked, by our people-by-role rule. [KNOWN: counts; UNKNOWN: who]
- **Connections (Q7):** the facility's machines and services. The test harness and DataFed are neighbors. [INFERRED]
- **What it teaches about ORNL (Q8):** a big facility runs its user manual as an open Git project and takes edits from anyone. That's a cheap, public window into how the lab supports users. [KNOWN: README; INFERRED: the lesson]
- **Student angle (Q9):** this is the easiest real contribution in the catalog. Fixing a typo or an unclear step in the docs only needs Git, a text editor and `pip install sphinx`, with no supercomputer. The contributing guide walks through every step. [KNOWN: `contributing/index.rst`; INFERRED: the ease]
- **Searched without result (Q10):** an OSTI record (none, expected for docs); a CI or publish workflow in the repo (none); a license file (none).

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Verified: no license in the GitHub API, 67 stars, 124 forks, 8 open, default branch master, last push 2026-10-23. No corrections.
