---
id: redshift-live-2026-8-depth-of-field-post-effects
title: Redshift Live (near-real-time) gained depth of field and post effects in 2026.8 but still lacks refraction and portal lights
domain: redshift
tags: [redshift live, bloom, depth of field, post effects, refraction, portal lights, arch viz, look dev]
applies_to: Redshift 2026.8
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=KoL7OAANlJ8, src:yt-transcripts, https://www.youtube.com/watch?v=74lleTzTfC4]
feeds: [redshift, coach]
conflicts: ledger
---
Live is a separate mode next to Production; it came from the architecture product and gives near-real-time updates, undersampled while moving and progressive when still [1:06:11-1:07:44]. Intended for look-dev and scene layout, not final.
2026.8 added depth of field (focus distance plus bokeh) and post effects: bloom, flares, streaks, LUTs, colour controls [1:08:16-1:09:50], plus a combined-depth style global for GI and reflection bounces [1:10:22].
Not yet: refraction, portal lights (delete them for Live) [1:05:07, 1:08:16].

Ledger disagrees: §5 says Redshift 2026.8 added refraction support (and transparent shadows) to Live, so "still lacks refraction" is wrong for 2026.8. Trust the ledger until a test settles it.

**Use it:** use Live for blocking and look-dev only; the preview picker warns that refraction and portal lights are missing there. Pairs with the existing card on Live's AOV gaps.
Transcript support: Second upload; trainer on a M3 Mac, Live stems from the Vectorworks previewer, refraction missing at 2026.8 in her words (ledger says otherwise, ledger-check stands). (https://www.youtube.com/watch?v=74lleTzTfC4 [1:05:09-1:10:50])
