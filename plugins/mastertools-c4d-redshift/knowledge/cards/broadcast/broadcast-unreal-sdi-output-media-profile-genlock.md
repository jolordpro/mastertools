---
id: broadcast-unreal-sdi-output-media-profile-genlock
title: Set SDI out through a media profile: pick output port, 59.94, external genlock; check timing in Timed Data Monitor
domain: broadcast
tags: [unreal, sdi, media profile, genlock, aja, blackmagic, media capture, deep-read]
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
Patrick Wambold: production used Blackmagic 8K Pro cards. Without one, create an empty media profile, auto-configure proxies (one source, one output), then set the output (AJA fill, port, 59.94) and external reference with the genlock input, and set it as default in Project Settings [44:00-46:36]. Check timing in Window, Developer Tools, Timed Data Monitor [46:36-47:06]. The controller's media output points at the proxy asset, and it only works in Play mode; for editor preview use the Media Capture panel, and enable/disable SDI buttons exist in Play and in the web remote [47:06-48:43].

**Use it:** Checklist item for live work: frame rate, port, genlock reference, then monitor.
