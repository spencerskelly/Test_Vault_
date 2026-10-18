# Pass 4 — Source profiles and Phase 8 ledger acceptance status

## Verified locally

- Reduced QEAX local SQLite integrity checked, with 14,688 connectors.
- Previously generated private Phase 8 ledger revalidated: **14,688 rows, 14,688 unique source connector IDs, zero duplicates, summary total 14,688, native_certified 0**.
- Locally reconstructed six-case staging checker suite was executed: **6 tests, all passed** (success, duplicate ID, missing aggregate, missing ledger, incomplete row count, incorrect native certification).
- No proprietary rows or GUIDs were committed.

## Not yet verified / not accepted

- The **exact committed** `15_Testing/test_phase8_atomic_outputs.py` was not run from a complete repository checkout. Its six tests were not the six reconstructed local checks above. In particular the mocked exception case and pre-existing destination scenario still need direct execution.
- The full `15_Testing/run_gated_phase8.py` was **not run with the actual registry JSON in a complete checkout**. The local rehearsal used the same normalization logic but an empty fallback registered-family set, so registry-specific diagnostics may differ.
- A native SysML v2 parser/serializer has not accepted any of these candidates. Native certified: **0**.
- The standalone `normalize_qeax_phase8.py` still permits a direct ledger run without the new preflight; the protective gate is not universal.
- Base Vault build, Bootstrap first-open, and importer CI path repair are still separate release blockers.

## Completion criteria for Pass 4

1. Run the exact committed transactional suite in checkout: `python3 -m unittest discover -s 15_Testing -p test_phase8_atomic_outputs.py -v` and repair any failing tests.
2. Run `15_Testing/run_gated_phase8.py` with the private exact-hash reduced profile, full profile disposition policy, actual `14_Workbench/registry/family_disposition_registry.v0.2.json`, and a brand-new private output directory.
3. Confirm exactly 14,688 CSV rows, no duplicate source connector IDs, matching summary JSON, no partial staging folders, and zero native-certified claims.
4. Test deliberately wrong source profile and forbidden-nonempty synthetic SQLite policy cases; verify no output is created.
5. Document the aggregate-only comparison versus the provisional local rehearsal. Keep the entire ledger and source inputs outside GitHub.

**Decision:** Pass 4 source-profile rules and transactional tooling are prepared, but end-to-end checkout verification is PENDING. Release NO-GO. Next gated task: verify committed suite and registry execution, or proceed to Pass 5 methods with Pass 4 explicitly open; never silently mark this gate complete.
