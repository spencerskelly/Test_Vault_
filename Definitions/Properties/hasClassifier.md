---
uid: 20260930133525656skellyspencer
id: INFO-00053
status: Active
property: hasClassifier
appliesTo: 
required: No
setBy: Translator; resolved in stage 2
canChange: 
---
# hasClassifier

The element named by the EA Classifier field of a Port, or by the PDATA1 typing link of a Port when the target is not a Port note (a Hardware Component or a Signal). Written by the translator on the Port note; inverse generated. Temporary (W-125, W-127): kept to keep the import clean and resolved in a later stage into copyOf/hasCopy or another relationship, then removed.

## Direction

Temporary pair, written by the translator on the note; the inverse `classifierOf` is generated. It is resolved in stage 2 and then removed.

## Where it sits

After `tags`, in the order of `relationships.yaml` (W-126). It may hold several values.
