---
id: redshift-aov-judge-in-bucket-mode
title: Judge AOVs in bucket mode, because progressive Render View shows some passes wrong
domain: redshift
tags: [render view, progressive, bucket, aov preview, redshift]
applies_to: Redshift 2024
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=CXx75LxGxOw, src:yt-transcripts, https://www.youtube.com/watch?v=ARykOD6lG3c, https://www.youtube.com/watch?v=5hQKHD8fSs8, https://www.youtube.com/watch?v=iqrISqFY3bQ, https://www.youtube.com/watch?v=OMTPokoFp5E]
feeds: [CHECKS render view]
conflicts: none
---
In progressive mode some passes look weird or broken; switch to bucket rendering to see the correct output [20:13-20:43]. He says to check the documentation for which passes work.

**Use it:** Warn when someone is judging an AOV in progressive mode.
Transcript support: custom AOVs do not show in progressive mode; switch to bucket in the render view (https://www.youtube.com/watch?v=ARykOD6lG3c [10:40-11:00])
Transcript support: Object ID pass and Puzzle Matte render black in the progressive Render View until bucket rendering is on (https://www.youtube.com/watch?v=5hQKHD8fSs8 [08:49-10:23])
Transcript support: Puzzle Matte shows nothing without bucket rendering (https://www.youtube.com/watch?v=iqrISqFY3bQ [02:36])
Transcript support: Final-quality noise only judged with bucket rendering on (https://www.youtube.com/watch?v=OMTPokoFp5E [02:37])
