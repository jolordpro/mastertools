---
id: lookdev-fmx-iridescence-from-view-angle-driving-a-ramp
title: "FMX 2014 TD student: fake iridescence by taking the angle between camera ray and surface normal and driving a colour ramp"
domain: lookdev
tags: [fmx, lookdev, iridescence, fresnel, student, manuel, deep-read]
applies_to: any
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=8tW77BsgtPY, src:yt-transcripts]
feeds: [redshift]
conflicts: none
---
Manuel's bug shell: iridescence means colour shifts with viewing angle; he computed that angle (camera ray against surface normal) and fed it into a ramp so the colours can be art-directed [18:07-18:38]. The coloured regions creep across the shell as it turns, with the yellow part facing the camera [19:10]. He also made the reference bug rougher because the real one looked too cute [18:38].
In Redshift terms this is a facing-ratio or Fresnel-style driver; ledger not checked, neutral.

**Use it:** Fake thin-film colour by a facing-ratio ramp when no true iridescence shader is available; the ramp gives art-directable colours.
