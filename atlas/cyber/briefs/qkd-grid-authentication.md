Short brief: peer-reviewed paper and news; research prototype. Independent research, not affiliated with ORNL. People by role only. Last checked: 2026-11-21.

# Quantum key distribution for grid message authentication (EPB testbed)

- Paper: https://www.nature.com/articles/s41598-022-16090-w (Scientific Reports, 2022-07-26, open access) [1]
- OSTI: https://www.osti.gov/biblio/1879969 (sponsors include CESER) [2]
- 2025 follow-on news: https://www.ornl.gov/news/ornl-partnership-epb-tests-new-method-protecting-quantum-networks/ (2025-01-13) [3]
- License: Paper: open access. Prototype software: UNKNOWN (not public).
- Status: research (prototyped and demonstrated; not described as deployed)
- ORNL relationship (RULES 13): KNOWN: ORNL authors and research org [1, 2].
- Years visible in public sources: 2022 to 2025

## Walkthrough (plain language)
- **What it is:** Using keys from quantum key distribution (QKD) to authenticate control messages between grid devices, demonstrated on the EPB utility fiber network in Chattanooga. [KNOWN: 1]
- **The problem:** Grid control traffic (SCADA) needs messages that can't be forged. [KNOWN: 1]
- **What goes in:** Keys from commercial QKD hardware, read over a serial cable into a local key file. [KNOWN: 1]
- **What happens:** Each MQTT message gets a GMAC tag computed with a single-use QKD key and a fresh IV; keys carry serial numbers and are flagged as used so they can't be replayed. [KNOWN: 1]
- **What comes out:** Authenticated publish-subscribe messages between a distribution center and a substation. [KNOWN: 1]
- **Where humans act:** Engineers run the QKD link. [INFERRED]
- **What it is not:** Not whole-link encryption and not post-quantum cryptography. It uses QKD keys for message authentication. [KNOWN: 1]
- **Example:** The demonstration used Raspberry Pi 3 B+ boards acting as virtual energy-resource agents at each end. [KNOWN: 1]
- **Unknown:** Whether the software was published.

## How it works
1. QKD hardware at both sites over dedicated fiber. [KNOWN: 1]
2. A Python background service stores the keys. [KNOWN: 1]
3. The MQTT publish callback adds the tag; the subscriber verifies it. [KNOWN: 1]
4. 2025 follow-on: automatic polarization compensation kept an entangled signal running more than 30 hours with no downtime on EPB's quantum network, funded by ORNL LDRD and DOE ASCR. [KNOWN: 3]

## Outside-in signals
- OSTI lists several ORNL QKD papers from 2021 to 2024 with CESER among the sponsors. [KNOWN: OSTI API query, 2026-11-21]
- A patent application on the polarization method is mentioned. [KNOWN: 3]

## What stands out (interpretation)
Security students usually meet "quantum" as hype. This paper is concrete and readable: MQTT, GMAC, key serial numbers, replay protection.

## Related
- [TASQC](../../../projects/tasqc.md): earlier quantum-secured timing for the grid. [INFERRED: same theme]
- Atlas dossier: [quantum networking and grid security](../../guide/project-dossiers/quantum-networking-and-grid-security.md).

## Known / Inferred / Unknown
- KNOWN: Method, demo setup, funding.
- INFERRED: Status.
- UNKNOWN: Code.

## Sources (accessed 2026-11-21 unless noted)
1. https://www.nature.com/articles/s41598-022-16090-w (Scientific Reports paper); supports: method and demonstration
2. https://www.osti.gov/biblio/1879969 (OSTI record via API); supports: sponsor
3. https://www.ornl.gov/news/ornl-partnership-epb-tests-new-method-protecting-quantum-networks/ (ORNL news, 2025-01-13); supports: polarization follow-on

## Verification
Sweep 1 done on 2026-11-21: each load-bearing source above was fetched that day unless it is marked as seen in a search result. Sweep 2 (an independent re-read) has not been done, so this brief is not yet promoted to `discovery/catalog.csv`. See the [cyber atlas verification notes](../verification.md).
