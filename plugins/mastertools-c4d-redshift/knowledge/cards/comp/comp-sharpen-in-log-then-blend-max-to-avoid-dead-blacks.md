---
id: comp-sharpen-in-log-then-blend-max-to-avoid-dead-blacks
title: Sharpening a linear CG render directly crushes blacks; convert to log, sharpen, convert back, and blend the result over the original in max mode
domain: comp
tags: [sharpen, log, dead blacks, max blend, nuke, vfx vibe, whisper, deep-read]
applies_to: Nuke
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=b0hbVd9aZkA, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
The presenter says a plain Sharpen node on an EXR (default linear) gives dead blacks [30:44, 31:23]. His fix: linear-to-log, sharpen, log-to-linear, then merge over the unsharpened image with the Max operation so only brighter pixels gain and darks are untouched [32:39]. Then ease with a softening of about 0.3 to 0.6 if it looks sketchy [34:24]. Whisper transcript is partly garbled (Hindi/English mix); values heard are approximate.

**Use it:** Sharpen after comp in a log-like space, and judge the blacks on a waveform; never sharpen straight on linear EXR.
