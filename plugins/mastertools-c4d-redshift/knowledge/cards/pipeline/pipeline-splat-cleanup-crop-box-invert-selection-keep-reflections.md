---
id: pipeline-splat-cleanup-crop-box-invert-selection-keep-reflections
title: Clean splat floaters with a crop box and an inverted selection, but keep reflection splats because a reflection is itself a splat
domain: pipeline
tags: [gaussian splatting, crop box, floaters, cleanup, reflections, file size, deep-read]
applies_to: Postshot
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=ERuRMOVO58Q, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Two tools: select-and-delete, and a crop box that keeps only splats inside it [09:20]. Align the box to the grid, scale it to contain only what is needed; this also cuts export size [09:51]. Faster than deleting strays: select the area you want, invert, delete (about 200,000 splats gone in one step) [10:22]. Caution: a glass bowl's highlight is a splat that fades in by view direction, so a mirror becomes a mirror dimension of splats; delete only what is clearly out of bounds [10:52][11:23]. A depth-limited selection helps in hard to pick spots [11:23]. Result: a detailed scene exported as a .ply at about 122 MB [12:25].

**Use it:** cleanup order for the checker: crop, invert-delete, then local depth select, and flag any deletion near glass or shiny areas.
