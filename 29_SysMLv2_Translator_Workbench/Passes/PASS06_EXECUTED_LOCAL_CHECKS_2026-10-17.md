# Pass 6 — Executed local Phase 8 regression and ledger audit

Date: 2026-10-17. This check was freshly executed against files already present in the local private working environment, **not** a checkout of exact GitHub main files.

Command 1: `python -m unittest -v /mnt/data/pass04_validation/test_phase8_local_atomic.py`. Result: **6 tests passed**, covering valid output, duplicates, incomplete ledger, missing ledger, missing aggregate, and forbidden native certification.

Command 2: `python /mnt/data/pass04_validation/verify_phase8_ledger.py <reduced-qeax> <local-private-ledger>`. Results: 14,688 source connectors and 14,688 local ledger rows; duplicate IDs 0; missing IDs 0; unknown IDs 0; raw field mismatches 0; missing endpoint objects 0. Status PASS. Dispositions: deferred_review 6,378; family_candidate 429; orientation_normalized 3,601; owner_endpoint_identified 1,408; role_normalized 2,872. Native certified: 0.

Explicit limits: The synthetic tests and validator match the independent local logic, **not** the exact committed GitHub modules. Full checkout exact-code test results and confirmed GitHub Actions completion have **not** been obtained. Actual BOM ingestion and native SysML v2 parser certification are still pending. No private model records, GUIDs, ledger files, or local private paths were committed.

Next: attain exact checked-out regression CI evidence before closing Pass 6.
