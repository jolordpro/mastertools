---
id: broadcast-aximmetry-hdr-camera-switch-16-bit-float-plus-tone-mapper-bloom
title: Aximmetry (2018): HDR needs the camera set to 16-bit float output plus a tone mapper before bloom and streaks show
domain: broadcast
tags: [aximmetry, composer, hdr, tone mapper, bloom, streaks, lens flare, specular intensity, 16 bit float, 8 bit, deep-read]
applies_to: Aximmetry Composer (2018)
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=ORANezf5Q9o, src:yt-transcripts]
feeds: []
conflicts: none
---
To make a highlight read as very bright [30:09-32:48]: raise the specular colour's intensity multiplier above 1 (he goes toward 10), switch the camera to HDR so output goes from 8 bits per channel to 16-bit floating point, then add a tone mapper node. Without HDR output the white just burns out.
The tone mapper has a threshold for when effects start, a bloom (size, intensity), streaks (cinema, cross, star), and a simulated lens reflection from bright areas. Same chain as a real-time glow pass in broadcast graphics.

**Use it:** Keep HDR output on in any real-time graphics chain that uses glows, and tune threshold before size.
