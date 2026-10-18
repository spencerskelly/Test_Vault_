# Phase 9 — Source direction evidence comparison

Added local-only source-to-ledger generalization direction comparison and five synthetic tests. It reads QEAX SQLite in read-only mode, compares raw identities, endpoints, direction and family to local Phase 8 ledger, and reports only aggregate errors and file SHA-256 hashes.

This does not authenticate the ledger or establish Sparx connector orientation semantics. It cannot grant native certification; the report always states `native_certified=0` and `direction_semantics_certified=false`. Before connecting to the canonical graph, require complete verified source/ledger/registry manifest and independent semantic confirmation.

Mac:
```
git pull --ff-only origin main
python3 -m unittest -v 15_Testing/test_phase9_source_direction_assessment.py
python3 15_Testing/phase9_source_direction_assessment.py --qeax "$HOME/Documents/Vaults/Engineering_Data/EA_2026_10_15_endgame_mini.qeax" --ledger "$HOME/Documents/MDSE_Local_Phase8/run_20261017/local_only_phase8_ledger.csv"
```

Source-model records must remain local. Native emission disabled.
