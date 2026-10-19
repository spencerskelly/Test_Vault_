# STEP-03N — Attachment identity inventory

Date: 2026-10-18. Source: reduced QEAX. A source-faithful identity audit is now in `25_Testing/v2_step03n_attachment_identity_audit.py`.

Observed aggregate evidence:
- 144 EA Artifact elements: 93 Image, 51 Document.
- 42 Artifact elements have no connector endpoint.
- 120 rows in `t_document`; 114 have a unique GUID match to an EA model object.
- Among matched embedded-document rows: 93 Image artifacts, 7 Document artifacts, 13 Requirements, 1 Class.
- 6 embedded document rows lack a direct model-object GUID match.

These categories overlap and **must not be summed** as missing files or flagged notes. Matching document GUID alone proves a record-level link, not full ownership semantics. Unconnected artifacts may still have valid ownership by containment, document references, or intentionally deferred classification.

Local validation:

```bash
git pull --ff-only origin main
python3 25_Testing/v2_step03n_attachment_identity_audit.py "/Users/spencerskelly/Documents/Vaults/Engineering_Data/EA_2026_10_15_endgame_mini.qeax"
```

The audit is read-only, outputs aggregate counts, and does not touch diagrams. It creates zero flags. Before generating `flagNote`, resolve source IDs and attach review entries to the **responsible note**, not to new attachment notes. Recover any prior identity-grounded flags, avoiding manufactured counts. Preserve all source records.

Remaining: tests for alternate GUID styles and ambiguous matches, ownership by containment and connector orientation, source-identified review ledger, STEP-03C flag staging, Workbench in-browser acceptance.
