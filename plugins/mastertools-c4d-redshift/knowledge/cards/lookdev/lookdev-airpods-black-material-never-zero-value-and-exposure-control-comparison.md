---
id: lookdev-airpods-black-material-never-zero-value-and-exposure-control-comparison
title: "HTArchviz beginner: set black materials to a small non-zero value, and compare renders with and without the exposure control before deciding to use it"
domain: lookdev
tags: [airpods, lookdev, albedo, exposure, vray, beginner, deep-read]
applies_to: 3ds Max V-Ray
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=nUk3Zs91kZU, src:yt-transcripts]
feeds: [redshift]
conflicts: none
---
He says he used to put full zero black on products and learned not to; use a value of 1 or 2 instead because there is no true zero reflectance [10:31-11:03].
He prefers shaping with lights over the camera exposure control, and checks by cloning the frame buffer and rendering with the exposure setting on and off to see the difference [13:09-15:05].
A white environment backdrop adds white reflections to black plastic; a black backdrop at a low value (5) was nicer [16:12-16:46].
Final pass in the V-Ray frame buffer: curves to darken blacks, highlight burn to reduce clipped speculars [31:34-33:07].
Supports the existing albedo card.

**Use it:** Black-product look-dev: albedo floor above zero, compare with and without any exposure control, finish with a levels/curves pass.
