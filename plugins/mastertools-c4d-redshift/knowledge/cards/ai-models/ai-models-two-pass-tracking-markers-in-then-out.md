---
id: ai-models-two-pass-tracking-markers-in-then-out
title: Keep the camera track alive through a generative relight: include tracking markers in the mask, run once, then paint markers out in a second pass
domain: ai-models
tags: [beeble, hoon kim, conrad curtis, siggraph 2026, tracking markers, green screen, camera tracking, two pass, switchx, deep-read]
applies_to: SwitchX (2026)
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=weXc-JGwewo, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Kim [39:51-40:21]: Beeble does no separate camera solve. Users keep the green-screen tracking markers inside the mask so the generated background carries them, then run a second pass to remove the markers; the track stays valid.
Also on camera: shooting on flat gray rather than green helps if the background is complex, since a simple shot needs no screen at all [45:35-46:42].

**Use it:** if an AI step replaces a background that needs a solved camera, solve and mark first, then clean up last.
