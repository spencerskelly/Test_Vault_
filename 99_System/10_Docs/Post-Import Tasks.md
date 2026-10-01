---
uid: 20260928142805000skellyspencer
id: INFO-00021
status: Draft
---
# Post-Import Tasks

Work that has to be done in the vault after the import (stage 2, Workspace Decision Log W-30 and W-37) and before it is released. The vault is not released until every task here is finished (W-55). Each fix is a separate commit, and the reason goes in `99_System/10_Docs/Review Changes Log.md` (W-38). Add new tasks at the bottom as they are decided.

## Task 1: Flow connectors attached to a block instead of a port

**What it is.** In EA some users drew a flow connector (type Connector or InformationFlow) on a block or a Part, when it belongs on a port of that block. The import keeps each connector on the object where it was drawn (W-55) because no rule can choose the port. In the current export 118 connectors are affected: 94 Connectors with no end on a port, 15 Connectors with one end on a port, and 9 InformationFlow connectors with one end on a port.

**Review table (W-156).** The import writes a table of the affected connectors in `99_System/11_Import`, one row per connector keyed by GUID, with the ends as drawn (element, owner, assembly), the notes they resolved to and the candidate Ports on each block end, so no one needs to open EA. The table is `Review - Block-Level Flow Connectors.csv` (name final, W-216), and it replaces the hand-made snapshot below. Its columns are `ea_guid, ea_type, ea_name, category`, then for each end (`start`, `end`) `<end>_element`, `<end>_owner`, `<end>_assembly`, `<end>_note`, `<end>_candidate_ports` (`;` between Port notes), then `connector_values` (Name and Notes joined by ` | `) (W-217). The line on the notes ends with the connector GUID: `REVIEW port needed: Connector <name or unnamed> to [[other end]]: connector {GUID}`.

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

## Task 5: Review the tag lines after the import

**What it is.** Every tag now has a rule (W-29 to W-95): 82 are dropped, 36 become body lines under their EA tag name (W-93), and 3 are structure. Some body lines will become properties (W-94, W-95). This task reviews the imported lines and settles which properties are needed. It also answers the two questions W-87 left open.

**How to find them.** `99_System/03_Schemas/ea-tag-dispositions.yaml` lists every tag and its decision. Search the vault for the line name, for example `Current Max:`. `99_System/CSV_EA/tagvalue_summary.csv` lists every tag with its row count, and `t_objectproperties_all.csv` holds every value, including the `Status` tags that the trimmed `t_objectproperties.csv` leaves out.

**What to check.**
1. Which body lines become properties (the ratings, `SignalType`, and the FMEA scores `Severity`, `Occurence` and `Detection` are the candidates), and their final names. Line names stay as the EA tag names until then (W-93).
2. Whether the `Heading` value of `Object Type` (1,491 elements) is needed to fold headings into document notes (Task 4).
3. Whether the one `Discontinued` requirement should be Retired.
4. The values kept as written that need a check: `Current Max` of `320A` on an A160 part, `x/0` in `Cable Compatibility`, the MoSCoW legend written as a `Webasto MBDV Profile::Priority` line and the format legend in `User Story`, and the unexplained `Style` and `Quantity`.

**How to resolve them.** Decide in groups, log each group in the Decision Log, and change the rules for the next fresh import (W-36, W-37). Record any per-note change in `Review Changes Log.md`, keyed by the element GUID.

**Done when.** Each candidate in item 1 is a property or stays a line, and items 2 to 4 are answered in the log.

## Task 6: Clear the Port review flags

**What it is.** The Port rules of the element mapping leave four kinds of Port for a person to check after the import (W-114, W-122, W-123, W-130). The import writes one fixed line for each in the `Source: EA` section of the Port note. Counts are from the current export and will change if the rules change.

**How to find them.** Search the vault for each line:
- `REVIEW subtypeOf: target port is not on an ancestor block` (146). The `subtypeOf` link follows EA's redefinition link, but the target Port sits on a block with no family link to this one, or on the same block. Confirm it, correct it, or remove it.
- `REVIEW port: added from an assembly, no matching port on the block: port {GUID}` (617). A Part's or Object's Port had no match on its block (no `PDATA3` link and no Port of the same name), so it was added to the block as a Port of its own. `Review - Added Ports.csv` in `99_System/11_Import` (W-157) lists every instance Port folded into the note with its Part and assembly. Its columns are `ea_guid, ea_type, ea_name, category, note, owner, assembly, block_note, block_ports` (W-218); `category` is one of: unnamed instance Port, named and the block has no Ports, named and no match among the block's Ports, named and several Ports on the block have that name. Merge it into an existing Port, rename it, or keep it.
- `REVIEW owner: ActivityPartition has no mapping yet` (42). The Port belongs to an ActivityPartition, which had no mapping when the import ran. Link it to its owner once that element is mapped.
- `REVIEW block: owner Part has no block` (26). The Part that owns the Port has no `PDATA1`, or its block is not in the export, so the Port stayed with the Part. Find the block, or accept the Part as the owner.

