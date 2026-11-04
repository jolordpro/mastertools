---
id: pipeline-same-look-across-engines-test
title: Test whether one look can render indistinguishably across several renderers and engines before committing to a pipeline
domain: pipeline
tags: [[nora shramek, riot, unity, unreal, maya, consistency, look unification, arcane], deep-read]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=r2PXd6l7kBg, src:yt-transcripts]
feeds: [lookdev]
conflicts: none
---
Nora Shramek's Riot R&D team (herself, a materials tech artist, a senior character artist) was asked to unify the look across games and make real-time resemble Arcane [16:33-17:34]. They rendered the same asset in Unity, Unreal, Maya and an engine with no lighting and tried to make all indistinguishable. Older League art was hand-painted, with lighting baked into flat diffuse, which was slow [16:02].

**Use it:** same test applies to matching Redshift and AE or live-engine versions of one graphic: pick a reference frame and measure difference between outputs.
