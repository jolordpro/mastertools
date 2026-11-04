---
id: comp-colour-handoff-names-app-view-domain
title: A colour hand-off note must say which app, view and processing domain judged the picture, not just the colour space
domain: comp
tags: [hand-off, color space, view, domain, nuke, after effects, ocio, sdr view, documentation]
applies_to: After Effects, Nuke
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=-g6JTD8cge4, src:yt-transcripts]
feeds: [CHECKS, comp planner]
conflicts: none
---
Imagica [06:18]: Nuke artists mostly judged shots through an SDR view, not high scene-linear values on an HDR display, so the hand-off had to carry app, view and processing domain.
The VFX team kept an ACES linear flow in Nuke; AE had a custom OCIO environment with SDR and HDR monitored together [05:47].

**Use it:** include app, view and domain in the colour line on every hand-off card.
