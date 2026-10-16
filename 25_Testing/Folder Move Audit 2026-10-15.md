# Test_Vault_ — Folder move impact audit

**Date:** 2026-10-15
**Commit observed:** `1fe603a03ebbbe9d8c956d389fc905b4c8d6957c` (54 changed paths)
**Result:** **NOT VERIFIED / LIKELY BROKEN v1 release tooling**. This is a source-level audit only; no full checkout, test suite or CI was executed.
**Scope:** New numbered v1/v2 layout, navigation, release path contracts and some high-risk executable references.

## Verified current layout

| Area | V1 | V2 |
|---|---|---|
| Base | `10_Base Vault` | `20_Base Vault` |
| Importer | `11_Importer` | `21_Importer` |
| Bootstrap | `13_Bootstrap` | `23_Bootstrap` |
| Workbench | `14_Workbench` | `24_Workbench` |
| Tests | `15_Testing` | `25_Testing` |
| Definitions | `16_Definitions` | `26_Definitions` |
| Translator planning | — | `29_SysMLv2_Translator_Workbench` |
| Cross-version governance | `55_Workspace` | Shared references only |

## Confirmed stale path references in active code/configuration

- **P0:** `10_Base Vault/Definition/mdse-release.yaml` still resolves `Importer/Tools/...`, `Importer/Definition/...`, `Base Vault/Tools/...`, `Base Vault/Runtime/...`, `Base Vault/Definition/...`; moved destinations are numbered. Also inspect `99_System/...` and any renamed schema roots.
- **P0:** `10_Base Vault/Testing/check-release.py` opens `Base Vault/Definition/mdse-release.yaml`, scans `Importer/Definition`, accesses `00_Workspace` and `Importer/Tools`. Several are moved, so its checks are not reliable in current form.
- **P0:** `11_Importer/Tools/v0.8.19/sync_source_profile.py` derives the repository root correctly but points at unnumbered `Importer/Definition` and `Importer/Tools` (lines 7–8).
- **P0/P1:** `10_Base Vault/Tools/v0.8.0-r2/build-base.py` contains unnumbered `Base Vault/Definition/mdse-release.yaml` references. Check all resolved input paths and runtime output before changing.
- **P1:** `15_Testing/consolidation/step19_generated_base.py` and `step17_registry_review.py` resolve `Base Vault/Definition`; `step17_registry_review.py` also uses prior testing and workspace folder names.
- **P1:** `10_Base Vault/Tools/v0.8.0/build-plugin-config.py` references unnumbered `Base Vault/Runtime/Plugins`; check both versions of build-plugin-config, plugin lock and release payload.
- **P2:** historical consolidation docs and Workbench manuals still mention `55_Workbench`, `66_Testing`, `00_Workspace`, `Definitions/Properties`; historical notes may intentionally preserve old paths, but living instructions need updating.
- **P2:** `77_Definitions/Properties/Property Dictionary.base` contains a filter for `Definitions/Properties` rather than its new numbered location; likely breaks the Obsidian Base query.

## What has been repaired

- Root `README.md` navigation rewritten for the numbered v1/v2 directories and linked to this report.
- V2 documentation previously added to `26_Definitions` and its research/translator work tracked in `29_SysMLv2_Translator_Workbench` (as seen in the organization commit).

## What has not been validated

- No cloned local repository checkout, complete filename enumeration, static full-tree link scan or CI run was available through this inspection.
- No build, importer, Workbench, Bootstrap, plugin packaging, Obsidian UI or runtime tests executed.
- Existence of certain directories does **not** certify `main` is operational.

## Required repair order (before claiming success)

1. **Inventory all tracked files** at HEAD and build a complete old-path -> new-path manifest. Review root and release-owned path rules; do not globally replace provenance/history text.
2. **Update v1 release manifest** to actual numbered paths with a strict distinction between source repo paths and output generated-vault paths.
3. Update v1 executable source-profile sync, base builder/config generator, release checker, CI workflow locations, and consolidation test scripts consistently with the manifest.
4. Run `check-release.py`, source-profile sync `--check`, base generation, Workbench npm tests/build and all applicable GitHub Actions on the moved tree; record exact commands, commits and outputs.
5. Audit Markdown links, Wikilinks, Obsidian Bases, Canvas references and generated fileclass configuration. Include dynamic strings in scripts.
6. Independently validate v2 README and planned tools; do not claim a v2 runtime exists based on scaffolding.
7. Re-run the same checks against a clean clone, with no untracked compatibility copies masking stale references. Preserve explicit rollback commit/backup before code-wide path changes.

## Approval / compatibility

This folder move is a **path migration**, not permission to change v1 semantics or to mix v1/v2 schemas. Fixes applicable to both require separate validation and approval. Actual release eligibility remains pending until executable acceptance evidence is recorded.
