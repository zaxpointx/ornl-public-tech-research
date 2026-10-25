# Cyberwheel
- Official page: none separate from the repo [KNOWN: GitHub API homepage empty]
- Repo: https://github.com/ORNL/cyberwheel
- Docs: README, plus `cyberwheel/emulator/README.md` for emulation setup [KNOWN: README]
- License: MIT, copyright 2024 an individual developer (named in the LICENSE) [KNOWN: LICENSE file, https://github.com/ORNL/cyberwheel/blob/main/LICENSE]
- Status: borderline active. Last push 2025-08-26, about 14 months before this brief [KNOWN: GitHub API; "borderline" INFERRED]

## What it is (plain English, 2-4 sentences)
Cyberwheel is a training ground for AI cyber defenders. It simulates a computer network where an attacker ("red" agent) tries to break in and a defender ("blue" agent) tries to stop it, and AI agents learn by playing that game over and over [KNOWN: README]. The learning method is reinforcement learning (RL). An agent tries actions, gets a reward or penalty, and slowly figures out what works, the same idea used to train game-playing AIs [KNOWN: README says RL; explanation general background]. The goal is autonomous cyber defense, meaning software that can respond to attacks without a human clicking every button [KNOWN: README].

## How it works (plain English, no jargon without definition)
- You describe a network in config files: hosts (computers), subnets (groups of hosts), services running on them, and decoy hosts (fake machines meant to lure attackers, also called honeypots) [KNOWN: data/configs folders host_definitions, network, services, decoy_hosts].
- Red agents follow attack "killchains", the step-by-step stages of an attack like scanning, breaking in, then moving to other machines [KNOWN: README mentions killchains; definition general background]. Blue agents take defensive actions, and detectors model the alerts a defender would see [KNOWN: red_actions, blue_actions, detectors folders].
- A reward module scores each step, and that score is what the RL agent learns from [KNOWN: reward folder; role INFERRED].
- Version 2.0 (August 2025) added three things. Both red and blue can be AI agents that learn against each other. One agent can train across many different networks (small up to 100 hosts, medium 1,000, large 10,000). And there's an "emulation" mode using Sandia National Labs' FIREWHEEL tool, which emulates the network instead of purely simulating it [KNOWN: README]. ORNL's FY2025 LDRD completed-projects report says the emulation uses a modified Firewheel, which it describes as built on QEMU (a machine emulator) and able to stand up networks of virtual nodes, so the emulation mode does run virtual machines [KNOWN: https://www.osti.gov/servlets/purl/3025007, accessed 2026-10-24].
- It's built on Gym, the standard interface for RL environments. It logs to Weights & Biases (an experiment tracker) and has a Dash web app that shows each episode as a network graph [KNOWN: README "Built With" and About].

## How the project is organized (repo structure, languages, build, maintainers/org unit, release cadence)
- Languages: about 99% Python [KNOWN: GitHub languages API]. Requires Python 3.10 [KNOWN: README].
- `cyberwheel/` package: `cyberwheel_envs` (the RL environments), `network`, `red_agents`/`red_actions`, `blue_agents`/`blue_actions`, `detectors`, `observation` (what the agent "sees"), `reward`, `runners` (training and evaluation entry points), `emulator`, `data/configs`, `tests`, `utils`, and `legacy` [KNOWN: repo tree].
- Build: Poetry, a Python dependency manager (`pyproject.toml`, `poetry.lock`), plus requirements.txt. Graphviz is needed for visualization [KNOWN: README].
- The README's roadmap lists unit tests and detailed documentation as still to do [KNOWN: README "Next Steps"].
- Contributors: about 8 per the GitHub API, counting anonymous ones [KNOWN: contributors pagination]. The README lists six contacts with ornl.gov emails [KNOWN: README Contacts]. Names were left out of this brief on purpose, see the README.
- Releases: v1.0.0 (tag only), v1.1.0 (2025-03-10) and v2.0 (2025-08-11) [KNOWN: GitHub releases and tags API]. The repo was created 2024-07-08 [KNOWN].
- Org unit: [UNKNOWN].
- DOE CODE record code-134699 (2024) and the 2024 conference paper (OSTI 2478356) both list ORNL as research org [KNOWN: https://www.osti.gov/api/v1/records?q=cyberwheel, accessed 2026-10-24]. ORNL's FY2025 LDRD Completed Projects report names Cyberwheel as the test bed for project 11049, "Automating Cyber Defense Using Reinforcement Learning" (Director's R&D Program, AI area), so it was developed under ORNL's internal LDRD program [KNOWN: https://www.osti.gov/servlets/purl/3025007, accessed 2026-10-24].
- Papers: "Towards a High Fidelity Training Environment for Autonomous Cyber Defense Agents" (2024, https://doi.org/10.1145/3675741.3675752) and "The Path to Autonomous Cyber Defense" (2024, https://arxiv.org/pdf/2404.10788.pdf) [KNOWN: README Papers section; papers themselves not read this pass].

## Who uses it / why it matters
- Researchers building AI that can defend networks at machine speed [KNOWN: README purpose].
- For a cybersecurity student it's a good hands-on way to learn red/blue team concepts, attack killchains, honeypots and RL together. It's Python only and MIT licensed, so it's easy to fork and experiment with [INFERRED].
- Named users: [UNKNOWN].

## Related projects
- Uses FIREWHEEL (Sandia National Laboratories) for emulation [KNOWN: README].
- No direct links to other catalog projects found [INFERRED]. It's the only cyber entry in batch 1.

## Known / Inferred / Unknown
- [KNOWN] MIT, Python 3.10/Poetry, red vs. blue RL, v2.0 features, FIREWHEEL emulation, two linked 2024 papers.
- [INFERRED] Development has slowed since August 2025, and it's a good fit for student learning.
- [UNKNOWN] Owning division, funding, and whether development is continuing.

## Sources (URL, accessed date)
- https://github.com/ORNL/cyberwheel (README, LICENSE, tree), accessed 2026-10-24
- https://api.github.com/repos/ORNL/cyberwheel (+ /languages, /releases, /tags, /contributors), accessed 2026-10-24
- https://doi.org/10.1145/3675741.3675752 and https://arxiv.org/pdf/2404.10788.pdf, linked from the README, not opened

## Fact-check notes (ORNL Fact Checker, 2026-10-24)
- Retagged: "real virtual machines" isn't in the README; split into KNOWN emulation + INFERRED VMs.
- Added: DOE CODE code-134699 and OSTI 2478356 confirm ORNL; possible LDRD funding (INFERRED).
- Verified: MIT (2024 an individual developer (named in the LICENSE)), v2.0 multi-agent/multi-network (100/1,000/10,000 hosts)/FIREWHEEL, Python 3.10 + Poetry + Graphviz, Gym/W&B/Dash, Next Steps list, tags v1.0.0/v1.1.0/v2.0, six ornl.gov contacts, arXiv 2404.10788 title. ACM DOI returned 403 (publisher block), paper confirmed through OSTI.
- Unverifiable: owning division and whether development continues.
- No restricted content or implied ORNL affiliation found; contact names correctly left out.
- Update (map.md spot-check, 2026-10-24): read the LDRD report itself. LDRD funding and QEMU-based virtual machines in emulation mode both retagged KNOWN.
