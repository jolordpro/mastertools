---
id: redshift-metal-expose-few-sliders-in-a-controller-group
title: Wrap a complex metal in a group node that exposes only a few sliders, so client notes become one-slider changes
domain: redshift
tags: [polygon division, redshift, metal, group node, start node, controller, presets, client notes, deep-read]
applies_to: Cinema 4D 2024, Redshift
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=-lpj38Cql4c, src:yt-transcripts]
feeds: [redshift, coach]
conflicts: none
---
Pick the controls you will retouch (base roughness, scratch amount, micro-scratch amount, bump amount, corner radius), connect each to one float, and add them as inputs of a group node named controller. Mark the group as the start node so those sliders show whenever the preset is used [37:49-41:17].
Example note: the client says the surface is too soft in reflections; drop base roughness to 0.125 for a newer, shinier look, or raise it to roughen [33:25, 41:17].
Order sliders so base roughness is first [41:17].

**Use it:** supports building reusable material presets with a short control list; matches a note-driven revision loop.
