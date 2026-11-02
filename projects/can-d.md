Short brief (RULES 21): built from an ORNL publication page and an OSTI software record; no public code.

# CAN-D (CAN Decoder)

- Official page: https://www.ornl.gov/publication/can-d-modular-four-step-pipeline-comprehensively-decoding-controller-area-network-data (IEEE Transactions on Vehicular Technology 70(10), Oct 2021, doi 10.1109/TVT.2021.3092354) [KNOWN: fetched 2026-10-29]
- OSTI: https://www.osti.gov/biblio/1822873 ("CAN-D: Controller Area Network Decoder Codebase", software, 2020-11-23, ORNL, USDOE) [KNOWN: OSTI API, accessed 2026-10-29]
- Repo / Docs: none public [KNOWN]
- License: UNKNOWN. An old ORNL licensing page for it now opens an unrelated page. [KNOWN: stub-search-2026-10-24.md]
- Status: unknown

## Walkthrough
CAN-D figures out what the raw messages inside a car mean. [KNOWN: paper abstract]
The problem: a car's computers talk over a CAN bus (Controller Area Network, a shared wire where every module broadcasts short messages). Carmakers keep secret which bits mean speed, RPM or brake pressure, and it differs by make, model and year. Without that map, researchers can't read the data. [KNOWN: abstract, paraphrased]
What goes in: logs of raw CAN traffic recorded from a vehicle. [KNOWN: OSTI]
What happens: a four-step pipeline finds each signal's boundaries (which bits, how many), its byte order (endianness), whether it's signed (how bits turn into a number), and, using standard diagnostic queries, what physical quantity some signals represent. [KNOWN: abstract]
What comes out: a .dbc file, the standard format that lists signal definitions, which can then translate that car's messages live or after a drive. [KNOWN: OSTI]
Where humans act: someone records the drive logs and uses the decoded data. [INFERRED]
What it is not: not an attack tool. The paper frames it as enabling security, privacy, tuning and diagnostic research. [KNOWN: abstract]
Example: a 2-byte field in message 0x1A0 rises when you accelerate. CAN-D works out that it's big-endian and unsigned, and diagnostic matching labels it as vehicle speed. (Illustrative.)
Unknown: whether the codebase was ever released or licensed.

## What it is (plain English, 2-4 sentences)
A research pipeline and codebase for reverse-engineering CAN signal definitions from raw logs. The paper says earlier methods ignored byte order and sign, and that handling them grows the problem from 128 to about 4.72×10²¹ possible ways to split a message, which they solve as an optimization problem. [KNOWN: abstract] It was evaluated on 10 vehicles and also put on lightweight hardware as an OBD-II plug-in for live decoding. [KNOWN: abstract]

## How it works (plain English, no jargon without definition)
1. Signal boundaries: classifiers guess where each signal starts and how long it is. [KNOWN]
2. Byte order: an optimization picks the best mix of boundaries and endianness. [KNOWN]
3. Signedness: a classifier decides signed versus unsigned (the paper reports an F-score above 97%). [KNOWN]
4. Meaning: diagnostic standards (OBD-II queries) label a subset of signals with physical units. [KNOWN]
Output: the .dbc file. [KNOWN: OSTI]

## How the project is organized
No public repo, so layout, languages, build, contributors and releases are all [UNKNOWN] (RULES 21). Searched: the OSTI record links field, GitHub search and the github.com/ORNL repo list (discovery/stub-search-2026-10-24.md).

## Timeline
| Date | Event | Source | Tag |
|---|---|---|---|
| 2020-11-23 | OSTI software record 1822873 | https://www.osti.gov/biblio/1822873 | [KNOWN] |
| 2021-10 | IEEE TVT paper | publication page | [KNOWN] |

## Who uses it / why it matters
UNKNOWN beyond the paper. It matters because you can't secure what you can't read. Decoding CAN is step one for car intrusion detection research. [INFERRED from the abstract's motivation]

## Related projects
Filled by the connections pass, matching connections/map.md.
| Related item | Relationship | Source | Tag |
|---|---|---|---|
| Akatosh, [Cyberwheel](cyberwheel.md) | related topic (ORNL cyber tools); map link 69 | OSTI 1822873 | [INFERRED] |
| [Cyberwheel](cyberwheel.md) | lineage checked, none found; map link 69 | deep-dives/cyberwheel | [UNRELATED] |

## What stands out
It's one of the most hands-on, student-relevant projects in the cyber set: a real reverse-engineering problem with a published method, even though the code isn't public. Open tools like SavvyCAN or cantools let you try the same idea on your own car's logs. [INFERRED; not tried]

## Ten questions (GOAL.md)
1. Problem and audience: unreadable car network data, for vehicle security and diagnostics researchers. [KNOWN]
2. Place in the tree: ORNL cybersecurity and vehicle research. The division isn't named on these pages. [UNKNOWN]
3. Who pays: USDOE per OSTI, program UNKNOWN.
4. Code: UNKNOWN.
5. Alive: last public sign is 2021. [KNOWN]
6. Outside users: UNKNOWN; citation counts not checked.
7. Connections: OBD-II and the .dbc format. [KNOWN]
8. What it teaches: ORNL registers code on OSTI even when it isn't released. [KNOWN]
9. Student path: read the paper, then record your own car's CAN with a cheap adapter and decode it with open tools. [INFERRED]
10. Still unknown: code release and licensing. Searched without result: a public repo; the licensing page is dead.

## Known / Inferred / Unknown
- KNOWN: method, evaluation scope, output format, the OSTI record and the paper.
- INFERRED: significance and the student path.
- UNKNOWN: code, license and users.

## Verification notes
Filled by the fact-check pass.

## Sources (URL, title, accessed date, what it supports)
- https://www.ornl.gov/publication/can-d-modular-four-step-pipeline-comprehensively-decoding-controller-area-network-data, ORNL publication page, accessed 2026-10-29, supports the method and evaluation
- https://www.osti.gov/biblio/1822873, OSTI "CAN-D: Controller Area Network Decoder Codebase", accessed 2026-10-29, supports the input/output and date

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
- Re-read the ORNL publication page (IEEE TVT 70(10), pp. 9685-9700, Oct 2021, DOI 10.1109/TVT.2021.3092354) and OSTI 1822873 (2020-11-23, ORNL, USDOE, software). Verified: the four steps, 128 growing to 4.72E21 tokenizations, signedness F-score above 97%, 10 vehicles, the OBD-II plug-in, and .dbc output used for real-time or post-drive translation. OSTI also mentions visualization methods.
- Older papers are still left out.
- Related-projects table checked against connections/map.md and its sources; rows match. (Map links 69, 84 and 86 got factual updates; see verification/log.md.)

### Second pass (2026-10-29)
- Re-verified via Crossref: IEEE TVT vol. 70, issue 10, pp. 9685-9700, October 2021. The F-score, 10 vehicles and 4.72E21 match the abstract. The only verbatim figure is a number, no copied prose. No issues found.
