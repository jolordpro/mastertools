---
id: comp-looks-plugin-aces-aware
title: Magic Bullet Looks (Jan 2024 update) reads After Effects' colour management, so its tools preview correctly on ACEScg
domain: comp
tags: [magic bullet looks, aces, halation, optical diffusion, spot exposure, film emulation]
applies_to: Magic Bullet Looks, After Effects Jan 2024
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=IcLiz8e8ffc, src:yt-transcripts]
feeds: [elevate]
conflicts: none
---
The plugin picks the project's colour profile and shows the right preview, so exposure and film tools work on scene-linear data [37:43-38:44].
Tools shown: Optical Diffusion for glow and haze, Halation for red edges on hot highlights, Film Negative and Film Print, Spot Exposure, Color Remap [39:15-43:25]. Exposure first in the chain works on everything after it [41:20].
Host rates Colorista inside Looks as quick to use; Lumetri under ACEScg is untested [1:07:06] [1:34:09].

**Use it:** use as the finishing recipe in elevate for a comp stage once the AOV stack matches.
