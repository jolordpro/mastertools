---
id: lighting-rs-dome-light-rotates-but-cannot-translate-use-a-bent-plane-or-move-the-scene
title: A Redshift dome light only rotates: to shift a backdrop up or down, move the scene or hang the image on a bent plane
domain: lighting
tags: [maxon, redshift, dome light, hdri, backplate, backdrop, deep-read]
applies_to: Redshift 3.5 in Cinema 4D R26 (2022)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=RpiCCLHjlWQ, src:yt-transcripts]
feeds: [lighting, coach]
conflicts: none
---
Maxon trainers: the dome is a vector environment, so moving it up or down does nothing; only rotation changes the view [35:09-36:43]. Workarounds: lift the whole scene, or put the image on a plane with a bend (spline wrap or spherify also work) and move the plane; a texture node has offsets, the dome does not [36:13-38:15].
Related: switch off Background to hide the HDRI, or enable Back Plate and drop a different image there so lighting stays on the HDRI; the dome texture also takes a PNG sequence for an animated backdrop [27:49-29:14]. Hue, saturation and gamma on the dome texture tint the light, for example half saturation and an orange tint for a bronze set [26:39-27:40].
Two-dome colour trick: a duplicate dome as the background colour with its diffuse, reflection, transmission, scatter, GI, volume and shadow contributions all zero (listed in the Details tab), so only the HDRI lights [32:29-34:02].

**Use it:** When a user cannot reposition an HDRI background, offer the bent-plane backdrop. Supports lighting-dome-bg-dome-quad-rig.
