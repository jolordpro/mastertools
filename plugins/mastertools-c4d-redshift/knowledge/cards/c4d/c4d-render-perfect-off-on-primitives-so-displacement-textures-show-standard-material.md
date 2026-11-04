---
id: c4d-render-perfect-off-on-primitives-so-displacement-textures-show-standard-material
title: Cinema 4D: a displacement texture will not show on a primitive sphere until Render Perfect is turned off on the object
domain: c4d
tags: [cinema 4d, displacement, render perfect, primitive, sphere, sub polygon displacement, pbr, deep-read]
applies_to: Cinema 4D standard/physical renderer
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=p-XJG8bLKBM, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Tutos (beginner channel) [05:29-06:46]. Displacement was connected and sub-polygon displacement switched on (which adds virtual polygons and render time), yet the sphere stayed perfectly round in the picture viewer. The cause was a setting on the sphere: Object tab, Render Perfect, which must be off. After switching it off the displacement showed [06:13-06:46]. He builds the material from Poly Haven 4K PNGs: diffuse, rough, AO, bump, normal (GL version) and displacement, with reflection type GGX and the rough texture in the layer colour [00:11-05:06]; specular and reflection strength set to 0 after loading the rough map [04:09].

**Use it:** Add to scene checks: displacement on a parametric primitive needs Render Perfect off. Redshift has its own tessellation route.
