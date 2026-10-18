# SysML v2 translator + Workbench build readiness, stability and UX gate

Date: 2026-10-17. Status: review and actionable gate plan; no implementation or parser acceptance claimed.

## Current conclusion
Approved mappings are sufficiently developed to begin engineering. Production write, native parser acceptance and consistent multiple-view UX are not yet demonstrated. Phase 5 typed graph is synthetic; Phase 6 covers all source connector families by disposition but not conversion; Phase 7 produced one diagnostic per 14,688 connectors and zero native accepted; Phase 8 did not execute full JS engine or native serializer. BOM schema proposals are partially validated but not authorized as production writer. The recent approved aggregation, independent UID, MDSE YAML flagLink and Workbench advanced Merge Notes decisions must be implemented.

## Must decide before stable authoring
1. **Authoritative canonical representation**: one semantic graph with stable UID for each note/definition and stable separate identity for usages, relationships and source records; precise direction of synchronization between vault Markdown/YAML and .sysml text, and conflict treatment when edited externally.
2. **Native syntax/runtime pin**: pin exact OMG SysML v2 language, standard libraries, parser and serialization convention, define support for absent multiplicity and qualified names. Parser acceptance required on all emitted native structures, not just string matching.
3. **Source-specific YAML extension schema**: namespace BOM-only data and EA original metadata; make flagLink references UID-bound, independently keyed by source connector, with note-body reason and tracked resolution state. Set rules for metadata upgrade and avoiding ungoverned fields.
4. **Identity and editing governance**: EA notes and BOM part notes always remain separate with distinct UIDs initially; EA alias matching BOM part number is a candidate only. Define UID redirects, note move/rename, deleted/replaced notes, approved Merge Notes preview, safe transactional update and rollback.
5. **Usage record identity**: multiple EA connectors and separate BOM rows remain distinct usages even with matching endpoints; define stable keys, name collision handling and when an operator can explicitly assert same occurrence. Absent multiplicity must remain unspecified.
6. **BOM number and units**: multiplicity vs measured quantity; exact-decimal numeric storage, approved dimensions/UOM and `ea` collision rule, source revisions/configuration/effectivity, alternates not inflating consumed quantities. Confirm writable schema and migrator.
7. **Semantic completeness and fallback**: each element and connector must be native, MDSE extension, flagLink or deliberately excluded with rationale; unsupported native constructs cannot be faked. All unresolved relationships remain visible in note YAML and note-body explanation and are not native serialized.
8. **Reimport/merge policy**: human edits are distinct from source observations; three-way compare from last import, dry-run diff and explicit conflict resolution. No silent overwrite of notes, YAML, usages, redirects or curated diagrams.

## Workbench user experience release requirements
- Definitions and usages appear distinctly in hierarchy and diagrams; typed navigation, Where Used reverse query, provenance and role/quantity display.
- Draw-line-then-choose operation validates endpoints and ownership before mutation; native binding distinct from connection, exposure and port ownership.
- All structural/visual/table/text views edit one canonical graph; no independent mutable projections; edits are atomic with undo and Git diff.
- Contextual validation diagnostics explain source issue, suggested fix and whether it blocks export; flagged links remain browsable and editable in notes.
- Source EA and BOM note matches presented as review candidates, never automatically merged. `Advanced Actions → Merge Notes` preview, choose survivor UID, redirects, inbound-link review, rollback and audit trail.
- Work safely offline in vault, no auto-delete or excessive note generation, deterministic filenames/IDs, stable navigation even after note moves.

## Build and acceptance sequence
1. Freeze schemas/operation catalog, canonical data model and UID/provenance contract.
2. Implement pure semantic transform shared by EA/BOM evidence adapters (separate source records, same target semantics).
3. Implement deterministic native SysML v2 serializer and pinned external parser/library conformance fixtures across each approved element/relationship family.
4. Implement Markdown/YAML rendering, flagLink explanation rendering, and source-ledger reconciliation (all rows exactly once).
5. Implement guarded Workbench editing via canonical graph and preview, atomic save, undo, view synchronization and stable UID navigation.
6. Implement three-way incremental reimport with protected human edits, conflict UI and rollback.
7. Implement advanced Merge Notes only after redirect/link integrity tests and staged transaction support.
8. Golden-import a synthetic part+action+state+port+requirement+connection+unit+alternate fixture, then reduced QEAX and BOM sample; verify reproducible hashes, parser success, count reconciliation, no lost links and zero silent overwrites.

