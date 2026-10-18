# Step 89 — Complete four-ref Git tree classification

> Audit captured 2026-10-14. Source: GitHub Git tree recursive API; no blob contents read. All four responses returned `truncated: false`.

| Ref | Commit/tree input | Tracked non-directory paths |
|---|---|---:|
| main | `main` | 891 |
| step22 | `58ab10870f11757cf1bf367ecd5868be9b60933d` | 61,329 |
| pr42 | `4eaddbd1364633ba21038dc85a51a76c374d354d` | 894 |
| pr43 | `55c26304a1e7bb7b9d73c373a7c12a186ef59dc8` | 61,377 |

## Complete union classification

**61,399 distinct paths**; 50 divergent, 821 identical across four, 60,483 same content where shared, 45 single-reference paths. Counts sum to 61,399.

Divergent means multiple Git mode/type/SHA entries for the same path. Different SHA does not necessarily imply a Git merge conflict. Many differences are intentional schema migrations.

## All divergent paths (50)

### .github (2)

- `.github/workflows/p03-legacy-compat-tests.yml`
- `.github/workflows/p04-workbench-readonly.yml`

### .obsidian (3)

- `.obsidian/community-plugins.json`
- `.obsidian/core-plugins.json`
- `.obsidian/plugin-lock.yaml`

### 00_Workspace (8)

- `00_Workspace/00 - Current State.md`
- `00_Workspace/Handoff Prompt - MDSE v0.8 Implementation.md`
- `00_Workspace/MDSE Plan - Path to a Golden Model.md`
- `00_Workspace/MDSE Tool Definitions and Boundaries.md`
- `00_Workspace/Post-Import Tasks.md`
- `00_Workspace/README.md`
- `00_Workspace/Workbench Performance and Stability Roadmap.md`
- `00_Workspace/Workspace Decision Log.md`

### 99_System (25)

- `99_System/03_Schemas/ea-connector-mapping.yaml`
- `99_System/03_Schemas/ea-element-mapping.yaml`
- `99_System/03_Schemas/element-types.yaml`
- `99_System/03_Schemas/local-model.yaml`
- `99_System/03_Schemas/relationships.yaml`
- `99_System/06_Fileclasses/Actor.md`
- `99_System/06_Fileclasses/Artifact.md`
- `99_System/06_Fileclasses/Diagram.md`
- `99_System/06_Fileclasses/Document.md`
- `99_System/06_Fileclasses/Failure Mode.md`
- `99_System/06_Fileclasses/Functional Flow.md`
- `99_System/06_Fileclasses/Info.md`
- `99_System/06_Fileclasses/Issue.md`
- `99_System/06_Fileclasses/Item Flow.md`
- `99_System/06_Fileclasses/MDSE Link Targets.base`
- `99_System/06_Fileclasses/Object.md`
- `99_System/06_Fileclasses/Plan.md`
- `99_System/06_Fileclasses/Procedure.md`
- `99_System/06_Fileclasses/Requirement.md`
- `99_System/06_Fileclasses/Result.md`
- `99_System/06_Fileclasses/Setup.md`
- `99_System/06_Fileclasses/Use Case.md`
- `99_System/06_Fileclasses/Verification.md`
- `99_System/06_Fileclasses/modelCheck.md`
- `99_System/10_Docs/MDSE Modeling Ruleset 1.23.md`

### Base Vault (9)

- `Base Vault/Definition/Enabled Plugin Stack.md`
- `Base Vault/Definition/MDSE Workbench User Guide.md`
- `Base Vault/Definition/mdse-release.yaml`
- `Base Vault/Runtime/Plugins/breadcrumbs/data.json`
- `Base Vault/Runtime/Plugins/mdse-workbench/main.js`
- `Base Vault/Runtime/Plugins/mdse-workbench/manifest.json`
- `Base Vault/Testing/check-release.py`
- `Base Vault/Tools/v0.8.0-r2/build-plugin-config.py`
- `Base Vault/Tools/v0.8.0-r2/update-plugin-lock.py`

### Importer (2)

- `Importer/Definition/Translator Definition.md`
- `Importer/README.md`

### README.md (1)

- `README.md`


## High-impact dispositions

- `.github/workflows/p03-legacy-compat-tests.yml` and `p04-workbench-readonly.yml`: differing PR42/PR43 additions; manually curate one workflow each.
- `99_System` (25) and `Base Vault` (9): governed data/schema/release/compiled artifacts; review semantic compatibility, no blind overwrite.
- `.obsidian` (3): check plugin-lock and human configuration provenance.
- `00_Workspace` (8), `Importer` (2), `README.md` (1): reconcile source-of-truth and documentation revisions.

## Verification limitation and gates

- This is **complete Git-tree path/object inventory**, not a merge attempt or semantic review.
- PR43 HEAD changed after observation; rerun inventory before release or branch deletion.
- Existing real-QEAX import, Windows/macOS GUI acceptance, history/archive approval and release signoff remain open.
- No merges, tags, PR retargets or branch deletions performed.

## Next Step 90

Review all 50 path divergences against individual Git SHA identities and assign each one an ownership and resolution class; use this full list, not truncated comparisons.
