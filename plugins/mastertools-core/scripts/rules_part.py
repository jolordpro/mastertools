#!/usr/bin/env python3
"""Print one part of a rules file, for a SessionStart hook.

Claude Code keeps at most 10,000 characters of each hook command's output. Past
that, the session gets only a file path and a 2,000-character preview, and most
of the rules never reach it. So each rules file is cut at its "## " headings into
parts under LIMIT characters, and hooks.json runs one command per part.

Usage:
  rules_part.py <rules file> <part number>   print that part (nothing if it has none)
  rules_part.py <rules file> --count         print how many parts the file needs

Parts after the first open with a "(part N)" line, so they read on their own.
Never fails the session: a missing file prints nothing and exits 0.
"""
import sys
from pathlib import Path

LIMIT = 9000  # under the 10,000 cap, with room for the "(part N)" line


def parts(text):
    """Split at "## " headings into chunks under LIMIT characters, in order."""
    sections, cur = [], []
    for line in text.splitlines(keepends=True):
        if line.startswith("## ") and cur:
            sections.append("".join(cur))
            cur = []
        cur.append(line)
    if cur:
        sections.append("".join(cur))
    out, chunk = [], ""
    for s in sections:
        if chunk and len(chunk) + len(s) > LIMIT:
            out.append(chunk)
            chunk = ""
        chunk += s
    if chunk:
        out.append(chunk)
    return out


def title(text):
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "Rules"


def render(text, n):
    """Part n (1-based) as printed, or "" when the file has no such part."""
    ps = parts(text)
    if n < 1 or n > len(ps):
        return ""
    if n == 1:
        return ps[0]
    return f"# {title(text)} (part {n})\n\n" + ps[n - 1]


def main(argv):
    if len(argv) != 3:
        return 0
    path = Path(argv[1])
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return 0
    if argv[2] == "--count":
        print(len(parts(text)))
        return 0
    try:
        n = int(argv[2])
    except ValueError:
        return 0
    out = render(text, n)
    if out:
        out = out if out.endswith("\n") else out + "\n"
        sys.stdout.buffer.write(out.encode("utf-8"))  # any locale, never an encoding error
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
