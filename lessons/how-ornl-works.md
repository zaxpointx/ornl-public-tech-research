# How ORNL works, seen from the outside (first draft)

Independent research from public sources only; not affiliated with ORNL. Draft started 2026-10-24 (ET).
Every lesson here is built from evidence already in this repo: [connections map](../connections/map.md) (cited as "map link N"), [signals files](../signals/), [project briefs](../projects/) and [verification](../verification/log.md). No new sources were fetched for this draft. Tags follow RULES.md: [KNOWN] means each example is stated in a cited source; [INFERRED] means the cross-project pattern is a reading of several facts, not something any source says. Most lessons are INFERRED on purpose: no single public page describes "how ORNL works". People are described by role only.

## Lesson 1. Facility testing code wakes up with each new machine
**Pattern.** Software that exists to bring up and check a supercomputer shows bursts of activity when a new system arrives and goes quiet in between.
- [OLCF Test Harness](../projects/olcf-test-harness.md): 213 and 146 commits in 2016 and 2017, a quiet 2018 to 2021, then a rise from 2022 to a peak of 203 commits in 2025; Frontier is the only machine with its own example config; three releases in 18 months after a single release before 2025. [KNOWN: [signals/olcf-test-harness.md](../signals/olcf-test-harness.md)]
- [ExaTN](../projects/exatn.md) shows the reverse side: it was built for Summit (CUDA arch 70 example) and has no Frontier build, and it stopped in 2023. [KNOWN: [signals/exatn.md](../signals/exatn.md)] Reading: code that is not moved to the next machine tends to stop. [INFERRED, low]
- [ExaGO](../projects/exago.md) and [HydraGNN](../projects/hydragnn.md) both carry Frontier build or install scripts. [KNOWN: map links 26, 170]
- The neutron tools show a similar wake-up around a facility upgrade instead of a new computer (see Lesson 6). [INFERRED, low to medium]

**Tag:** [INFERRED, low to medium]. The timing fit with Frontier is a reading of commit counts; the discovery pass rated it low confidence.
**For a student:** release and test tooling around a new machine is real, recurring work; Linux, Slurm/LSF job schedulers and Python test frameworks show up in this kind of repo. [INFERRED from the harness docs naming Slurm and LSF]

## Lesson 2. Quiet repos can still be widely used or cited
**Pattern.** A repo's commit history and its outside impact are separate signals. Several projects are quiet or small in commits but heavily cited by groups with no ORNL author.
- [ExaTN](../signals/exatn.md): no commits after 2023-07-19, yet 16 of 19 works citing its 2022 paper have no ORNL author. [KNOWN]
- [XACC](../signals/xacc.md): code quiet since 2023-2024, 143 citing works, 96 with no ORNL author, but only 35 PyPI downloads last month. [KNOWN: map link 164]
- [Thermochimica](../signals/thermochimica.md): commits fell from 837 (2021) to 16 to 46 a year, yet it is built into INL's MOOSE and cited mostly from outside ORNL. [KNOWN: map link 52; signals file]
- Datasets are the extreme case: [Daymet](../signals/daymet.md) versions are cited over a thousand times, about 96% without an ORNL author, and outside groups maintain their own client libraries. [KNOWN]

**Tag:** [INFERRED, medium]. Citation counts are KNOWN (OpenAlex); "still used" vs "only cited" can't be told apart from citations alone.
**For a student:** do not judge a lab project by its last commit date; check citations and who embeds it.

