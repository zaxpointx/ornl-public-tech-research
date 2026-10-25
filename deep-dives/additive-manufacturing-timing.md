# Additive manufacturing (3D-printing) tools: timing

## History, build targets, funding (discovery pass) (accessed 2026-10-24)

Scope: the five 3D-printing simulation tools in the catalog: adamantine, AdditiveFOAM, 3DThesis, Finch, Myna. Question from the editor: does their activity line up with any program start, end or funding shift? Sources are public git history (default branch, subject lines and dates only), GitHub tags, OSTI and DOE CODE records via the OSTI API, and the public Exascale Computing Project site.

### Outside milestones
- The Exascale Computing Project (ECP) "ran from 2016–2024" and its site says it has concluded. [KNOWN: https://www.exascaleproject.org/] ExaAM was its metal additive manufacturing application; the project overview paper is OSTI 1839327 (2022-01-10), sponsors NNSA and Office of Science. [KNOWN: OSTI API 1839327]
- EERE's manufacturing office shows up in OSTI sponsor fields as "Advanced Manufacturing Office" on 2021 records (1813276, 1772644) and as "Advanced Materials & Manufacturing Technologies Office (AMMTO)" from 2023 records on. [KNOWN: OSTI API sponsor fields] The exact rename date is not in these records. [UNKNOWN]
- Wayback snapshots were not used (the availability service errored all session). [UNKNOWN]

### Commits per year (default branch)
| Tool | First commit | Per year | Tags |
|---|---|---|---|
| adamantine | 2016-06-30 | 2016 56, 2017 47, 2018 0, 2019 29, 2020 113, 2021 229, 2022 173, 2023 140, 2024 171, 2025 159, 2026 172 | v1.0 2024-10-01, v1.1 2026-01-23 |
| 3DThesis | 2019-06-11 | 2019 1, 2020 1, 2021 3, 2022 0, 2023 8, 2024 85, 2025 14, 2026 7 | 2.0.0 2020-01-16, 3.0.0 2023-04-12, 4.0.0 2025-05-29 |
| AdditiveFOAM | 2023-03-28 | 2023 33, 2024 11, 2025 17, 2026 7 | 1.0.0 2023-06-13, 1.1.0 2025-05-14, 1.2.0 2026-06-29, 2.0.0 2026-08-31 |
| Finch | 2023-05-15 | 2023 98, 2024 86, 2025 4, 2026 4 | 0.1.0 2024-02-23, 0.2.0 2024-09-05 |
| Myna | 2023-05-11 | 2023 38, 2024 201, 2025 123, 2026 113 | 1.0.0 2024-08-19, 1.1.0 2025-04-09 |
[KNOWN: git log and git tag on public clones, 2026-10-24]

Monthly detail for 2024: Finch's work sat in Feb to May (36, 20, 14, 6) around its 0.1.0 tag, then nearly stopped. Myna climbed through mid-2024 and peaked in Aug and Sep (43, 32) around its 1.0.0 tag. 3DThesis went from almost nothing to a burst in Oct and Nov 2024 (37, 27). [KNOWN: git log by month]

Authors per year by commit email: adamantine 1 to 3 through 2023, then 7, 8 and 6 in 2024 to 2026; Myna 9 in 2024; 3DThesis 7 in 2024 after years of 1. Email counts can overcount people. [KNOWN: git log] The ornl.gov email share is a lower bound: Myna 83 to 100% every year; Finch 73% in 2023; adamantine 0% in 2016 to 2017, then 21 to 51%; AdditiveFOAM 15% in 2023 and 0% since. [KNOWN: git log; lower bound because personal emails are common]

### Software records and who pays
- 3DThesis: DOE CODE code-26241 (2018-12-21), sponsor just "USDOE". [KNOWN: OSTI API]
- AdditiveFOAM: code-108345 (2023-06-13, same day as its 1.0.0 tag), sponsors Office of Science and NNSA. Its 2025 code paper (OSTI 3002891) lists EERE and Office of Science. [KNOWN: OSTI API]
- Finch: code-122647 (2024-02-23, same day as 0.1.0), Office of Science and NNSA. [KNOWN: OSTI API]
- Myna: code-141169 (2024-08-19, same day as 1.0.0), Office of Science. Its 2025 paper (OSTI 3002570) lists AMMTO, Nuclear Energy and Office of Science. [KNOWN: OSTI API]
- adamantine: the 1.0 paper (OSTI 2472702, 2024-10-17) lists LDRD (ORNL's internal research fund) and EERE. [KNOWN: OSTI API]
- Office of Science plus NNSA is the same sponsor pair as the ExaAM overview paper. [KNOWN: OSTI API] That the three 2023-24 software records were filed under ExaAM money is [INFERRED, medium] from the matching sponsor pair and timing; the records do not name ECP.

### What the timing suggests
- Three tools (AdditiveFOAM, Finch, Myna) all got public repos within about seven weeks in spring 2023, the last full year of ECP. [KNOWN dates] Finch's activity collapsed after 2024, right as ECP ended. [KNOWN dates] That ECP's end caused the drop is [INFERRED, low to medium]; nothing public states it.
- Myna and adamantine kept going past 2024, and their later papers list EERE/AMMTO and Nuclear Energy rather than NNSA. [KNOWN: OSTI sponsor fields] A shift from exascale money toward applied manufacturing and nuclear money is [INFERRED, medium] from the sponsor fields only.
- adamantine is the one long-runner: an older solo project (2016 to 2017, no commits in 2018), then a steady team from 2020 on. Why it restarted in 2019 to 2020 is [UNKNOWN]; LDRD on its paper is the only funding clue.
- Each DOE CODE record was filed the same day as a first release tag, so releases and lab software filings move together. [KNOWN dates]

### Searched without result
- Any public statement linking these tools' start or slowdown to ECP or ExaAM funding: OSTI records, the four ORNL-MDF/ORNL repo READMEs, adamantine's README and the ECP home page checked, none says so. The only ECP trace is Finch's README listing Cabana, a library hosted in the ECP-copa GitHub org, as a dependency. (2026-10-24)
