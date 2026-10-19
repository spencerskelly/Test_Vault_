# STEP-03I — Reproducible source graph exporter integration (2026-10-18)

**Status:** STEP-03H read-only exporter and four synthetic regression tests committed to `Test_Vault_` main. The source baseline is **not** a native SysML v2 conversion or golden import.

Files:
- `25_Testing/v2_step03h_raw_graph_export.py`
- `25_Testing/test_v2_step03h_raw_graph_export.py`

Verified locally against the supplied reduced QEAX: 11,447 source objects / nodes and 14,688 source connectors / edges, no source connector endpoint loss. The generated full graph and QEAX remain local. Earlier translated graph had 11,445 nodes, so do not equate the two representations until reconciled by source identity. No EA diagrams are read or emitted. This baseline does not run the semantic registry or apply `flagNote`/`flagLink`.

Local repeatable procedure:

```bash
python3 -m unittest discover -s 25_Testing -p 'test_v2_step03h_raw_graph_export.py' -v
python3 25_Testing/v2_step03h_raw_graph_export.py /private/EA_2026_10_15_endgame_mini.qeax /private/new-empty-graph-dir
python3 25_Testing/v2_step03e_identity_crosswalk.py /private/EA_2026_10_15_endgame_mini.qeax /private/new-empty-graph-dir/nodes.jsonl --output /private/crosswalk.json
```

Keep generated `nodes.jsonl`, `edges.jsonl`, `export_summary.json`, and per-object reports private. Generated graph files can be large; this source-faithful baseline is for reproducibility, troubleshooting and crosswalk, not an approved distributed model.

**Next gates:** verify the committed exporter and four tests on the user's Mac; reconcile source identities with previous translated graph if available; attach independently proven review flags; connect the *approved SysML v2 registry* rather than mapping raw EA types directly to final MDSE classes; validate the actual Workbench graph schema and browser rendering. Do not process EA diagrams before the golden import.
