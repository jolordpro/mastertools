---
id: comp-shadow-matte-invert-multiply-and-clone-the-transform
title: Shadow matte over a plate: invert it, Multiply onto the background, adjust with ColorCorrect, and clone the transform so shadow and colour line up
domain: comp
tags: [shadow matte, multiply, background plate, transform clone, alt k, nuke, sarkamari, deep-read, reza, arnold, merged aov, shadow catcher, invert, premult]
applies_to: Nuke 12.3
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=4A9kbUZpqIU, src:yt-transcripts, https://www.youtube.com/watch?v=xwD_UPqbmCU]
feeds: [comp, CHECKS]
conflicts: none
---
The useful part of the shadow pass is white, so invert it; it then looks like AO [31:01]. Multiply (not over) onto the background plate, not into the character's colour path [31:34-33:36]. Premult first; reduce shadow strength with ColorCorrect gamma, not mix, and scale it with a Transform (1.2 in his case) [34:07-35:12]. Clone the transform (Alt-K) to the colour pass so both stay aligned [35:42]. Then merge foreground over the background, and add small grade tweaks to the foreground to match [36:12-37:14].
Merged from `comp-shadow-catcher-invert-premult-multiply-over-background`: Reza [23:49-26:58]: the shadow pass is white where shadow falls; invert it, premult, then Merge (multiply) over the background, aligned. Gamma on a color correct changes density to match plate richness; add a blur if edges are hard. Reformat the plate (a 6000x4000 background vs a smaller render) first.

**Use it:** A basic recipe for a CG object on a plate; check the shadow direction against the plate's shadows.
