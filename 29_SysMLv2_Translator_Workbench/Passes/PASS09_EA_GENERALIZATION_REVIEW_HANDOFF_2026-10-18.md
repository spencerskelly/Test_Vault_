# Phase 9 — Review-only EA generalization handoff boundary

The existing canonical model now has a companion, opt-in `reviewEAGeneralizationEvidence()` transport validator. It requires explicit raw EA `Source -> Destination`, subtype-to-supertype role, source connector reference, source snapshot SHA-256, ledger SHA-256, normalized endpoint consistency, and the Phase 8 `orientation_normalized` disposition. It checks canonical endpoint kinds using the production graph validator.

**CRITICAL LIMIT:** The hash strings, provenance and source disposition remain caller-supplied. This module DOES NOT open or independently compare the QEAX, ledger or attestation; `reviewable=true` only means the submitted contract is internally consistent. An adversarial or mistaken caller can fabricate this record. `sourceAuthenticated=false`, `nativeCertified=false`, and `mayEmitNative=false` in every outcome, even when caller claims `verified` or `nativeCertified`. No actual QEAX connection is promoted.

The returned candidate is a non-persisted review projection; it is not a native SysML v2 construct or an authorization to mutate the graph. This adapter intentionally does not auto-attach it to Workbench views. Native emission remains disabled.

Nine synthetic tests cover positive review shape, absent/reversed direction, unsupported role, missing hashes, deferred status, missing endpoints and spoofed certification. CI workflow added; no Actions execution confirmed.

Next: connect a **trusted local issuer** within the QEAX read-only reconciliation script, compare exact raw connector row, normalized result, snapshot and ledger fingerprints at issue time, and ensure the JS consumer only sees a local authenticated record or a host-verified immutable digest. A text field claiming success alone is not evidence. Expand relationship-specific provenance and view behavior only after that gate.

Workbench structural and visual views must keep lexical containment separate from subtype specializations, retain navigation to both definitions and their original connector evidence, validate cycles, and preserve round-trip direction/roles. Binding Port and port-as-part distinctions remain untouched.

Local synthetic test:

```sh
git pull --ff-only origin main
node --test 15_Testing/test_ea_generalization_review_handoff.mjs
```

No raw source elements, GUIDs or ledgers committed.