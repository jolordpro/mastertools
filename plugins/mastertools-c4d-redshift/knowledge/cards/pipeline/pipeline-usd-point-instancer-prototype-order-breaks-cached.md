---
id: pipeline-usd-point-instancer-prototype-order-breaks-cached
title: Per-frame cached point instancers break when the prototype list changes between frames; reorder prototypes by occurrence
domain: pipeline
tags: [usd, point instancer, prototypes, copy to points, cache, proto indices, luca scheller, deep-read]
applies_to: Houdini Solaris / OpenUSD
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=VSE7ayrRStg, src:yt-transcripts]
feeds: []
conflicts: none
---
Point instancers store positions and orientations as arrays with a prototype relationship list and proto indices [43:04]. In Houdini, scrubbing live looks right, but caching to disk can show the wrong shapes because the prototypes map differently per frame [44:07-44:38]. The fix is to reorder points and prototypes based on which prototypes occur across the range, using a side-car attribute [44:38-45:40]. Relationships and composition arcs are not animatable; only attributes carry animation [43:04]. Give artists one path attribute and let the pipeline handle the rest [45:08].

**Use it:** A render-checker for USD instancers should compare live and cached instance appearance.
