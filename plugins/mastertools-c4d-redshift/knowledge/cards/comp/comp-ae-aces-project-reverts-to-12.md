---
id: comp-ae-aces-project-reverts-to-12
title: After Effects: new projects default back to ACES 1.2, and an sRGB JPEG needs a media colour space override
domain: comp
tags: [after effects, aces 1.3, aces 1.2, 32 bit, interpret footage, jpeg, color management]
applies_to: After Effects 2024, ACES 1.3
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=CXx75LxGxOw, src:yt-transcripts]
feeds: [CHECKS 5, comp readiness]
conflicts: none
---
Set the project to 32 bits per channel and ACES 1.3 CG; a fresh project reverts to 1.2 [26:04-27:26]. A baked sRGB JPEG looks wrong until Interpret Footage > Color overrides its media colour space to sRGB display [28:27]. Switch the display to raw to read data passes [1:07:21].

**Use it:** Put the working-space check at the top of the comp readiness list, and stamp the AE build.
