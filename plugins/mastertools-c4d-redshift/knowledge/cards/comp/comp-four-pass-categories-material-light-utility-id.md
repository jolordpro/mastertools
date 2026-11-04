---
id: comp-four-pass-categories-material-light-utility-id
title: Render passes fall in four jobs: material AOVs, light groups, utilities, and IDs
domain: comp
tags: [render passes, aovs, light groups, utilities, id mattes, beauty rebuild, data passes, deep-read]
applies_to: Nuke, Redshift/Arnold/Octane passes
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=UCUXhXKDnWQ, src:yt-transcripts]
feeds: []
conflicts: none
---
Tony Lyons (CompositingMentor). Two big groups [00:30-01:16, 07:51-08:22]. Beauty-rebuild passes recreate the beauty: material AOVs (diffuse, specular, reflection, SSS, refraction, texture/colour, emission, raw lighting) change the shader, and light groups (key, rim, fill, HDRI, emitting objects) change intensity, colour or temperature per light. Data passes are helpers: utilities (depth, motion vectors, normals, position, ambient occlusion, UVs) feed defocus, motion blur and relight; IDs (RGB object IDs, texture IDs, Cryptomatte) exist only to cut mattes. He keeps IDs separate from utilities because they have one purpose [05:15-06:47].
His naming habit: when he says AOVs alone he means material AOVs [02:05-02:37].

**Use it:** Group a pass list by these four jobs before choosing what to render for a shot; skip categories the comp will not use.
