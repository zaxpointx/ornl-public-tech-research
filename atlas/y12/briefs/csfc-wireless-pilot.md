Short brief, no public code. Independent research, not affiliated with Y-12, CNS or NNSA. People by role only. Last checked: 2026-11-22.

# Classified Wi-Fi pilot using NSA's Commercial Solutions for Classified (CSfC)

- Source: NNSA FY 2025 Performance Evaluation Report for CNS, Key Outcome 6.1 and Objective 6.3 [1]
- Status: pilot completed in FY 2025; an enduring system depends on a later decision. [KNOWN: 1]

## Walkthrough (plain language)
- **What it is:** A test of whether Wi-Fi can be used safely inside a high-security building, built to NSA's public CSfC Wireless LAN design (layered commercial encryption). [KNOWN: 1]
- **How it was built:** Mostly virtual servers and network, but real CSfC-approved endpoint, access points, switch and wireless controller, built with an NSA "Trusted Integrator". [KNOWN: 1]
- **Use case tested:** A wireless hand scanner used during an inventory process. No classified data was used in the pilot. [KNOWN: 1]
- **Monitoring:** Alerts from the wireless controller and the SIEM were checked, and the team defined wireless intrusion detection (WIDS) steps to add to the incident response plan if the system goes permanent. [KNOWN: 1]
- **Unknown:** Products, configuration, and whether it will be deployed. Not pursued (out of scope).

## What stands out (interpretation)
It shows the site's direction: bring normal modern tools (wireless, smart procedures) into secure spaces using public, standards-based designs. CSfC and SIEM-based wireless monitoring are things a student can study from public NSA and NIST material. [INFERRED]

## Known / Inferred / Unknown
- KNOWN: Pilot scope as described in the report.
- INFERRED: Direction of travel.
- UNKNOWN: Everything beyond the report's paragraph. No guessing.

## Sources (accessed 2026-11-22)
1. https://www.energy.gov/sites/default/files/2026-02/Y-12%20FY%202025%20Performance%20Evaluation%20Report.pdf (NNSA PER, dated 2025-12-12); supports: all of the above

## Verification
Sweep 1 done on 2026-11-22: each load-bearing source above was fetched that day unless marked as seen in a search result. Sweep 2 (an independent re-read) has not been done, so this brief is not promoted to `discovery/catalog.csv`. See the [Y-12 atlas verification notes](../verification.md).
