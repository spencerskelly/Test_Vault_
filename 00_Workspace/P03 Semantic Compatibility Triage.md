# P03 — Semantic Compatibility Triage for 68 Modified/Deleted Paths

Date: 2026-10-13
Repository: spencerskelly/Test_Vault_
Audit PR #41
Main reference 19f565859e4b9fb7ae63004f1b6f0a7de1b9144e; Step22 reference 58ab10870f11757cf1bf367ecd5868be9b60933d.
Status: COMPLETE PATH-LEVEL FIRST PASS; SEMANTIC DIFF & RUNTIME TESTS PENDING. Not deletion approval.

## Source basis

User-provided `Step22_Modified_Deleted_Paths.csv`, listing **47 M + 21 D**, plus read-only GitHub fetch of both trees for: element-types.yaml, relationships.yaml, local-model.yaml, mdse-release.yaml, Object.md, and one example deleted template/property note. All 68 source path names have been classified into safety review types, with no automatically approved destructive removals.

## Key confirmed changes

- Core element-types changes from blob `8053b8bb3794db5efd56093f842e27c593a6101c` in main to `3f694feadb2eafd41498aff5ebc24946b9715f6d` in Step22; Step22 says version 1.18.
- Relationship schema changes from blob `c440e3925d33d0c819e8a75d1b03f3c79d72e995` to `413fd5d32d12331413fda30653c7a3a38ac2d2ab`; Step22 version 1.36 includes first-class `hasState/stateOf`, `hasDesign/designOf` and defines Object-level `hasPart/partOf`.
- Local Model schema changes from blob `04b8592d9faef48aa1c952747a26e1ee917e8b58` to `361dee8269f9fbdfd16bcee33a1b808015f7ba5a`; Step22 version 0.5 has same-owner reciprocal Interface `equals` and contextual Connection `exposes`.
- Release manifest changes from blob `a1692487d555f20ae08c7595f7eea5902f391619` to `6d06db25ed50ff390460c567b8fa769981aacc9e`. This remains pre-release; the candidate is not an approved release by virtue of being present.
- `99_System/05_Templates/Design.md` existed on main (blob `4d4130495c56ba348cabfab9be7bea946dfa2584`), absent on Step22. `Definitions/Properties/exposes.md` existed on main (blob `61c5e38804c3379aded402f4848ddc94efb2b72d`), absent on Step22. Their *functionality* replacement cannot be inferred merely from schema declaring related local field.
- Object fileclass modified from main `004b0b72c7360f4c7af3e659006c9057e04e5e65` to Step22 `d35c2db238bf637b617d920f32a68aab7ce6639c`.

## Specific deletion gates

- Six template files deleted: Design, Function, Port, State Machine, State, Step.
- Six matching fileclass files deleted: Design, Function, Port, State Machine, State, Step.
- Nine property definition files deleted: equals, exchanges, exposes, hasClassifier, hasFlow, hasPort, interfaces, receives, transmits.
- Not all deprecated note classes are automatically replaced by Local Model: check old note parsing, links/backlinks and Obsidian Fileclass creation separately. Older historical models may require lossless migration or legacy readers.
- Do not restore removed property files wholesale without first reconciling their semantics to the canonical 1.36 and 0.5 schemas. `equals` and `exposes` now have specific local-context semantics; treating old first-class properties as drop-in substitutes risks inconsistent data.

## Modified path gates

- 5 semantic schemas: cross-version migration and importer mapping.
- 19 surviving fileclass/Obsidian UI definitions: Fileclass/frontmatter compatibility and real note handling.
- 11 Base/Obsidian release/runtime files: lock/payload hash and clean Base test.
- 8 Workspace history/current-state docs: preserve historic decisions and distinguish pending proposals.
- 2 importer docs, 1 rules document and 1 README: align statements to current semantics.
- 21 deletions all HOLD; no deletion is approved here.

## Next bounded engineering action

Compare **full content diffs** for all 21 deletions against corresponding surviving schema/fileclass/template mechanisms, with precise before/after field mapping and representative old-note fixture tests. Generate an integrated migration design and test acceptance sheet before authoring the curated branch. Then test all 47 modified paths by risk tier; especially plugin and release scripts.

Note: a 68-row companion CSV with proposed dispositions and evidence fields was generated in the user-facing workspace; GitHub checkpoint records conclusions, but not that full CSV. Runtime tests have not been executed in this pass.

No GitHub runtime code, source model, branch, PR, release or archival state was changed.
