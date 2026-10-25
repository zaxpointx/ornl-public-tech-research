# Signals: hydragnn

## History, build targets, funding (discovery pass) (accessed 2026-10-24)
Public artifacts only (RULES 15-16). Contributor data is counts only. Source: a fresh clone of https://github.com/ORNL/HydraGNN plus the OSTI API, unless another source is given.

### What the outside tells us that the inside doesn't
- **It's expanding from materials into the power grid.** Two OSTI datasets are "HydraGNN_OPF_GFM_2026 - Ensemble of predictive graph foundation models for power grid appl[ications]". OSTI 3377970 (2026-07-01) lists DOE's Office of Electricity (OE) as a sponsor, alongside ASCR. OSTI 3239722 is dated 2026-07-14. [KNOWN: osti.gov/biblio/3377970, /3239722] The repo's `examples/opf`, `opflearn` and `pglearn` folders (OPF is optimal power flow) first appeared on 2026-09-24. [KNOWN: git log] The brief and README frame HydraGNN as materials and molecules. The outside shows a new grid line with its own funder. [INFERRED, high confidence]
- **The origin date disagrees.** An ornl.gov news story says the team "started developing HydraGNN" in 2022. [KNOWN: https://www.ornl.gov/news/lupo-pasini-receives-nersc-early-career-achievement-award] Git's first commit is 2020-10-08, and the software DOI is 10.11578/dc.20211019.2 (2021). [KNOWN] The news date likely marks the funded program, not the code. [INFERRED, medium]
- **Frontier is the main target, but public CI is CPU-only.** GitHub Actions runs on `ubuntu-latest` with CPU PyTorch wheels. [KNOWN: .github/workflows/CI.yml] At HEAD, "frontier" appears in 127 files, "crusher" (Frontier's early test system) in 41, "rocm" in 74 and "gfx90a" (the AMD MI250X GPU architecture) in 20. Perlmutter (22), Aurora (11) and Andes (6) trail. `scripts/hpc/` has olcf, nersc and alcf subfolders, added 2026-08-21. [KNOWN: git grep counts] GPU testing happens on the machines themselves, not in public CI. [INFERRED, high]
- **There's a GPU-vendor collaborator.** DOE CODE code-180990 (HydraGNN v5.0, 2026-05-12) lists Advanced Micro Devices (AMD) as a research org next to ORNL. [KNOWN: osti.gov/biblio/code-180990]
- **PyPI lags the releases.** Git tags show v4.0 (2025-08-15) and v5.0 (2026-04-14), while PyPI still serves 3.0 (the connections pass, below). Users who `pip install` get a version two majors old. [KNOWN: tags; INFERRED: practical effect]

### Signal ledger
| Signal | What it suggests | Tag, source | Confidence |
|---|---|---|---|
| Commits per year: 2020 50, 2021 427, 2022 113, 2023 45, 2024 126, 2025 126, 2026 182 (all branches, 1,069 total; 928 on default) | A 2021 burst, a 2023 lull, then steady growth since 2024 | [KNOWN: git log] | high |
| Distinct active authors per year: 3, 14, 6, 4, 15, 24, 14 (2020-2026). New authors 2024 10, 2025 15, 2026 9. 50 total | The team roughly tripled after 2023, which coincides with the graph-foundation-model work | [KNOWN: git log, counts only; INFERRED: cause] | medium |
| Top author 34% of commits, top three 66% | A core group with a wide outer ring | [KNOWN] | medium |
| Last 12 months: 228 commits, peaks 2026-01 (46) and 2026-08 (32) | Actively developed | [KNOWN] | high |
| `examples/multidataset_hpo_sc26/` added 2026-02-13 (38 commits), with Aurora PBS job scripts | Prepared for an SC26 (Supercomputing 2026) submission | [KNOWN: folder; INFERRED: purpose] | medium |
| Sponsor fields: LDRD + ASCR (manuals 2224153, 3367035); LDRD + BES (3252731); OE + ASCR (3377970); SC (code-164024, code-180990). The ornl.gov news story credits ORNL's AI Initiative (AI for Scientific Discovery thrust) | A stack of funders: internal seed money, then Office of Science, now Office of Electricity too | [KNOWN: OSTI API; ornl.gov news] | high |
| Research orgs on 2538215 and 1893210 include LBNL/NERSC | A NERSC partnership, consistent with the Perlmutter scripts | [KNOWN: OSTI API] | high |
| Job trace: a 2025 public postdoc announcement naming HydraGNN expansion | Possible new funded projects in late 2025 | [OUT OF SCOPE, rule 16: the only source was a post on a personal social media account, so the link and quote were removed by the fact-check pass 2026-10-24. Reinstate only if an official ORNL job posting with the same title is found.] | none |
| Commit author metadata that points at lab systems | Not analyzed | [OUT OF SCOPE, rule 16: it would describe ORNL infrastructure; row removed by the fact-check pass 2026-10-24] | none |
| Wayback captures of the repo page: closest returned are 2022-07-22, 2024-12-13 and 2026-06-06 | Light archive interest. The availability API only returns the nearest capture, so these are bounds, not a full list | [KNOWN: archive.org/wayback/available] | low |

## Who actually uses it (connections pass)
Accessed 2026-10-24 (ET). Artifacts only; institution names come from OpenAlex author affiliations, no individuals profiled.

**Outside vs inside:** The brief infers HydraGNN is for scientists screening molecules and materials with AI, and reads 127 stars / 48 forks as a modest outside user base. The outside traces say most visible use is ORNL's own: the citing works that mention HydraGNN in OpenAlex are almost all ORNL-authored (sometimes with LBNL, AMD, Utah), and GitHub shows no real dependent repos.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| PyPI | `HydraGNN` exists, latest 3.0, 2 releases on PyPI | [KNOWN] | https://pypi.org/pypi/hydragnn/json |
| Downloads | pypistats "recent": 2 last day, 12 last week, 26 last month (as of 2026-10-24). Downloads are not users: mirrors and CI inflate them | [KNOWN] counts; [INFERRED] meaning | https://pypistats.org/api/packages/hydragnn/recent |
| conda-forge | No `hydragnn-feedstock` (404) | [KNOWN] | https://github.com/conda-forge/hydragnn-feedstock |
| Spack | No `hydragnn` or `py_hydragnn` package.py (404) | [KNOWN] | github.com/spack/spack-packages builtin |
| GitHub "used by" | Dependents page lists only 2 repos, both PyPI mirror/aggregator repos | [KNOWN] list; [UNRELATED] as real users | https://github.com/ORNL/HydraGNN/network/dependents |
| GitHub interest | 127 stars, 48 forks, 20 open issues, pushed 2026-10-24 | [KNOWN] | GitHub API repos/ORNL/HydraGNN |
| Code search `import hydragnn` | Not reachable without login | [UNKNOWN] | logged in not-found.md |
| Citations | Software DOI 10.11578/dc.20211019.2: 15 citing (OpenAlex); 2022 J. Cheminformatics paper (10.1186/s13321-022-00652-1): 18; 2022 MLST multi-task paper (10.1088/2632-2153/ac6a51): 28 | [KNOWN] | api.openalex.org |
| Who mentions it | Of citing works matching "hydragnn" (13 for the software DOI, 4 for the 2022 paper), every listed one has ORNL among author institutions; outside co-institutions seen: LBNL, AMD, University of Utah | [KNOWN] list; [INFERRED] that use is mostly in-house | OpenAlex filter cites:W4286899761 / W4306392318 + search=hydragnn |

Reasoning: PyPI presence but low downloads, no conda/Spack, no real dependents, and ORNL-authored citing work suggest an ORNL-led research code used mainly by its own team and DOE HPC collaborators [INFERRED, medium confidence]. Matching on "hydragnn" in OpenAlex is a mention, not proof of use.


## Sweep notes (fact-check pass, 2026-10-24)
- Re-fetched and verified: OSTI 3377970 (OE + ASCR sponsors, 2026-07-01) and 3239722 (2026-07-14), DOE CODE code-180990 (AMD listed as research org), the ornl.gov news story ("In 2022, Lupo Pasini and his team started developing HydraGNN"; AI Initiative funding), CI.yml (`ubuntu-latest`, CPU PyTorch wheels), tags v4.0 2025-08-15 and v5.0 2026-04-14, PyPI 3.0 (tag v3.0 is 2023-12-12, so two majors behind holds).
- Not re-run: git grep counts and per-year commit and author counts (the discovery-pass clone). Taken as reported.
- Corrected: the job trace row (personal social post) and the lab-system author metadata row are now out of scope under rule 16.
