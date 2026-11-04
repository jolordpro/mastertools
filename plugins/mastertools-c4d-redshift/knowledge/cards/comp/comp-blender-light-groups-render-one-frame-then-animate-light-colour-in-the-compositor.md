---
id: comp-blender-light-groups-render-one-frame-then-animate-light-colour-in-the-compositor
title: Render one frame with light groups, save each light pass with its alpha, and animate each light's colour or strength in the compositor; Blender 3.2 alpha could not do it with shadow catcher or HDRI lighting
domain: comp
tags: [motion-dreams, blender, light groups, relight, compositing, file output, deep-read]
applies_to: Blender 3.2 alpha (2022)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=HA6B5iYxwUI, src:yt-transcripts]
feeds: [composition]
conflicts: none
---
Three lights (key, fill, rim) each get a light group pass in the view layer and are assigned in each light's shading panel [01:34]. In the compositor each pass is denoised, then combined with Mix set to Add [02:05-02:38]. Because they are separate, you can change shadow depth, boost a rim with Exposure, or tint a light with Multiply, all without re-rendering [02:38-03:40]. For an animation he saved each pass as RGBA PNG through a File Output node, using Set Alpha to give the passes an alpha, then in a new file animated the pass colours over a background and rendered [03:40-04:43]. Limits in that alpha build: not working with a shadow catcher object or with HDRI lighting [05:14].

**Use it:** Version caveat: check current Blender before using. Supports comp-light-group-relight-limits-ae-vs-nuke.
