---
uid: 20260928142805000skellyspencer
id: INFO-00021
type: Info
subtype: Guide
status: Draft
---
# Post-Import Tasks

Work that has to be done in the vault after the import (stage 2, Workspace Decision Log W-30 and W-37) and before it is released. The vault is not released until every task here is finished (W-55). Each fix is a separate commit, and the reason goes in `99_System/10_Docs/Review Changes Log.md` (W-38). Add new tasks at the bottom as they are decided.

## Task 1: Flow connectors attached to a block instead of a port

**What it is.** In EA some users drew a flow connector (type Connector or InformationFlow) on a block or a Part, when it belongs on a port of that block. The import keeps each connector on the object where it was drawn (W-55) because no rule can choose the port. In the current export 118 connectors are affected: 94 Connectors with no end on a port, 15 Connectors with one end on a port, and 9 InformationFlow connectors with one end on a port.

**How to find them.**
- Search the vault for `REVIEW port needed`. The import writes that line in the `Source: EA` section of both end notes of each affected connector.
- `99_System/11_Import/Block-Level Flow Connectors.csv` lists the 118 by connector GUID, with the two ends, how many ports each end has available, and a category. It is a snapshot made from the current export; the ledger from the accepted import run (W-35) replaces it.

**Categories in the snapshot.**
- Choose port (74): at least one block-level end has several ports, or one end has none while the other has several. A person picks the port.
- Create ports (38): no port exists on the block-level ends. The port has to be created first.
- Single candidate at each block-level end (5): one obvious port per end. Confirm and move.
- End missing from the export (1): the connector points at an element that is not in the export. Find out what it should join.

**How to resolve one.**
1. Open both end notes and the connector's values (Name, Notes) in their `Source: EA` sections.
2. Decide which port on each block-level end carries the flow, or create it using the port structure set in the element mapping.
3. Move the connector to the ports, and keep its values on both ends, as for any flow connector.
4. Delete the `REVIEW port needed` line on both notes.
5. Add a row to `Review Changes Log.md`, keyed by the connector GUID, saying why that port was chosen.

**Done when.** A search for `REVIEW port needed` finds nothing, and every row of the snapshot is either moved or has a reason in the log.

## Task 2: Third-party standards content in attachments

**What it is.** The import brings in every linked document from EA as an attachment (W-76), including RTF documents and pictures that look like figures and tables from standards (for example `Figure 7.5 Example of a Bottom-Enclosure`, `Table 7.4 Comparative Tracking Index`, `1 Scope`, `5 Definitions`). Whether the vault may hold this content has not been decided.

**How to find them.** `99_System/11_Import/Linked Document Attachments.csv` lists all 376 linked documents with the element they are attached to, the element type, whether the content is text, pictures or an image, and the size. The 235 Artifacts of subtype Document and the 11 design-constraint requirements hold the picture and text documents; the 129 Artifacts of subtype Image hold circuit images that are your own work. Attachment files sit in the same folder as their note and are named `<note file name> asset <n>` (W-77), so a search for `asset` lists them. It is a snapshot from the current export; the ledger from the accepted run (W-35) replaces it.

**How to resolve it.**
1. Decide which documents are third-party content and which are yours.
2. For third-party content that may not stay, remove the attachment and its embed, and add a row to `Review Changes Log.md` keyed by the document's element GUID.
3. Before release, check the git history. Files committed in the baseline import stay in history after removal, so a removal may need a history rewrite.

**Done when.** Every row of the snapshot is kept or removed with a reason in the log, and the history question is settled.

## Task 3: Convert `Universal BMID Product Reqs` into note text

**What it is.** The import attaches the linked document `Universal BMID Product Reqs` (19,277 characters) unchanged as an `.rtf` file (W-78). It looks like your own requirements, so the text should be readable and searchable in the vault, which an RTF attachment is not.

**How to find it.** Search for `Universal BMID Product Reqs`, or open the row in `99_System/11_Import/Linked Document Attachments.csv` (`Content` is `text`, `Text_Chars` is 19,277).

**How to resolve it.**
1. Open the `.rtf` attachment and check the text is yours to publish (Task 2).
2. Convert it to Markdown and put it in the main text of the note it is attached to, as a reviewed commit.
3. Keep the `.rtf` attachment or remove it, and add a row to `Review Changes Log.md` keyed by the document's element GUID.

**Done when.** The text is in the note and searchable, and the log row exists.

## Task 4: Fold unconnected standard and stakeholder requirements into document notes

**What it is.** The import brings in every requirement as its own note (W-81). The earlier plan, and W-16, fold clauses that no other element connects to into the note of their standard or stakeholder document. That is now done here, after the import.

**How to find them.** In `99_System/CSV_EA/requirement_connectivity_audit.csv`, requirements with `Direct_Connectors` and `Child_Connectors` both 0: 9,788 rows in the current export (`requirement` 5,221, `Regulatory Requirement` 3,155, `Webasto Requirement` 1,363, and a few others). Of these, 817 are drawn on a diagram and 7,491 have a note, so check those before folding. The handoff counted 10,052; the two figures are not reconciled. It is a snapshot; the ledger from the accepted run (W-35) replaces it.

**How to resolve them.**
1. Decide which documents fold and which clauses stay as notes, for example a clause drawn on a diagram or with tagged values worth keeping.
2. Fold in batches, one reviewed commit per document. Put the clause text in the document note under a clause anchor.
3. Retire the folded note (`status` Retired), do not delete it (W-18). Its `id` stays reserved and links to it keep working.
4. Add a row to `Review Changes Log.md` for each batch, keyed by the document.

**Done when.** Every unconnected requirement is either folded, with its note retired and the clause anchor in place, or kept with a reason in the log.

## Task 5: New analysis of the tagged values

**What it is.** Four tags were dropped without carrying anything into the notes (W-87): `Status`, `Webasto MBDV Profile::Status`, `Object Type` and `Webasto MBDV Profile::Object Type`. 36 other tags are still undecided and default to a line in the source section below the GUID (W-29). Spencer decided to run a new analysis on the imported vault before settling them.

**How to find them.** `99_System/CSV_EA/tagvalue_summary.csv` lists every tag with its row count, and `t_objectproperties_all.csv` holds every value, including the `Status` tags that the trimmed `t_objectproperties.csv` leaves out. `99_System/03_Schemas/ea-tag-dispositions.yaml` shows which tags are decided.

**What to check.**
1. Whether the `Heading` value of `Object Type` (1,491 elements) is needed to fold headings into document notes (Task 4).
2. Whether the one `Discontinued` requirement should be Retired.
3. For each of the 36 pending tags, whether its values are worth a body line or a property, or should be dropped.

**How to resolve them.** Decide the tags in groups, log each group in the Decision Log, and change the rules for the next fresh import (W-36, W-37). Record any per-note change in `Review Changes Log.md`, keyed by the element GUID.

**Done when.** No tag is `pending` in `ea-tag-dispositions.yaml`, and the two checks above are answered in the log.
