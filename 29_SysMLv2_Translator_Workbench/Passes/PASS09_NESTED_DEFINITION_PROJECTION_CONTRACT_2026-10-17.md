# Phase 9 — Nested PartDefinition projection contract (synthetic)

Added a fail-closed synthetic projection for coincident lexical containment and direct specialization. Two **distinct** candidate edges exist only with explicit definition-intent approval and verified direction; otherwise review outcome has no projected edges. Even the synthetic approved path has `nativeCertified=false` and does not invoke a native emitter.

Six synthetic tests cover unapproved intent, two independent edges, owner mismatch, reversed direction, PartUsage exclusion and self-specialization.

Important: `lexicalContainment` and `specialization` here are internal graph descriptions, not invented SysML v2 custom relationships. The approved native semantic representation and parser syntax remain separate gates. Existing source-model nested hardware observations do not themselves constitute operator approval of definition intent.

Workbench requirements: display independent owner and subtype structures; visual specialization distinct from composition; navigate both source and target and retained local EA evidence; validate owner/specialization cycles and exact kinds; preserve provenance and round-trip; never collapse Binding Ports or part-as-port.

Local tests: `python3 -m unittest -v 15_Testing/test_phase9_nested_definition_projection.py`. CI and Mac results not yet observed. No source rows or GUIDs committed. Native emission disabled.