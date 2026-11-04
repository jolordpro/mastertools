---
id: pipeline-solaris-one-scene-many-hydra-delegates-same-lights-and-materials-clusters
title: In Houdini Solaris one USD stage renders in Karma, RenderMan, Arnold or Redshift just by switching the viewport's Hydra delegate; shading may differ per renderer
domain: pipeline
tags: [solaris, hydra, usd, karma, renderman, arnold, redshift, delegate, deep-read]
applies_to: Houdini 18.0 Solaris, 2020
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=q-vXgQYDUL8, https://www.youtube.com/watch?v=lidw4rllGV4, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
The viewport always runs through Hydra, even the OpenGL view; the Storm delegate is a Hydra sample [q-vXgQYDUL8 09:55-10:57]. Changing the delegate re-renders the same scene live; the first render in RenderMan or Arnold takes longer to initialise [10:57-11:29].
Shading differs between renderers since each has its own algorithms; for exact looks use the renderer-specific features [13:02-13:32].
Materials are made as a cluster: Karma principled, Arnold, Redshift and RenderMan shaders side by side, each built as the artist already knows [14:02-14:33].
Hydra acts as a translator: a generic light is turned into whatever light the active renderer needs, so there is no Arnold light or RenderMan light node [lidw4rllGV4 08:17-09:51, 12:58-15:05].

**Use it:** Concept source for a renderer-agnostic USD shot pipeline: author once, check in several renderers.
