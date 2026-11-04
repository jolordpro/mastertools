---
id: broadcast-rtings-judder-microjudder-stutter-are-three-different-faults
title: Judder is uneven frame repeat (3:2 on 24 fps over 60 Hz), micro-judder is dropped frames from de-judder processing, stutter is low-frame-rate gaps that are worse on OLED, bright and big screens
domain: broadcast
tags: [rtings, judder, micro-judder, stutter, 3:2 pulldown, 24p, 25p, 60 hz, oled, black frame insertion, motion interpolation, deep-read]
applies_to: TVs, RTINGS test bench 2.1 (2025)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=oEOkjYnsTMs, src:yt-transcripts]
feeds: [[CHECKS, shakedown, motion-critique]]
conflicts: none
---
RTINGS (display testing lab, medium). Judder [00:34-02:10]: 24 fps on a 60 Hz display uses 3:2 pulldown (alternate frames shown 3 and 2 times) so every other frame seems faster; 2:2 for 48 Hz and 5:5 for 120 Hz repeat evenly, no judder. It shows only when the stream has uneven pulldown and the TV cannot correct it; 17 of 70 TVs on the old bench could not. Test: a white square cycles 24 or 25 slots per second, 1 s exposure photo, uniform shade means even frames [02:41]; 25p over 60 Hz was not de-juddered properly by any of the first 10 TVs [03:11]. Micro-judder [03:43-05:49]: occasional dropped frames from de-judder in complex motion; shows less with native apps or match-frame-rate on the streaming box; Sony Cinemotion on High was worst in their batch. Stutter [05:49-09:27]: low-frame-rate gaps between frames; worse with sample-and-hold, OLED (instant response), higher brightness, bigger screens (10 px per frame is a larger gap on 100 in than 55 in), and pans at a speed the eye can track; individual sensitivity varies. Fixes: black frame insertion (may fight de-judder) and light motion interpolation [09:47-10:52].

**Use it:** Review vocabulary: name the artefact before asking for a fix. Pan-heavy sports graphics and 24p film looks should be checked on a 60 Hz path, not only on the edit monitor.
