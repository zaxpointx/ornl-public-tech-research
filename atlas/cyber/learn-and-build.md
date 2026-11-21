# What a cybersecurity student can learn and build from ORNL's public cyber work

Written for Cayden (17, cybersecurity student at TCAT, aiming at an ORNL internship). Independent research, not affiliated with ORNL. Last checked 2026-11-21.

## The short answer
You don't need ORNL's private code to practice ORNL-style work. Most of their public cyber projects boil down to ideas you can rebuild on your own gear: diff a system before and after, watch a CAN bus, make logs tamper-evident, authenticate messages, and attack your own toy model to make it stronger. **Pick two of the projects below, finish them, and write them up with sources the way this repo does.** That is the portfolio piece. [INFERRED: advice, based on the evidence below]

Ground rules for every project: your own machines, VMs or lab hardware only; no scanning or touching systems you don't own; no real vehicles you don't own; no malware.

## What ORNL's own job posts ask for (public posts, November 2026)
| Post | Skills named | Gate |
|---|---|---|
| AI Cyber Engineer, Emerging Cyber Technologies Research Group (req. 17230, 2026-11-04) | ML pipelines, evaluation and benchmarks, "file and network traffic analysis" | MS plus a DOE clearance [KNOWN] |
| Senior R&D Professional, Resilient Communications Group (req. 17427, 2026-11-10) | embedded Linux, Python, embedded C/C++, Git, software-defined radio, signal analysis, ML | BS plus 15 years, DOE clearance [KNOWN] |

**What this means for you:** full-time research jobs want a degree and a clearance, so the near-term door is student programs, and the AMIGO story shows a SULI undergraduate intern wrote code that ended up in a licensed product. [KNOWN: job posts; AMIGO story] The skills that show up across posts and projects are Linux, Python, packet and file analysis, embedded systems and Git. [KNOWN: posts; INFERRED: the pattern] Those are all things TCAT and home projects can build.

Sources: https://jobs.ornl.gov/job/Oak-Ridge-AI-Cyber-Engineer-TN-37830/1437296400/ ; https://jobs.ornl.gov/job/Oak-Ridge-Senior-R&D-Professional-Secure-and-Resilient-Communications-TN-37830/1449333600/ ; [AMIGO brief](briefs/amigo.md)

## Eight projects, easiest first

### 1. Linux persistence hunt with Systemd Snapshot (a weekend)
- **ORNL piece:** [Systemd Snapshot](briefs/systemd-snapshot.md), a pure-Python tool that maps systemd boot dependencies and can diff two snapshots.
- **Build:** spin up an Ubuntu VM, snapshot it, add a harmless test service of your own that starts at boot, snapshot again, run the `diff` action, and write up what changed and how a defender would spot it.
- **Learn:** systemd internals, persistence, forensic diffing (the same idea as [Akatosh](../../projects/akatosh.md)).
- **Watch out:** the repo has no license, so read and run it locally, but don't republish its code.

### 2. CAN bus intrusion detector on real data (one to two weeks)
- **ORNL pieces:** the [ROAD dataset](briefs/road-can-dataset.md) (CC BY 4.0), [CANRate](briefs/canrate.md), [SHIELD](briefs/shield-can.md)'s three detector types.
- **Build:** load ROAD captures in Python; write a timing detector (message gaps per CAN ID) and check it against the labeled fabrication and fuzzing captures; report precision and recall. Optional: replay traffic on Linux's virtual `vcan0` with `can-utils`, or on two Raspberry Pis with CAN boards and run CANRate.
- **Learn:** CAN basics, time series features, honest evaluation. This lines up with the most active ORNL cyber lane ([vehicle deep dive](deep-dives/vehicle-cyber.md)).

### 3. Authenticated MQTT messages with replay protection (a weekend)
- **ORNL piece:** the [QKD grid authentication](briefs/qkd-grid-authentication.md) paper, which tags each MQTT message with a one-time key, a timestamp and a key serial number.
- **Build:** the same scheme with ordinary pre-shared keys (HMAC or AES-GMAC from Python's `cryptography` package) between two Raspberry Pis or containers; show that a replayed or edited message gets rejected.
- **Learn:** MQTT, message authentication codes, nonces, replay attacks. No quantum hardware needed; the quantum part only changes where keys come from.

### 4. Tamper-evident settings log (one week)
- **ORNL piece:** [Cyber Grid Guard](briefs/cyber-grid-guard.md) checks device settings against a ledger.
- **Build:** a hash-chained log (each entry includes the hash of the previous one) of fake "device settings", copied to three machines; a checker that flags any edit and names what changed.
- **Learn:** integrity, hash chains, why redundancy matters. You don't need a blockchain platform to show the idea.

### 5. Run and extend Cyberwheel (ongoing)
- **ORNL piece:** [Cyberwheel](../../projects/cyberwheel.md), MIT-licensed RL cyber defense simulator; full write-up in [deep-dives/cyberwheel](../../deep-dives/cyberwheel/synthesis.md).
- **Build:** a longer training run, a new network layout, or a comparison of two defender settings, written up with charts.
- **Learn:** reinforcement learning, attack and defense modeling, reproducible experiments.

### 6. Labeled traffic for your own home lab (one week)
- **ORNL pieces:** [pcapmunger](briefs/orca.md) overlays attack captures onto background traffic; the [Data Driven User Emulator](briefs/data-driven-user-emulator.md) explains why background traffic must look human.
- **Build:** capture normal traffic in your own lab, overlay a capture of a port scan you ran against your own VM, and test whether Zeek or Suricata flags it.
- **Learn:** PCAP tooling (tcpdump, Wireshark tools), labeled datasets, IDS testing.

### 7. Mini "Photon" against your own toy model (one to two weeks)
- **ORNL piece:** [Photon](briefs/photon.md) turned a hyperparameter-search tool into an attack-search tool.
- **Build:** train a small image or tabular classifier, then use an off-the-shelf optimizer (Optuna, or DeepHyper itself) to search for the smallest input change that flips its answer; then retrain with those examples and measure the improvement.
- **Learn:** adversarial examples, search, robustness. Keep it to your own model; no jailbreaking real services.

### 8. Pull CVEs and product names out of advisories (one week)
- **ORNL piece:** [Stucco](briefs/stucco.md)'s entity extraction and its labeled corpus.
- **Build:** a small extractor (regex first, then a simple ML model) that finds CVE IDs, product names and versions in public advisories, stored as a tiny graph.
- **Learn:** threat intelligence basics, NLP, STIX-style modeling. Check each Stucco repo's license file before reusing anything.

## A note on where this happens
The 2021 paper on ORNL's AI/ML cyber range was presented at a conference held in Cookeville, Tennessee, home of Tennessee Tech. [KNOWN: [range brief](briefs/ai-ml-cyber-range.md)] Regional events like that are a realistic place to hear lab researchers talk about this work in public.
