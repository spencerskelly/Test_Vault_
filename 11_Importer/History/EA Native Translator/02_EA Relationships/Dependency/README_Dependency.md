---
uid:
type: EA Relationship Type Definition
status: Working
eaConnectorType: "Dependency"
connectorCount: 6762
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# EA Relationship Type — Dependency

## Source identity

- **Connector_Type:** `Dependency`
- **Observed connectors:** 6762

## Observed variants

| Variant | Connectors | Endpoint combinations | Matrix rules | Disposition distribution |
|---|---:|---:|---|---|
| [[EA Relationship - No Stereotype\|No stereotype]] | 667 | 95 | 27, 58 | Review 471; Settled 196 |
| [[EA Relationship Stereotype - ASILDecompose\|ASILDecompose]] | 4 | 1 | 69 | Review 4 |
| [[EA Relationship Stereotype - deriveReqt\|deriveReqt]] | 1416 | 26 | 23, 57 | Settled 1410; Review 6 |
| [[EA Relationship Stereotype - RecoveryRequirement\|RecoveryRequirement]] | 14 | 5 | 68 | Review 14 |
| [[EA Relationship Stereotype - refine\|refine]] | 1114 | 30 | 20, 22, 65 | Settled 1114 |
| [[EA Relationship Stereotype - satisfy\|satisfy]] | 2444 | 49 | 15, 17, 54, 71 | Review 733; Settled 659; Deferred 1048; Exception 4 |
| [[EA Relationship Stereotype - trace\|trace]] | 770 | 118 | 24, 25, 26, 50 | Settled 291; Review 479 |
| [[EA Relationship Stereotype - verify\|verify]] | 333 | 8 | 63, 64 | Settled 325; Review 8 |

## Observed endpoint combinations

