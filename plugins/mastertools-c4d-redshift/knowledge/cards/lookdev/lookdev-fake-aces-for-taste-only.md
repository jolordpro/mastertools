---
id: lookdev-fake-aces-for-taste-only
title: 'Fake ACES' (just the ACES view with sRGB-style colour choices) is fine for taste work but not for matched or brand colour
domain: lookdev
tags: [aces, fake aces, view transform, hdri, textures, brand colour]
applies_to: C4D with Redshift view transform
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=7uY4-bPvRKs, https://www.youtube.com/watch?v=IcLiz8e8ffc, src:yt-transcripts]
feeds: [lookdev, coach]
conflicts: none
---
Zak picks colours while looking through the ACES view without converting HDRIs or textures, and gets the tone mapping and wide gamut; colours can look more vibrant than they should [30:23-32:27].
Maxon's hosts say that using ACES only as a LUT-style look is technically wrong but gives pleasing results; learn the real specification [1:26:18-1:27:55].
A true workflow converts HDRIs and textures and is needed for matching live action or client colours [32:27].

**Use it:** tell the user which mode they are in; matched work needs real ACEScg conversion.
