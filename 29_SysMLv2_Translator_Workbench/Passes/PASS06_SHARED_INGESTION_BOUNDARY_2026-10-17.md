# Pass 6 — Neutral shared ingestion boundary

Added `15_Testing/shared_source_ingestion.py` in commit `8c33e75` and five synthetic tests in commit `261fbf9`. The new boundary yields the existing EA and BOM source-evidence envelopes without converting them into target SysML v2 or MDSE semantics. Identity includes `(source_kind, snapshot_id, record_kind, source_key)`. Thus a BOM line, EA element and BOM part cannot be implicitly merged because of overlapping source keys or names.

An aggregate audit returns total counts, per-kind counts, duplicate source identities and nativeCertified=0 without source rows or IDs. Duplicate identity blocks. The EA iterator keeps a read-only database connection open while yielding; it closes the connection on full exhaustion or generator close. BOM ingestion delegates to the explicit-header worksheet reader and retains original quantity, units and row location.

Five synthetic tests cover distinct EA/BOM identity, duplicate detection, no source fields in aggregate report, unsupported EA category and missing snapshot rejection. Tests were committed but **not run from a complete repository checkout**, so they are not yet accepted. No actual ALL_BOMs workbook has been ingested and no private source data was committed.

Remaining: execute tests from checkout, verify EA iterator behavior against the reduced QEAX, run the actual production BOM locally when available, add duplicate BOM-line and revision/effectivity reconciliation rules, and implement a durable non-semantic source manifest with explicit disposition for each row. Native SysML v2 emission stays disabled.
