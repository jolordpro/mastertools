---
id: comp-unreal-render-linear-srgb-tone-curve-off-then-aces-transform-in-resolve
title: Unreal to Resolve: render EXR in linear sRGB with the tone curve off, then convert with an ACES Transform node; expect about one stop darker than the viewport
domain: comp
tags: [unreal, movie render queue, tone curve, linear srgb, aces transform, resolve, ocio, exr, viewport match, deep-read]
applies_to: Unreal Engine 5.x, DaVinci Resolve 19
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=2Q3CybANHKE, src:yt-transcripts]
feeds: [CHECKS, coach]
conflicts: none
---
William Faucher (practising artist, but he says he is no colour scientist). EXR always; JPEG/PNG fall apart in grading [01:35]. Tone curve on (default) gives a 1:1 viewport match but a baked non-linear image that grades poorly; tone curve off writes linear sRGB, which he recommends [04:10]. Do not confuse tone curve with tone mapper [01:35]. Resolve ACES Transform node: tone-curve-on frames use input sRGB linear (odd but right) and output sRGB texture; tone-curve-off frames use input linear sRGB and output sRGB; ACEScg frames use input ACEScg and output sRGB, and the last two come out identical [08:20]. Linear frames sit about one stop under the viewport because Unreal's curve is ACES-flavoured, not true ACES [09:24]. For a perfect match: create an OCIO config asset pointing to OCIO:default, then in the viewport enable OCIO display with linear sRGB and the ACES 1.0 SDR video view [03:07, 10:28]. Optional: set post-process blue correction and expand gamut to zero [05:14].

**Use it:** supports project-level ACES input cards; the rule is to keep one reference JPEG to prove the conversion before grading.