| Source endpoint | Target endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---:|---|---|---|
| [[EA Stereotype - functionalRequirement]] | [[EA Stereotype - requirement]] | 560 | 23 | Settled | Map: derivedFrom / derivedBy |
| [[EA Stereotype - designConstraint]] | [[EA Stereotype - requirement]] | 542 | 23 | Settled | Map: derivedFrom / derivedBy |
| [[EA Stereotype - System State]] | [[EA Stereotype - requirement]] | 364 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| [[EA Stereotype - System State]] | [[EA Stereotype - designConstraint]] | 340 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| [[EA Element - No Stereotype]] | [[EA Stereotype - requirement]] | 336 | 54 | Review | Review: satisfy endpoint pattern |
| [[EA Stereotype - requirement]] | [[EA Stereotype - requirement]] | 295 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - testCase]] | [[EA Stereotype - requirement]] | 272 | 63 | Settled | Map: verifies / verifiedBy |
| [[EA Stereotype - requirement]] | [[EA Stereotype - requirement]] | 236 | 22 | Settled | Map: refines / refinedBy |
| [[EA Stereotype - designConstraint]] | [[EA Stereotype - designConstraint]] | 228 | 22 | Settled | Map: refines / refinedBy |
| [[EA Stereotype - System Function]] | [[EA Stereotype - functionalRequirement]] | 224 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Element - No Stereotype]] | [[EA Stereotype - functionalRequirement]] | 196 | 54 | Review | Review: satisfy endpoint pattern |
| [[EA Stereotype - System Function]] | [[EA Stereotype - requirement]] | 185 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[README_UseCase]] | [[EA Stereotype - functionalRequirement]] | 179 | 20 | Settled | Map: describes / describedBy |
| [[EA Element - No Stereotype]] | [[EA Stereotype - requirement]] | 176 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| [[EA Stereotype - Document]] | [[EA Stereotype - Regulatory Requirement]] | 173 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Element - No Stereotype]] | 160 | 54 | Review | Review: satisfy endpoint pattern |
| [[README_UseCase]] | [[EA Stereotype - requirement]] | 155 | 20 | Settled | Map: describes / describedBy |
| [[README_InformationItem]] | [[EA Stereotype - requirement]] | 121 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| [[EA Stereotype - Image]] | [[EA Stereotype - Hardware Component]] | 103 | 24 | Settled | Map: describes / describedBy |
| [[EA Stereotype - System Function]] | [[EA Element - No Stereotype]] | 88 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Stereotype - requirement]] | [[EA Stereotype - requirement]] | 78 | 23 | Settled | Map: derivedFrom / derivedBy |
| [[README_UseCase]] | [[EA Stereotype - designConstraint]] | 70 | 20 | Settled | Map: describes / describedBy |
| [[EA Element - No Stereotype]] | [[EA Stereotype - designConstraint]] | 60 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| [[EA Element - No Stereotype]] | [[EA Element - No Stereotype]] | 58 | 27 | Settled | Map: dependsOn / dependencyOf |
| [[EA Stereotype - functionalRequirement]] | [[EA Element - No Stereotype]] | 55 | 23 | Settled | Map: derivedFrom / derivedBy |
| [[EA Stereotype - System State]] | [[EA Stereotype - extendedRequirement]] | 53 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| [[EA Stereotype - System Function]] | [[EA Stereotype - System State]] | 51 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - Hardware Function]] | [[EA Stereotype - requirement]] | 49 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Stereotype - designConstraint]] | [[EA Element - No Stereotype]] | 40 | 23 | Settled | Map: derivedFrom / derivedBy |
| [[EA Element - No Stereotype]] | [[EA Stereotype - System State]] | 39 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - System Function]] | 35 | 27 | Settled | Map: dependsOn / dependencyOf |
| [[EA Stereotype - System Function]] | [[EA Stereotype - System Function]] | 35 | 27 | Settled | Map: dependsOn / dependencyOf |
| [[EA Stereotype - Hardware Function]] | [[EA Stereotype - functionalRequirement]] | 31 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Stereotype - System State]] | [[EA Element - No Stereotype]] | 30 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| [[EA Stereotype - designConstraint]] | [[EA Stereotype - Regulatory Requirement]] | 29 | 23 | Settled | Map: derivedFrom / derivedBy |
| [[EA Stereotype - designConstraint]] | [[EA Stereotype - requirement]] | 27 | 22 | Settled | Map: refines / refinedBy |
| [[EA Stereotype - testCase]] | [[EA Stereotype - designConstraint]] | 26 | 63 | Settled | Map: verifies / verifiedBy |
| [[EA Stereotype - testCase]] | [[EA Stereotype - functionalRequirement]] | 26 | 63 | Settled | Map: verifies / verifiedBy |
| [[EA Stereotype - System Function]] | [[EA Element - No Stereotype]] | 25 | 27 | Settled | Map: dependsOn / dependencyOf |
| [[README_InformationItem]] | [[EA Stereotype - requirement]] | 25 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Stereotype - System State]] | 23 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - Software Function]] | [[EA Stereotype - requirement]] | 22 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[README_InformationItem]] | [[EA Stereotype - Hardware Component]] | 22 | 24 | Settled | Map: describes / describedBy |
| [[README_InformationItem]] | [[EA Stereotype - requirement]] | 21 | 24 | Settled | Map: describes / describedBy |
| [[EA Stereotype - designConstraint]] | [[EA Stereotype - designConstraint]] | 20 | 23 | Settled | Map: derivedFrom / derivedBy |
| [[EA Stereotype - designConstraint]] | [[EA Stereotype - extendedRequirement]] | 20 | 23 | Settled | Map: derivedFrom / derivedBy |
| [[EA Stereotype - functionalRequirement]] | [[EA Stereotype - functionalRequirement]] | 20 | 23 | Settled | Map: derivedFrom / derivedBy |
| [[EA Element - No Stereotype]] | [[EA Stereotype - designConstraint]] | 20 | 54 | Review | Review: satisfy endpoint pattern |
| [[EA Stereotype - System Function]] | [[EA Stereotype - Hardware Function]] | 18 | 27 | Settled | Map: dependsOn / dependencyOf |
| [[EA Stereotype - requirement]] | [[EA Stereotype - functionalRequirement]] | 18 | 22 | Settled | Map: refines / refinedBy |
| [[README_Issue]] | [[EA Stereotype - functionalRequirement]] | 16 | 25 | Settled | Map: affects / affectedBy |
| [[EA Stereotype - functionalRequirement]] | [[EA Stereotype - requirement]] | 15 | 22 | Settled | Map: refines / refinedBy |
| [[README_InformationItem]] | [[EA Stereotype - Software Component]] | 14 | 24 | Settled | Map: describes / describedBy |
| [[EA Stereotype - functionalRequirement]] | [[EA Stereotype - designConstraint]] | 13 | 23 | Settled | Map: derivedFrom / derivedBy |
| [[EA Stereotype - Module Function]] | [[EA Stereotype - requirement]] | 13 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Element - No Stereotype]] | [[EA Element - No Stereotype]] | 12 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - Software Function]] | [[EA Stereotype - functionalRequirement]] | 12 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Stereotype - Document]] | [[EA Stereotype - requirement]] | 11 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| [[EA Stereotype - Module]] | [[README_Text]] | 11 | 50 | Review | Review: trace endpoint pattern |
| [[README_Issue]] | [[README_UseCase]] | 11 | 25 | Settled | Map: affects / affectedBy |
| [[EA Stereotype - Software Component]] | [[EA Stereotype - Software Component]] | 10 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - requirement]] | [[EA Stereotype - Document]] | 10 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - Hardware Function]] | [[EA Stereotype - System State]] | 9 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Stereotype - functionalRequirement]] | 9 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| [[README_InformationItem]] | [[EA Stereotype - functionalRequirement]] | 9 | 24 | Settled | Map: describes / describedBy |
| [[EA Stereotype - System Function]] | [[EA Element - No Stereotype]] | 8 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - Module Function]] | [[EA Stereotype - functionalRequirement]] | 8 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Stereotype - System Function]] | [[EA Stereotype - designConstraint]] | 8 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Element - No Stereotype]] | [[EA Element - No Stereotype]] | 8 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| [[README_Object]] | [[README_Text]] | 8 | 50 | Review | Review: trace endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - System State]] | 8 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - designConstraint]] | [[EA Stereotype - requirement]] | 8 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - extendedRequirement]] | [[EA Stereotype - Document]] | 8 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - requirement]] | [[EA Stereotype - requirement]] | 7 | 58 | Review | Review: Dependency endpoint pattern |
| [[README_UseCase]] | [[EA Element - No Stereotype]] | 7 | 20 | Settled | Map: describes / describedBy |
| [[EA Stereotype - Module Function]] | [[EA Element - No Stereotype]] | 7 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Stereotype - Document]] | [[EA Stereotype - requirement]] | 7 | 24 | Settled | Map: describes / describedBy |
| [[EA Stereotype - block]] | [[README_Text]] | 7 | 50 | Review | Review: trace endpoint pattern |
| [[README_InformationItem]] | [[EA Stereotype - Physical System Variant]] | 7 | 24 | Settled | Map: describes / describedBy |
| [[README_InformationItem]] | [[EA Element - No Stereotype]] | 7 | 24 | Settled | Map: describes / describedBy |
| [[EA Stereotype - functionalRequirement]] | [[EA Stereotype - requirement]] | 7 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - requirement]] | [[EA Stereotype - designConstraint]] | 6 | 23 | Settled | Map: derivedFrom / derivedBy |
| [[README_InformationItem]] | [[EA Stereotype - functionalRequirement]] | 6 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| [[EA Stereotype - functionalRequirement]] | [[EA Stereotype - functionalRequirement]] | 6 | 22 | Settled | Map: refines / refinedBy |
| [[EA Stereotype - Physical System Variant]] | [[README_InformationItem]] | 6 | 50 | Review | Review: trace endpoint pattern |
| [[README_InformationItem]] | [[EA Stereotype - Module]] | 6 | 24 | Settled | Map: describes / describedBy |
| [[README_Issue]] | [[EA Stereotype - designConstraint]] | 6 | 25 | Settled | Map: affects / affectedBy |
| [[EA Element - No Stereotype]] | [[EA Stereotype - System Function]] | 6 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Stereotype - requirement]] | 6 | 50 | Review | Review: trace endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Hardware Function]] | 5 | 27 | Settled | Map: dependsOn / dependencyOf |
| [[EA Stereotype - Hardware Component]] | [[EA Stereotype - Hardware Component]] | 5 | 58 | Review | Review: Dependency endpoint pattern |
| [[README_Issue]] | [[EA Stereotype - designConstraint]] | 5 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - designConstraint]] | 5 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - extendedRequirement]] | [[EA Stereotype - requirement]] | 5 | 23 | Settled | Map: derivedFrom / derivedBy |
| [[README_InformationItem]] | [[EA Stereotype - Hardware Component]] | 5 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| [[EA Stereotype - functionalRequirement]] | [[EA Stereotype - designConstraint]] | 5 | 22 | Settled | Map: refines / refinedBy |
| [[README_Action]] | [[EA Stereotype - requirement]] | 5 | 54 | Review | Review: satisfy endpoint pattern |
| [[README_InformationItem]] | [[README_UseCase]] | 5 | 24 | Settled | Map: describes / describedBy |
| [[EA Stereotype - functionalRequirement]] | [[EA Stereotype - functionalRequirement]] | 5 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - requirement]] | [[README_InformationItem]] | 5 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - Hardware Function]] | [[EA Stereotype - Hardware Function]] | 4 | 27 | Settled | Map: dependsOn / dependencyOf |
| [[EA Stereotype - Module Function]] | [[EA Stereotype - System State]] | 4 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - testCase]] | [[README_Object]] | 4 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - requirement]] | [[EA Stereotype - Physical Component]] | 4 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - functionalRequirement]] | [[EA Stereotype - requirement]] | 4 | 69 | Review | Review: RAAML ASILDecompose |
| [[EA Stereotype - System State]] | [[EA Stereotype - designConstraint]] | 4 | 68 | Review | Review: RAAML RecoveryRequirement |
| [[EA Stereotype - Functional]] | [[EA Stereotype - requirement]] | 4 | 23 | Settled | Map: derivedFrom / derivedBy |
| [[README_MISSING Endpoint]] | [[README_MISSING Endpoint]] | 4 | 71 | Exception | Review — endpoint missing from t_object |
| [[README_InformationItem]] | [[EA Element - No Stereotype]] | 4 | 24 | Settled | Map: describes / describedBy |
| [[README_Issue]] | [[EA Stereotype - Physical System Variant]] | 4 | 25 | Settled | Map: affects / affectedBy |
| [[README_Object]] | [[EA Stereotype - requirement]] | 4 | 26 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - designConstraint]] | [[EA Stereotype - System State]] | 4 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - requirement]] | [[README_Text]] | 4 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Stereotype - System State]] | 4 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - requirement]] | [[EA Stereotype - designConstraint]] | 4 | 64 | Review | Review: verify endpoint pattern |
| [[EA Stereotype - Hardware Function]] | [[EA Stereotype - System Function]] | 3 | 27 | Settled | Map: dependsOn / dependencyOf |
| [[EA Stereotype - requirement]] | [[README_Change]] | 3 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - requirement]] | [[EA Stereotype - Hardware Component]] | 3 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Stereotype - Physical Component]] | 3 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - designConstraint]] | 3 | 68 | Review | Review: RAAML RecoveryRequirement |
| [[EA Element - No Stereotype]] | [[EA Stereotype - requirement]] | 3 | 68 | Review | Review: RAAML RecoveryRequirement |
| [[EA Stereotype - System State]] | [[EA Stereotype - requirement]] | 3 | 68 | Review | Review: RAAML RecoveryRequirement |
| [[EA Element - No Stereotype]] | [[EA Stereotype - requirement]] | 3 | 23 | Settled | Map: derivedFrom / derivedBy |
| [[EA Stereotype - designConstraint]] | [[EA Stereotype - Document]] | 3 | 57 | Review | Review: deriveReqt non-Requirement endpoint |
| [[EA Stereotype - functionalRequirement]] | [[EA Stereotype - extendedRequirement]] | 3 | 23 | Settled | Map: derivedFrom / derivedBy |
| [[EA Stereotype - performanceRequirement]] | [[EA Stereotype - requirement]] | 3 | 23 | Settled | Map: derivedFrom / derivedBy |
| [[README_InformationItem]] | [[EA Stereotype - System State]] | 3 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| [[EA Stereotype - requirement]] | [[EA Stereotype - designConstraint]] | 3 | 22 | Settled | Map: refines / refinedBy |
| [[EA Stereotype - Hardware Function]] | [[EA Element - No Stereotype]] | 3 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Stereotype - System Function]] | [[EA Stereotype - extendedRequirement]] | 3 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Element - No Stereotype]] | [[EA Stereotype - functionalRequirement]] | 3 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| [[README_InformationItem]] | [[EA Stereotype - Hardware Function]] | 3 | 24 | Settled | Map: describes / describedBy |
| [[README_InformationItem]] | [[README_InformationItem]] | 3 | 24 | Settled | Map: describes / describedBy |
| [[README_InformationItem]] | [[README_Object]] | 3 | 24 | Settled | Map: describes / describedBy |
| [[README_Issue]] | [[README_InformationItem]] | 3 | 25 | Settled | Map: affects / affectedBy |
| [[EA Element - No Stereotype]] | [[EA Stereotype - requirement]] | 3 | 50 | Review | Review: trace endpoint pattern |
| [[README_Action]] | [[EA Stereotype - Hardware Component]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Platform]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - System Partner]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Element - No Stereotype]] | [[README_Text]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - Hardware Function]] | [[EA Element - No Stereotype]] | 2 | 27 | Settled | Map: dependsOn / dependencyOf |
| [[EA Stereotype - Module Function]] | [[EA Stereotype - System Function]] | 2 | 27 | Settled | Map: dependsOn / dependencyOf |
| [[EA Stereotype - Software Function]] | [[EA Stereotype - System Function]] | 2 | 27 | Settled | Map: dependsOn / dependencyOf |
| [[EA Stereotype - Software Function]] | [[EA Stereotype - System State]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| [[README_Change]] | [[EA Element - No Stereotype]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - System Partner]] | [[EA Stereotype - requirement]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - block]] | [[EA Stereotype - Software Component]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - block]] | [[EA Stereotype - block]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - designConstraint]] | [[EA Stereotype - Document]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - functionalRequirement]] | [[EA Stereotype - Hardware Component]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - functionalRequirement]] | [[EA Stereotype - designConstraint]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - requirement]] | [[EA Stereotype - System State]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Element - No Stereotype]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Physical Component]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - requirement]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Stereotype - Hardware Component]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Element - No Stereotype]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| [[README_UseCase]] | [[README_Issue]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| [[README_UseCase]] | [[EA Stereotype - System State]] | 2 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - designConstraint]] | [[EA Stereotype - functionalRequirement]] | 2 | 23 | Settled | Map: derivedFrom / derivedBy |
| [[EA Stereotype - requirement]] | [[EA Stereotype - Regulatory Requirement]] | 2 | 23 | Settled | Map: derivedFrom / derivedBy |
| [[EA Stereotype - requirement]] | [[EA Stereotype - extendedRequirement]] | 2 | 23 | Settled | Map: derivedFrom / derivedBy |
| [[EA Stereotype - Document]] | [[EA Stereotype - designConstraint]] | 2 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| [[README_InformationItem]] | [[README_Action]] | 2 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| [[README_InformationItem]] | [[EA Stereotype - Hardware Function]] | 2 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| [[README_InformationItem]] | [[EA Stereotype - System Function]] | 2 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| [[README_InformationItem]] | [[EA Stereotype - designConstraint]] | 2 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| [[EA Stereotype - designConstraint]] | [[EA Stereotype - physicalRequirement]] | 2 | 22 | Settled | Map: refines / refinedBy |
| [[EA Stereotype - Hardware Function]] | [[EA Stereotype - Functional]] | 2 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Stereotype - Hardware Function]] | [[EA Stereotype - designConstraint]] | 2 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Stereotype - Software Function]] | [[EA Stereotype - designConstraint]] | 2 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Stereotype - requirement]] | [[EA Stereotype - requirement]] | 2 | 54 | Review | Review: satisfy endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Stereotype - Regulatory Requirement]] | 2 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| [[EA Stereotype - System State]] | [[EA Stereotype - System State]] | 2 | 54 | Review | Review: satisfy endpoint pattern |
| [[EA Element - No Stereotype]] | [[README_UseCase]] | 2 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - System Function]] | [[EA Stereotype - System Function]] | 2 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - testCase]] | [[README_Text]] | 2 | 50 | Review | Review: trace endpoint pattern |
| [[README_Change]] | [[README_Issue]] | 2 | 50 | Review | Review: trace endpoint pattern |
| [[README_Change]] | [[README_Object]] | 2 | 50 | Review | Review: trace endpoint pattern |
| [[README_Change]] | [[README_UseCase]] | 2 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - Hardware Component]] | [[EA Stereotype - Module]] | 2 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - Hardware Component]] | [[EA Stereotype - requirement]] | 2 | 26 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Module]] | [[EA Stereotype - Physical Component]] | 2 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - Physical Component]] | [[EA Stereotype - requirement]] | 2 | 26 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Physical System Variant]] | [[EA Stereotype - requirement]] | 2 | 26 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - block]] | [[EA Stereotype - Hardware Component]] | 2 | 50 | Review | Review: trace endpoint pattern |
| [[README_InformationItem]] | [[EA Stereotype - System Function]] | 2 | 24 | Settled | Map: describes / describedBy |
| [[README_InformationItem]] | [[EA Stereotype - Physical Component]] | 2 | 24 | Settled | Map: describes / describedBy |
| [[README_InformationItem]] | [[EA Stereotype - Physical Component + block]] | 2 | 24 | Settled | Map: describes / describedBy |
| [[README_InformationItem]] | [[EA Stereotype - System State]] | 2 | 24 | Settled | Map: describes / describedBy |
| [[README_Issue]] | [[EA Stereotype - Software Function]] | 2 | 25 | Settled | Map: affects / affectedBy |
| [[README_Issue]] | [[EA Stereotype - testCase]] | 2 | 25 | Settled | Map: affects / affectedBy |
| [[README_Issue]] | [[EA Stereotype - Hardware Component]] | 2 | 25 | Settled | Map: affects / affectedBy |
| [[README_Object]] | [[EA Stereotype - Image]] | 2 | 50 | Review | Review: trace endpoint pattern |
| [[README_Object]] | [[EA Element - No Stereotype]] | 2 | 26 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - designConstraint]] | [[EA Stereotype - Hardware Component]] | 2 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - designConstraint]] | [[EA Stereotype - System Partner]] | 2 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - extendedRequirement]] | [[EA Stereotype - extendedRequirement]] | 2 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - extendedRequirement]] | [[EA Stereotype - requirement]] | 2 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Stereotype - Image]] | 2 | 50 | Review | Review: trace endpoint pattern |
| [[README_UseCase]] | [[EA Stereotype - Module Function]] | 2 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - requirement]] | [[EA Stereotype - functionalRequirement]] | 2 | 64 | Review | Review: verify endpoint pattern |
| [[README_Action]] | [[EA Stereotype - Physical Component]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Software Function]] | 1 | 27 | Settled | Map: dependsOn / dependencyOf |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Hardware Component]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Element - No Stereotype]] | [[README_Issue]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Element - No Stereotype]] | [[README_Object]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - designConstraint]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - requirement]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - Software Function]] | [[EA Element - No Stereotype]] | 1 | 27 | Settled | Map: dependsOn / dependencyOf |
| [[EA Stereotype - Software Function]] | [[EA Stereotype - Hardware Function]] | 1 | 27 | Settled | Map: dependsOn / dependencyOf |
| [[EA Stereotype - Software Function]] | [[EA Stereotype - Software Function]] | 1 | 27 | Settled | Map: dependsOn / dependencyOf |
| [[EA Stereotype - System Function]] | [[EA Stereotype - Module Function]] | 1 | 27 | Settled | Map: dependsOn / dependencyOf |
| [[EA Stereotype - System Function]] | [[EA Stereotype - Software Function]] | 1 | 27 | Settled | Map: dependsOn / dependencyOf |
| [[EA Stereotype - System Function]] | [[EA Stereotype - Physical System Variant]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - System Function]] | [[EA Stereotype - Software Component]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - System Function]] | [[EA Stereotype - requirement]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - testCase]] | [[EA Stereotype - Image]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - testCase]] | [[README_InformationItem]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - Data Interface]] | [[EA Stereotype - Hardware Component]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - Hardware Component]] | [[README_Text]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - Physical System Variant]] | [[EA Element - No Stereotype]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - Physical System Variant]] | [[EA Stereotype - Hardware Function]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - Physical System Variant]] | [[EA Stereotype - Physical Component]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - System Partner]] | [[EA Stereotype - System Partner]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[README_Issue]] | [[EA Stereotype - testCase]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[README_Issue]] | [[EA Stereotype - requirement]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Element - No Stereotype]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Element - No Stereotype]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - Regulatory Requirement]] | [[EA Element - No Stereotype]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - designConstraint]] | [[EA Stereotype - designConstraint]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - designConstraint]] | [[EA Stereotype - requirement]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - designConstraint]] | [[EA Stereotype - System State]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - extendedRequirement]] | [[EA Stereotype - extendedRequirement]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - functionalRequirement]] | [[EA Stereotype - functionalRequirement]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - requirement]] | [[EA Element - No Stereotype]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - requirement]] | [[EA Stereotype - System Function]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - requirement]] | [[EA Stereotype - Physical System Variant]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - requirement]] | [[EA Stereotype - block]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - requirement]] | [[README_Text]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - System Function]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - designConstraint]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - System State]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Element - No Stereotype]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Stereotype - Module]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Stereotype - requirement]] | 1 | 58 | Review | Review: Dependency endpoint pattern |
| [[README_UseCase]] | [[README_UseCase]] | 1 | 27 | Settled | Map: dependsOn / dependencyOf |
| [[EA Stereotype - System Function]] | [[EA Stereotype - requirement]] | 1 | 68 | Review | Review: RAAML RecoveryRequirement |
| [[EA Stereotype - System Function]] | [[EA Element - No Stereotype]] | 1 | 57 | Review | Review: deriveReqt non-Requirement endpoint |
| [[EA Stereotype - Regulatory Requirement]] | [[EA Stereotype - requirement]] | 1 | 23 | Settled | Map: derivedFrom / derivedBy |
| [[EA Stereotype - designConstraint]] | [[README_InformationItem]] | 1 | 57 | Review | Review: deriveReqt non-Requirement endpoint |
| [[EA Stereotype - functionalRequirement]] | [[EA Stereotype - Regulatory Requirement]] | 1 | 23 | Settled | Map: derivedFrom / derivedBy |
| [[EA Stereotype - requirement]] | [[EA Stereotype - functionalRequirement]] | 1 | 23 | Settled | Map: derivedFrom / derivedBy |
| [[EA Stereotype - System State]] | [[EA Element - No Stereotype]] | 1 | 57 | Review | Review: deriveReqt non-Requirement endpoint |
| [[EA Stereotype - Document]] | [[EA Stereotype - functionalRequirement]] | 1 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| [[README_InformationItem]] | [[EA Stereotype - Module]] | 1 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| [[README_InformationItem]] | [[EA Stereotype - Software Component]] | 1 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| [[README_InformationItem]] | [[EA Stereotype - extendedRequirement]] | 1 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| [[EA Stereotype - designConstraint]] | [[EA Stereotype - functionalRequirement]] | 1 | 22 | Settled | Map: refines / refinedBy |
| [[EA Stereotype - requirement]] | [[EA Stereotype - System State]] | 1 | 65 | Settled | Map: describes / describedBy (non-Requirement refinement) |
| [[README_UseCase]] | [[EA Stereotype - extendedRequirement]] | 1 | 20 | Settled | Map: describes / describedBy |
| [[README_Action]] | [[EA Element - No Stereotype]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - extendedRequirement]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| [[EA Stereotype - Module Function]] | [[EA Stereotype - System Function]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| [[EA Stereotype - System Function]] | [[EA Stereotype - System Function]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| [[EA Stereotype - Document]] | [[EA Stereotype - extendedRequirement]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| [[EA Stereotype - Hardware Component]] | [[EA Element - No Stereotype]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| [[EA Stereotype - Hardware Component]] | [[EA Stereotype - extendedRequirement]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| [[EA Stereotype - Physical Component]] | [[EA Stereotype - requirement]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| [[EA Stereotype - designConstraint]] | [[EA Element - No Stereotype]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| [[EA Stereotype - designConstraint]] | [[EA Stereotype - requirement]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| [[EA Stereotype - designConstraint]] | [[EA Element - No Stereotype]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Webasto Requirement]] | 1 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| [[EA Stereotype - System State]] | [[EA Stereotype - Document]] | 1 | 54 | Review | Review: satisfy endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Stereotype - Webasto Requirement]] | 1 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| [[EA Stereotype - System State]] | [[EA Stereotype - performanceRequirement]] | 1 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| [[README_Action]] | [[EA Stereotype - Image]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Image]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Element - No Stereotype]] | [[README_Text]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - Hardware Function]] | [[README_InformationItem]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - Hardware Function]] | [[EA Stereotype - System State]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - Software Function]] | [[EA Element - No Stereotype]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - System Function]] | [[README_InformationItem]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - System Function]] | [[EA Stereotype - requirement]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - testCase]] | [[README_Change]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[README_Actor]] | [[README_InformationItem]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - Image]] | [[README_InformationItem]] | 1 | 24 | Settled | Map: describes / describedBy |
| [[README_Boundary]] | [[EA Element - No Stereotype]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[README_Boundary]] | [[EA Stereotype - Module]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[README_Change]] | [[README_InformationItem]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - Business Line]] | [[EA Stereotype - requirement]] | 1 | 26 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Hardware Component]] | [[EA Stereotype - Hardware Component]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - Hardware Component]] | [[EA Stereotype - functionalRequirement]] | 1 | 26 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Module]] | [[README_InformationItem]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - Physical Component]] | [[EA Stereotype - Image]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - Physical Component]] | [[README_Text]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - Physical System Variant]] | [[EA Stereotype - designConstraint]] | 1 | 26 | Settled | Map: Requirement appliesTo source element |
| [[EA Stereotype - Software Component]] | [[README_Text]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[README_InformationItem]] | [[README_Actor]] | 1 | 24 | Settled | Map: describes / describedBy |
| [[README_InformationItem]] | [[EA Stereotype - Platform]] | 1 | 24 | Settled | Map: describes / describedBy |
| [[README_InformationItem]] | [[EA Stereotype - block]] | 1 | 24 | Settled | Map: describes / describedBy |
| [[README_InformationItem]] | [[README_Text]] | 1 | 24 | Settled | Map: describes / describedBy |
| [[README_Issue]] | [[EA Element - No Stereotype]] | 1 | 25 | Settled | Map: affects / affectedBy |
| [[README_Issue]] | [[EA Stereotype - System Function]] | 1 | 25 | Settled | Map: affects / affectedBy |
| [[README_Issue]] | [[EA Stereotype - System Partner]] | 1 | 25 | Settled | Map: affects / affectedBy |
| [[README_ProxyConnector]] | [[README_Issue]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Element - No Stereotype]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Element - No Stereotype]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - Regulatory Requirement]] | [[EA Stereotype - requirement]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - designConstraint]] | [[EA Stereotype - Physical Component]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - designConstraint]] | [[EA Stereotype - Software Component]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - designConstraint]] | [[EA Stereotype - designConstraint]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - extendedRequirement]] | [[EA Stereotype - Webasto Requirement]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - functionalRequirement]] | [[EA Stereotype - System Function]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - functionalRequirement]] | [[EA Stereotype - System Partner]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - functionalRequirement]] | [[EA Element - No Stereotype]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - requirement]] | [[EA Stereotype - Hardware Component]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - Hardware Function]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Element - No Stereotype]] | [[EA Stereotype - System State]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Stereotype - Document]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Stereotype - Physical Component]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Stereotype - Physical System Variant]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Stereotype - designConstraint]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Stereotype - functionalRequirement]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[README_Text]] | [[EA Stereotype - Hardware Component]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[README_Text]] | [[EA Stereotype - System Partner]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[README_Text]] | [[README_Object]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[README_UseCase]] | [[EA Element - No Stereotype]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[README_UseCase]] | [[EA Stereotype - requirement]] | 1 | 50 | Review | Review: trace endpoint pattern |
| [[EA Stereotype - testCase]] | [[EA Stereotype - Hardware Function]] | 1 | 64 | Review | Review: verify endpoint pattern |
| [[EA Stereotype - testCase]] | [[EA Stereotype - extendedRequirement]] | 1 | 63 | Settled | Map: verifies / verifiedBy |
| [[EA Stereotype - requirement]] | [[EA Element - No Stereotype]] | 1 | 64 | Review | Review: verify endpoint pattern |

## Canvas

[[CANVAS_Dependency]]
