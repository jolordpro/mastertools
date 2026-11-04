---
id: redshift-object-id-integer-user-data-shader-switch-recolours-one-shader
title: Recolour one object in a shared shader: give it an object ID, read it with an integer User Data node, and let a Shader Switch drive a multiply composite
domain: redshift
tags: [object id, user data, integer, shader switch, composite, client change, recolour, greyscalegorilla, chad, deep-read]
applies_to: Redshift 2.x in C4D (2017 stream)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=MuVzbVhMUvI, src:yt-transcripts]
feeds: [lookdev, coach]
conflicts: none
---
Client says one building should be red. Instead of a new material: set Object ID 1 in that object's Redshift tag, read it with an integer User Data node (object ID), and feed the Shader Switch's selector; slot 0 is white, slot 1 is red; the switch is the blend colour of a Composite in Multiply mode over the wood so the grain stays [51:13-54:44].
Later requests (forklift red, trees green) only needed the same ID or ID 2 and a new colour in the switch [54:44-56:21]. The tag must sit on each object, not only the parent group, so he Ctrl-dragged the tag onto the tanks [56:21-56:52].
Result: still one shader, and colours editable on the fly.

**Use it:** pipeline: scene notes that say 'make X a different colour' become an ID plus a switch slot, not a duplicate material.
