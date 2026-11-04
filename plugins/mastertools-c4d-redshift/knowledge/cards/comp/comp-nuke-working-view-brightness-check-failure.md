---
id: comp-nuke-working-view-brightness-check-failure
title: Failure story - Alex tended to comp too dark because the viewer gain or transform was brighter than the output
domain: comp
tags: [alex, levelup plus vfx, nuke, viewer gain, display transform, too dark, final output, deep-read]
applies_to: Nuke
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=ETV1VTV0vNg, src:yt-transcripts]
feeds: [comp, shakedown]
conflicts: none
---
He says he often ends up with scenes that are too dark, and on this one likely worked with the view slider or Rec.709 transform brightening the image, then fixed it at the end with the final colour-space step [04:36-05:06].
He also notes the working image looks balanced but is much brighter than the final, so he checks that the foreground survives the later darkening [15:03].

**Use it:** QC habit: check the viewer is reset (gain 0, correct transform) before judging brightness, and compare the final-output view of the subject.
