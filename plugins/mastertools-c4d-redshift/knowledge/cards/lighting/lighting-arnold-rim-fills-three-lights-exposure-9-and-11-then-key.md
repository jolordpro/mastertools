---
id: lighting-arnold-rim-fills-three-lights-exposure-9-and-11-then-key
title: Arnold area-light recipe: three rim lights (left and right at exposure 11, middle at 9), then a smaller key at 11
domain: lighting
tags: [arnold, maya, rim light, key light, exposure, soft edge, before after, render snapshot, deep-read]
applies_to: Maya Arnold
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=dfrk5t6X-7E, src:yt-transcripts]
feeds: []
conflicts: none
---
Host duplicates the left rim for the right side and mirrors its Y rotation (negative 120 becomes positive 120) [01:40]. Settings on every light: roundness 1, soft edge 1, samples 2, transmission 1 (stronger kicks on glass and metal reflections) and nothing else touched [02:47]. Left and right rims at exposure 11, middle rim at 9 [04:52]. The side rims also act as a soft fill that softens contact shadows on the floor without blowing out [03:51]. Key light made about half the size of the rims, exposure 9 then 11, aimed from an angle [06:31]. He saves a render-view snapshot after each light, named with the lights and exposures, to flip before and after [09:00].

**Use it:** the named before/after snapshots per light are a habit worth copying for light tests.
