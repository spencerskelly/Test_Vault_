---
uid:
type: Translation Verification
status: Working
decisionArea: "Requirement Verification"
---
# Requirement Verification Cases

## Purpose

Define translator fixtures that prove the Requirement rules are implemented correctly.

## Core fixtures

### RV-REQ-001 — Functional requirement classification

**Input**

EA Requirement with stereotype `functionalRequirement`.

**Expected output**

```yaml
type: Requirement
requirementType: Functional
eaStereotype: functionalRequirement
```

### RV-REQ-002 — Generic requirement preservation

**Input**

EA Requirement with stereotype `requirement`.

**Expected output**

```yaml
type: Requirement
requirementType:
eaStereotype: requirement
```

No functional/design classification may be inferred from the stereotype alone.

### RV-REQ-003 — Function satisfaction

**Input**

EA Function-like source element with `satisfy` to Requirement, matching Matrix Rule 15.

**Expected output**

Function `satisfies` Requirement.

### RV-REQ-004 — State satisfaction normalization

**Input**

EA State with `satisfy` to Requirement, matching Matrix Rule 17.

**Expected output**

Requirement `appliesTo` State.

State must not directly satisfy the Requirement.

### RV-REQ-005 — Requirement derivation

**Input**

EA Requirement → `deriveReqt` → Requirement.

**Expected output**

Derived Requirement `derivedFrom` source Requirement.

### RV-REQ-006 — testCase verification

**Input**

EA Activity «testCase» → Dependency «verify» → Requirement.

**Expected output**

Test `verifies` Requirement.

### RV-REQ-007 — unsupported satisfy endpoint

**Input**

EA source pattern that uses `satisfy` but does not match an approved endpoint rule.

**Expected output**

No invented MDSE satisfaction relationship. Create review/migration evidence according to the current matrix disposition.
