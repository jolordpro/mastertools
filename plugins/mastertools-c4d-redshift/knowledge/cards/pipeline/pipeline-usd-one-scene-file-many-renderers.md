---
id: pipeline-usd-one-scene-file-many-renderers
title: USD replaces per-renderer scene files, and one file can carry shaders for several renderers
domain: pipeline
tags: [usd, hydra, ifd, rib, ass, renderer, interchange, deep-read]
applies_to: USD, Hydra delegates
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=hBYSHFRnFlo, src:yt-transcripts]
feeds: []
conflicts: none
---
Each renderer used to have its own scene dump: Mantra reads .ifd, RenderMan reads .rib, Arnold reads .ass. Each holds geometry, lights, shaders and render settings, and the renderer reads it from disk [17:05-18:07].
USD works the same way (compose, write, render) but can also be read by any renderer with a Hydra delegate and shared across software. Shaders still have to be defined per renderer, but they can all live in the same file so the renderer can be switched [18:07-19:09]. He names Arnold, RenderMan, Redshift and V-Ray as third-party delegates [01:03-01:34].
Transfer: a Redshift look and a Karma look can sit side by side in one stage.

**Use it:** Use as the plain-words reason for USD in pipeline notes: one scene file, renderer swapped by shader set, not a re-export.
