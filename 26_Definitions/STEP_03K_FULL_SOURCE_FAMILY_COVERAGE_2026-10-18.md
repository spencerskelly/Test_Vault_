# STEP-03K — Reduced QEAX aggregate registry coverage and identity reconciliation

Date: 2026-10-18. Status: **aggregate coverage and source-identity reconciliation passed; complete governed annotation execution pending on user's checked-out repository**.

## Input and method

Reduced local QEAX `EA_2026_10_15_endgame_mini.qeax` and previously generated STEP-03H `nodes.jsonl` from same QEAX. Both were kept out of GitHub. Normalized EA exact family as `type[:stereotype]`, treating SQLite NULL and empty stereotypes consistently. Compared against the **60 element-family and 26 connector-family keys** in `24_Workbench/registry/sysml_v2_approved_family_resolver.v0.1.json`. Ran STEP-03E identity crosswalk on the existing raw source graph. No diagrams involved.

## Results

| Metric | Value |
| --- | ---: |
| EA source objects | 11,447 |
| Raw source graph nodes | 11,447 |
| EA source connectors | 14,688 |
| Raw source graph edges | 14,688 |
| Observed / approved element families | 60 / 60 |
| Observed / approved relationship families | 26 / 26 |
| Element records with approved family key | 11,447 |
| Connector records with approved family key | 14,688 |
| Unmatched family keys | 0 |
| Source objects without verified graph identity | 0 |
| Graph nodes without unique source identity | 0 |
| Multiply represented source objects | 0 |
| Duplicate graph identities | 0 |

Normalization detail: `Note` and `NoteLink` appear with both NULL and empty `Stereotype`, which are the same exact approved family after normalization, not separate outliers.

## Limits

These results **do not** establish parser eligibility, row-level conditional evidence, SysML-native translation, attachment flag identity reconciliation, the previous 11,445 transformed-node representation, or browser Workbench acceptance. Do not treat the observed zero unmatched *families* as zero unresolved *relationships*. STEP-03J full annotation must still be executed with its real checked-out registry, and appropriate flags must be restored from STEP-03C. The raw graph deliberately has 11,447 nodes, not the prior transformed count.

## Reproducible Mac execution

From `Test_Vault_`, run on a private local QEAX path (set `QEAX` appropriately):

```bash
QEAX="/absolute/path/to/EA_2026_10_15_endgame_mini.qeax"
ROOT="$HOME/Documents/MDSE_Local_STEP03K"
mkdir -p "$ROOT"
python3 25_Testing/v2_step03h_raw_graph_export.py "$QEAX" "$ROOT/raw"
python3 25_Testing/v2_step03j_approved_family_annotation.py "$ROOT/raw/nodes.jsonl" "$ROOT/raw/edges.jsonl" "$ROOT/annotated"
python3 25_Testing/v2_step03e_identity_crosswalk.py "$QEAX" "$ROOT/annotated/nodes.jsonl" --output "$ROOT/crosswalk.private.json"
cat "$ROOT/annotated/annotation_summary.json"
```

Use fresh empty `raw` and `annotated` output dirs; the exporter and annotator reject nonempty destinations. Nothing at row level should be committed to GitHub.

Next: full local execution evidence, attachment `flagNote` and `flagLink` ownership, strict row-level semantic transformations, Workbench UI acceptance; keep EA diagrams excluded until golden import.
