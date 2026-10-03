---
uid:
type: Translation Verification
status: Working
decisionState: Working
decisionOwner: Human
implementationState: Partial
verificationState: Fixture Defined
lastReviewed: 2026-09-27
decisionArea: "Requirement Verification"
---
# Requirement Verification Cases

## RV-REQ-001 — Functional requirement subtype

**Input:** EA Requirement with stereotype `functionalRequirement`.

**Expected output**

```yaml
type: Requirement
subtype: functional
eaStereotype: functionalRequirement
```

## RV-REQ-002 — Generic requirement preservation

**Input:** EA Requirement with stereotype `requirement`.

**Expected output**

```yaml
type: Requirement
subtype:
eaStereotype: requirement
```

No subtype is inferred from the generic stereotype alone.

## RV-REQ-003 — Function satisfaction

Function-like source element with approved `satisfy` pattern → Function `satisfies` Requirement.

## RV-REQ-004 — State satisfaction normalization

EA State with `satisfy` → Requirement `appliesTo` State. State does not directly satisfy Requirement.

## RV-REQ-005 — Requirement derivation

Requirement → `deriveReqt` → Requirement becomes `derivedFrom / derivedBy`.

## RV-REQ-006 — testCase verification

Activity «testCase» → Dependency «verify» → Requirement becomes Test `verifies` Requirement.

## RV-REQ-007 — unsupported satisfy endpoint

No invented MDSE satisfaction relationship; preserve/review according to the matrix disposition.
