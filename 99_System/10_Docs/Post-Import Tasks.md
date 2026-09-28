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

**How to find them.** `99_System/11_Import/Linked Document Attachments.csv` lists all 376 linked documents with the element they are attached to, the element type, whether the content is text, pictures or an image, and the size. The 235 Artifacts of subtype Document and the 11 design-constraint requirements hold the picture and text documents; the 129 Artifacts of subtype Image hold circuit images that are your own work. It is a snapshot from the current export; the ledger from the accepted run (W-35) replaces it.

**How to resolve it.**
1. Decide which documents are third-party content and which are yours.
2. For third-party content that may not stay, remove the attachment and its embed, and add a row to `Review Changes Log.md` keyed by the document's element GUID.
3. Before release, check the git history. Files committed in the baseline import stay in history after removal, so a removal may need a history rewrite.

**Done when.** Every row of the snapshot is kept or removed with a reason in the log, and the history question is settled.
