---
id: comp-nuke-soften-render-to-0-2-then-zdefocus-from-the-depth-pass-with-focal-plane-setup
title: Soften CG to about 0.2, then match plate depth of field with ZDefocus: set focal point from the footage, check Focal Plane Setup, lower size to about 0.4 and cap the maximum
domain: comp
tags: [alfie-vaughan, nuke, zdefocus, depth pass, soften, depth of field, deep-read]
applies_to: Nuke
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=fxfuhl8Q7ys, src:yt-transcripts]
feeds: [composition]
conflicts: none
---
He adds a Soften on top of every CG render; default is high so he uses about 0.2 to take off the crisp rendered look [12:58]. The depth pass (Blender mist) runs dark near to light far [13:30]. ZDefocus: put the focal point where the plate is sharp (the floor tiles), then push it slightly back for artistic licence so the headlight is crisp [14:00-14:30]. Output 'focal plane setup' shows green in focus, blue in front, red behind [14:00]. Result default was far too strong: size down to about 1 then 0.4, and lower the maximum so edges do not go wild [14:30-15:01]. Plate had shallow depth of field so the back of the car blurs and the front stays sharp.

**Use it:** Compare against comp-post-dof-zdefocus for edge halos; add the Soften-then-ZDefocus order to the CG-over-plate checklist.
