# Native SysML v2 Subsetting — supported, not currently mapped
Date: 2026-10-16
Status: ACCEPTED AS SUPPORTED CAPABILITY; NOT CONFIRMED IN CURRENT EA MODEL

## Semantics
Feature subsetting means all values of a subsetted feature are also values of the broader feature. It does not create new occurrences, a new type, or ordinary part containment. Example: two priority modules selected from four existing charger modules.

## Project decision
- Support native SysML v2 subsetting in the canonical note-based model and Workbench.
- User does not recall explicitly modeling subsetting in current EA source. Do not invent subsets or infer them from aggregation, generalization, or names during migration.
- Discovery/audit may identify possible candidates, but those require user review before conversion.
- Preserve distinct meanings for specialization, typing, containment, redefinition, and subsetting.

## Workbench
- Structural view: show subset usage and the broader feature; do not imply the subset is an additional BOM constituent.
- Visual view: distinct subset relationship; show members as a subset, not another composite assembly.
- Editing from text/tree/diagram updates authoritative SysML v2 syntax in the owning note; all other views refresh.
- Validate compatible features and subset constraints, cardinality and reference resolution.
- Do not require separate notes for usages; canonical definitions shared across types.

## Next native relationship
Feature redefinition: refining or replacing an inherited feature within a specialized definition. Review formal meaning, scope and difference from subsetting before approval.
