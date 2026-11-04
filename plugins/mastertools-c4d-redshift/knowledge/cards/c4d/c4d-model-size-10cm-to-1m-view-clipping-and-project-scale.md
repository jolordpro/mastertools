---
id: c4d-model-size-10cm-to-1m-view-clipping-and-project-scale
title: Cinema 4D likes objects between roughly 10 cm and 1 m: a 2 cm model clipped, fixed by view clipping or by scaling the project
domain: c4d
tags: [scale, clipping, project scale, units, working size, lionel, maxon, low-confidence, deep-read]
applies_to: C4D R26 (2022)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=TonSU8Ljm5c, src:yt-transcripts]
feeds: [shakedown, coach]
conflicts: none
---
The imported part was about 2 cm, so the editor clipped it. Quick fix: Project Settings view clipping to small or tiny [07:15-08:01]. His preference: keep the scene near the size C4D is comfortable with (about 10 cm to 1 m, he also said up to 10 m; a default cube is 200 cm) and scale the project up by 10 instead [08:01-08:35]. Captions garble the exact scale value.
Later benefit: shader values such as a round-corner radius stay readable without typing strings of zeros [58:41].

**Use it:** scene check: flag tiny scene scale; suggest rescaling rather than living with tiny numbers.
