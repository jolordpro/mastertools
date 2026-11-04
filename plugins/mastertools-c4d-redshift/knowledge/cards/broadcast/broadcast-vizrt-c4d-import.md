---
id: broadcast-vizrt-c4d-import
title: Vizrt Viz Engine: FBX is the recommended route; C4D scenes import without C4D if Save Polygons Cache and animation cache are ticked
domain: broadcast
tags: [vizrt, viz engine, fbx, cinema 4d import, livelink, alpha, dxt]
applies_to: Viz Artist guide 5.x
status: V2
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://documentation.vizrt.com/viz-artist-guide/5.5/CINEMA_4D.html, https://documentation.vizrt.com/viz-artist-guide/5.4/Import_of_Files_and_Archives.html, src:research-production-pipelines]
feeds: [live-system export check]
conflicts: none
---
FBX brings PBR materials generated on import. LiveLink is one way, C4D to Viz. C4D import supports the classic render pipeline only. Clip playout needs the "with Alpha" option; texture compression picks DXT1 or DXT5 by alpha. The guide read is 5.x, so verify against the current version.

**Use it:** for live targets check caches saved, alpha textures present, texture sizes, polygon budget.
