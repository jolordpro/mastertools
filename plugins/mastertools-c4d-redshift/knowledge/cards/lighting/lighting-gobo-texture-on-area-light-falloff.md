---
id: lighting-gobo-texture-on-area-light-falloff
title: A texture on the area light acts as a gobo, giving soft falloff on metal that geometry alone does not
domain: lighting
tags: [gobo, cookie, area light texture, falloff, metal, jewellery, reflections]
applies_to: Redshift area light
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=kN00Z7UsW5U, src:yt-transcripts]
feeds: [elevate]
conflicts: none
---
Gradient mask textures on a light create a fake soft falloff on curved or metal surfaces [D 27:04-28:39]. They matter little with spread at full (diffused away) [27:04]. Without the texture the disc is the same intensity everywhere.

**Use it:** elevate: a suggestion for dull metal highlights, always tested on the hero at final spread.
