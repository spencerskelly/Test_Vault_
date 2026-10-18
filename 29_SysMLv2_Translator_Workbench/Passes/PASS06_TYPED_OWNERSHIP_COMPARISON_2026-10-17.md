# Pass 6 — Reduced QEAX typed ownership comparison (2026-10-17)

## Local read-only result

The new conservative typed ownership classifier was reconstructed locally and applied to the reduced QEAX (14,688 connectors; 2,267 Aggregations). Aggregation outcome: 154 typed composite-owner **candidates**, 2,064 incompatible or not-yet-recognized endpoint kinds, 12 port/interface reviews, 37 shared/ambiguous ownership reviews. These sum to 2,267. A further 12,377 connectors are non-Aggregation; 44 self-referencing connectors were intercepted before family classification. Thus overall totals remain 14,688.

The previous Phase 8 normalized result reported 1,408 owner-endpoint-identification candidates. Difference: **1,254**. This is primarily a **taxonomy coverage difference**, not evidence of 1,254 invalid source relationships. The strict classifier recognizes only `Class «block»`, `Object` and `Part` as part-like, while the reduced EA uses numerous `Class` stereotypes including `Hardware Component`, `Module`, `Physical Component` and `Physical System Variant`. Among 2,064 unrecognized/incompatible Aggregations, 1,734 are Class–Class; another 148 Activity–Activity and 76 State–State need their respective nested action/state-usage treatment and should **not** become part usage. Other stereotypes include `System Partner` and context classifications, which must not be swept into PartDefinition by default.

No model-specific GUIDs, source record IDs or ledger were committed. Categories are aggregate-only. Native certified = 0.

## Policy decision and next action

The audit confirms the narrower classifier is conservative. Do **not** modify the actual semantic eligibility rules based on stereotype labels alone. Create a reviewed versioned source stereotype classification table (EA source concept -> canonical Definition/Usage or deferred) with Workbench structural/visual representation, containment/connection, navigation, validation and provenance obligations. Then rerun the comparison by reconciled source type and aggregation-end orientation; separately preserve nested State/Activity semantics and distinguish real full/proxy ports.

Exact committed Python synthetic tests and integration tests were not executed from the full checkout. This local execution used equivalent reconstructed classifier code, not the checked-out module. Release acceptance remains pending.
