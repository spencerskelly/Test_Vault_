# Phase 9 — Mandatory canonical specialization orientation

The production `validateCanonicalRelationships()` now rejects any `specialization` edge without `direction: subtype-to-supertype`. Previously it only rejected an explicit wrong direction and inadvertently allowed missing direction. Updated nested Workbench synthetic fixture and canonical relationship tests; added missing-direction negative regression and preserved two-node cycle test with explicit direction.

**Trust boundary:** an asserted direction string is not independent EA provenance attestation. This is a necessary representation invariant, not proof that an actual source connector is correctly oriented. Phase 8 local ledger and evidence verification must supply provenance and independently verified roles before an actual model edge can qualify. No native emitter or Workbench visual rendering enabled.

Node suite on Mac (execution not yet confirmed):

```sh
git pull --ff-only origin main
node --test 15_Testing/test_phase9_nested_definition_workbench_contract.mjs 15_Testing/test_phase9_canonical_relationship_validator.mjs
```

Workbench requirements remain: explicit directed edge subtype to supertype, distinct lexical containment, navigation to both definitions, source direction evidence and round-trip local provenance, no automatic conversion to composition or a PartUsage. Native certification is zero.