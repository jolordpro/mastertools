---
id: comp-normals-relight-add-detail-then-mix
title: Normal-based relight looks plasticky until fine detail is mixed into the normals and reoriented to the base normals
domain: comp
tags: [normals, relight, nuke, detail normals, frequency separation, normal mixer, plastic look]
applies_to: Nuke (Compositing Academy normals toolkit, Apr 2026)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=M-iKJu9hYBk, src:yt-transcripts]
feeds: [comp planner, composition]
conflicts: none
---
[02:03] Low-resolution proxy normals give sharp triangles and a plastic look. The fix [02:35]: generate detail normals from the image, by luminance or by frequency (detail size), and mix them into the base normals.
[03:05] The mixer reorients the detail normals to face the same direction as the base; random orientations break relighting. [05:42] Normals made from the image alone do not follow the model's curvature, so always mix with the render's normals.
Detail can be targeted with a roto and strength knob [06:44].

**Use it:** comp relight tip: pass the render normals through a detail mix before adding light.
