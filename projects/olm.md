# ORIGEN Library Manager (OLM)
- Official docs: https://scale-olm.readthedocs.io [KNOWN: PyPI project links, README]
- Repo: ORNL's GitLab mirror https://code.ornl.gov/scale/code/olm and the PyPI page https://pypi.org/project/scale-olm/. Main development happens in a developer's personal GitHub repo, linked from PyPI and named in the README as "the main development repository"; we leave that account out of this brief. [KNOWN: README, PyPI] The reading pass didn't follow the GitLab mirror link (team rule), so the mirror is cited from the README and DOE CODE.
- Package: https://pypi.org/project/scale-olm/ (latest on PyPI 0.14.2, 2025-05-29; repo README says latest stable v0.14.3) [KNOWN: PyPI JSON API, README]
- DOE CODE: code-122128, "ORIGEN Library Manager", DOI 10.11578/dc.20240212.1, research org ORNL, sponsor NNSA [KNOWN: OSTI API, accessed 2026-10-24]
- License: BSD-3-Clause, "Copyright 2024 UT-Battelle, LLC" [KNOWN: PyPI license field, GitHub API]
- Status: active (last push 2026-06-12) [KNOWN: GitHub API]
- ORNL relationship: KNOWN. The OSTI record names ORNL as research org, and UT-Battelle holds the copyright. That passes rule 13 even though the repo is on a personal account.
- Years visible in public sources: 2023 to 2026
- Last checked: 2026-10-28

## Walkthrough (plain language)
- **What it is:** a Python command-line helper for SCALE, ORNL's licensed nuclear analysis suite. It builds and checks the data libraries SCALE uses for quick spent-fuel calculations. [KNOWN: OSTI description, README]
- **Key terms:**
  - **Spent fuel:** fuel that's been used in a reactor. It's full of new isotopes (atoms made during operation), and people need to know which ones and how much, for storage, transport and safety.
  - **ORIGEN:** SCALE's module that tracks how isotopes build up and decay over time. [KNOWN: README links SCALE/ORIGEN]
  - **Reactor library:** a pre-computed table of data for one fuel type over a range of conditions, so ORIGEN can answer fast instead of re-running a full physics model. [KNOWN: OSTI "enables rapid spent fuel calculations"; INFERRED: plain reading]
  - **ORIGAMI:** a SCALE tool that uses those libraries to do quick spent-fuel calculations for a whole fuel assembly. [KNOWN: OSTI, quickstart]
  - **TRITON / Polaris:** SCALE's detailed physics programs that OLM drives to make the library data. [KNOWN: variant names `triton_pin_uox_quick`, `polaris_bwr7x7_uox_quick`]
  - **UOX / MOX:** uranium oxide fuel, and mixed uranium and plutonium oxide fuel. [KNOWN: variant and collection names]
- **The problem:** building a reactor library by hand means writing many near-identical SCALE input files, running them, stitching the outputs together and checking them. OLM turns that into one config file and a few commands. [KNOWN: docs step-by-step; INFERRED: "by hand"]
- **What goes in:** a JSON config (`config.olm.json`) with six sections: `model`, `generate`, `run`, `assemble`, `check` and `report`. [KNOWN: tested `olm init` output, 2026-10-28]
- **What happens** (the `olm create` stages; each can be turned on or off with flags) [KNOWN: `olm create --help`]:
  1. **Generate:** fill an input template for every combination of settings, such as enrichment and coolant density. The quick UOX example writes 6 SCALE input files. [KNOWN: tested]
  2. **Run:** hand those inputs to SCALE's runtime, `scalerte`. [KNOWN: docs step-by-step]
  3. **Assemble:** combine the outputs into one library using OBIWAN, a tool that ships with SCALE. [KNOWN: docs]
  4. **Check:** run consistency tests on the library. [KNOWN: config `check` section]
  5. **Report:** produce a PDF summary. [KNOWN: quickstart, config `report` section]
- **What comes out:** an ORIGEN reactor library plus a PDF report, which ORIGAMI can then use. [KNOWN: quickstart]
- **Where humans act:** a nuclear analyst picks or edits the config and reviews the report and checks. [INFERRED]
- **What it is not:** it isn't a reactor simulator itself, and it doesn't replace SCALE. Without SCALE it can only do the generate step. [KNOWN: docs; tested]
- **What's unknown:** who outside ORNL uses it.
- **Example:** `olm init --variant triton_pin_uox_quick uox_quick` sets up a config for a single fuel pin of a common 17x17 assembly. Running the generate step then writes six SCALE input files. Each one describes the fuel, the cladding (the metal tube around the fuel) and boron-laced water, at a different setting. [KNOWN: tested 2026-10-28]

## What it is (plain English, 2-4 sentences)
OLM is a small, open, pip-installable wrapper around a big licensed code. It automates making and checking SCALE's spent-fuel data libraries. It's the rare piece of ORNL's nuclear tool chain with public code you can read and run. [KNOWN: README, OSTI, PyPI]

