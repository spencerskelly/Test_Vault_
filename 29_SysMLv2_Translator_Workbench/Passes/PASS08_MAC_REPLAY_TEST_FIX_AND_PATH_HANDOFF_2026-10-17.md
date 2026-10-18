# Pass 8 — Mac replay invocation corrections

User ran six synthetic replay tests on macOS Python 3.12: five passed, one errored in `test_missing_column` before exercising the verifier. `csv.DictWriter` rejected a row containing `diagnostics` after the test intentionally omitted that header. Corrected the test writer to include only keys in the current headers (commit 5a4590e). This addresses the test fixture, not the production replay logic.

User then ran the replay tool using the literal example paths `/path/to/reduced.qeax`, `/path/to/local_only_phase8_ledger.csv` and `/path/to/registry.json`; SQLite could not open the nonexistent QEAX path. Added a preflight input-file existence check with a targeted command-line error (commit 81a137e).

Re-run from the local repository:

```sh
git pull --ff-only origin main
python3 -m unittest -v 15_Testing/test_replay_phase8_local_normalization.py
find "$HOME" -name '*.qeax' -o -name 'local_only_phase8_ledger.csv' 2>/dev/null
```

Use actual **absolute local file paths** for the QEAX, a matching generated Phase 8 ledger and the central eligibility registry JSON. If no ledger exists, generate a fresh local ledger with `14_Workbench/registry/runtime/normalize_qeax_phase8.py` using its `--qeax`, `--registry`, and `--out` parameters, directing output outside the repo. Never upload these files.

The fixes are committed; a new Mac or CI test run has not yet been observed. Full 14,688-record replay and independent EA semantic confirmation remain pending. Native emission disabled.