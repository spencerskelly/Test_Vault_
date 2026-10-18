# Phase 9 — Fail-closed source replay prerequisite

Added `15_Testing/phase9_generalization_evidence_gate.py` and three synthetic tests. The local gate calls the existing complete QEAX/ledger replay first. Failed reconciliation or unequal source and ledger row counts block semantic review; a successful replay permits **review only**, never native certification.

This is intentionally **not yet a trusted direction handoff**. It neither binds an independently issued ledger manifest nor checks a selected connector's source direction, identity, and endpoint mapping in a single atomic operation. A caller-supplied canonical direction still cannot be trusted. Do not connect this helper directly to production canonical specialization edges as source attestation. A later pass must bind per-connector evidence to a verified full-source snapshot and validate raw direction independently, then add production integration and synthetic tampering tests.

No private QEAX or ledger uploaded. Workbench keeps subtype and lexical parent distinct in both structural and visual views; navigation and round-trip evidence remain required. Native emission disabled.

Run: `python3 -m unittest -v 15_Testing/test_phase9_generalization_evidence_gate.py`.
