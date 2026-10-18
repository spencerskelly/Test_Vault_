# Pass 8 — Normalization replay acceptance handoff

Reduced source QEAX: 11,447 elements, 14,688 connectors; read-only source-table integrity was verified. The matching previously generated Phase 8 ledger and registry files are not present in the current runtime, so full replay was **not** executed against source rows here.

Added six synthetic replay tests (`test_replay_phase8_local_normalization.py`) covering exact match, changed direction, role, normalized orientation, missing ledger row, and missing column. CI workflow now watches the replay code and test and runs it with the other local-evidence synthetic suites. Committing tests is not the same as observing a successful CI run.

Mac/local verification in `Test_Vault_`:

```sh
git pull --ff-only origin main
python3 -m unittest -v 15_Testing/test_replay_phase8_local_normalization.py
python3 15_Testing/replay_phase8_local_normalization.py --qeax '/absolute/local/path/to/reduced.qeax' --ledger '/absolute/local/path/to/local_only_phase8_ledger.csv' --registry '/absolute/path/to/phase8-registry.json'
```

Expected successful report: `source_count=14688`, `ledger_count=14688`, `valid=true`, `error_counts={}`, `native_certified=0`. These are acceptance criteria, not observed results. Do not commit model or ledger. This replay recomputes normalized decisions with the **same** Phase 8 `decide()` implementation, establishing regression consistency but not independent SysML semantic correctness. Next: independent semantic oracle for EA direction, aggregation ownership, generalization and allocation roles; bind provenance hashes and reproduce state before allowing any eligibility.

Note: source QEAX and ledger must match the same immutable source snapshot; if the ledger predates recent QEAX edits, regenerate it first using `normalize_qeax_phase8.py`. Preserve the local-only outputs.