---
id: redshift-proxy-swap-in-cloner-updates-every-shot-like-xref
title: Re-export the asset as a new proxy file and swap it in the cloner: every scene using it updates, like an xref
domain: redshift
tags: [proxy, xref, asset update, client change, cloner, greyscalegorilla, chad, deep-read]
applies_to: Redshift 2.x in C4D (2017 stream)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=MuVzbVhMUvI, src:yt-transcripts]
feeds: [pipeline, coach]
conflicts: none
---
Client asks for grey mechs instead of yellow. He changed the shader in the source scene, exported a second proxy under a new name (without Remove or Add to Scene), then in the army scene loaded the new file into the cloner's proxy slot and the whole crowd changed at once [23:28-26:39].
His reasoning: with ten shots using the same mech, update the asset once and point to it, instead of pasting a material into every scene. Alternative he calls boring: switch the proxy to object materials and paste a shader in each file.

**Use it:** pipeline: version proxy files by name and update the reference; keep the previous proxy so an earlier shot can still be rendered.
