# Phase 9 — Nested generalization endpoint audit

Read-only QEAX structural check of the October 15 reduced source: 1,677 same-stereotype generalization candidates include 16 nested endpoint appearances across 8 unique EA elements. Source appearances 9 and target appearances 7; all nested endpoints occur in Hardware Component relationships. Counts of appearances and unique elements must not be confused.

The QEAX provides `ParentID`, `Classifier`, `Classifier_guid`, and extended stereotype records in `t_xref`. A parent reference is **not** sufficient evidence of SysML v2 part usage; a nested definition may still be legitimate. An absent classifier is likewise not sufficient proof of definition semantics.

Added an aggregate-only tool to distinguish unique nested endpoint elements, source/target appearances, parent EA kinds/stereotypes, optional classifier links and extended-stereotype record presence without exporting private IDs or names. Three synthetic regression tests committed; execution not yet independently observed.

Operator commands:

```sh
git pull --ff-only origin main
python3 -m unittest -v 15_Testing/test_phase9_nested_generalization_evidence.py
python3 15_Testing/phase9_nested_generalization_evidence.py --qeax "$HOME/Documents/Vaults/Engineering_Data/EA_2026_10_15_endgame_mini.qeax"
```

Workbench rule: structural ownership and subtype links remain separate; visual specialization cannot imply a part usage merely because `ParentID` is populated. Preserve navigation, source provenance and independent syntax/semantic validation. Binding Port and port-as-part semantics remain distinct. No native certification or emitter authorization.
