# Pass 6: Original connector evidence retained in Phase 8 ledger

Updated `14_Workbench/registry/runtime/normalize_qeax_phase8.py` on main (42f43ab) to add original connector `Direction`, `SourceRole`, `DestRole`, `SourceCard`, `DestCard`, source/target aggregation flags, and both original endpoint type/stereotype pairs alongside normalized fields. These extra fields go **only into the local-only detailed CSV**. Public aggregate results remain counts without model rows.

Updated `15_Testing/phase8_deferred_evidence_compat.py` (a3fbcf9 and f3649ed): it now reports whether extended source fields exist and no longer reports them as absent when supplied. Retention of a field does not prove its value is adequate evidence. Added synthetic schema tests (a44e6a8).

Open gates: full repo checkout test run, complete local re-execution of Phase 8 on reduced QEAX and verified 14,688-row coverage, exact source field fidelity tests, native parser conformance, semantic reviewer approval and actual BOM validation. Native certified remains **zero**; no native emitter is enabled. No private model data or detailed ledger was committed.
