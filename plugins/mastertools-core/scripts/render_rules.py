#!/usr/bin/env python3
"""Render one core rule template with a person's profile, for the start hook.

Usage:
  render_rules.py <template.md> [--profile <profile.md>] [--plugin <name>] [--platform darwin|linux|...]
                  [--part N | --count] [--max-chars N]

Prints the rendered text. Claude Code cuts any hook output over 10,000 characters to a
2,000-character preview, so the start hook prints one part per command: --part N cuts the
render at its "## " headings into parts under PART_LIMIT characters and prints part N (nothing
when there is no such part); --count prints how many parts it needs. Parts after the first open
with a "# <title> (part N)" line. Exits 1 when what it prints is over --max-chars (default 9900).

Template syntax:
  {{name}} {{name's}} {{he}} {{him}} {{his}} {{plugin}} {{<field>}}
      Replaced by the profile value. Capitalised at the start of a sentence.
      A line holding a field token whose value is empty is dropped.
  {{s:sees|see}} the first word for he or she, the second for they.
  {{<field>+}}   value plus a space, or nothing.
  {{+<field>}}   a space plus value, or nothing.
  {{block:<id>}} alone on a line: the profile's block <id>, else the default block, else the line is dropped.
  {{#mac}} ... {{/mac}} on their own lines: the lines between are kept on macOS only.

Profile format: "key: value" lines before the first "## " heading, then blocks:
  ## Block: <id>
  ~~~
  <text, may hold tokens>
  ~~~
Defaults come from core/rules/DEFAULTS.md (same format); the profile overrides them.
Never fails the session on a missing profile: the defaults speak of "the user".
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rules_part import LIMIT as PART_LIMIT, parts, render as part  # noqa: E402  (the live hook's own printer, unchanged)

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULTS = os.path.join(HERE, "..", "rules", "DEFAULTS.md")
PRONOUNS = {"he": ("he", "him", "his"), "she": ("she", "her", "her"), "they": ("they", "them", "their")}


def parse_profile(path):
    fields, blocks = {}, {}
    if not path or not os.path.isfile(path):
        return fields, blocks
    lines = open(path, encoding="utf-8").read().splitlines()
    i = 0
    while i < len(lines) and not lines[i].startswith("## "):
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", lines[i])
        if m:
            fields[m.group(1).lower()] = m.group(2).strip()
        i += 1
    while i < len(lines):
        m = re.match(r"^## Block:\s*([A-Za-z_]+)\s*$", lines[i])
        i += 1
        if not m:
            continue
        while i < len(lines) and lines[i].strip() != "~~~":
            i += 1
        i += 1
        body = []
        while i < len(lines) and lines[i].strip() != "~~~":
            body.append(lines[i])
            i += 1
        i += 1
        blocks[m.group(1).lower()] = "\n".join(body)
    return fields, blocks


def values(fields, plugin):
    v = dict(fields)
    name = v.get("name") or "the user"
    subj, obj, poss = PRONOUNS["they"]
    p = (v.get("pronouns") or "").lower().split("/")
    if p and p[0] in PRONOUNS:
        subj, obj, poss = PRONOUNS[p[0]]
        if len(p) == 3:
            subj, obj, poss = p
    v.update({"name": name, "name's": name + "'s", "he": subj, "him": obj, "his": poss})
    v["plugin"] = plugin or v.get("plugin") or "mastertools-core"
    return v


SENTENCE_START = re.compile(r"(^\s*(?:[-*] )?(?:\*\*)?|[.!?]\s+|[.!?]\*\*\s+)$")


def fill(line, v):
    # {{s:<singular>|<plural>}}: verb agreement with the pronoun (he sees, they see).
    line = re.sub(r"\{\{s:([^|}]*)\|([^}]*)\}\}", lambda m: m.group(2) if v["he"] == "they" else m.group(1), line)
    out, pos = [], 0
    dropped = False
    for m in re.finditer(r"\{\{(\+?)([A-Za-z_']+)(\+?)\}\}", line):
        pre, key, post = m.group(1), m.group(2).lower(), m.group(3)
        val = v.get(key, "")
        out.append(line[pos:m.start()])
        if not val and not pre and not post:
            dropped = True
        if val and SENTENCE_START.search("".join(out)) and not pre:
            val = val[0].upper() + val[1:]
        out.append((" " if pre and val else "") + val + (" " if post and val else ""))
        pos = m.end()
    out.append(line[pos:])
    return None if dropped else "".join(out)


def render_lines(text, v, blocks, platform):
    # split("\n"), not splitlines(): a block's trailing blank line is kept, so a dropped block leaves no extra gap.
    result, mac = [], None
    for line in text.split("\n"):
        s = line.strip()
        if s == "{{#mac}}":
            mac = platform == "darwin"
            continue
        if s == "{{/mac}}":
            mac = None
            continue
        if mac is False:
            continue
        m = re.match(r"^\{\{block:([A-Za-z_]+)\}\}$", s)
        if m:
            body = blocks.get(m.group(1).lower())
            if body:
                result.extend(render_lines(body, v, blocks, platform))
            continue
        filled = fill(line, v)
        if filled is not None:
            result.append(filled)
    return result


def render(text, v, blocks, platform):
    return "\n".join(render_lines(text, v, blocks, platform))


def main(argv):
    args = {"--profile": None, "--plugin": None, "--platform": sys.platform, "--max-chars": "9900", "--part": None}
    pos, count = [], False
    it = iter(argv)
    for a in it:
        if a == "--count":
            count = True
        elif a in args:
            args[a] = next(it, None)
        else:
            pos.append(a)
    if len(pos) != 1:
        print(__doc__, file=sys.stderr)
        return 2
    dfields, dblocks = parse_profile(DEFAULTS)
    pfields, pblocks = parse_profile(args["--profile"])
    fields = {**dfields, **{k: x for k, x in pfields.items()}}
    blocks = {**dblocks, **pblocks}
    v = values(fields, args["--plugin"])
    out = render(open(pos[0], encoding="utf-8").read(), v, blocks, args["--platform"])
    if count:
        print(len(parts(out)))
        return 0
    if args["--part"]:
        out = part(out, int(args["--part"]))
        if out and not out.endswith("\n"):
            out += "\n"
    sys.stdout.buffer.write(out.encode("utf-8"))  # any locale, never an encoding error
    if len(out) > int(args["--max-chars"]):
        print(f"render_rules: {os.path.basename(pos[0])} is {len(out)} chars, over {args['--max-chars']}; "
              "Claude Code would cut it to a preview.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
