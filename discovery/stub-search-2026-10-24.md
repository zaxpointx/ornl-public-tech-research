# OSTI-only stubs: search for public pages (discovery pass) (accessed 2026-10-24)

Goal: find a public docs page, repo or landing page for the 8 stub-osti-only projects so they can qualify for a brief (RULES 14). Searched: each OSTI record's own links field, GitHub repository search for each name, the github.com/ORNL repo list (179 repo names read), and a web search per project, then fetched each candidate page. Only pages a search or another public page actually showed were opened. People are left out; pages that list staff are cited for the project facts only.

Whether a project page, news story or publication page counts as a "public docs page" under rule 14 is the editor's call. Each row says what kind of page it is.

| id | Public repo | Best public page found | What kind of page | Tag |
|---|---|---|---|---|
| hyperion | none found | https://www.ornl.gov/division/projects/hyperion (resolves; describes the tool) | ORNL project page | [KNOWN] |
| urban-net-toolkit | none found | https://www.ornl.gov/news/urban-net-infrastructure-modeling-tool-be-incorporated-eagle-i (2022-08-04) | ORNL news story | [KNOWN] |
| akatosh | none found | https://www.ornl.gov/news/ornl-researchers-enable-real-time-forensic-analysis-new-cybersecurity-tool (2018-08-28) | ORNL news story | [KNOWN] |
| heartbeat-malware | none found | https://www.ornl.gov/publication/heartbeat-detecting-malware-periodic-power-signal-injection-and-monitoring (ORNL report ORNL/TM-2022/2732; OSTI dates it 2022-10-01, the ORNL page shows Feb 2024; doi 10.2172/2305827) (corrected in a fact-check pass, 2026-10-29) | ORNL report page | [KNOWN] |
| can-d | none found | https://www.ornl.gov/publication/can-d-modular-four-step-pipeline-comprehensively-decoding-controller-area-network-data (IEEE TVT, Oct 2021) | ORNL publication page | [KNOWN] |
| wufi-ornl | none found (closed-source PC program) | https://wufi.de/en/service/free-wufi-versions/ (Fraunhofer IBP, lists the free "WUFI ORNL (Pro)" version) | partner's product page | [KNOWN] |
| cpad | none found | only OSTI: software 1396084 and patent 1632617 (2020-02-25, ORNL research org) | patent record | [KNOWN] |
| cincinnatus | none found | none | none | [UNKNOWN] |

## Facts worth carrying into briefs if they qualify
- Hyperion: the project page says it reads a compiled program and works out what it does without the source code. [KNOWN: project page] ORNL news says it was licensed non-exclusively to one company in 2015 and exclusively to another in 2017. [INFERRED: search results only, not fetched; RULES 8 says a snippet is never final evidence] (corrected in a fact-check pass, 2026-10-29)
- URBAN-NET: the 2022 story says it began in 2015 as an ORNL internal research (LDRD) project and was being folded into DOE's EAGLE-I outage-monitoring system, which is funded by DOE's cybersecurity and emergency response office (CESER). [KNOWN: news story] There's also a 2016 IEEE BigData paper (doi 10.1109/bigdata.2016.7840902) and a KDD 2019 showcase paper. [INFERRED: search results only, not fetched] (corrected in a fact-check pass, 2026-10-29) The 2016 paper's DOI is confirmed by Crossref. [KNOWN: api.crossref.org]
- Akatosh: the 2018 story says it snapshots computers on a network, then compares snapshots when an intrusion alert fires so analysts can tell real incidents from false alarms. It was picked for the DHS Transition to Practice program. [KNOWN: news story] Demo paper at ACM CCS 2017 (doi 10.1145/3133956.3138854). [KNOWN: the DOI is registered in Crossref; the ACM page returns 403 to us] (corrected in a fact-check pass, 2026-10-29)
- Heartbeat: the 2024 ORNL report says it measures a computer's power draw while a small routine runs on a timer, and flags changes from a learned baseline as signs of hidden malware. It has been tested in a lab and ORNL was looking for a deployment partner. [KNOWN: report page] ORNL news (2024-09-18) says one company took R&D licenses for Situ and Heartbeat in 2023, then a commercial license for Situ; the story does not say what happened to Heartbeat's license. (corrected in a fact-check pass, 2026-10-29) Heartbeat was funded by ORNL's internal Technology Innovation Program; Situ by ORNL LDRD, DOE, DoD and DHS. Both came from the Cyber Resilience and Intelligence Division. [KNOWN: https://www.ornl.gov/news/u2opia-signs-license-commercialize-anomaly-detection-technology-cybersecurity, fetched 2026-10-24] This ties it to the catalog's situ entry. [KNOWN]
- CAN-D: peer-reviewed paper describing the method (working out signal layouts from raw car network logs). [KNOWN: publication page]
- WUFI-ORNL: Fraunhofer's page describes a free, limited version of its WUFI Pro moisture software for non-commercial use, made with ORNL, with climate data for 62 US and Canadian cities. [KNOWN: wufi.de] The code belongs to the partner; ORNL's part is [UNKNOWN] beyond co-development.

