---
id: redshift-aov-output-transform-default
title: Redshift renders AOVs through the output transform to sRGB by default unless told otherwise
domain: redshift
tags: [aov, output transform, srgb, aces, after effects, colour, comp, linear, redshift, display transform]
applies_to: Redshift with OCIO/ACES
status: U
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://community.acescentral.com/t/valid-c4d-redshift-after-effects-aces-workflow/3451, https://3dart.it/en/redshift-using-aces-with-after-effects, src:research-agency-pipelines, https://www.youtube.com/watch?v=vEoIXTbyz6o, src:yt-transcripts, https://help.maxon.net/r3d/cinema/en-us/Content/html/Intro+to+AOVs.html]
feeds: [CHECKS 5]
conflicts: none
---
A forum thread and a tutorial say AOVs go through the output transform by default, so EXR passes can arrive display-transformed rather than scene-linear. The research marks it unverified.
It affects whether passes add back to the beauty in comp.
Merged from `comp-aov-output-transform-default`: Forum-level claim: AOVs go through the output transform by default. Matches the farm warning that Bake display transform can apply a curve twice.

**Use it:** verify on a draft: read a pass pixel value before and after changing the transform setting, then treat the result as a rule.
Transcript support: Beauty AOV with Direct Output on and Apply Color Processing off gives an unprocessed image (2020 build). (https://www.youtube.com/watch?v=vEoIXTbyz6o [10:59])
Maxon check (2026-10-31): Maxon docs settle the default. Each AOV has an Apply Color Processing switch (view transform, tone mapping, gamma). It is on by default only for the lighting AOVs (diffuse, specular, SSS, reflection, refraction, emission, GI, caustics, volume, translucency), not for every AOV. (https://help.maxon.net/r3d/cinema/en-us/Content/html/Intro+to+AOVs.html)
