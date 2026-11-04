# Master Tools

Claude doesn't know the craft. A good setup takes months.

Master Tools is that setup, already built: one core of working rules for creative work, plus modules that add the craft. It runs in Claude Code.

The core is always in. Work gets a check before it counts as done. A profile sets a name, pronouns, how technical the answers get, and the words Claude never uses. Model routing, a build method for longer jobs and safety hooks come with it.

## Install

Two lines in a terminal install the core:

```bash
claude plugin marketplace add jolordpro/mastertools
claude plugin install mastertools-core@mastertools-stable
```

Each module is one more line, with its name from the list below:

```bash
claude plugin install mastertools-writing@mastertools-stable
```

A new Claude Code session picks up the setup.

## Modules

- **After Effects** · `mastertools-after-effects` · Scripts, expressions or panels for After Effects, even small ones.
- **Cinema 4D, Redshift and shot polish** · `mastertools-c4d-redshift` · Cinema 4D and Redshift rendering, polish notes on 3D and After Effects shots, and plans for comping CG into live footage.
- **Career for motion designers** · `mastertools-career` · A senior-level job hunt or portfolio audit as a motion designer.
- **Claude API developer** · `mastertools-developer` · Prompt caching checks for apps built on the Claude API.
- **Frames and layout** · `mastertools-frames` · Notes on framing, layout and crops.
- **Leadership** · `mastertools-leadership` · Leading other leaders.
- **Time log** · `mastertools-ledgers` · A running log of the time Claude saves, with a timing block in each script Claude writes.
- **Motion craft** · `mastertools-motion-craft` · Designing or reviewing motion.
- **Photoshop and Adobe plugins** · `mastertools-photoshop-uxp` · Photoshop scripts, and UXP plugins for Photoshop, InDesign and Premiere Pro.
- **Plan and review** · `mastertools-plan-review` · Plans pressure-tested, facts researched, and work audited before it counts as done. Suggested alongside the core.
- **Threads and handoff** · `mastertools-threads` · Long projects that run across sessions or accounts.
- **UI design** · `mastertools-ui-design` · App and web screens, judged against a taste profile that grows from picks over time.
- **Writing** · `mastertools-writing` · Copy that other people read.

## Profile

`profile.md` holds the few facts the core rules read at the start of every session: a name, pronouns, a tech level, banned words, and how finished files get handed over. Every field is optional. A field left out uses the default, and with no file at all the rules speak of "the user".

It lives at `~/.claude/profile.md`, in the hidden .claude folder at the top of the home folder. The core plugin's Profile setting can point to a different file. A short one:

```
name: Sam
pronouns: they/them/their
tech_level: Sam writes code daily; skip the basics.
banned_words: deep dive, circle back
```

## Licence

MIT. Free to use, change and share, as long as the copyright line travels with every copy.

Copyright (c) 2026 Jo Lord

Full text in [LICENSE](LICENSE).
