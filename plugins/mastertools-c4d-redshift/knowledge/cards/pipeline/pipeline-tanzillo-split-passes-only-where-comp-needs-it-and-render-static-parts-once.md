---
id: pipeline-tanzillo-split-passes-only-where-comp-needs-it-and-render-static-parts-once
title: Do not over-split passes; split only what comp will adjust, and render a static background once, starting at the first frame that changes
domain: pipeline
tags: [mike-tanzillo, critique, passes, aovs, render time, static background, farm, deep-read, lighting-critique]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=sCDCs5At8uY, src:yt-transcripts]
feeds: [coach, estimator]
conflicts: none
---
Mike Tanzillo sCDCs5At8uY [05:23-06:57]: with a locked camera, render the long environment alone (perhaps on a farm); other renders are short. Break out animated elements, and the background can start at the first frame where anything changes (for example when a door opens). He used to split everything for comp flexibility but AOVs now make it easy and complexity explodes; he keeps things baked together unless a shadow or element needs a tweak, accepting longer renders.

**Use it:** Plan passes from the notes expected in comp, not from what can be separated.
