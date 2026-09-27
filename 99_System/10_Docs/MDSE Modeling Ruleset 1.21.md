# MDSE Modeling Ruleset 1.21

## Status

Current reusable modeling ruleset for new Ampure vaults.

## 1. Model meaning before structure

Classify the concept semantically before choosing a type. Search for an existing authoritative definition before creating a new one. Prefer reuse, then instance, true specialization, decomposition, and only then a new independent concept.

Folder placement is navigation only.

## 1.1 Type and subtype nomenclature

The primary reusable engineering-entity type is **Object**. The former top-level type name `Thing` is deprecated.

`Object` may represent physical hardware, software, firmware, or other reusable engineering entities according to its approved subtype. In translator material, use **EA Object** for the Sparx EA metaclass and **MDSE Object** for the MDSE type whenever ambiguity is possible.


Every modeled note uses `type` for its primary MDSE semantic class and `subtype` for an approved specialization/classification within that type.

The former property name `kind` is deprecated and must not be used in new notes.

`subtype` as a property is distinct from the semantic `subtypeOf / supertypeOf` relationship. Use the relationship only for true reusable generalization between modeled elements.

## 2. Generalization

Use `subtypeOf` only for a reusable invariant semantic distinction. Use `instanceOf` for concrete occurrences, deployed/location-specific objects, configured realizations, or cases where the difference is ordinary data/configuration.

## 3. Product control

`control` is independent from type and boundary. Do not create subtypes just to represent control, ownership, location, or lifecycle.

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

`Ampure_Data` is the common company vault.

Company-owned enterprise identities include, when designated:

- People
- Organizations
- Business Areas
- Roles
- common Processes
- enterprise Product / Product Line identity

Engineering/product-line vaults own detailed technical structure, requirements, designs, tests, issues, configurations, and other domain semantics.

Reference authoritative elements across vaults; do not fork identities for convenience.

## 11. Cross-vault identity

Every note has an immutable 30-character `uid`. Every vault has an immutable `vault_uid` in `.vault.yaml`.

Canonical durable note reference:

```text
uid:<30-character-id>
```

Canonical section reference:

```text
uid:<30-character-id>#<section-anchor>
```

Paths and vault names are current-location metadata, not durable identity.

## 12. Vault creation and splitting

Users create new vaults; AI does not autonomously create or split them.

When scale, access, lifecycle, ownership, search quality, or AI context becomes problematic, AI may recommend that the user consider splitting a vault.

## 13. Cross-vault views

For system/reference-level navigation across vaults:

- link to an authoritative `.base` view when one exists;
- otherwise link to the target README/index.

For semantic note-to-note relationships, target the specific note UID directly.

## 14. Integrity before handoff

Before handoff: YAML parses; IDs/UIDs are unique; links resolve where accessible; inverses are synchronized; subtype semantics are defensible; Functions have performers where applicable; requirement basis/satisfaction/verification gaps are visible.
