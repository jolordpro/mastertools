---
id: pipeline-usd-class-prim-edit-instances-later
title: A class prim lets you edit every instance of an asset after it is written and referenced elsewhere
domain: pipeline
tags: [usd, class prim, inherits, solaris, point instancer, primvar, per instance override, deep-read]
applies_to: USD, Solaris
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=TLJPDt4YpYM, src:yt-transcripts]
feeds: [pipeline plan]
conflicts: none
---
Keating [21:22-23:26]: an asset authored with a class prim always looks to it for additions or changes. You can then add a variant (3D glasses, horns, a hat) into that class path without hunting for where the asset is referenced, so you can still change things after writing to disk or after it is in another scene.
Per-instance variation also comes from point attributes on a point instancer: a base-color-tint primvar read by the shader overrides colour per instance [20:21-21:22]. Explore Variants spawns one reference per existing variant [19:19].

**Use it:** Pattern for many-variant scenes: variants plus class prim plus instancer attributes, not separate files.
