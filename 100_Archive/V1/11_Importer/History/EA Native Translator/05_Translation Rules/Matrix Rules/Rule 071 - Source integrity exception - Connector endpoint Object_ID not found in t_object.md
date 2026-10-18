---
uid:
type: Translation Rule
status: "Review / Exception"
matrixRuleId: 71
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 71 — Source integrity exception — Connector endpoint Object_ID not found in t_object

## Source pattern

- **EA Connector:** Source integrity exception
- **EA Stereotype / Pattern:** Connector endpoint Object_ID not found in t_object
- **Source Endpoint Semantics:** Missing endpoint
- **Target Endpoint Semantics:** Missing endpoint

## MDSE relationship

- **Source YAML Relationship:** none
- **Target YAML Inverse:** none

## Transformation rule

Do not silently drop. Emit import exception with Connector_ID, ea_guid, raw type/stereotype, and missing Object_ID values.

## Body detail rule

Preserve full raw connector record in traceability output.

## Status

Review / Exception

## Review trigger

Any Start_Object_ID or End_Object_ID cannot be resolved

## Source basis / notes

9 observed connector rows use Object_ID 0 / missing endpoints.
