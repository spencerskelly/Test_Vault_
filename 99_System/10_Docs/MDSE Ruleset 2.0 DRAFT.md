# MDSE Ruleset 2.0 (DRAFT)

Status: DRAFT, 2026-10-19. Not in force. Ruleset 1.23 governs until 2.0 is baselined by owner approval.

Purpose: one place for every rule that governs the MDSE vault, importer, Workbench, Bootstrap, and AI processes. Each rule has an ID, a source, a status, and an enforcing test. Rules from 1.23 and the v2 ADRs are carried over. Where two sources conflict, the conflict is listed in section 14 and the rule is marked open.

Rule IDs use the form `R-<section>.<n>`. Source references use the document name and section, for example `1.23 §16.4` or `ADR-V2-07`.

## 1. Identity and types

- **R-1.1** Every model note has an immutable 30-character `uid` in the form `yyyyMMddHHmmssSSS` plus a 13-character author code. The `uid` never changes after creation. Source: 1.23 §16.1, `AI_INSTRUCTIONS.md`. Status: approved.
- **R-1.2** `id` is `PREFIX-NNNNN`, with the prefix from the class in `element-types.yaml`. Never reused. Source: `AI_INSTRUCTIONS.md`. Status: approved.
- **R-1.3** The primary reusable engineering type is `Object`. `Thing` is deprecated. Source: 1.23 §1.1. Status: approved.
- **R-1.4** `type` is the semantic class. `subtype` is an approved classification within that type. `kind` is deprecated. Source: 1.23 §1.1. Status: approved.
- **R-1.5** `subtypeOf` is used only for a reusable invariant semantic distinction. Ordinary data or configuration variation is not a `subtypeOf`. Source: 1.23 §2. Status: approved.
- **R-1.6** Notes in `99_System` carry no `type` or `subtype`. Source: 1.23 §1.1 (W-243). Status: approved.
- **R-1.7** Search for an existing authoritative definition before creating a new one. Prefer reuse, then instance, then specialization, then decomposition, then a new concept. Source: 1.23 §1. Status: approved.

## 2. Note format and templates

- **R-2.1** A model note is created from the class template in `99_System/05_Templates`. Template properties keep their order (`type`, `subtype`, `id`, `uid`, `status`, `tags`). Source: `AI_INSTRUCTIONS.md`. Status: approved.
- **R-2.2** Template fields are always present in a note. Source: decision recorded in the MDSE definition, 2026-10-19. Status: approved by owner.
- **R-2.3** A source field that has no data and is not a template field is not written to the YAML. Source: decision recorded in the MDSE definition, 2026-10-19. Status: approved by owner.
- **R-2.4** A note has two zones. The user zone is above the first managed heading and is never rewritten by tooling. The managed footer is below it. Source: ADR-V2-06. Status: proposed (owner confirmation of Q1–Q6 pending).
- **R-2.5** `## SysML v2` is the last `##` section and holds exactly one fenced `sysml` block. A second `sysml` fence is an error. Source: ADR-V2-06. Status: proposed.
- **R-2.6** `status` is set to the template default. Only a person advances it. Source: `AI_INSTRUCTIONS.md`. Status: approved.
- **R-2.7** `eaGUID` appears only at the bottom of notes translated from EA. It is not in frontmatter. Source: `AI_INSTRUCTIONS.md`, MDSE definition principles. Status: approved.
- **R-2.8** Notes are never deleted. A note is retired by setting `status` to Retired. The `id` stays reserved. Source: `AI_INSTRUCTIONS.md`. Status: approved.

## 3. Relationships

