---
id: lookdev-c4d-standard-pbr-metal-needs-conductor-fresnel-and-a-metalness-mask
title: In Cinema 4D's standard renderer, a paint-over-metal PBR material needs a metal reflectance layer with conductor Fresnel masked by the metalness map
domain: lookdev
tags: [cinema 4d, pbr material, metal, conductor, dielectric, metalness map, displacement, tutos, deep-read]
applies_to: Cinema 4D 2024 standard renderer (not Redshift)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=dgczAvhQszA, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
Tutos [00:36-10:32]: diffuse goes in Colour for fully metal, or in the default reflectance layer for mixed paint and metal. Roughness maps go in at 100% strength. For mixed materials add a reflectance layer named "metal", attenuation set to Metal, roughness and reflectance maps loaded, and the metalness map in the layer mask so painted areas do not reflect like metal [03:50-04:28]. Fresnel type: conductor for metals, dielectric for plastics [05:09]. Then AO into diffusion, normal map, and a height map into displacement; he cut displacement height to 1 after a test [06:16]. If displacement does not show, a "Render Perfect" tag setting on the object has to be unchecked [06:48]. Raise the viewport texture preview size to match the map (4K) at the cost of speed [02:12]. Texture prompts for "copy image" answered No to avoid duplicates.

**Use it:** Only for the C4D standard renderer; Redshift materials use their own metalness slot, so do not copy the layer set-up there.
