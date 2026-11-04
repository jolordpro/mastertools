---
id: comp-kelly-lut-clipping-comes-from-its-bounds-not-from-luts
title: "Cullen Kelly: a LUT only destroys data if its own input range is narrower than the image, so check the range, not the label 'LUT'"
domain: comp
tags: [cullen-kelly, lut, clipping, destructive, bounds, range, polish, deep-read]
applies_to: DaVinci Resolve, any LUT
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=dSYTWErq0Vw, src:yt-transcripts, src:polish-roster]
feeds: [comp, shakedown]
conflicts: none
---
Kelly: every LUT has a fixed lower and upper input boundary. His example: Log C footage encodes to 0-1; a LUT that only spans 0.2 to 0.6 clips everything outside that band the moment it is applied [10:33-12:08]. A LUT that spans 0 to 1 and is fed Log C does not clip top or bottom. 'LUTs are destructive' is true of that LUT, not of LUTs in general.

**Use it:** When a LUT is suspected of clipping, check its input range against the working space before blaming the LUT; a check could flag any LUT whose domain is narrower than 0-1 for the working container.
