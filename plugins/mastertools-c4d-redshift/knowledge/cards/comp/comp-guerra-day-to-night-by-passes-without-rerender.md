---
id: comp-guerra-day-to-night-by-passes-without-rerender
title: Hugo Guerra turned a daytime Redshift shot to night in comp by pulling sun from the diffuse, GI, reflection passes and the shadow pass
domain: comp
tags: [hugo guerra, day to night, aov, redshift, shadow pass, comp relight, nuke, deep-read]
applies_to: Redshift AOVs, Nuke
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=NaCJiquNnYY, src:yt-transcripts]
feeds: []
conflicts: none
---
With the split Redshift AOVs (GI, diffuse, reflection, refraction, raw passes) he graded each, subtracted the sun, and used the shadow pass to negate sun shadows rather than re-render [03:45-05:51]. The sun/dome contribution was removed from diffuse and from reflections and speculars [05:51]; the daytime lake was graded via refraction passes [06:21]. A new cloudy HDR sky was brought in, the same grading copied to the foreground element so depth of field and motion blur stay controllable, and a ramp faked distant city light [07:25-08:57]. He says none of it is physically accurate; it is a comp hack that works in parts [07:25].

**Use it:** For a lighting-change request late in a job, check whether the AOV set allows a pass-level grade before agreeing to re-render. Needs raw and filter passes plus shadow.
