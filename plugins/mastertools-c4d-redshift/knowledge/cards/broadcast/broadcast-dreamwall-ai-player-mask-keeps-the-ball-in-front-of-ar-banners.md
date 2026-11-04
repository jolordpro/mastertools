---
id: broadcast-dreamwall-ai-player-mask-keeps-the-ball-in-front-of-ar-banners
title: Ball vanishes behind virtual banners; DreamWall fixed it with an AI-made real-time mask of players and ball layered above the AR
domain: broadcast
tags: [dreamwall, thibault baras, ar, occlusion, ai mask, ball, virtual banners, virtual advertising, matte, zero density, spain, deep-read]
applies_to: Zero Density Reality Engine plus a third-party AI mask (2021)
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=cE3jw6MO9kw, src:yt-transcripts]
feeds: []
conflicts: none
---
The AR problem: virtual boards cover the ball and players unless something cuts them out [1:24:16]. Baras describes two fixes. Spain's method puts real colour banners on the stand so a key can protect the ball. DreamWall could not do that, so they worked with an AI company: it detects players and the ball in real time and outputs a mask (shown in blue) with a confidence value [1:25:55-1:27:04].
The mask becomes a layer on top of the AR, so virtual objects sit behind anything that moves, and real LED content can be replaced or virtual added [1:27:36-1:28:07]. He notes the model was trained to find moving elements such as players, and he does not name the vendor.

**Use it:** When planning in-stadium AR, put a moving-object mask on the checklist, with a fallback of real colour banners if no AI mask exists.
