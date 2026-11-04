---
id: lighting-false-color-exposure-check-aim-for-grey-middle
title: Use a false color view to set key light exposure: aim at the grey middle band; red then white means highlights are lost
domain: lighting
tags: [false color, exposure, filmic, key light, calibration, troy sobotka, blender guru, deep-read]
applies_to: Blender 2.8 Filmic (2019)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=UQz6AI88jAI, src:yt-transcripts]
feeds: []
conflicts: none
---
Blender Guru (2019) [07:19-10:30]. Monitor brightness differs, so a render that looks right can look wrong on a phone; a hardware calibrator helps, and false color removes guesswork. Ramp from black (no data), blue, aqua, green, grey (middle exposure), green, then red and white (clipped). Aim the key around grey, slightly above at most. In the 2019 version both under and over exposure showed green, which is confusing; the author asked the Filmic creator for a change and the upcoming build would use a slightly bluer green and a yellower green and a tighter grey. If it looks flat, do not raise the lamp (that desaturates): use the High Contrast look instead of Base Contrast.

**Use it:** Our exposure check can use the same logic: report the portion of the subject in grey/green and flag red/white. Rendering in a scene-referred view transform is assumed.
