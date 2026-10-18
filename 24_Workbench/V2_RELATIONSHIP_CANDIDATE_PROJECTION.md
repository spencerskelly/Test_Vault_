# V2 build — relationship candidate projection

Status: implemented; synthetic regression wired into CI. Native emission remains disabled.

## Purpose

Read a bounded set of source EA connectors and compare their exact connector-type/stereotype families with the approved SysML v2 semantic registry. Produce **aggregate-only review evidence**. This pass does not decide endpoint roles, direction, multiplicity, ownership, or whether the target is valid native SysML v2 syntax.

## Run locally

```sh
python3 21_Importer/project_v2_relationship_candidates.py /path/to/source.qeax --limit 100
python3 -m unittest 25_Testing/test_v2_relationship_candidate_projection.py
```

The source database is opened read-only. Output contains candidate target counts, evidence gates, source dispositions, and explicit zeros for generated native relationships. No original element identities, connector IDs, GUIDs, model names, or endpoint pairs are printed.

## Rules and safeguards

- Registry: `24_Workbench/registry/sysml_v2_semantic_rules.v0.2.json`.
- An exact `Connector_Type:Stereotype` match is required, preserving distinctions such as `Dependency:verify` versus `Dependency:satisfy`.
- Empty-stereotype generic connector families can match an explicitly registered `Type:` rule; named unrecognized stereotypes are **not silently coerced** into that generic family.
- Unknown families remain `UNMATCHED_REVIEW`, subject to semantic review.
- Duplicate family keys, unsafe emission authorizations, unsupported source schema and invalid slice sizes fail closed.
- Every row remains deferred, even when a registry rule has a native candidate.

## Workbench boundary

Structural and visual views may display provisional candidates with a **review** status, but must not turn those candidates into authoritative containment, connection, verification, or allocation edges. Selection must keep original EA source direction and provenance distinct from the proposed SysML semantic orientation. Validation must surface gates and unmatched families. Round-trip must leave EA source unmodified and must not synthesize native declarations.

## Follow-up step

Build a **typed endpoint evidence join** for the bounded connector slice: read EA start/end elements, preserve EA direction exactly, normalize only where a separately evidenced approved rule applies, and classify role-dependent gates. Test generalization orientation, ownership/multiplicity, satisfy/verify objective roles, and proxy/full-port relationships. No native text emission until parser and evidence checks exist.

No v1 tooling dependency is introduced. Approved semantic values can be carried forward into the v2 registry, but v2 code and documentation stand alone.
