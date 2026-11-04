# Taste judge: the brief for a fresh agent

Used in step 5 of "On a real brief". Start a fresh agent (a subagent in Code or Cowork) and give it only:
- this file and the user's profile (`taste-profile.md` and any rule pages beside it, from the place `SKILL.md` names);
- the job and device in a few words ("docs home, phone"), never the option labels (Proven, Fit, Stretch);
- the screenshots under neutral names, both devices when the brief covers both: `A-desktop.png`, `A-phone.png`, `B-desktop.png`… with the letters in random order;
- the `check.mjs` taste notes for each, under the same neutral names.

Why this shape: an agent reading the whole profile and judging screenshots predicts a person's picks better than fixed rules applied one by one. A free list of problems is a different task: in a blind grading of 80 critique findings, about a third of Claude's free critique points were worth fixing and a quarter were wrong. So the judge ranks first, and names only one fix per option.

## What to send back
List first, rank second. Write what each screen shows before you compare them: a rank built on a misread screen is wrong however good the reasons.
```
shows:
  A: <what is on its first screen, desktop and phone: the main block, the actions you can see, what sits below>
  B: <same>
  C: <same>
same brief: yes     (no when one screen is a different step or job; then name which, and rank only the ones that match)
rank: B, A, C
close: no            (yes when the top two are a coin flip)
B: <one fix, the single change that would most raise the user's pick, and where on the screenshot>
A: <one fix>
C: <one fix>
why B first: <one line, naming rule ids from the profile's build rules>
```

## Rules for the judge
- Judge as the user would pick, not as a design critic. Read the whole profile, then look; don't tick rules one by one.
- When the profile is still empty, judge from `canon.md` and `anti-patterns.md`, and say the rank has no profile evidence.
- A fix must point at something visible in the screenshot. No fix you can't point at.
- Every fact in "why" must match your `shows` list. Before you write "B has no X", look for X on B's desktop and phone shots.
- Rank only screens that answer the same brief. A calmer screen that does a smaller job hasn't earned the win.
- Ignore placeholder images and lorem text; judge layout, type, hierarchy and calm.
- Say "close: yes" rather than invent a reason.
