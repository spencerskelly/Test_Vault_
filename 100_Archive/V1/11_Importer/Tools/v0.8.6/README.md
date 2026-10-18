# EA to MDSE Native Importer v0.8.6

v0.8.6 preserves the v0.8.5 decoder and decode-only attachment check, and implements W-324: no name or folder is shortened for length, and links go to file names.

## Changes from v0.8.5

- **No length-driven shortening.** Removed: filename cutting to fit a path limit, the `folder_N` folder compaction that replaced long folder names (v0.8.3), and duplicate-marker truncation. Kept: the semantic folder rules (repeated ancestor wording, connector wording, folder = note) and the 75-file `folder_N` split, which exists for folder size, not length.
- **Hard stop 400 characters** (`MAX_GENERATED_PATH`). It blocks a run and never cuts. The longest planned path in the EA8647 CSV extract is 379 before folder normalization.
- **One forced cut:** a file name over 255 bytes (`FS_COMPONENT_MAX_BYTES`) cannot exist on macOS or Windows. It is cut at a word boundary, bytes not characters, keeps `~a`, and appears in `Review - Altered Names and Paths.csv`. A folder component over 255 bytes blocks the run. Two note names in the extract are affected.
- **`Review - Long Paths.csv`** (new, in `99_System/11_Import`): every note and attachment path over 212 characters (`LONG_PATH_REVIEW_THRESHOLD`, review only) with uid, id, EA GUID, length, path and link target. It is the input to Post-Import Task 9. Nothing is changed because of it.
- **Links go to the file name.** v0.8.0 to v0.8.5 wrote every link as the full vault path. Now a link is `[[File name]]` when that name is unique among all notes and the base vault's existing notes (case-insensitive); otherwise it is the shortest trailing path that is unique, as Obsidian's "shortest path when possible" writes it. The Run Manifest reports both counts. Evidence CSVs keep full paths so each line stays resolvable (W-156).
- **Decode-only needs the benchmark.** The button refuses to run until `attachment_benchmark.json` is loaded.

## Expected effect on attachments

The 9 attachment path failures in the v0.8.5 decode-only run were 221 to 262 characters. All are under the 400 hard stop, so the benchmark (376 documents, 390 files) should now pass. Not yet run against the real `.qeax`.

## Limits

- Tested in a Node harness with synthetic cases: deep folders kept verbatim, 250-character names kept, over-255-byte names cut at a word boundary, multibyte names, the 75-file split, link-target uniqueness (case-insensitive, base notes counted), and the long-path report.
- Not tested in Obsidian. Whether Workbench and the other plugins resolve a link by Obsidian's resolver, not by comparing path text, is unverified (WB-106 reader in the `MDSE_Workbench` repo).
- Link targets that are paths (names not unique) break if a folder in that path is renamed outside Obsidian. See Post-Import Task 9.
