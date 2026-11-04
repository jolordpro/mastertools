---
id: lookdev-glass-needs-contrast-environment-and-gi
title: Glass only reads as glass in a contrasty environment with global illumination on; a flat environment makes it look artificial
domain: lookdev
tags: [glass, hdri, contrast, global illumination, lighting environment, keyshot, deep-read]
applies_to: KeyShot product mode (principle general)
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=Bbj18-933Vg, src:yt-transcripts]
feeds: [coach, lookdev]
conflicts: none
---
Even a correct glass material looked wrong in a flat HDRI [01:04]. He switched to a higher-contrast three-panel studio HDRI with highlights and dark areas, and from basic to product mode, which enables more ray bounces and global illumination, and the glass looked far more real [01:34]. Environment also changes how both glasses compare at the end [13:31]. Reflection on the front face, edge reflections and the offset stripe pattern together sell it [02:05].

**Use it:** before tuning glass material numbers, fix the environment contrast and bounce depth.
