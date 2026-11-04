---
id: motion-unreal-render-image-sequences-not-video-for-frame-accuracy
title: Unreal's media framework is not guaranteed frame-accurate for video, so render with image sequences
domain: motion
tags: [unreal, media framework, image sequence, frame accuracy, prores, hap, patrick-wongbo, deep-read]
applies_to: Unreal Engine 4.25-4.26
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=WLdmYnkFoK4, src:yt-transcripts]
feeds: [motion-critique]
conflicts: none
---
Patrick Wongbo [41:38-42:09]: video plays fine for live or loop backgrounds (ProRes and HAP are supported), but frame accuracy of video is not guaranteed in the media framework of that time, so any shot that will be rendered out should use image sequences instead. A media track in Sequencer replaces the usual source, player, texture, material chain: add the track and pick the media texture directly [42:40]. The media track only controls playback; it has no opacity keys, so fades are done in the material [43:42].

**Use it:** Flag Unreal scenes that play video plates into a render; swap to image sequences before rendering.
