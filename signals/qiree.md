
## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- The project is small and slow-moving: 48 commits in about 2.5 years, with none after 2025-12-02. [KNOWN: git log] Read: an early research prototype, not a staffed product. [INFERRED, medium]
- The release dates disagree. The v0.1.0 tag commit is dated 2025-12-02, the GitHub release was published 2026-05-05 (UTC), and DOE CODE gives 2025-01-15. [KNOWN: git, GitHub API, code-149694] Read: the code was frozen, then announced months later. [INFERRED, low]
- ASCR is the main sponsor, on 3 of 6 OSTI hits including the DOE CODE record. LDRD and BES each appear once. [KNOWN: OSTI API]
- CI runs on ubuntu-latest, and one job picks its runner from an expression. There's no named supercomputer and no GPU runner. [KNOWN]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2023-06-20, last 2025-12-02. 48 commits across all branches, 46 on default | git | [KNOWN] |
| Commits per year | 2023: 1, 2024: 30, 2025: 17 | git log --all | [KNOWN] |
| Active / new authors per year | 2023: 1/1, 2024: 6/5, 2025: 6/3. 9 emails in total. Top three 37%, 22%, 18% | git log | [KNOWN] |
| Tags | v0.0.0 2024-06-25, v0.1.0 2025-12-02 (release published 2026-05-05 UTC) | git, GitHub API | [KNOWN] |
| Funding | code-149694 lists ASCR. Across 6 OSTI hits: ASCR 3, LDRD 1, BES 1 | OSTI API | [KNOWN] |
| Wayback | Nearest captures 2024-12-11 and 2026-06-07 | availability API | [KNOWN], but only bounds the dates |

## Who actually uses it (connections pass)
Accessed 2026-10-24 (ET). Artifacts only (RULES 16); institution names from OpenAlex, no individuals profiled. Detail in connections/map.md links 117, 141-145.

**Outside vs inside:** The inside presents QIR-EE as a cross-platform engine for running quantum programs (QIR) on many backends. Outside, it has no package on PyPI, Spack or conda-forge and 0 GitHub dependents; its one visible consumer is ORNL's own IRIS runtime (Q-IRIS), and its papers are ORNL-led with Georgia Tech and Quantum Science Center partners.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| PyPI / Spack / conda-forge | None (404 for qiree in all three) | [KNOWN] | pypi.org; spack-packages builtin; github.com/conda-forge |
| Downloads | Not applicable (no registry package) | [KNOWN] | n/a |
| GitHub "used by" | "0 Repositories" | [KNOWN] | https://github.com/ORNL-QCI/qiree/network/dependents |
| In-house consumer | IRIS build lists DeviceQIREE.cpp / LoaderQIREE.cpp; Q-IRIS paper (OSTI 3018176) integrates IRIS with XACC "via ... (QIR-EE)" | [CORROBORATED] | github.com/ORNL/iris src/runtime/CMakeLists.txt; https://www.osti.gov/biblio/3018176 |
| Citations | OpenAlex: QIR-EE software record (Georgia Tech, ORNL), "A cross-platform execution engine for the quantum intermediate representation" (2025, 4 cites; ORNL, Georgia Tech, Quantum Science Center, a university), several 2026 ORNL QIR runtime papers | [KNOWN] | api.openalex.org search=QIR-EE |
| Backends it targets | qsim (default), XACC and Pennylane Lightning (optional) | [KNOWN] | CMakeLists.txt options |

Reasoning: no packaging, no dependents, and an ORNL-internal consumer suggest a research engine used by ORNL quantum-computing groups and partners, not yet adopted downstream [INFERRED, medium confidence].
