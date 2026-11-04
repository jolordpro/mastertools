---
id: education-path-tracing-corridor-and-sample-ladder-teaching-pattern
title: Teaching pattern: explain noise with a corridor (hard shadow vs gradient) and a 1, 5, 30 sample ladder on the same frame
domain: education
tags: [computerphile, path tracing, indirect light, samples, depth, noise, teaching pattern, deep-read]
applies_to: any
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=3OKj0SQ_UTw, src:yt-transcripts]
feeds: [[coach]]
conflicts: none
---
Computerphile (university lecturer, simple custom path tracer). Without indirect light, every occluded point gets one flat ambient value (he uses 10%), so a corridor shows a hard shadow edge; with indirect rays the corridor falls off as a gradient (his toy numbers: 60% lit near, 20% further down) [09:25-13:33]. Each indirect sample picks a random direction; averaging N of them is the Monte Carlo estimate, so one sample gives a single wall colour, which is wrong [15:37-16:39]. The ladder at the same depth 3: 1 sample is blotchy, 5 is better but still grainy and coloured, 30 irons most noise out, and a clean frame took hours to render [17:10-18:12]. Contribution per extra bounce shrinks fast, by depth 5 each ray adds little but still adds the soft shade [07:52-08:23]. Rays near the surface edge contribute less than rays near the normal [14:36].

**Use it:** Coach explanation for "why more samples, not more depth": noise is under-sampling of directions; depth only adds energy that is already small. Pair with the Redshift trace-depth card.
