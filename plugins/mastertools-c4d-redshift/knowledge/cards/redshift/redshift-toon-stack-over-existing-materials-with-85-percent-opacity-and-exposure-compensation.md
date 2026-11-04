---
id: redshift-toon-stack-over-existing-materials-with-85-percent-opacity-and-exposure-compensation
title: Redshift Toon quick look: stack a Toon material over existing materials at about 85% opacity, raise camera exposure to compensate, and mix with photoreal
domain: redshift
tags: [redshift toon, material stacking, opacity, camera exposure, material override, c4d, effectatron, ledger-check, deep-read]
applies_to: Cinema 4D + Redshift 3.6 (video April 2024)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=ZCojy8uF3FY, src:yt-transcripts]
feeds: [redshift, elevate]
conflicts: none
---
Derek Kirk (Effectatron). Create a Toon material, take its base colour fully down, set geometry opacity to about 85 percent, then apply it to all geometry (not lights or camera) so it sits on top of the existing materials rather than replacing each one [03:37-04:41]. Toon renders darker, so raise the camera's optical exposure to compensate and keep the lighting balance [05:12-06:14]. Photoreal effects such as fog and depth of field still work; the speaker likes that toon can be mixed with photoreal [03:04].
Material Override in render settings (Effect) with one toon material gives an instant flat toon blockout for concept swipes; uncheck to go back [08:50-10:25].
Fix: stacked toon grays out transmissive parts such as glass. Split the glass polygons into their own object (select by the glass material tag, Split) and delete the toon from that object [11:26-14:30].
His note: KitBash assets did not work with Redshift 3.6 at the time; vendor said fix was coming (decay).
Ledger: camera-exposure compensation is a speaker choice; do not treat it as a general light-balance rule.

**Use it:** for a quick toon look-test on an existing scene, use the stack plus camera exposure lift, not a per-material rebuild; split glass first.
