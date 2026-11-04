---
id: pipeline-usd-small-facts-extent-singleton-lazy-read
title: USD small gotchas: set extent on boundable prims, layers are one-per-session singletons, relationships are not animatable, files read lazily
domain: pipeline
tags: [usd, extent, bounding box, primvars, singleton layer, lazy loading, gotchas, luca scheller, deep-read]
applies_to: OpenUSD
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=VSE7ayrRStg, src:yt-transcripts]
feeds: []
conflicts: none
---
Always set the extent on boundable types or bounding-box lookups fail [40:59]. A layer exists once in memory, so copying content into one layer can make two nodes show the same data [19:29-20:00]. Binary USD files read lazily, so even a very large data set (a reported 1.5 TB case) can be traversed in seconds [21:34]. Only primvars (prefixed) get exported to the renderer, and are how render settings or display colour are set [10:08-10:38]. Array attributes expose NumPy buffers for fast editing in Python [12:11]. Houdini stores a temporary node ID in metadata, stripped on write, handy for jumping to the node that made an edit [55:03].

**Use it:** Reference list for debugging odd USD results.
