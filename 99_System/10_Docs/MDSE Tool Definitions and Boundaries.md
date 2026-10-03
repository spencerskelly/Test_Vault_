# MDSE Tool Definitions and Boundaries

**Status: current through W-328, 2026-10-03.** This page is the comparison map for the MDSE toolchain. It does not replace each tool's detailed definition; it says where authority lives, what each tool owns, and what it must not own.

## Authority rule

For now, every MDSE tool except the standalone Workbench implementation is managed in **spencerskelly/Test_Vault_**.

- **Workbench implementation:** `spencerskelly/MDSE_Workbench` is authoritative for Workbench source, tests and built release artifacts. Product/interface decisions are registered in `MDSE Workbench/` in Test_Vault_ so they can be compared with the rest of the toolchain.
- **All other tools:** authoritative definition, source and release configuration remain in Test_Vault_ unless a later W-decision deliberately moves one out.
- **Model semantics:** schemas, Ruleset and W-decisions in Test_Vault_ govern every tool. A tool may not silently broaden or redefine model semantics.
- **Historical/archived material:** evidence only. It never overrides a current source.

## Tool comparison

| Tool / capability | Primary purpose | Authority / source | Owns | Does not own |
|---|---|---|---|---|
| **MDSE Workbench** | Everyday engineering interface: Create, Explore, Details, Inherited, Review and safe model edits | Implementation: `spencerskelly/MDSE_Workbench`; product/decision registry: `MDSE Workbench/` | UI behavior, disposable index, ModelRef-based navigation, schema-valid edit transactions, generated views, Review disposition | MDSE semantics, importer mapping, release packaging, Git commits |
| **MDSE Bootstrap** | Make a released vault ready for a person and verify the controlled runtime | `MDSE Bootstrap/` and `MDSE Bootstrap/plugin/` | startup/release verification, author registration, per-person initialization; exact repair/enable scope is a current design decision | model semantics, engineering edits, Workbench behavior, importer behavior |
| **EA → MDSE Importer** | Deterministically translate the governed EA source into a fresh MDSE base and produce reconciliation evidence | `99_System/09_Tools/EA_to_MDSE_Native_Importer/`, [[Translator Definition]], mapping schemas and reconciliation docs | source translation, deterministic naming/identity allocation, Local Model writing, import evidence | everyday model editing, Review disposition, runtime plugin management |
| **Base / release builder** | Produce the fully configured engineering vault delivered to users | `mdse-release.yaml`, `build-base.py`, `build-plugin-config.py`, `update-plugin-lock.py`, `check-release.py` | runtime payload, governed plugin configuration, pins/hashes, release consistency | engineering model semantics beyond copying governed schemas/config |
| **Runtime community plugins** | Supporting Obsidian capabilities | vendored payload + `.obsidian/plugin-lock.yaml`; settings generated in Test_Vault_ | their specific UI/runtime capability | MDSE semantic authority or correctness |
| **Cross-vault infrastructure** | Future resolution/navigation across separately governed vaults | deferred; archived resolver under `99_System/archive/01_Admin Archived Plugins/` is reference only | future cross-vault identity/resolution/navigation | current v0.8 behavior |

## Shared contracts

All tools that touch model content must agree on these contracts:

1. `relationships.yaml` — endpoint validity and relationship vocabulary.
2. `element-types.yaml` — model classes, properties and ordering.
3. `local-model.yaml` — Local Model record grammar and validation.
4. Ruleset + Workspace Decision Log — semantic meaning and precedence.
5. `ModelRef` concept — Workbench-facing address of either a note or local record; future shared-core/headless tooling should use the same identity boundary.
6. Native Obsidian links/block IDs — persisted navigation; tools must preserve block fragments.
7. Release manifest / plugin lock — exact runtime pairing.

## Current semantic alignment checkpoint

- Requirement scope uses `appliesTo`, including Requirement → State / State Machine.
- Only Function and Design use `satisfies`.
- State and State Machine never satisfy a Requirement (W-327).
- Local occurrences are local records, not fake notes.
- Reusable definitions remain first-class notes.
- Workbench reads schemas rather than inventing private model rules.
- Cross-vault resolution is intentionally deferred, but the ModelRef boundary must not block it later.

## Comparison protocol

When changing one tool:

1. Start here to identify neighboring tools/contracts.
2. Read that tool's authoritative detailed definition.
3. Compare the proposed change against the shared contracts above.
4. If the change alters semantics, log a W-decision first; if it changes only Workbench UX/implementation, use the WB decision path.
5. Update this map only when ownership/boundaries change, not for ordinary implementation details.
