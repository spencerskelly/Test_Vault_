# Golden Import — 26-family relationship decision audit
Date: 2026-10-17. Status: decision coverage only; NOT native translation acceptance.
Read-only reduced QEAX: 14,688 connectors in 26 exact type/stereotype families. No source IDs or model rows in repository.

| EA connector family | Count | Decision |
|---|---:|---|
| Generalization | 3735 | specialization |
| Abstraction:allocate | 2605 | native allocation |
| Aggregation | 2267 | owned PartUsage where physical containment is evidenced, else review |
| Dependency:satisfy | 1330 | native satisfy |
| Realisation | 883 | part-to-action perform; part-to-requirement allocate; part-to-part allocate; else review |
| Dependency:refine | 596 | Dependency plus Refinement metadata |
| Dependency | 429 | native Dependency |
| Dependency:trace | 414 | Dependency with trace provenance |
| Association | 395 | ConnectionUsage if connectivity proven; otherwise review |
| UseCase:extend | 378 | conditional optional case usage |
| ControlFlow | 271 | Succession with source guards |
| Dependency:deriveReqt | 232 | requirement derivation |
| NoteLink | 220 | MDSE YAML links; no native relationship |
| UseCase:include | 219 | required nested case usage |
| Sequence | 193 | reference-only interaction |
| StateFlow | 171 | state transition |
| Nesting | 137 | approved nested state/activity/port/requirement usage; else organizational |
| Usage | 128 | generic Dependency unless independently stronger evidence |
| Dependency:verify | 47 | verification |
| Dependency:RecoveryRequirement | 10 | requirement derivation |
| Connector | 9 | port-to-port ConnectionUsage |
| Abstraction:Derive | 6 | requirement derivation |
| Abstraction:trace | 5 | Dependency with trace provenance |
| Usage:Responsibility | 4 | allocation when role is evidenced |
| Abstraction:Refine | 3 | Dependency plus Refinement metadata |
| Realisation:deriveReqt | 1 | requirement derivation only with compatible requirements/roles, otherwise review |
| **Total** | **14688** | **26 families** |

All families have an approved translation direction or explicit non-native/review disposition. Semantic eligibility remains per-connector; native success is NOT claimed.
Implementation gate: exact-family precedence (notably Realisation:deriveReqt over generic Realisation); trusted endpoints/direction/ownership; 14,688 source rows with exclusive dispositions; official parser validation; private model ledger.