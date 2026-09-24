# AI / Agent Rules

Before substantial edits, read:

- `99_System/10_Docs/MDSE Modeling Ruleset 1.19.md`
- `99_System/10_Docs/Vault Architecture and Cross-Vault Rules.md`
- `99_System/03_Schemas/relationships.yaml`

Rules:

- Never invent missing source facts.
- Prefer reuse over duplication.
- Folder placement is navigation, not semantic authority.
- Author the forward/owner-side relationship; generated inverse fields are derivative.
- Use stable `uid` identity for durable cross-vault references.
- Do not copy Company-owned identities into domain vaults.
- Draft AI-created model changes under `90_Concept/AI_Workspace` unless explicitly authorized otherwise.
- AI does not decide to create/split vaults. Users create vaults. AI may flag when scale, access, lifecycle, search, or context quality suggests a split.
