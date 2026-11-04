---
id: c4d-standard-renderer-speed-ambient-occlusion-ray-depth-z-blur-simple-and-fake-caustics
title: Standard renderer (C4D, 2019 tutorial): drop AO max ray depth 100 to 60 saves 1 s, to 30 saves 2 s; Z-Blur lens to simple; replace single-colour caustics with a tinted light
domain: c4d
tags: [teamwnj, standard renderer, ambient occlusion, max ray depth, global illumination, ambient light, z blur, caustics, render time, lens flare, deep-read]
applies_to: Cinema 4D Standard renderer, version not stated (uploaded 2019-02); not Redshift
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=XuoDTdHngaA, src:yt-transcripts]
feeds: [redshift, estimator]
conflicts: none
---
Channel TeamWnJ states these apply only to the Standard renderer [00:33]. Test frame 1920x1080, 72 dpi, 24 fps [00:33-01:03]. Sec counts are per frame of his small test scene.
AO: his one always-on effect. Lower Max Ray Depth: 100 to 60 saved about 1 s, 100 to 30 saved about 2 s, but he saw quality drop at 30 [01:03-01:36].
GI: he calls it a time waster and fakes it with ambient lights; falls back to GI mostly in VFX work [01:36-02:06].
Depth of field: for Z-Blur, change blur type from lens to simple; loses bokeh, may save about a second [02:06-02:37]. Glow and object glow have little to tune [02:06-02:37]. Lens effects: skipping lens flares saves their whole cost [03:09-03:39].
Caustics: skip them when light passes through only one solid colour; instead tint the light and exclude the window mesh from it; this fails for multi-colour glass [02:37-03:09].
Do not copy any of these into Redshift; they are Standard-renderer timings from a toy scene.

**Use it:** when Standard/Physical output is slow and the shot allows it, test AO ray depth and Z-Blur type before buying hardware; never port the numbers to Redshift.
