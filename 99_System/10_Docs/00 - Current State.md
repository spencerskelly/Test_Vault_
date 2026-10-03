# Current State

**Last verified: 2026-10-03. Read this first, human or AI.** It says what is current, what is historical, where each rule lives and what is not built yet. If any other file disagrees with this page, this page and the files it names as current win. The machine-readable twin is `99_System/03_Schemas/mdse-release.yaml`.

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
2. [[MDSE Plan - Path to a Golden Model]]: the plan from here to a golden model (gates, run procedure, post-import order, improvements per component, decisions needed).
3. [[MDSE v0.8 Cross-Repository Reconciliation - 2026-10-02]]: the implementation contract (identity, reruns, naming, Local Model 0.2, evidence set, gates, build order).
4. [[MDSE Modeling Ruleset 1.23]]: what the model means and how imports are governed.
5. [[Translator Definition]]: what the stage 1 importer must do.
6. [[Workspace Decision Log]]: every decision (W-01 to W-328); newest last. Where a log entry marks an earlier one superseded, the later one governs.
7. [[MDSE Tool Definitions and Boundaries]]: authoritative ownership/boundary map for Workbench, Bootstrap, importer, base/release tooling and deferred cross-vault infrastructure.
8. [[Handoff Prompt - MDSE v0.8 Implementation]]: copy-ready prompts for a new AI chat (general, and Workbench).
9. [[Post-Import Tasks]]: the work done in the vault after an import, Tasks 1 to 9.
10. For AI tools creating or editing notes: `99_System/02_AI/AI_INSTRUCTIONS.md`.

## Where each rule lives

| Question | Authority |
|---|---|
| What a relationship may connect | `relationships.yaml` 1.35 |
| Note properties and their order | `element-types.yaml` 1.17, `Definitions/Properties` |
| Local part, endpoint, connection and flow records in a note body | `local-model.yaml` 0.2, Ruleset 1.23 section 15.7 |
| How EA elements, connectors, tags and fields map | `ea-element-mapping.yaml`, `ea-connector-mapping.yaml`, `ea-tag-dispositions.yaml`, `ea-field-dispositions.yaml`, `ea-package-rules.yaml` |
| Identity (`uid`, local tokens), reruns, source ownership | Reconciliation, "Settled identity rules" and "Source ownership and reruns"; Ruleset 1.23 section 16 |
| File and folder naming, path limit | Reconciliation, "Naming and path rules"; Ruleset 1.23 sections 15 and 16 |
| Run completion and evidence | Translator Definition, checks 1 to 9; Reconciliation, "Evidence package" |
| Tool ownership and boundaries | [[MDSE Tool Definitions and Boundaries]] |
| Workbench product direction | `MDSE Workbench/` folder (`WB-` decisions) |
| Workbench implementation/code | repo `spencerskelly/MDSE_Workbench`; `WB106_IMPLEMENTATION_CONTRACT.md` is the current implementation boundary |
| Runtime plugins, versions, settings | `.obsidian/plugin-lock.yaml` (generated), `99_System/01_Admin/Enabled Plugin Stack.md`, generators in `99_System/09_Tools/` |
| Bootstrap behavior and source | `MDSE Bootstrap/` in this repository (README, plugin source, Author Registration Spec, Base First-Open Test Sheet) |

## Tools

