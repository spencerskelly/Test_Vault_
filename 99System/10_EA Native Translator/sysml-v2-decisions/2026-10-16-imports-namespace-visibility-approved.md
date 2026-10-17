# Approved: SysML v2 Native Imports and Namespace Visibility
Date: 2026-10-16
Status: APPROVED — Option A, relationship review #8

## Plain language
An import makes a declaration from another namespace accessible under appropriate visibility rules. It does not move, copy, instantiate, specialize, or compose that element.

## Native concepts
- Membership import: imports a particular named member from a namespace.
- Namespace import: imports accessible membership of a namespace.
- Private/public/protected import visibility controls which contexts can access imported declarations. Exact scope and grammar must be validated in a conforming parser.
- Qualified references can be preferable to new imports where ambiguity or name conflicts exist.

## Project policy
- Support native SysML v2 import syntax and visibility.
- Workbench manages imports or qualified references automatically where safe; advanced users may inspect/edit imports.
- No special EA connector types will be transformed into imports.
- One canonical reusable definition per type; importing never creates a duplicate.
- Obsidian folder paths do not automatically establish SysML namespaces.
- SysML v2 syntax in canonical Obsidian notes remains authoritative, with structural and diagram edits updating source text.

## Workbench structural and visual views
- Structural: show source namespace, effective visibility, resolved symbol and owning declaration. Imported elements remain owned where originally declared.
- Visual: diagram actual elements/usages, not import arrows by default. Optional import/dependency explorer can visualize import resolution.
- Type selection auto-inserts legal import or qualified type reference, avoiding name shadowing/collisions.
- Rename, move, delete: update or invalidate references safely across notes; stage multi-note edits atomically and re-parse before commit.
- Validate import path, recursion/visibility, collisions, ambiguities and unresolved references.
- Index is derived and rebuildable from notes, not an independent semantic source.

## Example
```sysml
package CommonParts {
    part def Controller;
}
package ChargerSystems {
    private import CommonParts::Controller;
    part def Charger {
        part controller : Controller;
    }
}
```

## Not to confuse with
Membership (where element is declared); typing (usage : definition); specialization (kind-of); composite part usage (contains occurrence); reference part (non-owning occurrence).

## Next: Aliases
Review native alias membership and distinction from import, typing and renaming with Workbench behavior.
