# ORNL Atlas registries

These registries are the machine-readable spine of the atlas. They are deliberately separate from project prose so the atlas can grow by adding evidence and relationships instead of rewriting summaries.

## Files

- `sources.json` — public URLs, local provenance, retrieval status, evidence excerpts, and promotion state.
- `projects.json` — project or capability records and their proposed local translations.
- `facilities.json` — facilities, instruments, compute environments, or public infrastructure references.
- `software.json` — public software surfaces and local study tools. Candidate software stays a lead until its own primary record is checked.
- `roles.json` — public job families, teams, or role signals. A job posting does not prove a person's identity or a complete team structure.
- `edges.json` — typed relationships between records. Every non-local relationship carries a source ID and evidence level.

## Evidence states

- `verified` — the primary URL was directly fetched and the registry preserves a supporting excerpt or data point.
- `lead` — discovered in a source ledger or search pass but not promoted to verified in this repository.
- `blocked` — the URL is known, but direct retrieval failed or was blocked. The claim remains unknown.
- `local` — a safe local translation or tool, not an ORNL claim.

The registry never treats a search snippet as proof. `local_translation` and `study_proxy` relationships are explicitly not claims about ORNL implementation.

## Promotion rule

A lead becomes `verified` only after a researcher reads the primary source, records the fetch date, preserves a short supporting excerpt or data point, and updates the affected relationships. If a source contradicts an existing record, keep both records and mark the relationship or project as contested rather than silently replacing it.

## Validation

Run:

```bash
python3 scripts/validate_registry.py
```

The validator checks JSON syntax, unique IDs, dangling references, URL presence for external sources, and that every non-local edge names a source.

## Initial seed

The seed was compiled from the existing inside-out reconstruction and public-source ledgers on 2026-10-31. It is a starting map, not a census of ORNL.
