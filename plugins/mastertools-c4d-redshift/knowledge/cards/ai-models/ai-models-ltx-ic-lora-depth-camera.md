---
id: ai-models-ltx-ic-lora-depth-camera
title: LTX IC-LoRA adapters turn depth renders into photoreal video and copy camera moves from a reference; verified for LTX-2 only
domain: ai-models
tags: [ltx, ic-lora, depth, cameraman, lightricks, video model, 3d conditioned, trainer]
applies_to: LTX-2 / 2.3 / 2.5
status: V2
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://docs.ltx.video/open-source-model/usage-guides/ic-lo-ra, src:research-frontier-ai, https://www.youtube.com/watch?v=LcrSp_hzYvA, src:yt-transcripts]
feeds: [video preview]
conflicts: none
---
Pose and canny adapters also exist; Cameraman (pan, tilt, zoom, orbit) is Apache and for LTX-2.3. LTX provides a trainer for custom control adapters. LTX-2.5 (open, $0.09/s hosted, up to 20 s, 4K) adapters are unconfirmed.

**Use it:** the best open route to turn draft depth and camera into a motion preview.
Transcript support: Same idea (3D render as the structure source) with a hosted model rather than open weights. (https://www.youtube.com/watch?v=LcrSp_hzYvA [00:31])
