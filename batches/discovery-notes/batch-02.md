# Batch 02 scout (discovery) - 2026-10-24
Batch-1 rows were not edited (normalization is an editorial step). The 15 new rows use discovered_batch=2 and the top-level domain set, with finer detail in notes as "subdomain:".
## Added (15)
daymet, tesvis-modis, e3sm-elm, fates, data-workflow, pyrs, 3dthesis, myna, finch, vivaldi, mind-the-gap, hydrofleetintel, olcf-test-harness, qiree, django-remote-submission
## Sources checked (2026-10-24)
- DOE CODE API: https://www.osti.gov/doecode/api/search returned 404 for both GET and POST. The search UI is JavaScript-rendered, so no records were pulled. A retry is needed with the documented endpoint or a browser.
- daymet.ornl.gov and modis.ornl.gov (official pages).
- GitHub API: neutrons, ORNL-MDF, ornl-ndav, ORNL (vivaldi, mind_the_gap, HydroFleetIntel), E3SM-Project/E3SM, NGEET/fates, ORNL-QCI/qiree, olcf/olcf-test-harness.
- ORNL/gauntlet: the API lookup failed (it is listed in the org), so it was not added.
## Dedupe notes
- e3sm-elm points at the main E3SM-Project repo. The stale ORNL/E3SM fork was not added. ORNL's role in ELM and FATES is not verified, so it is tagged [INFERRED].
- The daymet repo_url points to helper scripts. Daymet itself is a data product and service.
- ornl-ndav is mostly archives from 2015-2017. Only django-remote-submission was added.
- Status uses archived only when GitHub flags the repo as archived. Stale repos are marked unknown.
## Priority 6 for deep reading
1. daymet: a major climate data product with a clear official page that names the ORNL division.
2. e3sm-elm: a core DOE climate model. The ORNL role needs verification.
3. myna: an active, well-scoped AM workflow hub that ties together 3DThesis, Finch and AdditiveFOAM.
4. data-workflow: the SNS facility data backbone, connected to Mantid.
5. tesvis-modis: a widely used remote-sensing service with a REST API.
6. olcf-test-harness: shows how OLCF tests its supercomputers.
## Leads for batch 3
- Retry DOE CODE: check the API docs at osti.gov/doecode/api/docs, or use a browser.
- ornl.gov software and technology licensing pages.
- ORNL DAAC web services and the SDAT/WebMap tools.
- More cyber and nuclear rows: ORNL/TASQC (stale), and nuclear codes like SCALE (license-restricted, so check only its public pages).
- The CASL/VERA public parts.
- ORNL/gauntlet.

## License and OSTI fixes (discovery pass 2026-10-24)
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
