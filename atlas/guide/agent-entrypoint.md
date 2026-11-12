# Read Atlas from Codex or Hermes

Atlas is a public-source research repository. This entry point is for readers of this checkout; it does not install an integration or change Hermes configuration.

## Retrieve a bounded context packet

From the repository root:

```sh
python3 scripts/atlas_query.py --search provenance
python3 scripts/atlas_query.py --node project-workflow-software-reconstruction
python3 scripts/atlas_query.py --node software-zambeze
```

The command emits JSON, performs no network access, and reads only the six public registry files. A node packet includes its record, listed references, incident typed graph relationships, neighboring records, supporting sources, and unresolved source IDs. Source URLs, excerpts, retrieval dates, and relationship limitations are retained. Search uses all supplied terms, case-insensitively, within each record. Unknown IDs and broken references return a nonzero exit code.

A listed software/facility reference is not proof of integration. A source marked verified means Atlas recorded a fetched source, not that every interpretation is valid or current. Read the source and dossier for load-bearing claims. Local translations describe our designs. The command intentionally preserves inferred, blocked, lead, and historical labels rather than turning everything in a neighborhood into verified facts.

## Read in this order

1. Retrieve the project packet and read its linked dossier, if present. For older records, follow the guide index.
2. Inspect supporting sources and the recorded revision/date. Re-fetch before making a claim about current behavior.
3. Read limitations and unknowns. Keep missing evidence visible in any derived answer.
4. For experiments, read the lab README and run only the named local fixture. A study proxy does not establish upstream compatibility or scientific validity.
5. Read the latest batch verification/handoff before continuing research. Preserve prior evidence and add corrections with their basis.

Start with [workflow software and local reconstruction](project-dossiers/workflow-software-and-local-reconstruction.md), its [research batch](../research/2026-11-10-workflow-systems/README.md), and the [local lab](../labs/cross-layer-pilot/README.md). The broader [research plan](research-plan.md) tracks lanes outside this completed batch.

## Continue discovery without losing evidence

Use one bounded question per batch: an unknown interface, an unverified repository, a compatibility boundary, or an experiment outcome. Record primary URLs, exact supporting passage or code datum, publication/retrieval dates, revision, evidence label, and limitation. Search snippets and agent summaries are leads. Integrate only after checking the underlying artifacts; then run an independent verification pass, the registry validator, the link checker, and relevant local tests.

Keep the research backlog separate from completed results. This batch's concrete follow-ups are in the workflow dossier. There is no standing background researcher or automatic refresh configured by this change.
