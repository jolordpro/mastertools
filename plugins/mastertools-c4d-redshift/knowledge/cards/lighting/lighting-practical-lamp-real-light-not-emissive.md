---
id: lighting-practical-lamp-real-light-not-emissive
title: Light a practical lamp with a real Redshift light at the bulb, not an emissive bulb material
domain: lighting
tags: [practical light, lamp, emissive, spotlight, area light, grain, gi, camera contribution]
applies_to: Redshift / C4D 2026
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=nwBpkCPFG0s, src:yt-transcripts, https://www.youtube.com/watch?v=jAz4Lb93gwY]
feeds: [elevate, coach, redshift]
conflicts: none
---
[18:48] An emissive bulb material is grainy because it relies on GI. [19:49] Instead set the bulb's RS object tag to override visibility so it casts no GI, then add a spot (cone-shaped fixtures) or area light (strips, tubes) at the bulb, zero its position, match the shape, add falloff.
[21:54] Exclude the bulb geometry from the light so it does not block it.
[28:36] To hide the light's own surface from camera, lower the light's Camera contribution to 0 (the speaker first said diffuse, then corrected himself).

**Use it:** advise this when a lamp scene is noisy and the bulb is the only light source.
