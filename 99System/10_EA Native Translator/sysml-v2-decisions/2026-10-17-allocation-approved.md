# APPROVED — Native SysML v2 Allocation Definitions and Usages
Date: 2026-10-17
Status: APPROVED — Relationship #17

## Plain language
Allocation assigns responsibility or maps the intent of one model feature to another feature that implements/realizes it. It is NOT a physical connection, requirement satisfaction, verification result, or blanket statement about runtime execution.

## Native semantics
Support native SysML v2 Allocation Definitions and Allocation Usages, including appropriately contextual/nested allocations, with source and target ends and valid owning context. Preserve intended source → target orientation. Validate exact native syntax and constraints against a conforming SysML v2 parser.

## EA mapping
Translate genuine EA stereotype «allocate» relations directly to native v2 allocations when endpoints/owning context resolve. Do not translate arbitrary EA Abstractions without that semantic evidence; do not invent allocations from dependency/realization links. Where converted aliases collapse duplicate definitions, remap allocation endpoints to canonical identities, preserving real distinct usages.

## Workbench structural and visual
- Structural view: show allocating source, implementing target, owner, allocation type/definition and nested allocations.
- Visual view: directional labeled allocation distinct from Connection, Binding, Dependency, Satisfaction.
- Inspector: navigate source/target, detail mapping intent, and validation state.
- Editing from any view writes authoritative SysML v2 syntax in owning Obsidian note; reparse to synchronize all projections.
- One reusable definition per type; individual allocation usages do not require separate notes.
- Validation includes endpoint references, context, native kind constraints, consistency after rename/move, and avoiding fabricated satisfaction assertions.

## Example
```sysml
action def ControlCharging;
part def SafetyController;
part def Charger {
    action controlCharging : ControlCharging;
    part controller : SafetyController;
    allocate controlCharging to controller;
}
```

## Relationship documentation
Explain when allocation is appropriate vs runtime performance, structural connection, dependency, satisfaction and verification. Include formal/native definitions, plain explanation, good/bad examples, structure, visuals, validation and EA mapping.

## Next review
Native SysML v2 Satisfaction and its proper subjects, including current EA Function/Design «satisfy» usage and whether design-only satisfaction is a project policy rather than normative native restriction.
