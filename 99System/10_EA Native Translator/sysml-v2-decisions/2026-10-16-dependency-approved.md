# Approved: EA Dependency → Native SysML v2/KerML Dependency
Date: 2026-10-16
Status: APPROVED — same semantic meaning and direction

## Meaning
A directed dependency asserts that one model element (the client/dependent) relies on another element (the supplier) without implying any more specific semantics of composition, connection, specialization, satisfaction or allocation.

## Import
- Translate EA Dependency to native SysML v2/KerML Dependency with same client/source → supplier/target meaning and arrow direction.
- Resolve endpoint identities after approved EA Copy→Alias consolidation; collapse only truly identical duplicate dependencies.
- Preserve direction and meaningful context. Validate legal native syntax, imports and endpoint references before export.
- Do not reclassify dependencies as allocation, composition, flow or requirement relationships automatically.
- The original EA connector is no longer authoritative following successful translation.

## Workbench
- Structural view: list dependencies under dependent element, with navigable supplier targets and reverse 'depended on by' index.
- Visual view: directional dependency line clearly distinguished from connection, inheritance, allocation or satisfaction. Selecting opens canonical relation and endpoint navigation.
- Editing dependency from any view modifies canonical SysML v2 syntax in owning note(s); reparse and synchronize all views.
- No duplicate definition or note is created by dependency. Dependency relations do not imply an owned part usage.
- Provide clear plain-language usage guide, good/bad examples and endpoint validation.

## Example
ControllerSoftware depends on CANProtocolDefinition for a particular protocol contract; that fact alone neither connects physical ports nor proves any requirement is satisfied.

## Documentation caveat
Precisely verify emitted textual syntax against OMG SysML v2/KerML parser before production export. Do not invent a SysML v2 keyword for a relationship that is already represented in KerML.
## Next discussion
Native structural connections and connector semantics, distinguished from dependencies, ports and interfaces.
