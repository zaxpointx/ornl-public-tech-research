# Y-12 for a cybersecurity student: realistic paths and things to build

Written for Cayden (17, high school junior and cybersecurity student at TCAT, living outside the Oak Ridge area). Independent research, not affiliated with Y-12, CNS or NNSA. Last checked 2026-11-22.

## The short answer
**There is no public Y-12 internship for high school students.** Y-12's summer internships start at college junior standing. [KNOWN: [S22](source-ledger.md#s22)] The realistic doors are (1) the **NOC/SOC analyst** track after TCAT plus certifications and experience, or (2) **college, then a Y-12 summer internship** in IT or software. Either way you'll need to be able to get a DOE **Q clearance**, which requires U.S. citizenship and a background investigation. [KNOWN: [S24](source-ledger.md#s24)] **Key takeaway: build the skills the NOC/SOC post lists, now, and document them publicly.** [INFERRED: advice]

## Paths, from soonest to latest

| Path | Who it's for | Requirements (public) | Fit for you now | Tag |
|---|---|---|---|---|
| Y-12-sponsored cyber camps with Roane State | Middle and high school students | Ran in 2020 (virtual, 30 students; digital forensics, scanning and recon exercises on fictional cases) | Unknown if still offered; worth asking Roane State | KNOWN: [S19](source-ledger.md#s19), [S20](source-ledger.md#s20); UNKNOWN: current |
| CNS cyber outreach to high school classes | High school cyber classes | CNS's chief information security officer spoke (virtually) to a local high school cybersecurity class in 2020 | Your teacher could ask CNS education outreach | KNOWN: [S18](source-ledger.md#s18); INFERRED: could be asked |
| ORNL NGSI (not Y-12) | HS juniors and seniors | Eligible counties listed are Anderson, Blount, Campbell, Knox, Loudon, McMinn, Monroe, Morgan, Roane, Sevier | Only if your county is on the list; yours isn't (as you found) | KNOWN-from-search-result: [S50](source-ledger.md#s50) |
| NOC/SOC analyst (Oak Ridge) | Entry-level IT/cyber | Bachelor's **or 8+ years of relevant education, training and/or experience**; Q clearance; 12-hour rotating shifts; on site; Network+, Security+, Splunk preferred | Real target after TCAT plus experience; the 8-year rule may count TCAT training plus work, but how CNS counts it is UNKNOWN | KNOWN: [S24](source-ledger.md#s24) |
| Y-12 summer intern | College students | Junior standing or higher; GPA 2.8 on the current page (an older recruiting page says 3.0); 10 weeks, 40 h/week; postings go up in October for the next summer | After 2 to 3 years of college | KNOWN: [S22](source-ledger.md#s22), [S23](source-ledger.md#s23) |
| NNSA MSIIP | Students at Minority Serving Institutions | 18+, U.S. citizen, GPA 3.0, 12-week summer or yearlong; places students at NNSA sites | Only if you attend an MSI | KNOWN: [S49](source-ledger.md#s49) |
| Roane State programs near Y-12 | Post-high school | Computer Information Technology program (ran the cyber camps); Nuclear Technology and Chemical Engineering Technology programs feed Y-12 operations jobs | Possible bridge if you move toward Oak Ridge | KNOWN: [S19](source-ledger.md#s19), [S45](source-ledger.md#s45) |
| Trades (for comparison) | TCAT graduates | TCAT Knoxville welding graduates have joined Y-12's UPF project as union apprentices | Shows CNS hires from TCATs; for trades, not cyber | KNOWN: [S46](source-ledger.md#s46) |

Commute: from outside the Oak Ridge area, plan for a long drive each way, which matters for 12-hour shift work. [INFERRED]

## What to study (all public)
- **NIST SP 800-82 Rev. 3, OT security.** The cyber AI job post names it. https://csrc.nist.gov/pubs/sp/800/82/r3/final [KNOWN: link checked]
- **NIST SP 800-171 Rev. 3.** What small defense suppliers must protect; the IBCI project was built around it. https://csrc.nist.gov/pubs/sp/800/171/r3/final [KNOWN: link checked; IBCI link from [S33](source-ledger.md#s33)]
- **GAO-22-104195's six foundational practices.** A one-page summary of how NNSA sites are graded. [S13](source-ledger.md#s13)
- **NSA Commercial Solutions for Classified (CSfC).** Public capability packages behind the Wi-Fi pilot. https://www.nsa.gov/Resources/Commercial-Solutions-for-Classified-Program/ (returned 403 to our automated check; open it in a normal browser)
- **The NOC/SOC tool list:** SIEM (Splunk free tier), Snort or Suricata IDS, packet capture (Wireshark), Linux and Windows admin, scripting.

## Projects you can build (own machines and VMs only)

Ground rules: your own machines, VMs or lab hardware only; never scan or touch systems you don't own; no malware; no real industrial equipment you don't own.

| # | Project | Inspired by | What you learn | Size |
|---|---|---|---|---|
| 1 | **Home SOC in a box:** Security Onion or Wazuh plus Splunk Free on a VM, feed it logs from your own machines, write 10 detection rules and a short incident report for each | [NOC/SOC](briefs/noc-soc.md) | Exactly the skills in the job post | 2 to 4 weekends |
| 2 | **G-code integrity checker:** a small CLI that hashes CNC part-program files, signs them, and refuses to "load" a file whose hash changed; add a tamper demo | [IBCI student project](briefs/ibci-mtews.md) | Hashing, signing, integrity in OT | 1 weekend |
| 3 | **Mini manufacturing cyber range:** OpenPLC (https://github.com/thiagoralves/OpenPLC_v3) plus a Modbus simulator in isolated VMs; capture normal traffic, then detect a bad write with Suricata rules; score the network with your own simple risk index | [MTEWS](briefs/ibci-mtews.md), [IIoT report](briefs/iiot-risk-report.md) | OT protocols, segmentation, detection | 3 to 5 weekends |
| 4 | **Run CISA's CSET on your home lab:** the free, MIT-licensed Cybersecurity Evaluation Tool (https://github.com/cisagov/cset) that the IBCI report mentions; write up your gaps against 800-171 | [IBCI](briefs/ibci-mtews.md) | Compliance assessment, the language NNSA uses | 1 weekend |
| 5 | **Predictive-maintenance digital twin:** stream a public bearing-vibration dataset over MQTT (Mosquitto), train a Random Forest to flag failures, show it on a web dashboard; stretch goal, a Unity view | [Digital twin + LLM](briefs/digital-twin-llm-maintenance.md) | MQTT, ML, dashboards; then threat-model it (who could spoof the sensors?) | 3 to 4 weekends |
| 6 | **Offline LLM maintenance-planner:** a local model with retrieval over made-up maintenance records that drafts a work package, with no internet connection | [LLM planning paper](briefs/digital-twin-llm-maintenance.md), [Bernie](briefs/bernie-ai-pilot.md) | RAG, agents, running AI air-gapped | 2 to 3 weekends |
| 7 | **Readiness tracker web app:** RCAPTS-style checklist app with roles, approvals, evidence uploads and an audit log; then run a secure-code review on it | [RCAPTS](briefs/rcapts.md) | Secure-by-design web development, the "weak spot" in the FY 2025 report card | 3 to 4 weekends |

**Best two to start:** #1 (direct match to the NOC/SOC job) and #2 (small, unusual, and easy to explain in an interview). [INFERRED: advice]

## How to talk about this honestly
- Say you studied Y-12's **public** record. Don't claim insider knowledge or affiliation.
- Don't speculate about what Y-12 runs internally. "The public report card says X" is fine; "they probably use Y" is not.
