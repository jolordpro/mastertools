---
id: c4d-farm-ocio-env-var-risk
title: OCIO is set by an OS variable, not stored in the .c4d file, so a headless node can fall back to a different config
domain: c4d
tags: [ocio, environment variable, farm, aces, mismatch, data maps, bake display transform]
applies_to: C4D 2026+ on farms
status: U
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://irendering.net/redshift-aces-color-management-render-farm/, src:research-agency-pipelines, src:research-gaps-deep]
feeds: [CHECKS 5]
conflicts: none
---
One farm vendor post (2026-10-24). It also claims ACES 1.x on the farm against 2.0 on the desk gives mismatches, that data maps (normals, Cryptomatte) get tagged sRGB by auto-detect, and that "bake display transform" applies a curve twice.
None tested.

**Use it:** record the OCIO config path and version in the scene fingerprint and compare on the node.
