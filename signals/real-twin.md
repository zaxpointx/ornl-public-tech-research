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
