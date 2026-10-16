# EA to MDSE Native Importer v0.8.0

This folder preserves the complete v0.8.0 importer candidate as a versioned implementation snapshot.

## Purpose

Keep each importer version in its own folder so behavior, acceptance findings, and changes can be compared over time without overwriting earlier implementations.

## Status

- MDSE release: 0.8.0
- relationships: 1.35
- element-types: 1.17
- Local Model: 0.2
- source model: EA8647
- path limit: 212 characters
- model files per generated folder: 75 maximum
- overflow behavior: preserve meaningful source/navigation subdivisions first; if a folder still exceeds 75 generated model files, create deterministic `folder_1`, `folder_2`, etc. mechanical subdivisions
- acceptance status: implementation candidate; real QEAX acceptance test pending
- keepability gate: WB-106 remains required before a whole-model import is treated as a retained production candidate

## Primary file

`EA_to_MDSE_Native_Importer_v0.8.0.html`

Future importer versions should use sibling version folders under `99_System/09_Tools/EA_to_MDSE_Native_Importer/`.
