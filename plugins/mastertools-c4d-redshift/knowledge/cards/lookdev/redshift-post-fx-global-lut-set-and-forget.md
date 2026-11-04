---
id: redshift-post-fx-global-lut-set-and-forget
title: Set Redshift post effects in the render settings, not per camera; Greyscalegorilla starts with the Advantix 200 LUT after colour management
domain: lookdev
tags: [post effects, lut, advantix 200, bloom, cameras, colour management order]
applies_to: Redshift in C4D (2023)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=le17-h6tUD0, src:yt-transcripts]
feeds: [lookdev, coach]
conflicts: none
---
Post effects set on a camera can be forgotten when you switch cameras; the settings in the render view gear apply globally [35:54-36:57].
Starting point: LUT Advantix 200 (ships with Redshift), applied after the colour management so the ACES transform comes first; it adds a mild S-curve and warms slightly [36:57-37:27].
Bloom hack for atmosphere: threshold very low, softness up, intensity far down; compare using snapshots [37:59-38:59].

**Use it:** a scene check can warn when post effects are set on one camera only.
