---
id: lighting-calahan-path-tracing-gives-bounce-for-free-and-new-tools-force-trade-offs
title: "Sharon Calahan: switching to a path tracer gives bounce light for free, but each tool upgrade means rewriting or abandoning old features"
domain: lighting
tags: [sharon-calahan, pixar, path-tracing, tools, polish, whisper, deep-read]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=JR6cmASjuuI, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
The biggest recent change for lighting: path-trace renderer means you get indirect bounce without adding another light as before, and you can still tweak it [13:14-13:46].
Each tool upgrade (water, cloth sims) brings compromises: new advances can drop old features you relied on, so each film decides what to exploit, rewrite or give up [13:46-14:23].

**Use it:** When moving engine or version, list the old features relied on and decide what to rebuild before the show starts.
