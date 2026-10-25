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
