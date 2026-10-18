# Phase 9 — Local source-backed direction handoff (review-only)

Added `15_Testing/phase9_direction_evidence_gate.py` and five synthetic tests. This reads a single generalization directly from the read-only QEAX and cross-checks its GUID, raw and normalized endpoints, source direction, family, and normalized status against one local Phase 8 CSV ledger row. It does **not** accept a caller-provided direction or `verified` boolean. Output contains only a status/reason and, if matched, `direction: subtype-to-supertype`; always `nativeCertified:false`.

**Security and semantics limitations:** This is a single-row spot check, not an authenticated trusted attestation. It does not independently verify complete ledger coverage or snapshot hashes; run existing Phase 8 full reconciliation and hash checks separately. It does not yet inspect EA connector stereotype, element type compatibility, provenance issuer, source-model meaning, cycle semantics, or official parser evidence. Its candidate result MUST NOT be accepted by the production JS validator as a trusted certification token. Integration to production remains pending. Native emitter stays disabled.

Run locally from Test_Vault_:

```sh
git pull --ff-only origin main
python3 -m unittest -v 15_Testing/test_phase9_direction_evidence_gate.py
```

Next: close missing source stereotypes and diagnostics in the gate; construct a signed/verified local issuer tied to QEAX + ledger + registry fingerprints, and feed trusted evidence into the canonical relation eligibility engine without exposing records. Preserve Workbench lexical containment versus specialization, navigation and private round-trip provenance.