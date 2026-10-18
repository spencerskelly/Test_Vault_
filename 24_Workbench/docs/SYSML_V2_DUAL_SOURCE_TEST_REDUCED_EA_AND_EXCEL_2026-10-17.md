# Dual-source v2 import test — reduced QEAX + available Excel workbook

Date: 2026-10-17. Test type: **real-source read-only preflight**, not a native import and not a full BOM structural test.

## Scope and forward compatibility
The planned self-contained, browser-operated HTML importer must accept original full QEAX after testing the reduced QEAX, and future Excel BOM workbooks via versioned source profiles, configurable but explicitly reviewed column mappings and fail-closed format detection. No expected row counts, known reduced fixture model IDs, sheet positions or field spellings may be compiled as universal assumptions. Source profile should select by schema/columns and record a hash. Distinguish *known profile with new data* from *unknown format requiring approval*. Ensure large QEAX runs use chunked/streaming analysis and progress/cancellation to avoid browser memory spikes; test with original model as a separate final gate.

## Actual two-source preflight
- EA source: reduced EA_2026_10_15_endgame_mini.qeax. SQLite quick_check `ok`; 11,447 objects, 14,688 connectors, 1,389 packages, 2,208 diagrams; no dangling connector endpoints or duplicate element GUIDs detected. Source preflight passed. Native text generation and parser not executed.
- Excel source: recovered actual workbook `B140594_Alternates_Review_Workbook_v1.xlsx`. 1 sheet `Alternates`, 20 data rows, 45 columns. This is **an alternates review workbook, not an assembly BOM**. It has `Original_PN`, `Compared_PN`, `Row_Type`, `RefDes` but lacks a source column identifying the internal part, parent assembly, and required quantity. The detector correctly reports `BOM_REQUIRED_HEADERS_MISSING`, `BOM_PARENT_CONTEXT_MISSING` and `ALTERNATES_REVIEW_SHEET_NOT_ASSEMBLY_BOM`. Do not invent assembly structure or pass this as a full BOM import.
- The actual original `ALL_BOMs` production Excel source has not been located among accessible source files in this test. **The two-source test is not yet complete as a translation acceptance test**; that file or an explicitly equivalent full BOM source is required to test BOM structure/usage output.

## Executable diagnostic fixture
Local-only CLI preflight `test_import_gate.py` uses SQLite read-only and standard-library XLSX ZIP/XML inspection, outputs aggregate + source column diagnostics. It was run with both real files. Its functionality is a reference behavior for the HTML importer's preflight, not the final browser UI. Raw model-specific ledgers and source workbook are not committed.

## Acceptance matrix
1. Reduced QEAX preflight/count reconciliation; full 11,447 elements and 14,688 connector outcomes after translation.
2. Authentic BOM assembly workbook profile detection, parent/child, quantity/unit, revisions, continuation-row alternates, one UID per distinct part number, 2020 epoch.
3. Unknown BOM sheet headers, relocated columns, type changes, altered quantity formats, formulas and mixed units must produce precise diagnostics and a reviewable mapping proposal. No silent heuristic translation.
4. Deterministic output hash, stable EA CreatedDate/Author UIDs and separate BOM UIDs across two identical imports.
5. Native SysML v2 parser test for all emitted constructs, YAML flagLink with readable note-body reason for unresolved relationships, no source row loss.
6. Browser tests on full original QEAX for progress, memory budget, cancellation, diagnostics export and full staging vault integrity.

**Gate:** GO for reduced EA import development and Excel source-profile/error handling; BLOCK on full BOM translation until original assembly BOM workbook is available and verified. Full native syntax/export acceptance remains blocked pending serializer and pinned parser.
