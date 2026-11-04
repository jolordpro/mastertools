---
id: comp-resolve-render-grade-routine-one-node-per-job-lift-blacks-first-halve-it
title: Resolve grade routine for renders: one node per job, lift blacks before the transform, then halve every move
domain: comp
tags: [resolve, grading, waveform, lift gamma gain, vignette, glow, film grain, h264 bitrate, dehancer, deep-read]
applies_to: DaVinci Resolve 19 (free and Studio)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=2Q3CybANHKE, src:yt-transcripts]
feeds: [elevate]
conflicts: none
---
Faucher's order after the ACES node: add serial nodes named for their job (contrast, colour correction, vignette, light ray, glow) [13:02]. Watch the waveform: lift moves low end, gamma mids, gain highs, offset shifts everything evenly [12:31]. If blacks nearly clip, raise them slightly in a node before the ACES transform so the contrast node has room to crunch them later [13:34]. Saturation cranked temporarily shows which colours dominate; hue-vs-sat and hue-vs-hue then pull blues down and warm greens for cohesion [14:35]. Circular masks paint a vignette and a fake god ray [16:38]. Glow set to screen is less strong; watch for too bloomy [17:39]. Rule of thumb: finish the grade, then halve it [17:39]. Film look creator (Studio, from v19) bundles these. His H.264/H.265 export rule: bitrate in kbps about frame rate x2000, so 24 fps = 48,000 and 30 fps = 60,000 (his number; check against delivery spec) [22:49]. He says a paid grain plugin that softens the image beats overlay grain [20:46].

**Use it:** the lift-blacks-before-the-transform and halve-it rules are portable review checks.
