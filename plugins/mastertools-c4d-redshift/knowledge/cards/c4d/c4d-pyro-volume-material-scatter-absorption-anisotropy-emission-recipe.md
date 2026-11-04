---
id: c4d-pyro-volume-material-scatter-absorption-anisotropy-emission-recipe
title: Redshift Pyro Volume material in C4D 2023.1 - scatter tint colours smoke, absorption darkens it, anisotropy lets light through, emission drives flame
domain: c4d
tags: [pyro, redshift, volume-material, scatter, absorption, emission, cinema-4d-2023, deep-read]
applies_to: Cinema 4D 2023.1 with Redshift (version not stated) Pyro Volume
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=TLlITrj5A_4, src:yt-transcripts]
feeds: [redshift, lookdev]
conflicts: none
---
Effectatron, 2022 [18:38-22:15].
- Density scatter colour: a higher scatter coefficient lets more light scatter through, and tinting it colours the smoke (red gave red smoke). Lower scatter gives darker smoke.
- Absorption kills light: higher = darker smoke. He used 0.25 then 0.5 with a dark grey scatter so smoke is dark but still lit [19:40-21:43].
- Anisotropy under scatter: raising it pushes more light through the smoke; lowering reflects it back [20:41].
- Emission is the flame; at 3 the fire gained a lot of energy [20:10].
- Check the look by turning the back light down and up: the back light drives the translucent edges [20:41].
- Finish in the Redshift post: LUT filmic medium high contrast (log conversion), colour contrast, red channel lows pulled down for a blue tint, small exposure raise. Exposure now lives in the Redshift camera object (convert the old camera tag) under optical and lens effects [22:15-23:18].

**Use it:** A tuning order for smoke in broadcast stings: scatter colour, absorption, anisotropy, then emission and backlight.
