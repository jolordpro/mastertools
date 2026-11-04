---
id: lighting-octane-default-environment-is-grey-set-it-to-black
title: Octane's default environment colour is grey and acts as ambient light; set it to black or contrast and shadows are flattened
domain: lighting
tags: [octane, new-plastic, environment, ambient, contrast, path-tracing, deep-read]
applies_to: Octane for Cinema 4D (2022 video)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=J5KwV7GfbEQ, src:yt-transcripts, https://www.youtube.com/watch?v=mNcq8GD1mfI]
feeds: [[redshift, elevate]]
conflicts: none
---
New Plastic (beginner series, 2022): the default grey render looks "ugly" because the grey environment colour lights everything and kills overall contrast; change it to black on the Settings > Environment tab unless you have a reason not to [04:15]. He works in the path tracing kernel for everything; only the depth settings and GI clamp matter for lighting, higher depth gives more bounces on diffuse and specular, and higher numbers cost render time [03:12][03:44]. Later he notes a pure black backdrop may show nothing of a light's effect, so a very dark grey was needed to see bloom [22:22].

**Use it:** a scene-check analogy for Redshift: look for a stray dome or ambient colour lifting the blacks before blaming the lights.
Transcript support: Sky tag intensity to 0 for dark dramatic scenes; HDRI colour profile must be linear if it looks overblown. (https://www.youtube.com/watch?v=mNcq8GD1mfI [03:44])
