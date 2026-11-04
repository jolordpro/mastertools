---
id: comp-perez-aces-cg-renders-straight-to-acescg
title: Render CG straight into ACEScg so no input transform is needed; if a render is in sRGB, give it the sRGB IDT and avoid doing that
domain: comp
tags: [victor perez, foundry, fmx, aces, cg, renders, input transform, deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=Y2mcVM8c7cA, src:yt-transcripts]
feeds: [redshift, CHECKS]
conflicts: none
---
CG renders can be written directly in ACEScg, the working space, so the read needs no IDT [31:53]. If renders come in another format, apply the matching IDT; sRGB renders get the sRGB one. His joke-with-a-point: don't render in sRGB [32:24].
Files from another facility arrive as ACES-compliant EXR; set the read to ACES2065-1 and that is all [32:55].

**Use it:** Redshift or C4D renders for comp: save EXR in the ACES working space the show uses, and tag the file so the comp artist sets no guess.
