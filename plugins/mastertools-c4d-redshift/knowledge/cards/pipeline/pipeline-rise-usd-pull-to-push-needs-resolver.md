---
id: pipeline-rise-usd-pull-to-push-needs-resolver
title: Moving to USD turned RISE's pipeline from pull to push, which forced a custom asset resolver so farm renders never switch versions mid-job
domain: pipeline
tags: [rise, andreas giesen, simon ohler, usd, asset resolver, push pipeline, houdini, solaris, deep-read]
applies_to: Houdini 18.5 / 19, USD
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=jpbMbafS9FY, src:yt-transcripts]
feeds: [pipeline plan, CHECKS]
conflicts: none
---
Rise (Andreas Giesen, Simon Ohler): the old pipeline asked artists whether to update on opening a file (pull). With USD, elements update automatically (push) [09:04].
That broke one case: a job rendering on the farm must not change asset versions mid-render, so they wrote their own asset resolver [09:35]. They also wrapped Solaris core nodes in 60+ HDAs to hide USD complexity and control usage [09:35].
Other reasons to switch: one context for look-dev to render [05:58], real packages for assets and shots, sparse layered overrides, variants, dependency tracking from a final comp back to textures [07:31], and MaterialX as a future-proof material format [08:01].

**Use it:** Pipeline design: any auto-update system needs a freeze rule for in-flight renders.
