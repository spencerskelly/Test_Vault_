# STEP-03J — Approved family review staging (2026-10-18)

The staged annotation tool is committed to main:
- `25_Testing/v2_step03j_approved_family_annotation.py`
- `25_Testing/test_v2_step03j_approved_family_annotation.py`

## Contract

Consume read-only STEP-03H `nodes.jsonl` and `edges.jsonl`, load **existing** `21_Importer/v2_approved_family_resolver.py` and approved `24_Workbench/registry/sysml_v2_approved_family_resolver.v0.1.json`. Add `approvedFamilyReview` per node/edge with resolver disposition and evidence requirements. Preserve complete original source fields. Unknown element families receive `flagNote`; unknown connector families receive `flagLink` (existing lists retained). Exact approved matches remain **native-uncertified**; this tool does not issue native SysML text or invent relationships, resolve conditional evidence, or classify a whole family as parser accepted. Diagrams are excluded by registry and tool.

The output is a new local directory containing `nodes.jsonl`, `edges.jsonl` and `annotation_summary.json`. Do not commit row-level graph data.

## Local commands

```bash
python3 -m unittest discover -s 25_Testing -p 'test_v2_step03j_approved_family_annotation.py' -v
python3 25_Testing/v2_step03j_approved_family_annotation.py \
  /private/raw-graph/nodes.jsonl /private/raw-graph/edges.jsonl \
  /private/new-empty-annotated-graph
```

Then run STEP-03B structural/flag parity against the staged data, but calculate the review count from the same source snapshot and independently check original attachment flag identities; annotations for unknown family kinds **do not replace** the 144 unresolved attachment ownership flags. The prior 159 expected flagNotes was from a different graph representation, not an invariant for this new output.

## Remaining gates

- Execute synthetic tests on user Mac, then real full reduced QEAX via STEP-03H → STEP-03J.
- Restore verified attachment review ledger flags via STEP-03C, preserving their per-row identity.
- Implement row-level directional and conditional-evidence decisions from approved registry without adding custom SysML syntax; allow unresolved links/notes as review flags.
- Validate Workbench actual browser loading, performance, source provenance and flag navigation.
- Verify native SysML parser output separately after semantic translation.
- No diagrams until tool completion and golden import.

**Not a golden import and not yet the complete semantic translator.**
