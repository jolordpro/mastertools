---
id: redshift-coating-layer-second-spec-lobe-for-smudged-metal-and-material-presets
title: Redshift material coat: a second specular layer (coat weight up, high coat IOR walked down) adds a faint smudge to metal; use the presets as starting points
domain: redshift
tags: [chad-ashley, maxon, uber shader, coat, clearcoat, specular, material presets, metal, deep-read]
applies_to: Redshift 2.x Uber shader (2017); default Redshift Material in R26/RS 3.5 (2022)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=LcxjkHFS-2k, https://www.youtube.com/watch?v=RpiCCLHjlWQ, src:yt-transcripts]
feeds: [lookdev, elevate]
conflicts: none
---
Chad: coating gives a second specular lobe on top of the base reflection. For a chrome-like metal he loaded the Iron preset, roughness about 0.35, coat weight to full, coat IOR to about 10, then walked the IOR down; the effect is very subtle, like dust or smudges that keep highlights from being perfect [39:26-41:28]. On plastic it reads like a clear coat over a rough first lobe [39:56-40:26].
Both talks like the built-in presets as a place to start: Chad on the Uber shader (Iron, Glass) [36:50-37:51]; the 2022 Maxon trainers say the default Redshift Material still has useful presets and is as capable as the newer Standard Material [1:55:27-1:57:02, V1].
Transfer: reflective sports trophy, helmet or logo materials; keep coat roughness low so it reads as polish not dirt.

**Use it:** The coach can name coat as the fix for 'metal looks too perfect' before adding roughness maps.
