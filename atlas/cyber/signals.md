# Outside-in signals across ORNL's public cyber work

Independent research, not affiliated with ORNL. Signals are read from public artifacts only (RULES 15 and 16): GitHub metadata through the public API, OSTI and DOE CODE records, Zenodo and PyPI counters, official job posts, and Wayback Machine capture lists. Nothing was scanned or probed. Read on 2026-11-21.

## What the outside tells us that the inside doesn't
1. **Public cyber code at ORNL is small and scattered.** Of the 191 public repos in the main ORNL GitHub org, about ten are security-related, and only Cyberwheel and OSCAR have more than a few hundred commits. [KNOWN: org listing via API; INFERRED: the "security-related" count is our judgment from names and descriptions]
2. **Big systems get licensed; helpers get released.** Situ, Heartbeat, AMIGO, AVUD and Cyber Grid Guard went to companies with no public code; pcapmunger, CANRate and Systemd Snapshot were released as small tools. [KNOWN: per brief; INFERRED: the pattern]
3. **Funding mix shifted.** Older records credit DHS S&T and IARPA (Stucco, Akatosh, Data Diode). Recent ones credit NNSA (CANRate, ELDSentry), CESER (CyTRICS, AI-PhyX, QKD papers), the Office of Electricity (Cyber Grid Guard), and LDRD or ASCR (fault benchmark, Cyberwheel, PETINA, EPB quantum). [KNOWN: per record; INFERRED: "shift", since the sample is small]
4. **Vehicles are the busiest public lane; AI security the most promoted.** [INFERRED from the dated artifacts below and the volume of 2025 to 2026 news]

## Code activity (GitHub API, 2026-11-21)
| Repo | Commits | First / last commit | Author names (last 100) | Releases | Stars |
|---|---|---|---|---|---|
| ORNL/oscar | 646 | 2026-11-08 / 2026-11-21 (latest 100) | 3 | v3.11.0 to v3.11.3 | 3 |
| ORNL/cyberwheel | 352 | to 2025-08-26 | 4 | v1.1.0 (2025-03), v2.0 (2025-08) | 57 |
| ORNL/PETINA | 157 | 2025-07-02 / 2026-10-13 | 5 | none on GitHub; PyPI 0.0.19 | 3 |
| ornl-sava/nv | 100+ | 2012-12-06 / 2016-01-25 | 3 | none | 31 |
| stucco/entity-extractor | 38 | 2014-01-09 / 2016-05-04 | 4 | none | 34 |
| stucco/auto-labeled-corpus | 23 | 2013-08-21 / 2019-11-27 | 6 | none | 97 |
| ORNL/TASQC | 14 | 2016-10-06 / 2019-05-21 | 5 | none | 2 |
| ORNL/CANRate | 9 | 2025-10-09 / 2026-02-19 | 1 | none | 0 |
| ORNL/Systemd_Snapshot | 3 | 2025-03-04 / 2025-08-25 | 1 | none | 2 |
| ORNL/pcapmunger | 1 | 2022-05-09 | 1 | none | 0 |

Commit totals come from the API's last-page link with one commit per page; first/last dates are from the latest 100 commits, so "first" is a floor for repos with more than 100 commits. [KNOWN: method]

## Usage counters
- ROAD dataset on Zenodo: 7,279 downloads, 3,255 unique, 6,328 views. [KNOWN: Zenodo API]
- PETINA on PyPI: 33 downloads in the last month. [KNOWN: pypistats API]
- Cyberwheel: 57 stars, 11 forks, 2 forks pushed after September 2025. [KNOWN: GitHub API] Cyberwheel is not on PyPI under that name (pypistats returned 404). [KNOWN]

## Funding sponsors on records (OSTI / DOE CODE / stories)
| Sponsor | Projects |
|---|---|
| NNSA | CANRate, ELDSentry |
| DOE CESER | CyTRICS (2026 report), AI-PhyX, QKD grid papers 2021 to 2024 |
| DOE Office of Electricity | Cyber Grid Guard |
| ORNL LDRD | CAN fault benchmark, Cyberwheel (see its deep dive), EPB polarization work (with ASCR) |
| DOE Office of Science ASCR | PETINA |
| DHS S&T | Stucco report; Akatosh transition program |
| IARPA | Data Diode |
| DoD / Navy | AMIGO (built on DoD request, used for a NAVWAR challenge) |

## Job posts (official board only, jobs.ornl.gov, searched 2026-11-21)
- Searching "cyber" returned 7 posts, including AI Cyber Engineer (cyber division) and a COMSEC Custodian. [KNOWN]
- "embedded" surfaced Senior R&D Professional, Secure and Resilient Communications (National Security Sciences). [KNOWN]
- "vulnerability" mostly surfaced classified-environment HPC and Linux posts and an information systems security officer post. [KNOWN] These are lab IT and operations roles, not research. [INFERRED]
- Reading: research hiring right now leans to ML-for-cyber and RF and embedded work, and almost every security post requires the ability to get a DOE clearance. [INFERRED from the posts read]

## Wayback Machine (capture lists only)
- hvcs.ornl.gov: first capture 2024-12, 9 monthly captures through 2026-07. [KNOWN]
- The CAISER page and the Securing Critical Assets page at their current URLs were first captured only in October 2026, and many ORNL images now sit under 2026 upload paths. [KNOWN] That suggests ornl.gov was restructured in 2026, so older URLs may differ. [INFERRED]
- The capture API returned no usable data for the Stucco and ORCA project pages. [KNOWN: logged in verification]

## Namesakes checked
- "Photon" and "Lantern" are common software names; only the ORNL CAISER pages and the March 2026 story are used. [UNRELATED: other projects with these names were not used]
- "OSCAR" is also a well-known HPC cluster toolkit; this atlas means ORNL's Open Source Central Alarm Monitoring. [UNRELATED: the cluster toolkit]
- "SHIELD" here is ORNL's CAN monitoring capability, not any other program of that name. [UNRELATED]
