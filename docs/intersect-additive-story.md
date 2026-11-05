# A print, a simulation and a neutron measurement

This independent public-source story compares three related but distinct pieces of research. It is not a facility operations guide. The [evidence ledger](public-research-sources.md#intersect-additive-research-batch) gives public URLs, quotes, fetch dates, maturity and unknowns. A source's own statement is [KNOWN]; a bounded comparison is [INFERRED]; [UNKNOWN] means the connection has not been established.

## The question

Metal can retain stress after it is printed. The INTERSECT autonomous additive manufacturing example aims to use observations and simulation to guide printing and improve the resulting stress distribution. Its architecture describes a research workflow across the Manufacturing Demonstration Facility (MDF), the Spallation Neutron Source (SNS) and the Oak Ridge Leadership Computing Facility (OLCF), and reports that the workflow was deployed across those facilities [KNOWN: S05, S06]. The stated aim of parts that are ready to use immediately is not itself evidence of completed safety qualification [KNOWN: S06].

The public architecture identifies two loops. One uses temperature measurements and a simulation to inform the next printed layer. The other uses neutron and imaging measurements to help validate the structural simulation and adapt the next part [KNOWN: S07]. These are documented design patterns; which specific components and facilities participated in each real-world run remains [UNKNOWN]. The architecture's “two times closer” residual-stress improvement is a target, not a reported measurement [KNOWN: S06].

## A related neutron result, without inventing the link

In 2023, Plotkowski and colleagues used neutron diffraction during additive manufacturing of a low-temperature-transformation steel; their published abstract combines diffraction, infrared and simulation data to interpret the evolution of strain during phase transformation [KNOWN: H01]. ORNL separately reports that its OpeN-AM platform was designed and built at MDF and used at SNS's VULCAN instrument for that type of steel experiment [KNOWN: S11]. This supports an experiment connecting manufacturing and neutron measurement, not a claim that it achieved the INTERSECT target, was automatically qualified for use, or was the exact architecture deployment above [UNKNOWN: H01, S05, S11].

## A software test with a simulated printer

A November 2025 peer-reviewed conference paper reports a cross-facility additive-manufacturing research prototype involving INTERSECT, [adamantine](../projects/adamantine.md), and [Flowcept](../projects/flowcept.md) [KNOWN: H02]. In the authors' described demonstration, the printer and measurement-service components were simulated; the paper also describes use of computing resources for simulations and Flowcept for recording provenance—information about what happened in a workflow [KNOWN: H02]. It is a meaningful test of software coordination, not proof that this agent-augmented demonstration controlled a real printer or that it used SNS. The relationship of this particular test to the complete three-facility deployment is [UNKNOWN: H02, S05].

The paper's authors include Daniel Rosendo and Stephen DeWitt [KNOWN: H03]. Separately, the INTERSECT architecture documentation identifies DeWitt as principal investigator for the additive manufacturing project [KNOWN: S06]. Authorship of the software paper alone does not establish leadership of every project. The paper's named use of adamantine and Flowcept corrects a broader earlier gap about whether these tools have a documented connection to INTERSECT additive research; it does **not** establish their use in every INTERSECT workflow or the OpeN-AM experiment [KNOWN: H02; UNKNOWN: H01, S05, S11]. The existing [Myna](../projects/myna.md) and [3DThesis](../projects/3dthesis.md) briefs remain related reading; their use in this specific test is [UNKNOWN: H02].

## What can a reader do safely?

Compare the three claims: an architecture and its target; a measured steel experiment; and a simulated-printer software demonstration. They answer different questions. A paper-based sketch using invented data can illustrate a feedback loop, but would not validate a real manufacturing process. Do not access facility services or treat this description as operating instructions. See the [software deep dive](../deep-dives/additive-manufacturing.md) for existing tool research and the [relationship index](research-relationships.md) for explicit unknowns.