## Dead or moved pages (searched, did not resolve to the project)
- https://www.ornl.gov/technology/90000140 (CAN-D licensing page in search results) now opens an unrelated publication page. [KNOWN: fetched 2026-10-24]
- https://www.ornl.gov/content/wufi-software redirects to the ORNL home page. [KNOWN: fetched]
- https://web.ornl.gov/sci/buildings/tools/wufi/ returned 403. [KNOWN]
- https://www.ornl.gov/sites/default/files/TIP-Heartbeat-2018.pdf returned 404. [KNOWN]

## Cincinnatus
A search summary tied it to a 2018 ACM CCS poster on OS-independent malware detection from memory snapshots (doi 10.1145/3243734.3278527, with ORNL among the institutions). The poster's abstract does not name Cincinnatus, so it stays [UNKNOWN] and is not linked (RULES 10). An ORNL AI expo abstracts page showed up in search but returned an error when fetched.

## Fact-check notes (2026-10-29)
First full check of this file (no earlier logged check found).
- Verified: the Hyperion, URBAN-NET, Akatosh, Heartbeat and CAN-D pages and the Fraunhofer WUFI page resolve; the WUFI page confirms a free, limited WUFI ORNL (Pro) version co-developed with ORNL, with climate data for 62 US and Canadian cities; CPAD's OSTI records are a 2016 software record and a 2020-02-25 patent, both ORNL research org; the URBAN-NET 2016 paper DOI is in Crossref.
- Corrected: Heartbeat's report date (OSTI says 2022-10-01; the ORNL page says Feb 2024; both now given).
- Corrected: the Heartbeat license sentence. The 2024 story doesn't call the company small or say Heartbeat stayed on an R&D license (same fix as map link 198 earlier).
- Corrected: three claims tagged KNOWN from unfetched search results (Hyperion licensing history, the KDD 2019 paper, the Akatosh CCS paper). The first two are now INFERRED. The Akatosh DOI is confirmed in Crossref, so it stays KNOWN with that source.
- Unverifiable: the URBAN-NET paper page itself (doi.org returned an error; Crossref has the record).
- Dead or moved pages were not re-requested, and no new ORNL addresses were tried (RULES 16).

### Second pass (2026-10-29)
- WUFI "62 cities", free for non-commercial use: re-read on wufi.de. Verified.
- CPAD stays a patent plus a software record, with no docs page: OSTI API. Verified.
- Cincinnatus stays UNKNOWN and unlinked; the poster DOI was not used as evidence. Verified as tagged.
- Heartbeat dates re-read from the OSTI API (report number ORNL/TM-2022/2732). Verified.
- No further corrections.