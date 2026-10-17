# Phase 7 — QEAX source-row reconciliation
Date: 2026-10-17. Status: read-only executable source-ledger diagnostic, NOT native import acceptance.
Source fixture SHA256: `69222c060a81b3e35a3e25f365f2a1f4c3dd6eaa19d77fbbd5ba9abdf365a822`.
Run: `python 14_Workbench/registry/runtime/reconcile_qeax.py --qeax /private/path/EA_2026_10_15_endgame_mini.qeax --out /private/local/output`.
All ledger columns, GUIDs, endpoint families and raw directions stay LOCAL and must NEVER be committed. Publish aggregate counts only.
## Actual run
14,688 connectors, 11,447 elements; exactly one disposition row per connector. 409 `candidate_only`; 14,050 `deferred_review`; 229 `evidence_only`. Native accepted: **zero**. Counts are exclusive dispositions. Diagnostics overlap, and must not be summed as though exclusive.
Diagnostics (overlapping): EA_GENERALIZATION_ORIENTATION_NOT_ATTESTED 3735; ALLOCATION_ROLE_UNATTESTED 2605; OWNERSHIP_OR_REALISATION_REVIEW 3150; SEMANTIC_REVIEW_REQUIRED 2192; TRACE_REFINE_REVIEW 1018; SATISFY_DIRECTION_UNATTESTED 1330; UNRESOLVED_ENDPOINT_KIND 1226; UNVERIFIED_DIRECTION 431; ENDPOINT_MISMATCH 82; NATIVE_PARSER_NOT_VERIFIED 429; NON_SEMANTIC_CONNECTOR 229.
## Evidence limitations
This runner produces a preliminary source ledger, **not** a final approved normalized canonical graph: kind mapping is deliberately coarse and conservative; raw EA `Direction` is recorded but not semantically attested; `SourceIsAggregate` and `DestIsAggregate` are extracted but not yet fully interpreted; role/trust evidence is not inferred. Compound Realisation semantic rule selection remains deferred. It does not invoke the Phase 4 JavaScript evaluator or a native parser. Source connector GUIDs and row identity remain local.
## CI
The GitHub connector's commit-workflow query for Phase 6 commit `3babcd4` returned no runs; that endpoint only reports pull-request-triggered runs, so **push workflow status remains unverified**. The new synthetic test module is for CI inclusion. Six synthetic unit tests were run locally and passed.
## Next gates
- Schema-verifiable mapping of all 60 element families into native Definition/Usage/context.
- EA raw connector orientation and source/destination role extractor with trusted evidence.
- Registry runtime integration and owner/cycle graph checks per row.
- Full native SysML v2.0 parser and pinned library conformance.
- Full source ledger persisted outside methods repo, remapped into canonical target identity and three-way merge tests.
