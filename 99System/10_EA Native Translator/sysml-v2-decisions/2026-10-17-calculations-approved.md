# APPROVED — SysML v2 Calculation Definitions and Usages
Date: 2026-10-17
Status: APPROVED — review #23

## Meaning
A calculation computes result value(s) from inputs using an expression or calculation behavior. It is distinct from a Boolean constraint, a required assertion, and an executed verification test. Reusable Calculation Definitions describe the computation; Calculation Usages apply it in particular model contexts.

## Native support
- Support native SysML v2 Calculation Definitions and Calculation Usages, typed inputs, return/result features, references to model attributes, and contextual reusable usages.
- Distinguish calculation expressions from constraints and binding relationships, while supporting native feature paths and applicable parameter bindings.
- Validate generated concrete textual syntax against the official SysML v2 grammar/parser before production release; do not treat illustrative snippets as a grammar oracle.

## EA import
- Import only explicit, semantically compatible EA calculation definitions/usages or mathematical formulas where endpoints, input/output values, and ownership can be resolved.
- Do not turn descriptive prose, raw notes, or guessed formulas into calculations.
- Flag ambiguous/unresolved numeric data, type/unit mismatches, or formula dependencies for review; preserve semantics rather than inventing missing calculations.

## Workbench
- Structural: calculation definition, its usages, owner, typed input parameters, output/result, expression and references to attributes.
- Visual: distinct input → calculation → result representation, with navigable value sources. Visual arrows represent value dependencies/parameter connections, not automatically physical connections or flows.
- Inspector/editing: formulas, references, parameter typing, units, and result features; edits to any view patch the authoritative SysML v2 syntax in the owning Obsidian note and synchronize all projections.
- Validation: resolvable symbols, correct input/output types, dimensions/units if known, return compatibility, unsupported operations, and calculation cycles when relevant.
- One canonical reusable definition per type; multiple contextual usages; no mandatory separate note per usage.
- Calculation execution/evaluation is optional functionality and must be distinguished from model syntax; do not claim verified numeric outputs absent computation.

## Example
A charger output-power calculation consumes voltage and current and yields power. A separate constraint may check power against a limit. No automatic requirement, constraint assertion, verification result, or physical connection is implied.

## Next review
Attributes, value types and units/quantity kinds: native definitions/usages and unit-aware value modeling.
