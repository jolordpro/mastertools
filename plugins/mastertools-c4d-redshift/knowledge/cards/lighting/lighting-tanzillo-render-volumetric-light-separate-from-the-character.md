---
id: lighting-tanzillo-render-volumetric-light-separate-from-the-character
title: Render volumetric light separately from the character so it does not wash out values or ruin the character's core
domain: lighting
tags: [mike-tanzillo, volumetrics, render-layers, pipeline, compositing, deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=sTCeHUto1IM, src:yt-transcripts]
feeds: [lighting, redshift, post-composite]
conflicts: none
---
Tanzillo [13:43-14:13]: always render the volumetric light apart from the character. Volume in the same render washes out values and bakes in sharp shadows at the edges. Keeping the character alone lets you hold its core look and mix the volume back in comp. A cat in the same session mixed a room-light layer with a volumetric-and-character-light layer at different strengths [57:17 T1]. He called the combined version a source of headaches [14:13 T2].

**Use it:** in C4D + Redshift, render volume light as its own pass or layer (check the redshift skill for the exact pass name) and add it back.
