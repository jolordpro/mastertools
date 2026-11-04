---
id: redshift-metal-scratch-blend-add-not-multiply
title: Blend scratch roughness onto a roughness stack with Add or Screen, not Multiply, and feed micro scratches through height
domain: redshift
tags: [polygon division, redshift, metal, scratches, roughness, add, screen, swirl marks, substance, deep-read]
applies_to: Cinema 4D 2024, Redshift
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=-lpj38Cql4c, src:yt-transcripts, https://www.youtube.com/watch?v=TonSU8Ljm5c]
feeds: [redshift]
conflicts: none
---
Roughness polarity: black = perfectly shiny, white = fully rough. White scratches on black therefore need Add or Screen (Screen milder) to roughen without erasing the layers beneath; Multiply removes what you want [24:35-26:38]. Scratch layer strength about 0.5-0.65, not 1.0 [26:38].
For micro scratches he prefers the height output over normal, because normal artifacts [25:05]. Use triplanar rather than UV projection so there are no UV distortions and it works on meshes without UVs [30:21].
Scale: one float drives the tiling of all scratch layers (smaller values read larger scratches) [28:14]. Bump amount for scratches around 0.03 and 0.28 for the micro layer [29:16, 32:25].

**Use it:** recipe for worn-metal looks; gold-coin soft metal takes more scratches, hard metals less.
Transcript support: Bump Blender needs blend weight above 0 and Additive mode. (https://www.youtube.com/watch?v=TonSU8Ljm5c [56:31-57:38])
