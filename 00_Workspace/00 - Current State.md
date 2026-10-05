# Current State

**Last verified: 2026-10-05. Read this first, human or AI.** It says what is current, what is historical, where each rule lives and what is not built yet. If any other file disagrees with this page, this page and the files it names as current win. The machine-readable release authority is `Base Vault/Definition/mdse-release.yaml`.

## Target and status

| Item | Value |
|---|---|
| MDSE release target | **0.8.0** (pre-release: controlled base packaging and importer candidate built; acceptance gates remain) |
| Relationships schema | 1.35 (`99_System/03_Schemas/relationships.yaml`) |
| Element-types schema | 1.17 (`99_System/03_Schemas/element-types.yaml`) |
| Local Model | 0.2 writer; readers accept 0.1 and 0.2 (`99_System/03_Schemas/local-model.yaml`) |
| Source model lineage | EA8647 |
| Generated path rule | hard stop 400 characters, nothing shortened for length (W-324); duplicate marker `~2`; alteration marker `~a` |

## Read in this order

1. This page.
2. [[MDSE Plan - Path to a Golden Model]]: the authoritative plan from here to a golden model (gates, run procedure, post-import order, improvements per component, decisions needed).
3. [[MDSE Impact-Focused Remaining Work - 2026-10-05]]: execution filter that breaks the remaining high-impact work into small steps and explicitly defers low-value expansion. It is planning/reference guidance and does not replace W/WB authority.
4. [[MDSE v0.8 Cross-Repository Reconciliation - 2026-10-02]]: the implementation contract (identity, reruns, naming, Local Model 0.2, evidence set, gates, build order).
5. [[MDSE Modeling Ruleset 1.23]]: what the model means and how imports are governed.
6. [[Translator Definition]] and [[Importer Operating Contract]]: what the stage 1 importer must do and how a run progresses; [[Importer Issue Register]] is the active systemic correction backlog.
7. [[Workspace Decision Log]]: every decision (W-01 to W-370); newest last. Where a log entry marks an earlier one superseded, the later one governs.
8. [[MDSE Tool Definitions and Boundaries]]: authoritative ownership/boundary map for Workbench, Bootstrap, importer, base/release tooling and deferred cross-vault infrastructure.
9. [[Handoff Prompt - MDSE v0.8 Implementation]]: copy-ready prompts for a new AI chat (general, and Workbench).
10. [[Post-Import Tasks]]: the work done in the vault after an import, Tasks 1 to 9.
11. For AI tools creating or editing notes: `99_System/02_AI/AI_INSTRUCTIONS.md`.

## Where each rule lives

| Question | Authority |
|---|---|
| What a relationship may connect | `relationships.yaml` 1.35 |
| Note properties and their order | `element-types.yaml` 1.17, `Definitions/Properties` |
| Local part, endpoint, connection and flow records in a note body | `local-model.yaml` 0.2, Ruleset 1.23 section 15.7 |
| How EA elements, connectors, tags and fields map | `ea-element-mapping.yaml`, `ea-connector-mapping.yaml`, `ea-tag-dispositions.yaml`, `ea-field-dispositions.yaml`, `ea-package-rules.yaml` |
| Identity (`uid`, local tokens), reruns, source ownership | Reconciliation, "Settled identity rules" and "Source ownership and reruns"; Ruleset 1.23 section 16 |
| File and folder naming, path limit | Reconciliation, "Naming and path rules"; Ruleset 1.23 sections 15 and 16 |
| Importer pipeline, trust boundaries and run states | [[Importer Operating Contract]]; detailed semantic behavior remains in [[Translator Definition]] and the schemas |
| Active importer systemic corrections | [[Importer Issue Register]] |
| Run completion and evidence | Translator Definition, checks 1 to 9; Reconciliation, "Evidence package" |
| Tool ownership and boundaries | [[MDSE Tool Definitions and Boundaries]] |
| Workbench product direction | `spencerskelly/MDSE_Workbench/docs/Definition/` (`WB-` decisions and implementation contract) |
| Workbench implementation/code | repo `spencerskelly/MDSE_Workbench`; `WB106_IMPLEMENTATION_CONTRACT.md` is the current implementation boundary |
| Runtime plugins, versions, settings | `.obsidian/plugin-lock.yaml` (generated), `Base Vault/Definition/Enabled Plugin Stack.md`, generators in `Base Vault/Tools/v0.8.0-r2/` |
| Workbench user guide | `Base Vault/Definition/MDSE Workbench User Guide.md` (release-managed copy of the standalone Workbench guide; mapped into generated vaults by W-341) |
| Bootstrap behavior and source | `Bootstrap/Definition/`, `Bootstrap/Tools/`, and `Bootstrap/Testing/` |

