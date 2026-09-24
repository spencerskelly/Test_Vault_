# External Model Import Governance

EA or other model imports are staged, not written directly over maintained vault content.

Required registries live in `99_System/11_Import`:

1. Identity Registry — source GUID ↔ MDSE ID/UID ↔ filepath/current vault.
2. Transformation Log — merges, collapses, semantic remaps, suppressions, renames.
3. Model Checks — ambiguity, naming, relationship, and source-model issues.
4. Pending Relationships — unresolved endpoints, including cross-package/cross-vault endpoints.

## Engineering migration direction

1. Import EA content into the engineering staging/base vault.
2. Classify and normalize semantics without inventing missing facts.
3. Establish stable note UIDs before splitting.
4. Split notes into Engineering Common and product-line vaults based on semantic ownership.
5. Preserve each note UID when it moves to its authoritative vault.
6. Rebuild the resolver index after the split.
7. Cross-vault relationships continue to point at the same note UID.

Do not create placeholder engineering elements merely to close unresolved links.
