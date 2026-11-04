---
id: pipeline-milk-sg-import-additive-layer-stack
title: Milk's SG Import builds a shot additively: asset, look dev, animation, then CFX, sculpt and groom layers, reading only what changed
domain: pipeline
tags: [milk vfx, shotgrid, usd, layers, sublayer, look dev, approved, deep-read]
applies_to: Houdini Solaris, ShotGrid (Milk VFX, FMX HIVE 2026)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=XfMp13jOSxE, src:yt-transcripts]
feeds: []
conflicts: none
---
Enrico (co-head of VFX, Milk VFX; surname not caught). Built on the creature show The Rats (2023-24) as a test bed [08:15-08:47]. A tool queries ShotGrid for assets and shots, then sublayers or references published caches into the stage in a vertical additive stack: base asset, look dev, animation, then CFX, shot sculpt, groom [09:49-10:50]. It brings no new cache, only reads transforms and vertex data from the animation cache, so the stage stays light [11:20]. It filters by published or approved status and warns when a newer version exists. Weakness: it needs a lot of user management and does not scale [11:20-11:50].

**Use it:** Model layer order as base, look, animation, then departmental overrides, and always show 'newer version exists'.
