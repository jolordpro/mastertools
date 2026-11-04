---
id: ai-models-ic-light-detail-mask-rerun-without-resampling
title: IC-Light detail restore: changing the transfer mask re-runs in seconds without resampling, and the mask needs three modes to avoid a first-run error
domain: ai-models
tags: [[ic light, detail transfer, mask, preview bridge, comfyui, text restore, no resample, auto adjust, levels], deep-read]
applies_to: ComfyUI IC-Light workflow
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=sMMYSmDHAY8, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
Detail restore uses a three-way mask switch [34:27-35:28]: (1) a hand-drawn mask over only the damaged text or logo, the recommended default; (2) a pass-through of the subject mask, only so the first run does not error because the manual mask is empty; (3) a saved mask loaded from file. Changing the mask re-runs very quickly because the sampler is not run again [39:30].
Finishing nodes were added after detail restore: an auto-adjust node with values at zero and strength 50, and Levels with the black point raised to 10, which he credits for better colour and contrast, and which he says suit any workflow [37:09, 38:56].
Mask the text only: transferring the whole subject lost relight detail [39:30]. If the product sits at 70% scale in the composition, the text is small and the default blur of 32 smears it, so use 16 [41:03].

**Use it:** the pattern is "return only the damaged parts from the source, and keep that step cheap to redo".
