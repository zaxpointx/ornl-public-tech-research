# Searched but not found

| date | project | query | where | note |
|---|---|---|---|---|
| 2026-10-24 | mantid | "Mantid" | OSTI records API (osti.gov/api/v1/records, product_type=Software) | no software record (earlier team finding, re-run batch 5) (Scout) |
| 2026-10-24 | xolotl | "Xolotl" | OSTI records API (osti.gov/api/v1/records, product_type=Software) | no software record (earlier team finding, re-run batch 5) (Scout) |
| 2026-10-24 | hecbench | "HeCBench" | OSTI records API (osti.gov/api/v1/records, product_type=Software) | no hits (Scout) |
| 2026-10-24 | iris | "IRIS" | OSTI records API (osti.gov/api/v1/records, product_type=Software) | no relevant hits; name collides with unrelated records (Scout) |
| 2026-10-24 | flowcept | "Flowcept" | OSTI records API (osti.gov/api/v1/records, product_type=Software) | only hit was an unrelated ORNL record (REDI) [UNRELATED] (Scout) |
| 2026-10-24 | stellarator-tools | "Stellarator", "PARVMEC" | OSTI records API (osti.gov/api/v1/records, product_type=Software) | no hits (Scout) |
| 2026-10-24 | snapred | "SNAPRed" | OSTI records API (osti.gov/api/v1/records, product_type=Software) | no hits (Scout) |
| 2026-10-24 | olcf-user-docs | "OLCF User Documentation" | OSTI records API (osti.gov/api/v1/records, product_type=Software) | no record; docs, not code (Scout) |
| 2026-10-24 | gedi-tutorials | "GEDI tutorials" | OSTI records API (osti.gov/api/v1/records, product_type=Software) | no relevant hits (Scout) |
| 2026-10-24 | adamantine | "adamantine" | OSTI records API (osti.gov/api/v1/records, product_type=Software) | no software record; a non-software search found journal article OSTI 2472702 naming ORNL (Scout) |
| 2026-10-24 | oncat | "ONCat" | OSTI records API (osti.gov/api/v1/records, product_type=Software) | no hits (Scout) |
| 2026-10-24 | post-processing-agent | "post processing agent" | OSTI records API (osti.gov/api/v1/records, product_type=Software) | no hits (Scout) |
| 2026-10-24 | live-data-server | "live data server" | OSTI records API (osti.gov/api/v1/records, product_type=Software) | no hits (Scout) |
| 2026-10-24 | situ | "Situ" sorted newest | OSTI records API (all types) | no newer Situ record; hits are unrelated in-situ papers [UNRELATED] (Scout) |
| 2026-10-24 | shift-exnihilo | "Shift" "Monte Carlo" "radiation transport" | OSTI records API (all types) | nothing naming the Radiation Transport Group (Scout) |
| 2026-10-24 | roof-savings-calculator | "Roof Savings Calculator" | OSTI records API (all types) | no software record newer than 2013-14; possible lead OSTI 1651267 (2019 ORNL cool-roof tool comparison), not yet read (Scout) |
| 2026-10-24 | cyberwheel | "Automating Cyber Defense Using Reinforcement Learning" | OSTI records API | only FY2025 report 3025007/3027393; no FY2023/FY2024 LDRD report hit giving start year (Connector) |
| 2026-10-24 | cyberwheel | ORNL fork of FIREWHEEL | github.com/ORNL, Cyberwheel repo | no fork found; modifications appear to be model components only (Connector) |
| 2026-10-24 | cyberwheel | predecessor ORNL cyber RL project | OSTI records API "credited developer A reinforcement learning cyber" | no pre-2024 ORNL cyber-RL predecessor found (Connector) |
| 2026-10-24 | roof-savings-calculator | https://www.roofcalc.com/ | direct fetch | HTTP 404 'Site Not Configured'; rsc.ornl.gov shows only the generic ornl.gov home page (Scout) |
| 2026-10-24 | shift-exnihilo | current name of Radiation Transport Group | ornl.gov / web search | no current group page found; 2015 JCP paper OSTI 1237627 names the group (Scout) |
| 2026-10-24 | landscan | LandScan HD / USA per-dataset resolution | landscan.ornl.gov (home page + public app text); /about, /viewer and dataset sub-URLs gave 403 | no per-dataset resolution stated (Scout) |
| 2026-10-24 | landscan | LandScan USA day vs night method detail | landscan.ornl.gov public text | only 'day-night (diurnal) population dynamics' stated; detailed wording is for Mosaic (Scout) |
| 2026-10-24 | exaca | ExaCA → Finch dependency | LLNL/ExaCA build files, DOE CODE 68592 | no dependency; only a README mention of Finch (Connector, map) |
| 2026-10-24 | mantid / xolotl / flowcept | project name | OSTI records API (product_type=Software) | no matching software record for any of the three (Connector, map) |
| 2026-10-24 | real-twin | "CARLA" | Real-Twin README + pyproject.toml | not mentioned; only SUMO/VISSIM/AIMSUN (Connector, map) |
| 2026-10-24 | shift-exnihilo / vera | Shift or CTF in VERA | https://www.ornl.gov/onramp/casl (WebFetch; curl blocked by Cloudflare) | page is only a 2015 CASL ALCC request stub (J. Turner); no Shift/CTF content (Connector) |
| 2026-10-24 | real-twin | contributors | GitHub contributors API ORNL-Real-Sim/Real-Twin | returned empty (Connector, map) |
| 2026-10-24 | shift-exnihilo | current name of ORNL Radiation Transport Group | ornl.gov (per Scout batch-05) | no current group page found; 2016 name only (Connector, map pass 7) |
| 2026-10-24 | landscan | per-dataset resolution of LandScan HD / USA | landscan.ornl.gov public pages (per Scout batch-05) | no per-dataset figure; sub-URLs 403/timeout (Connector, map pass 7) |
| 2026-10-24 | live-data-server | dependency file listing Mantid or post-processing-agent | live-data-server brief (repo README, src/) | none; both ties only INFERRED (Connector, map pass 8) |
| 2026-10-24 | post-processing-agent | upload call to live-data-server | post-processing-agent brief (code not re-checked) | not found/not checked; link 107 stays INFERRED (Connector, map pass 8) |
| 2026-10-24 | vera | Shift or CTF named as VERA component | OSTI 1237627 description, OSTI 1546053 description | only a VERA benchmark-suite mention for Shift; no component statement (Fact Checker sweep 2) |
| 2026-10-24 | energyplus | "flagship" or "main" wording, or a lead-lab statement | EnergyPlus README, OSTI 1395245 | not found; NREL/NLR lead stays INFERRED (Fact Checker sweep 2) |
| 2026-10-24 | scale | SCALE 6.3 validation overview volume | OSTI records API "SCALE 6.3 Validation" | no overview record; fifth-volume count stays INFERRED (Fact Checker) |
| 2026-10-24 | gitr | "GITR" | OSTI records API (product_type=Software) | no DOE CODE record (Fact Checker) |
| 2026-10-24 | cyberwheel | PI designation for LDRD 11049 | OSTI 3025007 p. 13 (project 11049 section) | not found; only a three-name team line (Reader, deep dive) |
| 2026-10-24 | cyberwheel | owning division or group name | ORNL/cyberwheel README, DOE CODE code-134699, OSTI 2478356 | not found (Reader, deep dive) |
| 2026-10-24 | cyberwheel | "deployed" or "production" wording | README, v1.1.0/v2.0 release notes, DOE CODE code-134699, OSTI 3025007 p. 13 | not found; "deployable in live networks" appears only as a goal (Reader, deep dive) |
| 2026-10-24 | cyberwheel | commits after 2025-08-26 | GitHub commits API, ORNL/cyberwheel | none (Reader, deep dive) |
| 2026-10-24 | cyberwheel | LDRD 11049 or contract number on the DOE CODE / CSET records | OSTI records API code-134699, 2478356 | no project number on either (Fact Checker) |
| 2026-10-24 | cyberwheel | what exactly was modified in Firewheel | OSTI 3025007 p. 13 | report says only "modified version" (Fact Checker) |
| 2026-10-24 | cyberwheel | "Cyberwheel" in the abstracts of papers citing DOI 10.1145/3675741.3675752 | Semantic Scholar citations API (33 citing) | 29 of 33 abstracts don't name it; full texts not read (Reader, deep dive) |
| 2026-10-24 | cyberwheel | author lists for 3 citing papers that use Cyberwheel | Semantic Scholar paper API | empty responses (likely rate limit); outside-ORNL authorship UNKNOWN (Reader) |
- 2026-10-24 | landscan | award year for R&D 100 | landscan.ornl.gov page bundle | not stated
- 2026-10-24 | landscan | /licensing page direct fetch | curl and WebFetch both 403 | used site bundle text instead
- 2026-10-24 | autobem | abstract or AutoBEM mention for data-center paper | OSTI 3384902 | no description in record
- 2026-10-24 | autobem | any AutoBEM software release after 2023 | DOE CODE 115947, Constellation | none found
| 2026-10-24 | cyberwheel | PyPI package / conda-forge feedstock / Spack package.py | pypi.org JSON, github.com/conda-forge, spack-packages builtin | all 404; GitHub dependents "0 Repositories" (Connector, signals) |
| 2026-10-24 | hydragnn | conda-forge feedstock / Spack package (hydragnn, py_hydragnn) | github.com/conda-forge, spack-packages builtin | 404; GitHub dependents only PyPI mirror repos (Connector, signals) |
| 2026-10-24 | datafed | conda-forge feedstock / Spack package (datafed, py_datafed); PyPI pydatafed, datafed-cli | github.com/conda-forge, spack-packages builtin, pypi.org | 404 (only `datafed` on PyPI exists); GitHub dependents "0 Repositories" (Connector, signals) |
| 2026-10-24 | cyberwheel, hydragnn, datafed | GitHub code search for imports | github.com/search?type=code | not reachable: requires login (Connector, signals) |
| 2026-10-24 | cyberwheel | pypistats recent downloads | pypistats.org API | 404, no package (Connector, signals) |
| 2026-10-24 | flowcept | "datafed", "globus", "hydragnn", "mantid" | ORNL/flowcept repo (code, docs, examples; shallow clone grep) | no mentions; links 18 and 19 stay UNKNOWN (Connector, map pass 12) |
| 2026-10-24 | flowcept | conda-forge feedstock / Spack py_flowcept | github.com/conda-forge, spack-packages builtin | 404 (Connector, map pass 12) |
| 2026-10-24 | flowcept | owning ORNL group | LICENSE, README, LDRD report 11521 | no group named; [UNKNOWN] (Connector, map pass 12) |
| 2026-10-24 | Scout | signals pilot | Wayback CDX API (web.archive.org/cdx) for the three repo URLs | Timed out or returned nothing, so the availability API was used instead. Earliest-capture dates are bounds only |
| 2026-10-24 | Scout | cyberwheel | Job postings naming Cyberwheel | No hits |
| 2026-10-24 | Scout | datafed | Job postings naming DataFed | No hits |
| 2026-10-24 | Scout | hydragnn | Job postings naming HydraGNN on jobs.ornl.gov directly | Official posting not found (a social-media mention was out of scope under rule 16 and has been removed) |
| 2026-10-24 | iris | Spack package `iris`; PyPI iris-runtime, iris-ornl | spack-packages builtin, pypi.org | 404; conda-forge iris-feedstock is SciTools Iris (UNRELATED) (Connector, map pass 13) |
| 2026-10-24 | iris | "hecbench", "tasmanian", "frontier", "olcf", "ExCL" | ORNL/iris README, docs, apps READMEs (shallow clone grep) | no mentions; HeCBench link 20 stays UNKNOWN (Connector, map pass 13) |
| 2026-10-24 | iris | funding/acknowledgement statement | ORNL/iris README | none found (Connector, map pass 13) |
| 2026-10-24 | iris | GitHub dependents | github.com/ORNL/iris/network/dependents | "0 Repositories" (Connector, map pass 13) |
| 2026-10-24 | oncat | Release notes | public pages (oncat.ornl.gov overview) | release notes not linked from public pages; the overview shows a "Release Notes" label but no followable link was used (Reader; guessed path withdrawn per lead, rule 16) |
| 2026-10-24 | Scout | laris | GitHub repo search "laris" (all orgs and org:ORNL), plus OSTI software records | Only OSTI 2000309, a conference paper. No public code |
| 2026-10-24 | Scout | iris-gnn | GitHub search "iris-gnn", plus OSTI | Only OSTI 2538031, a conference paper. No public code |
| 2026-10-24 | Scout | fftx-iris | GitHub search "fftx iris", plus OSTI | Only OSTI 2439840, a conference paper. No public code |
| 2026-10-24 | adamantine | Spack package / conda-forge feedstock / PyPI | spack-packages builtin, github.com/conda-forge, pypi.org | all 404; GitHub dependents "0 Repositories" (Connector, map pass 14) |
| 2026-10-24 | adamantine | "ORNL", "Oak Ridge", "Myna", "ExaCA", "Finch" | adamantine README | none (Connector, map pass 14) |
| 2026-10-24 | adamantine | specific EERE office (AMO/AMMTO) or MDF tie | OSTI 2472702 | only "EERE" generic (Connector, map pass 14) |
| 2026-10-24 | tasmanian | conda-forge feedstock; GitHub dependents | github.com/conda-forge; github.com/ORNL/TASMANIAN/network/dependents | 404; "0 Repositories" (Connector, map pass 14) |
| 2026-10-24 | tasmanian | "iris", "hecbench", "qiree" | TASMANIAN README | none; IRIS tie stays UNKNOWN (Connector, map pass 14) |
| 2026-10-24 | tasmanian | OpenAlex citing count | api.openalex.org search "TASMANIAN sparse grid" | 888 noisy hits, not usable as a count (Connector, map pass 14) |
| 2026-10-24 | oncat | ONCat tie to Mantid / data-workflow / live-data-server | projects/oncat.md, map sources | not sourced; UNKNOWN (Connector, map pass 14) |
| 2026-10-24 | hydragnn / datafed | Flowcept tie (links 18, 19) | signals/hydragnn.md, signals/datafed.md | none (Connector, map pass 14) |
| 2026-10-24 | xolotl | DOE CODE / OSTI software record | per Reader brief and lead note | none; research org UNKNOWN (Connector, map pass 15) [Librarian 2026-10-24: superseded, FC found OSTI 1513390 (ORNL paper calling Xolotl "our cluster dynamics model")] |
| 2026-10-24 | xolotl | conda-forge feedstock; PyPI; GitHub dependents | github.com/conda-forge, pypi.org, dependents page | 404 / 404 / "0 Repositories" (Connector, map pass 15) |
| 2026-10-24 | xolotl | "tasmanian" | whole Xolotl repo (shallow clone grep) | none; marked UNRELATED (Connector, map pass 15) |
| 2026-10-24 | qiree | PyPI / Spack / conda-forge package; GitHub dependents | pypi.org, spack-packages builtin, github.com/conda-forge, dependents page | 404 x3; "0 Repositories" (Connector, map pass 16) |
| 2026-10-24 | qiree | LICENSE-APACHE, LICENSE-MIT named in COPYRIGHT | ORNL-QCI/qiree main branch | missing (404; FC confirmed) (Connector, map pass 16) |
| 2026-10-24 | xacc | Spack package | spack-packages builtin xacc | 404 (Connector, map pass 16) |
| 2026-10-24 | exago | "sundials", "gridkit" | ORNL/ExaGO top-level CMakeLists.txt | none (Connector, map pass 16) |
| 2026-10-24 | cabana | ExaCA or adamantine reference | Cabana README | none (Connector, map pass 16) |
| 2026-10-24 | hecbench | OSTI / DOE CODE software record | OSTI records API (product_type Software) per Scout and Reader | none (Connector, map pass 17) |
| 2026-10-24 | hecbench | "ExCL", "Experimental Computing", "acknowledg" | ORNL/HeCBench README (current master) | none; link 11 ExCL part now UNKNOWN (Connector, map pass 17) |
| 2026-10-24 | hecbench | "iris", "tasmanian" | ORNL/HeCBench README | none; link 20 stays UNKNOWN, TASMANIAN UNRELATED (Connector, map pass 17) |
| 2026-10-24 | hecbench | GitHub dependents; package registries | dependents page; n/a | "0 Repositories"; no packages (Connector, map pass 17) |
| 2026-10-24 | hecbench | "frontier" | ORNL/HeCBench README | not named (Connector, map pass 17) |
| 2026-10-24 | xacc | named successor ("successor", "deprecated", "moved", "no longer") | eclipse-xacc/xacc README, NOTICE; OSTI 1339995 | none; link 163 UNKNOWN (Connector, map pass 18) |
| 2026-10-24 | xacc | conda-forge feedstock; GitHub dependents | github.com/conda-forge; dependents page | 404; "0 Repositories" (Connector, map pass 18) |
| 2026-10-24 | tnqvm | LICENSE file; OSTI record | ORNL-QCI/tnqvm master; not searched on OSTI | LICENSE 404; GitHub API license null; kept as outside node (Connector, map pass 18) |
| 2026-10-24 | zambeze | docs site reachable | https://docs.zambeze.org (linked from README and repo homepage) | no HTTP response at access time; docs read from repo `docs/source` instead (Reader) |
| 2026-10-24 | exago / gridkit | "gridkit" in ExaGO CMake and Spack package; "exago" in GridKit CMake; Spack gridkit | GitHub raw files; spack-packages builtin | none; no direct dependency (Connector, map pass 19) |
| 2026-10-24 | exago | PyPI / conda-forge package; GitHub dependents | pypi.org; github.com/conda-forge; dependents page | 404 / 404 / "0 Repositories" (Connector, map pass 19) |
| 2026-10-24 | cabana | conda-forge feedstock; GitHub dependents; ORNL-relevant PyPI package | github.com/conda-forge; dependents page; pypi.org | 404; "0 Repositories"; PyPI name taken by unrelated project (Connector, map pass 19) |
| 2026-10-24 | zambeze | ZambezeInterceptor class in current Flowcept | ORNL/flowcept src | not found (renamed MQTTBrokerInterceptor) (Connector, map pass 19) |
| 2026-10-24 | zambeze | conda-forge feedstock | github.com/conda-forge | 404 (Connector, map pass 19) |
| 2026-10-24 | matris | Spack / conda-forge / ORNL PyPI package; GitHub dependents | registries; dependents page | 404 / 404 / PyPI name is unrelated / "0 Repositories" (Connector, map pass 19) |
