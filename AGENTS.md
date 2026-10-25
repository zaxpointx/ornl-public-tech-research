# Research-team operating rules

This repository is an independent public-source reconstruction of ORNL-related technology. It is not affiliated with ORNL, UT-Battelle, or DOE.

## Scope and safety

- Use only public pages, public repositories, public documentation, OSTI/DOE records, and public papers.
- Study artifacts, never systems: do not scan networks, probe services, bypass access controls, log in, or seek restricted/export-controlled/classified material.
- Do not profile individuals. Use project roles and credited authors only when needed to establish authorship or source provenance.
- Summarize copyrighted material in original language; keep quotes short and attributed.

## Evidence standard

- Tag claims `[KNOWN]`, `[CORROBORATED]`, `[INFERRED]`, `[UNKNOWN]`, or `[UNRELATED]`.
- Every load-bearing claim needs a primary source URL, access date, and a short evidence note. Search snippets are discovery aids, not final evidence.
- Never upgrade a source's wording: studied, prototyped, tested, deployed, and operated are different claims.
- Keep negative searches in `verification/not-found.md`; failure to find a source is not proof of absence.
- A project is not complete until its brief has passed two independent review sweeps.

## File ownership

- `discovery/catalog.csv`: catalog editor only.
- `INDEX.md`: editorial lead only; counts must be generated or checked by the validator.
- `projects/`: project researchers, one project per batch owner.
- `signals/`: signals researcher after the project brief exists.
- `deep-dives/`: deep-dive lead, one project at a time.
- `verification/`: evidence checker; never erase corrections.
- `connections/map.md`: relationship analyst, using evidence from briefs and verification.
- `docs/` and `batches/`: editor after review.

Do not have two workers edit the same file concurrently. Researchers write batch artifacts; the editor merges shared indexes and maps after review.

## Definition of done for one project

A project has a complete brief when it answers: purpose and users; inputs, flow, outputs, and human decisions; repository/docs structure; languages/build/tests/releases; funding or ownership where public evidence exists; upstream/downstream relationships; outside use or citations; status; unknowns and searches; and source URLs with access dates. It must pass two review sweeps.

A deep dive additionally includes a synthesis, timeline, system/data-flow map, roles, source ledger, missing-artifacts ledger, claim-boundary ledger, and verification report.

## Standard batch

Work in batches of no more than five projects. Each batch must update its project briefs, source/evidence notes, verification log, unknowns ledger, connections, batch summary, and index status together. Run `python3 scripts/audit_atlas.py` before committing.
