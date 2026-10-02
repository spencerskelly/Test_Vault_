# Current State

**Last verified: 2026-10-02. Read this first, human or AI.** It says what is current, what is historical, where each rule lives and what is not built yet. If any other file disagrees with this page, this page and the files it names as current win. The machine-readable twin is `99_System/03_Schemas/mdse-release.yaml`.

## Target and status

| Item | Value |
|---|---|
| MDSE release target | **0.8.0** (pre-release: base vault and importer not built yet) |
| Relationships schema | 1.35 (`99_System/03_Schemas/relationships.yaml`) |
| Element-types schema | 1.17 (`99_System/03_Schemas/element-types.yaml`) |
| Local Model | 0.2 writer; readers accept 0.1 and 0.2 (`99_System/03_Schemas/local-model.yaml`) |
| Source model lineage | EA8647 |
| Generated path limit | 212 characters; duplicate marker `~2`; alteration marker `~a` |

## Read in this order

1. This page.
2. [[MDSE v0.8 Cross-Repository Reconciliation - 2026-10-02]]: the implementation contract (identity, reruns, naming, Local Model 0.2, evidence set, gates, build order).
3. [[MDSE Modeling Ruleset 1.23]]: what the model means and how imports are governed.
4. [[Translator Definition]]: what the stage 1 importer must do.
5. [[Workspace Decision Log]]: every decision (W-01 to W-320); newest last. Where a log entry marks an earlier one superseded, the later one governs.
6. [[Handoff Prompt - MDSE v0.8 Implementation]]: copy-ready prompt for a new AI chat.
7. For AI tools creating or editing notes: `99_System/02_AI/AI_INSTRUCTIONS.md`.

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
| Workbench product direction | `MDSE Workbench/` folder (`WB-` decisions) |
| Workbench code, next build | repo `spencerskelly/MDSE_Workbench`, `WB106_IMPLEMENTATION_CONTRACT.md` |

## Tools

| Tool | Status | Next step |
|---|---|---|
| Importer v0.8.0 | **not built** | Build from the v0.5.2 lineage plus useful v0.7 code, per the Reconciliation build order. No release-conformant importer exists. |
| Importer v0.5.2 | accepted fallback and safety lineage | Starting point for v0.8.0 |
| Importer v0.7 | evidence only, never accepted | Do not use to generate a model to keep |
| Importers v0.1 to v0.5.1 | history | See `99_System/09_Tools/README_09_Tools.md` |
| Clean 0.8.0 base vault | **not built** | Generate from this workspace; must declare `mdse_release: "0.8.0"`. The old base repository is obsolete. |
| MDSE Workbench 0.1.15 | built; typecheck, 31 tests and build pass (2026-10-02) | WB-106: Local Model reader, ModelRef, block fragments, occurrence-aware views |
| MDSE Bootstrap 0.2.0 | pinned in `plugin-lock.yaml`; **no source or release found** | Locate or publish the source, or defer it from the base plugin set |

Workbench is not yet pinned in `plugin-lock.yaml`; the base must pin a WB-106-capable release.

## File status registry

**Current:** the files in "Read in this order", `Definitions/`, `99_System/03_Schemas/`, `99_System/05_Templates/`.

**Reference (valid support, not rule authority):** [[MDSE v0.8 Toolchain Review - 2026-10-02]] (code-gap audit), [[Post-Import Tasks]], [[Review Changes Log]].

**Proposal (not decided):** [[MDSE Platform Roadmap and Critical Points - 2026-10-02]].

**Historical or superseded (each carries a banner pointing to what governs now):**

| File | Governed now by |
|---|---|
| [[Handoff - Continue Here]] (top section current, body historical) | this page, [[Handoff Prompt - MDSE v0.8 Implementation]] |
| [[EA Native Importer Comprehensive Handoff - 2026-10-01]] | [[MDSE v0.8 Cross-Repository Reconciliation - 2026-10-02]] |
| [[MDSE v0.8 Design Check - 2026-10-01]] | [[MDSE v0.8 Cross-Repository Reconciliation - 2026-10-02]] |
| [[MDSE Modeling Ruleset 1.22]] | [[MDSE Modeling Ruleset 1.23]] |
| [[Git and New Vault Setup]] | `Initialize-Vault.sh/.ps1`; clean 0.8.0 base once built |

**Archived (`99_System/archive/`, no authority, see its README):** old translator workspace `10_EA Native Translator/`; four retired empty CSVs in `11_Import retired/`.

**Outside this workspace:** repos `20260930`, `261001` and `Test_Vault_-base-vault-2026-09-30-rel133-v051` are reference only and carry warnings; do not patch them into a 0.8.0 model.

## Keeping this true (change protocol)

1. A decision is appended to the Workspace Decision Log as `W-n`.
2. In the same commit: update the authority document and schema it changes, and set "Current through W-n" in the Translator Definition.
3. If a file is replaced, put a callout banner at its top (`> [!WARNING] SUPERSEDED by [[...]]`, or `> [!NOTE] HISTORICAL ...`) and list it in `mdse-release.yaml` with `supersededBy`. Move it to `99_System/archive/` only when nothing current links to it.
4. If a schema version, tool status or document status changes, update `mdse-release.yaml` and the tables on this page.
5. Run `python3 99_System/09_Tools/check-release.py` (add `--workbench <clone path>` when Workbench is involved). It must pass before commit.
6. Never edit a historical or superseded file's content to match new rules. Add the pointer; leave the evidence.
