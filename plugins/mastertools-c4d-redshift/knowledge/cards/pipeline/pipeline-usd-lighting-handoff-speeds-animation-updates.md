---
id: pipeline-usd-lighting-handoff-speeds-animation-updates
title: With USD, lighting sees animation updates in minutes instead of days, but delegate support and light linking limit it
domain: pipeline
tags: [francesco giroldini, dreamworks, usd, hydra delegate, solaris, light linking, pipeline, handoff, deep-read]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=GcPlNw9kFVk, src:yt-transcripts, https://www.youtube.com/watch?v=NNUtKYRmcjY, https://www.youtube.com/watch?v=CpiumJctktM, https://www.youtube.com/watch?v=bwkCfp6G-F8, https://www.youtube.com/watch?v=jpbMbafS9FY]
feeds: []
conflicts: none
---
Francesco Giroldini (lead lighting/comp artist at DreamWorks, ex-Pixar and Blue Sky; Academy of Animated Art interview): his pipeline is USD now, but you need a render delegate and some renderers lack one; exporting light and shadow linking is tricky, so it is limited for lighting [32:29-33:17].
Previously an animation change needed a new Maya file and processing, a day or two up to a week; with USD it is near-instant [33:47-34:18].
It also lets him contact artists directly and override something with their agreement, so fewer producers get involved [34:18-35:19].
Studios are exploring Solaris and other USD editors [33:17].

**Use it:** Pipeline check: confirm the renderer has a USD delegate and test light-linking round trip before relying on it.
