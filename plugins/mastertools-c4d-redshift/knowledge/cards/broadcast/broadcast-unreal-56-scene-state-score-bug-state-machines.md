---
id: broadcast-unreal-56-scene-state-score-bug-state-machines
title: Scene State gives score-bug logic as separate state machines (score, down and distance, timeouts) with a diagnostic view
domain: broadcast
tags: [unreal, scene state, score bug, state machine, remote control, timeouts, deep-read]
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
Speaker is David Grownick, Epic senior product specialist and ex Fox Sports real-time graphics, so vendor view. Built for score bugs and tickers where transition logic is not enough [28:44-29:34]. Separate state machines handle score change, down-and-distance, touchdown, timeouts; a diagnostic view highlights the state you are in [29:34-30:36]. "Run event" tests a change inside the tree; a proper "push event" is what remote control will trigger [30:36-31:07]. Timeout events kill the lights one by one; a touchdown set to 6 plays the timed celebration then rolls the score and picks up team colour [31:07-32:08]. Grownick offers a sanitised sample.
His rule: timing is everything; you must be able to test constantly without breaking other states.

**Use it:** Model any scorebug spec as separate event machines with a way to dry-run each event.
