---
id: comp-grade-before-ocio-transform-glow-after
title: In Fusion with ACES: put colour correction before the OCIO colour-space node and display-referred effects after it
domain: comp
tags: [fusion, ocio, aces, grade order, sapphire, tint, gain]
applies_to: Fusion (2020 video)
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=vEoIXTbyz6o, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
[16:43] Do tints and gain before the OCIO colour space node; the same tint or gain after it works much worse.
[17:14] Some effects (Sapphire given as example) need sRGB or gamma input and want to sit after the transform.
Source space ACEScg, output sRGB (Rec.709 for broadcast) per the video.

**Use it:** give the comp coach one rule: scene-referred ops before the transform, display-referred ops after.
