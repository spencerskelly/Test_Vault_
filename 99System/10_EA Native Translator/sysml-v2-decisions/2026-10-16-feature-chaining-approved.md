# Approved — Feature Chaining as Native Syntax
Date: 2026-10-16
Status: APPROVED — native syntax capability, not a separately imported EA connector

## Meaning
A feature chain resolves a nested feature through existing features (e.g., charger.controller.processor). It does not create parts, ownership, interfaces or connections. Treat as native SysML v2/KerML syntax for addressing deeply nested usages, not a new MDSE edge.

## Intended use
- Author and resolve feature chains when internal block diagrams or structural views need to address features more than one level down.
- Two-layer (or deeper) diagram views may show nested ownership and a resolved endpoint path without flattening hierarchy.
- Only generate chains when context requires them; avoid gratuitous duplicate paths.
- No EA migration mapping creates a standalone relationship solely for feature chaining.

## Workbench
- Model authority remains native SysML v2 syntax in owning note.
- Structural tree navigates each segment of a chain; visual view draws an endpoint on the actual nested feature, with expandable context and path tooltip.
- Editing a connection endpoint on an internal block diagram patches the actual native endpoint reference/path in the note; no duplicate part or extra relation.
- Resolve scope, visibility, segment types and endpoint compatibility; error on unresolved paths.
- Layout/display depth is UI-only unless user edits semantic containment.
- Preserve a single canonical part definition; nested usages do not require individual notes.

## Next review
Membership/ownership and imports versus composite containment; native distinctions first, EA mappings second.
