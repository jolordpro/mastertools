---
id: redshift-targeted-sample-overrides-vs-global
title: Raising samples only where the noise is (for example reflection) beat raising them everywhere
domain: redshift
tags: [sample overrides, reflection, unified sampling, noise, glass, metal]
applies_to: Redshift in C4D (2025 video)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=Uk1_Cwi8BUQ, src:yt-transcripts, https://www.youtube.com/watch?v=kwFwyzjXsdM]
feeds: [coach, redshift]
conflicts: none
---
Method: GI to brute force, automatic sampling off, unified min about 4 and max about 256 [07:24]. Use Show Samples; white = max reached, aim for grey [01:04]. Find the noisy part (glass, metal, shadows), then override only that ray: reflection max x4 [02:39].
Full-res result as heard: about 24 s with the targeted override against about 37 s when the uniform samples were raised, and the uniform one was still noisier [06:19-06:52]. Garbled captions; treat numbers as approximate.
If max samples above 4000 seems needed, check the adaptive threshold first [03:40].

**Use it:** coach: when noise sits in one effect, suggest a per-ray override over a global samples increase.
Transcript support: Overwrite samples in Sampling Overrides sets one count for all lights; raising min/max also raises secondary rays but wastes time (https://www.youtube.com/watch?v=kwFwyzjXsdM [12:12-13:14])
