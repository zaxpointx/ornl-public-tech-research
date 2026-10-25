# Batch 02 summary (2026-10-24)

Discovery notes (`discovery-notes/batch-02.md`) are merged below.

## What was researched
- Discovery (the discovery pass): 15 projects were added (33 total): daymet, tesvis-modis, e3sm-elm, fates, data-workflow, pyrs, 3dthesis, myna, finch, vivaldi, mind-the-gap, hydrofleetintel, olcf-test-harness, qiree and django-remote-submission. Every license comes from the repo's own license file, and OSTI records were added where they exist.
- Briefs (the reading pass): 6 were written: [daymet](../projects/daymet.md), [e3sm-elm](../projects/e3sm-elm.md), [myna](../projects/myna.md), [data-workflow](../projects/data-workflow.md), [tesvis-modis](../projects/tesvis-modis.md) and [olcf-test-harness](../projects/olcf-test-harness.md).
- Connections (the connections pass): [map.md](../connections/map.md) now covers all 46 cataloged projects through batch 3, with 69 unique links (50 KNOWN, 25 INFERRED, 9 UNKNOWN). Shared-contributor links are now split. The shared contributor is KNOWN, but "same group" built on it is INFERRED.

## What was verified
- The fact-check pass checked all 6 briefs: 53 claims, with 43 verified, 6 corrected and 4 unverifiable.
- Corrections:
  - OLCF Test Harness: the README never mentions a v4.0, and NCCS comes from the developer affiliations rather than the OSTI research-org field.
  - e3sm-elm: a second OLCF DOI was added for the 1 km ELM datasets (OSTI 3005830).
  - Three tags were raised to KNOWN: MDF via ornl.gov/facility/mdf, Mantid's link to data-workflow via the post_processing_agent README, and TESViS working without an API key.
- qiree license: the repo wins over OSTI. Source files carry Apache-2.0 WITH LLVM-exception or Apache-2.0 OR MIT tags, and there's no GPL anywhere. OSTI's GPL-3.0 looks like a metadata error [INFERRED]. The LICENSE-APACHE and LICENSE-MIT files that COPYRIGHT points to are missing from the repo.
- Cyberwheel funding is now KNOWN. The FY2025 LDRD report names it as the testbed for project 11049 (OSTI 3025007/3027393).
- Nothing restricted, no implied affiliation and no copied text was found.

## Still unknown
- The code that generates Daymet. Only download helper scripts are public.
- Who leads the E3SM land group, and whether any ORNL division owns ELM work. ELM is multi-lab, and only specific ORNL papers and datasets are KNOWN.
- The source code for TESViS, since there's no public repo.
- data-workflow's owning division.
- ORNL's role in FATES. OSTI lists Los Alamos.
- Open question from the discovery pass: should fates and e3sm-elm stay in the catalog, since ORNL doesn't own them, or move to the connections map as outside projects? This needed an editorial decision.

## Investigate next
- Fact-check the 6 batch 3 briefs (scale, vera, gitr, real-twin, gauntlet, energyplus).
- The discovery pass has these appends queued: exaca, adamantine, oncat, post-processing-agent and live-data-server. The discovery pass is also running a DOE CODE confirmation pass on every batch 1 row.
- The connections-pass open targets: ExaCA, Cabana/Kokkos, XACC, HiOp/SUNDIALS/ExaGO, FAR3d vs VMEC, GITR vs Xolotl/SOLPS, and Real-Twin, which has no links yet.
- Retry fetches: contributor lists for Real-Twin and 3DThesis, and the READMEs for data-workflow and PyRS.

## Discovery notes
### Sources checked (2026-10-24)
- DOE CODE API: https://www.osti.gov/doecode/api/search returned 404 for both GET and POST. The search UI is JavaScript-rendered, so no records were pulled. A retry is needed with the documented endpoint or a browser.
- daymet.ornl.gov and modis.ornl.gov (official pages).
- GitHub API: neutrons, ORNL-MDF, ornl-ndav, ORNL (vivaldi, mind_the_gap, HydroFleetIntel), E3SM-Project/E3SM, NGEET/fates, ORNL-QCI/qiree, olcf/olcf-test-harness.
- ORNL/gauntlet: the API lookup failed (it is listed in the org), so it was not added.
### Dedupe notes
- e3sm-elm points at the main E3SM-Project repo. The stale ORNL/E3SM fork was not added. ORNL's role in ELM and FATES is not verified, so it is tagged [INFERRED].
- The daymet repo_url points to helper scripts. Daymet itself is a data product and service.
- ornl-ndav is mostly archives from 2015-2017. Only django-remote-submission was added.
- Status uses archived only when GitHub flags the repo as archived. Stale repos are marked unknown.
### Priority 6 for deep reading
1. daymet: a major climate data product with a clear official page that names the ORNL division.
2. e3sm-elm: a core DOE climate model. The ORNL role needs verification.
3. myna: an active, well-scoped AM workflow hub that ties together 3DThesis, Finch and AdditiveFOAM.
4. data-workflow: the SNS facility data backbone, connected to Mantid.
5. tesvis-modis: a widely used remote-sensing service with a REST API.
6. olcf-test-harness: shows how OLCF tests its supercomputers.
### Leads for batch 3
- Retry DOE CODE: check the API docs at osti.gov/doecode/api/docs, or use a browser.
- ornl.gov software and technology licensing pages.
- ORNL DAAC web services and the SDAT/WebMap tools.
- More cyber and nuclear rows: ORNL/TASQC (stale), and nuclear codes like SCALE (license-restricted, so check only its public pages).
- The CASL/VERA public parts.
- ORNL/gauntlet.

### License and OSTI fixes (discovery pass 2026-10-24)
Licenses below come from each repo's own license file. Every batch-2 row now records the license file URL in its notes.
- Custom UT-Battelle permissive: daymet, vivaldi, mind-the-gap, hydrofleetintel. olcf-test-harness uses a UT-Battelle BSD-3 style license.
- e3sm-elm: BSD-3-Clause. fates: BSD-3-style.
- qiree: Apache-2.0 WITH LLVM-exception or MIT, per its COPYRIGHT file. DOE CODE says GPL-3.0, which conflicts with the repo.
- DOE CODE/OSTI records list ORNL as the research org for mind-the-gap (152916), hydrofleetintel (code-123550), olcf-test-harness (code-153320, NCCS) and qiree (149694). The vivaldi record (126052) lists the developer as ORNL-affiliated.
- fates: DOE CODE 5445 lists Los Alamos, not ORNL.
- e3sm-elm: the DOE CODE records (148889, 123310) list "E3SM Project, DOE". ORNL is not shown, so its role is [UNKNOWN].
- daymet: no DOE CODE record found.
- Open question: should fates and e3sm-elm stay in the catalog, or be moved to connections/map.md?
- Concurrency note: another agent rewrote catalog.csv at 20:22:50 EDT (batch values became "02", and batch-1 notes were changed). That overwrote my first edit. I reapplied the 8 license/OSTI note fixes on top of their version and left their other changes alone. Validated: 33 rows, 9 columns, unique ids.
