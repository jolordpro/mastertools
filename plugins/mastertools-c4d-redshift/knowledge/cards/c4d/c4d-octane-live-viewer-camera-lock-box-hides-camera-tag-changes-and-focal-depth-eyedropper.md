---
id: c4d-octane-live-viewer-camera-lock-box-hides-camera-tag-changes-and-focal-depth-eyedropper
title: Octane (C4D): untick the camera box in the live viewer options to lock the view, but re-tick it when editing the Octane camera tag, or post and depth of field changes will not show
domain: c4d
tags: [octane, live viewer, camera lock, depth of field, thin lens, focal depth, eyedropper, deep-read]
applies_to: Octane for Cinema 4D
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=8zCqKpeF5Uc, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
3seater [05:59-07:56]. By default the live viewer follows the C4D camera, so moving the viewport moves the render. Unticking the camera checkbox in the live viewer options locks the view so the scene can be worked freely [06:22]. For depth of field, use the Thin Lens section of the Octane camera tag: the F eyedropper picks the focal depth from whatever geometry is clicked (he clicked the ring, the nearest object, ignoring lights behind), then the aperture value blurs foreground and background [06:55-07:25]. While the lock is on, changes to the camera tag (post processing, DOF) do not update in the viewer, so unlock to see them [07:25-07:56]. Captions are rough here; the exact menu path is the speaker's, check it in the plugin.

**Use it:** If an Octane camera setting seems to do nothing, check the lock box first. Pick DOF focus with the eyedropper, not by typing a distance.
