---
uid: fixture-v2-controller
class: Object
sourceRole: authoritative-model
primarySymbol: ControllerLibrary::Controller
fixture: true
---

# Controller

Synthetic reusable definition and typed CAN port.

## SysML source

```sysml
package ControllerLibrary {
    port def CanPort;
    part def Controller {
        port can : CanPort;
    }
}
```

## Rationale

A reusable definition is not a physical occurrence in a charger. See [Charger](Charger.md) for the owning contextual part usage.
