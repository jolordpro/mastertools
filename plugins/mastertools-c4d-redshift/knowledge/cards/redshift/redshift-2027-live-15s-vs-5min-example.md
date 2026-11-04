---
id: redshift-2027-live-15s-vs-5min-example
title: Maxon demo: one scene took about 5.5 minutes in Redshift Production and 15 seconds in Redshift Live
domain: redshift
tags: [redshift live, production, render time, preview, iteration, refraction]
applies_to: Redshift 2027.0, Mac demo
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=FmaKhqSITFQ, src:yt-transcripts]
feeds: [estimator, redshift]
conflicts: none
---
Live is near real time with automatic denoise; 2027 adds refraction, area-light spread and ray-traced DOF, and faster interactivity [50:35-51:37].
Same scene: Production about five and a half minutes, Live 15 seconds, with differences because not every feature is in Live [51:37-52:08].
Raise refraction trace steps for clean results in Live [51:06].

**Use it:** use Live only for look-dev and animatics; time estimates must come from Production.
