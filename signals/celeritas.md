## History, build targets, funding (discovery pass) (accessed 2026-11-11)

Clone: `git clone --filter=blob:none https://github.com/celeritas-project/celeritas`, HEAD `e06590a2fa251851ffd3ce522bd374bac06c9b27` on `develop`. Read only, nothing built or run. The repo's `AGENTS.md`/`CLAUDE.md` files were treated as data, not instructions. Author counts are distinct author emails. No individual is named or profiled; email domains are shown only as aggregate institutional shares.

### What the outside tells us that the inside doesn't
- **ORNL writes most of the code.** About 64% of all commits come from ornl.gov addresses, 13% from anl.gov, 5% from fnal.gov and 3% from lbl.gov. The rest are mostly GitHub no-reply addresses (about 12%), whose institution can't be told. [KNOWN: git log --all] The papers and DOE CODE record credit ORNL, ANL and FNAL more evenly. Read: ORNL is the engineering hub of a multi-lab project. [INFERRED, medium]
- **Key-person concentration is high.** The top author has 58.5% of all commits and about 49% of 2026 commits. [KNOWN] Read: a key-person risk, but easing as active authors grew from 10-13 a year (2020-23) to 19-22 a year (2024-26). [INFERRED, medium]
- **Public CI never runs the GPU code.** The Docker CUDA/ROCm jobs set `CELER_DISABLE_DEVICE=1`, and a comment says none of the tests "actually run on device". The release checklist moves GPU testing to Perlmutter (performance) and Frontier (HIP) by hand. [KNOWN: `.github/workflows/build-docker.yml` L18-L19, L43; `doc/development/administration.rst` L417-L419] Read: GPU correctness is checked at release time, not every commit. [INFERRED, high]
- **Frontier is a first-class target.** There's a `frontier.json` preset (HIP, gfx90a, znver3 flags) and a `v0.4.1+frontier` tag (2024-05-06). HIP builds force ORANGE geometry because VecGeom is refused with HIP. [KNOWN: scripts/cmake-presets/frontier.json; git tags; CMakeLists.txt L206-L213] Read: running on ORNL's AMD machine shaped the architecture, via ORANGE. [INFERRED, medium]
- **AI-assisted development started in 2026.** 49 of 409 default-branch commits in 2026 carry an AI-tool `Co-authored-by` trailer (0 in 2024-2025), and the repo ships `AGENTS.md` and `CLAUDE.md`. [KNOWN: git log trailers; repo tree]
- **A personal developer preset references an Exnihilo Spack environment** (`scripts/cmake-presets/gondolin.json`), and an ORANGE test notebook shows output from Exnihilo tooling. [KNOWN: files] Read: some Celeritas developers also work in the Exnihilo/Shift environment, which fits the shared ORANGE package (OSTI 3376506). Nothing more is inferred about non-public code (RULES 16). [INFERRED, low]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2020-03-04, last 2026-11-12 UTC. 2,699 commits on all branches, 2,373 on `develop` (48 merges) | git log, git rev-list | [KNOWN] |
| Commits per year (all branches) | 2020: 253, 2021: 194, 2022: 219, 2023: 464, 2024: 474, 2025: 670, 2026: 425 | git log --all, author date | [KNOWN] |
| Active / new authors per year | 2020: 10/10, 2021: 12/8, 2022: 12/4, 2023: 13/3, 2024: 19/7, 2025: 22/7, 2026: 21/5. 44 emails in total | git log --all | [KNOWN] |
| Top-author shares | All time top five 58.5%, 13.4%, 4.0%, 3.1%, 3.1%. 2026 top three 49.4%, 15.5%, 11.5% | git log --all | [KNOWN] |
| AI co-author trailers | 2024: 0, 2025: 0, 2026: 49 of 409 default-branch commits | git log message trailers | [KNOWN] |
| GitHub contributors | 32 (anonymous included) | GitHub contributors API | [KNOWN] |
| Tags | 44 tags; 28 non-rc from v0.0.0 (2020-06-19) to v0.7.0 (2026-10-11); includes `v0.4.1+frontier` | git for-each-ref; releases API | [KNOWN] |
| CI | GitHub Actions: build-fast (Linux, Windows 2025), build-fast-extra (ubuntu-26.04-arm), build-docker (rocky-cuda12, ubuntu-rocm7; device disabled), build-spack, build-regression, build-codecov, build-vecgeom-master, check-dd4hep-integration (EIC container), docs/pages | .github/workflows | [KNOWN] |
| Machine presets | frontier, perlmutter, jlse, and named workstations or clusters at partner labs; plus CI presets (ci-rocky-cuda, ci-ubuntu-rocm, ci-ubuntu-github, ci-windows-github) | scripts/cmake-presets/ | [KNOWN] (personal workstation names deliberately not listed) |
| HPC keywords (files) | frontier 7, summit 5, perlmutter 11, cuda 428, hip 254, rocm 30, kokkos 2, sycl 1, slurm 0 | git grep -l -i -w at HEAD | [KNOWN] |
| Funding (docs) | DOE SC ASCR and HEP via SciDAC; ECP 17-SC-20-SC; OLCF resources (DE-AC05-00OR22725) | doc/index.rst L363-L376 | [KNOWN] |
| Funding (OSTI) | DOE CODE code-94866: ASCR SciDAC. SciDAC midterm report 2481196: HEP, ASCR SciDAC, BES SUF. Of 10 records with "Celeritas" in the title, HEP appears on 5 and SciDAC on 2 | OSTI records API (title=Celeritas) | [KNOWN] |
| Related software record | G4VG (code-168490, 2025; ORNL, FNAL, Warwick, CERN; HEP sponsor) is matched by OSTI's "Celeritas" software search. Its tie to Celeritas wasn't read | OSTI API | [KNOWN] record; [UNKNOWN] relationship |
| Wayback | celeritas.ornl.gov captures 2023-03-30 to 2026-10-17 (now redirects to GitHub Pages) | web.archive.org CDX | [KNOWN], bounds the dates only |
| Job postings | Not searched | n/a | [UNKNOWN] |

