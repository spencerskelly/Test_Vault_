---
uid:
type: EA Relationship
status: Working
eaConnectorType: "Dependency"
eaConnectorStereotype: "satisfy"
eaProfile: "SysML1.4::satisfy"
connectorCount: 2444
inventoryBasis: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# EA Dependency — satisfy

## Source identity

- **Connector_Type:** `Dependency`
- **Effective stereotype:** `satisfy`
- **Profile / FQName:** `SysML1.4::satisfy`
- **Observed connectors:** 2444

## Inventory coverage

- **Unique endpoint combinations:** 49
- **Matrix Rule IDs:** `15, 17, 54, 71`
- **Disposition distribution:** Review 733; Settled 659; Deferred 1048; Exception 4
- **Coverage:** Complete — every observed endpoint combination has a disposition

## Observed endpoint combinations

| Source endpoint | Target endpoint | Count | Matrix rule | Coverage | Import disposition |
|---|---|---:|---|---|---|
| [[EA Stereotype - System State]] | [[EA Stereotype - requirement]] | 364 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| [[EA Stereotype - System State]] | [[EA Stereotype - designConstraint]] | 340 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| [[EA Element - No Stereotype]] | [[EA Stereotype - requirement]] | 336 | 54 | Review | Review: satisfy endpoint pattern |
| [[EA Stereotype - System Function]] | [[EA Stereotype - functionalRequirement]] | 224 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Element - No Stereotype]] | [[EA Stereotype - functionalRequirement]] | 196 | 54 | Review | Review: satisfy endpoint pattern |
| [[EA Stereotype - System Function]] | [[EA Stereotype - requirement]] | 185 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Element - No Stereotype]] | [[EA Stereotype - requirement]] | 176 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| [[EA Element - No Stereotype]] | [[EA Element - No Stereotype]] | 160 | 54 | Review | Review: satisfy endpoint pattern |
| [[EA Stereotype - System Function]] | [[EA Element - No Stereotype]] | 88 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Element - No Stereotype]] | [[EA Stereotype - designConstraint]] | 60 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| [[EA Stereotype - System State]] | [[EA Stereotype - extendedRequirement]] | 53 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| [[EA Stereotype - Hardware Function]] | [[EA Stereotype - requirement]] | 49 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Stereotype - Hardware Function]] | [[EA Stereotype - functionalRequirement]] | 31 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Stereotype - System State]] | [[EA Element - No Stereotype]] | 30 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| [[EA Stereotype - Software Function]] | [[EA Stereotype - requirement]] | 22 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Element - No Stereotype]] | [[EA Stereotype - designConstraint]] | 20 | 54 | Review | Review: satisfy endpoint pattern |
| [[EA Stereotype - Module Function]] | [[EA Stereotype - requirement]] | 13 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Stereotype - Software Function]] | [[EA Stereotype - functionalRequirement]] | 12 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Stereotype - System State]] | [[EA Stereotype - functionalRequirement]] | 9 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| [[EA Stereotype - Module Function]] | [[EA Stereotype - functionalRequirement]] | 8 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Stereotype - System Function]] | [[EA Stereotype - designConstraint]] | 8 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Element - No Stereotype]] | [[EA Element - No Stereotype]] | 8 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| [[EA Stereotype - Module Function]] | [[EA Element - No Stereotype]] | 7 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[README_Action]] | [[EA Stereotype - requirement]] | 5 | 54 | Review | Review: satisfy endpoint pattern |
| [[README_MISSING Endpoint]] | [[README_MISSING Endpoint]] | 4 | 71 | Exception | Review — endpoint missing from t_object |
| [[EA Stereotype - Hardware Function]] | [[EA Element - No Stereotype]] | 3 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Stereotype - System Function]] | [[EA Stereotype - extendedRequirement]] | 3 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Element - No Stereotype]] | [[EA Stereotype - functionalRequirement]] | 3 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| [[EA Stereotype - Hardware Function]] | [[EA Stereotype - Functional]] | 2 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Stereotype - Hardware Function]] | [[EA Stereotype - designConstraint]] | 2 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Stereotype - Software Function]] | [[EA Stereotype - designConstraint]] | 2 | 15 | Settled | Map: satisfies / satisfiedBy |
| [[EA Stereotype - requirement]] | [[EA Stereotype - requirement]] | 2 | 54 | Review | Review: satisfy endpoint pattern |
| [[EA Stereotype - System State]] | [[EA Stereotype - Regulatory Requirement]] | 2 | 17 | Deferred | Deferred: State/StateMachine satisfaction scope |
| [[EA Stereotype - System State]] | [[EA Stereotype - System State]] | 2 | 54 | Review | Review: satisfy endpoint pattern |
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

## Canvas

[[CANVAS_Dependency - satisfy]]
