# ADR-V2-06 — Note format: user notes on top, one SysML v2 block at the bottom

Date: 2026-10-18. Status: **PROPOSED.** The layout is derived from decisions already approved (V1 [Note Layout](../100_Archive/V1/16_Definitions/Note%20Layout.md) W-97, W-99, W-206; [ADR-V2-02](V2_RELEASE_ARCHITECTURE_DECISIONS_2026-10-18.md); ruleset 1.23 §16.4). Items marked ⚠ are new and need owner confirmation. Enforced by [`mdse_note_format.py`](../21_Importer/mdse_note_format.py) and CI.

## Decision

A note has two zones. People write in the top zone. The importer and Workbench own the bottom zone.

```
---                                    FRONTMATTER (governed order, W-97)
type: Object
subtype: part
id: OBJ-00042
uid: 20261018230000001skellyspencer
status: Draft
eaType: Hardware Component             (translated notes only)
tags: []
sourceRole: authoritative-model        (notes that own SysML text)
primarySymbol: ChargerProduct::Charger
<relationship fields>
---
# Charger                              ┐
                                       │  USER ZONE — humans own it.
Note text…                             │  Tooling never rewrites it.
## Notes                               │
## Aliases / ## Former ids             ┘
                                       (three blank lines, W-99)
## Source: EA                          ┐  MANAGED FOOTER — regenerated
EA GUID: {…}                           │  on reimport (ruleset §16.4).
- PN: 4050030                          ┘
## SysML v2                            ← always the LAST section
> hint line
```sysml
package ChargerProduct { part def Charger { … } }
```
```

## Frontmatter

| Key | Required | Rule | Set by |
|---|---|---|---|
| `type` | yes | a class in `99_System/03_Schemas/element-types.yaml` | importer / human |
| `subtype` | if the class has subtypes | one of that class's subtypes; absent when the class has none | importer / human |
| `id` | yes | `PREFIX-NNNNN`, prefix from the class | importer / human |
| `uid` | yes | 30 characters, `^\d{17}[a-z-]{13}$`, never changed | importer / human |
| `status` | yes | template default is `Draft`; a person advances it | human |
| `eaType` | translated notes | EA stereotype, else EA object type | importer |
| `tags` | yes | list | human |
| `sourceRole`, `primarySymbol` | notes that own SysML text | `authoritative-model`; fully qualified name declared in the block | importer / Workbench |
| relationship fields | as `relationships.yaml` | see ⚠ Q2 | Workbench |

Fixtures in this toolchain repository use `fixture: true` and ids `99000`–`99999`, a range the real vault never uses.

## The `## SysML v2` section

- It is the **last** `##` section. Exactly one per note.
- It contains one fenced `sysml` block and nothing else except the one-line hint.
- A note owns its **definition** and the **usages it owns** in the same block. Shared physical parts have one definition note and contextual usages in the owning definition's block.
- Packages organize folders and do not decide the semantic owner (STEP-00). A package that has a description also gets a `modelCheck`/`Package` note (W-147); that note has no SysML block.
- Anything else belongs above it. A second `sysml` fence anywhere is an error.

## Who may change what

| Part | Human | Importer rerun | Workbench |
|---|---|---|---|
| User zone | edits freely | **never touched** | never |
| Governed frontmatter | `status`, `tags`, own notes | refreshes EA-owned keys, logs overwrites | derived keys only |
| `## Source: EA` | no | rewrites | no |
| `## SysML v2` | only with the parser check | rewrites from the canonical graph | edits transactionally |

`replace_sysml_block()` guarantees the first row: it returns the text above the heading byte-for-byte, and a unit test mutates the function to prove the test fails if that ever changes.

## Workbench as relationship manager

Workbench reads and writes the SysML block. It does not keep a second copy of relationships. If the block changes outside Workbench, the graph freezes and asks for a refresh (owner-approved requirements in the [recovery handoff](MDSE_V2_RECOVERY_HANDOFF_2026-10-18.md)).

## Changes from earlier decisions

1. **`Source: EA` is no longer last.** V1 (W-99, Note Layout item 9) said it is always last. ADR-V2-02 makes `## SysML v2` the final section, so `Source: EA` is now second to last. Only the order changes.
2. **Local Model.** V1 notes carry a bottom `## Local Model` region (schema 0.5, 30-character block ids for parts, endpoints, connections, flows). In v2 that structure is SysML usages. V1 notes keep their region until migrated. ⚠ Q1 covers identity.
3. **Fixtures.** `class:` became `type:`. The sample vault's sibling `.sysml` file was folded into the note, because a second copy is a second authority.

## Enforcement

- `python3 21_Importer/mdse_note_format.py NOTE.md …` validates order, identity, class/subtype, footer layout and that `primarySymbol` is declared in the block.
- `25_Testing/test_v2_note_format.py`: 20 tests, including mutation checks that the rules actually fail.
- CI runs the validator on the golden and sample notes. The importer's output must pass the same validator before a ZIP can be called ready. The current interim generator (`v2_step03s_generate_notes.py`) does not emit this format yet.

## Open questions for the owner

| # | Question | Recommendation |
|---|---|---|
| **Q1** | With Local Model gone, where do the stable 30-character tokens for usages (parts, ports, connections) live inside the SysML text? Reimport and Workbench need them. | SysML short names, `part <'2026…'> controller : Controller;`. Must be accepted by the pinned parser **before** adoption; I have not verified it. |
| **Q2** | Frontmatter relationship fields (Breadcrumbs, Dataview, Rovo). Keep them as a *derived mirror* of the block, written only by Workbench in the same transaction, or drop them? | Keep as a derived mirror. Without it nothing can query "what satisfies REQ-x" without parsing SysML. |
| **Q3** | Only two EA fields (`Object_Type`, `Stereotype`) and **no** tagged values are decided as frontmatter properties. 38 tags are `Source: EA` body lines, including PN, MFG PN, Brand, Quantity, Piece Cost, Current Max. Which, if any, become frontmatter or SysML attributes? | Promote the Identity group (`id`, `SysML1.4::id`, `PN`, `MFG PN`, `Brand`) so they can be queried. See the [mapping matrix](V2_NOTE_MAPPING_MATRIX.md). |
| **Q4** | `sourceRole` and `primarySymbol` already exist in the golden fixture. Adopt them as the governed v2 property names? | Yes. They are in use and the extractor depends on them. |
| **Q5** | SharePoint: W-382 removed all path-length checks. Reinstate a blocking *report* (never shortening), and at what limit? | Gate at 400 decoded characters, and report the sync-root budget. See the [organization proposal](V2_FILE_ORGANIZATION_PROPOSAL_2026-10-18.md). |
| **Q6** | Rovo and SharePoint. The Atlassian SharePoint connector page lists Word, Excel, PowerPoint, PDF and web pages. Markdown is not listed. How will Rovo read the model? | Confirm with Atlassian. If `.md` is not indexed, generate a Rovo-readable projection (see the proposal). |
