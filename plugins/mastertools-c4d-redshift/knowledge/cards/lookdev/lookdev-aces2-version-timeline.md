---
id: lookdev-aces2-version-timeline
title: ACES 2.0 arrives by build: Redshift 2026.8 (Jul 22 2026) new config, 2026.9 OCIO 2.5.2, 2027.0 (Oct 14 2026) native ACES 2.0 default
domain: lookdev
tags: [lookdev, aces 2.0, ocio, redshift 2026.8, redshift 2027, version, colour]
applies_to: Redshift 2026.8-2027.0
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.motionmedia.com/mm-blog/whats-new-in-redshift-2026-8, https://digitalproduction.com/2026/09/16/redshift-2026-9-tightens-the-bolts/, https://www.vfxer.com/maxon-fall-2026-release-cinema-4d-2027-breakdown/, src:research-agency-pipelines, src:research-youtube, https://www.youtube.com/watch?v=PCtsdWnYhx8, src:yt-transcripts, https://www.youtube.com/watch?v=7e0SSka8Ar8]
feeds: [CHECKS version match]
conflicts: none
---
2026.8: new OCIO config with ACES v2.0 and OCIO v2.4 compatibility. 2026.9: OpenColorIO 2.5.2 and a display-profile naming fix; test custom configs first.
C4D 2027 / Redshift 2027.0 make ACES 2.0 native with an ACES 2 config by default.
Older ACES setup videos are explicitly out of date (one stops at Redshift 3.0.46): stamp every colour tip with the build it was true for.

**Use it:** version-match check: desk and farm must run the same Redshift build and the same ACES version.
Transcript support: C4D 2027 has ACES fully updated to 2.0 (https://www.youtube.com/watch?v=PCtsdWnYhx8 [01:07:15])