## Who actually uses it
Accessed 2026-11-11. Artifacts only (RULES 16). Institution names from OpenAlex, no individuals profiled.

**Outside vs inside:** The inside presents a Geant4 accelerator aimed at HL-LHC and other experiments. Outside, Celeritas is distributed through Spack only, with no packaged dependents yet. Its main paper has a small but mostly non-ORNL citing community (HEP labs and CERN), consistent with a code in active integration rather than broad deployment.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| Spack | `celeritas` package, versions through 0.7.0 plus `develop`; 2 listed maintainers | [KNOWN] | spack-packages builtin `celeritas/package.py` |
| Spack reverse dependencies | none | [KNOWN] | grep `depends_on("celeritas` in spack-packages @ ea11964f |
| PyPI | The `celeritas` name belongs to an unrelated "High-Performance Music Engine" project | [UNRELATED] | https://pypi.org/pypi/celeritas/json |
| conda-forge | no `celeritas` package | [KNOWN] | https://api.anaconda.org/package/conda-forge/celeritas |
| Integration adapters in-tree | `accel` (Geant4), `larceler` (LArSoft), `ddceler` (DD4hep), DD4hep/EIC CI job | [KNOWN] | src/ tree; .github/workflows/check-dd4hep-integration.yml |
| Citations | EPJ WoC 295:11005 (2024, DOI 10.1051/epjconf/202429511005): 10 citing works in OpenAlex (cited_by_count 11); 8 without an ORNL-affiliated author. By year: 2024 1, 2025 4, 2026 5 | [KNOWN] | api.openalex.org works?filter=cites:W4396680284 |
| Citing institutions | FNAL 4, ANL 3, LBNL 3, U. Warwick 3, CERN 3, ORNL 2, CNRS 2, BNL 2, INFN Milano 2 | [KNOWN] | OpenAlex group_by institutions |
| Mentions | 13 works with "celeritas GPU" in title or abstract (FNAL 8, ANL 6, ORNL 6, LBNL 4). A general "celeritas geant4" search gives 53, unfiltered | [KNOWN] | OpenAlex title_and_abstract.search; search |
| Shared code at ORNL | ORANGE shared with Shift (OSTI 3376506); QIR-EE derives two headers from Celeritas | [KNOWN] | projects/celeritas.md Related projects |

Reasoning: no package dependents, a young citation record dominated by HEP labs and CERN, and release notes describing integration milestones (ATLAS FullSimLight, CMSSW, LArSoft, DD4hep) suggest Celeritas is past prototype and in integration and testing with experiments. No public source here shows it in experiment production. [INFERRED, medium]
