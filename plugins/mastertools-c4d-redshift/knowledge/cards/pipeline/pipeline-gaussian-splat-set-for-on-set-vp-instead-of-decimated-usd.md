---
id: pipeline-gaussian-splat-set-for-on-set-vp-instead-of-decimated-usd
title: A gaussian splat set shows lighting and full detail on set where decimated USD looks poor, but heavy splats crash the app; use its decimate setting
domain: pipeline
tags: [gaussian splat, virtual production, usd, decimation, postshot, reality capture, jetset, blender, icosphere, deep-read]
applies_to: Jetset, Postshot, Reality Capture, Blender add-on
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=G0zHw0PbQ6A, src:yt-transcripts]
feeds: [pipeline design]
conflicts: none
---
Decimated USD with low-res materials helps framing but looks bad to cast and crew; a splat shows the scene lit and detailed [06:15][06:47]. Blender-to-splat steps via a Lightcraft add-on: render an icosphere camera track facing normals around the scene, export Reality Capture XMP metadata, run through Reality Capture, drag into Postshot [07:49][08:21]. First attempts had wrong scale and origin [06:47]. Three splat sizes tested (pause-and-save in Postshot); detailed ones crashed the app, lower ones gave a painterly look; the app has a splat decimate option in settings [08:21][08:52]. Jetset shows a splat plus a USD (animation) together and occludes the actor for nearer 3D, but splat sprites sometimes included the actor or robot [09:23][09:55].

**Use it:** prefer lit splats for approval-ready on-set previews, with a size budget set early.
