# OLCF test harness: does activity line up with new machine launches? (discovery pass, accessed 2026-10-24)

Short answer: yes, roughly. Each burst of work lands in the run-up to a new supercomputer or right after one opens. That's a timing match drawn from commit dates and subjects. No public source states the plan. [INFERRED, medium]

## Machine timeline (public sources)
- Summit debuted in June 2018 and was decommissioned in November 2024. Frontier debuted in May 2022 as the first exascale machine and opened to full user operations in April 2023. [KNOWN: [OLCF overview](https://www.olcf.ornl.gov/about-olcf/overview/), [ORNL news 2023-06-28](https://www.ornl.gov/news/exascale-blastoff-early-users-helped-launch-frontier-success/)]
- DOE opened bids for Frontier's successor, Discovery, in July 2024, with delivery targeted for 2027 or early 2028. [KNOWN: [OLCF 2024-07-19](https://www.olcf.ornl.gov/2024/07/19/doe-opens-bids-to-construct-ornls-next-generation-supercomputer/)]

## What the commits show (dates and subject lines only, all branches)
- Commits per year: 2015:21, 2016:213, 2017:146, 2018:6, 2019:17, 2020:37, 2021:29, 2022:121, 2023:105, 2024:81, 2025:203, 2026:79. [KNOWN: git log]
- **2016 to 2017, the Summit run-up.** This is the biggest early burst (96 commits in September 2016), and the following month brought "Adding support for summitdev" (2016-10-13), Summit's early test system. Titan, the machine of the day, shows up in 2016 subjects, and Summit shows up from 2017 to 2021. Activity nearly stops in 2018, the year Summit launched. [KNOWN: git log] Read: the harness was built up before Summit arrived, then went quiet once it was running. [INFERRED, medium]
- **2022 to 2023, the Frontier years.** Commits came back to 121 and 105. The 2022 work adds automatic timing metrics and support for the Slurm job scheduler. [KNOWN: commit subjects] The brief says the docs cover both Slurm and LSF, the older scheduler. [KNOWN: signals/olcf-test-harness.md] Read: retooling for Frontier. [INFERRED, medium]
- **2025, the busiest year since 2016.** 203 commits from two people by commit name (the 9 to 10 count comes from distinct email addresses, which overcount), and the v3.0 release on 2025-03-31. The work centers on sending test results and machine health into streaming metrics databases. [KNOWN: git log, tags] This comes right after Summit was retired and DOE asked for Discovery bids. [KNOWN dates] Whether it's tied to Discovery is [UNKNOWN]. A general push for better monitoring is just as likely. [INFERRED, low]
- Only one commit subject names Frontier (2026-10). Machine names live in config files more than in commit messages, so name counts undercount. [KNOWN; INFERRED about why]
- I didn't read machine configs, node details or any system layout (rule 16).

## Funding
- code-153320 (v3.1, 2025-07-28) lists only the DOE Office of Science as sponsor. [KNOWN: OSTI API records/code-153320] ASCR, the Office of Science's computing program that pays for OLCF, is named on 3 of the 4 other OSTI hits. [KNOWN: signals/olcf-test-harness.md] No separate machine-launch money is visible. [UNKNOWN]

## Ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| Summit | Debut 2018-06, retired 2024-11 | OLCF overview | [KNOWN] |
| Frontier | Debut 2022-05, full ops 2023-04 | ORNL news | [KNOWN] |
| Discovery | Bids opened 2024-07, delivery 2027 or early 2028 | OLCF news | [KNOWN] |
| Burst 1 | 2016:213, 2017:146; summitdev support 2016-10 | git log | [KNOWN] |
| Lull | 2018:6 | git log | [KNOWN] |
| Burst 2 | 2022:121, 2023:105; Slurm and metrics work | git log | [KNOWN] |
| Burst 3 | 2025:203; v3.0 2025-03-31; metrics streaming | git log, tags | [KNOWN] |
| Tags | v2.1 2021-02-24, v3.0 2025-03-31, v3.1 2025-07-28, v3.2 2026-09-10 | git | [KNOWN] |
| Cause | Not stated publicly | | [UNKNOWN] |

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Verified against a fresh clone: per-year commits, 96 commits in September 2016, the 2018 lull, all four tags and dates, and the 2026-10 Frontier mention.
- Corrected: summitdev support landed 2016-10-13, a month after the September burst; 2025's work came from two people by commit name (email counts give 9 to 10); code-153320's sponsor field says Office of Science, not ASCR, which appears on the other OSTI hits.
