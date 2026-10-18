# Pass 6 — Input fingerprint pinning (2026-10-17)

The Phase 8 CLI now fingerprints the **entire local QEAX file and the complete eligibility registry JSON** with SHA-256 before reconciliation, and checks both again before atomic publication. A changed input blocks publication. Each successful local result directory includes `input_attestation.local.json` recording both digests with `native_certified: 0`; this attestation remains local and must not be uploaded with model data.

Changes: input attestation and before/after hash checks in `14_Workbench/registry/runtime/normalize_qeax_phase8.py` (commit `85bd278`); three synthetic attestation tests in `15_Testing/test_phase8_input_attestation.py` (`24edeac`); CI workflow test registration corrected at `9b5c55f`. The exact committed tests and the updated CLI **have not yet produced a verified successful CI run**. The connected status query for previous main SHA returned no status records; that is inconclusive.

Limits: file hashing detects changed bytes but does not make the underlying SQLite and registry reads transactional against concurrent edits. Run against immutable local snapshots and pin a reviewed registry revision. No native syntax parser was used; native emission remains disabled. No real BOM input was validated.
