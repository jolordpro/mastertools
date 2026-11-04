---
id: lighting-blue-ambient-plus-warm-small-key-gives-blue-shadows-and-sharp-edges
title: Dark blue gradient ambient plus a warm small area key gives realistic blue shadows with defined edges
domain: lighting
tags: [hdri ambient, area light key, blue shadows, warm key, shadow softness, gradient environment, distance, deep-read]
applies_to: KeyShot (principle applies to any renderer)
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=umnswWAS2vw, src:yt-transcripts]
feeds: [elevate, redshift]
conflicts: none
---
Recipe [00:32-02:37]: environment a gradient with black at the bottom and a saturated dark blue at the top for ambient; a plane turned into an area-light material for the key, coloured slightly yellow by Kelvin. He explains that blue sky ambient makes shadows read blue in real life, which looks more real than grey shadows, a stylistic choice he likes [06:52-07:25].
Adjusting the key [03:08-05:48]: to align shadow directions, move the light farther away and raise it; if shadows are too soft, make the area light smaller; then raise intensity to compensate for distance (50 then 150 in his small millimetre scene). Add contrast and bloom from the image style last [06:52]. The plane came in at 1 mm in a millimetre scene so scale had to be raised [01:34].

**Use it:** the light-size-versus-softness rule from lighting-softness-is-relative-size-of-source-to-subject, in practice; a quick colour-script start for product stills.
