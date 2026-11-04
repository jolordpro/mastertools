# Defaults

Used when a profile leaves a field or block out. Same format as a profile (see profiles/EXAMPLE.md).

handover: Hand over each finished file as its full path, in its own code block.
aside_log: List each rule set aside in Next steps so it can be reversed.
check_skills: With the plan-review module installed, run challenger on plans before building and at gates, and shakedown on a finished build before calling it ready.
main_model: One model for the whole thread: Opus where the plan includes it, else the strongest one available.
effort_line: Effort is how hard Claude thinks before it answers, set per session from low to xhigh. Plan at high, run the challenger pass (the plan-review module's pressure test) at xhigh, build at medium, check at high. A session can't change its own effort, so remind the user when the phase changes.
plan_agent: Skip the built-in Plan agent: it starts without this conversation, so its plans miss what was already agreed.
ui_floor: , within the design-taste quality floor when the UI design module is installed

## Block: privacy
~~~
## Private data
- **Private stays private.** Anything the user calls private stays in its own project folder: never in shared rules, plugins, the knowledge base or anything public.

~~~
