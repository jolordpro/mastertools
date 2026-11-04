---
id: lookdev-texel-density-on-screen
title: For motion work, texture density only matters on screen: compare texture pixels to output pixels at the hero frame
domain: lookdev
tags: [lookdev, texel density, texture size, vram, uv, screen size]
applies_to: any
status: U
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.cryengine.com/docs/static/engines/cryengine-3/categories/1114113/pages/21267831, src:research-production-pipelines]
feeds: [PLAN Tactics preflight]
conflicts: none
---
Crytek's game target is about 512 texels per metre, 1024 for hero assets (search summary); no film or broadcast standard exists.

**Use it:** flag oversized and undersized textures from screen size, never from a fixed texels-per-metre rule.
