---
id: lookdev-bump-normal-displacement-what-each-channel-costs
title: Bump fakes relief from greyscale, normal fakes it from RGB direction, displacement moves geometry and costs render time; weigh it against what the camera sees
domain: lookdev
tags: [bump, normal map, displacement, 16 bit, material channels, render time, andrey lebrov, deep-read]
applies_to: Octane for C4D (2018), principle general
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=a8d6p-E4KSE, src:yt-transcripts]
feeds: []
conflicts: none
---
Andrey Lebrov [01:15-04:56, 10:47-11:50]. Diffuse = colour; specular = which areas are shinier; roughness = rough, worn or blurry areas. Bump uses greyscale (white up, mid-grey untouched, black down) and changes shading only. Normal uses RGB mapped to X, Y, Z and also fakes geometry only; good ones are baked from a high-detail mesh. Displacement really moves geometry, so it is king for detailing low-res meshes, benefits from 16- or 32-bit greyscale, traditional CPU engines need the mesh subdivided first, while Octane can displace any mesh with up to 8k maps. It costs render time, so weigh its benefit against a normal map, which sometimes gives the same look. For a more distant master shot, skip displacement. Add texture only to what the viewer will see; realistic usually means high-res, which raises render times. If a material does not feel right, test the lighting before changing the material [10:16].

**Use it:** The advisor can ask 'how close is the camera?' before recommending displacement over bump or normal.
