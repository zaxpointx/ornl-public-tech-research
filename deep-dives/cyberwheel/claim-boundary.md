# Cyberwheel deep dive: claim boundary
Owner: ORNL Reader. Written 2026-10-24. This page separates three things: what public sources actually say, what we infer from them, and what nobody has said. Use it before repeating any Cyberwheel claim outside this repo. Every row points to the source already cited in synthesis.md, timeline.md or system-flow.md. Fact Checker's ledgers and verification report in this folder are the final word if anything here conflicts with them.

## How to read this
- **Source says**: a primary source states it. You can repeat it, citing that source and keeping its wording.
- **We infer**: our reasoning from the sources. Say "appears to" or "likely". Don't present it as fact.
- **Nobody says**: we looked and found nothing, so don't claim it either way.
- **Don't say**: wording that goes beyond the evidence. These are easy mistakes to make.

## Ledger

| # | Topic | Source says | We infer | Nobody says / don't say |
|---|---|---|---|---|
| 1 | What it is | A "custom-built, realistic network test bed environment called Cyberwheel" for training RL cyber-defense agents. [KNOWN: OSTI 3025007 p.13] | | Don't call it a product, a tool ORNL uses to defend its own network, or a deployed system. |
| 2 | Maturity | v1.1.0 red agent "trained and tested on an inactive blue agent" [KNOWN: release notes]. LDRD text uses "developed", "showed", "study". [KNOWN: OSTI 3025007 p.13] | It's a research environment. | No source says "deployed", "production" or "operational" (logged in not-found.md). Don't upgrade the wording (rule 10). |
| 3 | Results | Agents could "autonomously deploy decoys in unseen network topologies that delay or deny adversarial actors", and agents trained in simulation could be moved to emulation. [KNOWN: OSTI 3025007 p.13] | | The "deploy" there means the agent places decoys inside the test network, not that Cyberwheel was deployed. No public numbers on how well this worked outside the papers. Don't say "stops attackers". |
| 4 | Funding | LDRD-funded. [CORROBORATED: OSTI 3025007 p.13 + DOE CODE code-134699 sponsor field] Project number 11049. [KNOWN, single source: OSTI 3025007] | "Internal" research, since LDRD is lab-directed. [INFERRED] | Funding amount, start date and contract number: not stated. |
| 5 | Institution | ORNL is the research org on DOE CODE code-134699 and OSTI 2478356; repo lives under github.com/ORNL. [KNOWN] | | Owning division or group: UNKNOWN. Don't guess one from author names. |
| 6 | People | Names appear as authors/credits on public records (see people-roles.md). [KNOWN] | | Who the PI or lead is: UNKNOWN. Authorship shows participation, not ownership or leadership. |
| 7 | Emulation | v2.0 "now supports emulation with FIREWHEEL", which Sandia researchers developed [KNOWN: v2.0 release notes]. The LDRD report calls it "a modified version of the Firewheel test bed" and "an experimental platform built on QEMU" [KNOWN: OSTI 3025007 p.13 only; the release notes don't say "modified"]. | "Modified" probably means Cyberwheel adds its own components rather than forking Firewheel. [INFERRED: Connector, lineage.md] | What exactly was modified: not stated. Don't say "fork". |
| 8 | Scale | The report describes FIREWHEEL as allowing "instantiation of networks with over 100,000 virtual nodes". [KNOWN, single source: OSTI 3025007 p.13; see lineage.md F9] | | That number describes Firewheel's capacity, not a Cyberwheel experiment. Don't say Cyberwheel trained agents on 100,000-node networks. |
| 9 | Attack content | Code docstrings name Atomic Red Team as the source of attack techniques. [KNOWN: repo code] | | Which ART version: UNKNOWN. |
| 10 | Activity | Last commit 2025-08-26; LDRD 11049 listed as completed in FY2025. [KNOWN: GitHub API; OSTI 3025007] | Development likely stopped when the LDRD ended. [INFERRED from dates] | No source says it's abandoned or archived. Status in the catalog stays what the repo shows, not "dead". |
| 11 | Private before public | First commit 2024-01-02, repo created 2024-07-08. [KNOWN: GitHub API] | Built privately, then published. [INFERRED] | |
| 12 | Outside use | Three papers say in their abstracts that they run or extend Cyberwheel (arXiv 2610.00590, arXiv 2610.00557, Entropy 10.3390/e27060622). [KNOWN, verified by Fact Checker] One more (ISDFS 2025) only describes it. | | Whether those authors are outside ORNL: UNKNOWN. Don't say "adopted by industry" or "used by other labs". 29 other citing abstracts don't name it; they may or may not use it. |
| 13 | Dependencies | README installs with Poetry; requirements.txt is a fallback "If running into issues with poetry". [KNOWN: README] | requirements.txt is stale, exported from an older lock. [INFERRED] | |
| 14 | Follow-on | | | Any FY2026 follow-on project or successor: not found. Don't claim one exists or doesn't. |
| 15 | Security relevance | | It's a training ground for automated defenders, so it sits in the cyber-defense research area. [INFERRED from purpose] | Don't suggest it holds real attack data, ORNL network details or anything sensitive. It's public, simulated and emulated only. |

## Where the boundary is most likely to slip
1. **"Deploy"** appears in the result quote, about decoys. Readers skim it as "Cyberwheel was deployed". Keep rows 2 and 3 apart.
2. **Funding vs. ownership.** LDRD funding plus an ORNL repo doesn't tell us which division owns it.
3. **Citations vs. adoption.** 33 citing papers is not 33 users. Only 3 abstracts show use, and author affiliations aren't checked.
4. **Quiet vs. dead.** No commits since August 2025 is a fact. Calling it abandoned is not.

## Would more public research move the boundary?
Only at the edges. Reading the full citing papers could settle author affiliations (row 12). An FY2026 LDRD report could settle row 14. The core claims (rows 1 to 5) rest on sources that agree, and nothing we could reasonably find would flip them. [INFERRED]

## Fact-check notes (ORNL Fact Checker, 2026-10-24)
- Spot-checked rows 2, 7, 8, 9, 10, 11 and 13 against primary sources. They're all right except row 7. The quote "a modified version" comes only from the LDRD report (p.13). The v2.0 release notes just say it "now supports emulation with FIREWHEEL". I fixed the attribution.
- Row 10: the last commit was 2025-08-26 (22:30 UTC). The report's title is "FY 2025 Completed Projects", and 11049 is listed in it. Verified.
- Row 11: first commit 2024-01-02, repo created 2024-07-08. Verified.
- No conflicts with source-ledger.md or verification-report.md.
