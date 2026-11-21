Short brief: DOE CODE record, no public repo. Independent research, not affiliated with ORNL. People by role only. Last checked: 2026-11-21.

# Data Driven User Emulator

- DOE CODE: https://www.osti.gov/doecode/biblio/96071 [1]
- License: UNKNOWN
- Status: unknown (record dated 2020-09-01)
- ORNL relationship (RULES 13): KNOWN: OSTI research org ORNL [1].
- Years visible in public sources: 2020

## Walkthrough (plain language)
- **What it is:** Software that drives real applications the way a person would, using models learned from real user data, to generate realistic traffic for testing intrusion detection. [KNOWN: 1]
- **The problem:** Traffic that doesn't look human makes IDS tests misleading. [KNOWN: 1]
- **What goes in:** Real user behavior data. [KNOWN: 1]
- **What happens:** Data-science models choose actions that drive actual applications. [KNOWN: 1]
- **What comes out:** Realistic background traffic. [KNOWN: 1]
- **Where humans act:** Experimenters configure it. [INFERRED]
- **What it is not:** Not an attack generator. [KNOWN: 1]
- **Example:** UNKNOWN beyond the record.
- **Unknown:** Code and models.

## How it works
1. Described only at record level. [KNOWN: 1]

## Outside-in signals
- Fits the range work in the 2021 cyber-range paper. [INFERRED]

## What stands out (interpretation)
Background traffic is the unglamorous half of every security experiment.

## Related
- [ORCA and pcapmunger](orca.md). [INFERRED]

## Known / Inferred / Unknown
- KNOWN: Purpose.
- INFERRED: Range link.
- UNKNOWN: Everything else.

## Sources (accessed 2026-11-21 unless noted)
1. https://www.osti.gov/doecode/biblio/96071 (DOE CODE record and OSTI API); supports: description

## Verification
Sweep 1 done on 2026-11-21: each load-bearing source above was fetched that day unless it is marked as seen in a search result. Sweep 2 (an independent re-read) has not been done, so this brief is not yet promoted to `discovery/catalog.csv`. See the [cyber atlas verification notes](../verification.md).