- **R-3.1** Only relationships defined in `relationships.yaml` are used. A relationship with no endpoint rule is not restricted, and `tracesTo` is provisional until replaced. Source: `AI_INSTRUCTIONS.md` (W-272, W-277, W-288). Status: approved.
- **R-3.2** Author the forward relationship only. Inverses are generated and must match. Where they disagree, the forward field wins. Source: 1.23 §4, `AI_INSTRUCTIONS.md` (W-275). Status: approved.
- **R-3.3** State ownership: `hasState` runs from Object or Condition to Condition. `stateOf` is the generated inverse. Source: `relationships.yaml` 1.36. Status: STALE in 1.23 §4 (W-291, W-292), which names State and State Machine. W-384 (2026-10-05) replaced the first-class Function, State, Design, Step, and Port classes with Behavior and Condition. Needs owner confirmation of the current wording.
- **R-3.4** Requirement scope uses `appliesTo`. Verification uses `verifies`. Which classes may `satisfies` a Requirement must be re-read from `relationships.yaml` 1.36. Source: 1.23 §7 (W-327). Status: STALE. 1.23 §7 names Function, Design, State, and State Machine, which W-384 removed as classes.
- **R-3.5** Behavior controlled by the modeled product is distinct from externally controlled behavior (Use Case). Human or external steps are not product behavior. Source: 1.23 §5. Status: wording STALE. 1.23 §5 says "Function"; W-384 uses Behavior.
- **R-3.6** Folder placement is navigation only. It creates no semantic relationship. Source: 1.23 §1, §9. Status: approved.
- **R-3.7** A repeated identical semantic relationship is not used to express quantity. Quantity is Local Model `multiplicity`. Source: 1.23 §15.7. Status: approved.

## 4. Import, merge, and rerun

- **R-4.1** Import is mechanical. The importer applies the Ruleset and does not interpret. Source: MDSE definition. Status: approved by owner.
- **R-4.2** Import is additive. An import never deletes existing content. Source: MDSE definition. Status: approved by owner.
- **R-4.3** An empty YAML property may be filled by an import. Source: MDSE definition. Status: approved by owner.
- **R-4.4** Content that does not match existing body content is added to the body. Source: MDSE definition. Status: approved by owner.
- **R-4.5** A change to any existing value requires approval, including EA-owned fields. Approval is given before the run (pre-approval, by field selection in the Start step) or after the run (review approval). Source: MDSE definition; supersedes 1.23 §16.4 (see section 14). Status: approved by owner; amendment pending.
- **R-4.6** Pre-approval applies to all notes in the run. Source: MDSE definition. Status: approved by owner.
- **R-4.7** A conflict is content that contradicts existing YAML, v2, or body content and is not approved for change. It is not applied. It is listed in the body with a `flagConflict` callout for engineer review. Source: MDSE definition. Status: approved by owner.
- **R-4.8** An engineer resolves a conflict by approving a change or by selecting the correct data by hand. Source: MDSE definition. Status: approved by owner.
- **R-4.9** A source record that disappears is reported with a `flagImport` callout. It is not deleted. This applies to EA-owned relationships. Source: MDSE definition; supersedes 1.23 §16.4 removal rule (see section 14). Status: approved by owner; amendment pending.
- **R-4.10** Every change to an existing file is listed in one dated changelog per import run. Each entry links the changed file, describes the change, and flags any conflict. Source: MDSE definition. Status: approved by owner.
- **R-4.11** Importing the same input again produces no changes and no changelog entries. Source: MDSE definition; 1.23 §15.6 (completion). Status: approved by owner.
- **R-4.12** A content change made by an engineer is not changed by an import unless approved. Source: MDSE definition; 1.23 §16.4. Status: approved.
- **R-4.13** Add-onto-existing matches a note by `uid`, not by path. Source: ADR-V2-07. Status: accepted.
- **R-4.14** A run is complete only when every planned entity reaches an explicit terminal state: written, intentionally suppressed by rule, or explicitly failed. There is no unexplained remainder. Source: 1.23 §15.6. Status: approved.

## 5. Flags

- **R-5.1** A flag is an Obsidian callout whose type names the issue. Types: `flagImport`, `flagConflict`, `flagLink`, `flagNote`. New types are added to this section before use. Source: MDSE definition. Status: approved by owner.
- **R-5.2** The importer and AI processes add flags. Only an engineer removes a flag, after the issue is resolved. Source: MDSE definition. Status: approved by owner.

