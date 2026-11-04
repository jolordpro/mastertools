---
id: lookdev-octane-textures-white-background-for-roughness-and-keep-the-transform-linked
title: Octane texture hygiene: white backgrounds for roughness and bump maps, matching colour space, and one transform node linked to every channel
domain: lookdev
tags: [octane, texture, roughness, bump, normal, non-colour data, transform, logo mask, uv, deep-read]
applies_to: Octane standard surface
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=wAVOwrxLHcA, src:yt-transcripts]
feeds: []
conflicts: none
---
Anton (September channel, a self-taught artist then finishing a VFX degree), auto-captions. Roughness and bump maps exported with a transparent PNG background misbehave in Octane; export with a white background [30:28]. Colour space: ACES for colour textures, non-colour data for normals, roughness needs none [27:53]. Keep the UV transform node plugged into normal and roughness as well as colour, or maps drift apart [44:37]. A duplicate transform scaled much smaller adds fine normal detail visible in close-ups at high resolution [46:21]. A logo texture plugged into specular weight or metalness makes only the logo shiny; a colourise plus multiply node gives it a black underlay for legibility [36:43]. Low base roughness (0.5) controls the shine [32:03].

**Use it:** a texture-export checklist item for logo and pattern work.
