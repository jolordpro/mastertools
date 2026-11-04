---
id: lookdev-glass-faceted-geometry-and-inner-objects-feed-refraction
title: Glass comes alive with faceted geometry and objects inside it to catch light
domain: lookdev
tags: [glass, facets, icosphere, refraction, gpu, deep-read]
applies_to: Blender Cycles (old GTX 470)
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=F-uZdwvup5c, src:yt-transcripts]
feeds: [elevate]
conflicts: none
---
The host makes glass read by giving it a lot to refract: an icosphere instead of a smooth sphere, a cylinder with 8 sides instead of the default 32, and an extra object inside to bring light in [00:33]. He also reflects textured light into the inside of other objects [01:04]. A 123-frame animation at only 10 samples took 10 to 11 minutes and still looked good apart from slight grain [00:02]. On his card GPU was 7.78 s against 49.2 s for CPU on the same still, about 6x; he usually sees 4x to 6x depending on scene [03:10]. The GPU figure is from an old card, so treat it as order of magnitude only.

**Use it:** if plain glass looks dead, add facets or an inner object before touching the material.
