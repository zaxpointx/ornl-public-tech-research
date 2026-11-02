# Vivaldi

- Official page: DOE CODE record https://www.osti.gov/doecode/biblio/126052 (DOI 10.11578/dc.20240416.1) [KNOWN]
- Repo: https://github.com/ORNL/vivaldi [KNOWN: GitHub API, accessed 2026-10-28]. The DOE CODE record's repo link points to a personal GitHub account instead of the ORNL org; that account is not named or followed here. [KNOWN: DOE CODE page, accessed 2026-10-24]
- Docs: the README only (no docs folder) [KNOWN: repo tree]
- License: UT-Battelle 2024 BSD-style open source license in `LICENSE.txt`; GitHub shows it as "Other" [KNOWN: LICENSE.txt line 1; GitHub API]
- Status: unknown (not archived on GitHub, but every commit is from one day, 2024-04-19) [KNOWN: GitHub API and git log]

## Walkthrough
Vivaldi is a small machine-learning script that guesses how tall a building is from the shape of its outline seen from above. The problem: maps of building footprints (2D outlines) cover the whole country, but heights (the third dimension) are missing for most buildings, and energy and population models need them. [KNOWN: README "Getting started"; the "why" is INFERRED from the related Gauntlet and AutoBEM briefs]
What goes in: a table with one row per building, holding about 65 shape measures made by ORNL's Gauntlet tool (things like area, perimeter and how compact the outline is), plus a known height for the training rows. [KNOWN: README "Data"]
What happens: a first script trims the list of measures down to the useful ones (recursive feature elimination), then a second script tunes and trains an XGBoost model and predicts heights building by building. [KNOWN: README steps; `src/rfe.py`, `src/vivaldi_bh.py`]
What comes out: printed error scores, plots, a saved data scaler (`my_standard_scaler.pkl`) and height predictions. [KNOWN: code; the exact prediction file is UNKNOWN]
Where humans act: someone has to get the Gauntlet table first. The README says that data sits in a PostgreSQL database and access is by request to the team, so it is not public. [KNOWN: README "Data"]
What it is not: not a mapping product or a dataset. No heights ship with the repo. [KNOWN: repo tree]
Example: give it a suburban block's outlines plus Gauntlet measures, and it would estimate that a long, narrow 1,200 sq ft outline is a single-storey house around 4 m tall. (Illustrative example, not from a source.)
Unknown: how accurate it is, which areas it was trained on, and whether ORNL still uses it.

## What it is (plain English, 2-4 sentences)
A two-script Python pipeline that predicts building heights from 2D footprint shape measures. It uses XGBoost, a popular "gradient boosted trees" model, which builds hundreds of small decision trees, each one fixing the last one's mistakes. [KNOWN: `src/requirements.txt`, README] It is the height step that sits after Gauntlet, ORNL's footprint shape tool. [KNOWN: README]

## How it works (plain English, no jargon without definition)
1. Input: a CSV or database table of buildings with Gauntlet's 65 shape features and a `height` column. [KNOWN: README "Data"; `vivaldi_bh.py` uses a `height` column]
2. Clean-up: drop buildings shorter than 2 m and compute a "just guess the median" baseline score to beat. [KNOWN: `filter_and_evaluate` in `vivaldi_bh.py`]
3. Feature trimming: `rfe.py` runs recursive feature elimination, meaning it repeatedly trains a model and throws away the least useful column until only the strong ones are left. [KNOWN: `rfe.py` lines 183-194]
4. Tuning: `hyperopt` runs Bayesian optimization, a smart search that tries model settings and learns which ones score better. In the public code the search is set to a single try (`max_evals=1`), with a comment saying to raise it. [KNOWN: `vivaldi_bh.py` line 220]
5. Training and scoring: XGBoost is trained, scored with mean absolute error, RMSE and R², checked with k-fold cross-validation, and explained with SHAP (a method that shows how much each feature pushed a prediction up or down). [KNOWN: imports and functions `ml`, `cross_val` in `vivaldi_bh.py`; `shap` in requirements]
6. Where a person acts: choosing the area, supplying the data, and reading the scores. [INFERRED: no automation around the scripts]

