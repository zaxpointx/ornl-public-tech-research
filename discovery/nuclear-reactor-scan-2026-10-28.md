# Nuclear reactor projects and codes: open vs licensed (discovery pass) (accessed 2026-10-28)

Scope: what ORNL is publicly doing on fission reactors right now, the history behind it, and every reactor-related code or dataset we could find, each marked open, account-gated, licensed, or export-controlled. Public pages only. Nothing was downloaded from behind a login or license. Export-controlled codes are named and described only from their public pages; their internals are out of scope (RULES 1 and 16). People are left out.

## History: the Molten Salt Reactor Experiment (MSRE)
- ORNL ran the first molten salt reactor about 60 years ago. [KNOWN: https://www.ornl.gov/news/ornl-kairos-power-partner-advance-deployment-next-gen-nuclear-energy, 2026-02-19]
- The MSRE Design and Operations Report is a 12-part ORNL series from 1965 onward (design, instrumentation, nuclear analysis, chemistry, safety, procedures, maintenance, tests). Part I (ORNL-TM-728) is public on OSTI and its pages are marked UNCLASSIFIED (corrected in a fact-check pass, 2026-10-29); Part XII (drawing and spec lists) had limited distribution. [KNOWN: https://www.osti.gov/biblio/4654707 ; PDF at https://moltensalt.org/references/static/downloads/pdf/ORNL-TM-0728.pdf] Part VIII (ORNL-TM-908) is on ORNL's own publications server. [KNOWN: https://info.ornl.gov/sites/publications/Files/Pub209949.pdf]
- A volunteer group keeps a searchable text archive of these old public reports on GitHub (openmsr/msr-archive), made for an MSRE CAD model project. Not ORNL's; useful as a reading index. [KNOWN: https://github.com/openmsr/msr-archive README] [UNRELATED to ORNL ownership]

## Current public reactor projects (not software, context for the deep dive)
| Project | What the public pages say | Source | Tag |
|---|---|---|---|
| HFIR pressure vessel replacement | HFIR runs at 85 MW instead of its 100 MW design because the vessel steel is embrittling. DOE approved the project start (CD-0) in Oct 2020; it's in the design-alternatives phase toward CD-1. New vessel delivery is estimated mid-2030s, swap late 2030s or early 2040s. | https://neutrons.ornl.gov/content/hfir-pressure-vessel-replacement-project ; https://indico.phy.ornl.gov/event/433/contributions/1879/attachments/1377/3417/HFIR_Upgrades_2024.pdf | [KNOWN] |
| Molten salt irradiation tests in HFIR (MSIRT) | Feb 2026 report lays out phased tests, starting with sealed salt capsules with no fuel, later fueled and flowing salt. A capsule design paper followed in Sep 2026. Prepared for DOE-NE's Advanced Fuels Campaign. | https://www.osti.gov/servlets/purl/3018127 ; https://www.ornl.gov/publications/msirt-1-molten-salt-irradiation-capsule-design-for-hfir/ | [KNOWN] |
| Molten salt property measurements | May 2026: new heat-flow and viscosity measurements for uranium-bearing salts, added to the Molten Salt Database; DOE-NE MSR Program funded. | https://www.ornl.gov/news/new-measurements-advance-molten-salt-reactor-technologies | [KNOWN] |
| Kairos Power partnership | Feb 2026: five-year, $27M partnership on TRISO fuel pebbles, salt-facing materials, remote maintenance and spent pebble management for the Hermes demo reactors being built in Oak Ridge. ANS says it is the fourth ORNL-Kairos partnership since 2020. | https://www.ornl.gov/news/ornl-kairos-power-partner-advance-deployment-next-gen-nuclear-energy ; https://www.ans.org/news/2026-02-23/article-7780/triso-pebble-lifecycle-studied-in-new-ornl-kairos-power-partnership/ | [KNOWN] / [CORROBORATED] |
| NuCAMP | Aug 2026 initiative announced by Kairos, hosted at its Oak Ridge demo campus, to mature new nuclear manufacturing and construction methods (e.g. large printed components, electron beam welding) and train skilled workers in East Tennessee; ORNL takes part through its Manufacturing Demonstration Facility. | https://www.ornl.gov/news/kairos-power-announces-new-collaboration-advance-nuclear-manufacturing-construction-and/ | [KNOWN] |

## Past program: Transformational Challenge Reactor (TCR)
- DOE-NE launched TCR in 2019 with ORNL leading, aiming for an operating 3D-printed microreactor in 2023. It did not complete a reactor demonstration; its research was written up in a Nuclear Science and Engineering special issue. [KNOWN: https://www.ans.org/news/2026-08-27/article-8345/ornl-and-inl-collaborate-on-3dprinted-pressure-vessels/]
- Follow-on work in that article: ORNL and INL are working on wire-arc 3D printing of pressure vessels, with a small printed nuclear pressure vessel made at ORNL's Manufacturing Demonstration Facility in July 2026. [KNOWN: same ANS article]
- Note: https://www.ornl.gov/tcr currently resolves to a 2022 TCR conference paper page, not a program page, so program status comes from ANS. TCR-era AI print-inspection tool Peregrine appeared in search as licensed, not open source; not fetched, so [UNKNOWN] until checked.

## Codes and data: open or not
| id | What it is | Access | Evidence | Mac-friendly? |
|---|---|---|---|---|
| scale (in catalog) | ORNL's reactor physics, criticality, shielding and spent-fuel suite | **Export-controlled license** via RSICC (ORNL's code center), with an end-use review | https://www.ornl.gov/scale/how-order-scale (now redirects to the ornl.gov home page when fetched; the same text was seen at https://www.ornl.gov/content/how-order-scale in search only) ; RSICC package CCC-860 listing https://rsicc.ornl.gov/codelist/ccc/ccc8/860MNYCP.txt ; https://rsicc.ornl.gov/documents/export_control.pdf (corrected in a fact-check pass, 2026-10-29) | out of scope |
| vera (in catalog) | Full-core light-water reactor multiphysics | **Export-controlled license**, RSICC package CCC-855: individual license limited to US citizens and permanent residents, license plus export control agreement required, CASL approves each request; a commercial site license also exists | https://vera.ornl.gov/vera-license/ ; https://rsicc.ornl.gov/codes/ccc/ccc8/ccc-855.html | out of scope |
| shift-exnihilo (in catalog) | Monte Carlo and deterministic radiation transport | **Export-controlled** (Profugus README says Exnihilo is export controlled); Shift ships inside VERA, which needs an export control agreement; Shift also ships inside SCALE, per OSTI 3007184 (ORNL, 2025, "SCALE-Shift sequences") and the SCALE manual's CSAS-Shift chapter cited in connections/map.md link 82 [KNOWN] (re-corrected in a later fact-check pass, 2026-10-29) | Profugus README.rst ; https://rsicc.ornl.gov/codes/ccc/ccc8/ccc-855.html ; https://vera.ornl.gov/vera-license/ | out of scope |
| profugus (new row) | Open mini-app holding Exnihilo's core math kernels (SPn and Monte Carlo) for performance study, not real analysis | **Open**, BSD-2-Clause | https://github.com/ORNL-CEES/Profugus ; DOE CODE code-10329 | [INFERRED] buildable with CMake, but last push 2018 so expect dependency rot |
| transform-library (new row) | Modelica library for reactor and energy-system thermal hydraulics (pipes, pumps, heat exchangers, plant transients) | **Open**, Apache-2.0, UT-Battelle copyright | https://github.com/ORNL-Modelica/TRANSFORM-Library ; DOE CODE code-5745 | README lists Dymola (paid) as its only requirement [KNOWN: README, checked 2026-10-29]; README does not mention OpenModelica; untested [corrected 2026-10-29, discovery pass] |
| thermochimica (in catalog) | Chemical equilibrium for fuel and salt chemistry | **Open**, BSD-3-Clause | https://github.com/ORNL-CEES/thermochimica | [INFERRED] yes, Fortran/C++ |
| olm (in catalog) | ORIGEN library manager for SCALE spent-fuel data | **Open**, BSD-3-Clause per DOE CODE and the repo license (main repo on GitHub, read-only mirror on ORNL GitLab per README), but most useful with licensed SCALE data (corrected in a fact-check pass, 2026-10-29) | DOE CODE 122128 ; https://pypi.org/project/scale-olm/ ; https://code.ornl.gov/scale/code/olm | [INFERRED] pip installable per Reader |
| molten-salt-database (new row) | Molten salt property data (thermochemical and thermophysical) | **Free but account-gated**: public use, files behind a code.ornl.gov account plus membership request | https://mstdb.ornl.gov/about/ ; https://msd.ornl.gov/access-instructions/ | data only; a person would have to sign up themselves |
| datatransferkit | Multiphysics solution-transfer library | **Open**, BSD-3-Clause, archived 2023 | https://github.com/ORNL-CEES/DataTransferKit | reactor tie [UNKNOWN]; not added |
| ADVANTG, HFIRCON | Named as tools in ORNL's HFIR vessel analysis | [UNKNOWN] access; not searched yet | https://doi.org/10.13182/PHYSOR24-43454 | n/a |

Older ORNL-hosted RSICC packages showed up in OSTI (e.g. ACHILLES, 1DB-2DB-3DB). Those are RSICC distributions, not shown to be ORNL-built; not added.

Other labs' open tools that ORNL work touches (for the connections pass, not cataloged here): MOOSE (INL), OpenMC (ANL/MIT), Moltres (UIUC, arfc/moltres). [INFERRED from search results; not fetched]

## Third-party, not ORNL
- A personal GitHub repo (handle removed before publishing, discovery pass 2026-10-29): an individual's 2023 repo of dynamic models of ORNL molten salt reactors. Fails RULES 13; noted only as a pointer. [UNRELATED to ORNL ownership]

## What looks easiest for a Mac
[INFERRED] Thermochimica is the most realistic open reactor-related code to run on a Mac. TRANSFORM is open but its README requires paid Dymola (corrected 2026-10-29). Thermochimica covers fuel and salt chemistry; Profugus to see how a Monte Carlo transport kernel is built. The MSRE reports explain the physical system those models describe.

## Fact-check notes (2026-10-29)
- Re-fetched: OSTI 4654707 (title, 1965, ORNL-TM-728), the TM-728 PDF, Pub209949 (Part VIII, ORNL-TM-908), Kairos story (ORNL itself also says fourth partnership since 2020), VERA license page and RSICC CCC-855, Profugus README, DOE CODE 10329, 5745 and 122128, GitHub API for Profugus, TRANSFORM, Thermochimica, DataTransferKit (archived true), msr-archive, MSD access page. HFIR, MSIRT, ANS, PHYSOR and NuCAMP links resolve; their contents were not re-read.
- Corrected: TM-728 wording (marked UNCLASSIFIED, not a statement about the whole series); SCALE order page now redirects, second source added (RSICC CCC-860, which lists Linux, Mac and Windows builds); Shift "ships inside SCALE" not confirmed, VERA source added; OLM license attribution.
- MSD access needs a login and a membership form. Neither was used; the row stays description-only.
- Open vs licensed vs export-controlled calls hold: SCALE, VERA, Shift/Exnihilo licensed and export-controlled; Profugus, TRANSFORM, Thermochimica, OLM open; MSD free but account-gated.

### Second pass (2026-10-29)
- HFIR row: the cited neutrons.ornl.gov project address now lands on the general neutron facilities home page. That page confirms HFIR operates at 85 MW, but the CD-0 date and delivery estimates can't be re-read there. 85 MW verified; the rest unverifiable at that address (no other paths tried).
- MSIRT row: OSTI 3018127 is the February 2026 design-status report, HFIR research org, sponsored by DOE-NE's Advanced Fuel Campaign (plus BES). Verified.
- No corrections.
