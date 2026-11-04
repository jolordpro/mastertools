---
id: c4d-standard-renderer-speed-area-shadows-accuracy-and-max-samples-visible-light-modes
title: Standard renderer lights: area shadows are the slowest (7 s default in his test); cut accuracy to 25% and lower max samples until fireflies appear
domain: c4d
tags: [teamwnj, standard renderer, area shadows, soft shadows, hard shadows, max samples, fireflies, visible light, physical sky, polygon count, deep-read]
applies_to: Cinema 4D Standard renderer, version not stated (uploaded 2019-02); not Redshift
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=XuoDTdHngaA, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
From the TeamWnJ tutorial. Polygons: render cost rises with count; a subdivided cube of 64 polygons took 0 s, a very large count about 2 s (the huge number is garbled in the captions: he says 125 thousand, then million) [03:39-04:24].
Shadow types: soft is natural and tunable (resolution setting); hard is fastest and unrealistic; area is slowest and most realistic, hardness varying with distance [04:24-05:10]. Default area shadows looked identical to hard shadows in the test but took 7 s [05:10].
Tune area shadows: drop accuracy to 25%, then lower max samples until fireflies show [05:10-05:41]. Final time quoted as 16 s with max samples 16; likely a mishearing, uncertain [05:10-05:41].
Visible light: invisible is fastest; use visible if nothing blocks it, volumetric only if objects intercept it [05:41]. Area lights: lower the samples in the Details tab until fireflies show, or swap the area light for something else [06:11].
Sky: if a physical sky is slow, use a plain sky or an HDRI on the background [06:11].

**Use it:** when tuning Standard-renderer shadows, step down area-shadow accuracy and max samples until fireflies appear, then step back one notch.
