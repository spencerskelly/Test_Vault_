# Approved: Referential Part Usage
Date: 2026-10-16
Status: APPROVED

## Rule
Use native SysML v2 `ref part` for a part usage referring to a part occurrence that is NOT compositionally owned by the containing assembly. Use ordinary composite `part` for an owned occurrence. Multiple assemblies using the same `part def` do NOT automatically require `ref part`; they can each own their own usage.

## Import and migration
Map genuine non-owning EA/SysML v1 part references to referential usages, with semantic check where EA connectors are ambiguous. EA remains import source only, not perpetual authority; validated SysML v2 syntax in the owning Obsidian note is the model source of truth.

## Workbench
- Structural tree: composite usages under owning assembly; referential usages marked as non-owning links, not extra owned children.
- Diagram: visibly distinguish non-owning references from owned part compartments; selecting references navigates to related occurrence and definition.
- Editor: insert/remove/change `part` or `ref part` by patching authoritative note syntax and refreshing both structural and diagram views.
- BOM: only composite owned usages contribute as constituents; referential usages do not count as separate newly owned parts.
- Both usage kinds can reuse same single canonical definition; usage notes are optional, not required.
- Validate target type and reference target resolution where context requires a particular occurrence.

## Next topic
Requirement relationship semantics: allocation, satisfaction, and verification should not be conflated. Determine native SysML v2 constructs and Workbench representations before approving mapping.
