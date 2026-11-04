---
id: redshift-c4d-set-driver-expressions-drive-many-materials-from-one-colour
title: C4D Set Driver and Set Driven (Absolute) on colour fields let two master colours steer every dice material, with the driver nulls renamed for safety
domain: redshift
tags: [set driver, set driven absolute, xpresso, expressions, color driver, procedural, dice, jon jags nee, deep-read]
applies_to: C4D + Redshift (2022 upload, Jon Jags Nee)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=eKG2QSWJYYM, src:yt-transcripts]
feeds: [redshift, lookdev]
conflicts: none
---
Right-click the colour field of each dice material and choose Expressions > Set Driver, then open the master material's shader graph, right-click the Maxon Noise colour and choose Set Driven (Absolute); the dice colour jumps to the master colour [14:07-15:08]. Repeat for the second colour [15:08].
Two small Xpresso nulls appear in the object manager; he renames them (driver to tutorial dice 1 and 2) so the link is traceable if something breaks [15:08-15:40]. Changing the master colours now changes every dice; noise type and scale can be changed once and the look follows [15:40-16:41].
Match noise scale and type across all textures if a copy should look identical [16:11].

**Use it:** art-directable rig: a few master colours drive many materials in a pitch scene.