Reading-pass note: as published, the scripts don't actually load a file. `vivaldi_bh.py` line 32 reads `df = df_us.csv` and `rfe.py` line 36 sets `df` to the string `'all_states.csv'`, so neither calls a CSV reader. Running them would fail until a user adds a `pd.read_csv(...)` line. [KNOWN: code, read 2026-10-28; not run, because the input data is not public]

## How the project is organized
- Files: `README.md`, `LICENSE.txt`, `vivaldi_workflow.png` (a diagram of the steps), and `src/` with `rfe.py` (194 lines), `vivaldi_bh.py` (396 lines), `requirements.txt`, `Dockerfile.txt` and `docker-compose.yml`. [KNOWN: repo tree]
- Language and tools: Python with pinned 2022-23 versions (numpy 1.22, pandas 1.4.2, scikit-learn 1.0.2, xgboost 1.7.5, hyperopt 0.2.7, shap 0.42, sqlalchemy and psycopg2 for PostgreSQL). [KNOWN: `src/requirements.txt`]
- Build: no package or build system. Docker Compose starts an idle container with the folder mounted at `/files`, and you run scripts inside it. [KNOWN: `docker-compose.yml`] The README's commands also mix up the service name (`vivaldi_by` versus `vivaldi_bh`), and the Dockerfile is saved as `Dockerfile.txt`, which Compose won't find by default. [KNOWN: README; INFERRED that the build fails as written, not run]
- Tests and CI: none. [KNOWN: repo tree]
- Contributors: one person in the git history, under two author names (2 commits under a full name, 8 under a GitHub handle committed through GitHub's web interface). [KNOWN: `git shortlog`, fresh clone 2026-10-29] (corrected in a fact-check pass, 2026-10-29) The README lists named contacts; they are not repeated here.
- Releases: none on GitHub. DOE CODE lists version 0.1. [KNOWN: GitHub; DOE CODE record]
- Why it was built this way: UNKNOWN.

## Timeline
| Date | Event | Source | Tag |
|---|---|---|---|
| 2024-04-16 | DOE CODE record and DOI 10.11578/dc.20240416.1 (v0.1) | https://www.osti.gov/doecode/biblio/126052 | [KNOWN] |
| 2024-04-19 | ORNL/vivaldi repo created; all 10 commits uploaded the same day | GitHub API; git log | [KNOWN] |
| after 2024-04-19 | no further commits | git log | [KNOWN] |

## Who uses it / why it matters
No outside users or citing papers were found. [UNKNOWN; see verification/not-found.md] It matters as the missing height step between Gauntlet's footprint shapes and 3D building models like the ones AutoBEM needs. [INFERRED: README says it turns 2D morphology into 3D height; the AutoBEM link is not stated by any source]

## Related projects
Filled by the connections pass, matching connections/map.md.
| Related item | Relationship | Source | Tag |
|---|---|---|---|
| [Gauntlet](gauntlet.md) | uses (its 65 shape features are Vivaldi's input) | README "Data" | [KNOWN] |
| [Mind the Gap](mind-the-gap.md) | related topic (geospatial building ML); map link 48 | both repos | [INFERRED] |
| LandScan, URBAN-NET-TOOLKIT | related topic (geospatial); map link 87 | https://landscan.ornl.gov/ | [INFERRED] |

## What stands out
It reads like a research snapshot uploaded in one sitting rather than a maintained tool: one day of commits, a one-try tuning setting and scripts that don't load their own data yet. The interesting part for a student is the method (feature trimming, then boosted trees, then SHAP to explain the model), which is a textbook tabular ML pipeline.

## Ten questions (GOAL.md)
1. Problem and audience: estimating building heights where only outlines exist, for researchers modeling buildings at scale. [KNOWN: README]
2. Place in the tree: geospatial building science, next to Gauntlet. Which division owns it is UNKNOWN. [INFERRED]
3. Who pays: the DOE CODE sponsor field is blank, so UNKNOWN.
4. Code: two Python scripts, scikit-learn, XGBoost and hyperopt, run in Docker. [KNOWN]
5. Alive: one day of commits in April 2024 and nothing since. [KNOWN]
6. Outside users: none found. [UNKNOWN]
7. Connections: upstream Gauntlet features in PostgreSQL; downstream is UNKNOWN.
8. What it teaches: ORNL registers even small research scripts on DOE CODE with a DOI. [KNOWN: record exists]
9. Student path: yes, with basic pandas and scikit-learn. They'd need to fix the data-loading lines and find a public footprint-plus-height dataset to stand in for the Gauntlet data. [INFERRED]
10. Still unknown: accuracy, training area and current use. Searched without result: outside citations (see verification/not-found.md).

## Known / Inferred / Unknown
- KNOWN: the ORNL org repo, the DOE CODE record and DOI, UT-Battelle license, the pipeline steps, the requirements, and the data-loading lines.
- INFERRED: the Docker setup fails as written; what it means for 3D building models.
- UNKNOWN: accuracy, funding, users, and whether it is still developed.

## Verification notes
Filled by the fact-check pass.

## Sources (URL, title, accessed date, what it supports)
- https://github.com/ORNL/vivaldi, the repo, README, LICENSE.txt and src/, accessed 2026-10-28, supports the code, license and history facts
- https://api.github.com/repos/ORNL/vivaldi, repo metadata, accessed 2026-10-28, supports creation date, stars (2), forks (0), not archived
- https://www.osti.gov/doecode/biblio/126052, DOE CODE record "Vivaldi", accessed 2026-10-24, supports the DOI, date, v0.1, the developer's ORNL affiliation, and blank sponsor and research-org fields (corrected in a fact-check pass, 2026-10-29: the record has no Research Org field; ORNL ties rest on the ORNL GitHub org and the UT-Battelle copyright line)

## Quality gate
- [x] Every load-bearing claim has a source and a tag
- [x] Facts are kept apart from interpretation
- [x] ORNL relationship is not overstated, and maturity verbs match the source
- [x] Walkthrough, flow, timeline and unknowns are present
- [x] Ten questions answered or marked UNKNOWN
- [x] No copied text beyond short cited quotes; people by role only
- [ ] Two fact-check sweeps done
- [ ] INDEX, catalog, LAB-TREE and connections map updated

## Fact-check notes (2026-10-29)
- Re-checked against GitHub API, a fresh clone and DOE CODE 126052: repo created 2024-04-19, last push the same day, 2 stars, 0 forks, not archived, license shown as NOASSERTION ("Other"); 10 commits on all branches, all author and committer dates 2024-04-19; file list, line counts (194, 396), the data-loading lines 32 and 36, `max_evals=1` at line 220, pinned requirements, the `vivaldi_by` typo, Compose `build: .` with only `Dockerfile.txt` present, Gauntlet v2's 65 features in PostgreSQL; DOE CODE release 2024-04-16, v0.1, DOI, blank sponsor, repo link on a personal account.
- Corrected: contributor wording (one person, two author names); DOE CODE has no research-org field, so it supports developer affiliation only.
- Extra observation: the README's Docker step runs `/files/vivaldi.py`, a file that does not exist in the repo. [KNOWN: repo tree]
- connections/map.md links 48, 58 and 87 match the brief's single Gauntlet row; no map changes needed.

### Second pass (2026-10-29)
- Re-verified: "hundreds of trees" fits the tuning range for n_estimators (100 to 1000, `vivaldi_bh.py` line 206); the README's data-access line points to a named contact, so it stays paraphrased with no name; first-pass fixes (contributor wording, DOE CODE fields) are in place. The GitHub languages API was rate-limited and is unverifiable this pass. No issues found.
