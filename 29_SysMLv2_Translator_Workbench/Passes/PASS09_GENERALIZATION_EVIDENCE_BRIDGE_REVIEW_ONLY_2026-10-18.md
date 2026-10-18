# Phase 9 — Source-direction evidence to canonical graph review bridge

Added `14_Workbench/registry/runtime/phase9-generalization-evidence-bridge.mjs` and six synthetic tests. The bridge checks candidate evidence schema, caller reconciliation flag, family, explicit EA direction, source connector reference, endpoint IDs and snapshot fingerprint format, then tests proposed specialization against the production canonical graph validator. It returns review-only status; nativeCertified is always false.

**Security and trust limitation:** reconciliationVerified is a caller-supplied boolean, snapshotSha256 is only syntax-checked, and connectorRef is not independently joined to the source ledger or QEAX. This is NOT authenticated trusted evidence. Even status `reviewable` must not be treated as a valid native translation, Workbench production mutation, or authority to emit. The bridge is intentionally not wired to an emitter.

Next: implement a local-only issuer that reads QEAX and Phase 8 ledger together, verifies the source snapshot and complete connector ledger, reconstructs selected evidence without client-supplied claims, and binds to verified graph IDs. Include fake token, stale ledger, and changed-endpoint negative tests. Preserve source rows locally; only aggregate code/test documentation in Test_Vault_.

Workbench requirement: structural and visual specialization separate from lexical containment and composition; source-to-supertype arrow, navigation to both definitions, explicit diagnostic status and local provenance for round-trip. Native emitter remains disabled.