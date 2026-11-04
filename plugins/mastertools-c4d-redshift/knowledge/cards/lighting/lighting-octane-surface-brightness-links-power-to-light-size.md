---
id: lighting-octane-surface-brightness-links-power-to-light-size
title: With Octane's surface brightness on, scaling a light changes its strength; turn it off to scale freely, and gobo detail sharpens as the light shrinks
domain: lighting
tags: [octane, new-plastic, surface brightness, power, gobo, distribution, light size, deep-read]
applies_to: Octane for Cinema 4D (2022 video)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=J5KwV7GfbEQ, src:yt-transcripts, https://www.youtube.com/watch?v=tfRTKzVCTNk]
feeds: [[redshift]]
conflicts: none
---
Surface brightness checked: the light's power is tied to its area, so smaller means weaker and bigger means stronger [09:23]. Unchecked, only the power value sets strength [09:23]. A black and white image or noise in the Distribution channel works like a gobo or cookie: black blocks light [07:20][07:50]. The noise needs a projection node (XYZ to UVW, perspective or spherical) or it stays fixed in world space when the light rotates [07:50]. Smaller light means sharper, higher-contrast gobo, but a weaker light; his example needed power around 2000 until he unchecked surface brightness [08:52][09:23]. Keyframing the projection's X rotation from 0 to 360 over the clip makes a perfect loop [08:21]. Colour or image in the Texture channel mixes with temperature, so a green drifts yellow or blue as temperature moves [06:49].

**Use it:** a note to find the equivalent "normalize intensity" behaviour in Redshift lights before resizing a light after matching exposure.
Transcript support: Blackbody emission with surface brightness power about 5 for neon geometry; default was too bright. (https://www.youtube.com/watch?v=tfRTKzVCTNk [02:37-03:45])
