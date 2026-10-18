# Phase 9 — Reduced QEAX generalization endpoint review distribution

Date: 2026-10-17. Read-only local source audit of reduced QEAX; only aggregate counts committed.

The expanded conservative Phase 9 matrix produced 3735 generalizations, 204 same-family candidates, and 3531 endpoint-kind review cases. All 3531 review cases have raw EA direction `Source -> Destination`; review is about semantics, not missing direction metadata.

| Review type pair | Count |
|---|---:|
| Class→Class | 1788 |
| Activity→Activity | 615 |
| Signal→Signal | 579 |
| State→State | 245 |
| UseCase→UseCase | 216 |
| Object→Class | 45 |
| Requirement→Requirement | 26 |
| Actor→Actor | 12 |
| Issue→Issue | 2 |
| Trigger→Trigger | 2 |
| State→Activity | 1 |
| Total | 3531 |

High-volume stereotype pairs include Hardware Component→Hardware Component (767), Logical Signal→Logical Signal (579), System State→System State (218), UseCase→UseCase (216), System Function→System Function (187), Physical Component→Physical Component (181), Module→Module (150), Activity empty→System Function (112), Data Interface→Electrical & Material Interface (108).

Interpretation: Same EA source stereotypes might indicate reusable native definitions, but can also represent usage, shared data semantics, or ill-modeled generalization. They must be reviewed against the approved EA→SysML v2 mapping before broadening the eligibility matrix. In particular maintain Binding Port, full ports as parts, port usages, semantic subtype and redefinition distinctions. Do not approve all `Class`→`Class` generalizations wholesale.

Added `15_Testing/phase9_generalization_endpoint_distribution.py` and synthetic tests to reproduce this aggregate-only distribution. Run:

```sh
git pull --ff-only origin main
python3 -m unittest -v 15_Testing/test_phase9_generalization_endpoint_distribution.py
python3 15_Testing/phase9_generalization_endpoint_distribution.py --qeax "$HOME/Documents/Vaults/Engineering_Data/EA_2026_10_15_endgame_mini.qeax"
```

Next pass: group candidate same-stereotype pairs into native semantic definitions for explicit review. Include Workbench hierarchy, visual graph, navigation, validation, and round-trip provenance. Native emission disabled.