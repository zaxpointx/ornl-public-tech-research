Short brief (RULES 21): capability page only. Independent research, not affiliated with ORNL. People by role only. Last checked: 2026-11-21.

# SHIELD (CAN intrusion monitoring for high-consequence cargo)

- Capability page: https://www.ornl.gov/capabilities/shield/ [1]
- License: UNKNOWN
- Status: unknown
- ORNL relationship (RULES 13): KNOWN: ORNL capability page [1].
- Years visible in public sources: UNKNOWN (page is undated)

## Walkthrough (plain language)
- **What it is:** An in-vehicle monitor that watches a truck's CAN/J1939 traffic for signs of tampering. [KNOWN: 1]
- **The problem:** Trucks carrying radioactive material can be tampered with during stops, or reached wirelessly through telematics. [KNOWN: 1]
- **What goes in:** Live CAN/J1939 messages. [KNOWN: 1]
- **What happens:** Three kinds of detection: signatures for known attacks such as reprogramming, timing checks for injected messages and denial of service, and content checks on decoded messages. [KNOWN: 1]
- **What comes out:** Alerts to the driver, dispatch or law enforcement. [KNOWN: 1]
- **Where humans act:** People receive and act on alerts. [KNOWN: 1]
- **What it is not:** Not a public tool. [KNOWN: no code]
- **Example:** A burst of extra messages on one CAN ID trips the timing check. (Illustrative; matches the timing category in 1.)
- **Unknown:** Code, deployment, date.

## How it works
1. Signature, timing and content-aware detection. [KNOWN: 1]
2. Integrates with ORNL's C-STAR and T-STAR monitoring systems. [KNOWN: 1]

## Outside-in signals
- The three detector types line up with the attack classes in the public ROAD dataset (fuzzing, fabrication, masquerade). [INFERRED: comparison only, no stated link]

## What stands out (interpretation)
A clean mental model for any CAN IDS: what you already know (signatures), when it arrives (timing), what it says (content).

## Related
- [VAAF](vaaf.md), [CAN-D](../../../projects/can-d.md). [INFERRED]

## Known / Inferred / Unknown
- KNOWN: Detector design.
- INFERRED: Fit with ROAD.
- UNKNOWN: Status.

## Sources (accessed 2026-11-21 unless noted)
1. https://www.ornl.gov/capabilities/shield/ (ORNL capability page); supports: all claims

## Verification
Sweep 1 done on 2026-11-21: each load-bearing source above was fetched that day unless it is marked as seen in a search result. Sweep 2 (an independent re-read) has not been done, so this brief is not yet promoted to `discovery/catalog.csv`. See the [cyber atlas verification notes](../verification.md).
