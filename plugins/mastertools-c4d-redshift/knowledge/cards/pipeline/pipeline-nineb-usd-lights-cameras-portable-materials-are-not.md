---
id: pipeline-nineb-usd-lights-cameras-portable-materials-are-not
title: USD lights, cameras and geometry come out the same in every app; shaders written for one renderer do not, which is what MaterialX is for
domain: pipeline
tags: [nine between, houdini, solaris, usd, portability, materialx, vex, karma xpu, deep-read]
applies_to: Houdini 19.5/20 Solaris
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=cE-Bbdspu_8, src:yt-transcripts]
feeds: [CHECKS, redshift]
conflicts: none
---
Everything built in a USD context (lights, cameras with focal length and aperture, geometry) should open identically in Maya or Blender [55:31]. The exception is shaders: Houdini VEX-based principled shaders are specific to Houdini and its renderers, so Arnold needs its own materials [56:03]. MaterialX is described as 'USD for materials': build once, render in Arnold, Redshift or V-Ray with a similar look [34:14-34:44, 35:45].
Karma XPU does not accept VEX shaders; displacement and subsurface break, only a preview shows [35:15].

**Use it:** Plan material handoff: moving a USD scene between renderers means rebuilding or converting shaders; MaterialX is the bridge, but check the Redshift support level.
