---
uid:
type: Translation Decision
status: Working
decisionArea: "Requirement Relationship Mapping"
---
# Requirement Relationship Mapping

## Purpose

Provide a Requirement-centered view of approved and unresolved connector translations.

## Settled mappings

| EA source pattern | Matrix Rule | MDSE result |
|---|---:|---|
| Function → `satisfy` → Requirement | [[Rule 015 - satisfy - Function → Functional Requirement]] | Function `satisfies` Requirement |
| Design → `satisfy` → Requirement | [[Rule 016 - satisfy - Design → Design Constraint]] | Design `satisfies` Requirement |
| State / State Machine → `satisfy` → Requirement | [[Rule 017 - satisfy - State - State Machine → requirement]] | Requirement `appliesTo` State / State Machine |
| semantic element → Realisation → Requirement | [[Rule 018 - Realisation - Requirement applicability]] | Requirement `appliesTo` element |
| Requirement → `refine` → Requirement | [[Rule 022 - refine - Requirement → Requirement]] | `refines / refinedBy` |
| Requirement → `deriveReqt` → Requirement | [[Rule 023 - deriveReqt - Requirement → Requirement]] | `derivedFrom / derivedBy` |
| testCase → `verify` → Requirement | [[Rule 063 - Dependency - verify — testCase → Requirement]] | Test `verifies` Requirement |
| Info → `trace` → Requirement | [[Rule 024 - trace - Info → element]] | Info `describes` Requirement |
| Issue → `trace` → Requirement | [[Rule 025 - trace - Issue → element]] | Issue `affects` Requirement |
| Object → `trace` → Requirement | [[Rule 026 - trace - Object → Requirement]] | Requirement `appliesTo` Object |

## Review / deferred families

- Generic Dependency involving Requirement
- Generic `trace` patterns not matching a settled endpoint rule
- Nonstandard `verify` patterns
- `allocate` involving Requirement
- RAAML `RecoveryRequirement`
- RAAML `ASILDecompose`
- Explicit Nesting
- Requirement-originating Realisation where applicability semantics do not match
- Non-Requirement `deriveReqt` endpoints

## Rule

A connector name alone never authorizes a semantic MDSE relationship when the endpoint pattern does not match an approved rule.
