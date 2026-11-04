---
id: comp-kelly-scene-space-looks-beat-display-space-luts
title: "Cullen Kelly: a look built in scene space beats a Rec.709 LUT forced into a wide-gamut pipeline; his 2383 LUT shows the workaround"
domain: comp
tags: [cullen-kelly, lut, 2383, film print, scene referred, display referred, rec709, hdr, polish, deep-read]
applies_to: DaVinci Wide Gamut
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=dSYTWErq0Vw, src:yt-transcripts, src:polish-roster, https://www.youtube.com/watch?v=Hlj5ep-85ys]
feeds: [comp, coach]
conflicts: none
---
A 709 LUT can be used inside a DWG project, even after a colour-space-transform sandwich, but likely leads to artifacts and clipping [52:38-53:09]. His 2383 LUT is the exception he built on purpose: a film print is display-referred and low dynamic range, so he profiled real 2383 data and carefully expanded it back to wide-gamut scene space [53:09-54:09]. V1 to v2 changed only the negative profile, which fed the print stage better and got closer to the stock designers' intent [57:46-58:16]. The ideal remains looks that start and end in scene space, like his Element LUTs, which borrow 2383's red density without leaving scene space [54:09-55:09].

**Use it:** Build and store look LUTs in the working (scene) space; when a display-referred reference exists, treat expanding it back to scene space as a deliberate, tested step.
