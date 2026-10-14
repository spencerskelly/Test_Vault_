# Branch Cleanup — Checkpoint 91: Schema and Release Semantic Gate (2026-10-14)

**Status: critical six-file content inspected, additional 44 divergent paths pending. Do not merge, delete refs, modify main, or promote release.**

## Examined refs
- `main`
- `consolidation/step22-single-repo-cutover-2026-10-11`
- Evidence: GitHub fetch_file bytes and blob SHA for six governed files, supplementing Step89 complete metadata inventory.

| File | main blob | Step22 blob | Decision |
|---|---|---|---|
| `99_System/03_Schemas/local-model.yaml` | `04b8592d9faef48aa1c952747a26e1ee917e8b58` | `361dee8269f9fbdfd16bcee33a1b808015f7ba5a` | Migration contract |
| `99_System/03_Schemas/relationships.yaml` | `c440e3925d33d0c819e8a75d1b03f3c79d72e995` | `413fd5d32d12331413fda30653c7a3a38ac2d2ab` | Graph relationship migration |
| `99_System/03_Schemas/element-types.yaml` | `8053b8bb3794db5efd56093f842e27c593a6101c` | `3f694feadb2eafd41498aff5ebc24946b9715f6d` | Type migration |
| `99_System/03_Schemas/ea-element-mapping.yaml` | `58730703c7737dfa1030a68035476d5dd6431983` | `f6b529e610202b8b5f4ef1566f16e22a2dbd3160` | Importer remapping |
| `99_System/03_Schemas/ea-connector-mapping.yaml` | `1cf170c7f8867b40f5fb4c1c0c51312951b1f5c9` | `60792ded785cbd130a00b76c240bbdd8c3788455` | Connector migration |
| `Base Vault/Definition/mdse-release.yaml` | `a1692487d555f20ae08c7595f7eea5902f391619` | `6d06db25ed50ff390460c567b8fa769981aacc9e` | Release approval gate |

## Verified substantive differences

1. Local Model `0.2 -> 0.5`: readableVersions expand from `0.1,0.2` to `0.1..0.5`; writer becomes `0.5`; explicit compatibility rules for 0.2/0.3/0.4 and upgraded local interfaces/equals. Reading is not authorization to silently rewrite old notes.
2. Element Types `1.17 -> 1.18`: prior first-class `Port`, `Function`, `State`, `State Machine`, `Design`, `Step` no longer appear in the same form; `Behavior` and `Condition` added and `Object` gains `interface` subtype. All references/fileclasses must be reconciled.
3. Relationships `1.35 -> 1.36`: endpoint type constraints changed to `Behavior`/`Condition`; earlier `hasPort/portOf`, `hasFlow/flowOf`, `exposes/exposedBy` pairs do not appear in the Step22 opening paired list. This is a graph migration, not simple YAML union.
4. EA mapping `1.0 -> 1.1`: original Port mapping `disposition: note; mdseType: Port`; Step22 uses `disposition: local; localKind: endpoint; localLabel: Interface`. Requires importer/local-ID and link stability tests.
5. Connector mapping `1.0 -> 1.1`: full semantic diff still needed to validate each connector-specific change.
6. Release manifest remains `mdseRelease: 0.8.0`, `releaseStatus: pre-release`, but moves schema relationships `1.35->1.36`, element types `1.17->1.18`, local model `0.2->0.5`; importer candidate `v0.8.6->v0.8.19` and Workbench `0.1.16->0.1.18`. Importer release remains null. The Step22 manifest is not proof of release authorization.

## Required next actions
- Create a complete old-to-new type migration matrix for all affected classes and frontmatter relationships.
- Check importer v0.8.19 handling for Port-to-local conversion, ID preservation, relationship rewiring, and old model read-only handling.
- Diff full connector mapping, release toolchain and Base Vault generated artifact/build SHA.
- Continue remaining Step89 fileclass and configuration divergences before any merge.
- Record named governance approval and actual Windows/macOS GUI / real QEAX acceptance separately; **do not infer acceptance** from static reading or synthetic tests.

This is an auditable six-file semantic review checkpoint, not the completion of all 50 path reviews.
