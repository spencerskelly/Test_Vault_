---
uid: fixture-v2-power-module
class: Object
sourceRole: authoritative-model
primarySymbol: PowerLibrary::PowerModule
fixture: true
---

# Power Module

Synthetic reusable definition. The multiple module occurrences belong to the parent Charger declaration.

## SysML source

```sysml
package PowerLibrary {
    part def PowerModule {
        port can : ControllerLibrary::CanPort;
    }
}
```
