---
id: ai-models-generative-relight-needs-190gb-vram-so-cloud-only
title: Beeble says SwitchX and SwitchHDR need about 190 GB VRAM (600 GB for 4K), so only SwitchLight runs locally
domain: ai-models
tags: [beeble, hoon kim, conrad curtis, siggraph 2026, vram, local inference, 4k, cloud only, privacy, dgx spark, deep-read]
applies_to: SwitchX, SwitchHDR (2026)
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=weXc-JGwewo, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Kim [41:24-41:55]: the generative models need at least about 190 GB of VRAM; 4K support would take four GPUs in parallel, around 600 GB. Beeble Studio, the local desktop app, runs only SwitchLight. Local versions come later, perhaps on DGX Spark.
Asked about plates that cannot leave the building [40:53-42:26]; also clients wary of proprietary products or of a model's origin [32:44-33:16, 55:51-56:21]. The reply: an enterprise tier exists and SwitchX has an API [33:16].

**Use it:** if a job has confidentiality limits, check the cloud and model-origin question before choosing a generative relight.
