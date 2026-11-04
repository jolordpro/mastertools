---
id: c4d-light-inside-a-cloner-does-nothing-check-render-instances
title: "Beeple's SIGGRAPH slip: lights inside a Cinema 4D Cloner did not change the scene until Render Instances was checked on the Cloner"
domain: c4d
tags: [beeple, cloner, render instances, light, troubleshooting, siggraph 2017, octane, deep-read, polish]
applies_to: Cinema 4D (2017, Octane)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=f8N2IryTFJc, src:yt-transcripts, src:polish-roster]
feeds: [CHECKS, shakedown]
conflicts: none
---
While live-building a tunnel at the Maxon booth, Beeple put a light inside a Cloner and changing the light did nothing; the scene stayed dark [02:51-03:54]. A neighbour spotted the cause: he had duplicated another Cloner that already had Render Instances set, and the audience called the fix out.
Takeaway from the stumble: when a light in a Cloner has no visible effect, check the Cloner's Render Instances setting.
He was using Octane at the time; whether the same applies to Redshift's instance handling was not discussed, so verify before relying on it.

**Use it:** The scene check could flag a Cloner with Render Instances on that contains lights or other items that must render individually.
