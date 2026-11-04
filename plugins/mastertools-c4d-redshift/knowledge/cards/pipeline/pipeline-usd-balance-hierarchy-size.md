---
id: pipeline-usd-balance-hierarchy-size
title: Balance USD hierarchy size: not a prim per tiny thing, and not one prim with 50 million points
domain: pipeline
tags: [usd, hierarchy, prims, granularity, lighting artists, luca scheller, deep-read]
applies_to: OpenUSD, Houdini Solaris
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=VSE7ayrRStg, src:yt-transcripts]
feeds: []
conflicts: none
---
Create enough prims for the lighter to filter, assign materials and hide things, because that is what they do at the end [33:35]. Avoid a prim for every little element, and avoid one prim holding millions of points since caching gets heavy [34:07]. In Houdini LOPs, driving an import from one path attribute keeps this simple for artists; relative paths (no leading slash) go under the import prefix [34:39-35:42].

**Use it:** Add 'prim count and size' to scene-check thinking for USD handoffs: both extremes cost something.
