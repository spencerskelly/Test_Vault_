# Test_Vault_

MDSE toolchain development repository. This is **not** a generated engineering model vault.

## V2 program start here

**[Open the MDSE v2 Master Map of Contents](MOC_MDSE_V2.md)** — authoritative navigation across project decisions, native definitions, importer, Workbench, validation, historical references, and known gaps.


- [V2 program home — decisions, definition map, implementations and tests](26_Definitions/V2_PROGRAM_HOME.md)
- [V2 goals, work breakdown and progress](26_Definitions/V2_PROGRAM_GOALS_AND_COMPLETION_2026-10-18.md)
- [V2 connector definitions](26_Definitions/V2_CONNECTOR_DEFINITIONS_INDEX.md)

## Versioned workspaces

| Area | V1 | V2 |
|---|---|---|
| Base Vault | [10_Base Vault](10_Base%20Vault/README.md) | [20_Base Vault](20_Base%20Vault/README.md) |
| Importer | [11_Importer](11_Importer/README.md) | [21_Importer](21_Importer/README.md) |
| Bootstrap | [13_Bootstrap](13_Bootstrap/Definition/README.md) | [23_Bootstrap](23_Bootstrap/README.md) |
| Workbench | [14_Workbench](14_Workbench/README.md) | [24_Workbench](24_Workbench/README.md) |
| Testing | [15_Testing](15_Testing/) | [25_Testing](25_Testing/README.md) |
| Definitions | [16_Definitions](16_Definitions/) | [26_Definitions](26_Definitions/README.md) |

[V2 SysML translator research and historical plan](29_SysMLv2_Translator_Workbench/README_SysMLv2_Translator_Workbench.md).

## Shared and cross-version

- [55_Workspace](55_Workspace/README.md) — workspace governance, decision history, current-state registry (some internal references still require path migration).
- [Reference](Reference/) — cross-version reference and architecture discussions.
- [99_System](99_System/) — inherited system schemas, runtime configuration and v1 baseline; **not automatically v2 authority**.
- [V2 architecture decisions](26_Definitions/Architecture%20Decisions.md), [v2 delivery plan](26_Definitions/V2%20Delivery%20Plan.md), [v2 BOM rules](26_Definitions/BOM%20Integration.md).

## Safety and development policy

- V1 and V2 release manifests, mappings, tools and dependencies must remain separately versioned.
- SysML v2 textual declarations govern formal structure and relationships in v2; v1 retains its established model semantics until specifically approved to change.
- Shared source extraction/provenance code should be version-neutral; any shared change requires independent v1 and v2 testing.
- Never place real imported engineering models or production BOM datasets in this tools repository.
- Use `main` as reviewed working truth, with short-lived branches when code changes need isolation.

## Move verification status

**2026-10-15:** Folder moves have left legacy references inside executable scripts and the v1 release manifest. The new directory tree is navigable, **but executable compatibility is not yet certified**. See [move impact audit](25_Testing/Folder%20Move%20Audit%202026-10-15.md) before running v1 release/build tasks. Do not treat a source file being present as evidence that the build still succeeds.
