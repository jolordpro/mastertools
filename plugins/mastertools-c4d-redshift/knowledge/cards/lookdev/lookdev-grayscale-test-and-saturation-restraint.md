---
id: lookdev-grayscale-test-and-saturation-restraint
title: Convert a render to grayscale to test realism; over-saturated colour is the most common CG giveaway, and a scene needs places for the eye to rest
domain: lookdev
tags: [colour, saturation, value, grayscale test, photorealism, blender guru, deep-read]
applies_to: any
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=Qj1FK8n7WgY, src:yt-transcripts]
feeds: []
conflicts: none
---
Blender Guru (2014) [00:32-04:13]. Colour is a top giveaway of a fake image: take a current render to grayscale and it often looks more photoreal at once. Saturation (purity) and value (brightness) are the two usual culprits; the demo shows a red at 100% saturation hard to look at, 20% saturation becoming a flesh pink, and 20% value turning it a muddy brown. One red mixed with white and black can build a whole painting. CG artists over-saturate, and saturation everywhere leaves the eye no resting place, which becomes irritating to look at.

**Use it:** Add a grayscale/desaturate view to the look check and flag scenes where most pixels are highly saturated.
