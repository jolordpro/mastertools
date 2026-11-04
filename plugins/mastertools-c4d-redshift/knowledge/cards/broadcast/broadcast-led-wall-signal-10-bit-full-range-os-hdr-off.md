---
id: broadcast-led-wall-signal-10-bit-full-range-os-hdr-off
title: LED wall signal chain from Unreal: send 10-bit full range with Windows HDR and driver HDR off, and tell the processor if it gets PQ or gamma
domain: broadcast
tags: [[led-wall, icvfx, unreal, ocio, pq, 10-bit, ndisplay, brompton], deep-read]
applies_to: Unreal Engine 4.27 (Epic In-Camera VFX tutorial 6)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=bh5wD1YapJo, src:yt-transcripts, https://www.youtube.com/watch?v=hN98GI8996w]
feeds: [CHECKS]
conflicts: none
---
Epic's stated expectations [01:04-02:37]: 10 bits per channel out of the GPU (8 bit will band), full-range signal (check the processor's incoming-signal panel), LED panels exposing their gamut to the processor. Do not turn on Windows HDR colour or the driver's HDR mode; those are for consumer content with metadata and let the OS interpret values. The engine frame buffer is half float, so linear scene values are encoded to 10 bit.
Then set the processor to the encoding you send; example is Brompton Tessera HDR format = PQ [03:09]. Until OCIO is applied the wall looks wrong because the desktop is sRGB-encoded [03:09].

**Use it:** Stage checklist item before any LED-wall plate or graphic test: bit depth, range, OS HDR off, processor encoding matches.
Transcript support: Seven LED walls of different pixel pitch were fed from several engines, so per-wall signal setup matters (https://www.youtube.com/watch?v=hN98GI8996w [07:29])
