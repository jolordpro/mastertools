---
id: c4d-2023-1-2-redshift-particle-driven-pyro-advection-recipe-cache-about-four-minutes
title: Particle-driven pyro in C4D 2023.1.2 + Redshift: thinking particles from a plane, field force at -5, vertex map, pyro density and colour only, cache took about four minutes
domain: c4d
tags: [emission probable, pyro, particles, thinking particles, field force, vertex map, density dissipation, smoothing, redshift, bloom, denoise, cinema 4d 2023.1.2, deep-read]
applies_to: Cinema 4D 2023.1.2 with Redshift (video uploaded 2022-12)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=cxAeBv8AfAs, src:yt-transcripts]
feeds: []
conflicts: none
---
Captions are very sparse and garbled (59 words/min), so treat this as an outline only. Speaker: Emission Probable (channel).
Particle setup: a plane as emitter, a time node limiting by frame count (360 in the video, with the compare value 240 as particle life plus dissipation) [01:08-02:28]; five particles per group [03:00-03:30]. A field force with absolute velocity -5 and a vertex map for the pyro parameter, both given the particle group (value 30 heard) [03:30-04:45]. Check the particles before adding pyro [04:45].
Pyro: smaller voxels are better; only density and colour used (temperature and fuel optional; he shows a temperature version) [05:28-06:49, 10:42]. Density buoyancy to 0, some density dissipation, smoothing 50 or more [06:49-07:21]. Save before caching because it is slow; his cache took about four minutes [07:21-08:00].
Render: Redshift camera, dome light, colour tints on the pyro, bloom, denoising enabled; he says he is not strong in Redshift, so settings are by eye [08:00-10:10].

**Use it:** use this only as a pointer to the workflow; rebuild from Maxon docs before relying on any number.
