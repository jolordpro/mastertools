---
id: comp-aces-grading-controls-roll-off-instead-of-clipping
title: In an ACES timeline, offset, lift and gain compress shadows and highlights like the eye, where Rec.709 YRGB clips; test it with the scopes
domain: comp
tags: [[aces, resolve, offset, lift, gain, highlights, scopes, learn-color-grading], deep-read]
applies_to: DaVinci Resolve with ACEScct
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=atdGKZnUQ5U, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Alex Jordan (Learn Color Grading, beginner channel): duplicate the timeline, one in Rec.709 YRGB and one in ACES, and drag offset up and down while watching the scopes. In 709 the waveform values move together and clip at the ends, losing shadow and highlight data [05:32-06:35]. In ACES offset behaves more like gamma, compressing both ends rather than clipping, and lift and gain do the same [06:35-08:38]. A warm push (offset toward yellow) looks more natural in ACES with fewer corrections [09:10-10:14]. He says this lets you push the image harder; the same colours can be reached in YRGB with more work [10:14].
Caveat: demonstrated by eye on scopes with an s-log clip; a beginner explainer, not measured.

**Use it:** In a grade or comp review, check whether a look was built before or after the view transform; extreme offsets in display-referred space clip.
