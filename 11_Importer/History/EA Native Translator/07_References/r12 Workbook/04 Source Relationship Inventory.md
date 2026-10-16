---
uid:
type: Info
status: Working
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# r12 — Source Relationship Inventory

| Connector_Type | Effective Stereotype | Profile / FQName | Connector Count | Unique Endpoint Combinations | Matrix Rule IDs | Disposition Distribution | Coverage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Generalization |  |  | 3974 | 107 | 1, 71 | Settled 3973; Exception 1 | Complete — every observed endpoint combination has a disposition |
| Abstraction | allocate | SysML1.4::allocate | 2795 | 156 | 10, 12, 13, 14, 53, 71 | Review 1816; Settled 977; Exception 2 | Complete — every observed endpoint combination has a disposition |
| Dependency | satisfy | SysML1.4::satisfy | 2444 | 49 | 15, 17, 54, 71 | Review 733; Settled 659; Deferred 1048; Exception 4 | Complete — every observed endpoint combination has a disposition |
| Aggregation |  |  | 2288 | 92 | 2, 3, 4, 51 | Settled 2158; Review 130 | Complete — every observed endpoint combination has a disposition |
| Dependency | deriveReqt | SysML1.4::deriveReqt | 1416 | 26 | 23, 57 | Settled 1410; Review 6 | Complete — every observed endpoint combination has a disposition |
| Dependency | refine | SysML1.4::refine | 1114 | 30 | 20, 22, 65 | Settled 1114 | Complete — every observed endpoint combination has a disposition |
| Realisation |  |  | 948 | 49 | 18, 48, 55 | Settled 920; Review 28 | Complete — every observed endpoint combination has a disposition |
| Nesting |  |  | 836 | 32 | 33 | Deferred 836 | Complete — every observed endpoint combination has a disposition |
| Dependency | trace | EAUML::trace \| SysML1.4::trace | 770 | 118 | 24, 25, 26, 50 | Settled 291; Review 479 | Complete — every observed endpoint combination has a disposition |
| UseCase | extend |  | 736 | 3 | 30, 60, 71 | Settled 733; Exception 1; Review 2 | Complete — every observed endpoint combination has a disposition |
| Dependency |  |  | 667 | 95 | 27, 58 | Review 471; Settled 196 | Complete — every observed endpoint combination has a disposition |
| Association |  |  | 603 | 55 | 5, 6, 7, 8, 34, 52 | Review 98; Settled 505 | Complete — every observed endpoint combination has a disposition |
| Connector |  |  | 574 | 15 | 41, 71 | Settled 573; Exception 1 | Complete — every observed endpoint combination has a disposition |
| UseCase | include |  | 522 | 2 | 31, 61 | Review 522 | Complete — every observed endpoint combination has a disposition |
| ControlFlow |  |  | 407 | 53 | 44 | Deferred 407 | Complete — every observed endpoint combination has a disposition |
| NoteLink |  |  | 349 | 27 | 45 | Settled 349 | Complete — every observed endpoint combination has a disposition |
| Dependency | verify | SysML1.4::verify | 333 | 8 | 63, 64 | Settled 325; Review 8 | Complete — every observed endpoint combination has a disposition |
| Connector | BindingConnector | SysML1.4::BindingConnector | 249 | 5 | 40 | Settled 249 | Complete — every observed endpoint combination has a disposition |
| Usage |  |  | 235 | 11 | 49, 59, 28/29 | Review 235 | Complete — every observed endpoint combination has a disposition |
| StateFlow |  |  | 200 | 12 | 47 | Deferred 200 | Complete — every observed endpoint combination has a disposition |
| Sequence |  |  | 199 | 31 | 43 | Deferred 199 | Complete — every observed endpoint combination has a disposition |
| InformationFlow | itemFlow | SysML1.4::itemFlow | 123 | 5 | 42 | Deferred 123 | Complete — every observed endpoint combination has a disposition |
| Dependency | RecoveryRequirement | RAAML::RecoveryRequirement | 14 | 5 | 68 | Review 14 | Complete — every observed endpoint combination has a disposition |
| Abstraction | Derive | StandardProfileL2::Derive | 8 | 3 | 66, 67 | Review 1; Settled 7 | Complete — every observed endpoint combination has a disposition |
| Abstraction | trace | EAUML::trace | 5 | 3 | 26, 50 | Review 4; Settled 1 | Complete — every observed endpoint combination has a disposition |
| Dependency | ASILDecompose | RAAML::ASILDecompose | 4 | 1 | 69 | Review 4 | Complete — every observed endpoint combination has a disposition |
| Usage | Responsibility | StandardProfileL2::Responsibility | 4 | 3 | 70 | Review 4 | Complete — every observed endpoint combination has a disposition |
| Abstraction | Refine | StandardProfileL2::Refine | 3 | 2 | 20 | Settled 3 | Complete — every observed endpoint combination has a disposition |
| Realisation | deriveReqt | SysML1.4::deriveReqt | 1 | 1 | 57 | Review 1 | Complete — every observed endpoint combination has a disposition |
| Realisation | refine | SysML1.4::refine | 1 | 1 | 65 | Settled 1 | Complete — every observed endpoint combination has a disposition |
| Allocate package precedence | 05 Product Design |  | 1003 |  | 72 | Settled | Source package context overrides endpoint-type rule. |
| Allocate package precedence | 04 Product Function |  | 1410 |  | 73 | Settled | Source package context overrides endpoint-type rule. |
| Allocate total |  |  | 2795 |  |  |  | Remaining allocate connectors use lower-precedence endpoint rules or Review. |
| Allocate remaining after package rules |  |  | 382 |  |  |  | Continue review one pattern at a time. |
| Allocate endpoint precedence | Either endpoint = Issue |  | 259 |  | 74 | Settled | Normalize direction regardless EA orientation: Issue affects element / element affectedBy Issue. EA source Issue: 213; EA target Issue: 48. |
| Issue allocate endpoint spread |  |  |  |  |  |  | Change : 42; Activity : 41; Object : 27; Activity System Function: 26; UseCase : 26; Action : 20; Requirement : 11; State System State: 10 |
| Allocate endpoint precedence | Either endpoint = InformationItem |  | 40 |  | 75 | Settled | Normalize direction regardless EA orientation: InformationItem describes element / element describedBy InformationItem. EA source InformationItem: 38; EA target InformationItem: 2. |
| InformationItem allocate endpoint spread |  |  |  |  |  |  | Object : 14; State System State: 5; Issue : 3; Activity : 3; Class Module: 3; Class Physical System Variant: 3; Class Platform: 2; Action : 2 |
| Allocate endpoint precedence | Residual State involvement |  |  |  | 76 | Settled | After Design, Function, Issue, and InformationItem precedence: State stateOf element / element hasState State. |
| State allocate endpoint spread |  |  | 1044 |  |  |  | Class Hardware Component: 312; Class Module: 267; Class Physical System Variant: 123; Class Business Line: 98; Class Physical Component: 95; Class Platform: 34; Class block: 31; Object : 19 |
| Allocate endpoint precedence | Requirement ↔ Activity |  | 18 |  | 77 | Settled | Normalize to Activity satisfies Requirement / Requirement satisfiedBy Activity. |
| Allocate endpoint precedence | Requirement ↔ Class or Artifact |  | 25 |  | 78 | Settled | Normalize to Requirement appliesTo element / element applies Requirement. |
| Remaining Requirement allocate endpoint types |  |  | 38 |  |  | Review | Issue : 26; State System State: 5; Object : 2; UseCase : 2; Change : 1; InformationItem : 1; Trigger : 1 |
