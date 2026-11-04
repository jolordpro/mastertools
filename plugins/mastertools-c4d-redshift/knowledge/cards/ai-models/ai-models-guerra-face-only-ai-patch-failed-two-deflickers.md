---
id: ai-models-guerra-face-only-ai-patch-failed-two-deflickers
title: A face-only AI pass comped over the plate failed because two separate deflicker passes drifted differently
domain: ai-models
tags: [beeble, face patch, deflicker, failure story, comp, hugo guerra, deep-read]
applies_to: Beeble, CopyCat
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=NaCJiquNnYY, src:yt-transcripts]
feeds: []
conflicts: none
---
Since the face was too low-res, he ran Beeble on only the face and tried compositing it back on the full-body pass [27:14]. It failed because deflickering the plate and deflickering the face separately flickered in different places [27:39]. He suggests hand-animating exposure changes as the possible fix but did not try it [28:09].

**Use it:** When two ML-processed layers must match, process them together or plan a manual exposure match; do not stack two independent deflicker passes.
