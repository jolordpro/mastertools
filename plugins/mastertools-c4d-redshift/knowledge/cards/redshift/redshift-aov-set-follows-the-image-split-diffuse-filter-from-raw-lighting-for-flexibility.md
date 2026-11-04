---
id: redshift-aov-set-follows-the-image-split-diffuse-filter-from-raw-lighting-for-flexibility
title: Choose AOVs by what the image needs; splitting Diffuse into filter plus raw lighting gives more post control than a combined Diffuse Lighting pass
domain: redshift
tags: [aov, diffuse lighting, raw, multiply, shadow, photoshop, psd, deep-read]
applies_to: Redshift in C4D
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=5hQKHD8fSs8, src:yt-transcripts]
feeds: [redshift, comp]
conflicts: none
---
No fixed AOV list: a reflective or refractive object needs reflection and refraction passes, a matte object does not [01:05-02:07].
The speaker keeps the Beauty pass only as a reference to prove the stack sums to the render, never in the final comp [02:39, 05:13]. Preview each pass in the render view first [02:07].
Starter set: Diffuse Lighting, Reflection, Specular, Refraction, GI, then Shadows [03:10-06:16]. Raw channels go on Multiply, not Add [07:48].
Shadows pass is used as a mask on a Levels adjustment layer [06:16-06:46].
If a lot of grading is expected, separate Diffuse Filter and Diffuse Lighting Raw; if little, a single combined pass is fine [07:17-08:18].
He saves PSD at 16 bits because Photoshop handles EXR poorly [02:07].

**Use it:** Choose the pass list from the grade plan: heavy grade, split passes; quick turn, fewer.
