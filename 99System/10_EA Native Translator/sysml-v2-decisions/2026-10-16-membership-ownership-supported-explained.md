# Native SysML v2 / KerML Membership and Ownership
Date: 2026-10-16
Status: SUPPORTED NATIVE CONCEPT; current EA migration mapping NOT CONFIRMED; no special EA link is to be invented.

## What it means in plain English
Membership answers **"What is declared inside this model element?"** Ownership answers **"Which model element actually owns the declaration?"** This is about the organization of the model and the context in which names/features are defined. It is not necessarily about which physical parts are assembled together.

Examples:
- A package declares `part def Controller;`: Controller belongs to that package's namespace.
- A `Charger` definition declares `part controller : Controller;`: `controller` is a feature member of Charger, and the part usage additionally conveys composite-assembly semantics.
- A separate `ref part monitoredController : Controller;` is a non-composite reference, even though its declaration has an owning context.

## Syntax example (illustrative; validate with SysML v2 parser)
```sysml
package ChargerArchitecture {
    part def Controller;
    part def Charger {
        part controller : Controller;
    }
}
```

## What it does NOT mean
- Package membership does NOT mean the controller is physically inside the package; a package is a model namespace.
- A file/folder containing a note does NOT by itself define SysML v2 package ownership.
- Feature membership alone does NOT prove that the usage is a composite part; referential usages also have declaration context.
- Reusing a definition does NOT mean every usage is independently owned by that definition.
- Definition inheritance (specialization) and membership are unrelated predicates.

## Comparison
| Concept | Question answered | Example |
|---|---|---|
| Package membership | Where is this type declared? | Controller definition declared in architecture package |
| Feature membership | Which definition declares this feature? | Charger declares a controller usage |
| Model ownership | Who owns this declaration? | Controller usage declaration owned by Charger definition |
| Composite part usage | What constituents make up the containing part occurrence? | Charger has controller |
| Referential part usage | Which occurrence is referenced but not compositionally contained? | Monitor references existing controller |
| Typing | Of which reusable definition is a usage? | controller : Controller |
| Specialization | What more general definition does this definition inherit from? | ProCore specializes Charger |

## Workbench
- Structure view: present namespace/package grouping and directly declared features, distinguishing inherited, composite, and referential usages.
- Visual: show packages as grouping and constituent parts as nested boxes where appropriate; do not render package membership as physical wiring or a generic connector.
- Note text is authority: edits to package/feature membership via tree or diagram update the owning note syntax and refresh projections.
- The canonical definition must not be duplicated solely because it appears under multiple usage contexts.
- Obsidian folders organize storage/navigation, and need not mirror semantic package membership. Workbench may propose mappings without silently changing namespaces.
- Validate naming/scope, membership ownership and references during moves, rename and export.

## Current-model policy
Native membership is intrinsic to SysML v2 parsing and model construction and will necessarily exist wherever declarations exist. However user does not currently use an explicitly modeled EA 'Membership' relationship that should be directly converted. Do not create additional explicit membership connections during EA migration solely to fill the catalog.
