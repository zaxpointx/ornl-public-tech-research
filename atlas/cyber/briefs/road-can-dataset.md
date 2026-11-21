Short brief: public dataset. Independent research, not affiliated with ORNL. People by role only. Last checked: 2026-11-21.

# ROAD (Real ORNL Automotive Dynamometer) CAN intrusion dataset

- Dataset: https://zenodo.org/records/10462796 [1]
- Paper preprint: https://arxiv.org/abs/2012.14600 [2]
- License: CC BY 4.0 [KNOWN: Zenodo API, 1]
- Status: active as a dataset: Zenodo shows 7,279 downloads (3,255 unique) as of the access date. [KNOWN: Zenodo API]
- ORNL relationship (RULES 13): KNOWN: the Zenodo record's title names ORNL and its first creator is listed under Oak Ridge National Laboratory [1].
- Years visible in public sources: 2020 (v1) to 2024 (record update)

## Walkthrough (plain language)
- **What it is:** More than 3.5 hours of real CAN traffic from one vehicle on a dynamometer, including labeled attacks, published so researchers can test CAN intrusion detectors on real data. [KNOWN: 1]
- **The problem:** Many CAN IDS studies used synthetic or private data, so results couldn't be compared. [INFERRED from 1, 2]
- **What goes in:** n/a (it is data). It holds ambient driving plus fuzzing, fabrication, advanced attacks and simulated masquerade attacks. [KNOWN: 1]
- **What happens:** Provided as raw CAN logs and, for many captures, as decoded signal time series. [KNOWN: 1]
- **What comes out:** A benchmark anyone can download. [KNOWN: 1]
- **Where humans act:** Researchers train and test detectors. [KNOWN]
- **What it is not:** Not code. [KNOWN]
- **Example:** Train a timing-based detector on ambient captures and check whether it flags the fabrication captures. (Illustrative.)
- **Unknown:** The vehicle model (not identified in the material we read).

## How it works
1. Download, unzip, and parse candump logs or signal CSV files. [INFERRED from 1]

## Outside-in signals
- Thousands of downloads make this the most-used public ORNL cyber artifact we found, by raw counts. [KNOWN: numbers; INFERRED: ranking, since most artifacts have no comparable counter]
- An unmerged branch of this repository already reproduces a timing-based CAN IDS on ROAD (branch `claude/research-team`). It is not part of main, so it is mentioned, not linked.

## What stands out (interpretation)
This is the dataset to start with for any CAN project on a laptop.

## Related
- [CAN-D](../../../projects/can-d.md): signal translation of the kind used for the decoded series. [INFERRED from overlapping credited authors on the Zenodo and CAN-D OSTI records; authorship proves participation only]

## Known / Inferred / Unknown
- KNOWN: Contents, license, downloads.
- INFERRED: Ranking.
- UNKNOWN: Vehicle identity.

## Sources (accessed 2026-11-21 unless noted)
1. https://zenodo.org/records/10462796 (Zenodo record via API); supports: contents, license, stats
2. https://arxiv.org/abs/2012.14600 (arXiv preprint); supports: citation, not re-read

## Verification
Sweep 1 done on 2026-11-21: each load-bearing source above was fetched that day unless it is marked as seen in a search result. Sweep 2 (an independent re-read) has not been done, so this brief is not yet promoted to `discovery/catalog.csv`. See the [cyber atlas verification notes](../verification.md).
