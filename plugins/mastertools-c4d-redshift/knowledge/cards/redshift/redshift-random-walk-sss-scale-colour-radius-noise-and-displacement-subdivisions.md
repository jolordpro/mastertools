---
id: redshift-random-walk-sss-scale-colour-radius-noise-and-displacement-subdivisions
title: Random-walk SSS: scale near 0.2 reads soapy, 0.01 is almost diffuse, black radius kills scattering, and noise in radius gives imperfections
domain: redshift
tags: [random walk, subsurface, radius, scale, soap, noise, displacement subdivision, ross mason, deep-read]
applies_to: C4D + Redshift standard material (2024 upload, Ross Mason)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=ZcZa-42w8QE, src:yt-transcripts]
feeds: [redshift, coach]
conflicts: none
---
Disable diffuse and reflection, set subsurface weight 1: it is washed out, so lower the scale (1 washes out; 0.5 and 0.1 still wash; he settled around 0.2, earlier render 0.25, he later said something like 2, caption unclear) [01:06-06:48]. Scale 0.01 gives almost no scattering, effectively a diffuse material [06:17].
Radius colour multiplies the scale: black radius removes all scattering even though the surface stays tinted; white restores it [06:48-07:20]. A Maxon Noise (scale 0.1, clamped for contrast) in radius mixes strongly scattering and diffuse patches [07:20-07:52].
A tint in radius (red at about 15-20 percent saturation) warms the scattered light; he warns not to go over the top [08:23-09:24]. Jagged displacement was fixed by raising max subdivisions to 6 [09:24].

**Use it:** supports `redshift-sss-radius-colour-and-scale` with a noise-in-radius trick and a displacement-subdivision fix.
