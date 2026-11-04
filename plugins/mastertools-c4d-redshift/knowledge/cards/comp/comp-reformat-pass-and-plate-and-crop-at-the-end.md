---
id: comp-reformat-pass-and-plate-and-crop-at-the-end
title: Reformat the background plate to the pass resolution, and crop the border at the end so unused pixels are not computed
domain: comp
tags: [reformat, crop, resolution, plate, bounding box, nuke, sarkamari, deep-read]
applies_to: Nuke 12.3
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=4A9kbUZpqIU, src:yt-transcripts]
feeds: []
conflicts: none
---
The plate was 6000 px but the passes had the custom size set in Maya, so a Reformat set the plate to the pass format [32:04-33:05]. At the end he dropped a Crop to remove the border, since the border is calculated whether seen or not, saving time [39:19-39:49]. ZDefocus on a 6K image was slow even on a strong machine, so he disabled it while working [38:17-38:47]. Arnold depth: use depth and set the output to focal plane setup, then fine-tune the plane [37:45-38:17].

**Use it:** Check for off-frame pixels and mismatched formats in comp builds; both slow renders.
