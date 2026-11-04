---
id: redshift-proxy-display-materials-and-override-settings
title: Redshift proxy object: bounding-box display, 10 percent mesh preview, material source, and what the overrides tab replaces
domain: redshift
tags: [proxy, bounding box, preview, materials from object, overrides, object id, greyscalegorilla, chad, deep-read]
applies_to: Redshift 2.x in C4D (2017 stream)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=MuVzbVhMUvI, src:yt-transcripts, https://www.youtube.com/watch?v=cR5PCFKhVJc]
feeds: [redshift, coach]
conflicts: none
---
Display: bounding box is fastest and what he leaves on; a mesh preview decimates to a set percentage (10 percent shown) only when position against ground or other objects matters [04:11-05:12].
Materials: from proxy file is the normal choice; switch to object and put a Redshift material on the proxy to change a colour at the last minute without reopening the source scene; scene mode matches by name [05:12-06:13].
Overrides: leave off and the proxy keeps whatever was baked in (object IDs, tessellation, displacement, visibility, matte, exclusions, trace sets); switch one on to set it on the proxy as a whole, for example a unique object ID for a puzzle matte [06:13-07:14]. Animated proxies get loop and ping-pong modes and detect their own frame count [07:14-07:44].

**Use it:** scene check: a proxy set to object materials with nothing assigned renders grey; the coach explains that case.
Transcript support: keep the source object in the project and re-export the proxy to iterate; old proxy files stay in the path list. (https://www.youtube.com/watch?v=cR5PCFKhVJc [03:40-05:12])
