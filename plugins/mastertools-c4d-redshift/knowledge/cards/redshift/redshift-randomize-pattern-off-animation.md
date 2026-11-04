---
id: redshift-randomize-pattern-off-animation
title: Turn Randomize Pattern on Each Frame off for denoised animation to reduce flicker
domain: redshift
tags: [randomize pattern, flicker, animation, denoise, noise pattern, sampling]
applies_to: Redshift 2026-2027
status: V
confidence: high
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/c4d/2027/en-us/Content/_REDSHIFT_/html/Denoising.html.md, https://help.maxon.net/c4d/2027/en-us/Content/_REDSHIFT_/html/Sampling+-+Advanced.html.md, src:research-agency-pipelines, src:research-gaps-deep, https://www.youtube.com/watch?v=L4riSkE7FwA, src:yt-transcripts, https://www.youtube.com/watch?v=G43QVR1TqXg]
feeds: [CHECKS flicker]
conflicts: none
---
With a different noise pattern per frame, denoised output changes frame to frame and shows as flicker. Keeping the pattern fixed makes noise static.
The other documented flicker cause is the irradiance cache (ledger section 6).

**Use it:** flag the setting as on in any animation that uses a denoiser.
Transcript support: Trainer keeps random pattern on for undenoised animation (stops stuck noise); a viewer says off for denoising in post [1:00:31]. (https://www.youtube.com/watch?v=L4riSkE7FwA [57:55])
Transcript support: Uncheck random noise pattern to stop denoised flicker, also lower threshold. (https://www.youtube.com/watch?v=G43QVR1TqXg [07:18])
