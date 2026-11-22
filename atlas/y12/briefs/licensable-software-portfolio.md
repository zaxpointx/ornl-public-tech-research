Short brief, no public code. Independent research, not affiliated with Y-12, CNS or NNSA. People by role only. Last checked: 2026-11-22.

# Y-12's licensable software portfolio (CNS licensing book, 2025)

CNS says it holds copyrights to multiple software codes covering knowledge preservation, predictive modeling, records management, decision tools and emergency management, and that it writes software because the site runs its own clinic, firehouse, communications and maintenance. [KNOWN: 1] All are offered for licensing; none is open source. [KNOWN: 1, 2]

| App | What it does (per the book) | Readiness note in book | Brief |
|---|---|---|---|
| RCAPTS | Readiness review tracking | licensed | [brief](rcapts.md) |
| eDC/RO | Routes documents for classification review | | [brief](edc-ro.md) |
| eIROS | Web workflow for information release requests and approvals | | this page |
| EMBOS / ERMS | Medical records and record maintenance | | [brief](embos.md) |
| EMInS | Emergency Management Information System: real-time data, maps, video, responder rosters, GIS links | "currently in use at Y-12" | this page |
| FMES | Facility Management Enterprise System: status boards for production, utility and facility systems, monthly reporting | | this page |
| HERO | Highly Efficient Reliable Operations: web view of product life-cycle tasks and production deliverables | | this page |
| ELMS | Electronic Logistics Management System: container inventory and history across enterprise sites | | this page |
| Knowledge Preservation Management | Captures video, animation, process maps and work instructions from retiring workers | | this page |
| Multi-Channel Analyzer Application | Windows touchscreen app that runs a gamma-spectrum analyzer, automates quality checks, saves spectra | | this page |

## What stands out (interpretation)
- The portfolio is **enterprise business software**, not security tools: workflow, records, dashboards, logistics. That is what most software engineers at a production plant build. [INFERRED]
- Licensing is the only public channel. Nothing is on GitHub or DOE CODE beyond three old OSTI records. [KNOWN: [signals](../signals.md)]
- A 32-second Y-12 video says several site-built programs are now used by other government and commercial groups. [KNOWN: 3]

## Sources (accessed 2026-11-22)
1. https://www.y12.doe.gov/sites/default/files/assets/document/ygg-16-0036R4_tt_commercialization_partnership_book.pdf (CNS Technology Transfer Commercialization and Partnerships Book, PDF dated 2025-03/04); supports: table, rationale. Developer names in the book are left out.
2. https://www.y12.doe.gov/technologies (Y-12 technology transfer page); supports: licensing process, OTCP
3. https://www.y12.doe.gov/library/video/software-development (Y-12 video page); supports: reuse claim

## Verification
Sweep 1 done on 2026-11-22: each load-bearing source above was fetched that day unless marked as seen in a search result. Sweep 2 (an independent re-read) has not been done, so this brief is not promoted to `discovery/catalog.csv`. See the [Y-12 atlas verification notes](../verification.md).
