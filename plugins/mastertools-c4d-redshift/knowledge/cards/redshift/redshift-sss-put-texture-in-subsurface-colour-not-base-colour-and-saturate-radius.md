---
id: redshift-sss-put-texture-in-subsurface-colour-not-base-colour-and-saturate-radius
title: With strong subsurface, feed the colour texture into subsurface colour only (base colour off) and feed a more saturated copy into radius for subtle realistic variation
domain: redshift
tags: [subsurface color, base color, radius, texture, diffuse, broccoli, tomato, renderbaron, deep-read]
applies_to: C4D + Redshift standard material (renderbaron upload 2023)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=a5BDzPkwlUM, src:yt-transcripts]
feeds: [redshift, coach]
conflicts: none
---
In the tomato scene the image texture is wired only to subsurface colour, not base colour, and base colour is scaled to zero, because subsurface already contains a diffuse component and a second one is superfluous [03:20-04:23].
Radius decides which colours penetrate full depth and which return at once: a light green was allowed 0.1 cm in, the leftover violet came back to the surface as a complementary tone [04:23-04:55]. Feeding a more saturated copy of the texture into radius, with the normal one in subsurface colour, gave subtle, realistic variation [04:55-05:26].
Anisotropy 0 is even; his wording: positive pushes scattering away from the light, negative back toward it, and the parameters show full strength in random walk mode [05:26-05:57].

**Use it:** scene check: both base colour and subsurface weight 1 with the same texture means doubled diffuse; the coach suggests a saturated radius copy.
