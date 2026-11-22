Short brief, no public code. Independent research, not affiliated with Y-12, CNS or NNSA. People by role only. Last checked: 2026-11-22.

# RCAPTS: Readiness Certification Assurance Process Tracking System

- OSTI software record: https://www.osti.gov/biblio/1231477 (2011-06-08, B&W Y-12 era contract) [1]
- License: copyright license to a small business (Weatherly Consulting), announced 2023-01-11 [2]; listed in NNSA's 2025 tech transfer calendar [3]
- Status: in use; the calendar says it supports the Uranium Processing Facility (UPF) project. [KNOWN: 3]
- Years visible: 2011 to 2025

## Walkthrough (plain language)
- **What it is:** A web-based, multi-user tool that manages readiness reviews, the formal checks DOE requires before a nuclear facility starts up or restarts (DOE Order 425.1). [KNOWN: 1, 3]
- **The problem:** For a big project, tracking every readiness requirement on paper is overwhelming. [KNOWN: 1]
- **What happens:** It routes workflows, notifies people when action is needed, stores evidence files and links, and gives real-time status. [KNOWN: 2, 4]
- **What comes out:** An organized evidence package for the review team. [KNOWN: 1]
- **Where it spread:** The licensee has supplied it to Savannah River, WIPP and the Nevada site under a commercial form of government-use licensing. [KNOWN: 3]
- **Stack:** The licensing book lists it among CNS apps; one sibling app in the same list runs on PHP in any JavaScript-enabled browser, but RCAPTS's own stack is UNKNOWN. [KNOWN: 4]

## What stands out (interpretation)
The clearest public example of Y-12 software escaping the fence: built in-house, then licensed and reused across the weapons complex. A clean "workflow + audit trail" app is also a very buildable student project. [INFERRED]

## Sources (accessed 2026-11-22)
1. https://www.osti.gov/biblio/1231477 (OSTI API record); supports: description, date
2. https://pantex.energy.gov/news/blog/cns-developed-software-streamlines-readiness-reviews-aids-small-business (CNS news, 2023-01-11); supports: license, features
3. https://www.energy.gov/sites/default/files/2024-12/NNSA%20Tech%202025%20Calendar_with%20links.pdf (NNSA tech transfer calendar, May 2025 page); supports: UPF use, other sites
4. https://www.y12.doe.gov/sites/default/files/assets/document/ygg-16-0036R4_tt_commercialization_partnership_book.pdf (CNS Technology Transfer Commercialization and Partnerships Book, PDF dated 2025-03/04); supports: features list

## Verification
Sweep 1 done on 2026-11-22: each load-bearing source above was fetched that day unless marked as seen in a search result. Sweep 2 (an independent re-read) has not been done, so this brief is not promoted to `discovery/catalog.csv`. See the [Y-12 atlas verification notes](../verification.md).
