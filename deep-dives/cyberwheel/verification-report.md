# Cyberwheel deep dive: verification report
Status: VERIFIED (2026-10-24). OSTI 3827147 as a successor stays UNVERIFIABLE.
Written in the fact-check pass, 2026-10-24. Covers synthesis.md, lineage.md, timeline.md, system-flow.md, people-roles.md and claim-boundary.md. The source list is in source-ledger.md and the gaps are in missing-artifacts.md. Every row is in verification/log.md.

## Result
The core picture holds. Cyberwheel is a public, MIT-licensed, LDRD-funded ORNL research environment for training RL cyber-defense agents. v2.0 added emulation through Sandia's FIREWHEEL. The repo has been quiet since 2025-08-26.
- Verified: LDRD funding (CORROBORATED, S3 + S4), project 11049 (KNOWN, one source), both p.13 quotes word for word, repo dates and license, the release-note wording, Atomic Red Team in the code, the Poetry install with requirements.txt as fallback, and the three abstracts showing use (S7, S8).
- Corrected:
  - map link 56: shared authors aren't independent, so it was split.
  - claim-boundary row 7: "modified version" is attributed to the LDRD report only.
  - "Internal" is now INFERRED, not KNOWN.
- Unverifiable: what Firewheel modification was made, who owns it at division level, and outside authors' affiliations.

## Wording to keep
Use "research environment", "developed", "showed". Don't use "deployed", "adopted", "dead", "fork", or "trained on 100,000 nodes". The reading-pass claim-boundary.md matches this report after the row 7 fix.

## Scope check
Everything is public: repo, OSTI/DOE CODE, a published LDRD report, papers. There's no restricted, internal or non-public content. Nothing implies we're affiliated with ORNL. The people named are limited to public credit lines (people-roles.md).
