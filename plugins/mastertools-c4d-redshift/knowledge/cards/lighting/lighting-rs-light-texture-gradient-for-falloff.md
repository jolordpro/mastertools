---
id: lighting-rs-light-texture-gradient-for-falloff
title: Put a gradient light texture on an area light to get a nicer falloff than the default, and set colour to Temperature first
domain: lighting
tags: [redshift, light texture, gradient, falloff, color temperature, area light, deep-read]
applies_to: Redshift area light
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=BlEM9iOzqMI, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
He sets the key light colour mode to Temperature (higher value reads cooler in his UI) [07:38]. He then adds a gradient as a light texture; it reads black and white values to shape the falloff, and he says removing it makes the falloff less nice [08:13]. Rim lights are copies with the colour pushed cooler or more natural, e.g. one rim kept less blue than the other [13:15].

**Use it:** suggest a gradient light texture when a soft box or key falls off flat.
