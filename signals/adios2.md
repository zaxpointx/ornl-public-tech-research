## History, build targets, funding (discovery pass) (accessed 2026-11-11)

Clone: `git clone --filter=blob:none https://github.com/ornladios/ADIOS2`, HEAD `e43363bd5596da4cf2d2c78d7c4940fb512fad2f` on `master`. Read only, nothing built or run. Author counts are distinct author emails. No individual is named or profiled; email domains are shown only as aggregate institutional shares.

### What the outside tells us that the inside doesn't
- **Activity came back in 2026 after a slump.** Commits fell every year from 2,147 (2019) to 377 (2025), then rose to 1,037 in 2026 so far, with 17 new authors. [KNOWN: git log --all, author date] Read: a revival, not a project in maintenance mode. [INFERRED, medium]
- **The 2026 surge is concentrated and partly AI-assisted.** One author accounts for 54% of 2026 commits, and 109 of 948 default-branch commits in 2026 carry an AI-tool `Co-authored-by` trailer. There were none in 2024 or 2025. [KNOWN: git log trailers] Read: much of the 2026 jump may be one maintainer working with AI tools, so raw commit counts overstate the increase in team size. [INFERRED, medium]
- **Code-writing is spread more widely than the copyright line suggests.** By author-email domain, about 27% of all commits come from kitware.com, 19% from a Georgia Tech address, 15% from ornl.gov, and about 27% from personal webmail domains (whose institution can't be told). [KNOWN: git log] Read: ORNL leads and holds the copyright, but a large share of engineering is done by partners, especially Kitware. [INFERRED, medium; personal-domain commits make the ORNL share a lower bound]
- **GPU testing on real hardware happens off GitHub.** GitHub Actions covers Linux, macOS, Windows and sanitizers. A separate GitLab pipeline runs Slurm jobs on OLCF Frontier (AMD gfx90a, ROCm 6.4.2, Kokkos-HIP and Cray builds) and on Ascent (CUDA 11.4.2, Kokkos-CUDA, NVHPC, XL). [KNOWN: `.gitlab/gitlab-ci-frontier.yml` L89-L128, `.gitlab/gitlab-ci-ascent.yml` L43-L67] Read: Frontier is the primary leadership-class target, tested routinely. [INFERRED, high] Account IDs and file-system paths in those files are deliberately not recorded (RULES 16).
- **The release cadence slipped once.** The stated goal is a release every 6 months, but there was no minor release between v2.10.0 (2024-04-03) and v2.11.0 (2025-11-16). [KNOWN: git tags; nutshell.rst L33] Read: the gap lines up with the 2025 commit low, so the team was probably smaller or busy elsewhere that year. [INFERRED, low] Whether it relates to a funding change: [UNKNOWN], no funding-timeline source was read.

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2016-07-14 (author date), last 2026-11-11. 11,940 commits on all branches, 11,741 on `master` (3,745 of those are merges) | git log, git rev-list | [KNOWN] |
| Commits per year (all branches) | 2016: 85, 2017: 1,330, 2018: 1,985, 2019: 2,147, 2020: 1,449, 2021: 1,052, 2022: 953, 2023: 841, 2024: 684, 2025: 377, 2026: 1,037 | git log --all, author date | [KNOWN] |
| Active / new authors per year | 2016: 7/7, 2017: 21/15, 2018: 26/13, 2019: 38/22, 2020: 35/11, 2021: 43/25, 2022: 28/10, 2023: 26/9, 2024: 23/9, 2025: 30/16, 2026: 33/17. 154 emails in total | git log --all | [KNOWN] |
| Top-author shares | All time top five 19.4%, 14.6%, 10.1%, 9.5%, 9.3%. 2026 top three 54.0%, 27.2%, 5.6% | git log --all | [KNOWN] |
| AI co-author trailers | 2024: 0, 2025: 0, 2026: 109 of 948 default-branch commits | git log message trailers | [KNOWN] |
| GitHub contributors | 145 (anonymous included) | GitHub contributors API | [KNOWN] |
| Tags | 32 tags; 25 non-rc from v2.0.0 (2017-06-30) to v2.12.1 (2026-04-28); v2.13.0-rc1 2026-10-27 | git for-each-ref; releases API | [KNOWN] |
| CI (GitHub) | `everything.yml` (Ubuntu 22.04 gcc/clang/MPICH/OpenMPI, macOS 15/26, Windows 2022/2025, sanitizers, ROCm serial, aarch64), plus `pypackaging.yml`, `sbom.yml`, `reuse.yml`, `scorecard-analysis.yml` | .github/workflows | [KNOWN] |
| CI (GitLab, OLCF) | Frontier (Slurm, 8 GPUs per job, gfx90a, ROCm 6.4.2), Ascent (CUDA 11.4.2), a Spack pipeline | .gitlab/*.yml | [KNOWN] |
| HPC keywords (files) | frontier 13, summit 8, perlmutter 8, aurora 4, polaris 2, ascent 10, slurm 5, cuda 39, rocm 8, hip 9, kokkos 45, sycl 6 | git grep -l -i -w at HEAD | [KNOWN] |
| Funding (docs) | "funded by the Department of Energy as part of the Exascale Computing Project" | docs/user_guide/source/introduction/nutshell.rst L35 | [KNOWN] |
| Funding (OSTI) | SoftwareX paper OSTI 1638101: sponsors DOE SC and SC/BES; research orgs LBNL, ORNL. Among 20 records with "ADIOS" in the title: USDOE 7, SC 7, NNSA 2 (Sandia ADIOS 1 items), ASCR 1, BES 1 | OSTI records API (title=ADIOS) | [KNOWN] |
| DOE CODE | No ADIOS2 software record found (only code-3272, a Sandia VTK reader for ADIOS 1 schema) | OSTI API product_type=Software, q=ADIOS / ADIOS2 | [KNOWN], logged in not-found |
| ORNL org page | CSMD software page "ADIOS2" (live fetch failed 2026-11-11; Wayback captures 2019-02-19 to 2024-10-24) | web.archive.org CDX and capture 20241024062808 | [KNOWN] |
| Docs site | Wayback captures of adios2.readthedocs.io from 2021-04-07 | web.archive.org CDX | [KNOWN], bounds the dates only |
| Job postings | Not searched | n/a | [UNKNOWN] |

## Who actually uses it
Accessed 2026-11-11. Artifacts only (RULES 16). Institution names from OpenAlex, no individuals profiled.

**Outside vs inside:** The inside describes a unified I/O framework "used in production". Outside, ADIOS2 is embedded in the broad HPC software stack: 22 Spack packages can depend on it (visualization, CFD, climate, molecular dynamics, linear algebra), it's on PyPI and conda-forge, and about two-thirds of the papers citing it have no ORNL author.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| PyPI | `adios2` 2.13.0.1001, 19 release entries, Apache classifier | [KNOWN] | https://pypi.org/pypi/adios2/json |
| PyPI downloads | Not retrieved: pypistats returned HTTP 429 three times | [UNKNOWN] | https://pypistats.org/api/packages/adios2/recent |
| conda-forge | `adios2` 2.12.1 (file downloads summed: 4,443,709); `libadios2` 2.12.1 (2,973,024). Cumulative across all files and versions, so not a count of users; CI and mirrors inflate it | [KNOWN] counts; [INFERRED] meaning | https://api.anaconda.org/package/conda-forge/adios2, .../libadios2 |
| Spack | `adios2` package, 14 version lines, 4 listed maintainers | [KNOWN] | spack-packages builtin `adios2/package.py` |
| Spack reverse dependencies | 22: adios_catalyst, ascent, casacore, fenics_dolfinx, fides, ftk, hermes_shm, lammps, libpressio_adios2, neon, openfoam, openpmd_api, paraview, py_adios4dolfinx, py_scifem, seacas, sensei, tau, trilinos, visit, vtk, wrf. Most are probably variant-gated (optional), not parsed | [KNOWN] list; [INFERRED] optional | grep `depends_on("adios2` in spack-packages @ ea11964f |
| Catalog dependents | HydraGNN (imports adios2), E3SM EAMxx/SCORPIO (links adios2pio when present) | [KNOWN] | pinned links in projects/adios2.md |
| Citations | SoftwareX paper (DOI 10.1016/j.softx.2020.100561): 267 citing works in OpenAlex (cited_by_count 269); 182 without an ORNL-affiliated author. By year: 2020 7, 2021 35, 2022 48, 2023 43, 2024 44, 2025 50, 2026 39 | [KNOWN] | api.openalex.org works?filter=cites:W3041193038 (and `authorships.institutions.id:!I1289243028`) |
| Citing institutions (top) | ORNL 85, ANL 39, LBNL 32, LLNL 15, U. Utah 15, U. Oregon 14, KTH 14, Rutgers 13, Georgia Tech 13, LANL 11, Kitware 10, Inria 9 | [KNOWN] | OpenAlex group_by institutions |
| Citing countries (top) | US 166, Germany 44, France 26, UK 24, China 17, Sweden 16, Italy 15, Japan 13 | [KNOWN] | OpenAlex group_by countries |
| Mentions | 83 works with "ADIOS2" in title or abstract; top institutions ORNL 13, HZDR 6, KTH 5 | [KNOWN] | OpenAlex title_and_abstract.search |

Reasoning: wide Spack reverse dependencies, cumulative conda-forge downloads in the millions, and about 68% non-ORNL citing works suggest ADIOS2 is genuinely used outside ORNL. The European citing institutions (HZDR, KTH, Inria) point to openPMD/PIConGPU and other non-DOE users. [INFERRED, medium-high; the openPMD link is only suggested by the openpmd_api Spack dependency and HZDR's citation count, and wasn't read in openPMD sources]
