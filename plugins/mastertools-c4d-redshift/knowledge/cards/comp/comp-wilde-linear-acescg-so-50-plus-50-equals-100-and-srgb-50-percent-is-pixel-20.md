---
id: comp-wilde-linear-acescg-so-50-plus-50-equals-100-and-srgb-50-percent-is-pixel-20
title: Michael Wilde (ILM texture artist): sRGB is non-linear (about 2.2 gamma), so 50 percent brightness is roughly a 20 percent pixel value; renders need linear ACEScg for the maths to add up
domain: comp
tags: [acescg, srgb, linear, transfer function, michael wilde, ilm, texturing, gamma, deep-read]
applies_to: Substance 3D Painter, ACEScg
status: V
confidence: medium
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=hDiYqODGoHg, src:yt-transcripts]
feeds: [coach, redshift]
conflicts: none
---
Wilde explains [2:09-6:16]: sRGB gives more code values to darks because eyes see small differences better in low light; the gamma 2.2 curve maps a brightness of 50 to a pixel value near 20 percent [3:10]. ACES is a colour management system from the Academy, not a colour space; for VFX texturing the only member he cares about is ACEScg, whose gamut covers nearly the whole visible range [4:13-5:15] and whose values equal intensity (linear), so doubling a pixel value doubles light and adding 50 and 50 gives 100; the same sums in a non-linear space give wrong results [5:15-5:45]. Goal: what you see in the paint viewport equals what appears at render time [5:45]. Sources mix compressed web JPEGs, high bit-depth set photos and procedurals, and ACEScg holds them all. Working pro (senior texture artist at ILM London), part 1 of 3, basics level.

**Use it:** One-line justification the coach can give when a client's sRGB textures look wrong in Redshift: they need an input transform to the linear working space.
