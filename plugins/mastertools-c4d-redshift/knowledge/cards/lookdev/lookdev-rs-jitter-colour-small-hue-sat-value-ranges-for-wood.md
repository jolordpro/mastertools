---
id: lookdev-rs-jitter-colour-small-hue-sat-value-ranges-for-wood
title: For wood, use colour Jitter with zero hue variation and only small saturation and value ranges so planks look cut from different boards
domain: lookdev
tags: [redshift, jitter, colour variation, saturation, value, wood, material variation, deep-read]
applies_to: Redshift Jitter colour
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=UjThhVMuV18, src:yt-transcripts]
feeds: [redshift, coach]
conflicts: none
---
Put a colour Jitter between the base colour output and the material input; defaults vary everything and look crazy [05:12][05:43]. For wood he sets hue min and max to 0 and 0, keeps saturation variation tiny (spoken values about 0.05 to 0.1, partly unclear) and value variation small, not much lighter than the base, down toward about 0.1 to 0.15 (numbers heard imperfectly) [06:14][06:46]. He exaggerates while setting up to make the change obvious, and sometimes also jitters roughness [07:18][07:48]. Seeds for each channel are changed separately.

**Use it:** rule of thumb: for natural materials keep hue fixed and tune value and saturation in small ranges.
