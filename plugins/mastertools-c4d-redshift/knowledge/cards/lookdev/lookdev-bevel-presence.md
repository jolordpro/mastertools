---
id: lookdev-bevel-presence
title: Perfectly sharp edges read as fake; bevels catch the highlight, 2-3 segments is often enough, but no width-to-size rule exists
domain: lookdev
tags: [lookdev, bevel, edge highlight, hard edges, modelling, material]
applies_to: any
status: V2
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [src:research-production-pipelines, https://www.youtube.com/watch?v=kN00Z7UsW5U, src:yt-transcripts]
feeds: [PLAN geometry hygiene]
conflicts: none
---
Sources agree on the principle (novedge, Marmoset); no published rule for bevel width relative to object size.
Check presence first: count hard edges above an angle threshold that have zero bevel width.

Transcript support: A rim only forms on curved edges; a 0.02 fillet already works; Round Corners node is the shader fake. (https://www.youtube.com/watch?v=kN00Z7UsW5U [15:08])
