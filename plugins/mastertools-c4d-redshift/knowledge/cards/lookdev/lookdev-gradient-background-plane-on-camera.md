---
id: lookdev-gradient-background-plane-on-camera
title: For a gradient background, use a plane parented to the camera with an Incandescent Ramp and a Redshift Object Tag that switches off everything but primary rays
domain: lookdev
tags: [gradient background, banding, dome light, incandescent, camera plane, object tag, ramp]
applies_to: Cinema 4D 2025 + Redshift
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=KnfiJy2ND2o, src:yt-transcripts, https://www.youtube.com/watch?v=kgZcffv-bZc]
feeds: [lookdev sheet, broadcast backgrounds]
conflicts: none
---
A dome gradient bands (8-bit) [27:41, 53:57]; the camera Background option accepts colour or image but not a gradient [54:28]. Make a plane a child of the Redshift camera, zero it, scale and push back [28:12]; add an Incandescent material with a Ramp into illumination colour [29:15]. Add a Redshift Object Tag and turn off shadows, reflection, refraction and GI so it is a pure background [30:23, 55:00]. Method came from a Redshift developer.

**Use it:** Use for broadcast backgrounds; a baked gradient image is the fallback with less control.
