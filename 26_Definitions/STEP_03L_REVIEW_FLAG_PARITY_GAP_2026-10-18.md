# STEP-03L — Flag parity and Workbench review gap

Date: 2026-10-18

STEP-03K local execution retained 11,447 nodes and 14,688 edges. Its zero flags reflect no unmatched approved *family keys*; this is not evidence of resolved row-level semantics or attachment ownership.

## Verified existing contracts

- STEP-03J stores unknown connector family records as an explicit `flagLink` property (array).
- STEP-03B graph gate counts links only by connector `type == "flagLink"` or review-like `disposition`.
- `24_Workbench/v2-flag-review.js` likewise reads review-like `disposition` and `type`, but not explicit `flagLink`.
- The existing flagNotes patcher `25_Testing/v2_step03c_stage_attachment_flags.py` expects a verified JSONL ledger containing `node_id` and `flagNote`; it rejects unmatched node IDs and conflicting preexisting values.

## Acceptance fix required

Count and display any nonempty `edge.flagLink`, including lists, without double counting a single flagged edge through legacy fields. Keep flagNote list handling intact. Add tests for both explicit and legacy forms, preservation of reviewed content, and malformed/duplicate graph IDs. Workbench flag filter must navigate to the affected edge/node, not merely show aggregate counts.

Attachment flags must come from verified attachment ownership. Never manufacture 144 flags solely to meet the historical aggregate gap. Flag provenance and source identifiers must be preserved. Unresolved conditional native candidate status must be evaluated using approved row-level evidence; do not treat family-coverage status as SysML semantic validation.

### Next controlled action

1. Implement and test explicit `flagLink` recognition in the review gate and Workbench.
2. Reconcile source-identified attachment flags; feed them through STEP-03C to a separate staged output.
3. Execute STEP-03B parity gate with independent, identity-grounded expected values.
4. Load both local JSONL files into Workbench and verify search, select, navigation, flag visibility and no data loss.
5. Keep diagrams excluded. No generated per-record data or private QEAX in GitHub.

This document records a **known gap**, not completed STEP-03L browser acceptance.
