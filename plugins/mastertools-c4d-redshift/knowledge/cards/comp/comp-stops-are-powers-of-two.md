---
id: comp-stops-are-powers-of-two
title: A stop is a x2 or x0.5 multiply; n stops equals multiply by 2 to the power n
domain: comp
tags: [tony lines, exposure, stops, nuke, multiply, pow, deep-read]
applies_to: Nuke, any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=ZrOiwMSGmIw, src:yt-transcripts]
feeds: [coach, motion-critique]
conflicts: none
---
Stops are relative to the current image: +1 stop is x2, +2 is x4, +3 is x8; -1 is x0.5, -2 is x0.25, -3 is x0.125 [11:00-12:34].
In Nuke a plain Multiply gives the same image as the Exposure node, which should be set to stops, not density [25:22-26:58]. The link is the expression pow(2, stops) [27:30].
Gain and Multiply on a Grade node are the same operation under two names [26:58].

**Use it:** When a supervisor says 'one stop down', apply x0.5. Write comp notes as stops, so a lighter can copy them.
