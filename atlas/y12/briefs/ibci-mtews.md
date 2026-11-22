Short brief, no public code. Independent research, not affiliated with Y-12, CNS or NNSA. People by role only. Last checked: 2026-11-22.

# IBCI and MTEWS: a cyber range for the manufacturing supply chain

- Report: *FY2019 Final Report for Industrial Base Cybersecurity Initiative (IBCI) Project*, Y/PM-19-120, CNS, 2019-10-01 [1]
- OSTI: https://www.osti.gov/biblio/1581185, DOI 10.2172/1581185 [1]
- Sponsors: DoD Manufacturing Industrial Base Policy and DOE's Advanced Manufacturing Office, plus Y-12 Plant Directed Research and Development (PDRD) money for university tasks [KNOWN: 1]
- Partners named: Los Alamos National Laboratory (co-lead), UNC Charlotte, University of West Florida, Idaho National Laboratory, Sandia [KNOWN: 1]
- Status: UNKNOWN after FY 2019. No later public report found.
- Years visible: 2019

## Walkthrough (plain language)
- **What it is:** A plan and prototype for a "Manufacturing Threat Evaluation Wargaming System" (MTEWS): a virtual copy of the kinds of networks small and medium manufacturers run, used to test how new attacks would spread and which defenses work. [KNOWN: 1]
- **The problem:** Weapons designs can leak through small suppliers deep in the supply chain that have little IT security. [KNOWN: 1, abstract]
- **What goes in:** Network characterization data from manufacturers (manual or semi-automatic for now), plus known exploits for manufacturing equipment. [KNOWN: 1]
- **What happens:** A VMware-based model of representative networks (prototype up to 350 nodes at UNC Charlotte), simulated workers as autonomous agents, and a draft "Manufacturing Network Risk Index" score. [KNOWN: 1]
- **What comes out:** Risk scores and best-practice guidance; long term, a national manufacturing cyber operations center. [KNOWN: 1, stated as a goal]
- **Where humans act:** Analysts characterize networks; penetration tests on real networks were planned to check that the range gives the same answers. [KNOWN: 1]
- **Side projects:** University students built a phone-based check that a machine-tool program (G-code "part program") on a CNC machine matches the reference copy by comparing hashes; another task checked machine-tool firmware integrity using independent sensors. [KNOWN: 1]
- **What it is not:** Not a tool for attacking anyone. Every test ran in isolated ranges or sandboxes. [KNOWN: 1, sandbox language]
- **Unknown:** Whether MTEWS was ever built beyond the prototype.

## What stands out (interpretation)
This is the closest public Y-12 project to the kind of work in the ORNL cyber atlas: a cyber range with simulated users and risk scoring, similar in spirit to ORNL's AI/ML cyber range and Cyberwheel. The part-program hash check is a great small student project. [INFERRED]

## Related
- [ORNL AI/ML cyber range](../../cyber/briefs/ai-ml-cyber-range.md) and [Cyberwheel](../../../projects/cyberwheel.md). [INFERRED: similar idea, no shared authors checked]
- [IIoT risk report](iiot-risk-report.md). [INFERRED: same OT-security concern]

## Known / Inferred / Unknown
- KNOWN: Sponsors, partners, tasks, 350-node prototype, risk index concept.
- INFERRED: Similarity to ORNL ranges.
- UNKNOWN: Outcome after 2019; any code.

## Sources (accessed 2026-11-22)
1. https://www.osti.gov/biblio/1581185 and full text https://www.osti.gov/servlets/purl/1581185 (OSTI record and PDF); supports: everything above. One specific equipment model named in the report is left out on purpose.

## Verification
Sweep 1 done on 2026-11-22: each load-bearing source above was fetched that day unless marked as seen in a search result. Sweep 2 (an independent re-read) has not been done, so this brief is not promoted to `discovery/catalog.csv`. See the [Y-12 atlas verification notes](../verification.md).