## 6. BOM scope and revisions

- **R-6.1** The vault holds the latest revision of each product in scope. Superseded revisions are not imported. Source: ADR-V2-08. Status: accepted.
- **R-6.2** One note per PartNumber. A part's properties come from its latest revision. Source: ADR-V2-08, MDSE definition. Status: accepted.
- **R-6.3** A usage records the child revision pinned by the parent. Parent PN and line number identify a usage. Source: ADR-V2-08. Status: accepted.
- **R-6.4** A PN whose latest revision cannot be determined is reported and not imported. Source: ADR-V2-08. Status: accepted.
- **R-6.5** Revision strings are stored as exported, not normalized. Source: ADR-V2-08. Status: accepted.
- **R-6.6** A child part's body lists each assembly that uses an older revision of it, with that usage. Source: MDSE definition. Status: approved by owner.
- **R-6.7** A parent that pins a child revision different from the child's latest revision is flagged with `flagConflict`. Source: MDSE definition. Status: approved by owner.
- **R-6.8** Alternate-part rows with a blank PN attach to the PN above them. They are not parts. Source: ADR-V2-08. Status: accepted.
- **R-6.9** Drawing-only lines are recorded as document references and excluded from quantities. Source: ADR-V2-08. Status: accepted.

## 7. Naming and paths

- **R-7.1** Use the shortest human-readable name that stays unambiguous in context. Source: 1.23 §15.1. Status: approved.
- **R-7.2** UID is the stable machine identity. The filename is a locator and may carry context for uniqueness. The visible heading is the engineering name. Source: 1.23 §15.1. Status: approved.
- **R-7.3** Default to EA Name. EA Alias is used only when Name is unsuitable for people. The original Name is kept in provenance. Source: 1.23 §15.1. Status: approved.
- **R-7.4** Ports use the filename form `i<owner> - <Port Name>.md`. The `i` convention is for Ports only. Source: 1.23 §15.1. Status: approved.
- **R-7.5** Duplicate names take `~2`, `~3`. Forced alterations take `~a`, `~b`. Numeric markers are duplicate-review items. Alphabetic markers are altered-name review items. Source: 1.23 §16.3. Status: approved.
- **R-7.6** Note filenames are unique across the vault, case-insensitive. Links use the filename: `[[File name]]`. Source: 1.23 §15.4a (W-382). Status: approved.
- **R-7.7** There is no total path-length limit. A single file or folder name the filesystem cannot create is shortened or blocked deterministically. Source: 1.23 §15.4 (W-382). Status: approved.
- **R-7.8** Folder structure follows the model's package nesting. A nested element's folder is named for its parent. Source: 1.23 §9. Status: approved.
- **R-7.9** Do not create mechanical `folder_N` subdivisions. Source: 1.23 §9 (W-347 era). Status: approved.
- **R-7.10** Automatic navigation files (`README`, `BASE_local`, `BASE_all`, `CANVAS`) are created only for the primary top-level domain folders. Source: 1.23 §9.1. Status: approved.
- **R-7.11** Imported filenames must not collide with reserved infrastructure names (`Template - `, `Rule - `, `README_`, `BASE_`, `CANVAS_`). A collision with an engineering note is blocking. Source: 1.23 §15.2. Status: approved.

## 8. Local Model

- **R-8.1** Local records use a kind prefix and a 30-character token: `part-`, `ep-`, `conn-`, `flow-`. The token is globally unique and never reused. Source: 1.23 §15.7, §16.1. Status: approved.
- **R-8.2** Persisted references use native Obsidian block links. The block ID equals the local ID. Source: 1.23 §15.7. Status: approved.
- **R-8.3** Part and endpoint records may carry `usage: standard | variant | option`. Omission means `standard`. Connections and flows carry no `usage`. Source: 1.23 §15.7. Status: approved.
- **R-8.4** The Local Model writer format is the `writableVersion` in `local-model.yaml` (currently 0.5). Readers support 0.1 to 0.5. Reading an older version never rewrites it. Source: `local-model.yaml`, W-384, W-398. Status: approved. 1.23 §15.7 names 0.2 and is STALE.
- **R-8.5** Local Model usages are SysML usages in v2. Stable tokens for v2 usages are an open question (ADR-V2-06 Q1). Status: open.

