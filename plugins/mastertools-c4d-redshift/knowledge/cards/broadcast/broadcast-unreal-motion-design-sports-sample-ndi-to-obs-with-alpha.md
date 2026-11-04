---
id: broadcast-unreal-motion-design-sports-sample-ndi-to-obs-with-alpha
title: Unreal's Motion Design sports sample sends rundown graphics with alpha over NDI to OBS; preview does not broadcast, take does
domain: broadcast
tags: [unreal, motion design, sports sample, ndi, obs, distroav, rundown, lower thirds, pixel prof, deep-read]
applies_to: Unreal Engine 5 Motion Design tools (2025), OBS, NDI Tools
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=lZpiYHbHgR8, src:yt-transcripts, https://www.youtube.com/watch?v=Ty6etYkvaC8, https://www.youtube.com/watch?v=jsXSW_fcTKY]
feeds: [[]]
conflicts: none
---
Pixel Prof Motion Design [01:03-05:18]: install the free NDI Tools (Windows) and the DistroAV plugin so OBS can receive NDI [01:03-01:37]. In Unreal, open the lower-thirds rundown in the sports sample; channel zero is already set to an NDI output with the source name "Unreal Engine output" and is started with Start All Channels (green light) [02:39-03:12]. Preview plays only inside Unreal; "take" or "take next" sends to the broadcast channel [03:44]. In OBS add an NDI source and pick the Unreal output; the alpha arrives so the graphic keys over the video, and takes show live [03:55-04:47].

**Use it:** Quick path to prove an Unreal lower-third rundown into a streaming switcher without SDI hardware.
Transcript support: Starting point is the Rundowns folder; each page holds remote-control values and names the level that plays it; Preview In/Next/Out simulates air; level assets named FS (full screen) in Content/Scenes. (https://www.youtube.com/watch?v=Ty6etYkvaC8 [02:37-04:39])
Transcript support: in-sample sequences drive visibility and transforms; rundown plays in Sequencer (https://www.youtube.com/watch?v=jsXSW_fcTKY [04:08-08:24])
