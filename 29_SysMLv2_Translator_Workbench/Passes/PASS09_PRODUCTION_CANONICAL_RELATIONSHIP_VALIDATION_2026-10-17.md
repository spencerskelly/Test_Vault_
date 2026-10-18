# Phase 9 — Production canonical relationship validation

Integrated `validateCanonicalRelationships` into the existing `validateGraph` implementation in `14_Workbench/registry/runtime/canonical-model.mjs`. Unlike prior stand-alone fixtures, Graph validation now checks declared `relationships` when present. It preserves lexical nesting and subtype generalization as two distinct graph semantics.

Checks: lexical edge must agree with node `ownerId`; specialization must link matching Definition kinds, require nonblank source provenance, honor explicit subtype-to-supertype direction if supplied, reject self/cyclic specialization, duplicate relationship edges, missing endpoints and unrecognized edge kinds. Iterative DFS avoids recursive stack overflow. Other relationship families remain in their existing eligibility gates; they are **not** generally covered by this narrow validator.

Added nine synthetic Node tests and updated existing nested-definition CI workflow to run both the old five-case Workbench contract and new nine-case relationship suite. CI execution is not yet confirmed.

Implementation caveat: `validateGraph` validates only fields and sourceRef presence, not trusted source attestation or native SysML v2 parser semantics. Omitted direction is allowed in this revision; downstream eligibility must still require verified EA orientation. No native emitter has been enabled. Existing synthetic graph relationships are not yet persisted or rendered in actual Workbench views.

Operator command:

```sh
git pull --ff-only origin main
node --test 15_Testing/test_phase9_nested_definition_workbench_contract.mjs 15_Testing/test_phase9_canonical_relationship_validator.mjs
```

The native nested definition parser workflow remains manual dispatch; results for its new nested-definition fixtures are not yet confirmed. No QEAX, source records, GUIDs, or private ledgers committed.