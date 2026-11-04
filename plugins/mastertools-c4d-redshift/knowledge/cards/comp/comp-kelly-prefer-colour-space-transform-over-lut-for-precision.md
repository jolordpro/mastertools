---
id: comp-kelly-prefer-colour-space-transform-over-lut-for-precision
title: "Cullen Kelly prefers floating-point colour space transforms to LUTs when both can do the job, because LUTs interpolate and have bounds"
domain: comp
tags: [cullen-kelly, lut, colour space transform, interpolation, precision, dctl, show lut, polish, deep-read]
applies_to: DaVinci Resolve, any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=dSYTWErq0Vw, src:yt-transcripts, src:polish-roster]
feeds: [comp, coach]
conflicts: none
---
A LUT is a table of sample points; most pixel values fall between the samples and are estimated by interpolation, however many samples there are, and the table has hard upper and lower bounds [40:08-43:47]. A colour space transform has neither limit. He says a very trained eye probably could not tell the two apart on an Alexa-to-709 conversion, but you do not have to wonder if you use the precise tool [44:19-44:49]. LUTs still win when the transform must travel: into a camera for a show LUT, or to someone who cannot run your maths, because a LUT is portable [44:49-45:52]. For his own YouTube intros he uses DCTL tools that compute every pixel rather than a baked LUT, mostly because they are quicker to build [59:14-59:49].

**Use it:** In the platform pipeline use transforms or OCIO for conversions; reserve LUTs for hand-offs that need a portable file.
