# Pass 6 — Streaming XLSX source reader

The BOM adapter now uses XML `iterparse` on the selected worksheet and releases each completed row from the parse tree. This avoids retaining the entire worksheet XML in memory. Changes: commits `97bf9fb` and `1af8b75` in `15_Testing/bom_xlsx_reader.py`.

Four synthetic streaming tests were added at commit `0f34c0e`: 1,500 source rows, formula refusal, duplicate Excel row detection, and gap/empty-row provenance. These tests are committed but have NOT been verified executed from a full repository checkout.

Known bounds: shared strings and worksheet metadata remain materialized; the parser assumes an ordinary OOXML worksheet with `sheetData` rows and requires explicit source columns. Do not infer part relationships, revision semantics, units or SysML v2 constructs from the adapter. No real BOM workbook has been tested through this code; no private records are in GitHub.

Next: execute exact synthetic suites in checkout and validate actual BOM workbook locally, using aggregate-only results and a reviewed header mapping. Continue to prohibit native v2 emission until parser and provenance acceptance.