## 9. SysML v2 section

- **R-9.1** The `## SysML v2` section is the sole authoritative native text. It is read and changed through the shared parser and validator with an optimistic version check. Source: `MDSE_V2_0_SHARED_NOTE_AND_RELEASE_CONTRACT`. Status: proposed.
- **R-9.2** The parser gate is run in CI and on a maintainer's machine. The ZIP carries a parser-check report. Workbench marks the report stale after any SysML change. Source: ADR-V2-07 (owner accepted 2026-10-19). Status: accepted.
- **R-9.3** Changes to the `## SysML v2` section by import require approval (R-4.5). Source: MDSE definition. Status: approved by owner; amendment pending (see section 14).

## 10. Releases and versions

- **R-10.1** Each issued importer is paired with one base vault using the same semantic release version. The importer checks it before writing. Source: 1.23 §15.8. Status: approved.
- **R-10.2** Relationship and element schemas keep their own version numbers. Source: 1.23 §15.8. Status: approved.
- **R-10.3** The Run Manifest records importer release, base release, relationship-schema version, and element-schema version. Source: 1.23 §15.8. Status: approved.
- **R-10.4** The runtime base carries `mdse_release` in `.vault.yaml`. Methodology material is not copied into engineering vaults. Source: 1.23 §15.9 (W-321). Status: approved.

## 11. Integrity and completion

- **R-11.1** Before handoff: YAML parses, `id` and `uid` are unique, links resolve, inverses are synchronized, Functions have performers where applicable, and requirement basis, satisfaction, and verification gaps are visible. Source: 1.23 §14. Status: approved. Note: 1.23 §14 cites `Translator Definition.md` §10, which is not in the repo (see section 14).
- **R-11.2** Canvas geometry is presentation only. It never creates a semantic relationship. Source: `AI_INSTRUCTIONS.md`. Status: approved.

## 12. AI processes

- **R-12.1** Every AI process has a written instruction file and an ID. The index is in `AI_INSTRUCTIONS.md`. Source: MDSE definition. Status: approved by owner.
- **R-12.2** AI processes do not edit model files unless the process is a note-creation process under R-2.x. Changelog review (AI-CR-01) is report-only. Source: `99_System/02_AI/processes/AI_Process_Changelog_Review.md`. Status: approved.
- **R-12.3** AI does not create or split vaults. It may recommend a split. Source: 1.23 §12. Status: approved.
- **R-12.4** AI does not invent source facts. Source: `AI_INSTRUCTIONS.md`, 1.23 §6. Status: approved.

## 13. Change control

- **R-13.1** A rule changes only by a dated decision that names the rule it replaces. Superseded rules are marked, not deleted. Source: this draft. Status: proposed.
- **R-13.2** Each rule in this Ruleset has an enforcing test or is listed as a gap. Source: this draft. Status: proposed.

## 14. Open conflicts