| Tool | Status | Next step |
|---|---|---|
| Importer v0.8.6 | **implementation candidate built; whole-model semantic write succeeded (v0.8.3 run)** | Run the decode-only attachment check on the real QEAX with `attachment_benchmark.json` (376 documents, 390 files, zero residual; W-323), then a full fresh-base run. W-324: no length-driven shortening, links by file name, `Review - Long Paths.csv` feeds Post-Import Task 9. Do not mark release-conformant until acceptance gates and WB-106 pass. |
| Importers v0.1 to v0.7, v0.8.0 to v0.8.5 | archived (W-326) | `99_System/archive/09_Tools retired importers/` with a README of their roles. None may generate a model. |
| Clean 0.8.0 base vault | **not issued** | Generate deterministically with `build-base.py`; validate with `check-release.py --base`. It is a lean runtime artifact and carries `mdse_release: "0.8.0"` in `.vault.yaml`. |
| MDSE Workbench 0.1.16 | built; typecheck, 52 tests and build pass (2026-10-03). Reads Local Model 0.1/0.2, `ModelRef`, findings report (**Check Local Model**); writes links Obsidian-style (W-324, W-325, WB-111, WB-112) | WB-106 remainder: occurrence-aware Structure, Interfaces, Where Used and Requirements views, Local Model popup (WB-105), Review integration |
| MDSE Bootstrap 0.3.0 | built (W-322); 6 tests pass; in every base | Run the [[Base First-Open Test Sheet]] in Obsidian. Source and docs: `MDSE Bootstrap/` |
| Runtime plugins (11) | vendored, pinned, hashed, configured (W-322) | `99_System/09_Tools/runtime-plugins/`; lock `.obsidian/plugin-lock.yaml`; see `99_System/01_Admin/Enabled Plugin Stack.md` |

Workbench 0.1.16 is pinned and enabled in pre-release bases (WB-106 is not complete; `wb106Version` stays unset until the occurrence-aware views are done). The **final issued** base must pin the WB-106-capable release (`wb106Version` in `mdse-release.yaml`); `check-release.py` fails a release build until then.

## Runtime-base alignment

W-321 removes the old manually curated base-content list. `mdse-release.yaml` now contains the one positive include list used by `build-base.py`. The generated engineering vault intentionally omits this Current State registry, the release manifest, Translator Definition, Decision Log, EA evidence, archives and Workbench design notes. Runtime consumers instead share the actual schemas: relationships 1.35, element-types 1.17 and Local Model 0.2. Initialization preserves the base's `mdse_release`.

**Controlled plugin release (W-322).** The base opens fully functional once Restricted mode is turned off: all 11 runtime plugins ship inside it, pinned and hashed in `.obsidian/plugin-lock.yaml` (schema 2), with governed settings for Templater, Fileclass, Breadcrumbs and Obsidian Git generated from the schemas. Obsidian 1.13.0 or later is required. MDSE Bootstrap checks every start against the lock and registers each person's author code. To change a plugin version, follow `MDSE Bootstrap/README_MDSE Bootstrap.md`.

## File status registry

**Current:** the files in "Read in this order", [[MDSE Tool Definitions and Boundaries]], `Definitions/`, `99_System/03_Schemas/`, `99_System/05_Templates/`, `MDSE Bootstrap/`, `MDSE Workbench/` (Workbench product direction).

**Generated (never edit by hand; change the schemas or payload and regenerate):** `99_System/06_Fileclasses/`, `.obsidian/plugin-lock.yaml`, `.obsidian/community-plugins.json`, `99_System/09_Tools/runtime-plugins/*/data.json`.

**Reference (valid support, not rule authority):** [[Review Changes Log]]; `99_System/CSV_EA/` (EA evidence used to define the rules); `99_System/11_Import/` snapshots named by [[Post-Import Tasks]].

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
2. In the same commit: update the authority document and schema it changes, and set "Current through W-n" in the Translator Definition.
3. If a file is replaced, put a callout banner at its top (`> [!WARNING] SUPERSEDED by [[...]]`, or `> [!NOTE] HISTORICAL ...`) and list it in `mdse-release.yaml` with `supersededBy`. Move it to `99_System/archive/` only when nothing current links to it.
4. If a schema version, tool status or document status changes, update `mdse-release.yaml` and the tables on this page.
5. Run `python3 99_System/09_Tools/check-release.py` (add `--workbench <clone path>` and/or `--base <generated-base path>` when those artifacts are involved). It must pass before commit.
6. Never edit a historical or superseded file's content to match new rules. Add the pointer; leave the evidence.
7. After a run or a decision that changes a step, update the run log and the item tables in [[MDSE Plan - Path to a Golden Model]].
