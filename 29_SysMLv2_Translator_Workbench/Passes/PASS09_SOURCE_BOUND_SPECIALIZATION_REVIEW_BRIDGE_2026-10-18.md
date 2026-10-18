# Phase 9 — Source-bound generalization to canonical review bridge

This pass adds a local-only review checker linking read-only QEAX generalization rows, the Phase 8 local-only disposition ledger, and a private graph-node mapping by `sourceId`. It directly compares the trusted source connector GUID, raw endpoints, explicit EA direction, normalized endpoints, coverage and mapped endpoint definition kinds, avoiding a caller-supplied `verified: true` token.

The checker reports only aggregate error categories/counts and two file SHA-256 digests. It never outputs individual source IDs, names, GUIDs or raw rows. It always returns `native_certified: 0`, `may_emit_native: false`. Source consistency does not equal approved SysML v2 eligibility.

Six synthetic test cases cover matched evidence, endpoint tamper, GUID tamper, missing graph mapping, usage misclassification, and emission denial. Tests are committed; execution has not yet been independently observed. Only synthetic model data was used in the tests.

Local-only command requires a **private** JSON graph mapping, such as `{"nodes":[{"id":"child","sourceId":10,"kind":"PartDefinition"}, ...]}`. Do not commit this mapping:

```sh
git pull --ff-only origin main
python3 -m unittest -v 15_Testing/test_phase9_source_bound_specialization_review.py
python3 15_Testing/phase9_source_bound_specialization_review.py \
 --qeax "$HOME/Documents/Vaults/Engineering_Data/EA_2026_10_15_endgame_mini.qeax" \
 --ledger "$HOME/Documents/MDSE_Local_Phase8/run_20261017/local_only_phase8_ledger.csv" \
 --graph /private/path/canonical_nodes.json
```

The private graph mapping is not automatically generated yet, so **full QEAX-to-canonical reconciliation has not been performed**. This is a read-only review tool, not production JS graph mutation, Workbench rendering, or native code emission. Next: derive the node mapping from the actual canonical graph and integrate a verified evidence object into `evaluateOnGraph` without introducing a parallel trust path; distinguish specialization direction, ownership and definition identity, preserving Workbench structural/visual/navigation/provenance requirements.