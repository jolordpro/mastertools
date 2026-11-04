---
id: redshift-aov-caustics-motionblur-cost
title: AOVs cost a little speed, caustics and motion blur cost a lot; export only the passes needed
domain: redshift
tags: [aov, caustics, motion blur, speed, post blur]
applies_to: Redshift in C4D
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=uKRqHwVr0F4, src:yt-transcripts, https://www.youtube.com/watch?v=FYq8sdCtsoY]
feeds: [coach, redshift]
conflicts: none
---
Motion blur slows renders, do it in post (ReelSmart) if possible [08:51]. Caustics are heavy: off unless wanted [10:00]. AOVs slow slightly: export only what the comp needs, or turn off to test speed [10:26].

**Use it:** scene check: list enabled AOVs vs what the comp template uses.
Transcript support: caustics barely changed frame time in one scene (2:20 to 2:44 across light combinations) (https://www.youtube.com/watch?v=FYq8sdCtsoY [13:03-16:12])
