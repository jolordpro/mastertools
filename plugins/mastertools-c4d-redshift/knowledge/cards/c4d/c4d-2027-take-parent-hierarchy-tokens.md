---
id: c4d-2027-take-parent-hierarchy-tokens
title: C4D 2027 adds Take Parent (with a number) and Take Hierarchy tokens so nested take variants get distinct file names
domain: c4d
tags: [takes, tokens, take parent, take hierarchy, output path, variants]
applies_to: Cinema 4D 2027.0
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=FmaKhqSITFQ, src:yt-transcripts]
feeds: [CHECKS, coach]
conflicts: none
---
Before there was only the current take name token. Now take parent (parent three picks the third ancestor) and take hierarchy (the full chain) are available [1:05:19-1:05:50].
In a demo, nested takes for product combinations rendered with names that followed the hierarchy [1:06:23].

**Use it:** an output-path check should accept these tokens as a safeguard against takes overwriting each other.
