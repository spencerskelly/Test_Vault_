# Golden Import Step 2 — EA Packages

Decision date: 2026-10-17. Status: APPROVED; runtime implementation pending.

- EA Packages are imported as **folders**, preserving the source organizational hierarchy.
- Package/folder containment is organizational only. It must **not** imply native SysML v2 ownership, PartUsage, specialization, dependency, membership, or any other engineering semantic relationship.
- Do not create a separate MDSE semantic note or native SysML v2 Package declaration merely because an EA Package exists.
- Preserve EA package IDs, source hierarchy and provenance in the import manifest or suitable folder metadata so rules may use package-specific exceptions where explicitly approved.
- Real semantic relationships derive only from modeled elements and connectors, independently of folder nesting.
- Verify deterministic folder paths, collisions and reimport stability; package rearrangement alone must not silently change native model semantics.
