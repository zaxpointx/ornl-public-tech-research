# Batch 05 summary (closed: 4 of 4 verified)

Closed 2026-10-24: all four briefs passed two fact-check sweeps.

Independent research from public sources only; not affiliated with ORNL. Date: 2026-10-24.

## What was researched
- The discovery pass ran OSTI software-record checks on the batch 01 rows and added 5 rows (discovered_batch 05): exaca, adamantine (materials), oncat, post-processing-agent and live-data-server (neutrons). exaca was later moved out of the catalog under RULES.md item 13, because the repo and DOE CODE record are LLNL's. It lives in connections/map.md as an outside project. So batch 05 has 4 catalog rows.
- The reading pass wrote 4 briefs: [Live Data Server](../projects/live-data-server.md), [Post Processing Agent](../projects/post-processing-agent.md), [adamantine](../projects/adamantine.md) and [ONCat](../projects/oncat.md). ONCat scope, decided editorially on 2026-10-24: read only its public overview and docs pages plus its public client repo if one exists. No API calls, no running the client against the service, no login pages. Anything that needs credentials is marked out of scope under RULES.md item 16. Order: adamantine, then oncat.
- The discovery pass also answered the reading-pass open questions from batch 4 (Model America download, roofcalc.com, the Radiation Transport Group, LandScan HD/USA). Those notes are appended below and fed the batch 04 sweep.
- The fact-check pass finished the Cyberwheel deep dive in the same round: [source ledger](../deep-dives/cyberwheel/source-ledger.md), [missing artifacts](../deep-dives/cyberwheel/missing-artifacts.md) and [verification report](../deep-dives/cyberwheel/verification-report.md).

## What was verified
Details are in [verification/log.md](../verification/log.md).
- Live Data Server and Post Processing Agent: 9 checks, 4 verified, 5 corrected, 0 unverifiable. Fixes were small: Python is 97%, there are 21 releases, and the 60 min / 70% values are the README's example config (the values are KNOWN, calling them "defaults" is INFERRED). The production URL and deployment size were reworded as out of scope under RULES.md item 16, so nobody researches them.
- Cyberwheel deep dive: 6 checks, 4 verified, 1 corrected, 1 unverifiable. The correction attributes "a modified version of the Firewheel test bed" to the LDRD report only (claim-boundary row 7). OSTI 3827147 as a successor is unverifiable.
- adamantine: 6 checks, 5 verified, 1 corrected, 0 unverifiable. Release 1.1 is dated 2026-01-23; the CHANGELOG's 2025 is likely a typo.
- ONCat: 4 checks, 3 verified, 1 corrected, 0 unverifiable. Only public pages and the pyoncat package files were read, nothing was run. The correction replaced a guessed release-notes URL with "not linked from public pages".
- Signals pilot (cyberwheel, hydragnn, datafed): 10 checks, 8 verified, 2 corrected, 0 unverifiable. HydraGNN's commit-metadata row and job-trace row are out of scope under item 16; DataFed release dates are now labeled as tag commit dates. The discovery-pass commit and author counts were taken on trust.
- Batch total, including the Cyberwheel deep dive: 35 checks, 24 verified, 10 corrected, 1 unverifiable.
- Before adamantine and ONCat, 24 full briefs and 2 OSTI-only drafts are verified (26 in total; the total after batch 04 was 24).

## Still unknown
- oncat: service source code (no public repo; only the pyoncat client, GPL-3.0, is public). Release notes are not linked from public pages.
- adamantine: ORNL's specific role beyond being a research org on OSTI 2472702.
- Cyberwheel: what Firewheel modification was made, its owner at division level, and outside authors' affiliations.