**How to resolve one.** Fix the note, delete the line, and add a row to `Review Changes Log.md`, keyed by the Port's EA GUID, saying why. Fix by rule where a group behaves the same, and log the rule in the Decision Log.

**Done when.** A search for each of the four lines finds nothing, and every fixed note has a reason in the log.

## Task 7: Resolve the provisional mappings

**What it is.** Stage 1 is mechanical (W-30), so several mappings are deliberately provisional and kept visible. This task settles them in stage 2, using `eaType` and the package as evidence. The counts are from the current export.

**What to resolve**
1. `modelCheck` notes (666: 632 of 13 small types, subtype = the EA type, and 34 Package notes, W-146, W-147). Decide the type of each group (Step, Functional Flow, Failure Mode, a folded line or something else) and change `type` and `subtype`.
2. Blank or mechanical calls to check from `eaType`: Object from Class (2,314; `Physical Context` 43 stay Objects (W-239), `System Partner` 182 may be Actor, W-139); Design and State from State (954 and 158; the 2 `Fault State` may be Failure Mode, W-142); Function with no stereotype (611, W-141); Verification from `testCase` (527, could be Procedure); Artifact from Document and Image (W-143); the Issue subtype (264, W-144); the 357 Use Cases with a blank subtype (W-140); the Design subtype `characteristic`; the 103 `part` Objects (W-138).
3. The temporary `hasClassifier` links (about 1,620: Port `Classifier` 443, Port typing not to a Port note 99, Object `Classifier` 498, FlowProperty typing 524, and 64 on Use Cases, ActivityPartitions, Actions and a Sequence; W-125, W-127, W-135, W-132, W-180). Turn each into `copyOf`, `hasPart`, `subtypeOf` or another link, then remove the pair.
4. `hasChild` (about 19,600 links from placement after W-178 removed the 781 that repeat a generalization, plus about 1,100 from connectors; W-149). Keep it, or replace it on a pair with a more precise link (a requirement decomposition, a comment link). Requirement under Requirement is 70% of them.
5. The 252 `REVIEW nesting direction` lines (independent `Nesting` connectors written as `hasChild`/`childOf`, W-151; 200 add a parent that placement never showed, 52 give a child a second parent). Each line holds the connector GUID (W-152), the key to its row in `Review - Nesting Direction.csv` in `99_System/11_Import`, which holds both ends as drawn (W-157). Its columns are `ea_guid, ea_type, ea_name, category, start_element, end_element, start_note, end_note, link_written, child_other_parent, diagrams` (W-219). Check the direction, fix or remove the link, and remove the line.
6. The `REVIEW subtypeOf: the two notes have different types` lines (W-152): 88 Generalization connectors, 87 links, on 81 notes, mostly Port and Object (39) and Function to Object (30). Decide for each whether it is a real "kind of" link, needs a different link (for example `hasPart` or `realizedBy`) or goes, and remove the line.
7. Shared aggregations are written as `includes` (W-159, amended by W-277), among them the countries grouped into market regions (278 connectors, `block` to `System Partner`) and about 30 real shared parts (Hardware Component and Module pairs). The membership link for regions is now `includes`. Decide whether the real shared parts become `hasPart` or stay `includes`.
8. Physical Context participation (W-139, W-159, W-237, W-239): no action. A Physical Context stays an Object block with its parts (`hasPart`, `hasChild`), as for any block; the Context class was removed in W-237.
9. `REVIEW hasChild: the two notes have different types` (W-159, W-171): 23 Aggregation links on 15 notes and 1 Use Case include to an Object. Decide the right link for each and remove the line.
10. `REVIEW modelCheck: realization` (W-160, W-167): 32 Realisation links on 29 notes kept as `realizedBy`/`realizes` because they fit neither `appliesTo` (an Object and a Requirement, either direction) nor Function to Use Case, 7 of them from a Package folder with no note. Decide the right link for each (for a Function or Design to a Requirement, `satisfies`), and remove the line.
11. `REVIEW modelCheck: satisfy` (W-163): 112 `satisfies` links on 89 notes whose source is not a Function or a Design, 92 of them from a State. Where the State is a design characteristic make it a Design note; otherwise decide the right link, and remove the line. `REVIEW modelCheck: deriveReqt` (W-164): 6 `derivedFrom` links that are not between two requirements; the same handling. `REVIEW modelCheck: refine` (W-165): 17 `refines` links on 16 notes that fit none of the refine rules, mostly from Info notes; the same handling. `REVIEW modelCheck: trace` (W-166): 102 `tracesTo` links on 82 notes that fit none of the trace rules; the same handling. `REVIEW modelCheck: verify` (W-168): 8 `verifies` links on 7 notes not from a Verification to a Requirement; the same handling. `REVIEW modelCheck: RecoveryRequirement` (W-168): 14 `satisfies` links on 13 notes that came from a RAAML recovery analysis; decide whether the recovery meaning needs its own link or a line, and remove the line. `REVIEW modelCheck: ASILDecompose` (W-168): 4 `derivedFrom` links whose direction the data does not show; confirm which requirement is decomposed, and remove the line. `REVIEW modelCheck: dependency` (W-169): 115 `dependsOn` links on 95 notes from Dependencies with no stereotype that fit no other rule (Design to Design and Object to Object most); decide the right link, and remove the line. `REVIEW modelCheck: allocate` (W-170): 180 `tracesTo` links on 123 notes from EA allocations that fit no rule (modelCheck to Issue 44, State to Object 26 and others); decide the right link, and remove the line. `REVIEW modelCheck: Derive` (W-170): 1 `derivedFrom` link from a Requirement to an Issue; the same handling. `REVIEW modelCheck: association` (W-172): 102 `tracesTo` links on 65 notes from EA Associations with no direction or clear meaning (Object to Object 72 most); decide the right link, and remove the line. `REVIEW modelCheck: usage` (W-173): 8 `dependsOn` links on 6 notes, among them the 4 `Responsibility` links; the same handling.
12. Long inverse lists (W-178, W-179): after the import, look at the notes with the longest generated lists (`applies` up to 133 on `SW PCE25 CTRL`, `supertypeOf` up to 127 on `lsWarning`) and decide whether any field becomes one-way, like `participants` (W-172).
13. Use Case include written as `hasChild` (W-278): 473 new links from EA Use Case include (W-171). EA modeling did not separate ownership from membership. For each link decide: `hasChild` where the base Use Case owns the included one, `includes` where the included Use Case is shared by several bases. Both relationships are allowed between Use Cases until then.

