---
id: pipeline-usd-one-material-per-renderer-plus-preview-surface
title: On a USD asset, assign two materials: a renderer-specific one and a USD preview surface, and the right one shows
domain: pipeline
tags: [pipeline, usd, materials, preview surface, 3delight, renderer, redshift, karma, deep-read]
applies_to: Houdini Solaris, 3Delight (captioned 3D light)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=CpiumJctktM, src:yt-transcripts]
feeds: [CHECKS, redshift]
conflicts: none
---
Materials were built in Houdini for 3Delight; in another USD renderer such as Karma or Redshift the workflow is the same but the material type differs [09:09]. A viewport showed the asset grey, because the viewer only understood the preview material, so he created both a 3Delight material and a USD preview surface, assigned both to the asset with a collect node [10:52] [11:23]. The correct one displays depending on renderer [11:23].
A Q&A answer says USD can store shaders and parameters, but whether materials export depends on the renderer and the Maya USD plugin [40:48] [41:18] [41:52].

**Use it:** Plan for USD: a viewport-safe preview material plus one per renderer. Do not assume Redshift materials survive a USD export.
