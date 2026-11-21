Short brief (RULES 21): ORNL news story only; patented and licensed. Independent research, not affiliated with ORNL. People by role only. Last checked: 2026-11-21.

# Cyber Grid Guard

- News: https://www.ornl.gov/news/ornl-developed-cybersecurity-framework-graduates-lab-electric-grid/ (2026-06-10) [1]
- Capability page: https://www.ornl.gov/capabilities/grid-security/ [2]
- License: Commercial license to GridForge Energy Solutions. [KNOWN: 1]
- Status: unknown (licensed; no public code)
- ORNL relationship (RULES 13): KNOWN: developed at ORNL [1].
- Years visible in public sources: up to 2026

## Walkthrough (plain language)
- **What it is:** A blockchain-backed system that checks whether data and device settings in a substation have been tampered with. [KNOWN: 1]
- **The problem:** Operators can't always trust the voltage, breaker and settings data their devices report, and tampering can cause outages. [KNOWN: 1]
- **What goes in:** Configuration and operating data from grid devices: voltage, frequency, breaker status, power quality. [KNOWN: 1]
- **What happens:** Data is copied across several servers and constantly checked against the latest settings recorded in a blockchain; logs trace where changes came from; each packet is matched to a device inventory kept in the ledger. [KNOWN: 1]
- **What comes out:** Alerts about unusual behavior or setting changes, naming the exact settings changed. [KNOWN: 1]
- **Where humans act:** Grid operators receive the alerts. [KNOWN: 1]
- **What it is not:** Not a cryptocurrency; it borrows the tamper-evident ledger idea. [KNOWN: 1]
- **Example:** Someone changes a relay's trip setting. The new value doesn't match the ledger, and the operator gets an alert naming the device and the setting. (Illustrative, built from 1.)
- **Unknown:** Ledger technology, code, performance numbers.

## How it works
1. Tested in a substation test bed at ORNL's GRID-C and in an operating ORNL substation, against simulated denial-of-service and multi-step data-altering attacks. [KNOWN: 1]

## Outside-in signals
- Funded by the DOE Office of Electricity. [KNOWN: 1]
- The licensee came through LabStart, a lab-commercialization nonprofit. [KNOWN: 1] Grid security is a live commercialization path in 2026. [INFERRED]

## What stands out (interpretation)
Tamper-evident logging can be rebuilt by a student with a hash chain and a few Raspberry Pis; no blockchain platform needed.

## Related
- [AI-PhyX](ai-phyx.md), [QKD grid authentication](qkd-grid-authentication.md): other ways to trust grid data. [INFERRED]

## Known / Inferred / Unknown
- KNOWN: Purpose, testing, license, sponsor.
- INFERRED: Commercial trend.
- UNKNOWN: Implementation details.

## Sources (accessed 2026-11-21 unless noted)
1. https://www.ornl.gov/news/ornl-developed-cybersecurity-framework-graduates-lab-electric-grid/ (ORNL news, 2026-06-10); supports: all claims
2. https://www.ornl.gov/capabilities/grid-security/ (ORNL grid security capability page); supports: grid communications and security group context

## Verification
Sweep 1 done on 2026-11-21: each load-bearing source above was fetched that day unless it is marked as seen in a search result. Sweep 2 (an independent re-read) has not been done, so this brief is not yet promoted to `discovery/catalog.csv`. See the [cyber atlas verification notes](../verification.md).
