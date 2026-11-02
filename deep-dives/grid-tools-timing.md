# Grid tools (GridKit, ReSolve, ExaGO): timing

## History, build targets, funding (discovery pass) (accessed 2026-10-24)

Scope: the three grid deep-dive tools. Question: does their activity line up with a program start, end, handoff or funding change? Sources are public git history (subject lines and dates only), GitHub tags, OSTI and DOE CODE records via the OSTI API, repo READMEs, and the public ECP site. Commit counts are from signals/gridkit.md and signals/exago.md (both swept) plus a fresh ReSolve clone.

### Outside milestones
- The Exascale Computing Project (ECP) "ran from 2016–2024". [KNOWN: https://www.exascaleproject.org/] ExaSGD, its power-grid application, shows up in ORNL-tagged OSTI records from 2020 to 2024 (for example 1738891, 2020-03-25; 2441467, 2024-05-29, which lists ECP as a sponsor). [KNOWN: OSTI API] ExaGO is ExaSGD's grid optimization code. [INFERRED, medium: OSTI hits for "ExaGO" and "ExaSGD" are largely the same records]
- ReSolve's README says its development "was supported by the Exascale Computing Project (ECP)". [KNOWN: github.com/ORNL/ReSolve README, Support section]
- OSTI 3385022, "Execution Plan for 'Next Generation Grid Simulations' Project", dated 2025-04-01, ORNL research org, sponsor Office of Science ASCR (its computing research program). Its abstract proposes large-scale dynamic grid simulations with many inverter-based resources (solar, wind and batteries tied in through power electronics) and says it builds on SciDAC institutes. [KNOWN: OSTI API 3385022] It does not name GridKit or ReSolve. [KNOWN: abstract read]
- ExaGO moved from PNNL to ORNL: the ORNL repo was created 2026-01-08 and pnnl/ExaGO is archived. [KNOWN: signals/exago.md, GitHub API]
- Wayback snapshots: not used this pass (availability service unreliable). [UNKNOWN]

### Commits per year (all branches unless noted)
| Tool | First commit | Per year | Tags |
|---|---|---|---|
| GridKit | 2017-02-01 | 2017 15, 2018 2, 2019 7, 2020 0, 2021 8, 2022 5, 2023 5, 2024 20, 2025 426, 2026 947 | v0.0.7 2023-07-17, v0.1.0 2025-04-14, v0.2.0 2026-10-01 |
| ReSolve | 2023-05-02 | 2023 167, 2024 74, 2025 220, 2026 405 (default branch: 142, 29, 66, 46) | latest v0.99.2 2025-11-04, v0.99.3 2026-08-12, v0.99.4 2026-09-25 |
| ExaGO | 2019-04-26 | 2019 280, 2020 265, 2021 375, 2022 185, 2023 205, 2024 33, 2025 9, 2026 255 | kpp2 2023-08-17, v2.0.0 2026-05-21, v2.1.0 2026-10-08 |
[KNOWN: git log and git tag on public clones]

Monthly detail: GridKit's climb starts around Dec 2024 (10) and Jan to Feb 2025 (17, 26), then peaks in Apr to May 2025 (42, 105), the same weeks as its v0.1.0 tag and right after the 3385022 execution plan date. ExaGO's 2026 work ramps Feb to Apr (37, 49, 53) right after the ORNL repo appeared. ExaGO's last busy stretch before that was Sep to Nov 2023 (18, 32, 54 across all branches; 9, 8, 14 on the default branch), a few months after its kpp2 tag. [KNOWN: git log by month]

### Software records and who pays
- GridKit: DOE CODE code-152622 (2025-03-14), sponsor just "USDOE". [KNOWN: OSTI API]
- ReSolve: code-114681 (2023-10-16), sponsor "USDOE"; ECP credit in README. [KNOWN]
- ExaGO: code-176348 "ExaGO v2" (2026-03-02), sponsor "USDOE". Its earlier ORNL-tagged papers list Office of Science and NNSA, ECP's two parent offices. [KNOWN: OSTI API]

### What the timing suggests
- ExaGO and ReSolve are both ECP-era codes. ExaGO's activity fell off a cliff in 2024 to 2025 (33, then 9 commits) as ECP ended. [KNOWN dates] That ECP's end caused the drop is [INFERRED, medium]: same timing, ECP-parent sponsors on its papers, but no public statement.
- ReSolve dipped in 2024 too (74 commits across all branches, 29 on the default branch) (corrected in a fact-check pass, 2026-10-29) but recovered in 2025 and 2026, so something kept it funded after ECP. [KNOWN dates] What that is, is [UNKNOWN]; the new DOE CODE record only says USDOE.
- GridKit sat nearly idle for seven years, then jumped in 2025 with about 20 authors. The new ASCR grid-simulation execution plan (April 2025) fits that jump, since both are ORNL, both are about dynamic grid simulation, and GridKit's busiest month followed it. [INFERRED, medium] The plan doesn't name GridKit, so the link stays a guess.
- ExaGO's 2026 restart lines up with its move to ORNL. Whether it is paid by the same new grid project is [UNKNOWN]; the shared contributors with GridKit (signals/exago.md) make it plausible but don't prove it.
- Unlike the same-day filings for three of the four 3D-printing records, these DOE CODE records land within one to three months before a release tag (GridKit record 2025-03-14 vs v0.1.0 2025-04-14; ExaGO v2 record 2026-03-02 vs v2.0.0 2026-05-21). [KNOWN dates]

### Searched without result
- A public source naming who funds GridKit's 2025 jump or ExaGO's 2026 restart: OSTI records for both names, both READMEs, and the 3385022 abstract checked; none names a program for either tool. (2026-10-24)

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Verified against fresh clones of ORNL/GridKit, ORNL/ExaGO and ORNL/ReSolve, the OSTI API and the GitHub API: first commits, per-year counts and tags for all three; GridKit's Dec 2024 to May 2025 monthly climb (19 distinct commit names in 2025); ExaGO's Feb to Apr 2026 ramp; ReSolve's ECP credit (README line 140); all six OSTI records, including 3385022's ASCR sponsor, ORNL research org and the fact that its abstract names neither GridKit nor ReSolve; pnnl/ExaGO archived and ORNL/ExaGO created 2026-01-08.
- Corrected: ExaGO's Sep to Nov 2023 monthly counts (were 4, 12, 18, which matched neither all branches nor the default branch).

## Fact-check notes (2026-10-29)
Second logged check of this file (the first was the 2026-10-24 sweep), on fresh treeless clones.
- Verified: ExaGO repo created 2026-01-08; GridKit monthly counts Dec 2024 to May 2025 (10, 17, 26, 42, 105, all branches, author dates); GridKit v0.1.0 tag exists; ECP "ran from 2016–2024".
- Corrected (label only): ReSolve's 74 in 2024 is all branches; the default branch has 29.
