# Test_Vault_

Development workspace for the MDSE toolchain and the initial golden-model effort. This repository is intentionally **not** the engineering vault delivered to end users; it defines, builds and tests the tools and release that create that vault.

## Version navigation

- **Version 1 (10–19):** legacy/release-compatible implementation, including `10_Base Vault/` and `11_Importer/`. Maintain independently.
- **Version 2 (20–29):** new standard SysML v2 development. Start at [`20_SysMLv2_Translator_Workbench/README_SysMLv2_Translator_Workbench.md`](20_SysMLv2_Translator_Workbench/README_SysMLv2_Translator_Workbench.md), then its [`Definition/`](20_SysMLv2_Translator_Workbench/Definition/README.md), [`Tools/`](20_SysMLv2_Translator_Workbench/Tools/README.md), and [`Testing/`](20_SysMLv2_Translator_Workbench/Testing/README.md) indexes.
- **Shared (outside 10–29):** source evidence definitions, governance, compatible helpers and reference material. Keep v1/v2 transformations and release pins independently versioned. A shared change must be tested against both, and proposed v1 adoption requires approval.

**Navigation note:** Some older links in this README still use paths predating the October 15 folder move. Follow the versioned entrypoints above while cross-reference migration is audited; do not assume a file has disappeared.

## Start here

1. `00_Workspace/00 - Current State.md` — current authority/status registry.
2. `00_Workspace/MDSE Plan - Path to a Golden Model.md` — gates and path to the first accepted model.
3. `00_Workspace/MDSE Tool Definitions and Boundaries.md` — ownership and contracts between tools.
4. `00_Workspace/Workspace Decision Log.md` — cross-tool/model decisions.
5. `99_System/10_Docs/MDSE Modeling Ruleset 1.23.md` — shared model semantics.
6. The owning tool folder/repository for implementation detail.

## Tool-development areas

- **Workbench** — `55_Workbench/` (source, tests, implementation contracts and product-definition documentation) within this repository. The former standalone Workbench Git history is retained for historical traceability, and archival requires separate approval.
- **Importer/** — importer definition, versioned tools, testing evidence and history.
- **Bootstrap/** — Bootstrap definition, versioned source and first-open testing.
- **Base Vault/** — release definition, build tools, runtime payload, release tests and initialization.
- **Cross-Vault/** — deferred future cross-vault capability and retained prior implementation evidence.
- **00_Workspace/** — cross-tool current state, roadmap, release reconciliation, decisions and handoffs.
- **99_System/** — shared MDSE semantic/runtime core. Do not use it as a generic dumping ground for tool implementations.
- **Definitions/** — shared MDSE definition notes used by the model/runtime.

## Development convention

`main` is the normal working truth. Tool revisions live in explicit version folders (for example `Importer/Tools/v0.8.6`, `Bootstrap/Tools/v0.3.1`). Use branches only when isolation is genuinely useful; do not use long-lived branches as the normal way to present options or retain versions.

Machine-readable release authority: `Base Vault/Definition/mdse-release.yaml`.
