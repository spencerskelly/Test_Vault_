# Phase 9 — Local source-matched specialization direction handoff

Added `15_Testing/phase9_local_specialization_direction_handoff.py`, a read-only, aggregate-only comparison of original QEAX generalization connector identity and direction against the Phase 8 ledger. It requires matching EA GUID, raw endpoints, explicit source direction, normalized endpoints, `GENERALIZE` rule, expected subtype-to-supertype role and `orientation_normalized` status before classifying an edge as a `STRUCTURAL_DIRECTION_CANDIDATE_ONLY`. Every discrepancy is counted by category; source rows and IDs are never printed. Eight synthetic negative/positive checks are committed.

**Trust and semantic limitation:** This tool does not emit or inject canonical edges and is NOT an independently authenticated trust issuer. A matching record proves agreement with read-only source metadata, not native SysML v2 specialization eligibility or EA modeling intent. In particular, source direction fields must still be assessed against Sparx EA semantics; matches with invalid endpoint definition kinds remain in review. Keep `trust_issuer=false` and `native_certified=0`.

Local commands:

```sh
git pull --ff-only origin main
python3 -m unittest -v 15_Testing/test_phase9_local_specialization_direction_handoff.py
python3 15_Testing/phase9_local_specialization_direction_handoff.py --qeax "$HOME/Documents/Vaults/Engineering_Data/EA_2026_10_15_endgame_mini.qeax" --ledger "$HOME/Documents/MDSE_Local_Phase8/run_20261017/local_only_phase8_ledger.csv"
```

Follow-up: require verified snapshot/ledger fingerprints from a trusted local issuer, semantic endpoint kind checks, actual mapping to canonical node IDs, parser-verified native model examples and Workbench navigation/visual acceptance. Retain lexical nesting separately from subtype specialization and preserve source provenance. Native emitter remains disabled.