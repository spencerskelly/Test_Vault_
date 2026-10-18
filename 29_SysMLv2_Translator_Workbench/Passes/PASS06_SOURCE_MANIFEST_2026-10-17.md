# Pass 6 — Source disposition manifest

Created `15_Testing/source_disposition_manifest.py` (`03c7422`) and six synthetic tests (`6c57146`). Every source evidence envelope gets an order-independent identity, SHA256 fingerprint of raw source and provenance, initial `uninterpreted` disposition, and a mandatory reason. Unknown or prematurely accepted native statuses are forbidden; duplicate source identity fails closed. Local-only manifest entries can contain source keys and fingerprints and must **never be committed**. Only `aggregate()` output is suitable for public methods reporting.

Tests cover deterministic ordering, EA/BOM isolation, duplicate rejection, invalid disposition, missing reason, and aggregate-only privacy. Tests are committed but not yet executed in a complete checkout. The manifest is currently in-memory, so very large datasets require a streamed/spooled local implementation before production. This is evidence bookkeeping, not SysML v2 translation.

Next: run full synthetic suite, apply local-only manifest to reduced QEAX, check exactly all categories, and implement a safe streaming manifest format with atomic private writes. Keep all model rows, keys, hashes, and GUIDs outside Test_Vault_.
