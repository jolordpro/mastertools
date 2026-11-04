---
id: lighting-aces-view-lets-sun-be-bright
title: With an ACES view transform the sun can be set at its real strength; under sRGB the same light had to drop to about a third
domain: lighting
tags: [aces, sun, infinite light, intensity, tone mapping, caustics, dynamic range]
applies_to: Redshift in C4D, ACES view in render view (2021)
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=7uY4-bPvRKs, src:yt-transcripts]
feeds: [elevate, coach]
conflicts: none
---
Infinite light multiplier 15 stays readable under the ACES view; in sRGB it clips, and the highest value without clipping was roughly 5 (about a third) [11:33-12:39].
Caustics also keep detail instead of blowing out, so no need to dim the light and lift exposure [13:10] [47:19].
Studio strobes are balanced to the camera exposure; sunlight is not, so dimming the sun to fit a low-range view is physically wrong [13:41].

**Use it:** the coach can recommend lighting in physical values with a tone-mapped view rather than dimming lights.
