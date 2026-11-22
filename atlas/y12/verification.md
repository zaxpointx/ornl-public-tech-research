# Y-12 atlas: verification notes

Independent research, not affiliated with Y-12, CNS or NNSA. Sweep 1 and spot checks done 2026-11-22. Sweep 2 (an independent re-read of every brief and re-fetch of load-bearing sources, RULES 11) is still to do. Until then, the 13 briefs stay in [y12-catalog.csv](y12-catalog.csv) and are not added to `discovery/catalog.csv`.

## What sweep 1 covered
- Every y12.doe.gov, energy.gov, gao.gov and pantex.energy.gov page marked "fetched" in the [source ledger](source-ledger.md) was downloaded on 2026-11-22. PDFs (FY 2025 PER, IG-0785, FY 2027 NNSA budget overview, CNS licensing book, IBCI report, NNSA tech calendar, LLNL Bernie poster) were read with pdftotext and each quoted number was checked against the text.
- OSTI records were read through the public OSTI API (`/api/v1/records`), including full abstracts and affiliations for every record cited.
- GitHub org and repo searches used the unauthenticated public search API. Zenodo used its public records API.
- One job post was read in full on DOE.jobs (NOC/SOC). Other job titles are search-result level only.

## Spot checks
| Claim | Check | Verdict |
|---|---|---|
| CNS contract runs to 2027-09-30 | NNSA contract page (S1) and NNSA strategy table (S2) agree; the 2024 press release (S4) said 2025 plus two 1-year options, which adds up to 2027 | verified (options exercised is INFERRED from the arithmetic) |
| FY 2025: Excellent overall, 92% of award fee, Goal 4 Very Good | PER text lines on ratings (S8) | verified |
| IT and Cybersecurity $688M to $935M (+36%) | FY 2027 overview summary table (S15) | verified |
| 38 laptops; 26 wireless-capable; majority with malware; no classified data | IG-0785 pages 4 to 5 (S11) | verified. A search-engine summary had wrongly said all 38 "lacked authorization"; the report says one was found in 2006 and up to 37 more "may have been" introduced. This atlas follows the report. |
| MTEWS prototype up to 350 nodes | IBCI abstract and body (S33) | verified |
| OSTI software records = 3 | OSTI API, research_org=Y-12, product_type=Software, x-total-count | verified |
| Y-12 intern GPA | Current student page says 2.8 (S22); older recruiting page says 3.0 (S23) | conflict kept visible in learn-and-build |

## Claims kept at a lower tag on purpose
- The Nuclear Production One protest history and "no RFI yet" come only from a gated trade-press extract (S47). Marked KNOWN-from-search-result.
- The FY 2026 performance plan wording (S9) comes from a search extract of a third-party mirror.
- All job titles other than the NOC/SOC post (S25) come from search results or aggregators, which RULES 16 does not count as official boards.
- ORNL's NGSI county list (S50) came from a search extract; ornl.gov returned 403 to our fetch on 2026-11-22.

## Searched, nothing found (bounded negative evidence)
| Date | Looking for | Where | Result |
|---|---|---|---|
| 2026-11-22 | A Y-12 or CNS GitHub org | GitHub user search, type org: "Y-12", "y12", "consolidated nuclear security", "cns-llc", "y12nsc" | none (only unrelated accounts) |
| 2026-11-22 | Repos mentioning Y-12 or CNS | GitHub repo search: "Y-12 National Security Complex", "Consolidated Nuclear Security", "y12nsc", "Y-12" oak ridge | 0 |
| 2026-11-22 | Y-12 datasets or software on Zenodo | Zenodo API, exact phrases "Y-12 National Security Complex" and "Consolidated Nuclear Security" | 0 |
| 2026-11-22 | DOE CODE software from Y-12 under CNS | OSTI API research_org "Consolidated Nuclear Security", product type Software | 0 (the 3 Y-12 software records predate or sit outside that org label) |
| 2026-11-22 | DOE CODE search endpoint | POST to a guessed doecode API path | not found; that guessed path was not retried, and the OSTI records API was used instead |
| 2026-11-22 | Public text of DOE cyber assessments of Y-12 | EA report title page (S10) | titles only, no reports |
| 2026-11-22 | A Y-12 high school internship | Y-12 student programs and university recruitment pages; web search | none; internships start at college junior standing |
| 2026-11-22 | Later MTEWS or IBCI results | web search for MTEWS and IBCI | only the FY 2019 report |
| 2026-11-22 | Software-focused Y-12 patents | 40 most recent OSTI patent records | one (task-load training) |
| 2026-11-22 | The Vulnerability Assessment Analyst post on DOE.jobs | direct fetch of the URL seen in search | 404 (likely closed) |

## Skipped on purpose
- **A university-hosted slide deck about Y-12 reliability engineering and maintenance tools** (rmc.utk.edu, posted 2025-11) was fetched once while checking a search result. Several slides carry a **CUI** (Controlled Unclassified Information) banner. Under this atlas's rules it was treated as controlled: **nothing from it is used, quoted or summarized here**, and it is not linked. Only the fact that it was skipped is logged. The related public journal articles on OSTI (S38, S39) were used instead.
- **Physical security content.** The 2021 OSTI talk on AI/ML testing of physical security systems (S36) is listed by title only and was not opened.
- **Specific site equipment.** One public OSTI report (S33) names a machine-tool model used at Y-12. It is left out; it adds nothing for learning and edges toward mapping site systems.
- **Personal names.** OSTI author lists, the licensing book's developer credits, news stories and a staff-profile page name people. None appear here; roles only.
- **Anything about classification decisions, nuclear material control, or the content of any oversight finding beyond the public wording.**

## Out of scope and not pursued
- Any probing, scanning, DNS or subdomain work, or guessed paths on Y-12, CNS, NNSA or DOE hosts.
- Gated sites (the GovWin market analysis was seen only as a search extract and not opened), sign-ups or logins.
- Contacting anyone at Y-12, CNS, Roane State or ORAU.
