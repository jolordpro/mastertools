---
id: c4d-beeple-scattered-heads-were-render-instances-and-a-bigger-scatter-froze-the-live-demo
title: Beeple's scene of about 300,000 heads used render instances; adding a bigger scatter froze Cinema 4D, and autosave was set to five minutes
domain: c4d
tags: [beeple, mike-winkelmann, instances, scatter, crash, autosave, cinema-4d, octane, deep-read]
applies_to: Cinema 4D + Octane (SIGGRAPH 2019 stage demo)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=DVJOZzRzlGg, src:yt-transcripts]
feeds: [[coach, shakedown]]
conflicts: none
---
In the SIGGRAPH 2019 live demo the head-field had about 300,000 polygons per head object (his stated size when asked "how big is this") [12:14]. When asked if he used instances, he said all of them were true render instances [18:42]. Scattering more heads on the ground made the viewport unresponsive; the helpers told him to hit Escape repeatedly and they recovered it [18:42][19:17]. His autosave interval was about five minutes, which risked losing the whole session, and the room told him to save by hand before big scatter changes [19:17][19:51]. Whisper transcript, numbers heard once: "300,000" may be a count, not polygons.

**Use it:** shakedown line for heavy scatter scenes: confirm render instances, set autosave short, and save before raising a scatter count. Transfers directly to C4D + Redshift scatter in stadium crowds.
