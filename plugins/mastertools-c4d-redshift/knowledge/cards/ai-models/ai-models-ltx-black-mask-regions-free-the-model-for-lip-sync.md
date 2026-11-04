---
id: ai-models-ltx-black-mask-regions-free-the-model-for-lip-sync
title: With audio, the control passes fight the mouth; a mask whose black area covers the mouth or face lets the model animate it
domain: ai-models
tags: [ai render, ltx, lip sync, mask, audio, facial animation, mickmumpitz, deep-read]
applies_to: LTX 2.3 (2026)
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=7J7hi-Hxpac, src:yt-transcripts]
feeds: []
conflicts: none
---
Mickmumpitz [03:37-04:40, 13:59-15:01]. Adding audio to depth plus outline guidance failed because the passes say nothing moves at the mouth. Fix: a black and white mask where white means follow the control precisely and black means free to generate. Black over the mouth gives lip sync; black over the whole face gives facial animation. The mask was made by laying a rough mask over the layout render in After Effects; rough is enough. The voice track must be dialogue only, no music, and at least as long as the video, or the model invents gibberish after it ends [14:30]. Lip sync is good close to camera and falls apart when the character is far away [21:13].

**Use it:** Treat 'where may the model invent' as an explicit mask when any AI step is allowed to touch part of a frame.
