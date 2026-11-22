Short brief, no public code. Independent research, not affiliated with Y-12, CNS or NNSA. People by role only. Last checked: 2026-11-22.

# EMBOS: Electronic Medical Business Operations System

- OSTI software record: https://www.osti.gov/biblio/1231514 (2012-04-16), sponsor DOE Office of Defense Programs [1]
- Licensing book entry: yes, with a sibling, ERMS (Electronic Record Maintenance System) [2]

## Walkthrough (plain language)
- **What it is:** A web-based electronic medical record built for Y-12's occupational health clinic. [KNOWN: 1]
- **The problem:** A DOE worker-safety rule (10 CFR 851) required medical records to be electronic by 2015. [KNOWN: 1]
- **What it tracks:** Exams, medical surveillance programs (asbestos, hearing, respirators), certifications, lab data, prescriptions, immunizations and Human Reliability Program processing, with interfaces to SAP and other site systems. [KNOWN: 1]
- **Stack:** The licensing book's ERMS entry says it runs in any JavaScript-enabled browser on a network with PHP installed. Whether EMBOS shares that stack is UNKNOWN. [KNOWN: 2]

## What stands out (interpretation)
It shows why a plant like Y-12 writes its own software: it runs its own clinic, fire department and maintenance, and each needs systems that meet DOE rules. The licensing book says this directly. [KNOWN: 2; INFERRED: framing]

## Sources (accessed 2026-11-22)
1. https://www.osti.gov/biblio/1231514 (OSTI API record); supports: description
2. https://www.y12.doe.gov/sites/default/files/assets/document/ygg-16-0036R4_tt_commercialization_partnership_book.pdf (CNS Technology Transfer Commercialization and Partnerships Book, PDF dated 2025-03/04); supports: ERMS stack note, self-sufficiency rationale

## Verification
Sweep 1 done on 2026-11-22: each load-bearing source above was fetched that day unless marked as seen in a search result. Sweep 2 (an independent re-read) has not been done, so this brief is not promoted to `discovery/catalog.csv`. See the [Y-12 atlas verification notes](../verification.md).
