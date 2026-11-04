---
id: ai-models-switchhdr-exposure-threshold-mask-ap0-exr
title: SwitchHDR makes 16-bit linear ACES AP0 EXRs from 8-bit SDR, with an exposure-threshold mask and optional prompt for the blown areas
domain: ai-models
tags: [beeble, hoon kim, conrad curtis, siggraph 2026, switchhdr, sdr to hdr, aces, ap0, exr, highlights, ltx, deep-read]
applies_to: SwitchHDR (2026)
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=weXc-JGwewo, src:yt-transcripts]
feeds: [comp]
conflicts: none
---
Kim [51:37-54:15]: SDR to HDR is a one-to-many problem, since a blown white could be cloud, sky or dirt. SwitchHDR is trained on real HDR footage and gives control: the mask comes from an exposure threshold (everything above it is open to new detail), and a prompt can steer what appears there.
Output is linear ACES 2065-1 (AP0) 16-bit EXR from 8-bit input [53:44]. Launched about two weeks before the talk [04:20].

**Use it:** a bit-depth gap in AI plates can be bridged for grading, but expect invented highlight detail; inspect before accepting.
