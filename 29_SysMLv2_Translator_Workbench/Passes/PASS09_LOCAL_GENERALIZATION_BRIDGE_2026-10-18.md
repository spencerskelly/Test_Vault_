# Phase 9 — Local-only EA generalization evidence bridge

Implemented `15_Testing/phase9_local_ea_generalization_bridge.py` as a narrow handoff from the existing Phase 8 QEAX/ledger normalization replay to review-only canonical-shaped relationship records. It imports the existing replay and rejects the entire handoff when row counts or normalized ledger replay do not match the source. It checks each Generalization's raw direction, source/target endpoint order, normalized endpoints, stereotype and `orientation_normalized` status before producing a local-only review record.

**Trust limitation:** this is a same-implementation normalization consistency gate plus independently checked raw QEAX direction. It is not a trusted externally signed attestation, does not validate eligible SysML definition kinds or all EA stereotype context, does not check semantic meaning of specialization, and does not connect to the production JS graph. Output records contain confidential original connector and element references; CLI refuses destinations inside repository and outputs only aggregate counts to console. Never commit the private JSON.

Review record status is `SOURCE_ORIENTATION_ONLY` and `nativeCertified=false` for every relationship. No native emitter path is enabled. The format may be used as input to a future **local-only** canonical graph integration after separate kind, source provenance and semantic gates.

Local commands:

```sh
git pull --ff-only origin main
python3 -m unittest -v 15_Testing/test_phase9_local_ea_generalization_bridge.py
python3 15_Testing/phase9_local_ea_generalization_bridge.py \
  --qeax "$HOME/Documents/Vaults/Engineering_Data/EA_2026_10_15_endgame_mini.qeax" \
  --ledger "$HOME/Documents/MDSE_Local_Phase8/run_20261017/local_only_phase8_ledger.csv" \
  --registry 14_Workbench/registry/family_disposition_registry.v0.2.json \
  --private-output "$HOME/Documents/MDSE_Local_Phase8/phase9_generalization_review.json"
```

Check that the output path does not already exist. Tests have been committed but have not yet been confirmed on macOS or CI. Workbench structural and visual behavior stays deferred: represent directed specialization separately from lexical containment, support source/target navigation and source provenance, flag review status, and forbid auto-generated part usages or source edits. Native emission disabled.