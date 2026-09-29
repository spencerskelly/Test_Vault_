---
uid:
type: Info
status: Working
workspace: EA Native Translator
---
# MDSE Type and Subtype Taxonomy

## Nomenclature

MDSE uses:

- **type** — primary semantic element class, such as `Object`, `Requirement`, or `Function`;
- **subtype** — approved specialization/classification within that type.

The former property `kind` is deprecated. The former top-level MDSE type `Thing` is renamed to `Object`.

## Authoritative taxonomy

| MDSE type | Prefix | Folder | Approved subtypes |
|---|---|---|---|
| Object | OBJ | `10_Objects` | `electrical`, `circuit`, `mechanical`, `software`, `firmware` |
| Port | PORT | `20_Ports` | `electrical & material`, `data`, `mechanical`, `generic physical`, `environmental`, `proxy`, `full` |
| Item Flow | IFLOW | `21_Item_Flows` | `information`, `energy`, `material` |
| Context | CTX | `25_Contexts` | — |
| Function | FUNC | `30_Functions` | `system`, `hardware`, `software`, `module` |
| Functional Flow | FFLOW | `31_Functional_Flows` | — |
| State | STATE | `35_States` | — |
| State Machine | SM | `36_State_Machines` | — |
| Transition | TRANS | `37_Transitions` | — |
| Requirement | REQ | `40_Requirements` | `functional`, `design`, `standard`, `stakeholder`, `engineering` |
| Design | DES | `41_Designs` | `characteristic`, `decision` |
| Use Case | UC | `45_Use_Cases` | `what`, `where`, `why`, `when` |
| Actor | ACT | `47_Actors` | — |
| Failure Mode | FM | `50_Failure_Modes` | — |
| Issue | ISS | `51_Issues` | `engineering issue`, `lifecycle risk` |
| Info | INFO | `55_Info` | `need`, `objective`, `concern`, `decision`, `assumption`, `rationale`, `finding`, `analysis`, `trade study`, `calculation`, `milestone`, `lesson learned` |
| Step | STEP | `60_Verification/01_Steps` | — |
| Verification | VER | `60_Verification/02_Verifications` | `test`, `analysis`, `inspection`, `demonstration` |
| Procedure | PROC | `60_Verification/03_Procedures` | `test`, `assembly`, `configuration`, `commissioning`, `calibration`, `maintenance`, `repair`, `decommissioning` |
| Setup | SETUP | `60_Verification/04_Setups` | — |
| Plan | PLAN | `60_Verification/05_Plans` | — |
| Result | RES | `60_Verification/06_Results` | — |
| Document | DOC | `70_Documents` | `standard`, `specification`, `report`, `drawing` |
| Artifact | ART | `71_Artifacts` | `image`, `document` |

## EA Object distinction

EA's source metaclass `Object` is **EA Object**. The target MDSE type is **MDSE Object**. Matching names do not imply automatic identity or conversion.
