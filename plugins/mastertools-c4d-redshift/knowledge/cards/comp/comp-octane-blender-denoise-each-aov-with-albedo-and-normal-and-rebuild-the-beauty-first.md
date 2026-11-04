---
id: comp-octane-blender-denoise-each-aov-with-albedo-and-normal-and-rebuild-the-beauty-first
title: Denoise AOVs separately, with denoise albedo and normal as auxiliary inputs, after proving the layered AOV rebuild matches the beauty; leave the volume out of the albedo/normal denoise
domain: comp
tags: [egomotion-academy, octane, blender, denoise, aov, open image denoise, albedo, normal, deep-read]
applies_to: Octane for Blender
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=NlDrXkb37lg, src:yt-transcripts]
feeds: [composition, coach]
conflicts: none
---
His reason: denoising the combined beauty cannot tell noise from fine detail across diffuse, reflection and refraction, so it smears sub-textures [26:46-27:19]. Method: build the AOVs in the Octane compositor (diffuse direct and indirect added, reflection added on top, refraction, subsurface, transmission, volume), then switch to the beauty and compare; it is right only when the rebuild equals the beauty [11:34-20:40]. Missing volume AOV made it too bright until added; transmission fixed the rest [19:04-20:07]. Apply OIDN to each, plug denoise albedo and denoise normal into its aux inputs and enable prefilter auxiliary (detail came back) [21:10-23:24]. Do not feed the volume through albedo/normal, which projects their structure into the fog; denoise it in its own group [24:26-26:04]. Final compare showed more detail than denoising the beauty [27:49-28:50].

**Use it:** Per-AOV denoise is a comp-side choice: render the aux passes, keep the layer-add check. Extends comp-denoise-direct-and-indirect-separately-then-multiply-colour.
