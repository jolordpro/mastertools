---
id: ai-models-code-motion-skill-rules-storyboard-first-svg-ui-overlap-keys-and-bug-fixes
title: Code-built launch video with Claude: storyboard first, SVG UI from Figma, overlapping keys, and the usual failures with their fixes
domain: ai-models
tags: [claude, code motion, launch video, storyboard, svg, easing, 60 fps, safe zones, skill, deep-read]
applies_to: Claude (Opus 5.5 per the video) generating code-rendered video
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=D5qpBbEWTxo, src:yt-transcripts]
feeds: [motion-critique]
conflicts: none
---
Sanji Nai-Chien (self-reported, sales-flavoured; low confidence). The motion skill he feeds Claude: four-beat story (attention, problem, fix, payoff), cut any scene that serves none [08:16]; important items stay on screen about 1.5 s; entries about 0.5 s with slight overshoot, exits faster than entries; clicks get a small press; cursor travels on an arc; nothing fully stops [08:49]. Build like AE: parent groups, offset starts by a couple of frames, start the next move before the last settles [09:21]. Specs 1920x1080 at 60 fps with safe zones for vertical [09:51]. Inputs: brief, scene-by-scene storyboard (what shows, how long, camera), brand colours and fonts, UI exported as SVG not screenshots, since zooms stay sharp [10:52]. First render broke: overlapping text, fast pan, layout off canvas, font fallback, counter jumping to 200 in one frame, cards popping together [11:55]. Fixes: lock canvas to 1920x1080 and position from centre (Figma frames were 1440), load fonts before frame 1, count up over about 1 s, stagger cards a few frames, slow the pan with easy ease [12:27]. Same prompt without a storyboard gave random scene order [14:01]. A change like counter 200 to 999 is one line and a few minutes to re-render [14:31].

**Use it:** the failure-to-fix list is a checklist for any code-generated animation (fonts loaded, canvas locked); numbers are his, not standards.
