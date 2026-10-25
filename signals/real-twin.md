# Signals: real-twin

## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- It's brand new and moved fast. The first commit was 2024-12-20, then 221 commits in 2025 from 9 people and 105 so far in 2026. [KNOWN: git log --all]
- One author has 72% of commits. [KNOWN] Read: one lead developer with a rotating group of helpers. [INFERRED, low]
- The DOE CODE record (code-147051) is dated 2025-06-02, the same day as the v0.1.0 tag. [KNOWN] Funding is EERE, DOE's energy-efficiency office (its transportation side), which fits traffic digital twins. [KNOWN: OSTI sponsor field]
- It builds wheels for several operating systems and publishes to PyPI, and it even tracks its own GitHub dependents with a workflow. [KNOWN] Read: the team expects outside users. [INFERRED, medium] It ships sample road-network data for Chattanooga. [KNOWN: realtwin/data_lib]
- No supercomputer target. The GPU-word hits are all in binary slides and images. [UNRELATED]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2024-12-20, last 2026-10-08. 352 commits on all branches, 275 on main | git | [KNOWN] |
| Commits per year | 26, 221, 105 (2024 to 2026) | git log --all | [KNOWN] |
| Active authors per year | 1, 9, 5. 10 emails. Top 72% | git log | [KNOWN] |
| Tags | v0.1.0 2025-06-02, v0.1.1 2026-03-13, v0.1.2 2026-05-12 (plus one dev tag) | git | [KNOWN] |
| CI | Wheel builds across a matrix of OSes, pylint, dependents tracking | .github/workflows | [KNOWN] |
| Funding | code-147051 lists ORNL as research org and EERE as sponsor | OSTI API | [KNOWN] |

## Who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry, GitHub and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users.

**Outside vs inside:** Real-Twin is the only one of this batch published on PyPI (`realtwin`, 285 downloads last month), but it's new: its 2026 paper has 1 citation, from ORNL. Visible use is still the ORNL mobility team.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| PyPI | `realtwin` 0.1.2, "A Unified Simulation Scenario Generation Tool for Mobility Research", links to ORNL-Real-Sim/Real-Twin; repo pyproject name `realtwin` 0.1.2 | [KNOWN] | https://pypi.org/pypi/realtwin/json ; pyproject.toml |
| Downloads | 285 last month (2026-10-24). Not users | [KNOWN] counts | https://pypistats.org/api/packages/realtwin/recent |
| conda-forge / Spack | None (404) | [KNOWN] | registries |
| GitHub "used by" | "0 Repositories"; 13 stars, 3 forks, last push 2026-10-08 UTC | [KNOWN] | network/dependents; GitHub API |
| Citations | "Real-Twin: A Multi-Platform Simulation Scenario Generation Tool for Mobility Research" (SSRN 2026, 10.2139/ssrn.6427276): 1 citing work, with ORNL author | [KNOWN] | api.openalex.org |
| Namesakes | Other "digital twin scenario generation" papers are different projects | [UNRELATED] | api.openalex.org |

Reasoning: packaged for outside use but too new to show adopters [INFERRED, low confidence].
