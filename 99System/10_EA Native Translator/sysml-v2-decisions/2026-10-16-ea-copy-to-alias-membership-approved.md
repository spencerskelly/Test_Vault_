# APPROVED — EA Copy maps to SysML v2 Alias Membership
Date: 2026-10-16
Status: APPROVED — Relationship #9

## Project-specific source semantics
The user confirms that **EA model relationship “Copy”** is used to mean another name/reference to the SAME model element, matching native SysML v2 alias membership. This rule refers to the actual EA model relationship called Copy, not generic EA Copy/Paste UI commands, EA Alias string fields, nor duplication of a definition.

## Native translation
- Map EA Copy to a native `alias <localName> for <qualifiedExistingElement>;` declaration, placed in the appropriate SysML v2 namespace.
- Alias is non-owning: it does not create a distinct reusable definition, usage, subtype or physical part.
- Preserve only ONE canonical definition per distinct type, as per approved model rules.
- Resolve direction/identity using actual source/target connector and names before conversion; do not assume source orientation is correct. An alias must resolve to an existing element and have a usable local name.
- If Copy represents a semantically independent element in a particular case, flag for correction rather than silently merge distinct elements.
- Obsolete EA connector does not need permanent preservation after validated migration.

## Workbench structural and visual projections
- Structure: aliases appear as references under the aliasing namespace and navigate to canonical definition; never duplicate definition as a tree-owned part.
- Diagram: can display alias in context; inspector reveals canonical qualified name and alias origin. Alias is not a second part box or a connection.
- Search resolves aliases to canonical element; rename/alias edits update the owning note's native SysML v2 syntax.
- Validate namespace, visibility, collisions, cycles/unresolved targets and identity.
- A usage of the type is still a separate native typed usage declaration; alias alone does not instantiate anything.
- No independent Markdown note required for alias.

## Educational distinction
EA Copy (project convention) = another name for same thing; native SysML v2 alias.
EA Paste as New = creates a new independent element, not an alias.
EA Paste as Link = diagram re-use/viewing the same element, not necessarily a named alias.
EA Alias field (metadata/filename hint) = not automatically a SysML v2 alias relationship.

## Example
```sysml
package CommonParts {
  part def Controller;
}
package VehicleSystems {
  alias ECU for CommonParts::Controller;
}
```

## Next
Continue native relationship inventory following alias membership.
