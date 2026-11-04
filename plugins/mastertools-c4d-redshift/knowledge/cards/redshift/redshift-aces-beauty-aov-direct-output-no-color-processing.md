---
id: redshift-aces-beauty-aov-direct-output-no-color-processing
title: For ACES comp, output the beauty AOV with Direct Output on and Apply Color Processing off
domain: redshift
tags: [redshift, aces, beauty aov, direct output, color processing, bloom, photographic exposure]
applies_to: Redshift 3.0.46 / C4D (2020 video)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=vEoIXTbyz6o, src:yt-transcripts]
feeds: [coach, comp-fix planner]
conflicts: none
---
[10:59] Add a Beauty AOV, enable Direct Output (skips the Picture Viewer colour processing) and untick Apply Color Processing. That also switches off Redshift's post effects (bloom, streaks, flares, colour control, LUTs), so rebuild bloom and vignette in comp. Keep Photographic Exposure off.
[11:30] Alternative if bloom must be baked: set the display mode to Linear instead of OCIO ACES, but it has to be switched back each time, which the speaker found error-prone.
Old build (2020); check against current Redshift before quoting.

**Use it:** the advisor can warn when a beauty is going to comp with the view transform or post effects baked in.
