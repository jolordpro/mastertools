---
id: pipeline-rise-unversioned-asset-symlink-and-pinning
title: Reference an unversioned asset file that links to the latest version, and let a resolver pin one shot to an older version
domain: pipeline
tags: [rise, usd, asset package, symlink, pinning, asset info, version, deep-read]
applies_to: USD
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=jpbMbafS9FY, src:yt-transcripts]
feeds: [pipeline plan]
conflicts: none
---
Rise exports each asset as one package file that payloads its model and surface layers [16:38-17:10]. Shots reference an unversioned file name that is really a symlink to the newest version, e.g. version 5 [17:42].
Because the layer view cannot show which version that is, export nodes also write asset-info metadata (identifier with the real version) [18:13]. A pinning UI shows it and can switch one asset to an older export for a given shot or file, for debugging or a one-off need [18:45].
The custom resolver (first based on Rodeo FX's open-source replace resolver) ignores the symlink and maps the same name to another path [19:16]. Validators run before every publish [16:38].

**Use it:** Handoff rule: 'latest' is a pointer, pins are explicit overrides, and metadata records the real version.
