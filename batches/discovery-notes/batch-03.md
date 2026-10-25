# Batch 03 discovery notes, 2026-10-24
## Added (13, discovered_batch "03")
- nuclear/fusion: far3d, korc, gitr, scale, olm, vera
- cyber: tasqc, akatosh, can-d
- buildings/transport: gauntlet, real-twin, stor4build, energyplus
## Sources checked
- OSTI records API (https://www.osti.gov/api/v1/records, product_type=Software). Keywords: nuclear, reactor, fusion, plasma, cyber, security, building, vehicle, transportation, traffic. Kept only records whose research_orgs include ORNL.
- DOE CODE biblio pages, for repo links.
- GitHub API, and each repo's own LICENSE file via raw.githubusercontent.com.
- The public GitLab API at code.ornl.gov, for OLM metadata.
- ornl.gov/scale, vera.ornl.gov and ornl.gov/onramp/casl-vera. These are public overview pages only. SCALE is distributed through a controlled channel, so no download links were recorded.
## Dedupe notes
- Skipped because they are already in the catalog: Cyberwheel (OSTI code-134699), AdditiveFOAM, Finch, Myna, Equilipy, mind_the_gap, Profugus.
- Real-Sim/FIXS was skipped because its repo was not reachable.
- J1939 Decoder was skipped because it lives in a personal repo.
- PKPass is an OLCF tool and a candidate for batch 4.
- VERA is cataloged as the overall suite. Its components (VERAView, VERAIn, CTF, MAMBA) are not split out, and MAMBA is LANL's.
## Caveats
- FAR3d: no license file was found.
- OLM: the license comes from GitLab metadata only.
- EnergyPlus: development is multi-lab and NREL-led [INFERRED].
- akatosh and can-d: no public repo was found.
## Priority 6 for deep reading
1. scale: ORNL's flagship nuclear safety suite, with an extensive public validation set on OSTI.
2. vera: a major ORNL-led reactor simulation effort with good public overviews.
3. energyplus: the dominant open building-energy engine, very active, with ORNL as a co-developer.
4. gitr: an active fusion plasma-material interaction code.
5. real-twin: an active, GPL transportation tool with an OSTI record.
6. gauntlet: a clean, MIT-licensed geospatial tool that feeds vivaldi.
## Leads for batch 4
- More ORNL cyber tools on OSTI: Cincinnatus, Heartbeat Malware Detection, CPAD, Situ, Hyperion.
- The ORNL-Real-Sim org.
- Shift/Exnihilo transport (public pages).
- olcf/pkpass.
- Building tools: Roof Savings Calculator, AutoBEM, the WUFI-ORNL version.
- Use the OSTI API with other keywords: grid, power, geospatial, LandScan.
