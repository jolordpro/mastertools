---
id: ai-models-controlnet-passes-from-3d-depth-lines-colour-masks
title: Feed Stable Diffusion ControlNet with passes from the 3D scene: inverted depth (white near), line art, and flat-colour region masks, rendered at Standard colour management
domain: ai-models
tags: [controlnet, depth pass, canny, line art, region masks, comfyui, stable diffusion, render passes, blender, deep-read]
applies_to: Blender, ComfyUI, SDXL (2024)
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=mu3JEfx3PHM, src:yt-transcripts]
feeds: [challenger, pipeline design]
conflicts: none
---
Creator (Sebastian Koenig style channel, name not given) replaces AI pre-processors, which flicker on sequences, with exact passes from the 3D scene [01:32][02:03]. Depth: enable the Z pass, normalise 0-1 with a map range, invert so near is white and far black, tweak with a curve, write via file output with colour management set to Standard (stated as very important) [02:03][02:33][03:05]. Lines: Freestyle as a render pass, white, thinner lines [03:05][03:37]. Masks: simple emission shaders in random flat colours, one per object or region; Cryptomatte does not work with these tools yet [03:37][04:07]. In ComfyUI the colours become hex-coded masks, each with its own regional prompt [04:38][05:08]. Strengths: depth ControlNet near full (maybe reduced slightly), canny at a low strength [05:39].

**Use it:** the same pass set (depth, outlines, ID colours) could be exported from C4D + Redshift to drive an AI restyle.
