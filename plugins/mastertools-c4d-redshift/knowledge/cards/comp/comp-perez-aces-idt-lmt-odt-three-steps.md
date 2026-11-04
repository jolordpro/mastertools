---
id: comp-perez-aces-idt-lmt-odt-three-steps
title: ACES is three standard transforms: IDT in, LMT for the look, ODT out, and comp work sits on IDT-only material
domain: comp
tags: [victor perez, foundry, fmx, aces, idt, lmt, odt, deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=Y2mcVM8c7cA, src:yt-transcripts, https://www.youtube.com/watch?v=v8P3rshGgdM]
feeds: [coach, CHECKS]
conflicts: none
---
Victor Perez (Foundry, FMX 2022) boils ACES to three steps. The IDT moves a camera, scan or sRGB image into ACES [14:12]. The ODT maps ACES to a display: sRGB monitor, Rec.709 projector or TV, Rec.2020 for HDR, P3 for cinema [16:20, 35:34]. The LMT sits between them and carries the creative intent [17:18].
Look layers he lists: the on-set CDL, a first-light grade, a chemical-style look such as bleach bypass, a saved preset, an HDR-to-SDR trim. Order matters, and it can travel in metadata [18:21-22:06].
Compositing happens after the IDT only. Nobody has graded the pixels yet [19:29].
Transfers: broadcast sports and C4D work have the same shape (render space, look, display), so the three-step picture is a good teaching frame.

**Use it:** The coach explains colour handoffs as input space, look, output transform; a scene check can ask which of the three each file has had.
