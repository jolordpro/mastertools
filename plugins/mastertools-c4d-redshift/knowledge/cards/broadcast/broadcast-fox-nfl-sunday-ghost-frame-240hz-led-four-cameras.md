---
id: broadcast-fox-nfl-sunday-ghost-frame-240hz-led-four-cameras
title: Fox NFL Sunday stage splits a 240 Hz LED wall into 60 Hz slots so four cameras each see their own perspective, one frame in four
domain: broadcast
tags: [virtual production, led volume, ghost frame, 240 hz, multi-camera, fox sports, nfl sunday, unreal engine, deep-read, unreal fest 2022, epic games, avalanche, andy blondin, bernt bk, multicamera, girraphic]
applies_to: Unreal Engine LED volume, Fox Sports
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=rOe6Gw9TvJg, src:yt-transcripts, https://www.youtube.com/watch?v=XAtjoawRN_Y]
feeds: [broadcast, pipeline design, estimator]
conflicts: none
---
Fox NFL Sunday volume (Fox Sports team; speakers not named in captions): a live show needs a preview, and multiple cameras each need their own render of the wall, which most volumes do not do (usually one tracked camera) [02:10][02:41]. Ghost frame: LEDs run at 240 Hz and are subdivided into 60 Hz increments so each camera takes every fourth frame, each with its own perspective and tracking data; the talent sees a blurry mix on the wall [02:41][03:12]. Cost: four engines per camera, four cameras, 4K per machine, so 16 engines for the wall; seven more for AR compositing; two for monitor tunnels showing parallax, 25 total [03:12][03:42][04:13]. Holding 60 fps at that resolution is called a challenge [03:42].
Merged from `broadcast-fox-led-studio-ghost-frame-16-engines`: A live director must see the shot they are about to take. With LED walls, when one camera's angle is rendered onto the wall the other cameras do not get theirs; he calls ghost frame technology the secret sauce that made live multi-camera work [04:22-05:29]. (How it works is not explained in the talk.) Fox's studio ran 16 Unreal engines for four cameras in real time and seven more just for AR; Girraphic worked on it [05:29]. BK's framing: Fox 'differentiates by being bold' [04:57].

**Use it:** reference when estimating render budget for a multi-camera real-time sports set; each added camera multiplies engine count.
