---
id: comp-bloom-as-separate-post-pass-screen-blend-and-gradient-vignette
title: Render bloom as its own low-sample post pass, screen it over the beauty, then add a gradient, grain and vignette in Camera Raw
domain: comp
tags: [octane, bloom, post processing, screen, photoshop, camera raw, grain, vignette, nikita kapustin, deep-read]
applies_to: Octane + Photoshop
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=gMs_iu3cMoY, src:yt-transcripts]
feeds: [elevate, post-composite]
conflicts: none
---
Kapustin renders the bloom/blur from Octane's post-processing AOV as a 16-bit PSD at far fewer samples (it does not need many) [41:07-42:45], places it over the beauty at Screen with reduced opacity so only a little bloom is added [43:16]. Jagged contours came from too low subdivision, so crank it before the final [43:48]. Finishing in Camera Raw: slight colour change, more contrast, texture up, a gradient from the right to pull the eye to the middle, then a little grain and vignette because real cameras show grain [44:21-46:00]. Final judged against a reference image pinned always-on-top.

**Use it:** The pass-then-screen bloom and the "darken the edges toward the hero" finish are cheap last steps.
