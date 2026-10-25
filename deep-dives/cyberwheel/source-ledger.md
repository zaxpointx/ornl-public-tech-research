# Cyberwheel deep dive: source ledger
Written in the fact-check pass, checked 2026-10-24. Every public source this deep dive relies on, what it's used for, and whether I refetched it. All sources are public. Nothing here needed a login or a form.

| # | Source | Type, publisher, date | Used for | Refetched 2026-10-24 | Notes |
|---|---|---|---|---|---|
| S1 | https://github.com/ORNL/cyberwheel (GitHub API, README, code) | Public repo, ORNL org | License MIT, created 2024-07-08, first commit 2024-01-02, last commit 2025-08-26, Poetry install, Atomic Red Team in `red_agents/art_agent.py` and `red_actions/art_techniques.py` | yes | 55 stars, 12 forks, Python 99%, not archived |
| S2 | GitHub releases v1.1.0 (2025-03-10) and v2.0 (2025-08-11) | Release notes | "inactive blue agent" (v1.1.0), FIREWHEEL emulation (v2.0) | yes | v2.0 doesn't say "modified" |
| S3 | DOE CODE code-134699, DOI 10.11578/dc.20240715.1 | OSTI software record, 2024-07-16 | ORNL research org, LDRD sponsor | yes | Sponsor: "USDOE Laboratory Directed Research and Development (LDRD) Program". No contract or project number |
| S4 | OSTI 3025007, DOI 10.2172/3025007, https://www.osti.gov/servlets/purl/3025007 | ORNL LDRD "FY 2025 Completed Projects" report, 2026-03-31 | Project 11049 "Automating Cyber Defense Using Reinforcement Learning", results quotes, Firewheel "modified version", QEMU, "over 100,000 virtual nodes" | yes (PDF, p.13) | Single source for 11049 and the 100,000 figure |
| S5 | OSTI 2478356, DOI 10.1145/3675741.3675752 | CSET '24 workshop paper (ACM), 2024-08-13 per Crossref; OSTI date 2024-08-01 | Original Cyberwheel paper; results in simulation | yes | OSTI sponsor is just USDOE. No 11049 mention |
| S6 | Semantic Scholar citations API for DOI 10.1145/3675741.3675752 | Index, accessed 2026-10-24 | 33 citing papers; 4 abstracts name Cyberwheel | not refetched this pass | Counts depend on the index |
| S7 | arXiv 2610.00590 and arXiv 2610.00557 (2026-09-30) | Preprints | Run Cyberwheel (abstracts) | yes (earlier tonight) | Author affiliations not checked |
| S8 | DOI 10.3390/e27060622 | Entropy (MDPI), 2025-06-11 | Extends Cyberwheel (abstract) | yes (earlier tonight) | |
| S9 | DOI 10.1109/ISDFS65363.2025.11012027 | ISDFS 2025 (IEEE), 2025-04-24, "Comparing Traditional Hacking Tools and AI-Driven Alternatives" | Describes Cyberwheel only | metadata yes | Doesn't run it |
| S10 | DOE CODE code-163934, DOI 10.11578/dc.20250912.17 | Sandia FIREWHEEL software record, 2024-10-24 | Firewheel is Sandia's | yes | |
| S11 | OSTI 1373059 "Firewheel." | Sandia conference record, 2016-07-01, NNSA sponsor | Firewheel predecessor (INFERRED link) | yes | Same name and lab only |
| S12 | OSTI 3827147, DOI 10.2172/3827147 | ORNL LDRD supplementary report (OT pentesting with AI), 2026-09-01 | Possible adjacent work only | metadata yes | No source ties it to Cyberwheel. Stays INFERRED/adjacent |
| S13 | cyberwheel/emulator README in repo | Repo doc | "Firewheel uses QEMU/KVM to host virtual machines" | not refetched | Cited by lineage F8 |
