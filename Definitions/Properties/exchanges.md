---
uid: 20260930133525663skellyspencer
id: INFO-00060
status: Active
property: exchanges
usedOn: see relationships.yaml
required: No
setBy: Translator (translated notes) or by hand
canChange: 
---
# exchanges

transmits, receives and exchanges say what data a Port sends, takes in, or both, and point at the Item Flow note for that data (W-177). The Port already connects to something (interfaces); these fields define what is exchanged with it. transmits is the source or out end, receives the target or in end; for an inout flow both Ports get exchanges. One-way: nothing is written back on the Item Flow note, which shows the Ports in its backlinks and can be queried.

## Direction

One-way: listed as one-way in `relationships.yaml`; no inverse field exists.

## Where it sits

After `tags`, in the order of `relationships.yaml` (W-126). It may hold several values.