## What to investigate next
- Signals pilot is done and swept; extending it was an editorial decision (it now covers every project, RULES.md item 17).
- Batch 06 briefs from the reading pass: flowcept, iris, tasmanian, xolotl written; qiree, hecbench next.
- Batch 07 (discovery): zambeze, matris; next Cabana and XACC, then Kokkos, HiOp and ExaGO after a rule 13 check (record ORNL's stated role, not ownership).
- The discovery-pass parked leads, listed below, once discovery resumes after the pilot.

---
# Batch 05 discovery notes (OSTI checks), 2026-10-24
Batch-1 notes were only appended to, with marker "Scout OSTI 2026-10-24". No other fields were changed.

## Batch-1 OSTI results (records API, product_type=Software)
| id | ORNL research org on OSTI? | record | OSTI license vs repo |
|---|---|---|---|
| resolve, tasmanian, exatn, hydragnn, gridkit, thermochimica, datafed | yes (earlier fact-check and reading-pass findings, not re-run) | see verification/log.md | per earlier findings |
| additivefoam | yes (prior; also seen this run) | code-108345 | not compared |
| cyberwheel | yes (prior; also seen this run) | code-134699 | not compared |
| mantid, xolotl | no hits (prior findings) | - | - |
| hecbench | no hits | - | - |
| iris | no relevant hits | - | - |
| flowcept | no Flowcept record (only an unrelated ORNL record, REDI, code-185154) | - | - |
| stellarator-tools | no match for "Stellarator" or "PARVMEC" | - | - |
| snapred | no hits | - | - |
| olcf-user-docs | no record (docs, not code) | - | - |
| gedi-tutorials | no relevant hits | - | - |

Totals: 9 confirmed ORNL (all from earlier findings), 0 newly confirmed, 9 with no OSTI record.

## Added (5, discovered_batch "05")
| id | domain | license (file) | OSTI | caveat |
|---|---|---|---|---|
| exaca | materials | MIT, LLNS copyright | DOE CODE 68592 lists LLNL as research org | ORNL role [UNKNOWN]; the repo is LLNL/ExaCA |
| adamantine | materials | Apache-2.0 WITH LLVM-exception | no hits | ORNL role not stated |
| oncat | neutrons | [UNKNOWN], no public repo | no hits | official page oncat.ornl.gov; the API needs credentials (not used) |
| post-processing-agent | neutrons | MIT, NScD copyright | no hits | |
| live-data-server | neutrons | BSD-3-Clause, ORNL copyright | no hits | |

## Parked leads
- LandScan USA and HD datasets (OSTI Dataset records).
- Denovo and ORANGE, from the public SCALE manual.
- OSTI searches on grid, microgrid, battery, isotope and HFIR.
- OpenStudio and BEopt (ORNL contributions).
- olcf/pkpass.
- The connections-pass targets: Cabana/Kokkos, XACC, HiOp, SUNDIALS, ExaGO.


## Open questions from the reading pass (lookups 2026-10-24)
All accessed 2026-10-24. Every page was opened directly; none of these rest on search snippets alone. No forms were submitted and no logins were used.

### 1. AutoBEM "Model America" v1.0: public download?
Yes, through Globus. A free Globus Connect Personal client is required. [CORROBORATED]
- Source A (primary):
  - Page: ORNL Constellation (OLCF/NCCS DOI service), "Model America - data and models of every U.S. building", https://doi.ccs.ornl.gov/dataset/9e968129-1ca9-5a71-93fa-24f009132a3a
  - DOI 10.13139/ORNLNCCS/1774134, released 2021-04-14. Five authors, all listed as ORNL.
  - Description section: "Please note that the download requires the free Globus Connect Personal". The page has a "Download Dataset on Globus" button.
  - The page states it covers 122,930,327 of the 125.7M detected U.S. buildings, as OpenStudio 3.1.0 / EnergyPlus 9.4 models per state_county.zip, and says the data are "free and openly available".
  - A banner warns that Globus maintenance on 2026-10-24/25 may interrupt downloads.
- Source B:
  - Page: ESS-DIVE (LBNL data repository), "Model America: Data and Models for every U.S. Building", https://doi.org/10.15485/2283980, which resolves to data.ess-dive.lbl.gov. Published 2021.
  - It names the release "Model America v1" and lists updates on 2025-09-23 (ID fixes) and 2026-09-06 (PNNL UBID identifiers).
  - The page was opened, but I read its access terms only through the indexed abstract, so ESS-DIVE's own download mechanics are [UNKNOWN].
- Not opened: OSTI's related records, such as the Arizona Model America datasets (osti 3424892/3424893, Zenodo DOIs). These are not v1.0.
- Catalog impact: the autobem software is still Closed Source per OSTI code-115947, but its output dataset is public.

### 2. roofcalc.com and newer OSTI records
- https://www.roofcalc.com/ returned HTTP 404 "Site Not Configured" (fetched 2026-10-24 about 20:40 EDT). The site appears to be down or the domain unconfigured [KNOWN for this fetch; it could be temporary].
- https://rsc.ornl.gov/ just shows the generic ornl.gov home page, with no RSC content [KNOWN].
- OSTI 1651267 names RSC [KNOWN]:
  - "Comparison of different simulation programs in modeling the energy savings of cool roofs", Huang (White Box Technologies), Levinson (LBNL) and New (ORNL). Conference paper, IC2UHI, 2019-12-01. Research org ORNL. https://www.osti.gov/biblio/1651267
  - Abstract: "The Roof Savings Calculator is a web-based application first developed in 2010 that uses detailed building energy simulations". It is a paper, not a newer software record.
- Situ: no software record newer than 2014 (logged earlier in not-found.md). Roof Savings Calculator: no software record newer than OSTI 1238771 (2013-11-22).

### 3. Radiation Transport Group as the home of Shift/Exnihilo [KNOWN]
- Source:
  - Paper: Pandya, Johnson, Evans, Davidson, Hamilton et al., "Implementation, capabilities, and benchmarking of Shift, a massively parallel Monte Carlo radiation transport code", J. Comput. Phys. (Elsevier), published 2015-12-21.
  - OSTI record https://www.osti.gov/biblio/1237627, full text https://www.osti.gov/servlets/purl/1237627, DOI 10.1016/j.jcp.2015.12.037.
  - Author affiliation line (title page): "Radiation Transport Group, Reactor and Nuclear Systems Division".
  - Introduction: "developed and maintained at Oak Ridge National Laboratory (ORNL) by the Radiation Transport Group".
- Current group name: [UNKNOWN]. I did not find a current ornl.gov group page.
- The SCALE manual CSAS-Shift chapter (https://scale-manual.ornl.gov/6.3.3/CSAS-Shift.html) places Shift in the Exnihilo suite but names no group. It was read as a public overview only, with no download links followed.

### 4. LandScan HD and USA (landscan.ornl.gov)
- Sources: the landscan.ornl.gov home page, plus the site's public JavaScript app text (/assets/index-*.js), which holds the About/Download copy. Direct /about, /viewer and dataset sub-URLs returned 403 to curl and timed out in WebFetch.
- Status [KNOWN]: HD and USA are legacy datasets. In the site's words they are "no longer actively updated but are preserved for archival and historical reference". They are succeeded by LandScan Global and LandScan Mosaic, and are still downloadable after you "provide your details" on a form. No form was submitted.
- Resolution [UNKNOWN per dataset]: the site says only "down to 100 meter grid resolution" (home page), and LandScan Global's modeling is at "30 arc-second resolution". No per-dataset figure for HD or USA was found on the public pages.
- Coverage [KNOWN]:
  - USA covers U.S. regions; the viewer lists Conus, Ak, As, Gu and others, each with day metadata.
  - HD covers individual countries; the viewer lists HD by country, with versions.
  - Per the site, HD was introduced in 2014, building on machine learning and computer vision applied to satellite imagery, for bottom-up estimates where census data are thin.
- Day/night [KNOWN]:
  - Per the site, LandScan USA (2004) added explicit "day–night (diurnal) population dynamics" using higher-quality national data, and was re-engineered in 2016.
  - The page gives no detailed day-versus-night method for USA [UNKNOWN].
  - The fuller day/night/ambient wording on the site belongs to LandScan Mosaic: nighttime emphasizes residential occupancy, daytime reflects workplaces, schools and other activity spaces. Applying that wording to USA would be [INFERRED].
- HD methodology citation listed on the site: Tuccillo et al., "LandScan HD: a high-resolution gridded ambient population methodology for the world", Population and Environment 47, 42 (2025). Not opened.
