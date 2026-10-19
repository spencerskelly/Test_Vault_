# STEP-03F — Identity crosswalk integrated into V2 toolset (2026-10-18)

**Status:** STEP-03E reconciliation script and five synthetic regression cases are now committed on `main` under `25_Testing/`. The previously issued local ZIP was not itself authoritative. This step imports reusable code, tests, and this procedure, not local QEAX or graph data.

## Authoritative files

- `25_Testing/v2_step03e_identity_crosswalk.py`
- `25_Testing/test_v2_step03e_identity_crosswalk.py`
- `25_Testing/v2_step03d_qeax_source_audit.py`
- `25_Testing/v2_step03c_stage_attachment_flags.py`
- `25_Testing/v2_step03b_graph_flag_gate.py`

## Local validation sequence

Run tests from the repository root:

```bash
python3 -m unittest discover -s 25_Testing -p 'test_v2_step03e_identity_crosswalk.py' -v
```

With a fresh graph exported from the same QEAX snapshot:

```bash
python3 25_Testing/v2_step03d_qeax_source_audit.py /private/EA_2026_10_15_endgame_mini.qeax
python3 25_Testing/v2_step03e_identity_crosswalk.py /private/EA_2026_10_15_endgame_mini.qeax /private/nodes.jsonl --output /private/source_graph_crosswalk.json
```

`source_graph_crosswalk.json` can contain individual source GUIDs: keep it private. Review `source_without_verified_node`, `graph_without_unique_source`, `multiply_represented_source_objects` and `duplicate_graph_ids`. Return code 2 means identity reconciliation needs review; **do not interpret every source object without a node as data loss**, because valid mergers/exclusions may exist, but each must be explained by exporter provenance. The comparator does not infer correspondence from names, package containment, or matching aggregate counts.

Previous baseline: 11,447 source objects and 14,688 connectors versus 11,445 exported graph nodes and 14,688 edges. Neither the exact missing two source IDs nor their dispositions have yet been proven. Do not equate 144 Artifacts with 144 missing attachment flags without identifier matching.

Once the graph identities are available: reconcile attachment ledger ownership, run STEP-03C staged flag serialization, run STEP-03B graph parity gate with the independently computed expected flag count (159 for previously audited reduced export), then exercise the actual Workbench UI. Keep diagrams excluded from tools until golden import acceptance.

**Remaining limitation:** canonical STEP-02W exporter source and the locally exported graph have not been recovered into this repository. The crosswalk is committed and usable, but **has not yet been wired into the canonical exporter or run against the historical graph**. Never call this a successful golden import merely from synthetic tests.
