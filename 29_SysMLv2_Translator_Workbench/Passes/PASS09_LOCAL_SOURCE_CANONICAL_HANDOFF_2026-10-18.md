# Phase 9 — Local EA source / ledger / canonical candidate handoff

Added `15_Testing/phase9_local_source_to_canonical_candidate.py` as a pure, local-only fail-closed consistency guard. It cross-checks raw EA connector identity, source/target, explicit direction, provisional Phase 8 normalized role, and canonical definition-kind pair; it returns a review-only specialization candidate with explicit subtype-to-supertype direction and source provenance.

This is **not** a trusted attestation issuer. The caller could forge both source and ledger dictionaries, and the canonical endpoint map is passed by the caller. A `candidate` result MUST NOT be interpreted as eligibility, certified provenance, semantic correctness, parser acceptance, or permission to emit. `native_certified` remains false for every result. Inputs must be populated locally from an independently verified, read-only QEAX snapshot and its matching Phase 8 ledger before this becomes a production pipeline.

Five synthetic fixtures test candidate noncertification and rejection of unsupported direction, identity mismatch, reversed ledger endpoints and usage-as-definition. These test methods have been committed; passing test execution is not yet observed.

Remaining work: establish a source-backed reader that binds input QEAX SHA-256, ledger/registry hashes, connector ID and canonical endpoint origin IDs and checks all assertions independently; integrate outcomes with the production JS `validateGraph` specialization edge and Workbench structural/visual views. Preserve nesting separately, never infer part composition from lexical ownership. Record relationship evidence and round-trip locally, not in the public repository.

Mac test:

```sh
git pull --ff-only origin main
python3 -m unittest -v 15_Testing/test_phase9_local_source_to_canonical_candidate.py
```

Native emission stays disabled.