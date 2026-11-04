---
id: broadcast-aximmetry-shadow-near-far-plane-defaults-and-refraction-camera-switch
title: Aximmetry (2018) 3D traps: shadow far plane defaults to 20 m, refraction is a camera switch, a transparent object loses its half shadow
domain: broadcast
tags: [aximmetry, composer, shadow near plane, shadow far plane, refraction, camera, transparency, shader, norm shader, ambient light, deep-read]
applies_to: Aximmetry Composer (2018)
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=ORANezf5Q9o, src:yt-transcripts]
feeds: []
conflicts: none
---
Spotlight shadows are computed only between a near and far plane, 20 m by default; moving the light far leaves a visible cut line, and stretching the far plane lowers shadow quality [12:32-13:04].
Refraction needs three things: a refract shader (the standard norm shader cannot do it; swap via change import source and the old settings carry over), refraction enabled on the camera because it costs resources, and a refraction index other than 1 [19:16-20:48].
Normal transparency removes the shadow at some opacity because half shadows are unsupported [18:46-19:16]. A light only affects the scene branch below its node [17:45]. Show helper geometries can be switched off so light cones do not obscure the view [10:27].
Collada import: import materials is optional, produces a general shader that is heavy; swap for a flat shader when only a colour map exists [27:03-29:42].

**Use it:** Use as a pre-flight list for a real-time 3D scene: shadow range, refraction cost, imported material weight.
