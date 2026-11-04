---
id: ai-models-project-ai-concept-render-back-onto-blocking-geometry
title: Prototype a set extension by rendering a depth-guided AI image from a block-out, then projecting it on the geometry
domain: ai-models
tags: [ai environment, projection, set extension, depth conditioned, prototype, background foreground split, deep-read]
applies_to: Blender, Flux depth blueprint
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=o5ZqrVNoeiI, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
He built the layout from simple cubes, ran a depth-conditioned Flux (Nvidia blueprint) with different prompts and seeds, and projected the result back from the camera view (UV project from view, image as texture) [01:55-03:09]. Moving the camera too far breaks the background; so he generated foreground and background separately and combined the shaders with a mask, giving a scene in about half an hour to an hour [03:09]. Shot basis: After Effects camera track brought into Blender, iPhone scan of the car park, Houdini crowd with Mixamo animations [01:06-01:37]. The Nvidia part is a sponsor segment.

**Use it:** an option for cheap pitch backgrounds; check client AI permission first (see agencies-check-ai-permission-before-upload).