## Recommended decision defaults
- Canonical semantic graph governs editing; `.sysml` is a verified projection, not an independent unsynchronized master. Obsidian Markdown/YAML stores the vault model and governed MDSE extras; bidirectional text edits require parse-and-validate before graph commit.
- Fail closed for unresolved native semantics: keep YAML flagLink and note explanation rather than generating invalid syntax.
- No automatic EA/BOM identity merge. Stable UIDs are never recycled; redirects must be retained when an operator merges notes.
- Authoring mode may use warnings; native publish/export gate rejects parser errors and unresolved blocking references, but flagged legacy relationships may remain in MDSE notes as explicit nonnative content.

## Required test evidence before shipping
Pinned parser version and native fixtures; source row disposition checksum; UID and usage collision checks; repeat-import idempotence; branch/conflict and rollback tests; Workbench multi-view snapshot coherence; runtime tests inside Obsidian; provenance-preserving merge/redirect tests; CI success and manual UX acceptance. Repo contains methods/tests/aggregate data only, never private raw model ledgers.

## Superseding approved authority and UI decisions — 2026-10-17

**Authoritative source: the note containing native SysML v2 syntax.** This supersedes any recommendation above that an independently persisted canonical graph governs edits or that .sysml is merely a derived projection.

1. The relevant Obsidian note containing SysML v2 source is authoritative at all times. Every Workbench structural, visual, tabular, form, and relationship edit must be applied to the note's v2 syntax (via validated, minimally scoped text modification), then reparsed and reflected in all other views.
2. Parsed semantic graphs, indexes and diagram/layout state are **derived and disposable**. Never store a competing authoritative graph. Reject invalid edits without changing the note; use atomic note writes and rollback/undo. An external/manual note edit invalidates projections and triggers a reparse and refresh. Preserve native semantics and surrounding human comments/formatting where possible.
3. MDSE-only values (EA/BOM provenance, unmappable source fields, `flagLink`, note UID and other governed metadata) remain in **the same note's YAML**, with narrative explanation in the body as required. Do not fabricate native v2 syntax for MDSE-only content. Note editing applies a single atomic transaction when both v2 and YAML must change.
4. The standard Obsidian File Explorer already provides vault navigation. **Remove the duplicate vault folder/file tree from the MDSE sidebar**. Do not remove native Obsidian File Explorer or note navigation.
5. Provide a compact **element selector dropdown scoped to the currently open note**, listing the definitions/usages/features within that note. Distinguish same-named entries via kind and qualified/containing path; selecting one focuses its details, relationships and view context. Handle note switching, empty/no-syntax notes, duplicate names and parse errors gracefully.
6. Move general Workbench actions and views toward an **on-demand popup/modal (or command-driven panel)** rather than a permanently space-consuming sidebar. Candidate surfaces: command palette, note context action, toolbar button. Keep an optional narrow contextual sidebar only if it adds distinct value. Preserve keyboard access, screen-size responsiveness and editor focus; no duplicate File Explorer.
7. The popup provides element selection, structural/visual/text/relationship/table views and validated actions. It must always show which note and selected element the action will change; preview edits and parse feedback before commit.
8. `Advanced Actions → Merge Notes` remains isolated from everyday actions. It requires preview, explicit confirmation, backup, surviving UID, redirect/link integrity validation and rollback. A merge updates the actual authoritative note(s), not a cached graph alone.
9. All view consistency and reimport tests must assert **note syntax + governed YAML → parsed model → views**, and **view action → atomic note edit → reparse → every view**. Include external editor modifications, multi-element notes, malformed v2 text, round-trip formatting, UID links, conflicts and undo.

