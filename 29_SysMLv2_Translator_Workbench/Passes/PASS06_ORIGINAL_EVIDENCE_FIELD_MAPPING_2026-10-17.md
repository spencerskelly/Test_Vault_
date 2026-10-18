# Pass 6 — Phase 8 original evidence naming correction (2026-10-17)

Corrected `15_Testing/phase8_deferred_evidence_compat.py` so `source_type` attestation reads `raw_source_type`, and `source_stereotype` attestation reads `raw_source_stereotype` in the expanded Phase 8 ledger. Required fields with null or empty values remain unattested; in particular optional source/target roles can be retained as raw blanks, but not declared usable evidence. `source_semantic_assertion` continues to require manual evidence, and native certification remains false.

Commit `62e6ddf`: implementation; commit `60f4e3a`: four synthetic field-mapping tests; commit `19fe397`: CI suite includes the new test. CI combined-status lookup for commit `19fe397` returned no status records; connected commit workflow lookup returned none but only supports PR-triggered runs. Thus this **does not establish CI pass or failure**. Full exact-code tests remain pending because the local GitHub clone is inaccessible. No model-specific data committed.

Pass 6 acceptance remains open for verified CI, full native SysML v2 parser, registry pinned local CLI, and actual BOM data. No eligibility was expanded and native emission remains disabled.
