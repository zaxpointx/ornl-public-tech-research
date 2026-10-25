# Goal: how ORNL builds and runs its public technology, seen from the outside

Set by Cayden Wilson, 2026-10-24. Every batch, brief, signals file and deep dive should serve this file. If a piece of work doesn't move one of the end results below, it waits.

## Why this exists

1. **Learning.** One GitHub repository where you can learn from real national-lab projects. It pulls together what is scattered across ornl.gov, GitHub, OSTI and DOE CODE records, technical reports and papers, and explains it in plain English. Nothing here is private. The value is in reconstructing scattered public pieces into one clear picture nobody else has put together.
2. **How ORNL works from the outside.** Lessons on how the lab actually funds, staffs, builds, releases, maintains and retires its software, drawn from the public traces projects leave. These are things people usually only learn by working there.
3. **Ask-anything readiness.** The repo should be organized well enough that Cayden, or an AI agent like Codex or Hermes reading it, can answer almost any question about a project from the files, with sources, and say honestly when something is unknown.
4. **Portfolio.** A public piece that shows how Cayden researches: careful sourcing, honest known/inferred/unknown labels, and OSINT done ethically.
5. **ORNL internship.** Understanding which parts of the lab do work that matches Cayden's skills (cybersecurity, networking, Python, Linux), what skills keep showing up across projects, and where a student could realistically learn or contribute.

## End results (what "done" looks like)

1. **The lab tree** (`LAB-TREE.md`). A top-down map that goes lab, then directorate or division (when a source says so), then research area, then facility or program, then project, then the tools each project uses or feeds. Every branch links to its brief. This is the trunk the rest of the repo hangs from.
2. **Full deep dives** on a handful of high-value projects, in the same format as `deep-dives/cyberwheel/`. Chosen by the ranking below, one at a time.
3. **How ORNL works** (`lessons/how-ornl-works.md`). Patterns seen across many projects, each backed by examples: how projects start (grants, programs, new machines), who pays (DOE offices, other agencies), how code is released (licenses, OSTI records, GitHub orgs), how projects stay alive or go quiet, how facilities like Frontier and SNS shape the software, and how teams hand code from one project to the next.
4. **Question bank** (`lessons/questions.md`). The questions a curious student or interviewer would ask, each answered from the repo with links, or marked unknown.
5. **Internship angle** (`lessons/internship-angle.md`). Which branches of the tree match Cayden's skills, which tools and languages keep recurring, which projects are open to outside contributions (good-first issues, contributor guides) and what a student would need to learn first. Internship programs and deadlines are tracked separately; this file is about the work itself.

## Questions every brief should be able to answer

1. What problem does it solve, and for whom?
2. Where does it sit in the tree: which area, facility or program?
3. Who pays for it, according to public records?
4. How is the code organized, and what languages and tools does it use?
5. Is it alive? What do its commit history and releases say about its life story?
6. Who outside ORNL actually uses or cites it?
7. What does it connect to, upstream and downstream?
8. What does it teach about how ORNL works?
9. Could a student learn from it or contribute to it, and what would they need to know first?
10. What is still unknown, and what was searched without result?

## How to pick the next deep dive

Rank candidates by how well they serve the goals above: they reveal how the lab works, they connect to many other projects, they touch cybersecurity or operations, and there is enough public material to say something real. Current order:

1. **The neutron data pipeline at SNS** (Mantid, ONCat, live-data-server, post-processing-agent, data-workflow). It follows data from the beam to the scientist and shows how a national user facility actually runs its software. It also has the odd revival story from 2021 to 2024.
2. **Supercomputer operations** (OLCF test harness and related tools). How the lab tests and brings up machines like Frontier.
3. **The 3D-printing ladder** (3DThesis, Finch, AdditiveFOAM, ExaCA, Myna, adamantine).
4. **The grid tools** (GridKit, ReSolve, ExaGO).

Cyberwheel is already done.

## Rules that do not change

Everything in `RULES.md` still applies. In particular:

- Public information only. No restricted, private, export-controlled or classified material, and no guessing about it.
- Study artifacts, never systems: no scanning, probing or network mapping.
- No profiling of individual people. Describe roles ("the lead developer", "a credited contributor"), not personal histories. This is stricter than the HIT-HD research, on purpose, because this repo is public.
- No claim of ORNL affiliation, and no copied copyrighted text beyond short cited quotes.
- Every claim is tagged known, corroborated, inferred or unknown, with a source.
