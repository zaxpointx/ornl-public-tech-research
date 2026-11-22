# Deep dive: Y-12's cyber program from the outside

Independent research, not affiliated with Y-12, CNS or NNSA. Public oversight documents only. Findings are reported at the level the documents state them; nothing is added or guessed. People by role only. Last checked: 2026-11-22.

## The short answer
Y-12 publishes almost nothing about its own cybersecurity, but its overseers do. Read together, 18 years of public records tell a consistent story: **a high-security site whose physical and cyber security has been repeatedly audited, an enterprise that GAO says was slow to manage risk in factory equipment (operational technology, OT), and a contractor that by FY 2025 was building a modern program (risk management framework, threat intelligence, vulnerability assessment, zero trust) but still struggling to build security into new systems.** [INFERRED from the timeline below]

**Key takeaway:** the public can see the *shape* of Y-12 cyber (teams, priorities, grades), never the *content* (systems, findings, vulnerabilities). That boundary is correct and this page stays inside it.

## Timeline

| Date | Event | What the public record says | Source |
|---|---|---|---|
| 2006-10 to 2008-01 | Unauthorized laptops | An ORNL contractor employee brought an unclassified laptop into a Y-12 Limited Area; Y-12 cyber staff did not secure it as evidence; the report to DOE headquarters came six days later instead of within 32 hours; up to 37 more ORNL laptops may have been brought in over prior years. DOE's Cyber-Forensic Laboratory examined all 38 laptops: no classified information, 26 had wireless capability, and a majority contained malware (the report notes malware ranges from benign to harmful). | KNOWN: [S11](../source-ledger.md#s11) |
| 2012-05 | DOE independent oversight inspection of Y-12's classified cyber program | Title only is public. | KNOWN: [S10](../source-ledger.md#s10) |
| 2012-07 / 2012-08 | Physical break-in at the uranium storage facility; IG special report | "Multiple system failures on several levels", including unmaintained security equipment and weak contractor governance. Physical, not cyber, but it reshaped security oversight. | KNOWN: [S12](../source-ledger.md#s12) |
| 2014-07 | CNS takes over Y-12 (and Pantex) | New operator. | KNOWN: [S1](../source-ledger.md#s1) |
| 2015-07 | DOE review of Y-12's unclassified cyber program | Title only. | KNOWN: [S10](../source-ledger.md#s10) |
| 2018-01 | DOE assessment of Y-12 unclassified and classified cyber programs | Title only. | KNOWN: [S10](../source-ledger.md#s10) |
| 2019 | CNS stands up the NOC/SOC; IBCI cyber range work with Los Alamos | 24/7 monitoring, 14 people by 2022. | KNOWN: [S16](../source-ledger.md#s16), [S33](../source-ledger.md#s33) |
| 2022-09 | GAO-22-104195 | NNSA and its contractors had not fully put in place six foundational cyber risk practices; in the OT environment NNSA had implemented none yet; subcontractor cyber oversight was inconsistent. Enterprise-wide, not Y-12-specific. | KNOWN: [S13](../source-ledger.md#s13) |
| 2023-06 | GAO-23-106309 | NNSA estimated there could be "hundreds of thousands" of OT systems across its sites; inventory and risk assessment still "very early"; each site assessed a single OT system as a learning exercise. | KNOWN: [S14](../source-ledger.md#s14) |
| 2024-04 | Y-12 Field Office created | Dedicated federal oversight for Y-12. | KNOWN: [S4](../source-ledger.md#s4) |
| 2024-09 | NNSA revises Supplemental Directive 205.1 | Contractors must flow cyber requirements down to subcontractors (closing a GAO recommendation). | KNOWN: [S13](../source-ledger.md#s13) |
| FY 2025 | NNSA report card on CNS | 30 of 33 IT implementation factors met (misses: IPv6, Energy Hub Access, data loss prevention); AI management and limited NNSA federated access done early; more work needed on endpoint detection and response, an enterprise secure network hub, OneNNSAccess and zero trust; cyber met expectations with self-assessments and maturity plans for a risk management framework (RMF) and vulnerability management; Cyber Threat Integration Team and Cyber Vulnerability Assessment Team maturing; **"integration of cybersecurity into organizational system development continues to be a challenge"**; inconsistent authorization packages delayed some systems. Classified Wi-Fi (CSfC) pilot completed. Goal 4 rated Very Good. | KNOWN: [S8](../source-ledger.md#s8) |
| FY 2026 | NNSA performance plan | Objective 4.5 asks for secure IT **and OT** systems and execution of NNSA's IT and cybersecurity program guidance. | KNOWN-from-search-result: [S9](../source-ledger.md#s9) |
| 2026-07 | DOE independent assessment of Y-12 classified and unclassified cyber programs | Title only. | KNOWN: [S10](../source-ledger.md#s10) |
| FY 2027 request | NNSA budget | Enterprise IT and Cybersecurity line: $935M requested vs $688M enacted in FY 2026 (+36%). Y-12 site total requested: about $2.55B. | KNOWN: [S15](../source-ledger.md#s15) |
| 2026-11 | Hiring | NOC/SOC analysts posted for Oak Ridge; other cyber titles (vulnerability analyst, cybersecurity AI engineer, software developer) seen in search results. | KNOWN: [S24](../source-ledger.md#s24); KNOWN-from-search-result: [S25](../source-ledger.md#s25) |

## What the record suggests (interpretation)
1. **Cyber at Y-12 is compliance-driven and enterprise-driven.** The vocabulary is NNSA's: program execution guidance, RMF, authorization packages, zero trust, OneNNSAccess. Y-12 implements enterprise initiatives more than it invents tools. [INFERRED]
2. **OT is the frontier.** GAO flagged OT as the weakest area enterprise-wide; the FY 2025 report card mentions Operational Technology Assessments and the FY 2026 plan adds OT to the IT objective; a 2026 job post (seen in search results) asks for NIST SP 800-82 OT security experience. [KNOWN: S13, S14, S8, S9, S25; INFERRED: "frontier"]
3. **AI is arriving on both sides.** AI management milestones, a Bernie AI pilot, and a "Cybersecurity AI Engineer" posting appear within about a year. [KNOWN: S8, S25; INFERRED: trend]
4. **"Secure by design" is the stated weak spot.** The report card's own words say building security into system development is still hard. That is a software engineering problem as much as a cyber one. [KNOWN: S8; INFERRED: framing]

## What the record cannot tell us
- Any specific finding, vulnerability, system or tool. The four DOE cyber assessment reports are not public, and that is correct. [KNOWN: S10]
- How many people work in cyber at Y-12. UNKNOWN.
- Whether any Y-12 cyber tool exists in code form. None found (see [signals](../signals.md)).

## For Cayden
Read GAO-22-104195's six practices and NIST SP 800-82 together: they are the public "syllabus" for what Y-12 and its peers are being graded on. See [learn and build](../learn-and-build.md).
