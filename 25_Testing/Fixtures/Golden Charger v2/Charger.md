---
uid: fixture-v2-charger
class: Object
sourceRole: authoritative-model
primarySymbol: ChargerProduct::Charger
fixture: true
---

# Charger

Synthetic contextual assembly. Multiplicity denotes three interchangeable power modules, not three separate reusable definitions.

## SysML source

```sysml
package ChargerProduct {
    part def Contactor;

    part def Charger {
        part controller : ControllerLibrary::Controller;
        part modules : PowerLibrary::PowerModule[3];
        part contactors : Contactor[2];
    }
}
```

## BOM source evidence — not generated formal assertions

| Internal Part Number | Manufacturing Part Number | Quantity | Interpretation |
|---|---|---:|---|
| CT-100 | MFG-C1 | 2 | Contactor line |
| *(blank)* | MFG-C2 | | Alternate for CT-100 |
| *(blank)* | MFG-C3 | | Alternate for CT-100 |

Per [BOM-ALT-001](../../../26_Definitions/BOM%20Integration.md), manufacturing alternates are not additional required uses, and substitutability needs separate review.

## Source ownership

The parent Charger definition owns its parts. Controller and Power Module notes own only reusable definitions.
