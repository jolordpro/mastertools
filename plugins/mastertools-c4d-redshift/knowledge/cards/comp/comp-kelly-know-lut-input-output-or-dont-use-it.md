---
id: comp-kelly-know-lut-input-output-or-dont-use-it
title: "Cullen Kelly: never use a LUT unless you know its input space, output space and type; an unlabelled LUT is a red flag"
domain: comp
tags: [cullen-kelly, lut, input color space, output color space, metadata, red flag, film look, polish, deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=dSYTWErq0Vw, src:yt-transcripts, src:polish-roster, https://www.youtube.com/watch?v=q1UuKhdmAyU]
feeds: [comp, shakedown, coach]
conflicts: none
---
LUTs are picky eaters: feed one the wrong thing and sooner or later it misbehaves, and that is the user's error [17:17-18:47]. Minimum to know: type, expected input space, delivered output space. Where to find it: the LUT's own header text (his Element LUTs state DaVinci Wide Gamut Intermediate in and out; open in a text editor or Lattice), then the file name (Log C to 709 tells you both ends), then ask the designer [55:39-58:16]. Resolve's film looks tell you the output (Rec.709) but expect film negative, which has no strict colour space, so they only suit scanned negative delivered in SDR [56:43-57:46]. If the designer did not label it, treat as a sign the LUT was not carefully built [58:16-58:46].

**Use it:** Add an intake check for any LUT or preset: input space, output space, type recorded before it enters a pipeline; reject unlabelled ones.
Transcript support: a LUT assumes an input encoding: Gorilla Grade LUTs expect gamma 2.2, so the display gamma must be set to match (https://www.youtube.com/watch?v=q1UuKhdmAyU [01:33-02:05])
