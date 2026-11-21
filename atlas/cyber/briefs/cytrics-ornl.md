Short brief: program role, no public code. Independent research, not affiliated with ORNL. People by role only. Last checked: 2026-11-21.

# CyTRICS work at ORNL (energy device supply-chain testing)

- ORNL news: https://www.ornl.gov/news/researchers-assess-grid-components-improve-cyber-physical-security/ (2022-11-18) [1]
- DOE CESER program page: https://www.energy.gov/ceser/cybersecurity-testing-resilient-industrial-control-systems [2]
- CyTRICS one-pager: https://cytrics.inl.gov/content/uploads/25/2025/07/2022-05-04-CyTRICS-one-pg_formatted.pdf [3]
- OSTI report: https://www.osti.gov/biblio/3364695 ("CyTRICS Assessment Report: Whole Home Battery Applications", ORNL/SPR-2026/4609, 2026-06-01) [4]
- License: n/a (program)
- Status: active (an ORNL CyTRICS report is dated 2026-06). [KNOWN: 4]
- ORNL relationship (RULES 13): KNOWN: ORNL is a performing lab [1]; OSTI lists ORNL as research org for the 2026 report, sponsor CESER [4].
- Years visible in public sources: 2018 (program conceived) to 2026

## Walkthrough (plain language)
- **What it is:** DOE's program to take apart and test the hardware, software and firmware in important energy-sector devices, and share findings with vendors and utilities. ORNL is one of the testing labs. [KNOWN: 1, 2, 3]
- **The problem:** Grid devices are built from global supply chains that even their makers can't fully see into. [KNOWN: 1]
- **What goes in:** Priority devices supplied by manufacturers under agreements. [KNOWN: 1, 3]
- **What happens:** Teams take devices apart, list every component and software file (a bill of materials), and test firmware for weaknesses; results go into a shared CyTRICS database. [KNOWN: 1, 3]
- **What comes out:** Hardware and software bills of materials and vulnerability findings, disclosed to vendors and asset owners. [KNOWN: 2, 3]
- **Where humans act:** Lab analysts do the teardown and testing; disclosure follows a standard vendor agreement. [KNOWN: 2]
- **What it is not:** Not public vulnerability publishing; the database is shared among participants. [KNOWN: 2]
- **Example:** For one small device, ORNL documented about 180 physical components and 3,500 software files. [KNOWN: 1]
- **Unknown:** Which devices were tested. That is not public, and this repo does not try to find out.

## How it works
1. Devices are prioritized by impact, prevalence and national-security interest. [KNOWN: 3]
2. A standard test process and reporting format. [KNOWN: 2]
3. The 2026 report applies the approach to mobile apps for home battery systems: dependencies, permissions and runtime behavior. [KNOWN: 4]

## Outside-in signals
- The 2026 OSTI report lists authors from ORNL, INL and PNNL, with ORNL as research org. [KNOWN: 4]
- A search result showed what looked like an ORNL monthly CESER status note (OSTI 3015555), but the record returns "not found" today, so it is not used here. [KNOWN: tried 2026-11-21; logged in the verification notes]

## What stands out (interpretation)
This is where embedded and firmware skills are used. The CRID fact sheet lists an Embedded Systems Lab, and an embedded systems security group was hiring a group lead in 2026. [KNOWN: fact sheet; DOE.jobs listing seen in search results]

## Related
- [AVUD](avud.md): earlier ORNL static firmware analysis for smart meters. [INFERRED: same skill area]

## Known / Inferred / Unknown
- KNOWN: Program design, ORNL role, the 2026 report.
- INFERRED: The staffing link.
- UNKNOWN: Device lists (out of scope).

## Sources (accessed 2026-11-21 unless noted)
1. https://www.ornl.gov/news/researchers-assess-grid-components-improve-cyber-physical-security/ (ORNL news, 2022-11-18); supports: ORNL role and numbers
2. https://www.energy.gov/ceser/cybersecurity-testing-resilient-industrial-control-systems (DOE CESER page); supports: program elements
3. https://cytrics.inl.gov/content/uploads/25/2025/07/2022-05-04-CyTRICS-one-pg_formatted.pdf (CyTRICS one-pager); supports: prioritization, data repository
4. https://www.osti.gov/biblio/3364695 (OSTI record via API); supports: the 2026 report

## Verification
Sweep 1 done on 2026-11-21: each load-bearing source above was fetched that day unless it is marked as seen in a search result. Sweep 2 (an independent re-read) has not been done, so this brief is not yet promoted to `discovery/catalog.csv`. See the [cyber atlas verification notes](../verification.md).
