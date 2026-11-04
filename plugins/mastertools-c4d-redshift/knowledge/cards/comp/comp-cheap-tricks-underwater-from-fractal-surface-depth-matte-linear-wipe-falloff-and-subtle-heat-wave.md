---
id: comp-cheap-tricks-underwater-from-fractal-surface-depth-matte-linear-wipe-falloff-and-subtle-heat-wave
title: Underwater look in comp: a Fractal Noise water layer matted by the foreground's inverted alpha, a linear-wipe falloff and a touch of Heat Wave
domain: comp
tags: [underwater, fractal noise, caustic beams, optical glow radiate, heat wave, match background, reference image, deep-read]
applies_to: After Effects, Red Giant Supercomp
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=-32g9bYyZuc, src:yt-transcripts]
feeds: [comp, lookdev]
conflicts: none
---
Build [30:03-38:36]: tint a low-contrast Fractal Noise solid, use Set Matte on the foreground layer's inverted alpha so its depth sliders set how high the water climbs; for the surface use Universe Fractal Background at a big scale, complexity 2, inverted, as a flat 3D layer, then a linear wipe with feather to fade it by distance; pre-compose it with collapse transformations ticked so Supercomp accepts the 3D camera [31:07-32:43]. In Supercomp: diffusion, haze (picks up sky brightness), additive surface with Optical Glow, Radiate near 100 and the radiate centre moved to throw beams down [34:17-35:23]. Re-add the subjects as a second foreground instance so water does not overlay faces, with a linear wipe from below so near parts are more visible [35:23-36:27]. Heat Wave in subtle amounts sells the water; Magic Bullet Looks (vignette from above) unifies [37:10-38:03].
Colour tip: drop a reference image in the comp and use Supercomp's Match Background on the colour correction instead of guessing the tint [33:15-33:46].

**Use it:** A reference-matched tint beats hand-tuned colour for stylised weather and water looks.
