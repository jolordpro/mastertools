---
id: lookdev-volpatto-bayer-sensors-resolve-about-75-percent-and-lens-mtf-caps-zooms
title: "Volpatto: a Bayer sensor resolves about 75 percent of its pixel count, so a 6K camera is roughly 4K, and a digital zoom cannot beat the lens"
domain: lookdev
tags: [resolution, mtf, bayer, sensor, polish, walter-volpatto, deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=mtAmXRWXTx0, src:yt-transcripts, src:polish-roster]
feeds: [shakedown]
conflicts: none
---
Chain of losses he lists: lens aberrations, an optical low-pass filter (a blur), then a single-chip colour mosaic capturing about a third of colour per photosite [15:42-17:47].
On an average natural image a Bayer camera delivers about 75 percent of the sensor's pixel count, so 6K is roughly 4K and 8K roughly 6K [17:47-19:53].
His thought experiment: a test pattern exactly matching the Bayer chips reads as white, and shifted one pixel reads as black [17:47-18:50].
If a lens gives an 8K image and you crop the centre two times, you effectively have a 4K lens, because the lens MTF stays the same [20:24-20:56].
Halving the photosite size, as he puts it, gives about four times the noise; larger photosites beat more pixels [22:58-23:59].

**Use it:** Don't promise sharpness from pixel count: count the full chain (lens, filter, debayer, scale) and don't zoom a crop beyond the lens limit.
