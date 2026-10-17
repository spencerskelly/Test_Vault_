# APPROVED — SysML v2 Attributes, ValueTypes, Quantities and Units
Date: 2026-10-17
Status: APPROVED — Native construct review #24

## Plain-language meaning
An Attribute Definition describes a reusable value type; an Attribute Usage defines a value-bearing feature in a context. These are not physical part occurrences. Quantities encode physical dimensions/kinds and measurement units; do not confuse a scalar number with a physical quantity or store units only as decorative text.

## Native modeling
- Support native SysML v2 Attribute Definitions and Usages, compatible primitive and value types, quantity kinds and units from the standard libraries when applicable.
- Preserve declared type, multiplicity, defaults versus fixed values, derived/calculated value meaning, feature membership and qualified references.
- Distinguish actual measured test results from modeled/default/design values; avoid silently treating measurements as static specification.
- Validate exact syntax, standard library references, units and semantics using conforming SysML v2 tooling before production export.

## EA migration
- Import EA Attributes and compatible explicit EA ValueTypes into native attribute usages and canonical attribute definitions, respectively, where semantics fit.
- Preserve declared type, explicit units and quantity kind, original value semantics, visibility, multiplicity and owning context when available.
- Do not automatically assign units based on the attribute name, number, or typical charger practice; unresolved or incompatible unit information creates a diagnostic.
- EA Objects are governed by the previously approved default part-definition import rule; do not reinterpret every EA Object as an attribute.
- Resolve Copy aliases before canonical references; do not duplicate shared definitions.

## Workbench
- Structural view: attribute table with name, type, quantity kind, value expression, unit, multiplicity, owner, provenance, default/fixed/calculated state; links to canonical type.
- Visual view: show properties on owner features/compartments, optional typed value connections and navigable constraint/calculation inputs, not physical connections by default.
- Editing: create/change type, units, default/fixed value, multiplicity and bindings in text/tree/diagram; changes patch canonical native SysML v2 text in owning Obsidian note and synchronize projections.
- Unit-aware UI conversion may change display units while preserving underlying physical meaning; explicit edit of stored model unit must be an intentional semantic change.
- Validation: type and value compatibility, dimension checks, conversions, literal/default semantics, cycles in derived values, resolution and duplicate names.
- One canonical definition per type; context-specific usages normally remain in owner's note.

## Worked distinctions
- `attribute outputVoltage` refers to a value-bearing feature of charger; it is not a nested circuit.
- Voltage in V and mV has same quantity kind if compatible; conversion must be dimensionally correct.
- A default of 480 V is not a test measurement and not a universal fixed rating.
- A power calculation is not a constraint unless tested/asserted separately.

## Next review
Enumeration Definitions and Usages / enumerated values: native syntax and difference from states, status attributes and permitted literals.