## Lesson 3. Big outside reach usually means shared, multi-institution ownership
**Pattern.** The most-used tools are not ORNL-only. Their copyright lines or OSTI records list several labs, and ORNL authors are a minority of citers.
- [Mantid](../signals/mantid.md): 1,807 citing works, about 61% with no ORNL author; ORNL's neutron sciences directorate is one of several copyright holders. [KNOWN: map link 53]
- [EnergyPlus](../signals/energyplus.md): 2,837 citing works, 30 with an ORNL author; hosted in another lab's GitHub org with ORNL as one named copyright holder. [KNOWN: map link 61]
- [Xolotl](../signals/xolotl.md): six copyright holders (UT-Battelle first) and fission-gas papers with other labs and universities. [KNOWN: map links 136, 140]
- [Cabana](../signals/cabana.md): README names six labs in its ECP co-design project; three quarters of citers have no ORNL author. [KNOWN: map links 146, 166]
- **Two contrasting shared-ownership paths:**
  - [EnergyPlus](../signals/energyplus.md): commits from ornl.gov addresses fell from 10% (2016) to 1% (2019) and 0% from 2022 on, development is led from another lab's GitHub org, and ORNL's own EnergyPlus-related DOE CODE records are add-ons such as stor4build (code-170060). [KNOWN: signals/energyplus.md history section] So ORNL now mostly builds add-ons rather than the engine. [INFERRED: the history section reads it as co-owner and user]
  - [Mantid](../signals/mantid.md): a multi-lab codebase (386 author emails, no author above 4%) where ORNL's commit share went from 48 to 63% (2010 to 2011) down to about 10 to 15%, and back up to 18 to 27% since 2023. [KNOWN: signals/mantid.md history section]

**Tag:** [INFERRED, medium].
**For a student:** contributing to a multi-lab project means working in a public, community-governed repo, which is often the easiest door in.

## Lesson 4. Code is handed down and reused across projects
**Pattern.** New ORNL projects often build on, plug into, or continue earlier ones, inside ORNL and across labs.
- Additive manufacturing: [3DThesis](../projects/3dthesis.md), [Finch](../projects/finch.md) and [AdditiveFOAM](../projects/additivefoam.md) each export data in a format for ExaCA (an LLNL repo); Finch and ExaCA can be built coupled; [Myna](../projects/myna.md) drives all of them. [KNOWN/CORROBORATED: map links 27-29, 70, 171-173] The "ladder" framing itself is editorial. [INFERRED: map link 33]
- Quantum: [TNQVM](../projects/tnqvm.md) is an accelerator plugin for [XACC](../projects/xacc.md) with optional [ExaTN](../projects/exatn.md) support, and [QIR-EE](../projects/qiree.md) has an optional XACC backend. [KNOWN: map links 142, 144, 162]
- Workflows: [Zambeze](../projects/zambeze.md) loads [Flowcept](../projects/flowcept.md) in its code, but current Flowcept no longer has the class Zambeze imports. [CORROBORATED/KNOWN: map link 114] So hand-downs can drift.
- Across labs: [ExaGO](../projects/exago.md) LICENSE says it uses code from ExaGO v1.6.0 while the PNNL repo is archived. [KNOWN: map link 148] That ORNL's repo is the continuation is [INFERRED]. [post-processing-agent](../projects/post-processing-agent.md) points to an older Mantid-org repo as its predecessor. [KNOWN: map link 105]

**Tag:** [INFERRED, medium] for the general pattern; each code tie is KNOWN as cited.
**For a student:** reading the interfaces between two repos (file formats, plugins, optional build flags) is a good way to understand a cluster.

## Lesson 5. Shared facilities act as hubs
**Pattern.** Facilities pull many unrelated projects together: projects target the same machines, acknowledge the same facility, or serve the same instruments.
- OLCF: [Flowcept](../projects/flowcept.md) (Frontier example, acknowledgement), [HydraGNN](../projects/hydragnn.md), [ExaGO](../projects/exago.md), [DataFed](../projects/datafed.md) (central services hosted in OLCF) and [E3SM ELM](../projects/e3sm-elm.md) datasets with OLCF DOIs. [KNOWN: map links 8, 26, 51, 78, 170]
- SNS and HFIR: [SNAPRed](../projects/snapred.md) (SNS), [PyRS](../projects/pyrs.md) (HFIR), [data-workflow](../projects/data-workflow.md), [ONCat](../projects/oncat.md), all around [Mantid](../projects/mantid.md). [KNOWN: map links 2, 23, 34, 36, 37, 75, 129]
- MDF: [Myna](../projects/myna.md) is built around the facility's Peregrine database. [KNOWN: map link 71]
- Caveat: a facility DOI is not proof of compute there. The Model America dataset has an OLCF DOI but its compute ran at Argonne's facility. [KNOWN: map link 99]

