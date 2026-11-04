---
id: lighting-rs-block-dome-with-black-plane-primary-ray-off
title: Block part of a dome with a pure-black plane (primary rays off) to restore dark falloff in the background while keeping the fill
domain: lighting
tags: [redshift, dome light, flag, negative fill, object tag, primary ray visibility, deep-read]
applies_to: Redshift object tag
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=BlEM9iOzqMI, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
After adding the dome fill, the nice falloff into darkness vanished [17:14]. Fix: a plane with a pure black material between dome and subject to block the dome on one side, then a Redshift Object tag with Primary Ray visibility off so the camera does not see the plane [17:45][18:19]. Fill is kept, darkness comes back. If a pure black is wanted, he says finish in comp [18:55]. See also lighting-bounce-card-negative-fill-plane.

**Use it:** a negative-fill flag in 3D; remember the tag or it appears in frame.
