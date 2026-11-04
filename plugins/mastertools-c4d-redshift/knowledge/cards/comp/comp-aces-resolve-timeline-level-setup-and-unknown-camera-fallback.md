---
id: comp-aces-resolve-timeline-level-setup-and-unknown-camera-fallback
title: Per-timeline ACES in Resolve: untick use-project-settings, set ACEScct and the Rec.709 output; unknown camera means no input transform and Auto Color will fail
domain: comp
tags: [[aces, resolve, timeline-settings, input-transform, unknown-camera, auto-color], deep-read]
applies_to: DaVinci Resolve (ACEScct)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=atdGKZnUQ5U, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Setup in the video [00:30-03:39]: copy the timeline, Timeline Settings, uncheck "use project settings", Color tab, color science ACEScct, set only the ACES output transform to Rec.709 (99.9% of cases, he says). Then per clip set the ACES input transform to its camera (Sony S-Log2 vs S-Log3, etc.) so mixed cameras normalise [04:29-05:01].
If the camera is unknown, set "no input transform", grade by hand; Auto Color mostly fails because of mismatch, and a fix he suggests is lowering gamma and raising gain slightly afterwards [10:46-11:46]. Existing card on project-level input covers linear sources.

**Use it:** Ask for camera and log format at turnover; unknown source means manual grade, no automatic shortcut.
