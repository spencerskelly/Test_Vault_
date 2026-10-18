# Phase 8 — EA normalized connector evidence
Date: 2026-10-17. Status: read-only source-oriented candidate normalization; not native SysML v2 conformance.
## Source data
Reduced October 15 QEAX, 14,688 connectors. Counts from a separate read-only local run: orientation_normalized 3,601; owner_endpoint_identified 1,408; role_normalized 2,872; family_candidate 429; deferred_review 6,378.
EA generalization source/destination metadata supports source subtype → destination supertype when the modeled kinds are compatible. This is a provisional role normalization, not proof of valid specialization.
EA Aggregation: observed 1,670 connectors with `DestIsAggregate=2` (destination composite end); 597 with `DestIsAggregate=1` (shared). Among composite source connections, 1,408 part-like endpoint pairs could identify owning endpoint. No child Usage is created automatically.
Abstraction:allocate endpoint pattern is normalized from activity-to-object into object-performs-action, and state-to-object into object-exhibits-state only for compatible typed pairs; others remain review. Realisation with implementation-to-requirement pattern is oriented for the previously approved Requirement→Implementation Allocation policy but remains review gated.
## Local operator command
`python 14_Workbench/registry/runtime/normalize_qeax_phase8.py --qeax /private/model.qeax --registry 14_Workbench/registry/family_disposition_registry.v0.2.json --out /private/local_phase8`
Keep the source GUID ledger and every source row out of Test_Vault_. Only aggregate counts are acceptable in methods documentation.
## Validation and integration limits
This phase integrates **registry family keys and Phase 3 operation rule IDs** in the local reconciliation; it does not execute the JavaScript eligibility engine, modify the canonical graph, or create native SysML v2. The raw EA direction is used with typed endpoint patterns, but EA source/target role validation against trusted documented Sparx behavior, aggregation end details, parent cycles, and classifier/port semantics is still necessary. Treat normalized outcomes as evidence candidates, not accepted translations.
Pending: a single common typed intermediate representation consumed by the JS engine; exact EA direction and role attestation; parser; graph ownership validation; idempotent staging.
## Quality gates
8 synthetic Python tests passed locally. The new test is discoverable with the current GitHub Actions `test_*.py` pattern, but remote workflow status has not been verified. No model data committed.
