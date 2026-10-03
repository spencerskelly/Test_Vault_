# EA to MDSE Native Importer v0.8.5

v0.8.5 preserves the v0.8.4 semantic write path and adds a stricter linked-document decoder plus a decode-only attachment check.

## Why this version exists

v0.8.4 fixed the EA ZIP wrapping of linked-document `BinContent`, but it could only be verified by a full 30,298-note fresh-base run. v0.8.5 verifies the whole linked-document population against the real `.qeax` in seconds, writes nothing, and reports PASS or FAIL against a benchmark file.

## Changes from v0.8.4

- **Decode-only attachment check.** Needs only the `.qeax` and a PASS plan (no output folder). It runs the same identity, path-planning (`planOutputPaths`) and attachment (`attachmentReconciliation`) code as the whole-model write, writes no vault, and downloads `Attachment Reconciliation - Decode Only.csv`.
- **Benchmark gate.** Load `attachment_benchmark.json` (this folder) with the Benchmark file picker. Nothing is built in: no benchmark loaded is FAIL. PASS requires 376 approved documents (247 ModelDocument + 129 ExtDoc), 376 decoded OK, 390 attachment files, and zero residual documents. Summary line: `ATTACHMENT DECODE v0.8.5 | docs 376/376 | files 390/390 | residual 0 | PASS`. The same line is logged and written to the Run Manifest by a full run.
- **Decoder hardening.** Sizes, CRC and flags come from the ZIP central directory (data descriptors work). CRC32 and size are verified per entry. Encrypted, ZIP64 and non-stored/deflate entries fail explicitly. With several entries, the single entry that decodes as RTF or a known image is used; otherwise `multi_entry_ambiguous`.
- **Outcome classes** per document: `OK`, `NO_PAYLOAD`, `ZIP_ERROR` (reason code in brackets), `UNSUPPORTED_TYPE`, `IMAGE_ERROR`, `PATH_ERROR`, `OWNER_ERROR`, `SKIPPED` (not ExtDoc/ModelDocument). Every document yields exactly one row; one bad row cannot hide the rest.
- `Attachment Reconciliation.csv` in a full run keeps its v0.8.4 columns. The decode-only CSV adds container, ZIP entry count/name, compression method, decoded bytes, payload type, embedded image count, files produced, outcome, reason and SHA-256 of the decoded payload.

## Limits

- Verified in a Node harness against synthetic ZIP fixtures (stored, deflate, data descriptor, multi-entry, nested, CRC mismatch, encrypted, bzip2, truncated). Not yet run against the real EA8647 `.qeax`.
- The benchmark holds totals only. There is no per-document expected file count, so a wrong split between documents with the right total would not be caught by the benchmark; use the CSV for that.
- Decode-only does not scan an output base, so it allocates `uid` values without existing-note reservation. File names and paths do not depend on `uid`, so the path-length and collision checks match the full run.
- Semantic write path, folder subdivision and WB-106 are unchanged.
