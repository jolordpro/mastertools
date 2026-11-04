---
id: pipeline-frameio-c2c-resolve-hero-dailies-settings-keep-timecode-and-source-name
title: Frame.io camera-to-cloud into Resolve: settings so hero dailies match the camera-to-cloud proxies (embedded timecode, real names, source filename, individual clips)
domain: pipeline
tags: [pipeline, dailies, frame.io, davinci-resolve, camera-to-cloud, proxies, conform, deep-read]
applies_to: DaVinci Resolve + Frame.io C2C
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=J2Tacu9hnN8, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Frame.io camera-to-cloud tutorial (Episode 7, vendor series, host Valentina V.). Connect the Frame.io account in Resolve internet accounts; C2C clips then appear as a volume in the media storage browser and new uploads show on refresh [01:14-02:15]. Pull files into a media pool bin; separate audio and video files are brought together there, and colour or window burn can be added [02:15]. For hero dailies from original camera files, set: Project Settings > General Options > Conform Options, use timecode = embedded in source clip, and assist using real names ticked [02:45]. In Deliver, custom render, render = individual clips, set codec, then file name uses = source name so the files conform to the C2C proxies [02:45-03:16]. Export to a drive or direct into the Frame.io project [03:16].

**Use it:** The match between proxy and hero depends on timecode and source name staying identical; check those two settings before sending dailies out.
