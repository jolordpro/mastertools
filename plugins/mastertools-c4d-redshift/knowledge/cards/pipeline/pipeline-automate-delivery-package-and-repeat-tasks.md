---
id: pipeline-automate-delivery-package-and-repeat-tasks
title: Automate the delivery bundle: a three-hour hand-built zip became a few minutes after a two-day script
domain: pipeline
tags: [rob nederhorst, automation, delivery package, zip, excel, dpx, nuke expressions, human error, scripting, deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=qlNn8Gim3qU, src:yt-transcripts]
feeds: []
conflicts: none
---
Nederhorst's Marvel (first Thor film) vendor work: each delivery had to be a specifically named zip with a set number of files, a specifically formatted Excel sheet, and DPX or JPEG or DNxHD movies. Two manual deliveries took about 3 hours each [33:23].
He then spent a couple of days scripting it; afterward one command made the Excel, DPXs and QuickTimes, zipped them and put them in a folder, a few minutes in all [33:55].
His test for automating: a 10-second task done 300 times a day is worth cutting to 1 second [31:50]. Host adds that automation also removes late-night naming errors on passes [34:26].
He also writes Nuke expressions so a setup copied to another shot is rendering on the farm within about 5 minutes [35:00].

**Use it:** Script delivery bundles (naming, manifest sheet, encodes, zip) as one command, and flag any task a person repeats many times a day as a script candidate.
