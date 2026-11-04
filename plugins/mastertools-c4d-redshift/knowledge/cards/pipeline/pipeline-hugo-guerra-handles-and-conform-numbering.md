---
id: pipeline-hugo-guerra-handles-and-conform-numbering
title: Give shots about 10 frames of handles and conform timelines from frame 1 so a changed cut can extend both ways
domain: pipeline
tags: [hugo guerra, handles, conform, xml, editorial change, frame numbering, scripts, deep-read]
applies_to: Nuke
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=FW942ZgK8Ic, src:yt-transcripts]
feeds: [pipeline plan]
conflicts: none
---
Asked what happens when the editor changes a cut, Hugo says a 100-frame shot gets ten frames of handle at each end so small trims fit [46:39-47:11]. Beyond that the shot is re-conformed from a new XML from the client and only that shot is re-exported [47:11].
His trick (captions garbled, low certainty): conform so the first frame is 1 and not 0, so the numbers still work if the editor extends backwards [47:41]. He hired a programmer to build and update the pipeline (incl. change detection) after Nuke 11 to 12 and 12 to 13 broke it [48:12-48:42].

**Use it:** Turnover spec: 10-frame handles; script to detect cut changes.
