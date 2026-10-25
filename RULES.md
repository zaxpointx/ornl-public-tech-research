# ORNL Public Technology Research: Team Rules

Repository root: this repository.
Coordination: an editor assigns batches and makes scope and status decisions; those are recorded as editorial decisions.

## Hard rules
1. Public information only: ornl.gov, osti.gov, energy.gov, public GitHub/GitLab orgs (e.g. github.com/ORNL and lab-affiliated orgs), public papers, public docs sites. Never log in, never bypass access controls, never touch anything marked restricted, CUI, export-controlled, or internal.
2. No copying copyrighted content. Summarize in your own words. Short quotes (under ~25 words) only when essential, always cited. Record licenses of repos as stated.
3. Never claim or imply ORNL affiliation. We are independent researchers. Do not contact ORNL staff.
4. Every claim gets a confidence tag:
   - [KNOWN] stated directly in a cited official/primary source (URL + date accessed)
   - [INFERRED] reasoned from sources but not stated outright (say what it's inferred from)
   - [UNKNOWN] open question we couldn't answer
5. Cite URLs for everything. Prefer primary sources (official pages, repo READMEs, docs, OSTI records) over news.
6. Save progress as you go. Never hold work only in chat.

## Layout
- discovery/catalog.csv        master list of projects (id,name,url,repo_url,org_unit,domain,status,discovered_batch,notes)
- projects/<project-id>.md     one plain-English brief per project (template below)
- verification/log.md          source checks: claim, source, verdict (verified/corrected/unverifiable)
- connections/map.md           how projects relate (shared code, shared facility, same group, dependencies)
- batches/batch-NN.md          per-batch summary: researched, verified, next
- INDEX.md                     curated entry point, kept current by the editor

## Project brief template (projects/<id>.md)
# <Name>
- Official page / Repo / Docs / License / Status (active, archived, unknown, stub-osti-only, draft-osti-only)
## What it is (plain English, 2-4 sentences)
## How it works (plain English, no jargon without definition)
## How the project is organized (repo structure, languages, build, maintainers/org unit, release cadence)
## Who uses it / why it matters
## Related projects
## Known / Inferred / Unknown
## Sources (URL, accessed date)

## Added 2026-10-24: evidence rules adapted from Cayden's deep-public-project-reconstruction skill
7. Two more tags join the three above:
   - [CORROBORATED] KNOWN and also confirmed by a second independent public source (cite both).
   - [UNRELATED] checked and found not to be part of the project (say what was checked). Use it to stop namesake mixups.
8. Load-bearing claims (ownership, funding, maturity, dependencies, licenses) record: URL, title, publisher, date, accessed date, the exact short quote (under 25 words) and page/section. A search snippet is never final evidence; fetch the page.
9. Searched-but-not-found ledger: verification/not-found.md. Log every search that came up empty (query, where, date). A failed search is bounded negative evidence, not proof something doesn't exist.
10. Keep the source's maturity verb: studied, designed, prototyped, tested, evaluated, deployed, operated. Never upgrade tested or deployed to "production" without a source saying so. Don't merge two projects, tools, or people without explicit binding evidence.
11. Two sweeps per batch. Sweep 1 is the normal pipeline. Sweep 2 (the fact-check pass, before the batch is called verified): re-read every brief and map link in the batch, re-fetch load-bearing sources, look for disconfirming evidence, fix overstatements, and log what changed.
12. Every brief opens with a plain-language walkthrough: what it is, the problem, what goes in, what happens, what comes out, where humans act, what it is not, what's unknown. One concrete example.

## Deep dives (deep-dives/<id>/)
For a few high-value projects, run the full reconstruction: executive synthesis, timeline by stage, system/data-flow map, people-and-roles (conservative: authorship proves participation, not ownership), source ledger, missing-artifacts ledger, claim-boundary ledger, and a verification report. State what's well understood, inferred, unknown, searched without result, and whether more public research would change the core answer.

## Catalog scope and status (added 2026-10-24, editorial decision)
13. Scope: a project stays in discovery/catalog.csv only if a primary source names ORNL as research org, copyright holder, repo owner, or a named contributing lab. Projects ORNL work depends on or ties to without that evidence go in connections/map.md as outside projects, not the catalog. (Applied 2026-10-24: exaca and fates moved to the map; adamantine stays on OSTI 2472702; e3sm-elm stays on ORNL's named ELM work.)
14. Status values: active, archived (only when GitHub flags the repo archived), unknown, stub-osti-only, draft-osti-only. stub-osti-only means the only public source is an OSTI record, with no public repo or docs page. A stub gets a brief only once a public docs page (including a public dataset landing page) exists for it. draft-osti-only means a brief was written from OSTI sources alone; it is kept but listed separately in INDEX and is not a full brief.

## Outside-in signals (added 2026-10-24, editorial decision)
15. Besides reading what a project says about itself, read the public traces it leaves, the way an analyst works out what a team is doing from the outside. Allowed signals: git history (commit cadence, contributor churn, CI configs and build flags that show which supercomputers or GPUs it targets, open/closed issues), reverse dependencies (who depends on it on PyPI, conda-forge, Spack, GitHub "used by"), package download counts, Wayback Machine snapshots (what was announced, renamed, or quietly removed), citing papers, public funding records (OSTI sponsor fields, LDRD reports, SBIR/award notices), public tech-transfer and license listings, and public job postings by project or team name only. Each signal finding gets a tag and a source like any claim, and the reasoning from signal to conclusion is written out (signal, what it suggests, how confident).
16. Hard limits on outside-in work: study artifacts, never systems. No scanning, probing, subdomain or DNS enumeration, port or service mapping, login-page discovery, or anything that maps ORNL networks or infrastructure. No profiling of individual people beyond public credit lines already allowed (no personal accounts, locations, or social media). No attempts to infer classified, export-controlled, or restricted work, and no speculation about what is hidden in non-public repos. If a signal points toward any of that, stop and log it as out of scope. Only follow links that a public page actually shows; never guess or try paths on ORNL hosts (for example `/release-notes`), since that counts as probing even when harmless. Job postings count only from official jobs boards, never social posts. [editorial decision 2026-10-24]
Outputs go in signals/<project-id>.md, using the same tags and a short "what the outside tells us that the inside doesn't" section at the top.
17. From batch 06 on, every project gets signals/<project-id>.md under items 15-16: the discovery pass writes the history, CI and funding section first, then the connections pass writes the usage section below it. The fact-check pass spot-checks at least one of the discovery-pass commit counts against a fresh clone when time allows. [editorial decision 2026-10-24]
