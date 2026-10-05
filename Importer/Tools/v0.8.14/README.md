# EA to MDSE Native Importer v0.8.14

v0.8.14 builds on v0.8.13 and implements W-380. It does not change Local Model 0.3 semantics.

## Change

The v0.8.13 planner already marked note-level connectors touching a W-377 definitionless contextual endpoint as review-only, but the generic semantic-review CSV did not persist the planner's detailed reason. That made the evidence weaker than the in-memory plan.

v0.8.14 closes that audit gap:

- `Review - Definitionless Local Endpoints.csv` adds `source_object_id` for the exact EA Port row.
- `Review - Semantic and Connectors.csv` now persists the connector planner's `detail` text.
- A W-377 connector review row therefore retains the `localendpoint:<Object_ID>` endpoint key plus the explicit reason that the note-level relationship is review-only while supported occurrence topology remains in the Local Model.

No canonical relationship mapping, Local Model record shape, Port-resolution rule, identity rule, or Workbench requirement changes.

## Acceptance support

`Importer/Testing/v0.8.14/imp009_output_acceptance.py` validates a completed whole-model output by cross-checking:

- Import State and Run Manifest version/schema/counts;
- definitionless endpoint review rows against Local Model Source Map;
- actual Markdown endpoint blocks (present, schema 0.3, no `definition`, no `usage`);
- local block-link resolution and definitionless endpoints used by connections where present;
- W-377 connector review evidence against exact definitionless EA Port Object IDs;
- absence of legacy `Review - Added Ports.csv` and `portgroup:` evidence.

The script intentionally leaves the final Workbench read/edit interaction as a separate manual/integration acceptance item.

## Validation required

- v0.8.14 static/source/syntax check.
- Run the output acceptance validator on a fresh real-QEAX whole-model import.
- Open that same vault with the pinned Workbench 0.1.17 candidate and prove Local Model 0.3 read/navigation/edit/reload on a definitionless endpoint.

IMP-009 remains `test required` until those real-source and Workbench gates pass.
