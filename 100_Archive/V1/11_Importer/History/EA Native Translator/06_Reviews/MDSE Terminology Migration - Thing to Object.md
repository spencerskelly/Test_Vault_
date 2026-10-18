---
uid:
type: Info
status: Settled
date: 2026-09-27
---
# MDSE Terminology Migration — Thing to Object

## Decision

The MDSE top-level type formerly named `Thing` is renamed to `Object`.

## Current classification

```yaml
type: Object
subtype: electrical
```

Approved Object subtypes remain electrical, circuit, mechanical, software, and firmware.

## EA source distinction

- **EA Object** — Sparx EA source metaclass with `Object_Type = Object`.
- **MDSE Object** — target MDSE semantic type.

The rename must never cause EA source evidence to be reinterpreted merely because the words match.

## Historical interpretation

Pre-migration MDSE methodology using `Thing` should be read as `Object` unless it explicitly records a literal historical/source value.
