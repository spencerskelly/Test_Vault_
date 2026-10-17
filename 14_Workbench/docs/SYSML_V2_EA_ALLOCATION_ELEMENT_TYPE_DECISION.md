# EA Allocation Default Translation — Element-Type-Driven Rule
Date: 2026-10-17
Status: approved default, subject to semantic validation
Supersedes narrower ambiguous guidance in SYSML_V2_EA_ACTIVITY_DESIGN_ALLOCATIONS.md.

For source EA connectors whose meaning/stereotype is allocation:
- Activity + Object -> object owns native SysML v2 PerformActionUsage, referencing corresponding action.
- State + Object -> object owns native SysML v2 ExhibitStateUsage, referencing corresponding state.
- Object + Object -> native SysML v2 AllocationUsage with source/target following original EA direction, subject to validation.

Activity/State cases are direction-independent for recognition, not for provenance: original source/target, connector GUID, stereotype and direction retained. Object-to-Object direction is semantically consequential and must not be arbitrarily reversed.

Classification relies on canonical mapped types and actual intent. Exceptions: unsupported endpoint type, unresolved identity, conflicting EA stereotype/meaning, wrong ownership/type, or relationships incapable of legal native construction. Keep an explicit disposition and source copy/flag; no silent coercion.

Workbench: drawing line between two elements yields filtered semantic choices; Activity/Object prioritizes Perform, State/Object prioritizes Exhibit, Object/Object may offer Allocate alongside other semantically eligible choices; never auto-create Allocate just because two objects are selected. Creation preview resolves owner, target, scope, and exact native construct.

BOM translator: object/part identities shared with EA mapping; BOM hierarchy or co-occurrence alone never implies allocation, perform, or exhibit. Preserve BOM source separate and existing native behaviors when reconciling.

Verification: test both EA endpoint directions for Activity/Object and State/Object, Object/Object both directions, shared definition reused by several objects, definition vs instance ownership, inconsistent connector stereotype, combined EA+BOM import, idempotent import, canonical graphical/text/table view sync, and source coverage ledger. 
