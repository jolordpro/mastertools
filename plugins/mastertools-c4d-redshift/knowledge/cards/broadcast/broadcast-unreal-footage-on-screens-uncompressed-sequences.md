---
id: broadcast-unreal-footage-on-screens-uncompressed-sequences
title: Playing footage in Unreal needs three assets and works best from uncompressed image sequences
domain: broadcast
tags: [unreal, footage, media player, media texture, image sequence, frame sync, deep-read]
applies_to: Unreal Engine 4.27 (concepts carry to UE5)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=bcL001ZFHBQ, src:yt-transcripts]
feeds: []
conflicts: none
---
Screens can show live Scene Capture, a static image or video. For footage: an image media source (image sequence), a media player asset, and a media texture that outputs the player into materials; apply to a 16:9 plane and add a media track in Sequencer [16:19-17:29]. They recommend uncompressed image sequences for smoother playback and better frame-sync accuracy [17:03-17:29].

**Use it:** Deliver background plates to a real-time package as uncompressed sequences, not compressed video.
