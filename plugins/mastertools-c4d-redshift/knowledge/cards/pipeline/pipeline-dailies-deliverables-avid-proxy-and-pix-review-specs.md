---
id: pipeline-dailies-deliverables-avid-proxy-and-pix-review-specs
title: Dailies deliverables: ask post for the editing codec first; example is DNxHD 1080p 36 8-bit for Avid and H.264 limited to 4000 for PIX review
domain: pipeline
tags: [dailies, dnxhd, h.264, pix, burn-in, render queue, naming, davinci resolve, deep-read]
applies_to: DaVinci Resolve
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=uaynELBZdSE, src:yt-transcripts, https://www.youtube.com/watch?v=rgZjL2e8yEg]
feeds: [delivery]
conflicts: none
---
Always ask the post house for its preferred editing codec [22:05]. The example editorial proxy uses the Avid AAF preset, DNxHD, type DNx 1080p 36 8-bit [22:37]. Review files for PIX used the H.264 master preset with video quality restricted to 4000 and checked audio tab; PIX specs vary by project [25:16]. Burn-ins from metadata: source timecode, source clip name, camera, good take, date, day, shot, take, scene, kept out of the key part of the frame, saved as a preset [23:10][23:40]. Both deliverables must share the same naming convention; use EDL clip name token to follow the media-pool name, render as individual clips, and use a different burn-in template for review files [25:48][26:22]. QC: play back all of the day's footage in a controlled room at 4K with the highest debayer, noting problems in description fields [21:33][22:05].

**Use it:** reference when specifying a review or proxy deliverable; the 4000 and DNx36 numbers are examples from one tutorial, not standards.
Transcript support: ProRes 422 Proxy or DNxHD 1080p 36 8-bit for Avid; ask the editor; 720p for very large projects (https://www.youtube.com/watch?v=rgZjL2e8yEg [14:31])
