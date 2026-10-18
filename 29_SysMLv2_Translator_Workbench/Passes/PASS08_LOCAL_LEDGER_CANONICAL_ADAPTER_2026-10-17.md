# Pass 8 — Local ledger to canonical connection review adapter

Created `14_Workbench/registry/runtime/phase8-ledger-connection-gate.mjs` as an opt-in, fail-closed review adapter. It consumes a projected local Phase 8 ledger record plus an attestation contract and delegates graph scope/type checks to existing `validateConnectionEvidence`.

Safeguards: source connector ID, explicit source direction, resolved source diagnostic status, normalized endpoints, connection family/owner-role evidence, and owner/endpoint graph validation. Outcomes are review-only and always `nativeCertified:false`. Seven synthetic tests were added and the Node CI workflow now runs them together with the existing canonical tests.

**Critical unresolved integration:** The `mdse-phase8-local-ledger-attestation/1` shape is currently a synthetic contract. There is no trusted issuer or independent verification binding this token to the reduced QEAX ledger and its snapshot. The existing Phase 8 ledger has no authoritative `connection_owner_id`, and its current reconciliation families and role mappings do not establish native Connector/Association semantics for this adapter. Consequently no actual source row has been approved and an untrusted caller could fabricate this flag; DO NOT use `valid:true` from this helper as proof of provenance, eligibility, or parser conformance.

Next: build a local-only issuer/verifier tied to complete source snapshot hash, ledger hash, schema version and registry hash, and establish source mapping and connection owner path from EA evidence. Integrate that verified evidence with the canonical graph without uploading source rows. Native emission disabled. Tests are committed but GitHub CI results are not yet confirmed.

Local test: `node --test 15_Testing/test_canonical_structural_invariants.mjs 15_Testing/test_phase8_ledger_connection_gate.mjs`.