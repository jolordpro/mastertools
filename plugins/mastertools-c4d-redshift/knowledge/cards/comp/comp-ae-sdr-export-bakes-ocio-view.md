---
id: comp-ae-sdr-export-bakes-ocio-view
title: Render SDR files (JPG, PNG, MP4) from After Effects with the output colour format set to the sRGB display SDR video; EXR needs no change
domain: comp
tags: [after effects, render queue, output module, color, sdr, media encoder, ocio, delivery]
applies_to: After Effects with built-in OCIO (early 2024)
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=IcLiz8e8ffc, src:yt-transcripts]
feeds: [delivery step, CHECKS]
conflicts: none
---
In the Render Queue, Output Module, Color tab, choose the sRGB display SDR video output so the ACES transform is baked into the SDR file. Do this for any SDR format including H.264 and ProRes [45:57-46:31].
Without it the colour is wrong; EXR output needs nothing [44:56-45:27].
Adobe Media Encoder was not ACES-ready at the time; use the Render Queue [44:25] [48:03]. Recheck on current builds.

**Use it:** a delivery step must name the output colour format for each SDR deliverable and warn against Media Encoder for ACES comps until verified.
