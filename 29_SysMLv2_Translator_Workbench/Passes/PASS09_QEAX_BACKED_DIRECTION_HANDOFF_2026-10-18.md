# Phase 9 — QEAX-backed source direction handoff, aggregate-only

Added `15_Testing/phase9_source_direction_bridge.py`, a local read-only check that compares the Phase 8 CSV ledger to the original QEAX `t_connector` identity, raw endpoints and direction, then checks generalization orientation/role and conservative independent endpoint family classification. The tool emits only aggregate counts. Unlike a caller-supplied `verified` boolean, it actually opens the read-only source database. It must never export per-connector evidence into the public repository.

The gate checks full ledger key coverage, duplicate/unknown source IDs, missing raw source identity, swapped normalized endpoints and unsupported generalization role. Six synthetic tests cover positive review-only, altered direction, endpoint, role, missing ledger row, and altered GUID. Tests committed; Mac/CI execution not yet confirmed.

**Scope:** This validates consistency of direction and typed candidate classification against *the file opened at runtime*. It does NOT authenticate the file's issuer, recheck every Phase 8 normalized field, certify a native semantic construct, or securely bind evidence through to the production JavaScript process. It does not elevate any model edge to eligible status and cannot be used to emit SysML v2. The existing canonical validator requires subtype-to-supertype orientation independently; no trust-token shortcut is added.

Local operator command (private artifacts remain outside repo):

```sh
git pull --ff-only origin main
python3 -m unittest -v 15_Testing/test_phase9_source_direction_bridge.py
python3 15_Testing/phase9_source_direction_bridge.py --qeax "$HOME/Documents/Vaults/Engineering_Data/EA_2026_10_15_endgame_mini.qeax" --ledger "$HOME/Documents/MDSE_Local_Phase8/run_20261017/local_only_phase8_ledger.csv"
```

Acceptance target: 14,688 source and ledger keys, no errors, 0 native certified. The generalization category breakdown is informative only. Workbench structural and visual implementations remain deferred; preserve lexical containment vs specialization, navigation to source/target, EA provenance and later round-trip validation. No private model records committed.