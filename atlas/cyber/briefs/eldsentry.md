Short brief: DOE CODE record, open source. Independent research, not affiliated with ORNL. People by role only. Last checked: 2026-11-21.

# ELDSentry

- DOE CODE: https://www.osti.gov/doecode/biblio/192285, DOI 10.11578/dc.20260916.1 [1]
- OSTI: https://www.osti.gov/biblio/code-192285 [2]
- The record links a public repository under an individual's GitHub account. Under this repo's people-by-role rule it is reached through the DOE CODE record rather than linked here.
- License: Listed on the DOE CODE record. [KNOWN: 1]
- Status: active (record dated 2026-10-01)
- ORNL relationship (RULES 13): KNOWN: OSTI research org ORNL, sponsor NNSA [2].
- Years visible in public sources: 2026

## Walkthrough (plain language)
- **What it is:** A small device built from off-the-shelf parts that sits between a truck's Electronic Logging Device (ELD) and its diagnostic port to block wireless attacks that come in through the ELD. [KNOWN: 2]
- **The problem:** Federal rules have required ELDs in most commercial trucks since 2017, and a 2024 university demonstration showed an ELD could be used as a wireless way into a truck's network. [KNOWN: 2]
- **What goes in:** Traffic between the ELD (or another untrusted device) and the SAE J1939 diagnostic port or the newer telematics port. [KNOWN: 2]
- **What happens:** Open-source firmware filters what the untrusted device is allowed to send. [KNOWN: 2]
- **What comes out:** A vehicle network that accepts only allowed traffic from the ELD. [INFERRED from 2]
- **Where humans act:** Fleet owners install it. [INFERRED]
- **What it is not:** Not a replacement for the ELD. [KNOWN: 2]
- **Example:** A compromised ELD tries to send engine commands; ELDSentry drops them. (Illustrative.)
- **Unknown:** Filter rules in detail, field tests.

## How it works
1. Inline filter hardware plus open firmware. [KNOWN: 2]

## Outside-in signals
- NNSA sponsorship ties this to the same radioactive-cargo transport mission as VAAF and SHIELD. [INFERRED from the sponsor field plus the VAAF story]

## What stands out (interpretation)
The newest ORNL vehicle-security release (October 2026) and the most buildable: off-the-shelf parts and open firmware.

## Related
- [CANRate](canrate.md): same sponsor, released the same year. [KNOWN: both NNSA per OSTI]

## Known / Inferred / Unknown
- KNOWN: Purpose, sponsor, date.
- INFERRED: Mission link.
- UNKNOWN: Rule set, testing.

## Sources (accessed 2026-11-21 unless noted)
1. https://www.osti.gov/doecode/biblio/192285 (DOE CODE record); supports: repository link, license list
2. https://www.osti.gov/biblio/code-192285 (OSTI record via API); supports: description, sponsor, date

## Verification
Sweep 1 done on 2026-11-21: each load-bearing source above was fetched that day unless it is marked as seen in a search result. Sweep 2 (an independent re-read) has not been done, so this brief is not yet promoted to `discovery/catalog.csv`. See the [cyber atlas verification notes](../verification.md).
