# STEP-03C — Guarded attachment flag serialization stage (2026-10-18)

Status: **stage and synthetic regression tests committed; canonical STEP-02W exporter integration pending**.

The repository contains graph viewers and preflight records but did not expose the source of the local-only STEP-02W exporter. To avoid silently claiming an exporter fix, a standalone, deterministic staging operation was committed as `25_Testing/v2_step03c_stage_attachment_flags.py` with synthetic tests in `25_Testing/test_v2_step03c_stage_attachment_flags.py`. Six synthetic cases were run locally against the implementation (five distinct tests are committed, including idempotency); all passed.

The stage consumes `nodes.jsonl` and a *local-only* `attachment_flags.jsonl` file whose rows are `{"node_id":"<stable existing graph node ID>","flagNote":<original review evidence>}`. The latter must be generated from the import's existing attachment review ledger using verified stable IDs; **do not infer IDs from names or fuzzy matches**. It writes a *different* staged output, preserving all original node fields. It rejects ambiguous/duplicate flag IDs, duplicate graph IDs, conflicting pre-existing flags, missing target nodes, or input/output path reuse. It does not add synthetic nodes, alter QEAX, or import diagrams.

Example local invocation:

```bash
python3 25_Testing/v2_step03c_stage_attachment_flags.py \
  /private/nodes.jsonl /private/attachment_flags.jsonl /private/nodes-staged.jsonl
python3 25_Testing/v2_step03b_graph_flag_gate.py \
  /private/nodes-staged.jsonl /private/edges.jsonl --expected-flag-notes 159
python3 -m unittest -v 25_Testing/test_v2_step03c_stage_attachment_flags.py
```

The 159 target is specific to the previously audited reduced graph, **not** a constant for future imports. The source review index still needs independently verified node-ID mapping and ownership checks; count parity by itself is insufficient. A fresh reduced graph must validate 11,445 node identities and 14,688 edge identities, preserved source payloads, endpoint completeness, expected flag identities, and 159 node-resident note flags before this checkpoint is accepted.

Next: integrate equivalent logic *within* the canonical STEP-02W exporter when its source is recovered, run a fresh export and the actual Workbench browser UI, and separately validate native SysML and Obsidian. Private data remains local and diagrams excluded. This commit does **not** establish full graph acceptance or golden-import readiness.
