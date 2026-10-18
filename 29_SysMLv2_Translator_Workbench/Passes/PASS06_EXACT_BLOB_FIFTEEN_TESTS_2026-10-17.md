# Pass 6 — Exact blob evidence tests: 15 passed

Date: 2026-10-17. The exact committed test `15_Testing/test_phase8_raw_evidence_values.py` was copied into the existing isolated local verified-code subset. Local `git hash-object` was `a252b455cff4b4c3e9da2481a1646f37e515a26d`, matching the GitHub tracked blob SHA previously returned by connected GitHub fetch. It contributes four cases for blank optional roles, missing source endpoint type, invalid aggregation flag and missing field.

Running `python -m unittest discover -s /mnt/data/pass06_exact_subset -v` executed **15 tests; 15 passed; 0 failures; 0 errors** across four exact-blob test modules:
- `test_phase8_deferred_evidence_compat` (5)
- `test_phase8_original_field_mapping` (4)
- `test_phase8_raw_evidence_coverage` (2)
- `test_phase8_raw_evidence_values` (4)

The source adapter remains the previously GitHub-blob-verified copy. Direct `git clone` remains unavailable because `github.com` DNS fails in the local execution runtime; the full Phase 8 normalizer file and end-to-end tests were **not** copied and executed on this pass. The GitHub combined status query returned an empty status list, which is inconclusive for Actions. Native parser, real BOM ingestion, and full CI verification remain open. No private QEAX source rows or ledgers were committed; nativeCertified=0.
