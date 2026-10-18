# MDSE v2 — SysML Source Ownership and Note Storage

**Status:** Historical Gate A proposal. **Superseded for implemented note layout and UX** by the approved 2026-10-17 SysML v2 note-authority and bottom-section decisions in `14_Workbench/docs/SYSML_V2_BUILD_READINESS_STABILITY_UX_GATE_2026-10-17.md`. The mid-note `## SysML source` example below is NOT the approved output layout. The approved layout has YAML frontmatter, user-authored Markdown, and a final `## SysML v2` fenced `sysml` region at the bottom. See `29_SysMLv2_Translator_Workbench/FIRST_RUN_FAST_TRACK_DEPENDENCY_RULES_DOC_AUDIT_2026-10-17.md` for first-run gates.  
**Scope:** Authoritative SysML language distributed across MDSE Markdown notes.  
**Date:** 2026-10-15.

## Decision proposed

Use **Markdown as the editing envelope** and **SysML v2 text as the semantic authority**. Each primary MDSE note can document one formal definition or element, but a Markdown file is *not automatically* a SysML owning namespace. Workbench indexes declarations from formally tagged source regions. The extracted, deterministic `.sysml` package set is the portable standards-facing artifact.

Never keep an independently editable relationship/structure copy in YAML, generated indexes, visual diagram files, or a separate BOM tree.

## Proposed note envelope (illustrative, not validated SysML source)

````markdown
---
uid: "stable-note-uid"
class: Object
sourceRole: authoritative-model
modelSymbol: "ProductLibrary::Controller"
---
# Controller

## Description
Engineering rationale, limitations and evidence.

## SysML source
```sysml
package ProductLibrary {
    part def Controller;
}
```

## Design notes
...
````

YAML identity fields are navigation/extraction metadata only. The SysML block owns the meaning. Do not infer SysML package membership from this note's folder.

## Ownership and file boundaries

- **Definition note:** owns a named reusable declaration when independently valid and unambiguous.
- **Assembly/context note:** owns a cohesive declaration in which local part usages, ports, interfaces, connections and constraints are made.
- **Element-view note:** documents an element formally declared in another source region; it cannot also author that declaration.
- **Knowledge note:** narrative and evidence only.
- **Reference notes:** index or summarize relations, but do not create semantic assertions merely by linking to notes.

A note can display multiple symbols, but it has at most one declared `primarySymbol` in metadata. A model symbol has exactly one authoritative owner, including when the symbol is a nested usage shown in a separate Obsidian note.

## Recommended v2 authoring constraint (first implementation)

1. Reusable definitions are standalone owning declarations in their authoritative source note.
2. Parent/context notes own their local usages and topology in one governed SysML region.
3. A separate note for a child usage is a **view/reference** unless an explicitly validated composition mechanism supports fragment ownership.
4. Workbench edits a child usage by locating its owner and changing the source region there; it never writes another copy to the child view.
5. Workbench renders a preview and validates symbol ownership before completing the edit.
6. Structural changes cannot be inferred from moving/renaming Markdown notes or directories.

### Why not independent fragments yet?

A standalone `part x : Definition` written in a child file can lose its enclosing owner/namespace. Splicing arbitrary fragments into parent braces creates duplicate or invalid declarations and makes valid external SysML exports uncertain. Fragment composition may be added after a formal namespace/owner map, deterministic ordering, conflict detection and independent parser tests exist.

## Source indexes (derived, disposable)

| Index | Key | Generated information |
|---|---|---|
| Note identity | stable UID | filename, source kind, primary symbol |
| Symbol table | resolved symbol / unique identity | authoritative note, source range and owner |
| Usage table | usage identity | declaration owner, typed definition, multiplicity |
| Relationship table | semantic kind + endpoints | owning source location, referenced symbols |
| Reverse usage | typed definition UID | parent usages and applicable configurations |
| Source ledger | EA/BOM source key | conversion decisions, revisions, preserved evidence |

Indexes are rebuilt from authoritative source plus governed import evidence; no manual edits to indexes.

## Workbench atomic write-back

1. Resolve requested symbol/usage to its single authoritative note and exact source region.
2. Confirm source hash/version and that dependencies still resolve; reject stale edits.
3. Parse existing source and stage an AST-aware edit (avoid global string replacement).
4. Validate syntax, symbol ownership, identifiers, endpoints, affected references and scope.
5. Show a semantic diff and save the minimum files atomically; if atomic writes across files are not possible, journal and safely recover/revert changes.
6. Re-index dependencies and refresh cached diagrams, BOM and Where Used views.
7. Record accepted source provenance and Git diff; no silent correction of ambiguous imports.

## Identity rules

- Note UID remains independent of filename/path and visible label.
- Qualified SysML name is a resolvable address, not necessarily permanent identity across rename.
- Source EA GUID/BOM source keys survive in an audit ledger.
- A symbol rename requires explicit reference-update analysis; an Obsidian rename alone is not a semantic rename.
- Do not assert a stable SysML element identity from note UID alone without the approved source-to-symbol identity map.

## Conformance gates

- Each formal symbol has exactly one authoritative owner and no duplicate declarations.
- Standard extracted SysML package set independently parses and resolves all intended cross-note names.
- Repeated extraction is byte-for-byte deterministic with a pinned compiler/spec baseline.
- A Workbench edit to one usage changes only its owning declaration and intended references.
- Markdown narrative, views and layout may change without changing SysML semantics.
- Failed validation does not leave an ambiguous partially updated source state.
- A BOM or Where Used index rebuild does not write relationships into child notes.
- All relative links in these docs resolve within the numbered repository layout.

## Open points

- Precise supported document-to-symbol source-region encoding, including nested declarations.
- Source composition details and package ownership for cross-file imports.
- Whether a separate `.sysml` file can be authoritative for selected large/cohesive model units, while preserving Markdown as the user interface; the default above is note-owned SysML blocks.
- Exact SysML parser/reference implementation pin, independent of Workbench.
- Safe editing support for references across packages and model scope.

## Adjacent work

- [Structural mapping](Structural%20Mapping%20Contract.md)
- [Translation matrix](Structural%20Translation%20Matrix%20-%20First%20Pass.md)
- [Architecture decisions](Architecture%20Decisions.md)
- [BOM integration](BOM%20Integration.md)
- [V2 test plan](../25_Testing/README.md)
- [V2 research plan](../29_SysMLv2_Translator_Workbench/README_SysMLv2_Translator_Workbench.md)
