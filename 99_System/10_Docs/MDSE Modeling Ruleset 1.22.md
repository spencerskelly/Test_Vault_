# MDSE Modeling Ruleset 1.22

## Status

Current modeling ruleset for the MDSE vault. Reissued from 1.21 (W-260): the cross-vault sections, `instanceOf` and the `control` and `boundary` note are removed; section numbers are kept so that references still resolve. The rules the translator follows are in `Translator Definition.md`.

## 1. Model meaning before structure

Classify the concept semantically before choosing a type. Search for an existing authoritative definition before creating a new one. Prefer reuse, then instance, true specialization, decomposition, and only then a new independent concept.

Folder placement is navigation only.

## 1.1 Type and subtype nomenclature

The primary reusable engineering-entity type is **Object**. The former top-level type name `Thing` is deprecated.

`Object` may represent physical hardware, software, firmware, or other reusable engineering entities according to its approved subtype. In translator material, use **EA Object** for the Sparx EA metaclass and **MDSE Object** for the MDSE type whenever ambiguity is possible.


Every model note (a note made from a class template in `99_System/05_Templates`) uses `type` for its primary MDSE semantic class and `subtype` for an approved specialization/classification within that type.

Notes in `99_System` are reference and system notes and carry no `type` or `subtype` (W-243).

The former property name `kind` is deprecated and must not be used in new notes.

`subtype` as a property is distinct from the semantic `subtypeOf / supertypeOf` relationship. Use the relationship only for true reusable generalization between modeled elements.

## 2. Generalization

Use `subtypeOf` only for a reusable invariant semantic distinction. Where the difference is ordinary data or configuration, it is not a `subtypeOf`; there is no `instanceOf` field (W-184).

## 3. Product control

Removed in 1.22. `control` and `boundary` are not properties of a note (W-88, W-112).

## 4. Relationships

Author only the forward/owner-side relationship. Paired/symmetric inverses are generated derivative YAML and must be synchronized before handoff.

The same semantic relationship vocabulary applies across vault boundaries.

## 5. Function vs Use Case

Function = behavior controlled by the modeled product.

Use Case = externally controlled behavior/scenario/actor goal.

Do not convert human/external-system steps into product Functions merely because they appear in a journey.

## 6. Evidence and uncertainty

Do not silently fill missing source information. Preserve ambiguity and create a model check when required.

## 7. Requirements

Requirement `appliesTo` defines scope. Function and Design may use `satisfies`. Verification uses `verifies`.

## 8. Verification

Verification defines reusable intent; Procedure orders activities; Setup defines capability; Plan selects campaign content; Result records execution evidence.

## 9. Navigation

Every model-facing folder contains:

- `00 - Views and Bases.md`
- `00 - Folder Contents.base`
- `00 - Folder Map.canvas`

Keep fewer than 25 modeled elements in an immediate folder when a durable semantic split exists. Do not create arbitrary overflow folders.

## 10. Company/domain authority

Removed in 1.22. The vault is one vault with no cross-vault links (W-01).

## 11. Cross-vault identity

Removed in 1.22 (W-01). Every note still has an immutable 30-character `uid` (W-13); its format is in `AI_INSTRUCTIONS.md`.

## 12. Vault creation and splitting

Users create new vaults; AI does not autonomously create or split them.

When scale, access, lifecycle, ownership, search quality, or AI context becomes problematic, AI may recommend that the user consider splitting a vault.

## 13. Cross-vault views

Removed in 1.22 (W-01).

## 14. Integrity before handoff

The checks a translator run must pass are in `Translator Definition.md` section 10. For hand-made work before handoff: YAML parses; ids and uids are unique; links resolve; inverses are synchronized; Functions have performers where applicable; requirement basis, satisfaction and verification gaps are visible.

