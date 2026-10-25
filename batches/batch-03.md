# Batch 03 summary

Independent research from public sources only; not affiliated with ORNL. Date: 2026-10-24.

## What was researched
- The discovery pass added 13 catalog rows (discovered_batch 03): far3d, korc, gitr, scale, olm, vera (nuclear/fusion); tasqc, akatosh, can-d (cyber); gauntlet, real-twin, stor4build, energyplus (buildings/transport). The discovery notes are appended below.
- The reading pass wrote 6 briefs: [SCALE](../projects/scale.md), [VERA](../projects/vera.md), [GITR](../projects/gitr.md), [Real-Twin](../projects/real-twin.md), [Gauntlet](../projects/gauntlet.md), [EnergyPlus](../projects/energyplus.md).
- SCALE and VERA (and Shift, cited inside SCALE) are described from public overview pages, the public manual and OSTI only. Nothing about the controlled distribution beyond "licensed, not open source".

## What was verified
This is the first batch checked under the two-sweep rule (RULES.md item 11). Details are in [verification/log.md](../verification/log.md).
- Sweep 1: 47 claims, 33 verified, 9 corrected, 5 unverifiable.
- Sweep 2: 15 checks, 7 verified, 7 corrected, 1 unverifiable. Every load-bearing source was refetched, and nothing contradicted the briefs.
- Notable outcomes:
  - SCALE's license moved from UNKNOWN to KNOWN "licensed, not open source", based on its OSTI datasets. The "fifth volume" is INFERRED to be a validation overview report, modeled on the 6.2.4 series (OSTI 1902803).
  - GITR's DIII-D and STRIPE ties are now KNOWN (OSTI 3452355, 3013481), and a missed 1.0 release was added.
  - Real-Twin has four GitHub releases, the latest being v0.1.2 (2026-05-12), which is also on PyPI.
  - For VERA, "Energy Innovation Hub" was downgraded to INFERRED, and the users group is unverifiable.
  - For EnergyPlus, "DOE's main program" is INFERRED. "Not ORNL-led" now reads "not ORNL-only", with the lead institution INFERRED (the NatLabRockies org).
  - "Shift is Monte Carlo" is CORROBORATED (SCALE manual 2.2.1 plus OSTI 1237627). Map link 82, Shift in SCALE, is also CORROBORATED.
- No restricted content and no maturity upgrades were found.

## Still unknown
- SCALE and VERA: source layout, languages and the owning ORNL division or group.
- Whether Shift and CTF are VERA components. This stays INFERRED, because a benchmark mention isn't membership, and the onramp CASL page is a 2015 stub.
- GITR: there's no DOE CODE software record, so its ORNL division is unknown.
- EnergyPlus: ORNL's specific role, and whether the NatLabRockies org is a renamed NREL (INFERRED).
- VERA: whether ORNL is the sole current developer.

## What to investigate next
- Map link 61 needs a corrected citation, since OSTI 1395245 lists only ORNL. The connections pass is fixing it.
- A primary source naming SCALE's ORNL group, or VERA's current developer list.
- Unread batch 03 rows: far3d, korc, olm, tasqc, akatosh, can-d, stor4build. akatosh and can-d are OSTI-only stubs.

---
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
