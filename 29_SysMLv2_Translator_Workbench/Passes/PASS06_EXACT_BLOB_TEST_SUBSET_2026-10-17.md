# Pass 6 — Exact committed evidence-adapter subset verified

Date: 2026-10-17. Used the connected GitHub file API to obtain two tracked files, copied their exact bytes into an isolated local directory and verified each `git hash-object` against the GitHub blob SHA before execution.

- `15_Testing/phase8_deferred_evidence_compat.py`: SHA `949ccb79e0467e727cb0e03feb632df8e8b44662`
- `15_Testing/test_phase8_original_field_mapping.py`: SHA `64c0d8dab95b006952f2d2d6d1945f7a2bdea563`
- `python -m py_compile` passed on both files.
- `python -m unittest -v test_phase8_original_field_mapping`: **4 tests run, 4 passed, 0 failures/errors**.

Tests covered EA original-kind alias recognition, blank optional endpoint roles, absence of source semantic assertions, and missing original type. This is verification of the **exact tracked file contents for this subset**, **not** a complete repository checkout, a full Phase 8 regression suite, a confirmed GitHub Actions run, or a native SysML v2 parser result. The original reduced QEAX and private ledgers were not copied to GitHub. Emission remains disabled; `nativeCertified=0`.

Next: verify further exact-blob tests and the full integration module, then capture a successful CI job URL and result. The actual production BOM and native SysML v2 parser are still outstanding.
