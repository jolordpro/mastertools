---
id: comp-frame-merge-with-motion-vectors-ghosting-and-forward-reverse-check
title: Merging neighbour frames with motion vectors ghosts wherever background is revealed; compare forward and reverse vectors to mask mismatched areas
domain: comp
tags: [motion vectors, temporal denoise, ghosting, forward reverse vector, displace node, frame blending, compositing, deep-read]
applies_to: Blender compositor, Cycles Vector pass
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=jyGQIKOPwGA, src:yt-transcripts]
feeds: [comp, redshift]
conflicts: none
---
Vector pass gives X/Y motion per pixel, two vectors in RGBA: to previous and from next frame; the debug view colours hue as direction and luminance as distance [02:47][03:19][03:54]. Displacing neighbours by vectors leaves a ghost copy: where the object moved away, the revealed background has a zero vector, which maps the old picture back into place, and shadows are not displaced [04:30][05:01][05:33]. Check: reverse vector of the current frame plus forward vector of the previous frame should return to the start; when they are not opposite, the frames do not match there and the area is masked out of blending [06:05][06:37][07:10]. Shadows still need a tight luminance threshold [07:10].

**Use it:** mask-by-vector-consistency is the idea behind any temporal merge in comp; relevant when using Redshift motion vector passes.
