# <Name>

Template for projects/<id>.md. Adapted 2026-10-24 from the team's RULES.md template plus the useful parts of an outside review's case-study template and engineering checklist. Section names below are the ones to use. Every claim gets a tag (KNOWN, CORROBORATED, INFERRED, UNKNOWN, UNRELATED) and a source. People are described by role only.

- Official page / Repo / Docs / License / Status (active, archived, unknown, stub-osti-only, draft-osti-only)
- ORNL relationship: KNOWN / CORROBORATED / INFERRED (which primary source names ORNL, per RULES item 13)
- Years visible in public sources: <first year> to <last year>
- Last checked: YYYY-MM-DD

## Walkthrough (plain language)
RULES item 12: what it is, the problem, what goes in, what happens, what comes out, where humans act, what it is not, what's unknown. One concrete example.

## What it is (plain English, 2-4 sentences)

## How it works (plain English, no jargon without definition)
Write the flow as numbered steps (input, processing, output, where a person acts). Every step has a source or is tagged INFERRED.

## How the project is organized
Fill from templates/engineering-checklist.md. Record what is visible; if no public source explains why a choice was made, the reason is UNKNOWN.

## Timeline
| Date | Event | Source | Tag |
|---|---|---|---|

## Who uses it / why it matters

## Related projects
Filled by the connections pass, matching connections/map.md.
| Related item | Relationship (uses, extends, shares data, same facility, related topic, unknown) | Source | Tag |
|---|---|---|---|

## What stands out
Interpretation only, kept apart from the facts above.

## Ten questions (GOAL.md)
Answer each in one to three sentences with a link, or write UNKNOWN.
1. What problem does it solve, and for whom?
2. Where does it sit in the tree: which area, facility or program?
3. Who pays for it, according to public records?
4. How is the code organized, and what languages and tools does it use?
5. Is it alive? What do its commit history and releases say?
6. Who outside ORNL actually uses or cites it?
7. What does it connect to, upstream and downstream?
8. What does it teach about how ORNL works?
9. Could a student learn from it or contribute to it, and what would they need first?
10. What is still unknown, and what was searched without result?

## Known / Inferred / Unknown

## Verification notes
Filled by the fact-check pass: what was checked, what was corrected, searches that found nothing (also logged in verification/not-found.md).

## Sources (URL, title, accessed date, what it supports)

## Quality gate
- [ ] Every load-bearing claim has a source and a tag
- [ ] Facts are kept apart from interpretation
- [ ] ORNL relationship is not overstated, and maturity verbs match the source (RULES item 10)
- [ ] Walkthrough, flow, timeline and unknowns are present
- [ ] Ten questions answered or marked UNKNOWN
- [ ] No copied text beyond short cited quotes; people by role only
- [ ] Two fact-check sweeps done (RULES item 11)
- [ ] INDEX, catalog, LAB-TREE and connections map updated
