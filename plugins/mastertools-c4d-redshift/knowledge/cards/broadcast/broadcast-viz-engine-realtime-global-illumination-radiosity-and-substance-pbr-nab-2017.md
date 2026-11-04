---
id: broadcast-viz-engine-realtime-global-illumination-radiosity-and-substance-pbr-nab-2017
title: Vizrt NAB 2017: Viz Artist 3.9 adds real-time global illumination; per-light radiosity bleeds colour and Substance PBR materials stay adjustable live
domain: broadcast
tags: [vizrt, viz artist, viz engine, global illumination, radiosity, substance, pbr, cornell box, nab 2017, virtual studio, deep-read]
applies_to: Viz Artist 3.9 / Viz Engine, NAB 2017
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=zBeBgKY596k, src:yt-transcripts]
feeds: [lookdev, broadcast templates]
conflicts: none
---
Vizrt booth demo (presenter unnamed) [00:06-10:00]:
- Cornell box test: change a wall colour and the bounce light recolours the room live; a light's radiosity setting raises or lowers the bleed, shadows feed the radiosity too [01:08-01:38].
- A virtual studio runs it with spotlights and dynamic reflections on the floor, in place of baked post-render looks, which the presenter calls static [02:11-03:13].
- Materials are Allegorithmic Substance PBR, procedural: edit tiling, ambient intensity, map size (1K to 2K), normal intensity, roughness, fibres or knots live [03:13-05:52].
- Turning off lights and raising radiosity on one spot lets one lit surface relight the room [05:52-06:55]; swapping wood for ceramic tiles, changing tile count, colour variation, grout colour, with the bleed updating at once [07:26-10:01].
- Objects imported from Maya, 3ds Max, C4D or Houdini keep their Substance look [07:56].

**Use it:** Viz-based sets get dynamic GI without baking; bake-free changes also mean no waiting on a farm.
