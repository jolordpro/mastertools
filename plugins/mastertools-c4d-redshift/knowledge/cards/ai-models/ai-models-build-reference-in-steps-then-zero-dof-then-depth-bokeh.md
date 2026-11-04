---
id: ai-models-build-reference-in-steps-then-zero-dof-then-depth-bokeh
title: Build AI reference frames in steps (clean 3D, background, figures) and with zero depth of field, then add bokeh from a depth map
domain: ai-models
tags: [beeble, hoon kim, conrad curtis, siggraph 2026, moyslab, blender mcp, depth map, bokeh, step by step, gaussian splat, reference, deep-read]
applies_to: any
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=weXc-JGwewo, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Moyslab (Italy) [19:19-22:33]: 90-minute comedy with twelve fantasy locations. For each: a world generated as Gaussian splat, mesh exported as GLB, cleaned and remodelled in Blender with a Blender MCP, two stand-in figures added, camera framed in 3D, background retextured with an image model, then gray figures replaced by real humans, then SwitchX.
Kim: doing it all in one inference run breaks the AI, so split into steps for control [21:30].
All reference images were made with zero depth of field; a depth map taken afterward sets the bokeh for each shot before SwitchX [22:00].

**Use it:** for any AI-assisted shot, stage the work: layout, background look, subject, then lens effects, so each step can be fixed alone.
