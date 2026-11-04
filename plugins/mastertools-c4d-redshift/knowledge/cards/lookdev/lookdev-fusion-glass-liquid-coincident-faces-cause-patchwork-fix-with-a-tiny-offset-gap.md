---
id: lookdev-fusion-glass-liquid-coincident-faces-cause-patchwork-fix-with-a-tiny-offset-gap
title: Autodesk Fusion render: liquid sharing faces with a glass shows a patchwork; offset the liquid face inward by a fraction of a millimetre so they do not touch
domain: lookdev
tags: [fusion, autodesk, glass, liquid, coincident faces, ray tracer, offset, press pull, deep-read]
applies_to: Autodesk Fusion (renderer-agnostic principle)
status: V
confidence: medium
decay: slow
read: 2026-10-31
recheck_by: 2029-10-31
sources: [https://www.youtube.com/watch?v=9yZCElLDRH4, src:yt-transcripts]
feeds: [lookdev, CHECKS]
conflicts: none
---
Autodesk QA engineer answering a user question [00:10-04:48]. Cause: in a ray tracer, two materials stuck side by side have coincident faces and the engine cannot tell which should apply to the ray crossing that interface [00:42]. Boundary Fill made a liquid body from the cup but still rendered a patchwork quilt [02:15-03:16]. Fix: name the bodies, hide the glass, Press/Pull the liquid face by a fraction of a millimetre (he used about 0.05, said unclear in captions), turn the glass back on: a tiny gap, clean render [03:16-04:18]. It worked in one move because the cup interior was tangent-continuous, so all faces moved together; with hard breaks, select every face that must move [04:18-04:48].

**Use it:** Same rule for C4D and Redshift liquids: never leave the liquid surface exactly on the glass surface. Supports the nested dielectric cards.
