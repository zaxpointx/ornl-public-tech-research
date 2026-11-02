# SNS neutron pipeline: does the revival line up with facility events? (discovery pass, accessed 2026-10-24)

Short answer: partly. The 2020 to 2022 restart looks like a software cleanup, not a facility event. The 2023 to 2024 bursts land inside and right after the SNS Proton Power Upgrade outage. That timing match is a correlation only. Nothing public says one caused the other. [INFERRED, low to medium]

## Facility timeline (public sources)
- The Proton Power Upgrade's long installation outage ran from August 2023 to April 2024. Beam commissioning started on 2024-06-07, and the user program resumed on 2024-07-11 at 1.7 MW. [KNOWN: [PPU completion paper, LINAC2024](https://doi.org/10.18429/jacow-linac2024-thpb045)]
- The final key performance goal was met by November 2024. [KNOWN: [ORNL news, 2024-11-07](https://www.ornl.gov/news/spallation-neutron-source-achieves-another-major-milestone/)]
- Beam power reached 1.9 MW in October 2025, with 2 MW planned for May 2026. [UNVERIFIED on recheck: the cited sns.gov/sts/timeline address now redirects to the general neutron facilities home page, which no longer shows these figures; the 2024 ORNL news item only says power would ramp to 2.0 MW "over the next two years"] (corrected in a fact-check pass, 2026-10-29)
- Funding: the PPU paper credits the DOE Office of Science, Basic Energy Sciences, Scientific User Facilities. That's the same program on the Mantid and ONCat OSTI records. [KNOWN] The three plumbing repos still have no funding record of their own. [UNKNOWN]

## What the commits show (commit subjects and dates only, read from the public repos)
- **2020 to 2022 restart = modernization.** data-workflow was moved to Docker in October 2020 and got GitHub Actions and tests. post-processing-agent switched to Python 3 in February 2021 and gained unit tests in September 2021. live-data-server was containerized in March 2022. [KNOWN: git log] Python 2 reached end of life in January 2020, which fits a catch-up wave. [INFERRED, medium]
- **During the outage.** post-processing-agent's biggest burst came while the beam was off: 28 commits in November 2023, 68 in December and 38 in January 2024. [KNOWN] Read: downtime may have been used for software work. [INFERRED, low]
- **Beam coming back.** live-data-server went from near zero to 28 commits in June 2024, 11 in July and 53 in August. data-workflow climbed through mid-2024 to a September peak of 33. [KNOWN] Read: the live data and monitoring side got attention as operations restarted at higher power. [INFERRED, low to medium]
- I didn't read deployment or secrets configuration, hosts or anything about internal systems (rule 16).

## Ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| PPU outage | 2023-08 to 2024-04 | LINAC2024 paper | [KNOWN] |
| Beam back | Commissioning 2024-06-07, users 2024-07-11 | LINAC2024 paper | [KNOWN] |
| Modernization commits | Docker 2020-10 (data-workflow), Python 3 2021-02 (post-processing-agent), containers 2022-03 (live-data-server) | git log | [KNOWN] |
| post-processing-agent burst | 2023-11:28, 2023-12:68, 2024-01:38 | git log, all branches, author dates | [KNOWN] |
| live-data-server burst | 2024-06:28, 2024-07:11, 2024-08:53 | git log, all branches, author dates | [KNOWN] |
| data-workflow 2024 | Peak 2024-09:33 | git log, all branches, author dates | [KNOWN] |
| Causal link | Not stated anywhere public | | [UNKNOWN] |

## Fact-check notes (2026-10-29)
First fact-check pass. Commit counts re-read from a fresh clone of each of the three public repos; facility facts re-read from the public pages.
- Verified: PPU paper DOI resolves; ORNL news 2024-11-07 confirms the final key performance parameter, hardware finished in April, commissioning in June and operations in July 2024; Docker move in data-workflow 2020-10-26; post-processing-agent "Use python3" 2021-02-22 and unit tests 2021-09; live-data-server containerization 2022-03-02.
- Commit spot checks (Rule 17): all monthly counts in the ledger match by author date on all branches. By committer date a few shift: post-processing-agent 2023-12 is 64 and 2024-01 is 42; data-workflow 2024-09 is 34. On the default branch only, live-data-server 2024-07 is 10, not 11. The ledger now names the date type.
- Corrected: the 1.9 MW / 2 MW line could not be re-verified because its source address now lands on a different page; tag lowered and explained. No other source was guessed at (Rule 16).
- The causal link stays UNKNOWN and the correlation reading stays INFERRED.
- Nothing restricted; no deployment or host details read.

### Second pass (2026-10-29)
Skeptical reread of the riskiest claims against sources not leaned on in the first pass.
- PPU dates: the LINAC2024 DOI resolves and ORNL news confirms the June/July 2024 restart. Verified.
- live-data-server 2024 counts: same by author and committer date (28, 11, 53). Verified.
- The causal claim stays UNKNOWN and the 1.9 MW line stays unverified; no other address was tried. Verified as tagged.
- No corrections.
