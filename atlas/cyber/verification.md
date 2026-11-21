# Cyber atlas: verification notes

Independent research, not affiliated with ORNL. Sweep 1 and spot checks done 2026-11-21. Sweep 2 (an independent re-read of every brief and re-fetch of load-bearing sources, RULES 11) is still to do. Until then, the 24 new projects stay in [cyber-catalog.csv](cyber-catalog.csv) and are not added to `discovery/catalog.csv`.

## What sweep 1 covered
- Every ornl.gov story or page cited as a primary source was fetched on 2026-11-21: Photon, CAISER launch, CAISER page, AI-PhyX, Cyber Grid Guard, VAAF, SHIELD, Stucco, ORCA, CyTRICS news, Securing Critical Assets, Grid Security, AI/ML cyber range, Lantern, AVUD, AMIGO and the EPB quantum story. The CRID fact sheet PDF was downloaded and its section and facility names checked with pdftotext.
- OSTI records were read through the public OSTI API: 1879969, 3364695, 1440330, 1239653, 1231925, 1822873, code-192285, code-177813, code-145906, code-96071, code-95906, code-2281.
- DOE CODE pages were read for 192285, 145906, 95906 and 96071 to find repository links.
- GitHub data came from the unauthenticated public API (repo metadata, commits, releases, forks, contents).
- Zenodo record 10462796 and the pypistats API were read for usage counts.
- Two job posts were read in full on jobs.ornl.gov (req. 17230 and 17427); search result titles were read for "cyber", "security", "vulnerability", "embedded", "intern", "reverse engineering" and "cyber-physical".
- The Scientific Reports QKD paper was read for its method and demo setup.

## Spot checks against fresh clones (RULES 17)
| Claim | API value | Fresh clone | Verdict |
|---|---|---|---|
| Cyberwheel has 352 commits, last on 2025-08-26 | 352, 2025-08-26 | 352, 2025-08-26T18:30-04:00 | verified |
| Systemd Snapshot has 3 commits and no license file | 3, no license | 3, no LICENSE file | verified |
| AVUD and Hyperion share credited authors | n/a | OSTI 1231925 authors vs AVUD page authors: six names in common | verified (participation only) |
| ROAD and CAN-D share a credited author | n/a | OSTI 1822873 vs Zenodo creators: one name in common | verified (participation only) |

## Claims kept at a lower tag on purpose
- The DHS archive page for STUCCO, the GovCIO interview about Photon's release timing, the 2011 SPIE paper on ORCA, the ORNL research-portal group profile, an ORNL staff page for the Embedded Systems Security group, the VAAF technology listing and the DOE.jobs group-lead listing were seen only in search results. They are marked "seen in search results" or KNOWN-from-search-result and are not load-bearing.
- Photon's performance numbers are ORNL's own claims.

## Searched, nothing found (bounded negative evidence)
| Date | Looking for | Where | Result |
|---|---|---|---|
| 2026-11-21 | Public Photon or Lantern code | ORNL GitHub org listing (191 repos), GitHub repo search `org:ORNL` with security terms | none |
| 2026-11-21 | Public VAAF or SHIELD code | ORNL org listing; DOE CODE keyword "controller area network" via OSTI API | none |
| 2026-11-21 | ORNL repos for malware, intrusion, attack, vulnerability | GitHub repo search `org:ORNL` per term | none beyond Cyberwheel, TASQC, DistGANs (not security) |
| 2026-11-21 | ORNL monthly CESER activity note (OSTI 3015555) | https://www.osti.gov/biblio/3015555 and the OSTI API | "not found"; seen only in a search snippet, not used |
| 2026-11-21 | OSTI software records on "adversarial" or "threat intelligence" at ORNL | OSTI API, product type Software | none |
| 2026-11-21 | Wayback capture lists for the Stucco and ORCA project pages | Wayback CDX API | no usable response |
| 2026-11-21 | Cyberwheel on PyPI | pypistats API | 404 |

## Out of scope and not pursued
- Device names in CyTRICS testing, OSCAR deployment sites, vehicle models and any vulnerability details.
- How AMIGO generates evasive samples.
- Personal accounts behind the ELDSentry and CAN fault-benchmark repositories (reached only through DOE CODE).
- Anything behind a login. No account was created anywhere.
