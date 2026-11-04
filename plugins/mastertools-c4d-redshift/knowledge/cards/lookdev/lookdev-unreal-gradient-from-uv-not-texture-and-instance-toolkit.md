---
id: lookdev-unreal-gradient-from-uv-not-texture-and-instance-toolkit
title: Make gradients in the material from UV coordinates, not an imported texture, and reuse a small material toolkit between projects
domain: lookdev
tags: [unreal, gradient, banding, material instance, toolkit, patrick-wongbo, deep-read]
applies_to: Unreal Engine 4.25
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=WLdmYnkFoK4, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
An imported gradient looks janky because of texture compression, and an 8-bit alpha holds only 256 grey levels [1:48:26-1:49:27]. Wongbo pulls the red channel of the texture coordinate with a power control and a direction control, exposed on an instance, for tails, trails and falloffs [1:43:49-1:45:54]. Instances share one master; changing parameters adds no extra draw call [1:44:22]. He keeps a colour-chart material to judge exposure [1:48:26], and recommends Epic's material masterclass for more small networks [1:46:55].

**Use it:** Rebuild fades procedurally and keep reusable material assets in a shared folder.
