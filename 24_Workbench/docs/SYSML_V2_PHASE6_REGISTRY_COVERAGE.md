# Phase 6 — Full source-family disposition and strict evidence gates
Date: 2026-10-17. Status: machine-readable family-disposition catalog, local audit and tests; native parser integration pending.
## Coverage
Phase 2 local aggregate: 838 patterns / 14,688 connectors. Existing Phase 3 rule families cover 606 patterns and 12,267 connectors. Newly defined explicit review families cover 205 patterns / 2,192 connectors. Evidence-only covers 27 patterns / 229 connectors. All 26 EA connector families have a disposition. **This is not per-connector semantic acceptance.** No model rows, IDs, or original diagram content are in this repository.
## Semantic decisions still open
- UseCase include/extend: validate native case/feature semantics; no assumed standard binary relation.
- Association and Connector: typed connection versus interface versus feature reference.
- ControlFlow, StateFlow, Sequence: occurrence/action context, guard/trigger/effect, message payload and native succession semantics.
- Nesting and Usage: namespace containment versus owned FeatureUsage versus Dependency.
- Derive, Verify, Responsibility, RecoveryRequirement, and Realisation:deriveReqt: evidence and normative construct must be resolved.
- Phase 3 Aggregation and Realisation remain review gated; no automatic ownership or satisfaction inference.
## Strict evidence
The validator requires family, connectorId, sourceId, targetId, explicit orientation and semantic role, plus an evidence object. Unknown fields, malformed roles and conflicting direction are rejected. This is an envelope validator; typed tags and actual EA-source attestation are still pending.
## Local audit runner
Run: `python 14_Workbench/registry/runtime/reconcile_fixture.py --registry 14_Workbench/registry/family_disposition_registry.v0.2.json --shapes /local/private/endpoint_shape_matrix.csv --output /local/private/summary.json`.
Only the aggregate summary may be copied into documentation. No fixture data or generated imported notes committed.
## CI and acceptance boundaries
GitHub Actions runs prior Phase 4/5 JavaScript tests plus Phase 6 Python synthetic tests. Local Phase 6 Python synthetic suite: 9/9 passed. Remote CI status not yet verified. Native SysML v2.0 parser, full source-level ledger, model ownership operation simulation, actual Workbench binding, reimport/idempotence and BOM reconciliation are not yet implemented.
