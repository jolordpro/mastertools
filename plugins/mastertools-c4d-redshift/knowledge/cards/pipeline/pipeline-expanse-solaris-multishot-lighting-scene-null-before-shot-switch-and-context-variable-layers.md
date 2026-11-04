---
id: pipeline-expanse-solaris-multishot-lighting-scene-null-before-shot-switch-and-context-variable-layers
title: Expanse's Solaris multi-shot lighting scene: null nodes before the shot switch, global overrides, light-group prefix, and a submitter-name context variable that picks the render layer
domain: pipeline
tags: [pipeline, expanse, solaris, multi-shot, shot switch, light groups, render layers, houdini, deep-read]
applies_to: Houdini Solaris, Karma XPU, Prism 2
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=jfH7JpjDO_w, src:yt-transcripts]
feeds: []
conflicts: none
---
Seven shots and three light set-ups in one scene [37:41-38:11]. Prism import nodes bring in each shot, with a null between each import and the shot switch so shots can be edited without breaking the switch; global overrides and a procedural preview toggle (global context variable) sit below [38:11-38:45]. A modified background-plate node reads the image plane from the Maya camera so the plate and the export filter match animation [38:45-39:18]. Blockers and reflectors come from a grid asset so artists need no shader or folder knowledge; default lights carry light group names, and a prefix is added to every light group name for later scripting [39:18-39:49]. Light linker and mixer follow. Render layers: the last word of the submitter name is a context variable that selects the layer [39:49]. Renderer used for the film: Karma XPU with MaterialX and a custom Karma fur shader [56:54-57:24].

**Use it:** Build shot-level edits behind nulls and drive layer choice from the job name so farm submission is a naming convention.
