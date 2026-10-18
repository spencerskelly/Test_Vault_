# Pass 6 — Exact Git blob regression subset: 11 successful tests

Date: 2026-10-17. The existing isolated local directory contained a blob-verified copy of the committed Phase 8 compatibility adapter and original-field mapping tests (the prior four-test gate). Added two more byte-for-byte committed test files; their local Git blob SHA-1 values matched the GitHub `fetch_file` blob SHA:

- `15_Testing/test_phase8_deferred_evidence_compat.py`: `550161fe04853d97d72cf146b8d527875c7a2125` (5 tests)
- `15_Testing/test_phase8_raw_evidence_coverage.py`: `24e4b10d5f57de35abf6ad150f11c90b7a384932` (2 tests)
- Previously verified `15_Testing/test_phase8_original_field_mapping.py`: `64c0d8dab95b006952f2d2d6d1945f7a2bdea563` (4 tests)
- Adapter `15_Testing/phase8_deferred_evidence_compat.py`: `949ccb79e0467e727cb0e03feb632df8e8b44662`

Executed `python -m unittest discover -s /mnt/data/pass06_exact_subset -v`: **11 tests, all pass, zero errors/failures**. Local isolation only, **not an entire clean checkout** or a confirmed GitHub Actions job. The exact Phase 8 normalizer end-to-end modules, independent private-ledger checker test module, source fingerprint suite, native SysML v2 parser and real production BOM validation remain outstanding. No model records, GUIDs, or local ledgers were committed; nativeCertified = 0.
