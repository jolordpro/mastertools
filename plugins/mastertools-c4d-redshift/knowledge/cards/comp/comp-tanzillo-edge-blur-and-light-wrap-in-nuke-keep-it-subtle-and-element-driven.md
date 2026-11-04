---
id: comp-tanzillo-edge-blur-and-light-wrap-in-nuke-keep-it-subtle-and-element-driven
title: Tanzillo's Nuke edge blur and light wrap - shuffle alpha to RGB, edge-detect, soften the edge 1 to 2 px, add a light wrap, and drive hair-only wrap from the hair element
domain: comp
tags: [mike-tanzillo, nuke, light-wrap, edge-blur, integration, edge-detect, deep-read]
applies_to: Nuke
status: V
confidence: medium
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=cP3AELeZf6o, src:yt-transcripts]
feeds: [comp, post-composite]
conflicts: none
---
Two ways to soften a CG subject into its plate [13:26-21:26]:
1. **Edge blur:** shuffle the alpha into RGB for a solid shape, run Edge Detect on that (the default edge detect on the beauty gives odd internal edges), erode and shrink the band, then blur the band itself so it does not look drawn. He says usually a one or two pixel blur, and the demo was deliberately extreme. Use the band as a mask to blur the subject slightly [14:03-15:38].
2. **Light wrap node:** feed foreground and background; it wants a bright background. Raise intensity to see it, use "generate wrap only" to get the wrap alone, and plus it back over the character in a separate node [16:08].
Goal: not pixel-perfect; a 2D photo has a soft edge bleed between objects, and it must not be obvious [16:38].
For animation, do not hand-draw a roto: take the hair render element, erode it, blur it about 50, and use that as the mask so the effect follows the head [19:47-21:26].

**Use it:** in comp for C4D + Redshift, build the edge mask from an object-ID or cryptomatte element instead of animated roto; keep wrap strength low.