| # | Conflict | Sources | Proposed resolution |
|---|---|---|---|
| C-1 | EA-owned fields replaced on rerun | 1.23 §16.4 vs R-4.5 | R-4.5 replaces it. Amend 1.23 §16.4. |
| C-2 | Removed EA relationships removed on rerun | 1.23 §16.4 vs R-4.9 | R-4.9 replaces it. Amend 1.23 §16.4. |
| C-3 | Same `uid` with different `type` is reported and not written | ADR-V2-07 vs R-4.7 | Conflict listed in body with `flagConflict`. Amend ADR-V2-07. |
| C-4 | `subtype`, `eaType`, `sourceRole`, `primarySymbol` refreshed from EA | ADR-V2-07 vs R-4.5 | Approval only. Amend ADR-V2-07. |
| C-5 | `## SysML v2` replaced on each rerun | ADR-V2-07 vs R-4.5, R-9.3 | Approval only. Amend ADR-V2-07. |
| C-6 | Superseded revisions not imported; mismatch reported as conflict | ADR-V2-08 vs R-6.6, R-6.7 | Parent flagged, child body lists older-revision usage. Close ADR-V2-08 open question. |
| C-7 | Template keeps all properties | `AI_INSTRUCTIONS.md` vs R-2.3 | Owner to confirm R-2.2 and R-2.3 scope. |
| C-8 | Translator Definition §10 cited but not present | 1.23 §14 | Create the Translator Definition or remove the citation. |
| C-9 | Local Model v2 identity tokens | ADR-V2-06 Q1 vs R-8.5 | Open. Needs parser verification. |
| C-10 | Ruleset 1.23 is behind the Decision Log. W-384 and later (W-320 to W-398) changed classes, Local Model schema (now 0.5), and element-types (now 1.18) after 1.23 was issued | 1.23 §3–§7, §15.7 vs W-384, W-398, `local-model.yaml`, `element-types.yaml`, `relationships.yaml` | Re-derive R-3.3 to R-3.5 and section 8 from the current schemas, not from 1.23. |
| C-11 | "The tool is never run over an existing vault" and "a released vault is never re-imported" | W-36, W-37 vs R-4.2 and Phase 2 BOM import into an existing vault | Owner's October 2026 direction (importer builds a vault or adds onto one) and ADR-V2-07 supersede W-36 and W-37. Record this as a new W-decision that names W-36, W-37, and W-62. |
| C-12 | Total path length: 212 characters, then 400 hard stop, then no limit, then 400 report-only | W-318/W-319, W-324, W-382, ADR-V2-06 Q5 | W-382 is the latest accepted decision (no limit). ADR-V2-06 Q5 proposes a 400-character report. Owner to confirm which applies. |
| C-13 | Identity conflicts are hard errors and never auto-repaired | W-317 vs R-4.7 (conflict listed with `flagConflict`) | Keep W-317 for identity (same `uid`, different type is an error and nothing is written). Use `flagConflict` for content conflicts. Owner to confirm. |
| C-14 | Dataview in the runtime stack | Project notes and `AI_INSTRUCTIONS.md` vs W-370 (Dataview removed 2026-10-04) | W-370 governs. Check `AI_INSTRUCTIONS.md` and templates for Dataview dependencies. |

## 15. Sources and inventory status

Read in full: Ruleset 1.23 §1–§16, `AI_INSTRUCTIONS.md`, ADR-V2-06/07/08, and the MDSE definition.

Scanned, not read in full: the Workspace Decision Log (`55_Workspace/Workspace Decision Log.md`, about 405 entries, W-01 to W-398, plus an Open section). I read the entry titles, the full text of W-30, W-36, W-37, W-38, W-62, W-317, and W-384, and keyword hits for rerun, overwrite, merge, empty fields, and supersession. The log has about 24 mentions of "supersede" and 4 of "reverse". Entries I have not read may carry further rules or conflicts. The log's decisions about empty fields (W-40, W-49, W-63, W-74) support R-2.3. W-30 (two-stage import, stage 1 faithful and mechanical) supports R-4.1. W-339 says the Workbench is an editor, which fits Phase 3.

Schema versions seen: `element-types.yaml` 1.18, `relationships.yaml` 1.36, `local-model.yaml` 0.5. Their contents were read only for headers and the class list.

Not yet inventoried:
- Remaining Workspace Decision Log entries, and its Open and Local Model sections in full
- `Structural Mapping Contract.md`, `SysML Source Ownership and Note Storage.md`, `Mapping and Conformance.md`
- `MDSE_V2_0_SHARED_NOTE_AND_RELEASE_CONTRACT`, `V2 Delivery Plan.md`
- `Translator Definition` (referenced, not present)
