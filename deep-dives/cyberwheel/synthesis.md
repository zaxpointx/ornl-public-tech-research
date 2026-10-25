# Cyberwheel deep dive: executive synthesis
Owner: ORNL Reader. Written 2026-10-24. Sources are public only. Fact Checker owns the ledgers and verification report in this folder.

## The answer in one paragraph
Cyberwheel is an ORNL research test bed for training AI network defenders with reinforcement learning (RL). An agent learns by trial and error from a reward score. Cyberwheel was built as the test bed for ORNL LDRD project 11049 (LDRD is lab-directed, in-house research funding [INFERRED: the source doesn't say "internal"]), "Automating Cyber Defense Using Reinforcement Learning". [KNOWN: OSTI 3025007, p. 13] It first simulates a network quickly from config files. From v2.0 (August 2025) it can also replay trained agents inside an emulated network of real virtual machines, using a modified version of Sandia's Firewheel. [KNOWN: v2.0 release notes; OSTI 3025007 p. 13] The project's own report says it showed agents could "autonomously deploy decoys in unseen network topologies that delay or deny adversarial actors", and that agents trained in simulation could be moved to emulation. [KNOWN: OSTI 3025007 p. 13, quote under 25 words] It's a research environment. No public source calls it deployed or production. [KNOWN: searched the README, release notes, DOE CODE and LDRD text; Fact Checker should log the negative in not-found.md]

## Well understood
- **Purpose and design:** red (attacker) and blue (defender) agents, decoys, detectors, rewards, a Gym interface, YAML configs. [KNOWN: README, repo tree, v1.1.0 notes]
- **Funding and institution:** ORNL LDRD Director's R&D Program, AI area. ORNL is the research org on DOE CODE code-134699 and on OSTI 2478356. [CORROBORATED: OSTI 3025007 plus the DOE CODE sponsor field "USDOE Laboratory Directed Research and Development (LDRD) Program"]
- **Timeline of releases** and of activity. See timeline.md.
- **Code-level flow** of a training step. See system-flow.md.

## Inferred
- **Dormancy:** active development likely stopped once the LDRD project finished. The last commit is 2025-08-26, and the project appears in the FY2025 completed list. [INFERRED: dates line up; no statement found]
- **Lineage:** "ART" in the code means Atomic Red Team, a public library of attack technique tests. The code docstrings name it, so this is KNOWN for the code. What upstream ART version it tracks is UNKNOWN.

## Unknown
- The owning division or group. No public source names it.
- Whether anyone outside the team uses it.
- Whether a follow-on project exists.
- The v1.0.0 tag date. The tag has no release object.

## Outside use (Connector's question, checked 2026-10-24)
Semantic Scholar lists 33 papers citing the 2024 ACM paper (DOI 10.1145/3675741.3675752). That's more than the 20 Connector saw, probably because the indexes differ. [KNOWN: https://api.semanticscholar.org/graph/v1/paper/DOI:10.1145/3675741.3675752/citations] Only 4 of the 33 abstracts name Cyberwheel. Only 3 of them say they actually run it:
- "Towards Hierarchical Cyber Defense with Large Language Models" (arXiv 2610.00590) runs its defenders "Using the high fidelity Cyberwheel environment". [KNOWN: abstract]
- "No One Architecture Fits All" (arXiv 2610.00557) tests red-team agents "in CybORG CAGE-4 and in Cyberwheel at two network scales". [KNOWN: abstract]
- An *Entropy* 2025 paper on graph embedding for autonomous cyber defense (DOI 10.3390/e27060622) says Cyberwheel "is extended by adding new fine-grained defense mechanisms". [KNOWN: abstract]
- An ISDFS 2025 paper (DOI 10.1109/ISDFS65363.2025.11012027) only describes Cyberwheel next to MITRE Caldera. It doesn't run it. [KNOWN: abstract]

So there is outside research use of Cyberwheel. Whether these authors are outside ORNL is [UNKNOWN], because the author lookup was rate-limited and the full papers weren't read. The other 29 citing abstracts don't name Cyberwheel. Some may still use it in the body. [UNKNOWN] This changes the earlier "named users: UNKNOWN". There are now three abstract-level research uses, and none is a deployment.

## Dependency files (Connector's question)
`pyproject.toml` plus `poetry.lock` is the authoritative dependency set. The README's install steps run `poetry install`, and it calls `requirements.txt` an optional fallback "If running into issues with poetry". [KNOWN: README lines 117-145] The two files disagree. pyproject asks for gymnasium ^1.1.0, ray ^2.43.0 and stable-baselines3 ^2.5.0, while requirements.txt pins gymnasium 0.28.1, ray 2.10.0 and SB3 2.2.1. [KNOWN: both files] That looks like requirements.txt was exported from an older lock and never regenerated. [INFERRED]

## Would more public research change the core answer?
Probably not. The purpose, funding, design and results all come from primary sources that agree. More reading could add the two papers' detailed experiment numbers (the ACM paper is behind a 403 for us, so its OSTI record is the route), any FY2026 follow-on LDRD, and Connector's Firewheel lineage. None of those would change what Cyberwheel is. [INFERRED]

## Maturity words, as written by the sources (rule 10)
- v1.1.0: RL red agent "trained and tested on an inactive blue agent". [KNOWN: release notes]
- LDRD: "developed", "showed", "study". [KNOWN: OSTI 3025007 p. 13]
- None of the sources say "deployed" or "production".

## Fact-check notes (ORNL Fact Checker, 2026-10-24)
- Verified both p. 13 quotes against the OSTI 3025007 PDF (https://www.osti.gov/servlets/purl/3025007), word for word: "autonomously deploy decoys in unseen network topologies that delay or deny adversarial actors" and "a modified version of the Firewheel test bed".
- Funding nuance: "LDRD-funded" is CORROBORATED (report p. 13 plus the DOE CODE code-134699 sponsor field "USDOE Laboratory Directed Research and Development (LDRD) Program"). The project number 11049 rests only on the report, so it's KNOWN from a single source. Neither code-134699 nor OSTI 2478356 carries a project number or contract number.
- "Built for ORNL's internal LDRD project": the report says agents were "trained in a custom-built, realistic network test bed environment called Cyberwheel". "Internal" is not in the source; LDRD is lab-directed by definition, so it's acceptable but INFERRED.
- What "modified" means in Firewheel is not stated anywhere on p. 13. The report gives only "modified version" plus "built on QEMU" and "over 100,000 virtual nodes". Connector's reading (Cyberwheel's own components, not a fork) stays INFERRED.
