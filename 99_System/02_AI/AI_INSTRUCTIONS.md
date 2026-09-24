# MDSE AI Instructions

Before substantial model editing, read:

- `99_System/10_Docs/MDSE Modeling Ruleset 1.19.md`
- `99_System/10_Docs/Vault Architecture and Cross-Vault Rules.md`
- `99_System/03_Schemas/relationships.yaml`

Default AI-authored drafts to `90_Concept/AI_Workspace`.

Rules:

- classify before creating;
- reuse authoritative concepts;
- never infer missing source facts;
- preserve stable UID identity when moving notes between vaults;
- do not duplicate Company-owned identities in domain vaults;
- use defined relationships only;
- author forward/owner-side relationships as semantic truth;
- synchronize generated inverses before handoff;
- treat cross-vault links as ordinary semantic relationships whose target is resolved by UID;
- do not create/split vaults autonomously.
