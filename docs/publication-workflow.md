# Publication workflow

This repository has two identities: a living atlas that can change as public sources change, and a book manuscript that must be frozen, reviewable, and citable. Keep those identities explicit.

## Source of truth

- `discovery/catalog.csv` is the coverage source of truth.
- `projects/` contains project-level briefs.
- `deep-dives/` contains book-length case studies.
- `connections/` contains relationship claims and diagrams.
- `verification/` contains fact-check history and searched-but-not-found evidence.
- `docs/book-plan.md` is the editorial source of truth for the manuscript.

Do not hand-edit summary counts in several places without updating the underlying source and running the audit.

## Living-edition process

1. Add or revise evidence in the appropriate brief, deep dive, signal, or ledger.
2. Record retrieval dates and preserve stable URLs or identifiers.
3. Run the structure audit.
4. Run a second sweep over load-bearing claims and search for disconfirming evidence.
5. Update the Book Plan and reading navigation if the manuscript structure changes.
6. Record the change in the repository history with a specific message.

## Numbered-edition checklist

- [ ] Freeze the catalog and record the snapshot date.
- [ ] Run the audit and preserve its output in the release notes.
- [ ] Confirm every chapter is complete or explicitly marked as a bounded gap.
- [ ] Re-fetch load-bearing sources and update retrieval dates.
- [ ] Review counts, links, evidence labels, maturity language, and unknowns.
- [ ] Check that no private, restricted, or unverified material entered the edition.
- [ ] Update `CITATION.cff` with the edition date and version.
- [ ] Add release notes and an errata entry point.
- [ ] Archive the frozen source tree through an appropriate public archive before claiming a permanent edition.

## Reproducibility boundary

The goal is reproducibility of the published analysis, not reconstruction of private browsing or model state. Future improvements should add a manifest containing the snapshot commit, catalog checksum, source retrieval dates, audit version, and any generated counts. Do not store credentials, private data, or sensitive browsing artifacts.

## Corrections and errata

Corrections should use the issue template, identify the affected claim or file, provide a public source, and state whether the correction changes the synthesis. Material corrections should be recorded in the verification log and the next edition's release notes.
