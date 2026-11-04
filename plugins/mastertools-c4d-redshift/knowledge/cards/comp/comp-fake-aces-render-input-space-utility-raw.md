---
id: comp-fake-aces-render-input-space-utility-raw
title: A render made with colours picked under the ACES view needs no input conversion: Utility Raw to ACEScg did nothing, so go straight from ACEScg to output sRGB
domain: comp
tags: [Zak, i_go_by_zak, fake ACES, OCIO, Utility Raw, input colour space, deep-read]
applies_to: Redshift EXR with Redshift colour management off
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=7uY4-bPvRKs, src:yt-transcripts, https://www.youtube.com/watch?v=3_dlZVNlrIc, https://www.youtube.com/watch?v=hDiYqODGoHg]
feeds: [comp-fix planner, CHECKS]
conflicts: none
---
Zak first treated his EXR as linear sRGB (Utility Linear sRGB into ACEScg) and it looked washed out versus the render view [33:00-34:02].
Utility Raw as the input matched the render view, and Utility Raw to ACEScg changed nothing, so that step can be dropped [34:34-35:36].
Reason: with Redshift colour management off the render is linear gamma and the colours were chosen in the ACES view, so they are already ACEScg values; only the sRGB gamma fix is left [35:36].

**Use it:** CHECKS: for a 'fake ACES' render, read the EXR as ACEScg (or Raw), not as linear sRGB; re-test on current OCIO config versions.
