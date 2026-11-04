---
id: lighting-octane-ies-light-needs-real-bulb-scale-and-target-null
title: An IES profile only looks right when the light object is about the size of a real bulb; aim every light with a Target tag on a null
domain: lighting
tags: [octane, new-plastic, ies, target tag, null, spotlight, barn doors, deep-read]
applies_to: Octane for Cinema 4D (2022 video)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=J5KwV7GfbEQ, src:yt-transcripts, https://www.youtube.com/watch?v=55eY1-LlY3k]
feeds: [[redshift]]
conflicts: none
---
Turning an area light into an IES light adds an image texture in the distribution channel; load a real IES file (free from manufacturers) to get a real beam shape [14:38]. The light object's scale changes how the IES looks, so size it like a real bulb, and turn off surface brightness to compensate for the small scale and lower the power [15:08]. A spotlight profile makes a spotlight from an area light; scale it to widen the spread [15:39]. Aiming: put a null where the light should look and add a Target tag; a built-in target light aims at the object's axis point, which may be off-centre, so he prefers a null [15:39][16:11][16:41]. Octane's spotlight adds a scattering medium for a visible cone and barn doors; inner and outer cone set falloff [16:41][17:42].

**Use it:** reinforces lighting-target-tag-null-on-lights; for Redshift photometric lights use real-sized sources with IES.
Transcript support: Tanzillo suggests an IES profile on gallery back-wall lights; first time in about six years of critiques he had said it, so IES is a niche tool for wall washers (https://www.youtube.com/watch?v=55eY1-LlY3k [11:06])
