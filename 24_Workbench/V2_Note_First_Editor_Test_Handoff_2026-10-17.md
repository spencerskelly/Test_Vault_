# Note-first Workbench editor — first offline test handoff

Date: 2026-10-17. Status: standalone HTML prototype prepared and JavaScript syntax-checked locally; **NOT** installed Obsidian plugin, native SysML v2 parser, or production writer.

The prototype is delivered separately as `v2-note-editor-test.html` (local conversation artifact); it is not claimed deployed to repository or plugin. It opens an `.md` note in browser memory, looks for a final `## SysML v2` heading with one `sysml` fenced block, populates an element selector from simple one-line part/port/action/state/item/attribute/use case declarations, and provides a popup with name/multiplicity edits. A successful edit changes the managed bottom syntax section and preserves frontmatter and prose preceding it. Export downloads an edited Markdown copy. The SysML source is collapsed by default and there is no duplicate vault tree. Advanced Merge Notes is visible only as planned/disabled.

## Manual acceptance steps

1. Open delivered HTML file in desktop browser, choose Example note.
2. Select `primaryModule` and use Workbench actions to change multiplicity from 4 to 5.
3. Expand the collapsed SysML section; confirm `primaryModule : PowerModule[5]` and unchanged design notes above.
4. Export revised note; compare original/freeform sections and YAML.
5. Open exported `.md`, check selected element appears and edit again.
6. Open malformed or unsupported Markdown and verify editor refuses to save rather than rewriting content.

## Explicit limitations and next implementation

- Browser-only file preview. Does not write directly into Obsidian vault; export-copy only.
- Lightweight regex recognizer, **not OMG-conformant parsing or source-aware AST editing**. Handles simple one-line syntax and no native semantic validation. Do not apply to production vault data yet.
- UI popup does not yet support create/remove elements, complex connections/bindings, graph edits, multi-note model consistency or stable source-span IDs.
- Next integrate with Obsidian plugin via vault/editor API: active note selection, derived parsed model, atomic validated note edits, content version checks, undo/redo and refreshing views. Replace lightweight recognizer with pinned native parser and syntax-preserving source transformation; add tests.
- Keep native syntax at end of note and MDSE-only metadata in governed YAML. No duplicate vault tree. Advanced Merge Notes is an independent future gate.

JavaScript source checked with `node --check`; browser UI and Obsidian runtime have not been tested in this environment.
