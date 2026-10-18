# EA to MDSE Native Importer v0.8.15

v0.8.15 builds on v0.8.14 and implements W-381.

## Fix

A newly generated MDSE base intentionally ships with `vault_uid: UNINITIALIZED` so every copied vault can receive a unique identity. v0.8.14 treated that valid fresh-base state as incompatible during output selection.

v0.8.15 separates **base compatibility** from **write eligibility**:

- an uninitialized generated base can be selected and fully checked for release, schemas and runtime plugins;
- model generation remains disabled;
- the operator enters a vault display name and governed 13-character author code;
- **Initialize selected base** allocates the normal UTC-millisecond + author-code vault UID and rewrites only `.vault.yaml`, preserving `mdse_release`;
- the importer immediately re-runs strict initialized-base validation;
- only a successful revalidation enables model generation.

A pre-initialized distributed base is intentionally not used because multiple extracted copies would otherwise share one vault identity.

No Local Model, connector, relationship, identity-token, path, attachment or W-377/W-380 semantic behavior changes from v0.8.14.
