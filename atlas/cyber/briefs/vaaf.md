Short brief (RULES 21): news story and lab site; offered for licensing; no public code. Independent research, not affiliated with ORNL. People by role only. Last checked: 2026-11-21.

# VAAF (Vehicle Attack Analysis Framework)

- News: https://www.ornl.gov/news/framework-available-study-vehicle-cyberattacks (2024-12-31) [1]
- Technology listing: https://www.ornl.gov/technology/202305432 [2]
- Heavy Vehicle Cyber Security site: https://hvcs.ornl.gov/research/ [3]
- License: Offered for commercial licensing. [KNOWN: 1]
- Status: unknown (no public code)
- ORNL relationship (RULES 13): KNOWN: developed at ORNL [1].
- Years visible in public sources: 2023 (technology ID) to 2026

## Walkthrough (plain language)
- **What it is:** A web app that lets someone without attack-writing skills run and analyze attacks on a vehicle's CAN bus, the network that links a vehicle's computers. [KNOWN: 1]
- **The problem:** Crafting CAN attacks takes expertise most testers don't have. [KNOWN: 1]
- **What goes in:** A vehicle's CAN bus. [KNOWN: 1]
- **What happens:** The framework emulates attacks and records metadata and CAN logs. [KNOWN: 1, 2]
- **What comes out:** Data on how the vehicle behaves under attack, and a planned security score per vehicle. [KNOWN: 1]
- **Where humans act:** Testers choose and run attacks in an authorized lab setting. [INFERRED]
- **What it is not:** Not public software. [KNOWN: licensing only]
- **Example:** UNKNOWN beyond the story.
- **Unknown:** Code and the attack library.

## How it works
1. A web front end over CAN tooling. [KNOWN: 1]
2. The lab site lists extending it to J1939, the heavy-truck CAN protocol. [KNOWN: 3]

## Outside-in signals
- The lab's current research list includes engine-controller firmware test benches, J1939 address-claim attacks, CAN attack detection and CAN forensics. [KNOWN: 3]
- The work is tied to protecting trucks carrying radioactive sources. [KNOWN: 1]
- Wayback first captured hvcs.ornl.gov in December 2024, the same month as the licensing story. [KNOWN: Wayback CDX, 9 monthly captures to 2026-07]

## What stands out (interpretation)
Vehicle security is the busiest public ORNL cyber line right now; see the [vehicle deep dive](../deep-dives/vehicle-cyber.md).

## Related
- [CAN-D](../../../projects/can-d.md), [SHIELD](shield-can.md), [CANRate](canrate.md), [ELDSentry](eldsentry.md), [ROAD dataset](road-can-dataset.md). [INFERRED: same lab area]

## Known / Inferred / Unknown
- KNOWN: Purpose, licensing path, J1939 extension.
- INFERRED: Lab workflow.
- UNKNOWN: Code.

## Sources (accessed 2026-11-21 unless noted)
1. https://www.ornl.gov/news/framework-available-study-vehicle-cyberattacks (ORNL news, 2024-12-31); supports: purpose, licensing, score plan
2. https://www.ornl.gov/technology/202305432 (ORNL technology listing); supports: title (seen in search results, not re-fetched)
3. https://hvcs.ornl.gov/research/ (ORNL HVCS site); supports: current research list

## Verification
Sweep 1 done on 2026-11-21: each load-bearing source above was fetched that day unless it is marked as seen in a search result. Sweep 2 (an independent re-read) has not been done, so this brief is not yet promoted to `discovery/catalog.csv`. See the [cyber atlas verification notes](../verification.md).
