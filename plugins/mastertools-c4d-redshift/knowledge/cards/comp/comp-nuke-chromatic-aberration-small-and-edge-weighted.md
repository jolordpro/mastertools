---
id: comp-nuke-chromatic-aberration-small-and-edge-weighted
title: Add chromatic aberration as a tiny scale difference centred on the frame, and crop before it to avoid colour edges
domain: comp
tags: [alex, levelup plus vfx, nuke, chromatic aberration, lens, crop, bounding box, deep-read]
applies_to: Nuke, AP chroma tool
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=ETV1VTV0vNg, src:yt-transcripts]
feeds: [comp]
conflicts: none
---
His rule: never overdo it; it should be barely felt [04:36]. With his tool the effect comes from the scale value, which must be only a hair away from 1 (about 1.05 in the end after trying lower; the captions are muddled on the exact digits) [43:12-43:43].
Centre the effect on the input, since real lenses show it more at the edges than the middle [43:43-44:15]. A big bounding box leaves a red or blue edge at the frame bottom, so crop before the node [44:15-44:47].
He says some people dislike it but he finds it adds realism [44:15].

**Use it:** supports the existing lens-match card with a concrete magnitude and the crop gotcha.