### Implementation specification (pending code)
- Specify a stable fenced-region/section convention for native SysML v2 within each note, including support for multiple elements and safe boundaries, while preserving ordinary Markdown.
- Establish a pinned parser and a source-span-aware edit engine; partial edits must not rewrite unrelated syntax or source provenance.
- Derived graph caches keyed by note content hash, with invalidation on vault change and editor buffer change.
- UI acceptance: no Workbench vault tree; open-note dropdown; popup opens without disrupting editing; each action changes note source then synchronizes all projections.

## Superseding note layout and model authoring contract — 2026-10-17

**Approved:** The authoritative native SysML v2 syntax resides at the **bottom of each Obsidian note**, under its own dedicated section. Users can author ordinary notes, explanations, images, links and other supporting content **above** this section, without the Workbench taking ownership of that content. This clarifies the earlier unspecified placement of native syntax.

### Note boundaries
- Existing YAML frontmatter is for MDSE UID, provenance, source-specific BOM fields and MDSE-only relationships (including `flagLink`); do not fabricate native syntax for this metadata.
- Freely editable Markdown content occupies the central/top body of the note. Workbench preserves it byte-for-byte unless a user explicitly edits that content.
- The final dedicated section, suggested heading `## SysML v2`, owns exactly one **managed** `sysml` fenced region containing all native definitions/features/usages attributable to the note. Allow multiple semantic elements/usages inside this section; the file's native source is authoritative.
- The managed region stays at the end of the note. The finalized delimiter/escaping strategy must be proven resilient to other fenced blocks and code examples in user-authored prose. Provide safe migration for existing notes and errors for duplicate/missing managed regions.

### Primary user interaction
- **Workbench interface is the primary authoring surface**. Users should not be expected to type or understand SysML v2 text to make normal model edits.
- The active-note element dropdown scopes selection to definitions, usages and features contained in the open note. Provide context-aware Add Element, Add Part/Action/State/Port/Attribute, Add Relationship, Change Type, Edit Name, Set Multiplicity, Configure Quantity/Unit, Move/Remove/Review operations according to semantic eligibility. Do not offer actions unsupported by the type or namespace.
- Use validated forms, property editor, visual diagram gestures, and relationship picker; preview the exact change, ownership, affected references and any failure reason where useful. An edit applies **to authoritative note syntax first**, then reparses and refreshes the dropdown, structure, diagrams, relationship panel, and tables. No independent graph or visual projection becomes authoritative.
- Source-aware rewriting targets only the relevant native syntax span; preserve comments and formatting outside the target span where possible. Changes involving YAML must be one atomic note transaction. Handle stale editor buffers / concurrent external modifications with content-version checks, fail-closed conflict prompt, Undo, Git diff, backup and rollback.
- Direct manual editing of native syntax remains possible for advanced users but is not required. Manual or external edits trigger reparse, validation and regeneration of derived views, not a competing editor-side model state.
- Keep the Obsidian File Explorer as the sole vault navigator. The MDSE popup or minimal contextual toolbar provides scoped model actions/views; no duplicate vault tree.
- Keep Merge Notes specifically in **Advanced Actions**, with reviewed survivor UID, independent EA/BOM note identity until approved, backlink/usage preservation, and undo/rollback.

### Illustrative note layout (not a final schema definition)

```markdown
---
uid: <stable-mdse-uid>
eaAlias: PC-100
bom:
  partNumber: PC-100
---

# Charger Assembly

Notes, design reasoning, attachments and supporting information written by users.

## SysML v2

```sysml
part def ChargerAssembly {
    part powerModule : PowerModule[4];
}
```
```

### Test gates
1. Add/edit a part and typed usage entirely from Workbench without touching source text.
2. Preserve prose and unrelated fences above the bottom managed section after every UI edit.
3. With multiple elements in one note, dropdown selection identifies exact owned usage, edits only that source span, and preserves stable usage identifiers.
4. Reject nonconformant generated edits atomically; keep the prior note and show actionable validation diagnostics.
5. External edit / note rename / reimport causes consistent reparse, conflict protection and updated views.
6. MDSE YAML metadata, source provenance and body `flagLink` explanation survive all native UI edits.
7. Native parse against pinned OMG-compatible grammar is a release gate, not an assumption.
