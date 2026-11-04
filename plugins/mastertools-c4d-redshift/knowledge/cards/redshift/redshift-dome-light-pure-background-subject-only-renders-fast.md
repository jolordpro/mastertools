---
id: redshift-dome-light-pure-background-subject-only-renders-fast
title: A dome light used only as a flat background keeps the colour constant under any key, and Thorup says it speeds buckets
domain: redshift
tags: [redshift, dome light, background, camera contribution, render speed, lukas thorup, alpha, deep-read]
applies_to: Cinema 4D + Redshift 3.x
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=dcLT_1mskBU, src:yt-transcripts]
feeds: [redshift]
conflicts: none
---
Thorup builds the backdrop of the Patagonia jacket shot as a Redshift dome light with every light contribution switched off except one that the auto-captions hear as "transmission" [20:18]. The jacket then goes black, which proves the dome is lighting nothing, and the backdrop colour stays the same whatever the spot does; changing it to grey or black is trivial [21:20].
He says the empty areas render almost instantly in bucket mode while the object takes the time, so it sped renders a lot [21:51] [22:25].
Unsure: the setting name is a caption guess. The existing card redshift-procedural-dome-background-contributions gives the camera-only setup, so trust that card for settings. The speed claim is his observation.

**Use it:** Keep as a lighting-independent backdrop recipe: dome contributes only to the camera, so the background never changes the subject's light.
