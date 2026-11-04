---
id: pipeline-nineb-usd-primvar-renames-cd-n-p-uv-v
title: On USD export Houdini attributes are renamed (Cd to displayColor, uv to st, N to normals, P to points, v to velocities); custom ones keep their names
domain: pipeline
tags: [nine between, houdini, solaris, usd, primvar, attributes, displaycolor, velocities, deep-read]
applies_to: Houdini 19.5/20 Solaris
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=cE-Bbdspu_8, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Standard attributes get USD names so apps agree: Cd becomes displayColor, N normals, P points, uv st, v velocities [1:52:20-1:53:24]. A custom attribute (his 'mask') keeps its name [1:50:46-1:52:20].
A shader reads a primvar with a geometry-property-value node; the name is case-sensitive and the type must match (color3f) [1:54:26-1:55:27]. Example use: a 0-1 mask primvar drives a mix between two materials, like dirt and grass [1:55:27-1:56:00].

**Use it:** When a colour or mask 'doesn't arrive' in the other app, check the primvar name on the prim before blaming the shader.
