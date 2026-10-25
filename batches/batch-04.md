# Batch 04 summary

Independent research from public sources only; not affiliated with ORNL. Date: 2026-10-24.

## What was researched
- The discovery pass added 13 catalog rows (discovered_batch 04): cincinnatus, heartbeat-malware, cpad, situ, hyperion (cyber); fixs, pyxodr3d, roof-savings-calculator, autobem, wufi-ornl (buildings/transport); shift-exnihilo (nuclear/fusion); landscan (climate/earth, a dataset); urban-net-toolkit (grid/energy). The discovery notes are appended below.
- The reading pass wrote 4 full briefs, [LandScan](../projects/landscan.md), [Shift / Exnihilo](../projects/shift-exnihilo.md), [FIXS](../projects/fixs.md) and [AutoBEM](../projects/autobem.md), plus 2 draft OSTI-only briefs, [Situ](../projects/situ.md) and [Roof Savings Calculator](../projects/roof-savings-calculator.md).
- Scope and status decisions made during this batch: RULES.md item 13 (catalog scope) and item 14 (status values, including stub-osti-only and draft-osti-only). autobem became a normal row (status unknown) because its Model America dataset has a public landing page. situ and roof-savings-calculator are draft-osti-only and listed separately in INDEX.

## What was verified
The fact-check pass ran sweeps 1 and 2 on all six briefs (RULES.md item 11). The counts below are the combined total for both sweeps. Details are in [verification/log.md](../verification/log.md).
- 33 claims: 16 verified, 15 corrected, 2 unverifiable. The restricted-content screen was clean. FIXS's private ProprietaryFiles repo was not opened.
- Notable outcomes:
  - AutoBEM: the 122.9M-building count is CORROBORATED (OSTI 3740812 plus Constellation DOI 10.13139/ORNLNCCS/1774134). Model America has been public since 2021-04-14, and its runs used the Argonne Leadership Computing Facility, not OLCF. Status was set to unknown, and a walkthrough was added.
  - Shift / Exnihilo: the Radiation Transport Group credit was read directly in the OSTI 1237627 full text (single source). CADIS / FW-CADIS is CORROBORATED. Status "active" and "not openly distributed" were downgraded to INFERRED. The VERA tie got a caveat, since it is only a benchmark-suite link.
  - LandScan: CC BY 4.0 and the HD/USA legacy status are now cited to the site's own text. The licensing page returns 403, so the site bundle text was used.
  - FIXS: MIT, 2023 UT-Battelle, ORNL as project lead per the README. The release history was corrected to 9 releases, including a "stable" tag from 2026-09-27.
  - Situ: "network" was narrowed to INFERRED. The OSTI text only says it scores events with probabilistic models.
  - Roof Savings Calculator: the input is "above-sheathing ventilation", not attic ventilation. roofcalc.com was unreachable on 2026-10-24.
- Map items from this sweep: link 85 (AutoBEM generates EnergyPlus/OpenStudio models; RSC runs AtticSim plus DOE-2.1E, which also settles link 100) and a caveat on link 99 that the compute was ALCF. Links 94, 97, 98, 101 and 102 checked out as written.

## Still unknown
- The year LandScan won its R&D 100 award, which the site doesn't state.
- Any AutoBEM software release after 2023, and whether the data-center paper (OSTI 3384902) uses AutoBEM, since that record has no abstract.
- Whether Shift / Exnihilo is still actively developed. That is now INFERRED from a 2025 paper.
- Situ's actual input data, and whether the tool still exists after 2014.
- Whether roofcalc.com is down for good or was only unreachable that day.
- urban-net-toolkit's scope, which is still INFERRED from its title.

## What to investigate next
- Connections pass: apply the link 85, 99 and 100 notes in map.md.
- Re-fetch roofcalc.com on a later date before calling RSC retired.
- The discovery-pass batch 4 leads: OSTI dataset records (LandScan USA/HD, LandCast), Denovo/ORANGE in the SCALE manual, the OSTI keywords not yet searched (grid, microgrid, battery, isotope, HFIR, neutron), ORNL OpenStudio measures, and PKPass.
- Unread batch 04 rows: pyxodr3d (has a repo), plus the OSTI-only stubs cincinnatus, heartbeat-malware, cpad, hyperion, wufi-ornl and urban-net-toolkit.

---
# Batch 04 discovery notes, 2026-10-24
## Added (13, discovered_batch "04")
- cyber: cincinnatus, heartbeat-malware, cpad, situ, hyperion (all OSTI-only, no repo)
- buildings/transport: fixs, pyxodr3d, roof-savings-calculator, autobem, wufi-ornl
- nuclear/fusion: shift-exnihilo (public overview only; distributed within SCALE)
- climate/earth: landscan (subdomain: geospatial; a dataset, not software)
- grid/energy: urban-net-toolkit
## Sources checked
- OSTI records API, searching each name plus the keywords malware, intrusion, geospatial and LandScan. Kept only records with ORNL as research org.
- GitHub org ORNL-Real-Sim (licenses read from raw files).
- Public pages: landscan.ornl.gov, an ornl.gov Shift publication page, the SCALE manual's CSAS-Shift page, and the Shift JCP 2016 and EPJ-N 2025 papers.
## Dedupe notes
- FIXS is the renamed Real-Sim (DOE CODE 110562). It was previously skipped as unreachable.
- Shift and Exnihilo are one row; Denovo is folded in. Related rows: scale, vera.
- Not added: ORNL-Real-Sim/paper_Agentic_Traffic_Intelligence (a paper code repo) and FIXS-Binaries (a distribution repo).
## Caveats
- 9 rows have only an OSTI record and no public repo. Their status is unknown and their license [UNKNOWN].
- autobem is marked Closed Source on OSTI.
- urban-net-toolkit's description was not read; its scope is [INFERRED] from the title.
- LandScan's license/terms were not read.
## Top 6 for deep reading
1. landscan: a globally used, R&D100-winning ORNL population dataset with a public viewer.
2. shift-exnihilo: a flagship exascale Monte Carlo transport code with strong public papers.
3. fixs: active, MIT-licensed vehicle-in-the-loop testing framework.
4. autobem: national-scale building energy modeling with high impact, though closed source.
5. situ: a representative ORNL cyber situational-awareness tool.
6. roof-savings-calculator: a long-running public tool (roofcalc.com).
## Leads for batch 5
- OSTI Dataset records from ORNL: LandScan USA, LandScan HD, the Myriad/LandCast work.
- Denovo/ORANGE details in the public SCALE manual.
- OSTI keywords not yet searched: "grid", "power system", "microgrid", "battery", "isotope", "HFIR", "neutron".
- ORNL building tools: the BEopt contributions, and the open-source ORNL OpenStudio measures.
- PKPass (olcf/pkpass).