**How to resolve them.** Decide in groups, log each group in the Decision Log, and change the rules for the next fresh import (W-36, W-37). Record any per-note change in `Review Changes Log.md`, keyed by the element GUID.

**Done when.** Nothing has type `modelCheck`, `hasClassifier` is gone, no review line named in items 5, 6, 9, 10 and 11 remains, and each group above has a log entry.

## Task 8: Update the `equals` relationships

**What it is.** In EA a `BindingConnector` joins two ports. Stage 1 writes each one as the symmetric field `equals` on both end notes (W-153), because that is what the connector says and it keeps the import mechanical (W-30). What Spencer means by it is that one port is also exposed at a higher layer: a circuit's antenna port, the PCBA's antenna port and the product's antenna port are the same antenna at different levels. That is a direction (outer and inner), so `equals` is replaced in stage 2 by a directional pair. The name is not fixed; the working proposal is `exposes` on the outer Port and `exposedBy` on the inner Port (`extends` is not used, because it already means UML extend and inheritance). The counts are from the current export.

**What to resolve.** 249 BindingConnectors. The import derives a direction for 245 of them and writes it in the review table (W-156): 185 from one level of containment, 60 more by following containment over several levels (not yet spot-checked); 4 have no containment path and need a decision.
- 185 have a clear inner and outer end: one end is a Port of an assembly block, the other is a Port of a Part inside that block (99 drawn inner to outer, 86 outer to inner, so the connector's order says nothing). Direction comes from that structure.
- 64 have no such structure and need a decision one by one: 17 join Parts in different assemblies, 29 involve an Object (Part and Object 15 and 14), 10 join two Objects, 7 join an Object and a Class, and 1 joins two Parts of the same assembly. Some may not be exposures at all and become `interfaces`.
- After the Port merge (W-114) the inner end is the block's own Port. 17 of the 154 inner block Ports connect to more than one outer Port, because the block is used in several assemblies, so the fields are lists. The assembly and Part context of each connector is kept on the line still to be defined (W-114), and it says which instance was wired to which outer Port.

**How to find them.** Search the properties for `equals`. The review table `Review - Equals Direction.csv` in `99_System/11_Import` (W-156, W-157) lists the 249 connectors by GUID with both ends as drawn and the derived outer and inner Port. Its columns are `ea_guid, ea_type, ea_name, category, start_element, start_owner, start_assembly, end_element, end_owner, end_assembly, start_note, end_note, derived_outer_note, derived_inner_note, containment_path, connector_values` (W-220); `category` is one level of containment (185), several levels (60) or no containment path (4).

**How to resolve one.** Decide which Port is outer and which is inner (assembly containment, or the context line). Write `exposes` on the outer Port and let `exposedBy` be generated on the inner one (the pair is in `relationships.yaml`, W-281), or change the pair to `interfaces` when it is not an exposure. Remove `equals` from both notes. Record the reason in `Review Changes Log.md`, keyed by the connector GUID, and log the naming decision in the Decision Log once.

**Done when.** No note has an `equals` field, and the name of the directional pair is logged.
