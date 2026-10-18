# Pass 4 — local Phase 8 transactional validation

Local-only reduced QEAX validation completed against the 2026-10-15 reduced source, using a locally reconstructed Phase 8 normalization and staging validator matching the committed algorithm. This is **not execution of the exact GitHub checkout**; the registry fallback set was empty in the local rehearsal, so treat the aggregate categories as provisional and rerun from the complete checkout using the actual registry.

Source quick_check: ok. Exact profile file digest matched. Connector count in selected profile: 14,688. CSV records written: 14,688. Unique source connector IDs: 14,688. Duplicate IDs: 0. Summary counts matched source and CSV. Staging directory was renamed into a private local output directory only after validation. Native SysML v2 certified relationships: 0.

Provisional statuses: deferred_review 6,378; orientation_normalized 3,601; owner_endpoint_identified 1,408; family_candidate 429; role_normalized 2,872. These are **not** accepted native SysML v2 relationships.

Six local staging-validation scenarios passed: valid output, duplicate IDs, missing aggregate, missing ledger, count mismatch, and false native certification. These are local independently recreated test cases, **not** proof that the committed `test_phase8_atomic_outputs.py` suite passed. The GitHub checkout is still unavailable from the local runtime.

No QEAX file, private connector IDs, GUIDs or row-level ledger was committed. Follow-up: run the exact committed six-test suite and gated runner from a full checkout with the actual registry, test rollback on a synthetic mid-run exception, verify no bypass of the gate, and reconcile all counts before any native import acceptance.