## Tools

| Tool | Status | Next step |
|---|---|---|
| Importer v0.8.12 | **active hardening candidate.** W-371 transaction state, W-372 separated run states, W-373 WAL blocking, W-374 initialized-vault gate, W-375 source SHA-256 and W-376 review-only relationship boundary are implemented with static/syntax/vector checks. Last whole-model real-QEAX semantic write remains v0.8.3. | Next semantic decision is IMP-009: whether every Local Model endpoint requires a reusable first-class Port definition. After that decision, continue the ranked register and then run targeted browser tests + a fresh real-QEAX import. Do not mark release-conformant until acceptance gates and WB-106 pass. |
| Importers v0.1 to v0.7, v0.8.0 to v0.8.6 | archived/reference once v0.8.7 is accepted as the active candidate (W-326 lineage) | `Importer/History/Importer Revisions/` with retained revision history. None may generate a model. |
| Clean 0.8.0 base vault | **candidate build path validated; not issued** | A 0.3.1-candidate base built successfully and `check-release.py --base` completed with **0 fail / 4 expected pre-release warnings** on 2026-10-03. Initializer defects were fixed in source and syntax-gated (W-336). Do not create the next integration vault until Workbench/Importer alignment is ready (W-337). |
| MDSE Workbench | **0.1.16 remains the pre-release Base pin.** The Step-60 standalone stability baseline remains frozen at `476fbcad08ecd03f8c2c49cd3126393beb6ab412`, but active 0.1.17 development has moved beyond that baseline through **WB-126**; the latest built artifact on 2026-10-05 is commit `e88d1b40a29d79b988cfb1b40e73717e8c6492a8`. The numbered Workbench stability roadmap remains closed. WB-125/WB-126 added fresh-source identity protection to relationship mutation paths; **WB-127 closes the remaining ordinary property/body writer symmetry and is the current Workbench pause boundary.** Workbench structured-editor expansion is intentionally paused while known importer corrections from the last imported model are worked. | Finish the bounded identity-safety boundary, then complete the minimum structured editor and rerun only the acceptance scope affected by post-freeze changes. Do not expand standalone hardening indefinitely; the next major value gate is one real importer/Base/Bootstrap/Workbench integration run. |
| MDSE Bootstrap 0.3.0 | pinned Base runtime; **0.3.1 staged-start candidate is built, reproducibility-tested and installed only in `261002083`.** W-347 defers normal full release hashing until Obsidian metadata settles while preserving exact pre-enable verification for disabled locked plugins and immediate author registration. CI now publishes/commits a checksummed candidate artifact; integration lock uses the exact 0.3.1 artifact hashes. | Validate first-open/startup behavior in the same `261002083` smoke gate. Do not promote 0.3.1 to the controlled Base until that user-side startup gate passes. |
| Runtime plugins (10) | vendored, pinned, hashed, configured (W-322) | `Base Vault/Runtime/Plugins/`; lock `.obsidian/plugin-lock.yaml`; see `Base Vault/Definition/Enabled Plugin Stack.md` |

Workbench 0.1.16 is still pinned and enabled in pre-release bases. The Step-60 0.1.17 stability baseline remains the accepted standalone reference, while post-freeze 0.1.17 development has continued through WB-126. W-339 intentionally expands WB-106 to include structured editing, so `wb106Version` remains unset until that editor gate is complete and the changed candidate passes its affected acceptance scope. The **final issued** base must pin the WB-106-capable release (`wb106Version` in `mdse-release.yaml`); `check-release.py` fails a release build until then.

## Runtime-base alignment

W-321 removes the old manually curated base-content list. `mdse-release.yaml` now contains the one positive include list used by `build-base.py`. The generated engineering vault intentionally omits this Current State registry, the release manifest, Translator Definition, Decision Log, EA evidence, archives and Workbench design notes. Runtime consumers instead share the actual schemas: relationships 1.35, element-types 1.17 and Local Model 0.2. Initialization preserves the base's `mdse_release`.

