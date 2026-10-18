# Pass 8 — Opt-in connector evidence gate in canonical model

Added `validateConnectionEvidence(graph, connection)` to the existing `14_Workbench/registry/runtime/canonical-model.mjs`, reusing the graph node identities. It is a conservative, opt-in candidate gate, not a native emitter.

It requires connector identity/provenance, a part owner, existing part/port usage endpoints, direct owner scope, explicit direction vocabulary, and an independently supplied `directionEvidence=true` flag. It reports diagnostics and always `nativeCertified=false`. Six additional Node tests exercise valid and rejected conditions, bringing `test_canonical_structural_invariants.mjs` to thirteen cases.

Important: a caller setting `directionEvidence=true` is NOT cryptographic or source attestation. The trusted local QEAX phase 8 ledger must supply and verify evidence before calling this gate; it is not wired to the ledger and does not certify roles or direction. The direct-child restriction intentionally defers nested port endpoint paths instead of flattening port/part distinctions. Full connection scope, multi-level feature chains, conjugation, interface ends, binding, and Workbench visual route rules remain open.

The existing automated canonical graph workflow watches the changed files. Its post-commit execution status is not yet verified. No private model data committed. Native emission remains disabled.

Local verification: `node --test 15_Testing/test_canonical_structural_invariants.mjs`.