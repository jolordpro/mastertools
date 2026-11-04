---
id: ai-models-ic-light-directional-lighting-masks
title: IC-Light directional lighting is steered by black-and-white gradient or shape masks into the latent, intensity about 0.8
domain: ai-models
tags: [ic-light, directional lighting, gradient mask, latent, light direction, comfyui]
applies_to: ComfyUI, IC-Light
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=sMMYSmDHAY8, src:yt-transcripts]
feeds: []
conflicts: none
---
White = light source, black = shadow [E 41:34-42:14]. Linear gradient, radial gradient, shape (circle) or hand-drawn masks; remap range 0.8 preferred, 1 too intense [43:22]. A coloured-bars option tints the light (navy worked, red too intense) [49:45-50:49].

**Use it:** idea only: a drawn light-direction mask is how this method accepts art direction, but the scene's real key direction should still come from the 3D light.
