# Branch Cleanup — Step 90: Divergent Path Ownership and SHA Gate (2026-10-14)

Status: **PARTIAL — classification completed at group level, critical SHA spot-check started. NO MERGE / NO DELETE / NO RELEASE.**

## Source and ref freshness

Source: `66_Testing/consolidation/STEP89_COMPLETE_FOUR_REF_TREE_AUDIT.md` on `integration/p03-legacy-compat-tests-20261013`, a full, nontruncated four-ref tree audit. Its pinned refs contained 61,399 union paths and 50 paths with different Git object IDs across shared refs. Step89 PR43 SHA was `55c26304a1e7bb7b9d73c373a7c12a186ef59dc8`; current PR43 SHA is `ea176532dd738765c8fdbf89c34fb59f330a2b82`. Git compare shows **exactly one additional file**, the Step89 audit document itself; no modification to the 50 previously reported divergences was observed in that one-commit delta. Other refs must still be pinned before merge.

## Ownership and resolution classes (all 50 paths)

| Paths | Count | Accountable review owner (role, not approval) | Proposed resolution | Gate |
|---|---:|---|---|---|
| `.github/workflows/p03-legacy-compat-tests.yml`; `p04-workbench-readonly.yml` | 2 | CI maintainer | Manual CI merge: preserve least-privilege and read-only, explicitly resolve PR42 vs PR43 versions | Tests, workflow permission and action trigger review |
| `.obsidian/community-plugins.json`; `core-plugins.json`; `plugin-lock.yaml` | 3 | Obsidian runtime owner | Manual human-config reconciliation | Windows/macOS plugin lock and startup evidence |
| Eight Step89-listed `00_Workspace/` documents | 8 | MDSE methodology/document owner | Reconcile current state/decision history without removing historical evidence | Document authority review |
| Five `99_System/03_Schemas/` YAML mappings/type/local-model/relationships | 5 | Schema governance owner | Governed semantic migration, **not overwrite** | Schema versions, importer/writer compatibility, regression checks |
| Nineteen `99_System/06_Fileclasses/` notes/bases | 19 | Fileclass/model owner | Governed semantic migration with backward compatibility tests | Fileclass/YAML/frontmatter acceptance |
| `99_System/10_Docs/MDSE Modeling Ruleset 1.23.md` | 1 | Ruleset governance owner | Governed rule reconciliation | Change decision + release alignment |
| Nine `Base Vault/` definition/runtime/tool/test divergences | 9 | Base Vault and release owner | Governed release/machine-artifact reconciliation, **no blind copying binaries** | SHA/build provenance + release manifest checks |
| `Importer/Definition/Translator Definition.md`; `Importer/README.md` | 2 | Importer owner | Document semantic reconciliation | Importer mapping/source contract |
| root `README.md` | 1 | Repository maintainer | Documentation reconciliation | Final single-authority navigation |
| **Total** | **50** | | | |

## Exact Git blob SHA spot-check (main versus frozen Step22)

| Path | main blob | Step22 blob | Decision |
|---|---|---|---|
| `99_System/03_Schemas/local-model.yaml` | `04b8592d9faef48aa1c952747a26e1ee917e8b58` | `361dee8269f9fbdfd16bcee33a1b808015f7ba5a` | semantic review required |
| `99_System/03_Schemas/relationships.yaml` | `c440e3925d33d0c819e8a75d1b03f3c79d72e995` | `413fd5d32d12331413fda30653c7a3a38ac2d2ab` | semantic review required |
| `Base Vault/Definition/mdse-release.yaml` | `a1692487d555f20ae08c7595f7eea5902f391619` | `6d06db25ed50ff390460c567b8fa769981aacc9e` | version changes confirmed |
| `Base Vault/Runtime/Plugins/mdse-workbench/main.js` | `64635f2312349032b3b798cc1a4ad4e0d34eb133` | `f8a0b6cfa454437e68edaff7d5adf21965606a3c` | binary build/provenance gate |
| `.obsidian/plugin-lock.yaml` | `2039b5ddda42ed8d6f08b00c987f05d775671f0e` | `c430670577318457972a154012d08c6d28e6d11b` | plugin compatibility gate |

Confirmed semantic delta in release manifest: `main` declares relationship 1.35, element types 1.17 and local model 0.2 (2026-10-03), whereas frozen Step22 declares 1.36 / 1.18 / 0.5 (2026-10-05). This is **not** an interchangeable text conflict or permission to promote Step22 release.

## Remaining acceptance before Step90 can close

1. Record Git mode/type/blob IDs for **all 50 paths, in each pinned ref**, from a rerun of the full tree script or its source JSON artifact; five critical paths have only a two-ref SHA spot check here.
2. Inspect actual content deltas and resolve each governed schema/fileclass/manifest/tool/document difference; assign named reviewers.
3. Preserve the distinct Step22 and PR42/PR43 CI workflows deliberately; no automatic union of all workflows.
4. Rerun complete metadata inventory at final pinned heads and confirm no new collisions.
5. Keep real QEAX, Obsidian GUI, release and cleanup gates blocked until their own evidence and approvals exist.

This record is a scoped, durable handoff, **not** a completed 50-path semantic reconciliation.
