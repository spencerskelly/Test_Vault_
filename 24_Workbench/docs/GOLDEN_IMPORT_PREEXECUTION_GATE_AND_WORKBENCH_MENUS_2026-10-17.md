# Golden Import — Pre-execution gate and approved Workbench action taxonomy

Date: 2026-10-17. Status: source integrity PASS; production import NO-GO; controlled synthetic/dry-run work GO.

## Confirmed live source
Local reduced fixture `EA_2026_10_15_endgame_mini.qeax` opened with SQLite read-only. `PRAGMA quick_check` returned `ok`. Counts: t_object 11447, t_connector 14688, t_package 1389, t_diagram 2208. This is basic source integrity, not semantic acceptance.

## Approved UI navigation and action taxonomy
Context popup has four distinct **navigation/filter dropdowns** scoped to the selected note/element: Links, Structure, Behavior, Requirements. These expose existing items and their actual links (including incoming/outgoing, owners, usages, actions/states and requirement/verification associations). They should be dynamically populated, not a list of dummy diagram links.
- **Note Actions:** create/add element, view/edit note model properties, add native attribute/part/port/action/state/requirement, rename, open note.
- **Link Actions:** select existing or make new typed relationship, change role/cardinality, navigate endpoints, inspect origin and resolve flagged links.
- **Advanced Actions (collapsed):** Merge Notes (with UID redirects, preview, rollback), Split Notes, bulk migration/repair, duplicate reconciliation, UID repair, destructive delete with impact preview, guarded source reimport and restore.
- Provide current-note element picker; show qualified kind/path when ambiguous. Popup from selected editor note or generated view; auto show setting OFF by default and manual command always available.
- Selection dropdown needs to update actual chosen subject. Show only actions valid for subject and source note. Generated Workbench view selection must identify actual model note, not canvas file.

## Import semantic authority
- One stable UID per imported note; keep independent EA/BOM notes even when EA alias matches BOM part number. Post-import reviewed merge only.
- Native SysML v2 **bottom section of each note is authoritative**; user Markdown above remains untouched. YAML frontmatter stores UID, source provenance, BOM-specific extensions and unresolved `flagLink`; flagged links have a readable explanation in the note body.
- Interface editors update source syntax first and reparse; no competing persistent semantic graph. Advanced direct text editing allowed but not normal user workflow.
- Multiple EA connectors can generate separate named PartUsage/ActionUsage/StateUsage/etc. Per-connector provenance, stable occurrence identity, explicit multiplicity, unspecified default, cycle protection.
- Preserve all source elements/connectors through native, MDSE-only, flagged or explicitly excluded dispositions, each with reason; keep source-specific row ledger local.

## Gate assessment
| Gate | Current evidence | Status |
| --- | --- | --- |
| QEAX database integrity | read-only quick_check ok and counts | PASS |
| Family mapping approvals | 60 element families and 26 relationship families reviewed, plus aggregation refinements | POLICY PASS, execution unproven |
| Native serializer and official pinned parser | No full native acceptance evidence; Phase 7 report counts zero native accepted | BLOCK |
| Full source-ledger-to-canonical graph and deterministic writer | Phase 8 normalization report explicitly lacks JS engine or native generation integration | BLOCK |
| Note writer and MDSE YAML flagLink emitter | Policy and prototype documented, actual vault note write integration unverified | BLOCK |
| Stable UID and separated EA/BOM identity | Policy, cross-source merge delayed | NEED TEST |
| Workbench popup, dropdowns, model editing | Initial modal launcher in source; full 4 dropdowns, selected-element effects and native editor are not implemented | PARTIAL |
| Build/Obsidian runtime test | Source commit only; no built installed plugin or manual Obsidian test evidenced | BLOCK |
| Three-way reimport, conflict/rollback | Plan only | BLOCK |
| Native BOM quantity/UOM writer and configuration effectivity | Proposal and partial read-only tests only | BLOCK for BOM production import |

## Safe execution sequence
1. Freeze source hashes, local private row ledger and versioned rules; ensure baseline archive of test vault.
2. Implement/verify all syntax emitters with synthetic 1-of-each-family fixtures, pinned SysML v2 parser, error-path tests, and YAML/body flagLink.
3. Dry-run all EA 11447 elements and 14688 connectors, then reconcile source counts and synthetic no-loss tests. Preserve model data only locally.
4. Stage generated notes in a separate test vault, not current live main; compare UID uniqueness, role counts, note section placement and unaffected prose.
5. Install plugin only after TypeScript build, test active-note popup, four dropdowns, View selection, editor transactions and flag reviews.
6. Re-run import twice: compare hashes, preserve manually edited prose, prove no duplicate notes/usages or silent overwrites. Exercise Undo and rollback.
7. Only then graduate to reviewed golden import and future BOM source integration. Keep external source-specific data out of Test_Vault_.

## Stop/go
**GO for tool development, synthetic parser fixtures, and local non-destructive dry runs. NO-GO for production import, replacing existing notes, native-validated label, or activating automatic Merge Notes.**

This record supersedes earlier vague readiness descriptions; approved menu taxonomy does not imply menu code is complete.
