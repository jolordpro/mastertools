---
id: lighting-say-start-with-a-flat-even-sky-and-a-floor-so-textures-behave-in-any-light
title: Say's baseline light rig: an even sky (Physical Sky in standard, a dome in Redshift) plus a floor, so textures are judged before dramatic light
domain: lighting
tags: [eric-say, baseline light rig, physical sky, dome light, hdri, c4d, redshift, deep-read]
applies_to: Cinema 4D standard and Redshift (NAB NY 2019)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=0Zg4lpwZGe0, src:yt-transcripts]
feeds: [redshift]
conflicts: none
---
Say begins every project with Physical Sky set to afternoon, GI on and all quality settings crushed to minimum, since the aim is a flat baseline, then adds a floor for shadows [21:57-22:29]. His reasoning: if textures behave in the even rig they behave in night or daylight later. The sky also gives a reflection map. In Redshift the equivalent is a Dome Light with an HDRI (he used an old industrial hall HDR that gives a notch of detail in the reflection) [28:12-31:17]. Redshift renders interactively fast on his single-GPU machine, and the team moved to it after a car job needed high-end reflections [29:13-30:15, 38:47].
Baseline material (standard render): specular turned up with a narrow width for a pin highlight, plus a Fresnel in the reflection layer [22:29-22:59].

**Use it:** Use as the default look-dev rig before building the final lighting.
