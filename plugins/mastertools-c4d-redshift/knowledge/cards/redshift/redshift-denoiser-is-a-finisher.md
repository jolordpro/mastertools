---
id: redshift-denoiser-is-a-finisher
title: Use denoising to remove the last few percent of noise; it can oversmooth and fails on very noisy input
domain: redshift
tags: [denoise, denoiser, noise, oversmooth, brush stroke, samples]
applies_to: Redshift 2026-2027
status: V
confidence: high
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/c4d/2027/en-us/Content/_REDSHIFT_/html/Denoising.html.md, src:research-agency-pipelines, https://www.youtube.com/watch?v=L4riSkE7FwA, src:yt-transcripts, https://www.youtube.com/watch?v=uKRqHwVr0F4, https://www.youtube.com/watch?v=0amlKMClE4s, https://www.youtube.com/watch?v=yAbuPpbbATA, https://www.youtube.com/watch?v=X5zVhc5ahl0, https://www.youtube.com/watch?v=eGAjsSNtX6E]
feeds: [advisor]
conflicts: none
---
Maxon's denoising page frames the denoiser as a finisher. Too aggressive use smooths detail, leaves brush-stroke artifacts and breaks down when the input is very noisy.
Do not cut samples and lean on the denoiser blindly.

**Use it:** the advisor never trades a big sample cut for denoiser strength without showing a before/after.
Transcript support: Trainer avoids denoising animation, prefers fixing sampling, denoise only at about 95 percent clean. (https://www.youtube.com/watch?v=L4riSkE7FwA [56:52])
Transcript support: Presenter rarely denoises finals because detail is lost; uses it for previews. (https://www.youtube.com/watch?v=uKRqHwVr0F4 [07:50])
