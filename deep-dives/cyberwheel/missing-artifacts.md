# Cyberwheel deep dive: missing artifacts
Written in the fact-check pass, 2026-10-24. These are things we looked for in public sources and didn't find. Every item is also logged in verification/not-found.md. Per rule 16, we don't guess at anything non-public.

| # | Missing artifact | Where we looked | Effect on claims |
|---|---|---|---|
| M1 | Contract or LDRD project number on the software or paper records | code-134699, OSTI 2478356 | 11049 stays KNOWN from one source (OSTI 3025007) |
| M2 | What was "modified" in Firewheel | OSTI 3025007 p.13, v2.0 notes, lineage sources | Stays INFERRED (lineage C3). Don't say "fork" |
| M3 | Any statement that Cyberwheel was deployed, operational or in production | Report, repo, releases, OSTI records | Keep the source verbs (developed, showed, study) |
| M4 | Owning division or group | DOE CODE, OSTI, repo | UNKNOWN. Don't infer it from author names |
| M5 | Funding amount and start date | OSTI 3025007 | Not stated |
| M6 | FY2026 follow-on or successor | OSTI search; 3827147 is only adjacent | Don't claim it either way |
| M7 | Affiliations of the authors who use Cyberwheel (S7, S8) | Abstracts only | "Outside use" stays UNKNOWN |
| M8 | Full text of the 29 citing papers whose abstracts don't name Cyberwheel | Not read | Citations aren't adoption |
| M9 | Atomic Red Team version | Repo code | UNKNOWN |
| M10 | Any results from a Cyberwheel experiment at 100,000-node scale | OSTI 3025007 | That figure is Firewheel's capacity only |
| M11 | An archive notice or deprecation statement | Repo (not archived), releases | Quiet since 2025-08-26 is a fact. "Dead" is not |
