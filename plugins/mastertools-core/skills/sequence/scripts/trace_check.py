#!/usr/bin/env python3
"""Trace check for a sequence build.

Maps every success measure in BRIEF.md (lines like "- **M1.** When ...") to the
plan phases whose "Delivers:" line names it, and every plan phase back to a
measure or "enabling". Prints a table and exits 1 on any orphan, so the check
can fail.

Usage:
  trace_check.py <buildplan dir>               full trace (BRIEF.md + PLAN.md)
  trace_check.py <buildplan dir> --brief-only  measures only: form and count

Exit codes: 0 pass · 1 orphan or malformed measure · 2 missing file.
"""
import re
import sys
from pathlib import Path

MEASURE = re.compile(r"^\s*[-*]\s*\**\s*M(\d+)\b\**[.:]?\**\s*(.*)$")
FORM = (re.compile(r"\bwhen\b", re.I), re.compile(r"\bchecked by\b", re.I), re.compile(r"\bpassing when\b", re.I))
MIN_MEASURES = 3


def read(path):
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        print(f"trace_check: can't read {path}", file=sys.stderr)
        sys.exit(2)


def measures(brief):
    found = {}
    for line in brief.splitlines():
        m = MEASURE.match(line)
        if m:
            found[f"M{int(m.group(1))}"] = m.group(2).strip()
    return found


def phases(plan):
    """Return [(heading, delivers or None)] for ### headings in the Phases section."""
    lines = plan.splitlines()
    start = next((i for i, l in enumerate(lines) if re.match(r"^##\s+Phases\b", l, re.I)), None)
    if start is not None:
        end = next((i for i in range(start + 1, len(lines)) if re.match(r"^##\s", lines[i])), len(lines))
        lines = lines[start + 1:end]
    out, current, delivers = [], None, None
    for line in lines:
        h = re.match(r"^###\s+(.+?)\s*$", line)
        if h:
            if current is not None:
                out.append((current, delivers))
            current, delivers = h.group(1), None
            continue
        d = re.match(r"^\s*[-*]?\s*\**Delivers:?\**:?\s*(.*)$", line, re.I)
        if d and current is not None:
            delivers = d.group(1).strip()
    if current is not None:
        out.append((current, delivers))
    return out


def main(argv):
    if len(argv) < 2:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    root = Path(argv[1])
    brief = measures(read(root / "BRIEF.md"))
    problems = []

    if len(brief) < MIN_MEASURES:
        problems.append(f"BRIEF.md has {len(brief)} numbered measures; at least {MIN_MEASURES} needed")
    for mid, text in brief.items():
        missing = [p.pattern.replace(r"\b", "") for p in FORM if not p.search(text)]
        if missing:
            problems.append(f"{mid} is not in the When / Checked by form (missing: {', '.join(missing)})")

    if "--brief-only" not in argv:
        plan = phases(read(root / "PLAN.md"))
        if not plan:
            problems.append("PLAN.md has no ### phases")
        served = {mid: [] for mid in brief}
        print("| Phase | Delivers |\n|---|---|")
        for name, delivers in plan:
            print(f"| {name} | {delivers or 'NOTHING'} |")
            if not delivers:
                problems.append(f"phase '{name}' has no Delivers line (name a measure or 'enabling')")
                continue
            if re.search(r"\benabling\b", delivers, re.I):
                continue
            ids = [f"M{int(n)}" for n in re.findall(r"\bM(\d+)\b", delivers)]
            if not ids:
                problems.append(f"phase '{name}' delivers '{delivers}', which names no measure")
            for mid in ids:
                if mid in served:
                    served[mid].append(name)
                else:
                    problems.append(f"phase '{name}' names {mid}, which BRIEF.md doesn't have")
        print("\n| Measure | Delivered by |\n|---|---|")
        for mid, names in served.items():
            print(f"| {mid} | {', '.join(names) if names else 'ORPHAN'} |")
            if not names:
                problems.append(f"{mid} is delivered by no phase")

    if problems:
        print("\nTrace check: FAIL")
        for p in problems:
            print(f"- {p}")
        return 1
    print(f"\nTrace check: PASS ({len(brief)} measures)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
