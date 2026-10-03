# 09_Tools — Current status

This folder holds the current importer, the base build and release-check scripts, the vendored runtime plugins and the vault initialization helpers. Older importers are in `99_System/archive/09_Tools retired importers/` (W-326); none may generate a model.

## Current importer

`EA_to_MDSE_Native_Importer/v0.8.6/EA_to_MDSE_Native_Importer_v0.8.6.html` (candidate; acceptance pending), with `attachment_benchmark.json` and a README in the same folder. It follows:
1. `../10_Docs/MDSE v0.8 Cross-Repository Reconciliation - 2026-10-02.md`
2. `../10_Docs/Translator Definition.md`
3. Workspace Decision Log through W-326
4. relationships 1.35
5. element-types 1.17
6. local-model 0.2

The matched clean base must declare `mdse_release: "0.8.0"`. v0.8 is a clean import into a fresh base; it is never run over an existing vault. What to do before and after each run: [[MDSE Plan - Path to a Golden Model]], sections 4 and 5.

## Important current rules

- source lineage: EA8647;
- one global 30-character identity-token namespace;
- Local Model Source Map authoritative on rerun;
- duplicate name marker `~2`;
- forced alteration marker `~a`;
- no length-driven shortening; hard stop 400 characters; 255-byte filesystem limit forces a cut (W-324);
- attachment failures non-blocking but reconciled;
- all source diagrams must reconcile although initial diagram creation is deferred.

Open improvements to the importer are listed in [[MDSE Plan - Path to a Golden Model]], section 9.

## File status (W-320)

| File | Status | Use |
|---|---|---|
| `EA_to_MDSE_Native_Importer/v0.8.6/EA_to_MDSE_Native_Importer_v0.8.6.html` | hardened implementation candidate; acceptance pending | Release/schema/plugin gates, Local Model 0.2, W-318 naming/path preflight with marker preservation, authoritative Source Map provenance, governed linked-document extraction, Source EA evidence, evidence package and stage-2 review views implemented. Real QEAX acceptance and the WB-106 keepability gate remain. |
| `build-base.py`, `check-release.py`, `update-plugin-lock.py`, `build-plugin-config.py` | current scripts | Base build, release alignment, plugin lock, governed plugin settings. |
| `99_System/archive/09_Tools retired importers/` | archived (W-326) | v0.1 to v0.7 and v0.8.0 to v0.8.5; roles in its README. |
| `Initialize-Vault.sh`, `Initialize-Vault.ps1` | current helpers | Initialize `.vault.yaml` once in a new disposable or real vault. |

The machine-checkable version of this table is `99_System/03_Schemas/mdse-release.yaml`; run `python3 99_System/09_Tools/check-release.py` after any change to tools, schemas or docs. Registry of current files: [[00 - Current State]].


## Base build and release alignment (W-321)

- `build-base.py <output>` generates the lean runtime base from the one positive include list in `mdse-release.yaml`.
- `check-release.py --base <output>` verifies the generated base contains exactly the governed runtime set, the same schemas, and `mdse_release`.
- `check-release.py --workbench <clone>` verifies Workbench version plus current schema fixtures and the frozen Local Model 0.1 compatibility fixture.
- Current State and `mdse-release.yaml` stay in the methodology workspace; they are not duplicated into engineering vaults.
- `Initialize-Vault.sh/.ps1` preserve `mdse_release`.
- W-322 replaces the W-321 Bootstrap deferral: see the controlled plugin release section below.

## Controlled plugin release (W-322)

| File | Role |
|---|---|
| `runtime-plugins/<id>/` | Vendored plugin code for all 11 runtime plugins, plus generated governed `data.json` |
| `build-plugin-config.py` | Generates governed settings, `../06_Fileclasses/` and its link-target Base from the schemas (`--check` to verify) |
| `update-plugin-lock.py` | Generates `.obsidian/plugin-lock.yaml` (schema 2, hashes) and `.obsidian/community-plugins.json` (`--check` to verify) |
| `build-base.py` | Also copies every locked plugin into the base and writes the base `.gitignore` |
| `check-release.py` | Also runs both `--check`s, verifies payload hashes and Bootstrap/Workbench versions, and the plugins inside a built base |

Bootstrap source and docs live in `MDSE Bootstrap/` at the workspace root. How to change a plugin version: `MDSE Bootstrap/README_MDSE Bootstrap.md`.


## Versioned importer layout

Starting with v0.8.0, each importer version lives in its own folder under `EA_to_MDSE_Native_Importer/`. Keep prior versions intact for comparison and acceptance-history review; do not overwrite an earlier version in place.


### v0.8.1 fixes

The first real v0.8.0 whole-model attempt passed QEAX preflight and planning, then exposed two implementation issues. v0.8.1 suppresses invalid Local Model part records when an EA Part folds to a non-Object semantic definition, preserving those cases as note-level/source evidence instead; and it checks required base marker files before reading them so selecting a non-base folder produces a clear validation result. v0.8.0 remains frozen in its own version folder for comparison.


### v0.8.2 path normalization

The next real EA8647 run passed preflight and whole-model planning but found a 236-character path whose folder hierarchy alone left too little room for a readable filename. v0.8.2 keeps the 212-character limit and collapses a deepest navigation folder when that folder repeats the complete note name as its trailing engineering label (for example `Access Control - Authorize from List/Authorize from List.md`). The note name remains unchanged and the path alteration is recorded for review. v0.8.1 remains frozen for comparison.


### v0.8.3 mechanical path compaction

After normalized/redundant folder handling, an overlong folder hierarchy no longer aborts solely because it leaves too little filename space. The importer preserves the engineering hierarchy first, then deterministically replaces the longest contributing non-root navigation folder with a sibling-stable `folder_N` label as needed. The replacement applies to the entire subtree, the 212-character path limit stays unchanged, and original source folder/final output path remain in review evidence.


### v0.8.4 attachment decoding

The first complete semantic whole-model write exposed that all 376 approved t_document attachments were being treated as raw content even though EA stores linked-document BinContent in ZIP payloads. v0.8.4 unwraps the EA ZIP payload before applying the existing image/RTF extraction rules and reports the active BUILD.version in its completion log. The governed target is 376 linked documents producing 390 attachment files, subject to explicit reconciliation of any residual failures.

### v0.8.5 decode-only attachment check

v0.8.5 adds a decode-only mode that decodes all approved linked documents from the real `.qeax` without writing a vault, using the same path-planning and attachment code as the whole-model write. It reports PASS only against `attachment_benchmark.json` (376 documents, 390 files, zero residual) and downloads a per-document CSV. The ZIP decoder now verifies CRC32 and size, reads sizes from the central directory, and fails explicitly on encrypted, ZIP64, unsupported-method or ambiguous multi-entry archives (W-323).

### v0.8.6 no length-driven shortening, links by file name

W-324 removes every rule that cut a name or folder to fit a length: the 212-character filename cut, the v0.8.3 `folder_N` compaction and duplicate-marker truncation. The hard stop is 400 characters and blocks without cutting; a file name over 255 bytes is the only forced cut. Links go to the file name, or the shortest unique path where the name is not unique (v0.8.0 to v0.8.5 wrote full paths). `Review - Long Paths.csv` lists paths over 212 characters for Post-Import Task 9. The v0.8.2 and v0.8.3 sections above describe behavior that W-324 supersedes.

### Importer history (W-326)

The version sections above (v0.8.2 to v0.8.6) describe how the v0.8 line developed. Everything older than v0.8.6 is archived; the sections stay as the change history.
