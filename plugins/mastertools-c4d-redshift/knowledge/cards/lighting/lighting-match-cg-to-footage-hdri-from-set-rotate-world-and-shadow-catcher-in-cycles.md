---
id: lighting-match-cg-to-footage-hdri-from-set-rotate-world-and-shadow-catcher-in-cycles
title: To light CG into a plate: use an HDRI close to the footage (ideally shot on set with a 360 camera), rotate it until the light direction matches, and use a shadow-catcher ground in Cycles with transparent film
domain: lighting
tags: [max-novak, blender, hdri, shadow catcher, cycles, transparent film, deep-read]
applies_to: Blender Cycles
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=QlbZDu2tZfE, src:yt-transcripts]
feeds: [elevate, composition]
conflicts: none
---
Goal: recreate the footage lighting in 3D [04:11]. Poly Haven HDRIs are a stand-in; the best result is an HDRI captured on set when filming, with a 360 camera [04:43]. Use a Mapping node (Node Wrangler, Ctrl+T) to rotate the environment by eye to where the sun or lamps sit [06:17]. A plane aligned to the track points becomes a shadow catcher: Cycles only (not Eevee), object setting on, Film Transparent on [06:47]. Tweak roughness and specular on bought models, which arrive too reflective [07:49]. He also notes the Blender 4.0 AgX view transform as an improvement on Filmic for pulling colour back in grade [08:20].

**Use it:** Ask for an on-set HDRI and a clean plate in any CG-over-plate turnover. Related: lighting-chrome-gray-ball-lens-grid-turnover.
