---
id: lighting-product-one-area-light-per-highlight-and-light-pass-ids
title: Build a product-shot rim look with one small area light per highlight, and exclude or isolate objects with light pass IDs
domain: lighting
tags: [octane, cinema 4d, product render, area light, light linking, light pass id, iphone, nikita kapustin, deep-read]
applies_to: Cinema 4D + Octane
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=gMs_iu3cMoY, src:yt-transcripts, https://www.youtube.com/watch?v=8zCqKpeF5Uc]
feeds: [elevate]
conflicts: none
---
Kapustin's iPhone product render [08:30-09:37]: every light has one job (one edge highlight, one back edge, one broad back wash), all aimed at a null so the aim never needs redoing; the camera-visibility of the light shapes is switched off. He keeps each light at the minimum power that shows, because over-bright lights give hot white pixels and fireflies later [12:15]. Keep a gap of dark between highlights and do not light the whole phone, so the focus stays on the glass and lenses [14:19]. To keep a light off an object, give the light a pass ID, then untick that ID in the object's tag (lenses here) [21:39-22:43]; to light only chosen objects, tick light-link invert and give those objects the ID [27:27-27:57]. A lens-only light was made a disk shape (round reflection in glass) with its own target null [23:46-24:48]. A light can be blocked by another light's geometry; shrink it or move it [38:30].

**Use it:** Use the one-job-per-light list and the exclude/invert pass ID trick as a checklist for hero product frames in Octane or Redshift light linking.
Transcript support: Light Pass ID on the light tag plus the Light Pass Mark tick in the object tag: an unticked number means that light does not touch the object. Kapustin video mNcq8GD1mfI [09:55] uses ID 3 to keep a light off the ground. (https://www.youtube.com/watch?v=8zCqKpeF5Uc [00:34-02:38])
