---
id: comp-convert-hdri-and-plate-to-acescg-or-the-sky-oversaturates
title: Convert the HDRI and the back plate to ACEScg too; an unconverted linear sRGB HDRI gives an oversaturated sky
domain: comp
tags: [aces, acescg, hdri, plate, linear srgb, utility linear srgb, davinci resolve, meshmen, deep-read]
applies_to: any ACES pipeline
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=3_dlZVNlrIc, src:yt-transcripts]
feeds: [redshift, post-composite]
conflicts: none
---
Augustine [19:42-23:28]: a shot HDRI stitched in linear sRGB, used as is, looks oversaturated and unreal in the sky next to the same HDRI converted from utility linear sRGB to ACEScg; with the OCIO colour-space transform the two match exactly in a test. For a Rec.709 camera use linear Rec.709 as the source, nearly the same except for a short linear toe [23:28]. Back plates: grade in Resolve, export as ACEScg EXR, load into the renderer, and view through the sRGB view; the render and plate then match closely [24:41-28:23]. Shadow-catcher pass and the alpha-forward shadow merge are done in the comp [32:01-33:04].

**Use it:** Add HDRI and plate to any "inputs converted" gate beside textures.
