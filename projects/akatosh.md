Short brief (RULES 21): built from an ORNL news story and an OSTI software record; no public code.

# Akatosh

- Official page: https://www.ornl.gov/news/ornl-researchers-enable-real-time-forensic-analysis-new-cybersecurity-tool (ORNL news, 2018-08-28) [KNOWN: fetched 2026-10-29]
- OSTI: https://www.osti.gov/biblio/1419663 ("Akatosh: Automated Cyber Incident Verification and Impact Analysis", 2016-10-06, ORNL, USDOE) [KNOWN: OSTI API, accessed 2026-10-29]
- Repo / Docs: none public [KNOWN]
- License: UNKNOWN
- Status: unknown

## Walkthrough
Akatosh helps security teams tell a real break-in from a false alarm. [KNOWN: news story]
The problem: an intrusion detection system (IDS), software that watches a network and raises alerts on odd activity, throws off thousands of alerts a day, and many are false. Analysts waste hours checking machines by hand. [KNOWN: news story]
What goes in: IDS alerts, plus regular snapshots of each computer's state. [KNOWN: news story]
What happens: Akatosh snapshots computers during normal work to get a baseline. When an alert fires, it takes another snapshot and compares the two. [KNOWN: news story]
What comes out: a summary of what changed around the alert, such as files copied or passwords pulled, sent to the administrator. [KNOWN: news story]
Where humans act: the analyst or admin reads the report and decides if it's real. [KNOWN]
What it is not: not an IDS itself. It works alongside existing ones. [KNOWN: news story; OSTI]
Example: an alert fires on a laptop. Akatosh's comparison shows a new process reading the password store right before the alert, so the analyst knows it's real. (Built from the story's examples, not a real incident.)
Unknown: what a snapshot contains technically, which operating systems it supports, and whether it was ever licensed.

## What it is (plain English, 2-4 sentences)
A system that combines IDS alerts with automated forensic analysis (examining a computer's state for evidence) to cut false positives and point responders at the root cause. It can also look back at any earlier state of a machine and compare states. [KNOWN: OSTI 1419663, paraphrased]

## How it works (plain English, no jargon without definition)
1. Baseline: periodic snapshots of hosts during normal operation. [KNOWN: news]
2. Trigger: an IDS alert. [KNOWN]
3. Compare: a new snapshot versus the baseline to show what changed leading up to and during the event. [KNOWN]
4. Report: a summary of relevant changes to the administrator. [KNOWN]

## How the project is organized
No public repo, so layout, languages, build, contributors and releases are all [UNKNOWN] (RULES 21). Searched: the OSTI record links field, GitHub search and the github.com/ORNL repo list (discovery/stub-search-2026-10-24.md).

## Timeline
| Date | Event | Source | Tag |
|---|---|---|---|
| 2015 | work began (per the story, from an internship) | news story | [KNOWN] |
| 2016-10-06 | OSTI software record 1419663 | https://www.osti.gov/biblio/1419663 | [KNOWN] |
| 2018 | selected for DHS S&T's Transition to Practice (TTP) program, 5th cohort; demoed at RSA and TTP Demo Days | news story | [KNOWN] |
| 2018-08-28 | news story; "several companies" interested in licensing | news story | [KNOWN] |

A demo paper at ACM CCS 2017 showed up in a search but wasn't refetched. [UNKNOWN until fetched]

## Who uses it / why it matters
UNKNOWN beyond the 2018 licensing interest. [KNOWN: news] Alert fatigue is one of the biggest day-to-day problems in a security operations center, so it targets a real pain point. [INFERRED from the story]

## Related projects
Filled by the connections pass, matching connections/map.md.
| Related item | Relationship | Source | Tag |
|---|---|---|---|
| CAN-D, [Cyberwheel](cyberwheel.md) | related topic (ORNL cyber tools); map link 69 | OSTI 1419663 | [INFERRED] |
| [Cyberwheel](cyberwheel.md) | lineage checked, none found; map link 69 | deep-dives/cyberwheel | [UNRELATED] |

## What stands out
For a cyber student this is a very readable idea: "diff the machine before and after the alert." It also shows DHS TTP as a route ORNL security tools take toward commercial use. [KNOWN fact; the framing is interpretation]

## Ten questions (GOAL.md)
1. Problem and audience: IDS false alarms, for SOC analysts and IT teams. [KNOWN]
2. Place in the tree: the story places it in a cyber and information security research group within computing sciences in 2017-18. [KNOWN: news]
3. Who pays: USDOE per OSTI; TTP is a DHS program. [KNOWN] Specific funding is UNKNOWN.
4. Code: UNKNOWN.
5. Alive: last public sign is 2018. [KNOWN]
6. Outside users: UNKNOWN.
7. Connections: works with existing IDS tools. [KNOWN]
8. What it teaches: interns can start projects that become lab tools. [KNOWN for this case]
9. Student path: the idea can be rebuilt with open tools such as osquery snapshots plus Suricata alerts, on your own lab machines. [INFERRED]
10. Still unknown: snapshot contents, licensing outcome and status. Searched without result: a public repo.

## Known / Inferred / Unknown
- KNOWN: purpose, method outline, the OSTI record and the TTP selection.
- INFERRED: the significance and the student rebuild idea.
- UNKNOWN: code, licensing outcome and current status.

## Verification notes
Filled by the fact-check pass.

## Sources (URL, title, accessed date, what it supports)
- https://www.ornl.gov/news/ornl-researchers-enable-real-time-forensic-analysis-new-cybersecurity-tool, ORNL news, 2018-08-28, accessed 2026-10-29, supports the method, TTP and the timeline
- https://www.osti.gov/biblio/1419663, OSTI "Akatosh", accessed 2026-10-29, supports the date, ORNL and description

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
- Re-read the 2018-08-28 ORNL story and OSTI 1419663 (2016-10-06, ORNL, USDOE, software). Verified: IDS pairing, the snapshot baseline and compare method, the report to administrators, examples of files copied and passwords extracted, work starting with a 2015 internship, the research group in 2017, the DHS S&T TTP fifth cohort, demos at RSA and TTP Demo Days, and "several companies" interested in licensing. The OSTI description adds near-real-time analysis and looking back at earlier states, as the brief says.
- Older papers are still left out: no primary source was fetched.
- Related-projects table checked against connections/map.md and its sources; rows match. (Map links 69, 84 and 86 got factual updates; see verification/log.md.)

### Second pass (2026-10-29)
- Reread: TTP fifth cohort, RSA and Demo Days, and licensing interest all come from one ORNL story, with no independent source found this pass, so they stay KNOWN, not CORROBORATED. The example stays labelled illustrative. No issues found.
