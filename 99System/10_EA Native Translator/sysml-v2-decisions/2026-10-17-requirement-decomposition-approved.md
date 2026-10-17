# APPROVED — Native SysML v2 Requirement Decomposition
Date: 2026-10-17
Status: APPROVED — Relationship #21

## Meaning
Requirement decomposition expresses subordinate requirements as nested requirement usages in a containing requirement context. These are constituent requirements/required constraints, not merely requirements derived through engineering analysis. Referenced requirement usages allow an existing requirement to participate without being compositionally owned or duplicated.

## Native project rule
- Support native nested composite requirement usages and non-owning referenced requirement usages where supported by SysML v2.
- Keep definition vs usage distinct: one canonical reusable requirement definition per distinct type, usages typically in their owners' notes without separate usage notes.
- Nested required constraints are not automatically subclasses or derivations. Keep library-based Derivation separate.
- Preserve correct requirement subjects, owning context, nested required conditions, multiplicity and identifier resolution.
- Verify exact syntax/context with conforming SysML v2 implementation before production export.

## EA migration
Map genuine EA requirement containment/aggregation to nested requirement usages only when endpoints and ownership semantics agree. Where requirements are shared across multiple contexts, prefer a referenced usage to duplicate definitions. Never turn EA `«deriveReqt»` into containment; prior derivation mapping remains intact. Flag ambiguous source containment rather than fabricating hierarchy.

## Workbench
- Structure: expandable requirement hierarchy showing composite children and distinctly marked non-owning referenced requirements; navigate to canonical definitions and where-used.
- Visual: nested requirement boxes/expandable hierarchy and distinguish reference from owned child; do not draw fake derivation/inheritance edges.
- Drag/drop: explicit choice of move as owned child vs add non-owning reference, with previews of effects on subjects and constraints.
- Inspector: parent, nested requirement usage, whether composite/referential, inherited constraints (if any), native qualified identity and validation.
- Every change in textual, structural or visual view patches native SysML v2 syntax in owning note(s); reparse and synchronize. Handle cross-note moves atomically.
- Validation: context, cycles where prohibited, references, names, required constraints, and no duplicate canonical definition.

## Teaching contrast
Decomposition: 'these are required subconditions of the parent.'
Derivation: 'engineering developed B from A'; no automatic inclusion/inheritance.
Subclassification: 'B is a kind of A.'
Satisfaction: 'a feature is asserted to meet applicable requirement.'
Reference: 'another context uses an existing requirement without owning it.'

## Next native review
Constraint definitions/usages and assertions; distinguish formulas/conditions from requirement definitions and from static attribute values.
