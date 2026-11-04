---
id: comp-spring-grade-in-the-edit-16bit-linear-exr-and-film-grain
title: Spring graded at the end in the edit on adjustment layers from 16-bit linear EXR, then added subtle grain plates to unify denoised frames
domain: comp
tags: [grading, 16-bit exr, film grain, filmic, adjustment layers, tiff, ffmpeg, delivery, deep-read]
applies_to: Blender sequencer, Filmic
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=aR3yNNGK_sc, src:yt-transcripts]
feeds: [CHECKS, elevate]
conflicts: none
---
Comp output was 16-bit EXR, linear, saved to the shots folder to save space since multilayer data was no longer needed [37:29]. Grading ran in the edit using adjustment layers on those frames, with the edit in Filmic, only small corrections to match shots [37:29] [38:00]. A generalised film look added warmth to highlights and a bit more contrast in shadows [38:30].
Subtle noise plates went over everything because the frames mixed denoised and real noise; this was to make the result feel organic [38:30] [39:00]. Output was a 16-bit TIFF sequence, then ffmpeg for the web [39:00] [39:32]. He corrects a slide error: 16 bit, not 12.

**Use it:** Delivery pattern: grade once in the edit from linear half-float frames, grain last, output a 16-bit intermediate, encode from that.
