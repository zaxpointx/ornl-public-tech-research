# Signals: gauntlet

## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- It's a one-time code release, not a living project. There are only 6 commits, all between 2025-07-09 and 2025-07-18, from 2 people, with no tags and no CI. [KNOWN: git log --all] Read: code published at the end of a funded effort. [INFERRED, medium]
- The first commit date matches the DOE CODE record date exactly (code-157761, 2025-07-09). [KNOWN]
- Sponsors are unusual for ORNL software: FEMA and DOE's Federal Energy Management Program. [KNOWN: OSTI sponsor field] Read: the work was for federal facilities and emergency planning, not for science users. [INFERRED, low]
- It ships as a Docker Compose app, with no HPC target. [KNOWN]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | 6 commits, 2025-07-09 to 2025-07-18 | git | [KNOWN] |
| Authors | 2 emails, 83% and 17% | git log | [KNOWN] |
| Tags and CI | None | repo | [KNOWN] |
| Funding | code-157761 lists ORNL as research org, FEMA and FEMP as sponsors | OSTI API | [KNOWN] |
| Other OSTI "gauntlet" hits | Mixed sponsors (NNSA and others), not checked as the same project | OSTI API | [UNKNOWN] |
