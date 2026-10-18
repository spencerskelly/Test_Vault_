# Pass 6 — Shared source-evidence envelope

Implemented `15_Testing/source_evidence_contract.py` (commit `45d6e09`) and six synthetic checks in `15_Testing/test_source_evidence_contract.py` (commit `dc2ca46`). Both EA and Excel BOM records use a common neutral envelope with a source type, snapshot, record kind, source key, raw evidence, provenance and `uninterpreted` disposition. EA retains EA row identity/GUID and connector orientation; BOM retains workbook, worksheet and row location. Same-looking source IDs are not merged. No native SysML v2 assertion is authorized by source loading.

No BOM workbook has yet been loaded by this module: `bom_envelope` is an adapter contract, not a workbook parser. The six tests are committed but not yet run from a full checkout. Parent BOM ownership, part-number uniqueness, units/quantity, revision and effectivity require separate evidence and rules before conversion. Source records must remain local and out of methods GitHub.

Next small pass: implement read-only XLSX worksheet iteration and map rows into the BOM neutral envelope, including explicit field mapping, empty-row policy and quantity/unit provenance. The eventual semantic translator must use the candidate registry only after rule validation; no native output yet.
