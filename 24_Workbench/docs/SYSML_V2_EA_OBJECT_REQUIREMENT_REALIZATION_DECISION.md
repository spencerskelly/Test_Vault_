# Approved EA Object-to-Requirement Realization Translation
Date: 2026-10-17
Status: APPROVED translation decision; implementation and conformance verification pending.

## Rule
For existing EA Realization connectors between an Object and a Requirement, where the Object provides an implementation path toward that Requirement:
- Translate to a native SysML v2 AllocationUsage, with **Requirement as source** and **Object as target**.
- Detect the roles by the mapped endpoint element types, rather than assuming the EA arrow direction.
- Preserve original EA connector direction, source and target GUIDs, connector GUID, type/stereotype, notes, tagged values and import rule version in provenance.
- This is an allocation of implementation responsibility / potential solution path. **It does not assert that the object satisfies the requirement**.
- Native SatisfyRequirementUsage is a separate explicit engineering assertion; VerificationCase and verify relationships are likewise separate.
- Do not globally map other EA Realization variants to Allocation: object-to-object and other endpoint combinations require separate semantic classification.
- If actual endpoints or semantics conflict, account for the EA connector and flag a clear exception; do not invent native model assertions.

## EA Translator
- Add ordered rule predicate: EA Realization + one mapped Requirement + one mapped Object -> requirement-to-object allocation.
- Preserve complete original connector evidence and distinguish this rule from Activity/Object or State/Object allocation mappings.
- Resolve ownership/context of requirement and object usages and validate that the emitted AllocationUsage is native and legal.
- Track target allocation ID, disposition, rule version and exception flag in source-to-target reconciliation ledger.
- Reimport must remain deterministic and idempotent.

## BOM Translator
- Reuse canonical object/part identity. BOM rows cannot themselves imply requirement allocation or satisfaction.
- Preserve existing requirement allocations through BOM update, revision, variant and quantity changes.
- Flag part identity mismatches without breaking existing provenance.

## Workbench
- Draw between Object and Requirement in either gesture direction; offer Allocation (responsibility mapping) only when valid, with preview showing **Requirement -> Object**.
- Give engineer access to relationship Definitions without leaving view; compare Allocation vs Satisfaction vs Dependency vs Realization (EA source classification).
- Requirement Coverage view: responsible objects, supporting actions, separately asserted Satisfaction and Verification, and outstanding exceptions; no implied satisfaction from allocation.
- Relationship type filters and saved custom views apply to presentation, not canonical model.
- Creation/removal/edit must preserve model integrity, stable IDs, undo/redo, reverse navigation and evidence.

## Vault definitions
- Add explicit definition note for native AllocationUsage, its requirement-to-object application, and distinction from Satisfaction.
- Preserve source EA Realization in provenance/exception metadata, not as a fabricated SysML v2 relationship.
- Link standardized help panel registry to this rule and examples.

## Validation
1. EA object->requirement Realization produces native requirement->object Allocation.
2. EA connector drawn backwards still produces correct semantic mapping while provenance retains direction.
3. Distinct Satisfaction assertions are never auto-created.
4. A requirement with multiple candidate objects yields independent allocations, not inferred satisfaction.
5. Unsupported Realization cases stay in mapping audit and review queue.
6. EA + BOM import permutations preserve object identity and allocation.
7. Workbench draw-to-relate shows valid options, explicit preview, and definitions.
8. Native v2 parser/semantic conformance and round-trip checks pass.
9. Complete source row accounting including exceptions.

## Follow-ups
REAL-01 Inventory all EA Realization connectors by mapped endpoint type and source direction.
REAL-02 Implement rule priority and stable, typed allocation generation.
REAL-03 Add source provenance/exception ledger and migration coverage tests.
REAL-04 Integrate Requirement Coverage and in-editor comparison reference.
REAL-05 Confirm native allocation legality and exact syntax in official v2 tooling.
REAL-06 Ensure BOM merge does not invent or delete allocations.
REAL-07 Review remaining Object->Object and other Realization patterns individually.

## Next relationship review
EA Realization with Object-to-Object endpoints; distinguish logical-to-physical mapping, type implementation, architectural responsibility or unsupported legacy realization semantics before adopting a default.
