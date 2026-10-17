# Phase 2 connector family mapping matrix
Date: 2026-10-17
Status: Candidate classifications, NOT parser validation or row-level acceptance.
These are rule-family definitions without source records, part identifiers, diagram names, endpoint counts or model data. Corpus-specific evidence remains in local audit output.

| EA family | Native candidate or disposition | Gate | Required check |
|---|---|---|---|
| Generalization | Specialization | conditional | Orient subtype/supertype |
| Abstraction:allocate | AllocationUsage | conditional | Endpoint kind and allocation direction |
| Aggregation | Owned feature/PartUsage/reference | review | Containment flags, cardinality, reuse |
| Dependency:satisfy | SatisfyRequirementUsage | conditional | Legal requirement/subject and direction |
| Realisation | Allocation/realization evidence | review | Object-Requirement vs Object-Object |
| Dependency:refine | Refinement evidence/Dependency | review | No uncontrolled semantic equivalence |
| Dependency | Dependency | conditional | Dependency semantics |
| Dependency:trace | Dependency or external trace evidence | review | Not automatic allocation |
| Association | Connection/Interface/ReferenceUsage | review | Semantic evidence required |
| UseCase:extend | Use-case extension/context | review | Verify legal native representation |
| ControlFlow | Succession/TransitionUsage | review | Guards, branch, occurrence context |
| Dependency:deriveReqt | Requirement derivation | conditional | Both requirement ends |
| NoteLink | Documentation attachment | evidence | Not a modeled dependency |
| UseCase:include | Use-case inclusion/context | review | Do not flatten to generic dependency |
| Sequence | Message/Succession | review | Event semantics required |
| StateFlow | TransitionUsage | conditional | State, triggers, guards and effects |
| Nesting | FeatureMembership/ownership | review | Distinguish namespace nesting |
| Usage | FeatureUsage/Dependency | review | EA-specific semantics |
| Dependency:verify | VerifyRequirementUsage | conditional | Verification case vs execution |
| Dependency:RecoveryRequirement | Requirement-related evidence | review | Source stereotype meaning |
| Connector | ConnectionUsage or view evidence | evidence | Unclassified connector |
| Abstraction:Derive | Derivation/evidence | review | Explicit directed mapping required |
| Abstraction:trace | Dependency/evidence | review | Case and direction |
| Usage:Responsibility | Feature ownership/Dependency evidence | review | Responsibility not automatically perform |
| Abstraction:Refine | Refinement evidence | review | Typed semantics |
| Realisation:deriveReqt | Requirement derivation candidate | review | Contradictory type/stereotype requires manual review |

**Gate codes**: conditional = approved direction pending per-row evidence/type checks; review = ambiguity must be resolved before conversion; evidence = preserve noncanonical source evidence without inventing native semantics; deferred = native feature exists but automatic import is not approved.
