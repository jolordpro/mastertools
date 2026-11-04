---
id: comp-ae-linear-exr-project-setup
title: For linear EXR in After Effects: 32 bpc, working space set, Linearize Working Space on before any grading, and force-interpret 16-bit EXR as linear
domain: comp
tags: [after effects, exr, linear workflow, 32 bit, linearize working space, interpret footage, cgstirk, deep-read]
applies_to: After Effects, V-Ray/Maya EXR passes (2019)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=AxviuFLniB8, src:yt-transcripts]
feeds: [comp checks]
conflicts: none
---
CGStirk [01:32-03:05]. Project settings: use 32 bits per channel for 32-bit float EXR (the speaker leaves it at 32 all the time); set the working space (sRGB if nothing else is specified, the monitor space); tick Linearize Working Space. Do it at the start: turning it on late changes every colour correction already made. AE treats an EXR as linear only when it is 32-bit, so for 16-bit EXR open Interpret Footage > Main > Color Management and force 'Preserve RGB'-style linear interpretation on (the speaker says set it to On). Use Remember Interpretation, then shift-select the other layers and Apply Interpretation.

**Use it:** Put as a first step of any AE pass-comp checklist: depth 32, linearize on, and apply the interpretation to every pass layer. A check can flag a comp of 16-bit EXR with no linear override.
