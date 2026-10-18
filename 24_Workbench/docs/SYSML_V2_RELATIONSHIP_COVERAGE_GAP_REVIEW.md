# SysML v2 Relationship and Modeling Construct Coverage — Review Summary
Date: 2026-10-17
Status: Review-level coverage inventory; not a complete certified metamodel or translator implementation.
Sources: SysML v2.0 Language / Transformation, prior approvals in this vault and reviewed decision documents.

## Status terminology
APPROVED: mapping/modeling policy agreed, not proof of code.
DEFERRED: native support approved but inferred EA/BOM mapping intentionally not approved.
REVIEW: mapping/evidence or normalization decision still needed.
VERIFY: exact official grammar/metamodel, parser and source-corpus checks pending.

## A. Approved existing-EA translation families
| Family | Approved policy |
|---|---|
| Activity/Function allocated to Object | Object owns PerformActionUsage, with source EA evidence |
| Design modeled as State allocated to Object | Object owns ExhibitStateUsage, reverse view role, source evidence |
| Object allocated to Object | Native Allocation, original intended direction |
| Object Realization to Requirement | Requirement -> Object Allocation; no inferred satisfaction |
| Object Realization to Object | Native Allocation only for genuine implementation mapping; other patterns still evidence review |
| EA Generalization | One-to-one native Specialization, no proactive redefinition |
| EA Dependency and compatible Usage | Native Dependency; other special cases distinct |
| Explicit compatible EA Information/Item/Object Flow | Native Flow; temporal payload transfers evaluated for SuccessionFlow |
| Sequence Messages / explicit signal interactions | Native Message when event semantics available |
| EA ControlFlow | Native Succession or guarded native transition with preserved branch semantics |
| EA StateMachine transitions | Native TransitionUsage with trigger/guard/effect where present |
| Valid EA port-to-port interface semantics | Native InterfaceUsage with typed PortUsages |
| Binding | Native binding with exact equality semantics; no generic 'exposes' rewrite |
| Copy | Canonical note with native alias only where identity-equivalent, relationships/content merged with provenance |
| EA part relationship multiplicity | Native part usage multiplicity; not automatic BOM quantity |
| Explicit EA attributes, quantities, enumerations, constraints, calculations, requirements | Map to reviewed compatible native definition/usage/standard-library constructs; verify actual evidence and syntax |

## B. Approved native modeling without automatic general inference
| Family | Status |
|---|---|
| Feature typing, definition/usage | APPROVED; one definition many usages |
| Composite/reference/shared usages | APPROVED prior rules retained |
| Native PortDefinition/PortUsage/Conjugation | APPROVED; explicit compatible EA conjugation only |
| Redefinition | DEFERRED automatic EA/BOM mapping, DVS family follow-up |
| Subsetting | DEFERRED automatic EA/BOM mapping |
| Variation and Variant | DEFERRED automatic source mapping; product family evaluation later |
| Namespace/import/alias membership, feature chaining, metadata, documentation, feature values, multiplicity | APPROVED Group 1 |
| Unioning/Intersecting/Differencing and enumerated advanced feature operations | APPROVED Group 2, detailed formal registry pending |
| Occurrence/Event Occurrence, TimeSlice/Snapshot | APPROVED Group 3, only explicit compatible EA import |
| Standard-library Causation | APPROVED Group 3, never inferred from mere succession |
| AnalysisCaseDefinition/Usage, TradeStudies library, objective/subject/evaluation/result | APPROVED Group 3, explicit compatible import only |
| Requirement verification and derivation; decomposition, satisfaction, constraints/assertions/calculations | Earlier approval, formal registry entries required |
| Local workflow action/state model plus separate custom Canvas | APPROVED design architecture |
| Workbench draw-to-choose operation menu and contextual definitions | APPROVED design requirements |

## C. Material gaps / next priorities
P0-01 Formal metamodel completeness: compare native SysML 2.0 + KerML operation inventory and normative libraries against catalog, not just previous conversation topics. Include feature membership kinds, definition/usage, portioning, occurrences, constraints, cases, assertions, metadata, expression and timing constructs.
P0-02 Build actual versioned machine-readable relationship/operation registry with a source/target/ownership eligibility engine shared by EA importer and Workbench; proposed docs do not yet constitute live registry.
P0-03 Generate individual vault-native definition Markdown entries for every approved construct with normative version, exact grammar, non-equivalence, EA/BOM mapping, structural and graphical presentation, navigation, validation, round-trip and provenance.
P0-04 Audit source EA export and BOM samples: count every t_object/t_connector and relationship shape, including missing ends, Copy identity conflicts, Realization subtypes, bad ports, branch/guard evidence and diagram-only artifacts; comprehensive source-to-target disposition ledger.
P0-05 Validate native syntax with official compatible parser/library for every mapping, including standard-library pinning. Earlier illustrative code snippets are not conformance evidence.
P0-06 Workbench proof of concept: draw line -> eligible operations -> selected native feature creation; info drawer open/close without losing current selection; type filters and custom views.
P0-07 Canonical file/view synchronization and round-trip with Obsidian notes/Canvas and Git provenance, stable IDs, undo and conflict detection.
P0-08 BOM identity and source reconciliation; where-used, parent-owned usages, quantity/UOM, revision history, variantOf and merge behavior.
P1-09 Product-family refinement for DVS: Redefinition, Variants, Subsetting; no speculative import.
P1-10 Workflow Canvas sequences, Messages, guarded branches, scoped views and native local semantics; leave visual polish to later.
P1-11 Analysis and trade study: dedicated Analysis View, source data versioning, reproducible calculation results, preference vs satisfaction/verification distinction.
P1-12 Revisit unsupported EA Realization, Trace/Abstraction, association, dependency stereotype families and any uncovered construct, with no silent conversion.

## Repository evidence boundary
Individual decision markdown files exist for approved topics in 14_Workbench/docs, but some earlier-reviewed requirement/attribute/binding/port decisions remain only referenced in consolidated documents, not normalized as individual verified semantic reference entries. Do not equate approval with implemented functionality. No automated end-to-end conformance or source corpus reconciliation is claimed by this summary.
