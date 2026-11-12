# Autonomous science: who chooses the next measurement?

This independent public-source account distinguishes a published materials result, a software demonstration, and a chemistry research project. It is not an account of present instrument configuration. Evidence excerpts, source dates, maturity and limitations are in [the source ledger](public-research-sources.md#autonomous-science-batch). Fetch date for this batch: 2026-11-04.

## Why a feedback loop matters

A researcher can decide what a measurement should seek and how to judge an answer; an algorithm can then use earlier measurements to choose what to measure next. This is an interpretation of the workflows below, not a claim that scientists or scientific judgment are absent [INFERRED: A01, A02]. An automatic sequence is not necessarily adaptive: here the distinguishing feature is that the next choice depends on information already obtained [INFERRED: A01, A02].

## One material, a published finding

In a 2022 study of ferroelectric materials, Yongtao Liu and coauthors report a machine-learning workflow that relates local domain structure to polarization-switching behavior. In piezoresponse force microscopy, the experiment uses measurements and their uncertainty to guide later measurements [KNOWN: A01]. In plain language, it chooses where to look next to learn how a material's local structure relates to its response.

The authors report that on-field and off-field hysteresis loops followed largely different discovery paths and sampling points; they interpret that as indicating different dominant mechanisms [KNOWN: A01]. This is a finding for the reported material and experiment, not a demonstrated universal law. An accepted manuscript attributes the workflow's conception to Sergei V. Kalinin, realization of the deep-kernel-learning workflow to Maxim A. Ziatdinov, and deployment to the microscope and results to Liu, with deployment help from Rama K. Vasudevan and Kyle Kelley [KNOWN: A02]. These are contributions to this paper, not claims about current jobs or leadership. Whether this particular study used the INTERSECT services below is [UNKNOWN: A01, A03].

## A microscope twin, a real computer, and a boundary

ORNL's 2022 INTERSECT highlight describes a configurable experiment interface, controller and machine-learning services, and an adapter for a Nion electron microscope or its digital twin; the algorithm chooses the next point using projected information gain [KNOWN: A03]. ORNL identifies Addi Malviya as principal investigator for this highlight [KNOWN: A03]. The highlight describes the capability, but its wording alone does not establish which reported run used a physical instrument rather than a twin [UNKNOWN: A03].

In an event reported in 2023, the demonstrators sent information from an electron-microscope digital twin to a real computing server, which analyzed it and sent results back for another scan [KNOWN: A04]. That demonstrates the reported twin-to-computer loop; it is not evidence that the event used a live microscope or that the loop produced a new materials discovery. Whether this demonstration and the 2022 highlighted workflow were the same implementation is [UNKNOWN: A03, A04].

Separately, ORNL's INTERSECT 4D scanning transmission electron microscopy proposal targets connecting microscopy at the Center for Nanophase Materials Sciences with computing, including structural reconstruction and deep-kernel learning [KNOWN: A05]. These are proposal targets, not proof that each target was achieved.

## Chemistry: preliminary results versus the larger ambition

The 2023 AutoFlowS paper describes an autonomous continuous-flow chemistry framework combining measurement, feedback, computational methods and compute resources, and reports preliminary results involving deuterated materials, copolymers and site-substituted molecules [KNOWN: A06]. Its abstract does not supply enough detail to independently quantify a yield or general speedup [UNKNOWN: A06]. ORNL's 2023 demo article quotes a comparison for some reactions, but does not give the reaction-by-reaction methods necessary to generalize that comparison; treat it as an attributed report, not a benchmark [KNOWN: A04].

The paper says the work was performed at CNMS and that INTERSECT supported development of the reactor system [KNOWN: A06]. This is a direct institutional relationship, not proof that AutoFlowS used the microscopy loop. The same paper lists Rama K. Vasudevan among its authors, and the ferroelectric paper lists Vasudevan as a coauthor too [KNOWN: A01, A06]. Shared authorship is a documented connection between publications, not proof that they share software, instruments, or scientific leadership [INFERRED: A01, A06].

## What remains unknown

Actual current deployments, the degree of routine operation, independent performance comparisons, and the exact software or dataset links between these experiments need further primary evidence. None of these examples establishes a fully general scientist-free laboratory. For wider context see [the guide](public-research-guide.md#connected-story-4-autonomy-still-needs-scientists), the existing [Flowcept](../projects/flowcept.md) and [Zambeze](../projects/zambeze.md) briefs; their use in these specific examples is [UNKNOWN]. A safe optional exercise is to sketch a feedback loop using invented measurements without connecting to any real instrument.
