# APPROVED: Note-authoritative SysML v2 and reusable definitions
Date: 2026-10-16
Status: APPROVED; supersedes conflicting statements in earlier 2026-10-16 mapping decisions.

## Non-negotiable rules
1. The **SysML v2 syntax stored in Obsidian notes is the authoritative model**. Visual diagrams and structural trees are synchronized editors/projections, never separately authoritative stores.
2. **Any valid edit from any view modifies the same underlying SysML v2 model and persists to its owning note(s)**. Text edits reparse and update both views; structural edits and diagram edits update text with validation and atomic saves.
3. **One reusable definition per distinct modeled type across the vault**, regardless of the number of usages. Do not duplicate a definition solely because it is used in different parent assemblies/products.
4. Usages are expressed in the owning notes using native SysML v2 usage syntax, including type reference, nesting, multiplicity, and any context-specific properties. **A usage does not require its own Markdown note**. Optional dedicated usage note only when justified by independent documentation/navigation needs; avoid creating duplicate semantic authorities.
5. EA is import source, NOT the continuing authority. Old EA connector records and links do not have to remain once the translated v2 model is correct; do not require permanent provenance retention or preservation of obsolete EA relationships. During import provide enough diagnostics to detect bad mappings; cleanup may discard obsolete source records.
6. EA Object → reusable `part def` as default. EA Generalization → native specialization as default, subject to validation and later reclassification. Once corrected, original EA connector can be discarded.
7. Native v2 relationships should be used wherever feasible; keep non-v2-specific extensions in a separate section rather than manufacturing new v2 keywords.

## Workbench write contract
- Parse each note's authoritative SysML v2 into an indexed semantic representation; indexes and diagrams are rebuildable.
- Each model feature and relationship has a stable address within note syntax for navigation and edits, even without one usage note per occurrence.
- Resolve definition symbols globally; every usage references its common type definition; support where-used via reverse indexing instead of back-references in definitions.
- Write structured/diagram edits through an AST-aware patch to the owner note(s), never just persist diagram geometry as if it were semantics.
- Validate and preview any cross-note effect; use atomic staged writes and rollback on parse/semantic failures.
- In text editing, preserve user-authored formatting, comments and unrelated note content. Keep layout metadata distinct and non-authoritative.
- When a structural/diagram edit spans multiple notes, perform a coordinated transaction; reparse and redraw all affected views.
- Deleting a usage removes its usage declaration from owning text; deleting a definition requires impact review for linked usages. 
- Do not create Markdown notes automatically for each usage; allow optional usage notes with a canonical link to the owning declaration, not another conflicting definition.

## Example
```sysml
part def CANTransceiver;
part def SafetyController {
    part canInterface : CANTransceiver;
}
part def GatewayController {
    part canInterface : CANTransceiver;
}
```
The single CANTransceiver definition is reused twice; the two usage declarations live in the two owner definitions' notes.

## Validation
- Confirm one canonical definition per symbol/identity, multiple legitimate usages; detect duplicate identities and dangling type references.
- Verify diagram edit→note syntax→structure, tree edit→note syntax→diagram, and text edit→both projections.
- Test multi-note rename, deletion, redefinition, nested parts, multiplicity, and shared definitions.
- Confirm rebuilding the index and diagrams purely from notes produces equivalent semantic results.
- Confirm import cleanup does not affect canonical v2 syntax or where-used reports.

## Documentation updates required
Previous decisions that mention permanent EA provenance as a requirement, separate model authority, or one note per usage should be read as SUPERSEDED by this file. Update corresponding Workbench backlog and implementation tests.
