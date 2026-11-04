---
id: redshift-denoise-engine-limits
title: Altus runs only in bucket mode and OptiX needs NVIDIA hardware
domain: redshift
tags: [altus, optix, denoise, bucket, nvidia, oidn, mac]
applies_to: Redshift 2026-2027
status: V
confidence: high
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/c4d/2027/en-us/Content/_REDSHIFT_/html/Denoising.html.md, src:research-agency-pipelines, https://www.youtube.com/watch?v=uKRqHwVr0F4, src:yt-transcripts]
feeds: [advisor, mac preset design]
conflicts: none
---
Altus single and dual pass work in bucket mode only. OptiX needs an NVIDIA GPU. OIDN is the vendor-neutral option (ledger section 3 covers it for Live).
A Mac therefore cannot use OptiX for a final.

**Use it:** when building a Mac preset, offer OIDN and skip OptiX; use bucket mode if Altus is wanted.
Transcript support: OptiX and OIDN in progressive; all four methods in bucket mode. GSG [59:27] hears NVIDIA-only denoisers are slightly better (hearsay). (https://www.youtube.com/watch?v=uKRqHwVr0F4 [05:46])
