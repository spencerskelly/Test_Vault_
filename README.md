# Test_Vault_

Development workspace for the MDSE toolchain and the initial golden-model effort. This repository is intentionally **not** the engineering vault delivered to end users; it defines, builds and tests the tools and release that create that vault.

## Start here

1. `00_Workspace/00 - Current State.md` — current authority/status registry.
2. `00_Workspace/MDSE Plan - Path to a Golden Model.md` — gates and path to the first accepted model.
3. `00_Workspace/MDSE Tool Definitions and Boundaries.md` — ownership and contracts between tools.
4. `00_Workspace/Workspace Decision Log.md` — cross-tool/model decisions.
5. `99_System/10_Docs/MDSE Modeling Ruleset 1.23.md` — shared model semantics.
6. The owning tool folder/repository for implementation detail.

## Tool-development areas

- **Workbench** — standalone repository `spencerskelly/MDSE_Workbench`; long-lived implementation + product-definition space.
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
