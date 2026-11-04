---
id: c4d-pyro-fire-writes-on-text-collider-tag-surface-thickness-4-voxel-2-zero-buoyancy
title: C4D 2023 Pyro fire that draws on a text shape - collider tag on a meshed container, surface thickness 4, voxel size 2, buoyancy and gravity at zero
domain: c4d
tags: [pyro, text, fire, collider, cinema-4d-2023, title, deep-read]
applies_to: Cinema 4D 2023 Pyro (2022)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=2yaRgwWYoDg, src:yt-transcripts]
feeds: [motion]
conflicts: none
---
PixelAffair, 2022 [00:35-09:37]. Recipe to keep fire inside lettering:
1. Text to a Volume Builder (voxel size 1) to a Volume Mesher, convert with Current State to Object; raise adaptive to cut polygons [01:45-03:20].
2. A small sphere with the Pyro tag sits inside the letters; give the meshed text a Collider tag so fire stays inside [04:23].
3. Fire would not travel: lower voxel size on sphere and Pyro object to 2 [04:53].
4. Surface thickness was too large and fuel spilled out; set it to 4 [05:57].
5. Gravity 0 in project settings and buoyancy and extra forces 0 on the Pyro object, so fire hugs the letters [06:27].
6. Dissipation was 7 percent, so fire died early; 1 or 2 keeps it, 0 keeps it forever [07:30].
7. A second sphere with a Pyro Fuel tag at the bottom explodes when touched by fire [08:35].
Smoke density was turned off for the demonstration.

**Use it:** A logo or title burn-on that can later be meshed (see the Volume Mesher card).
