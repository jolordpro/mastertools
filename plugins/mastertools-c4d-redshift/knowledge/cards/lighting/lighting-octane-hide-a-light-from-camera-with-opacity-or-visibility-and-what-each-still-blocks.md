---
id: lighting-octane-hide-a-light-from-camera-with-opacity-or-visibility-and-what-each-still-blocks
title: Hiding a light object from camera: opacity 0 also stops it blocking other lights; camera visibility off still casts shadows unless shadow visibility is off too
domain: lighting
tags: [octane, new-plastic, light visibility, opacity, camera visibility, shadow visibility, light pass id, deep-read]
applies_to: Octane for Cinema 4D (2022 video)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=J5KwV7GfbEQ, src:yt-transcripts, https://www.youtube.com/watch?v=mNcq8GD1mfI, https://help.maxon.net/r3d/cinema/en-us/Content/html/Common+Redshift+Light+Parameters.html]
feeds: [[redshift, shakedown]]
conflicts: [maxon-docs]
---
Opacity (on the light tag) hides the light object from camera while it still casts light; at zero it also no longer obstructs light from other sources [12:32][13:02]. Camera visibility off hides it but the object still blocks other lights and casts shadows; to match opacity zero also turn off shadow visibility [14:06]. Visible on diffuse or specular, and cast shadows, can be unticked per light [12:01]. Light pass ID lets you mark an object as unaffected by chosen lights and render per-light passes for post [13:02][13:34]. He rarely uses it.

**Use it:** a checklist for hidden key lights in a scene that casts a mystery shadow: check which visibility toggle was used. Redshift area lights have analogous "visible to camera" switches.
Transcript support: Light object opacity 0 so it does not show in camera. (https://www.youtube.com/watch?v=mNcq8GD1mfI [04:47])
Maxon check (2026-10-31): CORRECTION for Redshift: there is no visible-to-camera switch. Area and dome lights have a Camera contribution slider (0 to 2); set it to 0 to hide the light from camera. (https://help.maxon.net/r3d/cinema/en-us/Content/html/Common+Redshift+Light+Parameters.html)
