---
title: V2 Repository Stability and Reference-Safe Consolidation Register
status: governed-cleanup-in-progress
updated: 2026-10-18
---
# V2 repository stabilization and consolidation

[Master MOC](../MOC_MDSE_V2.md) · [Complete note census](MOC_REPOSITORY_NOTE_CENSUS_2026-10-18.md) · [Original native decisions](MOC_Catalogs/sysml_decisions_1.md) · [Approved exception audit](V2_APPROVED_EXCEPTION_HANDLING_AUDIT_2026-10-18.md)

## Confirmed progress
- A complete repository Git tree, rather than just the 1,433 original migration paths, was inspected.
- **917 Markdown notes** in the pinned snapshot `5eea630bee387213b1bc1c511b90cc0f679ea6a3` were linked in 13 read-only note catalogs.
- Additional catalog and program pages are linked from the central MOC. The new CI audit evaluates **all currently Git-tracked Markdown notes**, not a fixed historical count, and rejects unindexed entries.
- 35 preexisting SysML v2 approval notes under `99System/10_EA Native Translator/sysml-v2-decisions` were recovered and indexed. **These are original approvals, not new proposals.**
- `MOC_MDSE_V2.md` is the canonical program entry point; `V2_PROGRAM_HOME.md` is a secondary navigator with explicit back-links.
- Historical V1 archive stays immutable as a migration/reference boundary; **no archive file was deleted or moved**.
- Repository README old V1 links were corrected to the actual archived paths.

## Recovered approval precedence
1. Formal OMG SysML v2 and KerML/libraries for native constructs.
2. User-approved decision notes (October 16–17 `99System` corpus, later detailed `24_Workbench/docs/GOLDEN_IMPORT_*`, and October 18 clarifications).
3. Consolidated mapping audit/recovered family inventory, citing authoritative decisions.
4. Versioned executable policy/eligibility registry with test evidence.
5. Historic/provisional rules, V1 mappings, old handoffs and generated index files are references, not authority.

**Do not resolve a disagreement by deleting one copy of the semantic information.** Record the superseded document's successor, version, date and link, retaining original decision and source provenance.

## Consolidation opportunities (reference-safety status)

| Candidate | Evidence | Safe disposition now | Precondition for physical change |
|---|---|---|---|
| Two historic Workbench User Guide copies in `100_Archive/V1/10_Base Vault/Definition/` and `100_Archive/V1/14_Workbench/docs/User Guide/` | Same SHA-1 Git blob in pinned tree; byte-identical historical content | **Retain both; link to a shared archived MOC** | Full inbound Markdown/wikilink/Bases/Canvas/YAML/code/config lookup and UID/ID/effectivity check; existing historical paths must keep resolving |
| `99System/` vs `99_System/` | Similar-looking names, **different content and roles** | **Do not merge**; one is original v2 approvals, other is inherited system schemas/templates/records | Formal authority/UID/schema and code-path migration plan |
| `26_Definitions/V2_PROGRAM_HOME.md` and root MOC | Overlapping navigation, no duplicate model ownership | Root MOC canonical; keep program home as a linked subject-specific index | No destructive moves; all existing backlinks remain valid |
| Historic translator `29_SysMLv2_Translator_Workbench/Passes/` and Workspace handoff notes | Iterative log with source and test evidence; may contain similar summaries | Index and label historical; do not deduplicate based on title | Map source SHA, decision status and attachments before any redirect |
| Old `25_Testing/check_v2_import_kit.py` | Code examines historical V1 paths and release manifest; name can mislead | Mark explicitly historical diagnostic, exclude from v2-runtime path enforcement by exact path only | Update references through a versioned redirect/wrapper and confirm CI, then consider archival path move |
| One-time `stage_v2_archive_migration.py` | Deliberately names pre-migration roots | Retain as historical migration method with explicit audit exception | Never run in active production checkout; verify no runtime dependency |

## Retention classification of all currently indexed notes

- **Approved authority:** `99System` decisions and explicit later user-approved native mapping notes; retain and link to dedicated owner concepts.
- **Active V2 implementation:** `20/21/23/24/25/26` modules/tests/definitions; owner is the tool; review against release/pin.
- **Evidence/history:** `29_SysMLv2_Translator_Workbench`, `55_Workspace`, historical `100_Archive/V1`; retain for audit but index under historical status.
- **System/environment:** `99_System` templates and metadata; retain until replacement/compatibility decision; do not assume native authority.
- **Fixtures:** tests and synthetic model Markdown are validation evidence, not a production model release.
- **Unreviewed content:** catalog-only notes not yet tied to authority/owner/test; preserve and mark `indexed_only`, with no automated deletion.

## Reference-safe cleanup policy
1. No automatic delete or rename; preserve old paths, UID/id, citations and links.
2. For any candidate move: enumerate inbound Markdown, wikilink, frontmatter, canvas, Bases, JSON and source-code references. Report ambiguous basename/aliases separately.
3. Create destination or consolidated successor with explicit provenance. Stage link rewrites/redirect where supported and dry-run all changes.
4. Run full MOC coverage, schema/CI, parser fixture, Obsidian navigation and reimport idempotence tests. Do not merge if any unresolved inbound reference remains.
5. Only then mark the old file retired (retain historical link target where needed); remove physical bytes only under explicit approved retention policy.

## Remaining review workload
- **Indexing** is complete for the pinned 917 notes; **individual technical content review is not**. The highest-value backlog is approved decision recovery, sources used by active runtime, diagnostics and hidden tests, then historical-only notes.
- Build a source-to-authority-to-code/test machine ledger for each original approval, not one generic crosswalk for multiple semantics.
- Verify all current GitHub CI jobs, not only the new note coverage and native kind tests; no release certification implied.
- Confirm traceability and minimum parser/Obsidian acceptance for Use Cases, Occurrences, shared-owned usages, untyped review flags and exception resolutions.
