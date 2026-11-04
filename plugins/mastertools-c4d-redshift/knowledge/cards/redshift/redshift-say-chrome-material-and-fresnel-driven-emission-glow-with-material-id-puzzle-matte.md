---
id: redshift-say-chrome-material-and-fresnel-driven-emission-glow-with-material-id-puzzle-matte
title: Say's Redshift recipes: chrome metal in seconds, a Fresnel-shaped neon emission, and a material-ID Puzzle Matte pass for a glow in comp
domain: redshift
tags: [eric-say, redshift, chrome, ggx, fresnel, emission weight, coat, puzzle matte, material id, ledger-check, deep-read]
applies_to: Redshift 2.x in Cinema 4D R21 (2019)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=0Zg4lpwZGe0, src:yt-transcripts]
feeds: [redshift, comp]
conflicts: none
---
Claims in a 2019 talk, so check against the ledger before use [ledger-check]. Chrome: remove the diffuse, use GGX, a physically accurate IOR, reflection cranked, a small roughness for blur; Say says roughly ten seconds of effort looks good under an HDRI [30:15-31:50]. Emission: the Incandescent material is capped in brightness, so use the default Redshift material and its emission weight (he says up to 100), then a Coat for a laminated cover and a Redshift Fresnel (IOR 2 behaves like the default) plugged into emission colour so the glow falls off with angle [39:49-41:54]. Material-based pass: on the material's Output node set a Material ID to 1, add a Puzzle Matte AOV for it, and glow it in compositing; he says it only shows in the bucket render, not the IPR [42:26-42:57].
Texture tip: a ramp from a grunge map into reflection roughness, white meaning full blur; a floor with seams made by a cloner and bevel [36:39-39:18].

**Use it:** Do not apply these numbers without the ledger; keep the Puzzle Matte pass idea.
