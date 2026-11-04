---
id: comp-rec709-keeps-srgb-primaries-and-white-point-changes-gamma
title: sRGB and Rec.709 share primaries and D65 white point and differ in transfer function; HDR needs PQ (up to 10,000 nits) or HLG
domain: comp
tags: [rec709, srgb, d65, pq, hlg, rec2100, transfer function, primaries, whisper, deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=Hlj5ep-85ys, src:yt-transcripts]
feeds: [shakedown, redshift]
conflicts: none
---
Perez [29:31-39:00, 1:00:37]: a colour space is three primaries, a white point and a transfer function. sRGB (1996, HP and Microsoft; IEC standard 1999) uses D65, about 6500 K. Rec.709 keeps sRGB primaries and white point but has a slightly different gamma. Transfer-function families: linear (renders), log (film scans, camera log), gamma (sRGB, Rec.709), and for HDR hybrid log gamma (HLG) and perceptual quantizer (PQ), which carries up to 10,000 nits; PQ or HLG with Rec.2020 primaries are standardised as Rec.2100. D50 is a slightly warmer white. Visible spectrum quoted as 380 to 700 nm. Whisper transcript, numbers heard clearly.

**Use it:** Use as reference when the coach explains why an sRGB preview and a Rec.709 delivery differ by gamma only.
