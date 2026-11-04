---
id: lookdev-farm-ocio-drift
title: Farm renders can look different: OCIO is an OS variable, so headless nodes may fall back to defaults or a different ACES version
domain: lookdev
tags: [lookdev, ocio, farm, headless, aces mismatch, data maps, cryptomatte, normals]
applies_to: C4D + Redshift on farm nodes
status: U
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://irendering.net/redshift-aces-color-management-render-farm/, src:research-agency-pipelines, src:research-gaps-deep, https://www.youtube.com/watch?v=Y2mcVM8c7cA]
feeds: [CHECKS 5 colour space, PLAN render environment lock]
conflicts: none
---
Vendor claim (iRender): the OCIO variable is not stored in the .c4d file, so a node without it falls back.
Also listed: ACES 1.x on the farm versus 2.0 on the desk, data maps (normals, Cryptomatte) auto-tagged sRGB, and Bake display transform applying a curve twice.
Single vendor source; confirm with a test frame before treating as fact.

**Use it:** send a known-colour patch through desk and farm and compare values before a long job.
