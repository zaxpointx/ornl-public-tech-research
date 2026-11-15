# Time-Based CAN IDS Benchmark

- Repo: https://github.com/pmoriano/can-time-based-ids-benchmark, pinned at `e0c862d6c6cbb0d60ed2572a90dd483a3253ed0f` (2022-01-18, the only commit history; no tags or releases) [KNOWN: accessed 2026-11-15]
- DOE CODE: https://www.osti.gov/doecode/biblio/69319. Site ownership is ORNL and the developer affiliation is ORNL; the research-organizations field is empty. DOI 10.11578/dc.20220112.2, released 2022-01-17 [KNOWN: record JSON export, re-fetched by the referee 2026-11-15]
- Paper: "Time-Based CAN Intrusion Detection Benchmark", AutoSec 2021 (NDSS workshop), https://arxiv.org/abs/2101.05781, ORNL author affiliations [KNOWN]
- Data it needs: ROAD, https://zenodo.org/records/10462796 (CC BY 4.0) [KNOWN]
- License: GPL-3.0 [KNOWN: LICENSE @ e0c862d]
- Status: active (public, not archived; no commits since 2022-01-18)

## Walkthrough
This is ORNL's code for comparing simple ways to spot attacks on a car's internal network by timing alone. [KNOWN: paper]
The problem: a car's computers talk over a CAN bus, where every module broadcasts short messages, many on a fixed rhythm. An attacker who injects extra messages changes that rhythm. [KNOWN: paper §I-II]
What goes in: the ROAD dataset of real CAN traffic from one vehicle on a dynamometer, with normal drives and labeled attack captures. [KNOWN]
What happens: for each message ID, the code learns the normal gap between messages. It then flags frames whose gaps look too short, using four rules: Mean, Binning, Gaussian and KDE. [KNOWN: code]
What comes out: precision-recall results per detector, the paper's Table II and Fig. 2. [KNOWN: notebook outputs]
Where humans act: someone downloads ROAD, runs the notebook and picks thresholds. [KNOWN: README]
What it is not: not a deployed product, and not a masquerade detector. The paper excludes masquerade attacks because they keep normal timing. [KNOWN: paper §II-A]
Example: an attacker injects one fake speed frame right after each real one, so gaps on that ID halve. Binning sums the last six gaps and alerts once they fall below 3.5 times the normal gap. [KNOWN: code; the illustration is ours]

## How the project is organized
It's one Jupyter notebook plus `code/helper_functions.py`. There are no tests, no CI, no pinned dependencies and no releases. The notebook's "with outliers" results load pickles that no cell produces. The full engineering reconstruction, with pinned line citations, is in [the deep dive](../deep-dives/can-time-ids/reconstruction.md). [KNOWN]

## What we measured
We re-implemented the detectors, checked them against the pinned helper code, and ran them locally on ROAD in [the lab](../atlas/labs/can-time-ids-road/README.md), with the referee's verdicts in [the verification log](../verification/log.md). [KNOWN: recorded experiment, 2026-11-15]
- **Published numbers reproduce exactly.** The Mean and Binning confusion matrices match the notebook cell for cell on two seeds. Gaussian is off by 14 false positives.
- **Masquerade is invisible to Mean and Binning.** Recall is 0 on all 13 masquerade captures. Gaussian picks up a weak signal where the injector runs about 14% slower than the real module (coolant, recall 0.83, precision 0.32 or lower).
- **The detection rule, not the distribution, explains most of the Gaussian gap.** Swapping in Mean's "3 of the last 6" rule raises Gaussian's F1 from 0.26 to 0.92.
- **Half the labeled attack frames are real frames.** Labels mark every frame of the target ID during the attack window. Relabeling by payload keeps exactly 50.00% of positives in every targeted log, and F1 at the published optima drops to about 0.65.

## Related projects
| Project | Relation | Tag |
|---|---|---|
| [CAN-D](can-d.md) | Same lab's CAN research area; CAN-D decodes signals, this benchmark detects timing attacks | [INFERRED: shared topic and division; no code link] |
| ROAD dataset (lead `road-can-dataset` in [leads](../discovery/leads.csv)) | Required input data | [KNOWN: README] |

## Known / Inferred / Unknown
- Known: as cited above and in the deep dive.
- Inferred: the paper's "1,821 alerts per minute" looks miscalculated against the notebook's 852 false positives (about 69 per minute).
- Unknown: the code for the Raspberry Pi OBD-II plug-in the paper describes; whether the labelling convention was deliberate; current maintenance.

## Sources
https://github.com/pmoriano/can-time-based-ids-benchmark, https://www.osti.gov/doecode/biblio/69319, https://arxiv.org/abs/2101.05781, https://arxiv.org/abs/2012.14600, https://zenodo.org/records/10462796 (all accessed 2026-11-15).
