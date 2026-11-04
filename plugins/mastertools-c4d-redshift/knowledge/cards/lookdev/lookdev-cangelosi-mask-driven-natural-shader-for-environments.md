---
id: lookdev-cangelosi-mask-driven-natural-shader-for-environments
title: Alessandro Cangelosi: for a huge CG environment, one layered shader (rock, ice, snow) driven by painted masks and a few sliders beats painting every map
domain: lookdev
tags: [alessandro cangelosi, procedural shader, masks, snow, ice, rock, environment, 2012, art direction, deep-read]
applies_to: CG Garage podcast ep 307 (2020), guest Alessandro Cangelosi
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=Fa7z8RgPhA4, src:yt-transcripts]
feeds: [redshift, elevate]
conflicts: none
---
Guest Alessandro Cangelosi (freelance lighting and FX TD, Italy) built a procedural natural-shader collection for 3ds Max [24:26]. Pixomondo's 2012 team had a fully 3D environment, a matte-painted background and no time to paint masks for every rock and snow patch, so he made one shader that mixes rock, ice and snow, controlled by masks and a few parameters such as temperature, which decides whether ice melts or gets covered by snow [27:02, 27:34, 28:08]. Artists mark which area is rock, ice or snow and then adjust the sliders to reach the final look. He worked on it with a programmer for a C++ version, because the script version was slow [25:59, 26:30]. Used in V-Ray there.

**Use it:** A layered material with a mask per layer and a few global sliders suits art-directing big environments, in Redshift as a node setup with RS Color Layer and a few user-data or object-colour controls.