## Getting it running on a Mac (focus asked by the lead)
Tested on the team's Linux box on 2026-10-28, not on a Mac. Steps that are plain Python should carry over. [KNOWN: tested; INFERRED: carries over]
1. **Use Python 3.9 to 3.12.** The package says `>=3.9,<3.13`. [KNOWN: pyproject.toml] A recent Homebrew Python may be 3.13, so make a 3.12 environment, for example with `uv venv -p 3.12`. [INFERRED: the Homebrew default]
2. **Install from the source repo, not PyPI.** The PyPI 0.14.2 release lists only six dependencies (click, matplotlib, scipy, numpy, pytest, pydantic). It crashed for us on missing `h5py`, then `tqdm`. [KNOWN: PyPI requires_dist; tested] Cloning the repo and running `pip install .` installed v0.14.3, and `olm` worked. [KNOWN: tested]
3. **What works with no SCALE:** `olm init`, `olm schema`, and `olm create --generate --norun --noassemble --nocheck --noreport`. That last one writes real SCALE input files you can read. [KNOWN: tested]
4. **What needs SCALE:** run, assemble and check stop and ask for `SCALE_DIR` or `OLM_SCALERTE`. [KNOWN: tested error message] Generating a library needs SCALE 6.3.2 or later. [KNOWN: quickstart note] The docs' example path is a macOS SCALE app bundle, so SCALE itself has a Mac build. [KNOWN: docs step-by-step] SCALE is licensed, though, so we stop there. [KNOWN: scale brief]
5. **Realistic M4 Mac mini plan:** install from source and generate the quick UOX inputs. Then read them side by side with `data.olm.json` to see how one setting becomes a physics input. That's the learning; the heavy runs need the license. [INFERRED]

## How the project is organized
- Layout: `scale/olm/` (`__main__.py` CLI; `core.py`; `generate/` with comp, static, states, time and dynamic; `run.py`, `assemble.py`, `check.py`, `report.py`; `templates/`; `variants/`), `collection/` (about 30 fuel assembly types, for example `w17x17`, `ge10x10-8`, `svea100-0`, `mox_w17x17`), `docs/` (Sphinx), `notebooks/`, `examples/`, `testing/`, `data/`. [KNOWN: tree]
- Language: Python. Dependencies include click, h5py, jinja2 (templating), numpy, pydantic, scipy, structlog and tqdm. [KNOWN: pyproject.toml]
- Tests: pytest with hypothesis and coverage reporting via codecov. [KNOWN: pyproject.toml optional deps, codecov.yml]
- CI: GitHub Actions `test.yml` runs Python 3.9 to 3.12 on Ubuntu (no macOS job), plus `release.yml` and `auto-merge.yml`. [KNOWN: workflows]
- Docs: readthedocs with quickstart, step-by-step, config file and CLI and API references. [KNOWN: docs/source]
- Releases: 11 git tags, 11 PyPI releases since 2024-02-15. [KNOWN]
- Contributors: 5 including anonymous authors, 3 accounts, 6 git author emails. 4 stars, 2 forks, 4 open issues. [KNOWN: GitHub API, git log]
- Why it's developed on a personal account with an ORNL mirror: [UNKNOWN; not stated]

## Timeline
| Date | Event | Source | Tag |
|---|---|---|---|
| 2023-06-30 | GitHub repo created | GitHub API | KNOWN |
| 2024-02-14 | DOE CODE record code-122128 | OSTI | KNOWN |
| 2024-02-15 | First PyPI releases; earliest commit by committer date (earliest author date is 2023-03-27) | PyPI, git log | KNOWN (corrected in a fact-check pass, 2026-10-29) |
| 2024 to 2026 | 27, 17, then 49 commits (default branch, committer date; all branches give 32, 41, 53; 126 commits on all branches, 93 on default) | git log, fresh clone 2026-10-29 | KNOWN (corrected in a fact-check pass, 2026-10-29) |
| 2025-05-29 | PyPI 0.14.2 | PyPI | KNOWN |
| 2026-06-12 | Last push; README names v0.14.3 as stable | GitHub API, README | KNOWN |

## Who uses it / why it matters
- SCALE users who need custom ORIGEN libraries, for example for spent-fuel storage and transport analyses. [INFERRED from the OSTI description] Outside users are [UNKNOWN].

