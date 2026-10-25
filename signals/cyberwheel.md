# Signals: cyberwheel

## History, build targets, funding (discovery pass) (accessed 2026-10-24)
Public artifacts only (RULES 15-16). Contributor data is counts only. Source: a fresh clone of https://github.com/ORNL/cyberwheel plus the OSTI API, unless another source is given.

### What the outside tells us that the inside doesn't
- The project behaves like a funded, time-boxed study, not a maintained product. Commits run from 2024-01-02 to 2025-08-26 and then stop: zero commits in the last 12 months. The stop lines up with the FY2025 LDRD completed-projects report. [KNOWN: git history; INFERRED: the link to the LDRD end, medium confidence]
- It was never meant to be a package. pyproject.toml carries the classifier `Private :: Do not Upload`, which tells PyPI tooling to refuse uploads. [KNOWN: https://github.com/ORNL/cyberwheel/blob/main/pyproject.toml] So reuse means cloning, not `pip install`. [INFERRED, high confidence]
- No supercomputer target shows up anywhere. [KNOWN] The only GPU reference is an optional PyTorch `--device cuda` switch. [KNOWN: cyberwheel/runners/rl_handler.py, utils/parse_override_args.py] Words like "summit" or "aurora" match only inside bundled MITRE ATT&CK JSON. [KNOWN] The self-described "high fidelity" claim therefore rests on Firewheel emulation, not leadership-class compute. [INFERRED, high confidence]
- Outside attention has been light. The Wayback Machine's earliest capture of the repo page is 2024-10-01 and its latest is 2025-02-20. [KNOWN: archive.org availability API, see method note]

### Signal ledger
| Signal | What it suggests | Tag, source | Confidence |
|---|---|---|---|
| 352 commits on the default branch, 398 across all branches. 246 commits in 2024, 152 in 2025, none after 2025-08-26 | Activity ended rather than tapering off. The reading-pass 352 counts the default branch only | [KNOWN: `git rev-list --count HEAD` and `git log --all` on a clone, 2026-10-24] | high |
| 9 distinct author emails in total: 8 active in 2024, 5 in 2025, 1 new in 2025. 7 of the 9 use ornl.gov addresses | A small, stable in-house team with almost no outside contributors | [KNOWN: git log, counts only] | high |
| Top author made 26% of commits, top three made 69% | Work concentrated in a few people, so the project depends on a handful of contributors | [KNOWN: git log] | medium |
| Releases v1.0.0 2024-08-16, v1.1.0 2025-03-10, v2.0 2025-08-11. The last commit came 15 days after v2.0 | v2.0 reads as a wrap-up release | [KNOWN: git tags; INFERRED: wrap-up] | medium |
| No CI config (.github/workflows, GitLab CI, Jenkins or Travis are all absent) | Research-code practice, no automated testing in public | [KNOWN: repo tree at HEAD] | high |
| Sponsor fields: DOE CODE code-134699 says "USDOE Laboratory Directed Research and Development (LDRD) Program". OSTI 2478356 lists only "USDOE" | Funding is lab-internal LDRD, which matches link 56 | [KNOWN: OSTI API, 2026-10-24] | high |
| Job-posting search by project name found nothing | No public hiring tied to Cyberwheel, consistent with no follow-on build-out | [KNOWN: empty search, logged in not-found.md] | low (absence of evidence) |

### Out of scope / not recorded
- Nothing in this pilot pointed toward restricted work.
- Personal profile pages surfaced in searches were not used.

## Who actually uses it
Accessed 2026-10-24 (ET). Artifacts only; no people profiled beyond published author lists' institutions.

**Outside vs inside:** The inside frames Cyberwheel as a training ground for autonomous cyber defense agents (README), aimed at "live networks" someday (LDRD report, OSTI 3025007 p.13; the README does not use that phrase). From the outside, it is not packaged anywhere (no PyPI, conda-forge or Spack) and GitHub lists 0 dependent repos, so its visible users are researchers who clone it: 3 papers run or extend it, and their institutions are not yet checked.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| PyPI | No `cyberwheel` package (JSON API 404) | [KNOWN] | https://pypi.org/pypi/cyberwheel/json |
| Downloads | None to count (no PyPI package; pypistats 404) | [KNOWN] | https://pypistats.org/api/packages/cyberwheel/recent |
| conda-forge | No `cyberwheel-feedstock` (404) | [KNOWN] | https://github.com/conda-forge/cyberwheel-feedstock |
| Spack | No package.py under spack-packages builtin (404 for `cyberwheel`) | [KNOWN] | github.com/spack/spack-packages, repos/spack_repo/builtin/packages |
| GitHub "used by" | Dependents page reads "0 Repositories" | [KNOWN] | https://github.com/ORNL/cyberwheel/network/dependents |
| GitHub interest | 55 stars, 12 forks; last push 2025-08-26 | [KNOWN] (stars/forks are interest, not use) | GitHub API repos/ORNL/cyberwheel |
| GitHub code search for `import cyberwheel` | Not reachable without login | [UNKNOWN] | logged in not-found.md |
| Citations | Semantic Scholar 33 / OpenAlex 20 citing the CSET 2024 paper (DOI 10.1145/3675741.3675752); 4 name Cyberwheel | [KNOWN] | deep-dives/cyberwheel/synthesis.md; api.openalex.org |
| Actual use | arXiv 2610.00590 and 2610.00557 run it; Entropy 2025 (10.3390/e27060622) extends it ("is extended by adding new fine-grained defense mechanisms"); ISDFS 2025 only describes it | [KNOWN] | abstracts (checked); map.md link 108 |
| Who users are | Institutions of those 3 papers' authors | [UNKNOWN] | not checked |

Reasoning: no package + 0 dependents + recent use papers suggests a research artifact used by cloning, not a library others build on [INFERRED, medium confidence]. Claimed audience (autonomous defense for live networks, per OSTI 3025007 p.13) vs visible audience (academic RL-for-cyber researchers) [INFERRED].


## Sweep notes (fact-check pass, 2026-10-24)
- Re-fetched and verified: the `Private :: Do not Upload` classifier (pyproject.toml line 9), no CI config (.github/workflows, .gitlab-ci.yml, Jenkinsfile and .travis.yml all 404), tags v1.0.0 2024-08-16, v1.1.0 2025-03-10 and v2.0 2025-08-11, DOE CODE code-134699 (LDRD) and OSTI 2478356 ("USDOE" only).
- Not re-run: commit and author counts (the discovery-pass clone). Taken as reported. The rule 16 check is clean: no infrastructure, people or restricted-work content.
