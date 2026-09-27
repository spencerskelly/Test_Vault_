---
uid:
type: Info
status: Working
workspace: EA Native Translator
---
# MDSE Type and Subtype Taxonomy

## Nomenclature

MDSE uses a two-level classification vocabulary:

- **type** — the primary semantic element class, such as `Thing`, `Requirement`, or `Function`.
- **subtype** — an approved reusable specialization/classification within that type, such as `Thing / electrical` or `Requirement / functional`.

The former property name `kind` is deprecated. New and migrated notes use `subtype`.

This property nomenclature is distinct from the semantic relationship `subtypeOf / supertypeOf`, which remains the relationship used for true reusable generalization between modeled elements.

## Authoritative taxonomy

| MDSE type | Prefix | Folder | Approved subtypes |
|---|---|---|---|
| Thing | THG | `10_Things` | `electrical`, `circuit`, `mechanical`, `software`, `firmware` |
| Interface | INT | `20_Interfaces` | `electrical & material`, `data`, `mechanical`, `generic physical`, `environmental` |
| Item Flow | IFLOW | `21_Item_Flows` | `information`, `energy`, `material` |
| Context | CTX | `25_Contexts` | — |
| Function | FUNC | `30_Functions` | `system`, `hardware`, `software`, `module` |
| Functional Flow | FFLOW | `31_Functional_Flows` | — |
| State | STATE | `35_States` | — |
| State Machine | SM | `36_State_Machines` | — |
| Transition | TRANS | `37_Transitions` | — |
| Requirement | REQ | `40_Requirements` | `functional`, `design`, `standard`, `stakeholder` |
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

## Translator rule

A translator may create a `subtype` value only when the source semantics match an approved subtype above or an explicit methodology amendment adds a new subtype. Source stereotypes do not automatically expand this taxonomy.
