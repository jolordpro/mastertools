---
id: comp-resolve-color-managed-beginner-setup-wide-gamut-intermediate-and-per-clip-input
title: Resolve colour managed starter setup: automatic off, HDR DaVinci Wide Gamut Intermediate preset, output 709 G2.4, then set each clip's input space
domain: comp
tags: [[resolve, davinci-wide-gamut, input-color-space, setup, cullen-kelly], deep-read]
applies_to: DaVinci Resolve 17-era
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=TxCGR_gNTME, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Cullen Kelly's order [04:17-05:18][09:26-11:31]: Project Settings, Color Management, DaVinci YRGB Color Managed; turn off automatic colour management (it hides what is happening); processing mode = HDR DaVinci Wide Gamut Intermediate unless you have a reason; output colour space Rec.709 Gamma 2.4; save. The preset hides the input space, so you must still right-click clips and set Input Color Space to the camera's (Alexa Log C in his example); select all clips and set at once if they share one space [10:31-11:31].
For ACES the equivalent is project settings: ACES cct, input transform of the camera, output transform for the mastering display, after which all log clips normalise at once [01:37-02:42].

**Use it:** CHECKS item: if clips arrive in a managed timeline without an input colour space tag, flag it before grading.