**Controlled plugin release (W-322).** The base opens fully functional once Restricted mode is turned off: all 10 runtime plugins ship inside it, pinned and hashed in `.obsidian/plugin-lock.yaml` (schema 2), with governed settings for Templater, Fileclass, Breadcrumbs and Obsidian Git generated from the schemas. Obsidian 1.13.0 or later is required. MDSE Bootstrap checks every start against the lock and registers each person's author code. To change a plugin version, follow `Bootstrap/Definition/README.md`.

## File status registry

**Current:** the files in "Read in this order", [[MDSE Tool Definitions and Boundaries]], `Importer/Definition/`, `Bootstrap/Definition/`, `Base Vault/Definition/`, `Definitions/`, `99_System/03_Schemas/`, `99_System/05_Templates/`, `Bootstrap/`, `Base Vault/`, and the standalone `spencerskelly/MDSE_Workbench` repository for Workbench product/implementation authority.

**Generated (never edit by hand; change the schemas or payload and regenerate):** `99_System/06_Fileclasses/`, `.obsidian/plugin-lock.yaml`, `.obsidian/community-plugins.json`, governed runtime plugin `data.json` files under `Base Vault/Runtime/Plugins/`.

**Reference (valid support, not rule authority):** [[MDSE Impact-Focused Remaining Work - 2026-10-05]]; [[Review Changes Log]]; `99_System/CSV_EA/` (EA evidence used to define the rules); `99_System/11_Import/` snapshots named by [[Post-Import Tasks]].

**Archived (`99_System/archive/`, no authority, see its README):** old translator workspace `10_EA Native Translator/`; four retired empty CSVs `11_Import retired/`; `08_Scripts retired/`; retired importers v0.1 to v0.7 and v0.8.0 to v0.8.5 `09_Tools retired importers/`; `01_Admin Archived Plugins/`; `03_Schemas retired/vault-registry.yaml`; and these documents in `10_Docs retired/` (W-326):

| File | Governed now by |
|---|---|
| [[Handoff - Continue Here]] | this page, [[MDSE Plan - Path to a Golden Model]], [[Handoff Prompt - MDSE v0.8 Implementation]] |
| [[EA Native Importer Comprehensive Handoff - 2026-10-01]] | [[MDSE v0.8 Cross-Repository Reconciliation - 2026-10-02]] |
| [[MDSE v0.8 Design Check - 2026-10-01]] | [[MDSE v0.8 Cross-Repository Reconciliation - 2026-10-02]] |
| [[MDSE Modeling Ruleset 1.22]] | [[MDSE Modeling Ruleset 1.23]] |
| [[Git and New Vault Setup]] | `Initialize-Vault.sh/.ps1`; the issued 0.8.0 base |
| [[MDSE v0.8 Toolchain Review - 2026-10-02]] | [[MDSE Plan - Path to a Golden Model]] |
| [[MDSE Platform Roadmap and Critical Points - 2026-10-02]] | [[MDSE Plan - Path to a Golden Model]] |

Links to archived files keep working: Obsidian resolves them by file name.

**Outside this workspace:** repos `20260930`, `261001` and `Test_Vault_-base-vault-2026-09-30-rel133-v051` are reference only and carry warnings; do not patch them into a 0.8.0 model.

## Keeping this true (change protocol)

1. A decision is appended to the Workspace Decision Log as `W-n`.
2. In the same commit: update the owning authority document/schema. Only advance the Translator Definition's `Current through W-n` marker when the decision actually changes importer/stage-1 behavior (W-335).
3. If a file is replaced, put a callout banner at its top (`> [!WARNING] SUPERSEDED by [[...]]`, or `> [!NOTE] HISTORICAL ...`) and list it in `mdse-release.yaml` with `supersededBy`. Move it to `99_System/archive/` only when nothing current links to it.
4. If a schema version, tool status or document status changes, update `mdse-release.yaml` and the tables on this page.
5. Run `python3 "Base Vault/Testing/check-release.py"` (add `--workbench <clone path>` and/or `--base <generated-base path>` when those artifacts are involved). It must pass before commit.
6. Never edit a historical or superseded file's content to match new rules. Add the pointer; leave the evidence.
7. After a run or a decision that changes a step, update the run log and the item tables in [[MDSE Plan - Path to a Golden Model]].
