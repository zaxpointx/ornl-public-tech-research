
## History, build targets, funding (discovery pass) (accessed 2026-11-11)

### What the outside tells us that the inside doesn't
- The project is accelerating: 28 commits in 2025, 141 in 2026 so far, and authors went from 5 to 7, with 4 new in each year. [KNOWN: git log --all, author date] Read: staffing up during 2026, consistent with the cluster of 2026 papers. [INFERRED, medium]
- Public history compresses the first year and a half into two squashed commits (2024-01-24 and 2025-07-01), on top of a seed commit that is a snapshot of an outside project (PolymathicAI MPP; author date 2023-10-07). [KNOWN: git log e30068e, 8287288, 856c13f] Read: commit counts understate pre-2025 work; do not read 2023-2024 counts as activity. [INFERRED, high]
- Frontier is the clear target: the only ready environment is a shared ROCm 6.3.1 Conda env on Frontier, Slurm scripts use an OLCF allocation (ID left out under rule 16), MIOpen caches on node-local NVMe, 8 ranks per node, and the IPDPS 2026 paper reports a 32,768-GPU run on Frontier. There is no CI and no test suite. [KNOWN: README L6-L13; `examples/submit_batch.sh` L2, L9, L33-L41; OSTI 3367073] Two example inference scripts also carry an `--on_perlmutter` flag. [KNOWN: `examples/basic_inference.py` L19] Read: developed and validated by hand on Frontier, with NERSC Perlmutter as a secondary inference target. [INFERRED, high for Frontier, medium for Perlmutter]
- Funding on the MLST paper record is broad: LDRD, ASCR SciDAC, BES Scientific User Facilities and NERSC; the DOE CODE record names ORNL itself as sponsor. [KNOWN: OSTI API 3365777, code-173753] Read: seed money (LDRD) plus program money; NERSC listed suggests some runs there too. [INFERRED, low]
- Papers span three communities: ML (NeurIPS workshop 2024, MLST 2026), HPC (IPDPS 2026, related RingX at SC25) and fusion (Nuclear Fusion 2026). [KNOWN: README L72-L76; OSTI] A `paper-matey-solps2025` branch and a 2026-09 merge of fusion work point to fusion as the current growth area. [KNOWN: git branch -r; git log 631a413] [INFERRED, medium]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | Seed commit author date 2023-10-07; last commit 2026-09-17; 171 commits all branches, 169 on default; 3 remote branches besides main | git log --all, git rev-list, git branch -r | [KNOWN] |
| Commits per year | 2023: 1 (seed snapshot), 2024: 1 (squash), 2025: 28, 2026: 141 | git log --all, author date | [KNOWN] |
| Active / new authors per year | 2023: 1/1 (upstream seed author), 2024: 1/1, 2025: 5/4, 2026: 7/4; 10 emails in total; top three authors 58%, 27%, 11% | git log | [KNOWN] |
| Tags | v1.0.0 2026-01-26 ("Add MIT license headers and finalize v1.0.0"); pyproject still 0.1.0 | git for-each-ref; pyproject.toml L3 | [KNOWN] |
| Issues / PRs | 4 issues (all open); 53 PRs (4 open) | GitHub search API | [KNOWN] |
| CI | None; `tests/` empty | tree | [KNOWN] |
| HPC keywords (files) | slurm 22, cuda 11, miopen 10, rocm 9, flash 5, rccl 1 (a post-processing plot script), frontier 1, perlmutter 2 (an `--on_perlmutter` flag in two example inference scripts), aurora 1 (a code-attribution comment to Microsoft's Aurora model, not the ALCF machine) | grep -rli | [KNOWN] |
| Parallelism | torch.distributed "nccl" backend, DDP or FSDP, custom sequence-parallel groups with RingX attention over flash-attn | `matey/utils/distributed_utils.py`, `matey/train.py`, `matey/models/ringX_attn.py` | [KNOWN] |
| Funding | MLST paper: LDRD, ASCR SciDAC, BES SUF, NERSC; DOE CODE: ORNL; contract AC05-00OR22725 | OSTI API 3365777, code-173753 | [KNOWN] |
| Datasets published | Zenodo 19889470 (colliding thermals) and 19857523 (liquid-metal MHD), both CC-BY-4.0, both describe use in the MATEY study | Zenodo API | [KNOWN] |
| Repo stats | 13 stars, 9 forks | GitHub API | [KNOWN] |
| Wayback | Not checked this round | n/a | [UNKNOWN] |
| Job postings | Not searched this round | n/a | [UNKNOWN] |

### Usage signals (discovery pass, for the connections pass to extend)
| Signal | Finding | Tag | Source |
|---|---|---|---|
| PyPI | The name `matey` on PyPI (0.1.1) is an unrelated "schema-safe database workflow" tool | [UNRELATED] | https://pypi.org/pypi/matey/json |
| conda-forge / Spack | No feedstock; no `matey` or `py_matey` Spack package (control `py_numpy` 200) | [KNOWN] | conda-forge; spack-packages builtin |
| GitHub "used by" | 0 repositories | [KNOWN] | https://github.com/ORNL/MATEY/network/dependents |
| Citations | OpenAlex: MLST paper (W7160389725) cited 6 times; 4 with ORNL authors (co-institutions Argonne, Georgia Tech, UMass Amherst, York U.), 2 outside-only (U. Michigan; one with no institution listed). IPDPS paper cited once (ORNL); Nuclear Fusion paper cited once (Grand Valley State, ORNL, UT Austin) | [KNOWN] | api.openalex.org filter=cites |
| Code reuse into ORNL code | MATEY copies one helper (`parse_slurm_nodelist`) from a pinned HydraGNN commit | [KNOWN] | `matey/utils/distributed_utils.py` L239-L240 |

Reasoning: forks (9) and two outside-only citing papers within months of the journal paper suggest early outside interest in the adaptive-tokenization idea, but no dependents or packages and Frontier-specific scripts suggest the codebase itself is used mainly by the ORNL team and its interns [INFERRED, medium confidence].
