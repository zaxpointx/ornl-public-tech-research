Short brief (RULES 21): built from an OSTI paper record and a DOE CODE software record; the ORNL code is closed.

# Signal Clustering Similarity CAN Masquerade Detector

- Official page: https://www.osti.gov/biblio/1866690 ("Detecting CAN Masquerade Attacks with Signal Clustering Similarity", AutoSec 2022 at NDSS; arXiv 2201.02665) [KNOWN: OSTI record, re-fetched by referee 2026-11-15]
- DOE CODE: https://www.osti.gov/doecode/biblio/134139 (research org ORNL, developer affiliation ORNL, project type closed source, no repository, release 2024-07-10) [KNOWN: DOE CODE API, referee re-fetch 2026-11-15]
- Repo / Docs: none public [KNOWN]
- License: closed source [KNOWN: DOE CODE]
- Status: unknown

## Walkthrough
This detector tries to tell whether a recorded car-network capture contains a masquerade attack, where an attacker silences a real message and sends forged ones at the same timing. [KNOWN: paper]
The problem: masquerades keep a message's normal timing, so timing-based detectors miss them. Our [timing IDS lab](../atlas/labs/can-time-ids-road/README.md) measured recall 0 on all 13 ROAD masquerades for two of ORNL's timing detectors. [KNOWN: lab]
What goes in: a whole capture translated into signal time series (speed, RPM and so on), resampled to 10 Hz. [KNOWN: paper §III]
What happens: the detector computes how every pair of signals correlates, clusters the signals into a tree (a dendrogram), and compares that tree against trees from known-benign captures using the CluSim element-centric similarity. If the new capture's similarities to benign captures are lower than benign captures' similarities to each other (Mann-Whitney test), it is flagged. [KNOWN: paper §III]
What comes out: a per-capture verdict. DOE CODE describes the closed code as giving a probability score. [KNOWN: DOE CODE description; meaning of the score UNKNOWN]
Where humans act: someone chooses the benign baseline captures and reviews flagged captures. [INFERRED]
What it is not: not a real-time per-message detector. It works on whole files after the fact. [KNOWN: paper, Fig. 3 caption]
Example: a forged speedometer stream no longer moves with wheel speed, so the speed signals land in different clusters than in benign drives. (Illustrative.)
Unknown: which signals the paper kept, how it handled slow IDs, and how the closed 2024 code differs from the paper.

## What it is (plain English, 2-4 sentences)
A forensic detector for CAN masquerade attacks that looks at how a vehicle's signals move together rather than when messages arrive. The paper reports, on the public ROAD dataset, Ward-linkage significance for all five masquerade categories and F1 of about 90-94% in a 220-fold evaluation. [KNOWN: paper Tables II-III]

## How it works (plain English, no jargon without definition)
See the [artifact study](../deep-dives/can-signal-clustering/artifact-study.md) for the full spec with page citations and the ten places the paper is ambiguous (A1-A10). [KNOWN for stated steps; INFERRED for the choices marked there]

## How the project is organized
Closed code, so layout, languages, build, contributors and releases are [UNKNOWN] (RULES 21). A later public ORNL repository, `pmoriano/benchmarking-unsupervised-online-IDS-masquerade-attacks` (DOE CODE 141444, MIT), contains a windowed variant; it was read, not run (artifact study).

## Timeline
| Date | Event | Source | Tag |
|---|---|---|---|
| 2022-01 | arXiv 2201.02665 v1 | arXiv | [KNOWN] |
| 2022 | AutoSec 2022 paper (OSTI 1866690) | OSTI | [KNOWN] |
| 2024-07-10 | DOE CODE 134139 closed-source record | DOE CODE | [KNOWN] |
| 2026-11-15 | Independent rebuild on ROAD does not reproduce Tables II-III | [lab](../atlas/labs/can-signal-clustering-rebuild/README.md) | [KNOWN: recorded experiment] |

## Who uses it / why it matters
UNKNOWN beyond the paper and its later ORNL follow-ups. It matters as a rare published idea aimed at masquerades, the attack type timing detectors cannot see. [INFERRED]

## Related projects
| Related item | Relationship | Source | Tag |
|---|---|---|---|
| [Time-Based CAN IDS Benchmark](can-time-ids-benchmark.md) | same ROAD data; this method targets its measured blind spot | both labs | [KNOWN] |
| [CAN-D](can-d.md) | paper says the work leverages CAN-D signal translation | paper p.1 §I | [KNOWN] |
| ROAD dataset (lead `road-can-dataset`) | evaluation data | paper §III-C | [KNOWN] |

## What stands out
Our independent rebuild, on ROAD's released signal files, did not reproduce the paper: Ward significant in 0 of 5 categories, 1 of 13 masquerades flagged, and clean short benign crops flagged more often than real attacks. That points at capture length and driving regime as a confound, though the closed code may make choices the paper doesn't state. [KNOWN: recorded experiment; cause INFERRED]

## Ten questions (GOAL.md)
1. Problem and audience: masquerade attacks on vehicle networks, for automotive security researchers. [KNOWN]
2. Place in the tree: ORNL cyber and vehicle security research; division not stated in these records. [UNKNOWN]
3. Who pays: USDOE per DOE CODE; program UNKNOWN.
4. Code: closed; method public. [KNOWN]
5. Alive: 2024 DOE CODE record and a 2024 public windowed follow-up. [KNOWN]
6. Outside users: UNKNOWN; citations not checked.
7. Connections: CAN-D, ROAD, the timing benchmark. [KNOWN]
8. What it teaches about ORNL: closed code with an open paper and a later open variant is one way ORNL releases cyber work. [INFERRED]
9. Student angle: the whole pipeline can be rebuilt from public pieces (ROAD, CluSim, scipy), as the lab shows. [KNOWN]
10. Unknown: the closed code's choices and inputs; whether it reproduces its own tables on ROAD's released files.

## Sources (accessed 2026-11-15)
- https://www.osti.gov/biblio/1866690 and https://www.osti.gov/servlets/purl/1866690
- https://arxiv.org/abs/2201.02665
- https://www.osti.gov/doecodeapi/services/search/134139
- https://zenodo.org/records/10462796
- verification/log.md, referee sections dated 2026-11-15
