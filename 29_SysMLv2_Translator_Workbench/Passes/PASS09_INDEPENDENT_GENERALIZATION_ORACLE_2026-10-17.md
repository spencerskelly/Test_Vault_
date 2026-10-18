# Phase 9 / Pass 1 — Independent conservative generalization oracle

Phase 8 operator-verified full 14,688-row replay was successful with zero discrepancies, but that merely reproduced the Phase 8 normalizer. This pass adds a **separate**, conservative checker `15_Testing/phase9_independent_generalization_audit.py`, which does not import the Phase 8 normalizer. It inspects read-only QEAX generalization connectors and reports only aggregate categories.

Conservative positive candidate: raw connector type `Generalization`, blank stereotype, direction explicitly `Source -> Destination`, and both endpoints EA `Class` with exactly `block` stereotype. Every other pattern remains review-only. Even the positive result is an orientation/type candidate, **not** proof of correct subtype/supertype semantics or native parser acceptance. It must not approve an emitter or mutate an element.

Local tool separately tests ledger from/to orientation against the raw EA start/end and counts cases marked `orientation_normalized` by Phase 8 but not qualifying under this narrower oracle. No GUIDs, rows or names are printed. Eight synthetic cases and a CI workflow have been added; test execution has not yet been observed.

Local audit command from Test_Vault_:

```bash
git pull --ff-only origin main
python3 -m unittest -v 15_Testing/test_phase9_independent_generalization_audit.py
python3 15_Testing/phase9_independent_generalization_audit.py --qeax "$HOME/Documents/Vaults/Engineering_Data/EA_2026_10_15_endgame_mini.qeax" --ledger "$HOME/Documents/MDSE_Local_Phase8/run_20261017/local_only_phase8_ledger.csv"
```

Important semantic limitations: This is a conservative independent *policy oracle*, not an externally verified interpretation of all Sparx EA direction flags. Case-sensitive EA block stereotypes, UML classifiers, inherited definitions, specializations across compatible different definitions, and usages require evidence and separate review. `orientation_normalized` may legitimately be broader than this test; differences mean investigate, not rewrite source automatically. Native emission remains disabled.

Workbench requirement: a generalization candidate is drawn as subtype-to-supertype in the structural hierarchy and as a directed specialization link in visual views, with both endpoint navigation, explicit source orientation, validation status, and round-trip EA connector provenance. Do not confuse specialization with usage redefinition or part containment. No Workbench rendering change in this pass.