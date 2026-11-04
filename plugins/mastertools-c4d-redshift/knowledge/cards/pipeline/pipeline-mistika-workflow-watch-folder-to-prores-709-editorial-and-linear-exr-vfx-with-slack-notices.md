---
id: pipeline-mistika-workflow-watch-folder-to-prores-709-editorial-and-linear-exr-vfx-with-slack-notices
title: Mistika Workflows (SGO) - a watch folder triggers a Slack notice, fixes the RAW colour setting, then makes a Rec.709 ProRes for editorial and a linear EXR for VFX
domain: pipeline
tags: [mistika, sgo, dailies, watch-folder, prores, exr, linear, slack, deep-read]
applies_to: Mistika Workflows (2021)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=gqpVdX8k2xU, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Whisper transcript, so term spelling is garbled ("Mystica", "progress" for ProRes) [00:00-11:51].
Node order: Watcher on a folder (a short wait lets a sequence finish copying) -> Slack "new footage" message -> RED node setting one internal colour space and gamma for all RED files (his example DRAGONcolor and Log3 gamma, as heard; probably Log3G10) [02:18-03:26] -> ProRes for editorial in Rec.709 with a burnt-in slate (clip name and timecode) and optional 1080 proxy [04:00-05:05] -> EXR sequence at full resolution in linear for VFX [05:41-06:46] -> FTP upload set to run before the final Slack "finished" message [07:17-07:55]. Output folders get the name of the dropped folder; the editorial file had timecode and HD size, the EXR did not [10:14-11:22].

**Use it:** the department split is a model: editorial gets display-referred proxies, VFX gets scene-linear full size.
