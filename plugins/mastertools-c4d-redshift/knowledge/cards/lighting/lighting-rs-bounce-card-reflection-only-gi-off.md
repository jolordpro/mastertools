---
id: lighting-rs-bounce-card-reflection-only-gi-off
title: A bounce card with a ramp texture, invisible to camera and GI, adds only reflections; one card can also produce lots of light
domain: lighting
tags: [redshift, bounce card, ramp, visible to gi, reflections, object tag, c4d, deep-read]
applies_to: Redshift object tag, emissive card
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=BlEM9iOzqMI, src:yt-transcripts, https://www.youtube.com/watch?v=sjiuEeAp-JE]
feeds: [coach]
conflicts: none
---
Keys on the product were pure black and the reference showed blue reflections on them [21:44]. He made a light blocker plane and a bounce card, the card being a ramp from dark to the fill colour [22:21]. Primary visibility off, then Visible to GI off so it only adds reflections, not light to the scene [22:52][23:25]. Observation: a single bounce card can throw a surprising amount of light if used with care [22:52]. Background gradient: parent it under the camera so it follows camera moves [24:35].

**Use it:** for glossy hardware that reads black, add a reflection-only card before adding more lights.
Transcript support: a plain matte white card rotating off-camera gives a gem a moving reflection; render it as its own pass (https://www.youtube.com/watch?v=sjiuEeAp-JE [01:44])
