# Phase 9 — Review-only EA generalization to canonical graph handoff

Added `14_Workbench/registry/runtime/phase9-ea-generalization-review.mjs` and eight synthetic tests. The adapter checks explicit EA source direction, generalization family, normalized source/target agreement, role, nonblank provenance and existing production canonical graph relationship invariants. All outcomes are **review-only** (`nativeCertified:false`, `trustedSourceVerified:false`, `mutation:false`). It does not accept a caller supplied `verified:true` token as authority and does not emit native SysML.

The actual reduced QEAX has a locally reconciled 14,688-connector Phase 8 ledger, but this JS adapter does **not yet have authenticated binding to its per-row source evidence**. Identifiers and directions can be fabricated by an untrusted caller. Thus even `status:review` does not mean provenance has been independently trusted or semantic eligibility approved. Real-source translation remains blocked pending a local-only independently verified issuer and exact snapshot/ledger binding.

The relationship validator preserves lexical containment separately from specialization; Workbench must show separate structural hierarchy and directed visual specialization with endpoint navigation, validation, evidence status and round-trip provenance. No Binding Port collapse or part-usage inference.

Run synthetics with `node --test 15_Testing/test_phase9_ea_generalization_review.mjs`. CI workflow updated but results not confirmed. No QEAX/model rows committed.