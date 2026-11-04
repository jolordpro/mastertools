---
id: redshift-material-blender-additive-layer-with-white-blend-colour-adds-car-paint-glitter
title: Redshift material blender: an additive layer with white blend colour adds a car-paint flake glitter over a base material, because black would add nothing
domain: redshift
tags: [material blender, additive, blend color, car paint, metallic flake, glitter, dice, jon jags nee, deep-read]
applies_to: C4D + Redshift (2022 upload, Jon Jags Nee)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=eKG2QSWJYYM, src:yt-transcripts]
feeds: [redshift, lookdev]
conflicts: none
---
Glitter without Substance: add a car paint material, set layer weight and specular weight down, push the metallic flake weight and reflectivity up, set the base diffuse to white to see flakes, then density up and flake scale about 0.01 then 0.005 [05:15-06:48].
Plug it into the material blender as layer colour 1 on top of the base glass-like dice material, tick Additive and set blend colour to white; the blend colour is a 0 to 1 amount, and black means one plus zero, so nothing is added [07:20-07:52]. Colour changes on the base keep the glitter [08:23].
Base look: refraction weight up, roughness about 0.15 to 0.5, colour from a Maxon Noise scaled around 0.05 to 0.15 [02:06-04:44].

**Use it:** lookdev recipe for glitter, flake or sparkle over any base without a custom texture; the blend colour doubles as a mask slot.
