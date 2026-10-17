# Golden Import — Shared part with multiple owning usages

Decision date: 2026-10-17. Status: APPROVED; implementation and native parser verification pending.

- When a reusable component definition appears in several assemblies, create **one independent native SysML v2 `PartUsage` per owning assembly**, each typed by the **same** reusable `PartDefinition`.
- Each usage has its own stable contextual identity and owner. Do not clone the reusable definition or create another MDSE note for a usage.
- Preserve all source aggregation/composition connector identities, flags, multiplicities, orientation and provenance in the local relationship ledger.
- Validate each parent as a legitimate semantic owner, detect cycles and unintended duplicate usages, and ensure repeat import preserves all usage identities.
- Organizational package/folder nesting does not create usages.
