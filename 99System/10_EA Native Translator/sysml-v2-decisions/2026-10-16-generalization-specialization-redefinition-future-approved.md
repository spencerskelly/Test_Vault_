# Approved: Generalization remains specialization; redefinition is future explicit modeling
Date: 2026-10-16
Status: APPROVED

## Import rule
All EA Generalization relationships map by default to native SysML v2 specialization/subclassification. Direction remains specific definition -> general definition. Do not automatically translate imported Generalizations into feature redefinitions. Native validation should flag cases not representable as valid specialization, without silently creating unrelated constructs.

## Redefinition
Support native SysML v2 feature redefinition for future authoring and deliberate model corrections. It is a feature-to-inherited-feature relationship that refines/replaces an inherited feature's declaration in a more specific context; it is not the same edge as definition specialization. A specialized definition may both inherit and redefine particular features.

## Authority and user experience
Authoritative SysML v2 text lives in owning note. Structural and visual Workbench views edit that syntax and refresh from it. Allow future explicitly reviewed transformation to redefinition where source/target feature context supports it, including structural change when needed. Do not retain obsolete EA links as permanent source of truth. Retain one canonical reusable definition per type and optional usage notes.

## Visual and structural behavior
- Specialization: definition hierarchy and arrow from specific to general; inherited features visible.
- Redefinition: inherited feature and replacement/restricting feature traceable in context, with a distinct visual indicator and property inspector.
- Require target resolution and inheritance context validation.

## Next native relationship
Review further feature relationships (including reference subsetting) individually before accepting mappings.
