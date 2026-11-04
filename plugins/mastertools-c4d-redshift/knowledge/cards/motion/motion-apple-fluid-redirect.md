---
id: motion-apple-fluid-redirect
title: Apple iPhone X gestures are built to be interrupted and redirected mid-motion, so thought and gesture run in parallel
domain: motion
tags: [motion-tokens, product, chan-karunamuni, gestures, interruption]
applies_to: any
status: V
confidence: high
decay: slow
read: 2026-10-30
recheck_by: 2028-10-30
sources: [https://developer.apple.com/videos/play/wwdc2018/803/, https://www.youtube.com/watch?v=gttSJA-kDmQ, src:yt-transcripts]
feeds: [studies/motion-leaders]
conflicts: none
---
Chan Karunamuni (WWDC18) says the home, multitasking and app-switch moves are one gesture space across two axes, not separate gestures. A user can change course at any point, including while an app is launching. Interfaces that cannot be redirected force the person to decide before acting, which is slower.

**Use it:** Spec transitions as interruptible by default; list which in-flight states may be redirected.
