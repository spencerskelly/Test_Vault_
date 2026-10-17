# APPROVED — EA Copy Alias Consolidation and Relationship Merge
Date: 2026-10-16
Status: APPROVED; extends and takes precedence over 2026-10-16-ea-copy-to-alias-membership-approved.md

## Rule
EA Copy links identify aliases of the same conceptual model element. For each connected equivalence group of Copy-related EA elements, import ONE canonical SysML v2 definition and ONE canonical definition note. Represent the other names as native SysML v2 alias memberships in their proper namespaces as needed, rather than creating separate definition notes. Consolidate ALL relationships that were attached to ANY copied EA element onto the canonical model element, while preserving each relationship's meaning and direction. This is the project-specific EA-to-v2 translation policy.

## Deterministic migration
1. Build alias-equivalence groups from EA Copy edges (including chained copies). Only Copy edges act as alias-union signals. Do not infer identity from coincident names or shared types.
2. Choose one canonical EA element per group deterministically (explicit origin if available; otherwise stable documented tie-break). Map every group member GUID to canonical model identity during import. Prefer original name as canonical if reliably identified; other names become aliases.
3. Merge notes, documentation and non-conflicting properties into canonical definition; surface conflicts for review without destructive overwrite.
4. Rewrite endpoints of all non-Copy relationships through GUID→canonical identity map, maintaining source/target direction, relationship type, owning context, role names, multiplicity and property references.
5. Retain distinct semantic relationships even when rewritten endpoints coincide: deduplicate only genuinely equivalent edges with same kind, endpoints, context, roles and relevant attributes; do not drop meaningful parallel edges.
6. Copy edges become alias declarations and need not remain as general dependency or connection edges. If alias members have different names/namespaces, generate native alias membership declarations and import/qualification as needed.
7. If rewriting creates a self-reference, invalid classifier relation, ownership collision, definition-type disagreement, or inconsistent port/feature path, flag and repair explicitly before compliant SysML v2 export; do not silently delete it or fabricate semantics.
8. Remove redundant copied element notes after consolidation, once all endpoints and references are resolved. No long-term obligation to retain original EA links after successful migration.
9. Store usages in owning notes. Do not collapse distinct part usages/occurrences simply because their reusable definitions share an alias.
10. Verify relationship and information coverage with before/after semantic counts and issue report; source records may be discarded after clean migration.

## Workbench
- One canonical note/definition and its aliases in search and structural inspector; alias names navigate to same definition.
- All incoming and outgoing relationships from the copied EA elements appear on the canonical definition, retaining directions and types.
- Diagram views referencing any alias resolve to same model element, optionally displaying the alias appropriate for context, never a duplicate semantic node.
- Editing relationship from any view patches canonical SysML v2 syntax in owning note(s) and updates other projections.
- If merged relationships conflict, expose review findings and keep valid ones; source alias diagram nodes may be visually distinct presentations only, not distinct semantic definitions.
- Tests: chained Copy A↔B↔C, mixed incoming/outgoing edges, name collisions, duplicate edges, self-edge, usage versus definition, cycles, package namespaces, diagrams and cross-note links.

## Exact boundary
This policy is specifically the user's EA model meaning for a relationship named Copy. EA application's Copy/Paste-As-New action is NOT assumed to be equivalent to alias, and different legitimate occurrences/usages of a type are NOT merged by this rule.
