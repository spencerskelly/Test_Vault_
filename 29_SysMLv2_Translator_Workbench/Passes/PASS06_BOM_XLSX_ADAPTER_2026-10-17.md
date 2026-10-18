# Pass 6 — BOM XLSX adapter (bounded increment)

Committed `15_Testing/bom_xlsx_reader.py` (`47be0fb`) and five tests building a **synthetic XLSX ZIP/OOXML** (`5003ad5`). The adapter has no spreadsheet rewrite action and keeps the source worksheet, workbook ID and Excel row number. Explicit mapping is required for part_number, parent_part_number, quantity and unit. Entirely empty rows are skipped; missing part number and invalid quantity block. Missing units and parent fields stay missing without assumed defaults. Original quantities and units remain raw evidence, not converted into native part ownership or multiplicity. Formula cells are refused until explicit cached-value handling is reviewed.

The adapter builds an XML tree for each selected worksheet and is currently suitable for test and modest-sized XLSX sheets; a later improvement should use incremental XML parsing for large BOMs. Shared source strings and inline strings are handled. This source adapter does NOT read the proprietary ALL_BOMs workbook yet. There is no approved reconciliation of EA and BOM same-named parts and no native v2 emission.

**Verification:** Test file committed, not yet run in a complete GitHub checkout. A real workbook fixture test (local-only), numeric/cached-formula policy, revision/effectivity, alternate part grouping, non-duplicate BOM line identity and atomic downstream outputs remain open. No BOM records or spreadsheet contents entered the methods repo.

Next pass: execute synthetic suite in checkout where possible, add streaming worksheet parsing and implement BOM revision/variant evidence extraction without auto-inferred relationships. User must reply `y` before continuing.
