# SysML v2 approved translation baseline and first-test handoff — 2026-10-18

## Status and change control

**Approved semantic decisions are fixed implementation requirements, not open choices.** This document consolidates decisions already agreed in prior MDSE Continues conversations. It does not supersede a more specific approved mapping or authorize changes to an approved mapping. Where a historical 2026-10-15 document says `draft`, `candidate`, or asks for a decision that was subsequently made, preserve its historical wording and apply the subsequent approved decision. A code gap is not grounds for semantic reinterpretation.

V1 toolchain is complete/frozen. V2 work is active under numbered 20+ folders; shared test harnesses / registries may still physically reside in 14_Workbench and 15_Testing and must be treated as V2 dependencies, not permission to develop V1.

## Frozen semantic contracts

1. **Source authority**: Native OMG SysML v2 semantics govern formal model structure and relationships. Do not manufacture custom native v2 relationships. Unsupported/ambiguous EA semantics are recorded separately as explicit evidence/flagLink; do not silently drop or canonically assert them.
2. **Notes and usages**: One MDSE note per reusable defined element; occurrences/usages are declared in the owning note, not duplicated as definition notes. Shared elements reuse the same definition. Packages organize folders without by themselves implying formal composition.
3. **Text authority**: The last `## SysML v2` section, containing governed `sysml` fenced textual source, is authoritative. Free Markdown above is preserved. Workbench structural/visual navigation is derived from text and rebuilt from it; edits must update native text atomically and be parser validated.
4. **Metadata/provenance**: Governed YAML retains MDSE type/subtype and source EA type/stereotype, deterministic UID, original source identity/provenance and explicit `flagLink` review evidence. Do not treat YAML-only source labels as native SysML assertions.
5. **Definitions/relations**: Physical Objects as reusable `part def`, context-owned `part` usages, specialization distinct from containment, actual source multiplicity on usages, valid nested states and actions, requirements and verification, constraints/calculations, attribute/unit kinds, namespaces, causation versus temporal succession and analysis/trade studies according to the approved category decisions.
6. **Ports and connections**: Preserve ProxyPort/FullPort distinctions; FullPort may require part usage, ProxyPort port usage, and Binding Port remains semantically distinct. Preserve contextual endpoints, boundary/exposure, flows, messages, conjugation, binding/equality and connection semantics. Never conflate a graphical edge with native relationship validity.
7. **Source ingestion**: One common EA source graph, separate V1/V2 mapping profiles. No automatic folder-to-containment mapping. All EA States are represented as SysML v2 States. Stereotyped Function activities stay Functions regardless of EA folder location. Generalization orientation requires source-proven direction and native eligibility.
8. **UID and BOM**: Preserve approved EA identity allocation; BOM deterministic UID allocation uses 2020 baseline separately. One part-number definition note; BOM parent owns usages and quantities/UOM; manufacturing alternates are non-additive and effectivity/revisions are handled separately. Never invent variant/generalization based only on similar builds.
9. **Workbench**: Distinct structural and visual representation, containment/connection behavior, navigation, validation, round-trip/provenance for every approved mapping. Existing note-first actions and popup behavior govern UX, not independent semantic storage.
10. **Safety**: Keep QEAX, BOM originals, private ledgers, EA identifiers and generated real model content outside public Test_Vault_. Never promote source-only normalization, parser-only syntax acceptance, or accepted decisions into unwarranted 'native certified' claims.

## Where authorities live

- `26_Definitions/`: v2-approved architecture, structural semantics, BOM, mapping and user decisions.
- `29_SysMLv2_Translator_Workbench/`: historical and operational source profiles, approved family mapping discussion, passes 4–9 evidence and executable handoff notes.
- `14_Workbench/registry/`, `15_Testing/`: currently shared implementation locations for V2 registries, parsers, canonical graph, normalization and synthetic regression checks; relocate only after passing tests.
- `20_Base Vault/`, `21_Importer/`, `23_Bootstrap/`, `24_Workbench/`, `25_Testing/`: V2 product and acceptance targets. A placeholder README is not a runnable implementation.

## Evidence already established

- Reduced QEAX: 11,447 `t_object`, 14,688 `t_connector`, 1,389 `t_package`, 2,208 `t_diagram`; 100 SQLite tables; source integrity `ok` when inspected read-only on 2026-10-18.
- Phase 8 full ledger reconciliation: 14,688/14,688 replay, 0 reported errors, 0 native certified; counts are dispositions, not v2 output.
- Official parser positive/negative fixture CI: 2026-10-17 run 39099574792 passed. This establishes basic native parser execution, not all relationship semantics.
- Phase 9 generalization source-bound bridge: review-only; source direction and semantic guard gaps documented for follow-up; not native emitter permission.
- `24_Workbench/v2-workbench.html`: stand-alone read-only exploratory prototype; note-first editor handoff exists but isn't the deployed Obsidian plugin.

## First test on 2026-10-18

**Test A — source and governance (already runnable):** verify QEAX read-only SQLite integrity, source count/profile, ledger coverage and orientation check. Publish aggregate counts only.

**Test B — native syntax (runnable with pinned parser CI):** rerun positive+negative official parser workflow and golden charger fixture; record exactly which fixture, parser pin and syntax/semantic coverage passed.

**Test C — first generated import (not yet evidenced):** wire the vetted EA source reader and canonical graph through approved v2 serializer and bottom-of-note writer to an isolated disposable V2 Base, produce a small scoped native slice and diagnostics; independently parse; open read-only in Workbench. Do not label a deferred-only output 'golden'.

## Next implementation order — do not reapprove the ontology

1. Inventory V2-relevant executable files (including real code still located under 14/15), and identify actual callable importer/emitter/writer entrypoints.
2. Run the existing source/ledger and native parser fixture tests; capture reproducible aggregate outputs at exact SHA.
3. Implement only the missing graph→native emitter→note writer integration for one scope, using approved definitions and permitted relationships.
4. Test one small actual QEAX slice, validate syntax and source dispositions, then scale to all 11,447 elements/14,688 connectors with review queue.
5. Package as a stand-alone offline HTML test importer and disposable V2 base; integrate read-only Workbench and Bootstrap.
6. Run deterministic rerun, output audit, zero hidden drops, GUI inspection before golden acceptance.

**No approved semantic mapping is reopened by these steps.** Any discrepancy is recorded as implementation defect or an explicit new change request requiring separate user approval.
