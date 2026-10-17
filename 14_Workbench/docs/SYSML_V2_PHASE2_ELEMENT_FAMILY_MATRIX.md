# Phase 2 element family mapping matrix
Date: 2026-10-17
Status: Candidate classifications, NOT parser validation or row-level acceptance.
These are rule-family definitions without source records, part identifiers, diagram names, endpoint counts or model data. Corpus-specific evidence remains in local audit output.

| EA family | Native candidate or disposition | Gate | Required check |
|---|---|---|---|
| Package | Namespace/Package | review | Package provenance only; vault placement independent |
| Requirement:requirement | RequirementDefinition/Usage | conditional | Definition vs usage |
| Class:Hardware Component | PartDefinition | conditional | Actual physical ownership |
| UseCase | UseCaseDefinition/Usage | conditional | Case feature typing |
| Requirement:designConstraint | RequirementDefinition/Usage | conditional | Constraint requirement distinct from ConstraintUsage |
| State:System State | StateDefinition/Usage | conditional | Substate ownership |
| Activity | ActionDefinition/Usage | conditional | Owned action and execution semantics |
| Requirement:functionalRequirement | RequirementDefinition/Usage | conditional | Functional requirement |
| Signal:Logical Signal | ItemDefinition/EventOccurrence | review | Payload or event evidence |
| InformationItem | ItemDefinition | review | Typed item vs source annotation |
| Note | Documentation/metadata | evidence | No automatically created semantic node |
| Object | PartUsage/ItemUsage | review | Classifier and containing owner |
| Class:block | PartDefinition | conditional | SysML v1 stereotype validated |
| Class:Physical Component | PartDefinition | conditional | Physical semantics |
| Activity:System Function | ActionDefinition/Usage | conditional | Perform usage separate |
| State | StateDefinition/Usage | conditional | State usage/context |
| Issue | External issue evidence/metadata | evidence | Separate issue records |
| Class:Module | PartDefinition | conditional | Compositional usage owned by parent |
| Activity:Hardware Function | ActionDefinition/Usage | conditional | Performance mapping |
| Requirement | RequirementDefinition/Usage | conditional | Role and owner |
| Class:System Partner | PartDefinition/external role | review | Partner vs contained part |
| Class:Software Component | PartDefinition/ItemDefinition | conditional | Architecture source evidence |
| Activity:testCase | VerificationCaseDefinition/Usage | review | Do not auto-equate to test case |
| Class:Physical System Variant | PartDefinition; Variation candidate | deferred | Do not infer native Variant |
| Class:Electrical & Material Interface | InterfaceDefinition/PortDefinition | review | Actual interface and port identity |
| Class:Data Interface | InterfaceDefinition/PortDefinition | review | Port ownership/type |
| Activity:Software Function | ActionDefinition/Usage | conditional | Performed action |
| Artifact:Image | Evidence/documentation | evidence | Attachment, not native structure |
| Change | External change evidence | evidence | Do not invent a core relationship |
| Requirement:extendedRequirement | RequirementDefinition/Usage | conditional | EA extension metadata |
| Action | ActionUsage | review | Owner and parent action |
| StateNode | State/transition view element | evidence | Diagram artifact vs semantic object |
| Artifact:Document | Documentation/evidence | evidence | External evidence |
| Class:Physical Context | Case/PartDefinition | review | Context role evidence |
| Text | Documentation/view annotation | evidence | Not canonical object by default |
| Actor | External participant/PartDefinition | review | Boundaries and roles |
| Class:Mechanical Interface | InterfaceDefinition/PortDefinition | review | Full port vs proxy port |
| Decision | Control-flow decision | evidence | Guard/source action check |
| Class:Generic Physical Interface | InterfaceDefinition/PortDefinition | review | Interface identity |
| Port | PortUsage | review | Proxy/full/conjugation |
| Class | PartDefinition/ItemDefinition | review | No stereotype |
| Class:Platform | PartDefinition | conditional | Architecture |
| Synchronization | Succession control semantics | evidence | Preserve fork/join evidence |
| Activity:Module Function | ActionDefinition/Usage | conditional | Action ownership |
| Class:Business Line | Namespace/organizational metadata | evidence | Not automatically a part |
| Part:FlowProperty | Item/port feature | review | Legacy flow property |
| Signal:Software Parameter | AttributeDefinition/Usage or ItemDefinition | review | Parameter value or payload |
| Trigger | Transition trigger | review | Owner, guard and event |
| Boundary | Diagram annotation | evidence | Not native boundary node |
| Class:Software Unit | PartDefinition | conditional | Typed unit |
| ProxyConnector | Connection/interface or view artifact | review | No inference from glyph |
| Sequence | Interaction occurrence/view | evidence | Context needed |
| Requirement:Functional | RequirementDefinition/Usage | conditional | Stereotype normalization |
| Text:NavigationCell | View-only annotation | evidence | Do not import as model relation |
| Constraint | ConstraintDefinition/Usage | review | Expression and ownership |
| Event | EventOccurrenceUsage | review | Event typing |
| Part | PartUsage | review | Classifier/ownership |
| Requirement:Webasto Requirement | RequirementDefinition/Usage | conditional | External stereotype provenance |
| Requirement:performanceRequirement | RequirementDefinition/Usage | conditional | Numeric evidence |

**Gate codes**: conditional = approved direction pending per-row evidence/type checks; review = ambiguity must be resolved before conversion; evidence = preserve noncanonical source evidence without inventing native semantics; deferred = native feature exists but automatic import is not approved.
