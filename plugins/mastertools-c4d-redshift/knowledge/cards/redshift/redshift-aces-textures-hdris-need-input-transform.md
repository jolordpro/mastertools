---
id: redshift-aces-textures-hdris-need-input-transform
title: Under old Redshift ACES setups, diffuse/specular textures and HDRIs had to be converted to ACEScg and the colour picker is unmanaged
domain: redshift
tags: [aces, idt, diffuse texture, hdri, colour picker, brand colour, pico]
applies_to: Redshift 3.0.46 (2020 video); modern C4D 2026 tags inputs natively
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=vEoIXTbyz6o, src:yt-transcripts, https://www.youtube.com/watch?v=3_dlZVNlrIc]
feeds: [coach, lookdev]
conflicts: c4d-2026-ocio-acescg-default
---
[06:22] Only textures that set final pixel colour need converting: diffuse and specular colour (diffuse alone is enough nine times in ten).
[09:27] The C4D colour picker has no colour management, so for an exact brand colour use a Colour node and run it through an sRGB-to-ACEScg conversion.
[18:16] HDRIs were converted outside (Pico: input utility linear sRGB, 16-bit half EXR, target ACEScg).
Superseded in part by C4D 2026 OCIO input tagging; see the existing C4D 2026 card.

**Use it:** when a brand colour looks off under a view transform, check that its input space is tagged.
