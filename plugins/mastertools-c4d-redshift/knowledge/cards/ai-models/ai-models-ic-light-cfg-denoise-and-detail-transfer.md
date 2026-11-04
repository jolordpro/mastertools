---
id: ai-models-ic-light-cfg-denoise-and-detail-transfer
title: IC-Light settings that worked: CFG about 2, denoise 0.9, and mask only text and logos for detail transfer
domain: ai-models
tags: [ic-light, cfg, denoise, detail transfer, logos, text, mask blur, frequency separation]
applies_to: ComfyUI, IC-Light, Juggernaut checkpoint
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=sMMYSmDHAY8, src:yt-transcripts, https://www.youtube.com/watch?v=weXc-JGwewo]
feeds: [coach]
conflicts: none
---
CFG range 1.5-3 with 2 the sweet spot, steps 35 for that checkpoint, denoise 0.9 [E 31:59]. Generation distorts small text, so a high/low-frequency separation transfers details back from the original product photo through a mask [32:31-34:27].
Mask only the text or logo; transferring the whole subject loses the relight [39:30]. Mask blur 32 default, 16 for small text, 32 again for 4K [40:31-41:34, 57:24]. Upscale only by 2x, 4x, 6x, and never beyond the original photo's resolution [52:30-53:02].

**Use it:** if the platform ever offers AI relight, keep brand marks out of the generated area and return them from the source.
