---
id: comp-cdl-only-slope-offset-power-saturation-luminance-mixer-zero
title: Only slope, offset, power and saturation travel in a CDL, so match dailies with Lift, Gamma, Gain, Saturation and default Luminance Mixer to zero
domain: comp
tags: [cdl, asc cdl, lift gamma gain, luminance mixer, davinci resolve, dailies matching, deep-read]
applies_to: DaVinci Resolve
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=uaynELBZdSE, src:yt-transcripts]
feeds: [CHECKS, comp]
conflicts: none
---
For a grade to be exportable as a CDL, reduce operations to slope, offset, power and saturation, which Resolve names Lift, Gamma, Gain and Saturation [18:52][19:22]. Any other Resolve tool will not be carried by the CDL [19:22]. Resolve's Luminance Mixer compensates brightness loss from lift/gamma/gain but exists in no other software and is not written to the CDL, so default it to zero in project settings [08:14]. Result: decisions made in Resolve are reproduced in other software [08:44]. Matching aids: scopes, wipe, split screen, and up to four playheads (active playhead, shortcuts like Ctrl-Alt-A/B) [19:22][20:25]. Check the match in real time so the eye sees the luminance change [20:57].

**Use it:** a pre-send check for a handed-off grade: anything beyond SOP and saturation will not survive the CDL.
