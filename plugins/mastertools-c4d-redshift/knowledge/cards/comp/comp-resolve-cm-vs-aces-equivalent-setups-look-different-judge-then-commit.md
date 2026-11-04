---
id: comp-resolve-cm-vs-aces-equivalent-setups-look-different-judge-then-commit
title: Resolve colour management and ACES with matching input and output still render different pictures; compare on your footage, pick one, stop switching
domain: comp
tags: [[aces, resolve-color-management, cullen-kelly, color-management, rec709, alexa], deep-read]
applies_to: DaVinci Resolve 17-era project settings
status: V
confidence: medium
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=TxCGR_gNTME, src:yt-transcripts]
feeds: [coach, CHECKS]
conflicts: none
---
Cullen Kelly (colorist): both are colour management frameworks that turn what the camera saw into what the display can show [00:34][03:14]. ACES maps to: input transform = Resolve's input colour space, output transform = output colour space (Rec.709 = Rec.709 Gamma 2.4) [05:51-06:51]. With equal input (Alexa Log C) and output, switching framework changed the image, so flip through the whole timeline and judge which is closer to intent [07:54-08:56]. Resolve CM exposes more parameters; ACES is quick if you do not know how to set them [06:51-07:23]. The input lists differ: if a camera has no ACES entry but has a Resolve one, that alone justifies Resolve CM [12:03-12:35].
His advice: whichever you choose, commit; second-guessing mid-grade is the worst move [13:06-13:38]. Test rather than rely on someone else's workflow [13:38].

**Use it:** A platform note when delivering to a colourist: record framework, input and output space, and keep them fixed across the job.
