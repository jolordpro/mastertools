---
id: comp-png-bakes-colour-and-is-slow
title: PNG bakes colour, cannot hold passes, and a trainer says it is slower than EXR to read at 4K and above
domain: comp
tags: [png, exr, speed, multipass, 8-bit, after effects]
applies_to: After Effects, any renderer
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=IcLiz8e8ffc, src:yt-transcripts, https://www.youtube.com/watch?v=le17-h6tUD0]
feeds: [coach, CHECKS]
conflicts: none
---
A PNG beauty with the ACES view baked in is fine for simple curve and glow work, but not for multipass compositing [1:41:48].
Claim: EXR with good compression is faster than PNG in After Effects, and PNG is several times slower from about 4K; the chart was on screen and not described [1:42:42-1:44:18]. Treat the size of the gap as unsure.
Trainer's advice is that PNG has no reason to be used when passes or speed matter; the host says keep a working workflow.

**Use it:** use half-float EXR for comp deliveries and PNG only for baked finals.
