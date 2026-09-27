---
uid:
type: Info
status: Working
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# r12 — Deferred Review

| Topic | Current Handling | Why Deferred | Dry-Run Evidence to Capture | Decision Needed Later |
| --- | --- | --- | --- | --- |
| Item Flow / InformationFlow | Source only | User explicitly postponed Item Flow import until more of the importer is defined. | Counts, endpoint patterns, conveyed-item names/types, duplicate/reuse patterns. | Whether to create first-class Item Flow notes and interface carries/flowsOn links. |
| Explicit EA Nesting connector | Review/source only | Earlier packages did not establish stable semantics. | Counts by endpoint types, package examples, connector notes/stereotypes. | Semantic mapping by endpoint pattern. |
| Design satisfying Functional Requirement | Review | Conflicts with later stricter satisfaction semantics. | All Design→Functional Requirement satisfy connectors with names/packages. | Whether mapping is satisfies, appliesTo, omitted Function, or source-model error. |
| State / State Machine satisfy Requirement | Review | Older translator allowed it; later project direction restricted satisfaction to Function/Design. | All such connectors and nearby functions/designs. | Final satisfaction scope. |
| Physical Context / Use Case participants | Settled: one-sided `participants` YAML on owning Context/Use Case | No longer deferred. Subject versus participant semantic refinement is intentionally postponed to post-import cleanup. | Dry run should report participant counts, owning-element EA types, endpoint types, and connector patterns for validation. | Only revisit if post-import cleanup needs a distinct `subject` relationship or another context-specific semantic relation. |
| ControlFlow / Sequence | Inline/source detail | Avoid creating notes for flow constructs and avoid global sequence relationships. | Counts, branch patterns, guards, control nodes, repeated behavior usage. | Whether/when Functional Flow should become first-class in native import. |
| ObjectFlow | Inline/source detail | Item Flow / Functional Flow reconstruction is postponed for the native import. | Counts, endpoint types, conveyed objects/items, direction, guards, owner diagram/flow. | Whether ObjectFlow becomes Item Flow, Functional Flow edge, or another local construct. |
| StateFlow | Transition evidence / source detail | Older translator created Transition semantics, but current native rule says connectors do not become notes. | Counts, source/target State types, trigger/guard/effect, owning StateMachine, connector stereotypes. | Whether native import creates Transition notes from StateFlow or preserves them for post-import transformation. |
| Activity→Activity Realisation | Review/source only | Monitor System exposed the pattern but semantic meaning was not established. | Counts, Activity stereotypes/types, names, connector notes, package context. | Mapping by endpoint semantics or explicit Ignore/Deferred rule. |
| Issue→State Usage | Review/source only | Monitor System exposed the pattern; literal Usage is not trusted. | Counts, issue/state names/types, connector metadata, neighboring relationships. | Whether it means affects, state context, dependency, or source-model error. |
| Mixed trace endpoint patterns | Review/source only | Monitor System contained Activity/State/Requirement trace patterns outside approved endpoint rules. | Counts by exact source/target types/stereotypes and connector metadata. | Endpoint-specific semantic rules or explicit ignore decisions. |
| Full-model relationship combination reconciliation | Complete — 21,822 connectors reconciled | No longer deferred. 30 raw source families and 1,000 endpoint combinations are fully inventoried. | Observed Combinations sheet contains every grouped combination and its rule/disposition. | Maintain this reconciliation whenever source EA export changes. |
| RAAML RecoveryRequirement | Review | 14 observed connectors; no approved MDSE semantic equivalent yet. | Endpoint names/types, connector notes, RAAML stereotype, package context. | Decide whether this means recovery linkage, satisfaction, derivation, or another relation. |
| RAAML ASILDecompose | Review | 4 observed Requirement→Requirement connectors; decomposition semantics not yet approved. | Requirement statements, safety context, connector notes. | Choose parent/child, derivedFrom, refines, or retain source-only. |
| StandardProfile Responsibility | Review | 4 observed Usage connectors; current vocabulary has no responsibility relationship. | Business Line/block/Physical Context endpoint context and connector notes. | Decide whether to add a relationship or preserve only source evidence. |
