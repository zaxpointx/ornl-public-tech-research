Short brief (RULES 21): built from an ORNL project page and an OSTI software record; no public code.

# Hyperion

- Official page: https://www.ornl.gov/division/projects/hyperion [KNOWN: fetched 2026-10-29]
- OSTI: https://www.osti.gov/biblio/1231925 (software record, 2014-09-01, research org ORNL, sponsor USDOE) [KNOWN: OSTI records API, accessed 2026-10-29]
- Repo / Docs: none public [KNOWN: discovery/stub-search-2026-10-24.md]
- License: UNKNOWN (no public code)
- Status: unknown

## Walkthrough
Hyperion is a tool for working out what a compiled program really does without having its source code. [KNOWN: project page]
The problem: most software you run comes as a binary (machine code), so you can't read it the way you'd read Python. Malware hides in binaries, and so do plain bugs. [INFERRED: standard background]
What goes in: an executable program. [KNOWN: project page]
What happens: Hyperion computes the program's "behaviors", meaning what it does to its data and the full set of conditions under which each behavior happens. [KNOWN: project page and OSTI description, paraphrased]
What comes out: a behavior description that can be checked automatically against known malicious patterns, and read by experts to confirm the program does only what it should. [KNOWN: project page]
Where humans act: domain experts inspect the behaviors. [KNOWN: project page]
What it is not: probably not a sandbox that runs the program and watches it. The page says it looks "inside" an executable without source code but never says whether it runs it. [INFERRED: project page wording] (corrected in a fact-check pass, 2026-10-29) Whether it ever executes code is UNKNOWN.
Example: given an installer, it could report "under condition X, this writes to the startup folder". (Illustrative, not from a source.)
Unknown: the method in detail, the languages and CPU types it supports, and whether it's still developed.

## What it is (plain English, 2-4 sentences)
A cybersecurity research tool that analyzes executables to describe their behavior without source code. The same analysis is said to help check security properties and optimize programs. [KNOWN: project page; OSTI 1231925]

## How it works (plain English, no jargon without definition)
1. Input: a compiled program. [KNOWN]
2. Compute the behaviors and the conditions under which they occur. [KNOWN] How it does that is UNKNOWN from these pages. The approach sounds like static analysis, meaning analysis done by reading code rather than running it. [INFERRED from "without the use of the software's source code" and the absence of any mention of running it]
3. Check the behaviors against known malicious signatures automatically. [KNOWN]
4. Experts review the results. [KNOWN]

## How the project is organized
No public repo, so layout, languages, build, contributors and releases are all [UNKNOWN] (RULES 21). Searched: the OSTI record links field, GitHub search and the github.com/ORNL repo list (discovery/stub-search-2026-10-24.md).

## Timeline
| Date | Event | Source | Tag |
|---|---|---|---|
| 2014-09-01 | OSTI software record 1231925 | https://www.osti.gov/biblio/1231925 | [KNOWN] |

ORNL news stories about licenses to companies (2015 non-exclusive, 2017 exclusive) showed up in a search but were not refetched, so they're left out of the timeline. [UNKNOWN until fetched; discovery/stub-search-2026-10-24.md]

## Who uses it / why it matters
UNKNOWN from fetched pages. It matters as one of ORNL's older software-assurance tools, the kind used to check software before trusting it. [INFERRED from the project page's purpose]

## Related projects
Filled by the connections pass, matching connections/map.md.
| Related item | Relationship | Source | Tag |
|---|---|---|---|
| Cyber cluster (Cincinnatus, Heartbeat, CPAD, Situ) | related topic (ORNL cyber tools); map link 84 | OSTI 1231925 and the other OSTI records | [INFERRED] |
| [Cyberwheel](cyberwheel.md) | lineage checked, none found; map link 84 | deep-dives/cyberwheel | [UNRELATED] |

## What stands out
The public trail is thin for a tool that drew licensing interest: one project page, one 2014 software record, and no code. That fits a tool meant for licensing rather than open release. [INFERRED]

## Ten questions (GOAL.md)
1. Problem and audience: understanding untrusted binaries, for security analysts. [KNOWN]
2. Place in the tree: ORNL cybersecurity. The URL sits under a division projects path, but the division isn't named on the page. [KNOWN/UNKNOWN]
3. Who pays: USDOE per OSTI, program UNKNOWN.
4. Code: UNKNOWN.
5. Alive: UNKNOWN.
6. Outside users: UNKNOWN (license news not refetched).
7. Connections: UNKNOWN.
8. What it teaches: some ORNL security tools go out through licensing, not open source. [INFERRED]
9. Student path: no code to study. The topic (binary analysis) is learnable with open tools like Ghidra. [INFERRED]
10. Still unknown: method, users and current status. Searched without result: a public repo.

## Known / Inferred / Unknown
- KNOWN: what it's for and its inputs and outputs, from the project page and OSTI.
- INFERRED: that it works by static analysis, and that it was licensing-oriented.
- UNKNOWN: everything about the code, its users and its status.

## Verification notes
Filled by the fact-check pass.

## Sources (URL, title, accessed date, what it supports)
- https://www.ornl.gov/division/projects/hyperion, ORNL project page "Hyperion", accessed 2026-10-29, supports the purpose, inputs and outputs
- https://www.osti.gov/biblio/1231925, OSTI software record "Hyperion", accessed 2026-10-29, supports the date, ORNL and USDOE

## Quality gate
- [x] Every load-bearing claim has a source and a tag
- [x] Facts are kept apart from interpretation
- [x] ORNL relationship is not overstated, and maturity verbs match the source
- [x] Walkthrough, flow, timeline and unknowns are present
- [x] Ten questions answered or marked UNKNOWN
- [x] No copied text beyond short cited quotes; people by role only
- [ ] Two fact-check sweeps done
- [ ] INDEX, catalog, LAB-TREE and connections map updated

## Fact-check notes (2026-10-29)
- Re-read the ORNL project page and OSTI 1231925 (2014-09-01, ORNL, USDOE, software). The purpose, inputs, outputs, expert review and the security-check and optimization uses match both sources. They share the same wording, so the second source confirms rather than adds.
- Corrected: "not a sandbox" was tagged KNOWN but neither source says it; now INFERRED.
- License news dates are still left out: no primary source was fetched this pass.
- Related-projects table checked against connections/map.md and its sources; rows match. (Map links 69, 84 and 86 got factual updates; see verification/log.md.)

### Second pass (2026-10-29)
- Reread as a skeptic: the KNOWN claims match the ORNL page and OSTI word for word, so there's no independent third source; the "not a sandbox" fix is in place; license dates are still left out. No overclaiming found.
