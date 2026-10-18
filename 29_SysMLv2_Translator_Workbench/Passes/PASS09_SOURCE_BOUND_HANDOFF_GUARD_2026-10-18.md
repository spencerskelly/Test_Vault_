# Phase 9 — Source-bound specialization review gate hardening

Extended existing `phase9_source_bound_specialization_review.py` with `inspect_verified(...)`, an opt-in fail-closed gate requiring both complete QEAX-to-ledger source-row integrity verification and full Phase 8 normalization replay. These checks must precede any canonical graph specialization review. Required expected connector count defaults to 14,688.

Added four synthetic tests covering tampered row integrity, failed replay, count mismatch, and review-only success. No private QEAX or ledger committed.

**Important:** existing CLI `--qeax --ledger --graph` remains the original unverified diagnostic-only `inspect` path. It is **not** the trusted wrapper. Do not treat that CLI output as source-attested. The wrapper is callable in Python but its separate CLI, trust issuance and real graph materialization are next tasks. The previous Phase 8 input attestation is self-authored; integrity checks establish consistency, not independently trusted EA semantics. A clean review still reports `native_certified=0` and `may_emit_native=false`.

Test from repository:

```sh
git pull --ff-only origin main
python3 -m unittest -v 15_Testing/test_phase9_verified_specialization_gate.py
```

Workbench future gate: structural subtype distinct from lexical nesting; visual directed subtype→supertype; navigable source and target; validation/provenance bound to immutable local snapshot; round-trip without source leakage. No emitter enabled.