**Tag:** [INFERRED, medium] that facilities shape software; ties are KNOWN.
**For a student:** facility-run software (data pipelines, catalogs, test tools) is operations work close to Linux, networking and Python skills.

## Lesson 6. Facility pipelines get rebuilt together
**Pattern.** The SNS neutron data tools went quiet around 2017 to 2020 and came back together from 2021 to 2024, with team-maintained histories and fast releases.
- [data-workflow](../signals/data-workflow.md): burst 2012-2016, quiet 2017-2020, peak 447 commits in 2022, 107 tags. [KNOWN]
- [live-data-server](../signals/live-data-server.md): nothing 2017-2021, peak 118 commits in 2024. [KNOWN]
- [post-processing-agent](../signals/post-processing-agent.md): near stop 2017-2019, 101 commits in 2023, five releases in a year. [KNOWN]
- The repos share top contributors. [KNOWN: map link 35] A shared maintaining group is [INFERRED].

**Tag:** [INFERRED, medium]. Why the revival happened is [UNKNOWN]; no funding record was found for these three.
**For a student:** these repos show modern practice (CI, conda, Docker, release candidates) on facility plumbing.

**Update from the SNS deep dive ([walkthrough](../deep-dives/sns-neutron-pipeline.md)):**
- *The pipeline works like a relay race.* After a run, the translator that writes the data file sends a "ready" message. data-workflow routes it to two jobs, ONCat cataloging and Mantid reduction, and post-processing-agent runs both and reports back. WebMon then shows the status and the plots it pulls from live-data-server. The facility's software is mostly separate wiring programs around one shared physics engine. [KNOWN: data-workflow glossary and queue code; INFERRED: the lesson]
- *The revival tracks the beam shutdown.* The 2021 restart looks like cleanup (Python 3, containers). post-processing-agent's busiest months (2023-11 to 2024-01) fell inside the SNS Proton Power Upgrade outage (August 2023 to April 2024), and live-data-server's (2024-06 to 2024-08) came as the beam returned. [KNOWN: git log, [PPU paper](https://doi.org/10.18429/jacow-linac2024-thpb045)] No public source links the two, so the cause stays [UNKNOWN] and the timing match is [INFERRED, low to medium]. The outside-in lesson: a facility's downtime can be when its software gets rebuilt.

## Lesson 7. Many projects rest on one or two people
**Pattern.** Commit shares show that some research codes are carried by a single main developer, while facility tools are spread across teams.
- [ExaTN](../signals/exatn.md): top author 73% of commits, then stopped. [KNOWN]
- [Thermochimica](../signals/thermochimica.md): top author 74%, but 5 or 6 people active every year. [KNOWN]
- Contrast: [live-data-server](../signals/live-data-server.md) top author 21%, [post-processing-agent](../signals/post-processing-agent.md) 25%. [KNOWN]

**Tag:** [INFERRED, low]. A single main author doesn't by itself explain a project stopping.
**For a student:** small single-maintainer projects may welcome help, but check activity first.

## Lesson 8. Funding programs leave readable traces, and they line up with domains
**Pattern.** OSTI sponsor fields match the science area; internal LDRD money shows up on early or exploratory tools.
- Computing tools: ASCR on most Flowcept, Test Harness and QIR-EE records. [KNOWN: signals files]
- Domain offices: Nuclear Energy on 6 of 7 Thermochimica records; Fusion Energy Sciences on GITR; EERE on Real-Twin and adamantine; FEMA and FEMP on Gauntlet; Electricity (OE) on HydraGNN's power-grid models. [KNOWN: signals files; map link 127]
- LDRD: Cyberwheel (project 11049), Flowcept and Zambeze (project 11521), adamantine. [CORROBORATED/KNOWN: map links 56, 113, 125]
- ECP: ReSolve (DOE CODE), Cabana (README). [KNOWN: map links 7, 146]
- Many records just say "USDOE" (GridKit, XACC, TASMANIAN, ExaGO), so the program is unknown. [KNOWN]

**Tag:** [INFERRED, medium] for the domain match; each sponsor field is KNOWN.
**For a student:** the sponsor tells you which DOE office cares about a tool, which hints at where related internships sit.

## Lesson 9. How code is released varies, and openness is not universal
**Pattern.** Most catalog projects are on GitHub under ORNL or project orgs with UT-Battelle copyright and a DOE CODE record, but some stay licensed or closed.
- Open with DOE CODE records: DataFed, Thermochimica, GridKit, Myna and others. [KNOWN: map link 55]
- Licensed or closed: SCALE needs a license; AutoBEM software is closed source while its Model America dataset is free. [KNOWN: map links 63, 85, 98]
- OSTI-only stubs: several cyber tools exist only as OSTI records with no public code. [KNOWN: map link 84]
- Metadata can disagree: QIR-EE's OSTI license differs from the repo. [KNOWN: map gaps section]

**Tag:** [INFERRED, medium].
**For a student:** an OSTI record without code is a dead end for contributing; GitHub repos with a LICENSE are the usable ones.

## Lesson 10. Good to learn from, harder to join (draft)
**Pattern.** Most catalog repos are open to read, but fewer than half show a contributor guide, and none of the briefs that checked found open "good first issue" labels. So they are easier to study than to join as a newcomer.
- Contributor guides: of 46 catalog repos on GitHub read on 2026-10-24 (one unauthenticated root contents read each; ExaGO was rate-limited and is not counted), 16 have a root CONTRIBUTING file (for example [HydraGNN](../projects/hydragnn.md), [GridKit](../projects/gridkit.md), [Myna](../projects/myna.md), [Cabana](../projects/cabana.md), [data-workflow](../projects/data-workflow.md)), and [Mantid](../projects/mantid.md) keeps one under `.github/`, so 17 of 46. The other 29 show none at the root; `.github/` folders were not opened, so a few more guides may exist there. [KNOWN: GitHub contents API; mantid brief]
- Beginner issues: the seven briefs that checked labels ([Mantid](../projects/mantid.md), [SNAPRed](../projects/snapred.md), [PyRS](../projects/pyrs.md), [data-workflow](../projects/data-workflow.md), [post-processing-agent](../projects/post-processing-agent.md), [live-data-server](../projects/live-data-server.md), [KORC](../projects/korc.md)) found no open good-first-issue labels. Other repos were not checked. [KNOWN for those seven]
- Some repos without a guide still have developer docs, such as SNAPRed's developer section and PyRS's docs/developer folder. [KNOWN: briefs]

**Tag:** [INFERRED, medium] for "hard to join"; counts are KNOWN as of the read date.
**For a student:** start by reading and building, and pick repos with a CONTRIBUTING file and active issues if you want to send a first change.

## Open questions worth investigating
- Did the 2021-2024 neutron pipeline revival follow a funding or facility event? No public record found yet. [UNKNOWN]
- Does the Test Harness activity line up with other machine acceptances beyond Frontier? [UNKNOWN]
- What is Stork, who publishes it, and is it part of the AM handoff chain? [UNKNOWN: map link 174]
- Is ORNL/ExaGO officially the continuation of the PNNL repo? [UNKNOWN beyond LICENSE wording]
- Which DOE program funds tools whose records say only "USDOE"? [UNKNOWN]
- How do ExaTN and XACC citers use them: as running code or as references? [UNKNOWN]
- How are projects retired? Only LandScan HD/USA have an explicit "no longer actively updated" statement (map link 102). [UNKNOWN for code projects]
- Do the 29 repos without a root CONTRIBUTING file keep one under `.github/`, and do any repos beyond the seven checked carry good-first-issue labels? [UNKNOWN]
