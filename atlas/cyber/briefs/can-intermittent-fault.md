Short brief: DOE CODE record with public code. Independent research, not affiliated with ORNL. People by role only. Last checked: 2026-11-21.

# CAN intermittent fault detection benchmark

- DOE CODE: https://www.osti.gov/doecode/biblio/145906, DOI 10.11578/dc.20241022.1 [1]
- The record links a public repository under an individual's account; reached through the record.
- License: See the DOE CODE record. [KNOWN: 1]
- Status: unknown (record dated 2024-10-25)
- ORNL relationship (RULES 13): KNOWN: OSTI research org ORNL, sponsor ORNL LDRD [1].
- Years visible in public sources: 2024

## Walkthrough (plain language)
- **What it is:** Code and data comparing machine-learning and deep-learning models for catching intermittent faults in vehicle CAN data in a streaming setting. [KNOWN: 1]
- **The problem:** Faults that come and go are hard to catch, and the same signals matter for safety and security. [KNOWN: 1]
- **What goes in:** Labeled CAN time series. [KNOWN: 1]
- **What happens:** Models are compared using time-series cross-validation. [KNOWN: 1]
- **What comes out:** Benchmark results. [KNOWN: 1]
- **Where humans act:** Researchers pick the models. [INFERRED]
- **What it is not:** Not an intrusion detector, though the methods overlap. [INFERRED]
- **Example:** UNKNOWN beyond the record.
- **Unknown:** Result summary (not re-read).

## How it works
1. Supervised classification with time-series cross-validation. [KNOWN: 1]

## Outside-in signals
- LDRD funding means ORNL spent its own discretionary research money on CAN analytics. [INFERRED from the sponsor field]

## What stands out (interpretation)
A good template for a student ML project: a fixed dataset, several models, honest validation.

## Related
- [ROAD dataset](road-can-dataset.md). [INFERRED: same data domain]

## Known / Inferred / Unknown
- KNOWN: Purpose, sponsor.
- INFERRED: Overlap with security.
- UNKNOWN: Results.

## Sources (accessed 2026-11-21 unless noted)
1. https://www.osti.gov/doecode/biblio/145906 (DOE CODE record and OSTI API); supports: description, sponsor, date

## Verification
Sweep 1 done on 2026-11-21: each load-bearing source above was fetched that day unless it is marked as seen in a search result. Sweep 2 (an independent re-read) has not been done, so this brief is not yet promoted to `discovery/catalog.csv`. See the [cyber atlas verification notes](../verification.md).
