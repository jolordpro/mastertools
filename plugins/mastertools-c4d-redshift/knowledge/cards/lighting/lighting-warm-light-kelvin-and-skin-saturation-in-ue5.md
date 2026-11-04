---
id: lighting-warm-light-kelvin-and-skin-saturation-in-ue5
title: Warm fire light at 2000-2500 K goes very orange on skin, so pull saturation back on lights that hit skin or costume
domain: lighting
tags: [colour temperature, fire light, skin, saturation, josh toonen, unreal, light rig, deep-read]
applies_to: Unreal Engine 5 (2023)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=jAz4Lb93gwY, src:yt-transcripts]
feeds: []
conflicts: none
---
Josh Toonen [03:30-05:09]. Use the temperature setting; above about 6500 K makes little difference, but for warm lights it helps. Background fire lights sit between 2000 and 2500 K, which goes insanely saturated orange on skin, so reduce saturation for anything touching skin and keep some blue in the costume. Lower intensity so skin does not clip but still has range. Speed trick: parent all lights to an empty light rig actor around the character (set from Stationary to Movable) so the whole rig can be rotated while the framing stays put [03:37]. For a point light, find the position first; once happy, copy it to a spotlight and narrow the cone, with the outer cone at 90 while positioning because rotation matters less than location [05:41]. Attenuation radius at least 1000 for realism [06:11].

**Use it:** Settings to quote in the lookdev/lighting notes: warm temperature range for fire, and the saturation cut for skin.
