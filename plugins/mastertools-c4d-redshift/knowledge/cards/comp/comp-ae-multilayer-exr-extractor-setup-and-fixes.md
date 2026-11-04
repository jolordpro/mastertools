---
id: comp-ae-multilayer-exr-extractor-setup-and-fixes
title: AE multilayer EXR: match the sequence frame rate to the plate, linearize the working space, split passes with Extractor, set shadow below and AO multiply, check unmultiply
domain: comp
tags: [lightarchitect, after effects, multilayer exr, extractor, linearize working space, interpret footage, frame rate, unmultiply, ambient occlusion, deep-read]
applies_to: After Effects 2021, Blender EXR
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=UvESlM11nF8, src:yt-transcripts]
feeds: [[comp, shakedown]]
conflicts: none
---
LightArchitect (Blender VFX tutor, 2021, low). Steps [00:38-04:47]: import plate and EXR sequence; set the sequence frame rate to the project's (23.976 in his case) via Interpret Footage, since a mismatch breaks the camera track match; a plain drop shows black until passes are extracted; turn on Linearize Working Space with an sRGB working space in project settings and check the EXR's colour management is sRGB too; apply the 3D Channel Extractor effect and pick the layer (combined beauty), duplicate the layer per pass (shadow combined moved below the object, AO as Multiply); if a pass has no alpha, raise the black level in the Extractor; tick unmultiply on every pass layer so blurred transparent edges do not render dark artefacts.

**Use it:** Matches the comp template steps for Redshift multichannel EXRs in AE (frame rate, linear workspace, one Extractor per pass). Working space sRGB is his 2021 choice; confirm against current colour rules.
