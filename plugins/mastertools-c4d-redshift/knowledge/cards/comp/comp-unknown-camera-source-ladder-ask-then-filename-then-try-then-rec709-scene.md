---
id: comp-unknown-camera-source-ladder-ask-then-filename-then-try-then-rec709-scene
title: When a clip's camera is unknown: ask the DP, read the file name, try a few profiles, and fall back to Rec.709 scene
domain: comp
tags: [unknown source, stock footage, input colour space, darren mostyn, resolve, deep-read]
applies_to: DaVinci Resolve, any
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=AAeZKZ5feGA, src:yt-transcripts]
feeds: [coach, shakedown]
conflicts: none
---
Darren Mostyn's order for footage of unknown origin [22:47-24:53]: first phone the production company or DP; if that fails, read the file name (Sony, Canon and others each write names in a recognisable pattern) to find the maker; then try a few log profiles, which can work even across makers (he has used an ARRI profile on Canon footage); if none look right, set the input to Rec.709 Scene and grade it like display-referred. Rec.709 Scene is also what he uses for stock footage that is already graded. Then send it on to ACES or wide-gamut working space so it still sits in a managed pipeline. Single YouTube colourist, low confidence.

**Use it:** The coach's order of questions when a client sends footage with no spec, and a safe default so it never blocks the job.
