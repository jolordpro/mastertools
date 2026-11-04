---
id: broadcast-unreal-56-data-link-pulls-stats-from-sheet
title: Data Link maps fields to a Google Sheet, HTTP request or data table so big stat tables are not typed by hand
domain: broadcast
tags: [unreal, data link, google sheet, stats, remote control, field id, deep-read]
applies_to: Unreal Engine 5.5-5.6 Motion Design
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=QWT8IAUfWSk, src:yt-transcripts]
feeds: []
conflicts: none
---
Speaker is David Grownick, Epic senior product specialist and ex Fox Sports real-time graphics, so vendor view. Problem: a large stats table typed by an operator is slow and risks mismatches [33:11]. Link the graphic's rows to sheet columns (team name, wins, losses, win percentage) [33:42-34:13]. Works for archival or a few-minutes-old stats; true live push is a later goal [34:13-34:45]. Remote control still has to be set up first and a data-table actor maps field IDs (E101, E102...) [34:45-35:46]; sources can also be data tables or HTTP [35:46].

**Use it:** For sports tables, source the numbers by link and keep manual override as a fallback.
