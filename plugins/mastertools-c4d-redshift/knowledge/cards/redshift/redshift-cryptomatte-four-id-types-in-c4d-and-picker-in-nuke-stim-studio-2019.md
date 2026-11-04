---
id: redshift-cryptomatte-four-id-types-in-c4d-and-picker-in-nuke-stim-studio-2019
title: Redshift Cryptomatte in C4D offers object name, material name, Redshift object ID and user attribute; in Nuke the picker adds or removes pieces with control-click
domain: redshift
tags: [cryptomatte, aov manager, object id, material name, user attribute, nuke, stim studio, mattes, deep-read]
applies_to: C4D + Redshift, Nuke (2019 upload)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=Q3ceb1RsseE, src:yt-transcripts]
feeds: [redshift, comp]
conflicts: none
---
Add the Cryptomatte AOV in the Redshift AOV manager and pick an ID type [00:02-00:33]. Redshift writes the beauty plus a separate Cryptomatte EXR; Nuke needs the Cryptomatte gizmo from GitHub, connected to that EXR [01:10-02:46].
Object name gives one matte per object; material name one per material but a background recolour will not fix GI or reflections that already carry the colour [04:22-05:59]. Object ID needs a Redshift object tag with a number per object, and objects sharing a number merge into one matte [06:33-08:12].
User attribute: type a name in the AOV (he used the docs' example 'mate'), add a string user data with that same name to chosen objects, and only those become one matte [08:44-10:54].
In Nuke: picker add with control-click, pick-remove to subtract, output alpha as mask for a grade or hue shift [02:46-04:22, 08:12].

**Use it:** the coach picks the ID type by question: per object, per material, hand-picked groups (object ID), or free-form groups (user data).
