---
id: pipeline-dailies-project-settings-reel-name-timecode-framing
title: Set up dailies so every clip has a unique reel name and embedded timecode, and use framing charts to map resolution
domain: pipeline
tags: [dailies, reel name, timecode, conform, framing chart, davinci resolve, project settings, deep-read]
applies_to: DaVinci Resolve
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=uaynELBZdSE, src:yt-transcripts, https://www.youtube.com/watch?v=rgZjL2e8yEg]
feeds: [pipeline design]
conflicts: none
---
For conform, reel name and timecode are what make a clip unique, enabling automatic relink; get these right first [05:34][06:06]. Settings: resolution from sensor and capture area and target aspect, driven by the DoP's framing charts (in the example, whole frame fit to a 1.77 container) [06:39][07:09]. General options: use embedded timecode, and source clip file name for reel names (this can differ by conform workflow) [07:09][07:42]. Colour management: ACES with ACEScct [08:44]. Dailies lab duties: sync audio to picture, input metadata, best-light matching, real-time QC playback, render proxies, export metadata database [05:03].

**Use it:** a start-of-job checklist for any turnover that will be conformed later.
Transcript support: Output Blanking for delivery aspect, source timecode and clip name burn-in (https://www.youtube.com/watch?v=rgZjL2e8yEg [06:52])
