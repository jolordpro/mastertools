---
id: lighting-dome-bg-dome-quad-rig
title: Light with an HDRI dome, a separate background dome with contributions off, and a few area lights on a null rig; judge in clay mode
domain: lighting
tags: [dome light, hdri, area light, clay mode, key fill, background dome, rig]
applies_to: Redshift in C4D (2023)
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=le17-h6tUD0, src:yt-transcripts, https://www.youtube.com/watch?v=RpiCCLHjlWQ, https://www.youtube.com/watch?v=LcxjkHFS-2k]
feeds: [lookdev, coach]
conflicts: none
---
Start with an HDRI dome: reduce saturation to about 20 percent, rotate, set intensity, and use clay mode to judge key and fill [18:09-20:14].
Second dome as background with its light contributions switched off [20:46-21:16]. Area light as child of a null child of a controller null, 50 by 50 cm for a directional shadow, spread down for a sharper edge [21:47-23:24].
Fill from below: copy the light, 120 by 120 cm, spread full [28:04]. GI multiplier 1.5 on the dome adds bounce in crevices [33:45].

**Use it:** the coach can suggest the rig and the clay-mode check.
Transcript support: Maxon trainer lists the contributions zeroed on the background dome: diffuse, reflection, transmission, single and multi scatter, GI, volume, and shadows (https://www.youtube.com/watch?v=RpiCCLHjlWQ [32:29-34:02])
Transcript support: Chad (2017) likes the dome saturation control to tame blue HDRIs and the built-in back plate (https://www.youtube.com/watch?v=LcxjkHFS-2k [11:23-11:54])
