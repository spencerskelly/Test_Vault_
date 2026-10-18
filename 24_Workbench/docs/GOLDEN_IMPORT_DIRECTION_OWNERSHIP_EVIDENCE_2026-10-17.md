# Golden Import — Direction and Ownership Evidence Pass (2026-10-17)

Status: read-only full QEAX audit executed; source direction and parent correspondence evidence only. Not native acceptance.

Fixture SHA-256: `69222c060a81b3e35a3e25f365f2a1f4c3dd6eaa19d77fbbd5ba9abdf365a822`. 14,688/14,688 connectors, 26 families, private row ledger excluded from GitHub.

## Direction
- 14,257 have explicit raw EA `Source -> Destination` or `Destination -> Source` metadata. **Raw EA direction alone does not attest family-specific semantic orientation.**
- 431 have null/blank/`Unspecified` direction: **395 Association, 27 NoteLink, 9 Connector**. These are potentially undirected endpoint pairs, not automatically missing semantic direction. Preserve both endpoints and source evidence; do not invent arrow direction.

## Ownership and containment evidence
- 2,267 Aggregation connectors have one EA aggregate-end flag set; zero in this fixture with both/neither set. This identifies the flagged end, **not proof of physical containment**. Require independently supported assembly containment before emitting owned PartUsage.
- 137 Nesting connectors: 29 correspond to one endpoint's actual `t_object.ParentID`; 108 do not. For the 108, inspect native nesting roles separately; do not infer ownership from raw connector or package nesting.
- 442 ControlFlow/StateFlow connectors: 185 show same nonzero `ParentID` for both endpoint objects; 257 require workflow-owner evidence review. Shared EA parent is a clue, not alone proof of native owner.
- 11,842 other connectors do not call for this audit's ownership classification.

## Next gates
1. Trusted EA semantic orientation per family: generalization child -> parent, allocation source/target roles, requirement derivation, Realisation combinations, aggregation flagged-end semantics.
2. Compare nesting endpoints to approved nested State/Activity/Port/Requirement eligibility, not generic containment.
3. Distinguish direction-not-applicable from direction-unattested in the central evidence contract.
4. Run fully typed canonical graph with cycle/owner checks, then actual SysML v2 parser and library validation. Native accepted remains 0 until these gates.

No source names, IDs, GUIDs, connector ledger or generated model content are published here. The runnable audit tool and private ledger are held outside the repository pending integration into the central runtime.
