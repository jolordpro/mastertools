---
id: ai-models-comfyui-hunyuan3d-texture-existing-mesh-steps
title: Order of the free ComfyUI workflow that retextures a UV'd mesh: main view, prompt, de-light, other views, 4x upscale, face detail, bake
domain: ai-models
tags: [comfyui, hunyuan3d, texturing, uv, upscale, denoise, normal map, mixamo, workflow steps, deep-read]
applies_to: ComfyUI, Hunyuan3D, Flux/SDXL (2025)
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=o5ZqrVNoeiI, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Order [05:43-10:24]: load the mesh (leave UV auto-generation off if UVs exist); set the texture output size; pick the main view the texture is generated from (front for a humanoid, side for a quadruped); style prompt plus subject prompt plus negative prompt; background removed to white; de-lighting step often loses detail so blend it with the original; generate the other views (bad ones are re-rolled by changing the seed); upscale about 512 px views to 2K with ControlNet to hold proportions, optional second 2x for 4K; face detailer; bake to the original UVs, with a normal map. Keep denoise on the upscaler low, since a high value let it invent flip-flops [09:23-09:53].
In Blender set the normal map image to Non-Color [10:24]. The paid tier adds IP-Adapter style reference, inpainting masks, height map [11:27-12:29].
Setup traps: install missing custom nodes, then a Hunyuan wrapper folder was misnamed (missing a letter) and needed renaming [04:10-05:13].

**Use it:** a recipe reference; models change fast, but the order (main view, de-light, multi-view, upscale, bake) is the pattern to compare against.
