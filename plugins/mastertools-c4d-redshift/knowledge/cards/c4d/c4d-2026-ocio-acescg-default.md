---
id: c4d-2026-ocio-acescg-default
title: From C4D 2026, new projects default to OCIO with an ACEScg working space and need a tagged input space for every texture and colour
domain: c4d
tags: [ocio, acescg, colour management, c4d 2026, defaults, tone mapper, aces, lookdev, input space]
applies_to: C4D 2026 (Sep 2025)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://digitalproduction.com/2025/09/12/maxon-2026-release-new-colour-science-liquids-clouds-and-a-new-logo/, src:research-agency-pipelines, https://www.youtube.com/watch?v=PCtsdWnYhx8, src:yt-transcripts, https://www.youtube.com/watch?v=IcLiz8e8ffc]
feeds: [CHECKS 5, CHECKS 5 colour space]
conflicts: none
---
The ACES tone mapper is the default view. Colour inputs need a tagged space, so untagged maps are a mismatch source.
Legacy projects do not auto-match the new defaults.
Merged from `lookdev-c4d2026-ocio-acescg-default`: Since C4D 2026 (Sep 2025) a new project is OCIO + ACEScg working space, with the ACES tone mapper as default view. Legacy projects do not auto-match the new defaults. Untagged textures and colours are the usual source of wrong looks.

**Use it:** flag legacy scenes opened in 2026+ whose colour settings differ from the new defaults.
Transcript support: colour-space handling in 2026 used a hidden auto mode that 2027 now displays (https://www.youtube.com/watch?v=PCtsdWnYhx8 [01:07:42])
Transcript support: scenes created without OCIO need Convert to OCIO once; new OCIO scenes need nothing (https://www.youtube.com/watch?v=IcLiz8e8ffc [09:18])
