# Phase 9 — Source-backed direction bridge hardening (October 18, 2026)

Repository already had a read-only local `15_Testing/phase9_source_direction_bridge.py` comparing full Phase 8 ledger identities, raw connector endpoints/direction, and oriented Generalization role against the same source QEAX. This pass strengthened its candidate gate: **only `orientation_normalized` ledger status and blank source connector stereotype** can reach the conservative definition-family candidate classification. Deferred status and custom-stereotyped connectors now count as separate review categories. Two synthetic regressions added.

This does not issue cryptographically authenticated trust tokens and does **not** allow the canonical JavaScript graph to accept source direction merely because a caller sets `direction`. The operator must run the private local QEAX-backed bridge, and independently preserve verified evidence and source mapping; there is no cross-process signed attestation or actual source-record promotion in this pass.

Mac command:

```sh
git pull --ff-only origin main
python3 -m unittest -v 15_Testing/test_phase9_source_direction_bridge.py
python3 15_Testing/phase9_source_direction_bridge.py --qeax "$HOME/Documents/Vaults/Engineering_Data/EA_2026_10_15_endgame_mini.qeax" --ledger "$HOME/Documents/MDSE_Local_Phase8/run_20261017/local_only_phase8_ledger.csv"
```

Require zero `errors`, full 14,688 connector source/ledger coverage, `valid=true`, `native_certified=0`, `may_emit_native=false`. Candidate counts are review-only. All model rows stay local. Tests committed; independent local/CI pass not yet observed.

Next: implement a verifiable local-only snapshot-bound transfer contract to canonical JS evaluation, plus Workbench structural/visual/provenance contracts. Never confuse subtype with lexical nesting or physical composition.