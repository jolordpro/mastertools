---
id: ai-models-ai-does-not-recover-clipped-highlights-it-reconstructs-a-plausible-guess
title: An AI model filling a clipped highlight is reconstructing a plausible texture, not recovering the lost data; matters for restoration and forensic work
domain: ai-models
tags: [clipping, highlights, ai reconstruction, hdr, diffusion, diffhdr, restoration, vfx news, deep-read]
applies_to: Opinion segment, weekly VFX news video (Sept 2026)
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-31
sources: [https://www.youtube.com/watch?v=69ZiUbJdd-o, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
The channel's opinion segment [06:34-07:51]: when pixels clip to white the original information is gone; a generative model that adds texture is inventing something plausible. It names DiffHDR-style work that treats LDR-to-HDR conversion as radiance inpainting with a diffusion model. Fine for creative work, but for restoration, forensic or historical footage the difference between recovering and inventing matters.
Example given: a completely clipped white shirt given convincing fabric texture, with no way to know what the real shirt looked like.

**Use it:** the exposure check should treat clipped highlights as lost data; do not rely on AI inpaint to fix an overexposed plate that must be accurate.
