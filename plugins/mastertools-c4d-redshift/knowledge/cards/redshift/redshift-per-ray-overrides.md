---
id: redshift-per-ray-overrides
title: Per-ray sample overrides (reflection, refraction, AO, light, volume, SSS) replace or scale counts, and only work with Automatic Sampling off
domain: redshift
tags: [sampling overrides, per ray, reflection, refraction, ao, light samples, automatic sampling]
applies_to: Redshift 2026-2027
status: V
confidence: high
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/c4d/2027/en-us/Content/_REDSHIFT_/html/Sampling+-+Advanced.html.md, src:research-agency-pipelines, https://www.youtube.com/watch?v=L4riSkE7FwA, src:yt-transcripts, https://www.youtube.com/watch?v=Uk1_Cwi8BUQ, https://www.youtube.com/watch?v=Q5AZ7Xlh2I4, https://www.youtube.com/watch?v=s5ElfI1q8uU]
feeds: [advisor]
conflicts: none
---
Each effect can Replace its sample count or Scale the global one. Target the effect that is noisy instead of raising global samples.
The controls are available only when Automatic Sampling is off (the ledger notes it hides Min and Max).

**Use it:** when one effect is noisy, advise its override and give the time cost before touching global samples.
Transcript support: Replace or scale local samples; enable only for ray types in the scene; 512 starting value. (https://www.youtube.com/watch?v=L4riSkE7FwA [23:16])
Transcript support: Reflection override raised and tested; works with automatic sampling off. (https://www.youtube.com/watch?v=Uk1_Cwi8BUQ [02:39])
Transcript support: Sampling Overrides Scale mode multiplies the base (base 16, scale 2 gives 32) per effect; speaker's counts are scene-specific (https://www.youtube.com/watch?v=Q5AZ7Xlh2I4 [08:18-09:03])
Transcript support: overrides need automatic sampling off; doubling an override alone does not clean it, raise Max Samples too (https://www.youtube.com/watch?v=s5ElfI1q8uU [01:04-02:07])
