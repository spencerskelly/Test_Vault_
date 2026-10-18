# Phase 9 — Native nested definition + owner specialization fixture gate

Two synthetic source fixtures were added to the existing official SysML v2 Jupyter parser workflow:

- `Fixtures/synthetic_nested_definition_specializes_owner.sysml`: a `part def ParentHardware` owns a nested `part def ChildHardware specializes ParentHardware;` declaration. This is a nested **definition**, not a part usage.
- `Fixtures/synthetic_nested_usage_not_definition.sysml`: a `part def ParentHardware` with an owned `part nestedHardware;` usage, for contrasting syntax.

The OMG SysML v2.0 language specification documents both specialization using `specializes` and nested definitions (its normative text has an example of a nested item definition specializing its enclosing definition). Specification: https://www.omg.org/spec/SysML/2.0/Language/PDF . That supports syntax as a candidate, but parser acceptance in this repository has **not yet been observed**; the manual-dispatch workflow was modified to run both fixtures against the installed SysML Jupyter kernel. Tests should not be claimed passing until GitHub Actions executes.

Semantic limitations: parser acceptance alone will not prove that the eight actual EA nested Hardware Component declarations intended subtype-of-owner semantics. A definition's lexical owner and its general definition are distinct concepts. This fixture must never be generalized to automatic part composition, usage typing or redefinition. Workbench structural view must show independent lexical nesting and specialization; visual view must retain subtype→supertype and optionally show nesting without implying composition; navigation opens both definitions and their EA source evidence; validation checks context, direction, cycles and provenance; round-trip retains source relationship records locally. Binding Port remains distinct.

Operator action: From GitHub Actions manually dispatch `Native SysML v2 pilot fixture gate` and inspect the two new steps. Native emission is disabled, and nativeCertified remains zero.

No private model data or GUIDs committed.