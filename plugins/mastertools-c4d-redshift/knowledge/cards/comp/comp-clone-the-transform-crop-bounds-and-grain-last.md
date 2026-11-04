---
id: comp-clone-the-transform-crop-bounds-and-grain-last
title: Share one cloned transform between shadow and colour, crop after heavy nodes, and add grain last
domain: comp
tags: [sarkamari, reza, nuke, arnold, merged aov, transform, clone, crop, bounding box, grain, expensive nodes, zdefocus, deep-read]
applies_to: Nuke
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=xwD_UPqbmCU, src:yt-transcripts]
feeds: [comp]
conflicts: none
---
Reza [27:30-34:19]: moving the shadow requires the same move on colour, so Alt-K clones the Transform; match grade with a Grade (reduce gain, gamma up, slight red). ZDefocus with depth set to depth, focal point, output focal plane; falls back to CPU if the GPU errors. Add a Crop after processing-heavy nodes so nothing outside the frame is computed [31:12-32:45]. Grain (a preset) goes last because it is expensive, helping a clean foreground sit on a noisy plate [33:16].

**Use it:** keep clones for shared moves and put grain at the very end of a comp.
