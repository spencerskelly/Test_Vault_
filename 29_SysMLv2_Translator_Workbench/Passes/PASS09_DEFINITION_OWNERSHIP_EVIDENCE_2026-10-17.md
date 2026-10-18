# Phase 9 — Generalization endpoint definition/ownership evidence

Read-only audit of reduced October 15 QEAX. Exactly 1,677 same-stereotype, same-EA-kind generalizations in Hardware Component (767), Logical Signal (579), Physical Component (181), Module (150).

Both endpoints lack populated Classifier and Classifier_guid for every candidate edge. ParentID populated on 9 source endpoint appearances and 7 target appearances. IsSpec=0 and Abstract=0 on both endpoints of every candidate. These are **endpoint appearances** per edge, not unique element counts.

The absence of classifier linkage does not prove a definition. ParentID signals nesting, but not necessarily usage or containment in SysML v2. Abstract=0 is not evidence against specialization. No automatic promotion from any of these fields.

Added `15_Testing/phase9_definition_ownership_evidence.py` with aggregate-only output and six synthetic tests. Native certification remains zero. No source records, element names, private IDs or GUIDs are printed or committed.

Workbench follow-up: render provisional definition specialization separately from hierarchy nesting, typed usages, instances and redefinitions. Both visual and structural views must show reason-for-review, navigate endpoint definitions and carry source evidence and round-trip information locally. Avoid collapsing Binding Port, part-as-port and owner/connection semantics.

Local verification:

```sh
git pull --ff-only origin main
python3 -m unittest -v 15_Testing/test_phase9_definition_ownership_evidence.py
python3 15_Testing/phase9_definition_ownership_evidence.py --qeax "$HOME/Documents/Vaults/Engineering_Data/EA_2026_10_15_endgame_mini.qeax"
```

Next: compare endpoint classifier, ParentID, t_xref stereotypes and tagged definition/instance conventions; isolate 9/7 nested endpoint appearances in a **private local** review, without copying identifiers to GitHub. Official SysML v2 semantic validation still pending; native emission disabled.