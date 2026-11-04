---
id: redshift-toon-material-tone-map-ramps-quantize-diffuse-reflection-rim
title: Redshift Toon material (C4D, 2024): quantised shading comes from tone-map ramps on diffuse, reflection and rim, and lights must be pushed hard
domain: redshift
tags: [redshift toon, npr, tone map, ramp, rim light, cel shading, c4d, school-of-motion, deep-read]
applies_to: Cinema 4D + Redshift 3.6-era toon release (video April 2024)
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=i3YczHKxtbo, src:yt-transcripts]
feeds: [redshift, elevate, coach]
conflicts: none
---
EJ (School of Motion, April 2024, C4D with the first Redshift Toon release). Add the Toon preset material from the material manager and apply it to everything; the preset already holds a Toon material node with a base colour and a diffuse tone map [00:31-02:34]. The stepped look is just a ramp feeding the tone-map input; it acts like a multiply over the base colour, and a hue-tinted shadow chip (his example: a little purple against yellow) shows up as a tint [02:34-03:35].
Moving every knot by hand is slow, so the ramp's new exposure value shifts how the whole gradient maps across the object in one move [03:35-04:07]. Reflection has its own weight, colour, roughness and tone-map ramp, and it is Fresnel-driven [04:07-05:08]. Rim lighting is off by default (weight 0); at weight 1 it appears as a smooth, unquantised edge, so plug a third ramp into a rim tone map to step it [07:44-09:20].
Lights: with no lights the shader lights from the camera like a headlamp. Infinite lights work (only rotation matters, and the blue Z axis is the aim); any light added is very underpowered for toon, so push exposure (about 2 for an infinite light to match the default look, about 9 for a point light) [05:08-06:40]. To get a flat background colour, drop the dome light's exposure to about -8 so it adds no diffuse, then set its colour [07:12-07:44]. Rim lights can be steered: drag light objects into the rim-light list (up to five), and the rim highlight follows each light's position [09:50-11:22].
Speaker's limits at v1: no light-position-based line control yet.

**Use it:** when a toon look is requested, build tone maps per channel (diffuse, reflection, rim), raise light exposure well above photoreal values, and name rim lights by side so a revision can move them.
