---
id: redshift-procedural-dome-background-contributions
title: A procedural dome light as a background: camera contribution 1, diffuse, single scatter and GI at 0
domain: redshift
tags: [dome light, procedural, ramp, maxon noise, background, ray contributions, rs dome light material]
applies_to: Redshift 2026.5 / C4D 2026.2
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=dFYep-8B0aU, src:yt-transcripts, https://www.youtube.com/watch?v=dcLT_1mskBU, https://www.youtube.com/watch?v=Gfz0jfx0EmM]
feeds: [redshift, elevate]
conflicts: none
---
[26:32] Dome light > Add Graph creates an RS Dome Light material; set Map Source to Shader and feed a Ramp, Maxon Noise or Tile shader. No texture files needed.
[31:35] For a pure background: camera contribution 1, diffuse 0, single scattering 0, GI 0. It stays visible to camera, reflections and transmission but adds no light. Good behind clear plastic and glass.
The same graph can be a light with a gobo effect by leaving the contributions up.

**Use it:** suggest it when a gradient plane is used as a backdrop and reflections in glass look wrong.
Transcript support: Dome used only as background by setting its diffuse contribution to zero; also a low, large, blue-tinted fill area light for soft shadows. (https://www.youtube.com/watch?v=Gfz0jfx0EmM [01:06-01:38])
