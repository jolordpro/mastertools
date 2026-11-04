---
id: redshift-camera-tag-bokeh-override-image-and-f-stop
title: Redshift camera tag bokeh: turn on Override and Enable, pick an image, and keep the f-stop from going so low the bokeh won't clean up
domain: redshift
tags: [redshift, bokeh, camera-tag, f-stop, setup, polish, greyscalegorilla, deep-read]
applies_to: C4D + Redshift (2022 UI)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=aWkfAAJgiJ0, src:yt-transcripts, src:polish-roster]
feeds: [redshift, CHECKS]
conflicts: none
---
Steps: add a Redshift camera tag, open its Bokeh tab, switch on Override and Enable; focus distance and circle of confusion derive from the C4D camera [01:34]. Set f-stop on the camera's Physical tab. At f/1 the bokeh is huge and will never clean up in Redshift; f/11 gives a small shape; f/4.5 shows the map shape clearly [01:49-03:37]. Turn on 'use bokeh image' and choose the map, or drive it with an HDRI link tag for fast swapping [02:36-03:37]. Demo lens: about 200 mm.

**Use it:** Reference setup for lens presets: derive focus from the camera, pick f/4.5 to f/8 for visible but cleanable bokeh.
