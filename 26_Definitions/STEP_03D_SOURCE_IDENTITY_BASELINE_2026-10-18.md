# STEP-03D — Source QEAX baseline and identity reconciliation (2026-10-18)

Status: **source baseline audited; crosswalk to STEP-02W exported graph pending**.

Read-only SQLite audit of the supplied reduced `EA_2026_10_15_endgame_mini.qeax` found: `PRAGMA quick_check=ok`; 11,447 `t_object` rows, each with a distinct ID and nonblank EA GUID; 14,688 `t_connector` rows with unique connector IDs and zero missing source object endpoints. 1,388 objects are typed Package, 3 Boundary and 144 Artifact. This is a source inventory, not a claim these types map directly to exported graph nodes or review flags.

Prior STEP-03A output reported 11,445 exported graph nodes and 14,688 edges. **Two fewer exported nodes than source objects** requires a source-ID-to-graph-ID reconciliation. It may be deliberate filtering or conversion, but must not be assumed. Likewise, 144 source Artifact objects and 144 previously missing attachment flagNotes are merely numerically equal; no identity linkage has been established. Do not merge these assumptions.

Committed read-only source audit: `25_Testing/v2_step03d_qeax_source_audit.py`. Run locally on a trusted QEAX copy:

```bash
python3 25_Testing/v2_step03d_qeax_source_audit.py /private/EA_2026_10_15_endgame_mini.qeax
```

Acceptance tasks:
1. Recover or re-run canonical exporter to generate graph and explicit EA Object_ID/ea_guid -> graph node ID crosswalk, including disposition of every source object and the two-object discrepancy.
2. Derive attachment flag row identities from original local-only review ledger, **not** by inferring that 144 Artifact rows equal 144 flags.
3. Stage via STEP-03C using independently verified node IDs; run STEP-03B with count and ownership reconciliation for each flagged attachment.
4. Confirm 14,688 edge identities and end-to-end provenance, no broken endpoints, and no source loss; then test actual Workbench browser UI.
5. Continue separately with native SysML parse and Obsidian acceptance. Keep all EA diagrams out of tooling and keep raw QEAX and per-row ledgers local.

Result: the source QEAX itself does not block progress. **Graph crosswalk and attachment identity proof are the immediate next gates.** No golden-import acceptance claimed.