## Related projects
Filled by the connections pass, matching connections/map.md.
| Related item | Relationship | Source | Tag |
|---|---|---|---|
| [SCALE](scale.md) / ORIGEN | uses (builds ORIGEN reactor libraries; run and assemble need a SCALE install); map links 62, 210 | https://pypi.org/project/scale-olm/ ; https://code.ornl.gov/scale/code/olm (read-only mirror; main development is in a personal GitHub repo) ; DOE CODE 122128 | [KNOWN] |
| [VERA](vera.md) | related topic (VERA also bundles SCALE's ORIGEN); no OLM tie found; map link 203 | https://rsicc.ornl.gov/codes/ccc/ccc8/ccc-855.html | [INFERRED] |
| PyPI `scale-olm` | distribution (open, BSD-3-Clause, pip); map link 210 | https://pypi.org/pypi/scale-olm/json | [KNOWN] |
| NNSA | sponsor; map link 221 | https://www.osti.gov/doecode/biblio/122128 | [KNOWN] |

## What stands out
- The open helper is a window into a closed code. Its generated inputs show what a SCALE depletion model looks like without anyone needing SCALE's source. [KNOWN: tested; INFERRED]
- The PyPI release lists fewer dependencies than the code imports, which is an easy first contribution. [KNOWN: tested; INFERRED]
- NNSA sponsorship fits with spent-fuel accounting work, but we note the sponsor field only. [KNOWN: OSTI; INFERRED]

## Ten questions (GOAL.md)
1. **Problem and for whom:** automating SCALE's ORIGEN library builds and checks for nuclear analysts. [KNOWN]
2. **Where in the tree:** ORNL, then the SCALE code team, nuclear energy and fuel cycle. [KNOWN: SCALE links; INFERRED: the division]
3. **Who pays:** NNSA, per code-122128. [KNOWN]
4. **Organized how:** a Python CLI package with Sphinx docs, pytest and GitHub Actions. [KNOWN]
5. **Alive?** Yes, active through mid-2026. [KNOWN]
6. **Outside users:** none found. [UNKNOWN]
7. **Connections:** downstream of SCALE (TRITON, Polaris, OBIWAN) and upstream of ORIGAMI. [KNOWN: docs]
8. **What it teaches about ORNL:** even licensed codes grow open-source tooling around them. [INFERRED]
9. **Student angle:** yes. Install from source on Python 3.12, run the generate step, and read the inputs. A dependency fix for PyPI is a realistic first PR. [KNOWN: tested; INFERRED]
10. **Unknown and searched without result:** outside users. An OSTI search for "ORIGEN Library Manager" found only the code record. The macOS install wasn't tested on real Mac hardware.

## Known / Inferred / Unknown
- [KNOWN] purpose, sponsor, license, layout, CLI stages, the tested install and generate path, the PyPI dependency gap.
- [INFERRED] the Mac carry-over, who uses it.
- [UNKNOWN] outside users, why it lives on a personal account.

## Verification notes
_Filled by the fact-check pass._

## Sources (accessed 2026-10-28 unless noted)
- https://www.osti.gov/api/v1/records/code-122128 (2026-10-24)
- https://pypi.org/pypi/scale-olm/json and /0.14.2/json
- The main OLM development repo on GitHub, linked from the PyPI page (README.md, pyproject.toml, `.github/workflows/`, `docs/source/quickstart.rst`, `docs/source/step-by-step.rst`, `scale/olm/`)
- The GitHub API record for that repo (and its contributors list)
- Local test: Python 3.12 venv on the team's box, `pip install .` from a clone, `olm init` and `olm create --generate` only

## Fact-check notes (2026-10-29)
- Re-checked: GitHub API (BSD-3-Clause, created 2023-06-30, last push 2026-06-12, 4 stars, 2 forks, 4 open issues), PyPI (0.14.2 on 2025-05-29, 11 releases, six listed dependencies, UT-Battelle copyright), DOE CODE 122128 (ORNL research org, NNSA sponsor, BSD-3, release 2024-02-14), README wording on the GitHub main repo and ORNL GitLab mirror.
- Commit-count spot check against a fresh `--filter=blob:none` clone: the yearly counts match the default branch by committer date. Labels added; earliest author date is 2023-03-27. 11 tags and 6 author emails on default confirmed.
- Related-projects table is still empty, waiting for the connections pass.

## Fact-check notes (2026-10-29), official home
- DOE CODE 122128 lists https://code.ornl.gov/scale/code/olm as the repository. The README and the docs' Contributing page (https://scale-olm.readthedocs.io/en/stable/, "Locations") both say the main development repository is on GitHub with a read-only mirror on ORNL's GitLab. [CORROBORATED: README; readthedocs Contributing page, accessed 2026-10-29] So GitHub is the development home, and the GitLab copy that DOE CODE registers is the official ORNL-hosted mirror.
- The brief's last-activity date (2026-06-12) is the GitHub push date. The newest commit on any branch has an author date of 2026-06-12 01:38 ET and a committer date of 2026-06-12 13:06 ET (fresh clone). The catalog's 2026-09-11 came from GitLab metadata. The GitLab project page, fetched 2026-10-29, shows no dates, and no public page links to its API, so we didn't query it. [INFERRED] 2026-09-11 is a mirror-side activity date, probably a sync, and not new code, since the mirror is read-only and GitHub has nothing newer. [UNKNOWN] the exact cause on the GitLab side. The catalog row is left for the catalog owner.

### Second pass (2026-10-29)
- Re-verified with new sources: earliest git tags v0.12.0 and v0.12.1 are both 2024-02-15, matching PyPI's first uploads; `requires-python` ">=3.9,<3.13" in pyproject.toml; home and mirror wording confirmed by the docs' Contributing page. First-pass label fixes are in place. No issues found.
