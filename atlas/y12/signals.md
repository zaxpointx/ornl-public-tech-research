# Outside-in signals for Y-12 cyber and software

Independent research, not affiliated with Y-12, CNS or NNSA. Signals come from public artifacts only (RULES 15 and 16): the public OSTI API, GitHub and Zenodo public APIs, official job boards, public budget and oversight documents. Nothing was scanned or probed, and no Y-12, CNS, NNSA or DOE host was queried beyond reading public pages that search results or other public pages linked to. Read on 2026-11-22.

## What the outside tells us that the inside doesn't
1. **Almost no public code.** Zero GitHub orgs or repos for Y-12 or CNS, zero Zenodo records, and three OSTI software records, the newest from 2017. [KNOWN: API queries below]
2. **Licensing is the only software channel.** The 2025 licensing book lists about ten copyrighted apps; none is open source. [KNOWN: [S27](source-ledger.md#s27)]
3. **Patents are hardware.** OSTI lists 143 Y-12 patents; among the 40 most recent (2018 to 2023), one is mainly software. [KNOWN: OSTI listing; INFERRED: classification by title]
4. **Publication output dropped sharply after 2023.** OSTI records attributed to Y-12: 79 in 2021, 37 in 2023, 10 in 2024, 2 in 2025, 6 so far in 2026. [KNOWN: OSTI API counts] This could be indexing lag, a change in release policy, or less output; we can't tell which. [UNKNOWN]
5. **Cyber money is rising enterprise-wide.** NNSA's IT and Cybersecurity line goes from $598M (FY 2025 enacted) to $688M (FY 2026 enacted) to $935M (FY 2027 request). [KNOWN: [S15](source-ledger.md#s15)] How much reaches Y-12 is not broken out in the overview. [UNKNOWN]
6. **The site is assessed on cyber about every three to eight years, publicly by title only:** 2012, 2015, 2018, 2026. [KNOWN: [S10](source-ledger.md#s10)]

## OSTI counts (public OSTI API, research organization contains "Y-12", 2026-11-22)
| Query | Count |
|---|---|
| All records | 3,540 |
| Technical reports | 2,463 |
| Conference items | 714 |
| Patents | 143 |
| Journal articles | 134 |
| Software | 3 |
| Full text matches "cyber" | 14 (about 6 are actually about cybersecurity; the rest mention it in passing) |
| Words machine learning (unquoted) | 98 (the exact phrase returns far fewer; the most recent are in the briefs) |
| Words digital twin (unquoted) | 16; the exact phrase returns 2 (both 2026 journal articles) |

Method: `https://www.osti.gov/api/v1/records?research_org=Y-12&...&rows=1`, reading the `x-total-count` header. Counts include old Y-12 Plant records from the 1990s and depend on how OSTI tags organizations. [KNOWN: method; INFERRED: caveats]

| Year | OSTI records attributed to Y-12 |
|---|---|
| 2015 | 14 |
| 2018 | 55 |
| 2021 | 79 |
| 2023 | 37 |
| 2024 | 10 |
| 2025 | 2 |
| 2026 (to Nov 22) | 6 |

## Code and data platforms
| Platform | Query | Result |
|---|---|---|
| GitHub orgs | "Y-12", "y12", "consolidated nuclear security", "cns-llc", "y12nsc" | no Y-12 or CNS org (only unrelated accounts) |
| GitHub repos | "Y-12 National Security Complex", "Consolidated Nuclear Security", "y12nsc", "Y-12 oak ridge" | 0 |
| Zenodo | "Y-12 National Security Complex", "Consolidated Nuclear Security" | 0 |
| DOE CODE / OSTI software | research org Y-12, Y-12 National Security Complex, Consolidated Nuclear Security | 3, 1 (subset), 0 |

## Contract and money
| Signal | Value | Source |
|---|---|---|
| Operator contract end | 2027-09-30 | [S1](source-ledger.md#s1) |
| Planned recompete | award in 2027 (intent) | [S2](source-ledger.md#s2) |
| FY 2025 award fee available | $21M; CNS earned 92% of award fee | [S8](source-ledger.md#s8) |
| Y-12 site funding | FY 2025 enacted $2.78B; FY 2026 enacted $2.42B; FY 2027 request $2.55B | [S15](source-ledger.md#s15) |
| Y-12 Field Office funding | FY 2027 request $33.7M | [S15](source-ledger.md#s15) |

## Job posts (official job boards; search results marked)
| Title | Where seen | What it signals | Tag |
|---|---|---|---|
| Network/Security Operations Center (Intern/Co-op/Postgrad category, Associate level) | DOE.jobs, fetched | SIEM, IDS/IPS, Splunk, Security+; degree or 8+ years of training and experience | KNOWN: [S24](source-ledger.md#s24) |
| Vulnerability Assessment Analyst; Vulnerability Analyst | DOE.jobs and career.com search results (DOE.jobs page returned 404 when fetched) | Vulnerability work is staffed | KNOWN-from-search-result: [S25](source-ledger.md#s25) |
| Cybersecurity Artificial Intelligence Engineer | aggregator search results (posted 2026-08-15, closing 2026-11-12) | AI/ML threat detection plus OT security (NIST 800-53 for OT, NIST 800-82) | KNOWN-from-search-result: [S25](source-ledger.md#s25) |
| ISS Software Developer | Glassdoor search result | C#, Java, React, SQL, web APIs, DevSecOps for lab applications | KNOWN-from-search-result: [S25](source-ledger.md#s25) |

Aggregator listings are not load-bearing; RULES 16 counts only official boards, so these stay at the search-result level.

## Reasoning from signals to conclusions
- No code + licensing-only + hardware patents → software is treated as an internal asset or a licensable product, never as open research output. Confidence: high. [INFERRED]
- Rising budget + OT language in plans + an AI-and-OT cyber job → OT security and AI are where new cyber work is going. Confidence: medium (small sample). [INFERRED]
- Falling OSTI output → cannot interpret without more data. Confidence: low. [UNKNOWN]
