---
id: agencies-mvsm-shot-distance-strategy
title: ManvsMachine's Sleep: wide shots fake fine holes with a displacement map, close shots use VDB geometry, Redshift proxies keep scenes light
domain: agencies
tags: [manvsmachine, mvsm, sleep, displacement, vdb, proxies, shot distance]
applies_to: Maxon article 2024
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.maxon.net/en/article/deconstructing-sleep-with-maxon-one, src:research-agency-insiders]
feeds: [Tactics preflight]
conflicts: none
---
VDB (many spheres subtracted from a volume) is detailed but costly. Lighting recipe on that piece: area lights, a sun and an HDRI, tuned for mood. Redshift lets them move between C4D and Houdini and keep one look. Cinema 4D is their main pipeline tool.

**Use it:** plan geometry by shot distance before building.
