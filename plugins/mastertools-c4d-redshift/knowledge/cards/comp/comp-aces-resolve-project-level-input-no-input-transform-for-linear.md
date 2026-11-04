---
id: comp-aces-resolve-project-level-input-no-input-transform-for-linear
title: In Resolve ACES 1.3 project settings, set the camera input in the project; raw files choose themselves and ACES linear EXR is set as No Input Transform
domain: comp
tags: [aces, resolve, input transform, exr, aces linear, raw, r3d, arri logc3, rec709 output, vfx handoff, deep-read]
applies_to: DaVinci Resolve ACES 1.3
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=drEi66Xj5Hg, src:yt-transcripts, https://www.youtube.com/watch?v=atdGKZnUQ5U, https://www.youtube.com/watch?v=AAeZKZ5feGA, https://www.youtube.com/watch?v=2Q3CybANHKE]
feeds: [CHECKS, delivery]
conflicts: none
---
Project-level management: Colour science ACEScct, version 1.3, input transform (example ARRI LogC3), output Rec.709 for the mastering monitor [01:01][02:02]. Raw formats such as R3D are unpacked into the working space automatically and their input cannot be changed [05:09][05:40]. Linear EXRs from VFX vendors: there is no "ACES" input item any more; choose No Input Transform [06:11][06:42][07:16]. Wrong input mapping shows as an obviously wrong image (shot 3) [05:09]. Normalised image looks correct for display but not necessarily the creative intent [02:32].

**Use it:** delivery check: tell VFX vendors to return ACES linear EXR and tag it No Input Transform on the grading side.
