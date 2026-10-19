# V2 file organization — proposal

Date: 2026-10-18. Status: **PROPOSAL. No folder has been moved.** Approve a phase and it can be executed with the same gates used for the path repair: link audit, MOC coverage, workflow run.

## Two trees, not one

| Tree | What it is | Where it lives |
|---|---|---|
| **Toolchain repository** (this repo) | importer, Workbench, validators, fixtures, decisions, CI | GitHub, `Test_Vault_` |
| **Generated model vault** | the engineering model users open in Obsidian | **SharePoint** (first home); built by the importer, never hand-maintained here |

Everything below is about the first tree, except [SharePoint constraints](#sharepoint-constraints-on-the-generated-vault), which are about the second.

## What is wrong today (measured)

| Problem | Evidence |
|---|---|
| Archive dominates | `100_Archive` is 19.3 of 24.0 MB (80%) and 1,178 of 2,076 tracked files. |
| Decisions in five places | `99System/` (35 notes, a typo'd twin of `99_System`), `26_Definitions` (ADRs plus 49 `STEP_*` notes), `24_Workbench/docs` (80 `GOLDEN_IMPORT_*` + 37 `SYSML_V2_*` notes), `55_Workspace` decision log, the JSON registers. |
| Flat folders | `25_Testing`: 105 `test_*` and 58 other files in one directory, 30 of them `phase8_*`/`phase9_*`. `26_Definitions`: 89 files mixing ADRs, steps, 8 registers, audits. |
| Code and docs mixed | `24_Workbench` holds the Workbench prototype, the registry data, and 118 design notes. |
| Generated files hand-listed | The MOC, census and 13 catalogs were maintained by hand and fell 43 notes behind. |
| CI sprawl | 57 workflows. 6 retired today (see [`.github/workflows-retired`](../.github/workflows-retired/README.md)) because the tools they run no longer exist. Of the 51 left, 14 can fire on `main`/PRs. |
| Tracked build junk | 25 `__pycache__/*.pyc` files are committed; 19 are listed in the migration manifest, so deleting them requires updating that manifest (its checker fails with `MISSING_DESTINATION` otherwise). |

## Recommended: tidy in place, in four phases

Keep the numbered workstream folders (`20_`–`29_`). They are in 1,433 migration-manifest entries and in every workflow; a rename would break everything again. Instead fix the structure *inside* them.

| Phase | Move | Risk | Gate before merging |
|---|---|---|---|
| **1** | `99System/` → `26_Definitions/decisions/native-sysml/` (35 notes). Add `README`s to `88_Reference` and `99_System`. `git rm` the 25 tracked `.pyc` files and drop their 19 manifest entries in the same commit. | low | link audit, MOC coverage, manifest check |
| **2** | `26_Definitions/` into `adr/`, `steps/` (49 + titles), `registers/` (JSON), `audits/`, `concepts/`, `generated/` (matrix, step index, census), keeping `tools/` and `MOC_Catalogs/`. | medium: 247 links point at top-level `26_Definitions` files | repair tool driven by a move manifest, link audit |
| **3** | `25_Testing/` into `unit/` (`test_*`), `gates/` (`phase8_*`, `phase9_*`, `run_gated_*`, `gate_*`, `verify_*`), `fixtures/` (exists). `24_Workbench/docs` into `decisions/` (approved mappings) and `design/`. | medium: every workflow command changes | all 14 main-firing workflows run locally first |
| **4** | Move `100_Archive` out of the repo (separate repo, or a `v1-final` tag plus the archive MOC). Move `29_SysMLv2_Translator_Workbench` (122 research notes) to `88_Reference`. | higher: `check_v2_migration_manifest.py` reads the archive | decouple that check, keep the archive MOC and manifest |

Also, independent of phases:

- **CI:** replace the 51 live workflows with one path-filtered workflow driven by a suite manifest (`ci/suites.yaml`). The dead-path problem then cannot recur, because a suite either points at a file that exists or the manifest check fails.
- **Generated docs:** `V2_NOTE_MAPPING_MATRIX.md` and `V2_STEP_INDEX.md` are generated and checked in CI. Do the same for the census and the 13 catalogs.
- **`.gitignore`:** `__pycache__/` and `*.pyc` are now ignored, so no new ones are committed. Removing the 25 already tracked is in phase 1.

## Alternative: role-based tree (longer term)

```
docs/        adr/  mapping/  steps/  standards/
registry/    one source per mapping; the rest generated from it
tools/       importer/  base-builder/  validators/
plugins/     bootstrap/  workbench/
tests/       unit/  gates/  fixtures/
vault-base/  what ships: schemas, templates, fileclasses, sample
archive/     v1
```

Cleaner, but it renames every path the manifest, workflows and 1,466 links use. Do it only after phases 1–4 have proven the move tooling, and only if you want it.

## SharePoint constraints on the generated vault

Verified against Microsoft's [Restrictions and limitations in OneDrive and SharePoint](https://support.microsoft.com/en-us/help/3125202) (read 2026-10-18):

| Limit | Value | Consequence |
|---|---|---|
| File path, decoded, including name | **400 characters** | Ruleset W-382 removed all path-length checks from the importer. Reinstate a *blocking report*, never shortening (§15.4 intent). |
| OneDrive sync root + relative path | 520 | Users' local sync folder eats part of the budget. |
| Windows Explorer | 256 usable | Matters for anyone using Explorer or tools without long-path support. |
| Each file or folder name | 255 | |
| Invalid | `" * : < > ? / \ \|`, leading/trailing space, `~$` prefix, `_vti_`, `.lock`, `CON`/`PRN`/`AUX`/`NUL`/`COM0-9`/`LPT0-9`, `desktop.ini`, root folder `forms` | The importer must sanitize any EA name containing these before writing a file. |
| Sync | recommended ≤ 300,000 files total | ~35,000 objects is fine; attachments may add up. |

Not verified from primary documentation: a 5,000-item threshold applies to a *view*, and folders help (only a Microsoft Q&A answer was readable). Treat it as advisory; the checker warns above 5,000 items per folder.

[`25_Testing/check_sharepoint_safety.py`](../25_Testing/check_sharepoint_safety.py) enforces the table. This repository's active tree passes: 649 files, longest path 109 characters. Run it on every generated ZIP, with `--sync-root-length` set to your users' real sync-folder path length.

### Risks to test before rollout (not verified here)

1. **Rovo.** Atlassian's [SharePoint connector page](https://support.atlassian.com/organization-administration/docs/connect-sharepoint-to-teamwork-graph/) lists Word, Excel, PowerPoint, PDF and web pages. **Markdown is not listed.** If `.md` is not indexed, Rovo cannot query a vault that lives only in SharePoint as Markdown. Options: ask Atlassian to confirm; generate a Rovo-readable projection (HTML or `.docx` per note, or a Confluence space); or index through a custom connector.
2. **Git inside a synced folder.** The base vault ships the Git plugin. A `.git` directory inside a OneDrive-synced folder is widely reported to cause sync churn and corruption. Decide whether SharePoint or Git is the system of record for the vault.
3. **Shared `.obsidian`.** Obsidian writes per-user layout files into `.obsidian`. Several users on one synced folder may produce conflict copies. The current `.gitignore` excludes `workspace.json` and each plugin's `data.json`; SharePoint has no equivalent.

## Decisions needed

1. Approve phase 1 (safe) and phase 2?
2. Archive: separate repository, or tag plus MOC?
3. Rovo: confirm Markdown indexing with Atlassian, or plan a projection?
4. System of record for the vault: SharePoint or Git?
