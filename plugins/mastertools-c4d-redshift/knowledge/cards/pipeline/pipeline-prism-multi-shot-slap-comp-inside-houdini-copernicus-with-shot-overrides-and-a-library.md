---
id: pipeline-prism-multi-shot-slap-comp-inside-houdini-copernicus-with-shot-overrides-and-a-library
title: Prism multi-shot slap comp in Houdini Copernicus: lighting artists see the comped shot in the viewport, with per-shot color corrections published as versioned recipes
domain: pipeline
tags: [pipeline, prism, slap comp, houdini, copernicus, multi-shot, library, deep-read]
applies_to: Houdini Copernicus, Prism 2 (FMX 2026)
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=jfH7JpjDO_w, src:yt-transcripts]
feeds: []
conflicts: none
---
Scene building now creates a shot switch plus a slap comp with a section per shot [44:31-45:32]. A color correct added for one shot shows in the viewport and not on others; the nodes publish as a versioned slap comp, with the final renders able to apply it automatically [45:32-46:04]. Using Houdini recipes, node groups can be saved into a Prism library with a custom thumbnail for studio or project reuse [46:04-46:34]. Nuke 16/17 graph-scope variables give a matching shot-switch multi-shot comp, with per-shot overrides per render layer, and submission as separate Deadline jobs [46:34-47:35]. Prism's native render manager in Solaris lists passes and shot overrides and sends them to the farm [14:51-15:28].

**Use it:** Give lighting a live comped view per shot and publish shot-level corrections as versions.
