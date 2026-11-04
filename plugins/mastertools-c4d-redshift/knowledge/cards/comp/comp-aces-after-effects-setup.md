---
id: comp-aces-after-effects-setup
title: After Effects with ACEScg EXRs: working space ACEScg, display colour management off, Preserve RGB on, converter set to ACEScg input
domain: comp
tags: [comp, after effects, aces, acescg, exr, colour profile converter, multipass]
applies_to: After Effects, Redshift ACES
status: U
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://community.acescentral.com/t/valid-c4d-redshift-after-effects-aces-workflow/3451, https://3dart.it/en/redshift-using-aces-with-after-effects, src:research-agency-pipelines, https://www.youtube.com/watch?v=7uY4-bPvRKs, src:yt-transcripts, https://www.youtube.com/watch?v=CXx75LxGxOw]
feeds: [CHECKS 5]
conflicts: none
---
Community advice: without a Colour Profile Converter at ACEScg input, EXRs look washed out.
Old guides date from before ACES 2.0; re-test on current builds.

**Use it:** give the setup as a checklist stamped with the Redshift build it was tested on.
Transcript support: Preserve RGB export and the OCIO-plugin-plus-gamma-fix method null out in Difference; zak also gives the old Preserve RGB steps [20:30] (https://www.youtube.com/watch?v=7uY4-bPvRKs [42:08])
Transcript support: AE project must be 32 bit and ACES 1.3 CG; new projects revert to 1.2; sRGB JPEG needs a media colour space override [28:27]. (https://www.youtube.com/watch?v=CXx75LxGxOw [26:23])
