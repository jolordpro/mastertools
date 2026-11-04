---
id: comp-ae-ocio-managed-project-setup
title: After Effects OCIO project setup the Maxon trainer uses: OCIO colour management, ACEScg preset, 32 bpc, JPG interpreted as sRGB display
domain: comp
tags: [after effects, ocio, acescg, 32 bpc, project settings, interpret footage, sdr]
applies_to: After Effects with built-in OCIO (early 2024), Redshift 2024
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=IcLiz8e8ffc, src:yt-transcripts]
feeds: [comp-fix planner, coach]
conflicts: none
---
Project Settings, Color: switch from Adobe colour management to OCIO, choose the ACEScg (ACES 1.3) preset, 32 bits per channel; display is SDR video [22:58-24:00].
Import the EXR as a composition. A JPEG cannot hold ACEScg, so interpret it as the sRGB display SDR video space for it to match [25:02-26:04].
A new project once reverted to ACES 1.2 and looked clipped; check the preset every time [1:10:14].
Data images (UV, normal, bump) should keep raw pixel values; a screen grab of a web image is not HDR or raw [1:09:12-1:09:43].

**Use it:** the AE setup checklist should include the preset version and a visual match between EXR and JPG as the pass test.
