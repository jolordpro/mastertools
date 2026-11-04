#!/usr/bin/env python3
"""warm_paths.py - who do you already know at each target company?

Usage:
    python3 warm_paths.py Connections.csv targets.txt [--format markdown|csv|json]
        [--since YYYY-MM-DD] [--top 5] [--include-email]

Connections.csv is LinkedIn's data export (the "Notes:" lines above the header
are skipped automatically). targets.txt has one company per line, with optional
aliases after "|" (Meta|Facebook|Instagram) and optional "# comment" lines.
Emails are hidden unless you pass --include-email. Python 3.8+, stdlib only.
"""
import argparse
import csv
import difflib
import json
import re
import sys
from datetime import datetime

FUZZY_CUTOFF = 0.9  # heuristic: close enough to flag for a human check, never trusted as a match
# Trailing words dropped when comparing company names. "labs" and "ai" are NOT here on purpose:
# they can be part of the name itself (use an alias for "Scale AI" vs "Scale").
SUFFIXES = {"inc", "llc", "ltd", "limited", "corp", "corporation", "co", "company", "plc", "gmbh",
            "platforms", "technologies", "technology"}

# Tag order here is the order patterns are tried; RANK is the order paths are ranked.
TAG_PATTERNS = [
    ("design_leader", r"design\w*\s+(manager|director|lead|head)|head of (\w+\s+)?design|creative director"
                      r"|(vp|vice president)\b.*design|director,? (of )?design|manager,? design|design lead"),
    ("recruiter", r"recruit|talent|sourcer|people partner"),
    ("eng_manager", r"engineering manager|director of engineering|director,? engineering"),
    ("pm", r"product manager"),
    ("designer", r"designer|motion|animator|art director|brand"),
]
RANK = ["design_leader", "recruiter", "designer", "eng_manager", "pm", "other"]


def tag_position(position):
    for tag, pattern in TAG_PATTERNS:
        if re.search(pattern, position or "", re.I):
            return tag
    return "other"


def normalize(name):
    words = re.sub(r"[^\w\s]", " ", (name or "").lower().replace("&", " and ")).split()
    if words and words[0] == "the":
        words = words[1:]
    while len(words) > 1 and words[-1] in SUFFIXES:
        words.pop()
    return " ".join(words)


def parse_date(text):
    for fmt in ("%d %b %Y", "%Y-%m-%d"):
        try:
            return datetime.strptime((text or "").strip(), fmt).date()
        except ValueError:
            pass
    return None


def load_connections(path):
    """Find the real header row (after any Notes: preamble) and return connection dicts."""
    with open(path, newline="", encoding="utf-8-sig") as fh:
        table = list(csv.reader(fh))
    for i, row in enumerate(table):
        cells = [c.strip().lower() for c in row]
        if "first name" in cells and "company" in cells:
            header = cells
            break
    else:
        raise SystemExit("error: could not find a header row with 'First Name' and 'Company'.")
    out = []
    for row in table[i + 1:]:
        if not any(c.strip() for c in row):
            continue
        rec = {h: (row[j].strip() if j < len(row) else "") for j, h in enumerate(header)}
        position = rec.get("position", "")
        out.append({
            "name": ("%s %s" % (rec.get("first name", ""), rec.get("last name", ""))).strip(),
            "company": rec.get("company", ""), "position": position, "tag": tag_position(position),
            "connected_on": parse_date(rec.get("connected on", "")), "url": rec.get("url", ""),
            "email": rec.get("email address", ""),
        })
    return out


def load_targets(path):
    targets = []
    with open(path, encoding="utf-8-sig") as fh:
        for line in fh:
            line = line.strip()
            if line and not line.startswith("#"):
                names = [n.strip() for n in line.split("|") if n.strip()]
                targets.append({"company": names[0], "names": names})
    return targets


def sort_key(c):
    return (RANK.index(c["tag"]), -(c["connected_on"].toordinal() if c["connected_on"] else 0))


def match(connections, targets):
    """Exact (normalized name or alias) matches first, then fuzzy 'possible' matches."""
    lookup = {}
    for t in targets:
        t["exact"], t["possible"] = [], []
        for n in t["names"]:
            lookup.setdefault(normalize(n), t)
    for c in connections:
        norm = normalize(c["company"])
        if not norm:
            continue
        if norm in lookup:
            lookup[norm]["exact"].append(c)
            continue
        close = difflib.get_close_matches(norm, [k for k in lookup if len(k) >= 4], n=1, cutoff=FUZZY_CUTOFF)
        if close:
            lookup[close[0]]["possible"].append(c)
    for t in targets:
        t["exact"].sort(key=sort_key)
        t["possible"].sort(key=sort_key)
    return targets


def best_tag(t):
    return t["exact"][0]["tag"] if t["exact"] else None


def row_for(c, email):
    d = {"name": c["name"], "company_listed": c["company"], "position": c["position"], "tag": c["tag"],
         "connected_on": str(c["connected_on"] or ""), "url": c["url"]}
    if email:
        d["email"] = c["email"]
    return d


def build_report(targets, top, email):
    rep = []
    for t in targets:
        rep.append({"company": t["company"], "aliases": t["names"][1:], "first_degree_count": len(t["exact"]),
                    "best_path": best_tag(t) or "none",
                    "matches": [row_for(c, email) for c in t["exact"][:top]],
                    "possible_matches_check": [row_for(c, email) for c in t["possible"][:top]]})
    return rep


def table(rows, email):
    cols = ["name", "position", "tag", "connected_on", "url"] + (["email"] if email else [])
    out = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for r in rows:
        out.append("| " + " | ".join(r[c].replace("|", "/") for c in cols) + " |")
    return out


def render_markdown(rep, email):
    out = ["# Warm paths by target company", ""]
    for c in rep:
        if not c["first_degree_count"]:
            continue
        out += ["## %s: %d first-degree connection(s)" % (c["company"], c["first_degree_count"]), ""]
        out += table(c["matches"], email) + [""]
    possible = [c for c in rep if c["possible_matches_check"]]
    if possible:
        out += ["## Possible match, check before using", "",
                "Company names that are close but not the same. Confirm on LinkedIn.", ""]
        for c in possible:
            out += ["### %s" % c["company"], ""] + table(c["possible_matches_check"], email) + [""]
    none = [c["company"] for c in rep if not c["first_degree_count"]]
    out += ["## No first-degree path", ""]
    if none:
        out.append(", ".join(none))
        out.append("")
        out.append("Hint: ask a first-degree contact at an adjacent company, a vendor or an alumni group "
                   "for an intro, and search 2nd-degree connections on LinkedIn.")
    else:
        out.append("None. Every target has at least one first-degree connection.")
    out += ["", "## Summary", "", "| Company | Connections | Best path |", "|---|---|---|"]
    for c in rep:
        best = c["best_path"]
        if best == "none" and c["possible_matches_check"]:
            best = "none (possible match only)"
        out.append("| %s | %d | %s |" % (c["company"], c["first_degree_count"], best))
    return "\n".join(out) + "\n"


def render_csv(rep, email):
    import io
    buf = io.StringIO()
    cols = ["company", "match_type", "name", "position", "tag", "connected_on", "url"] + (["email"] if email else [])
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(cols)
    for c in rep:
        for kind, rows in (("exact", c["matches"]), ("possible", c["possible_matches_check"])):
            for r in rows:
                w.writerow([c["company"], kind] + [r[k] for k in cols[2:]])
        if not c["first_degree_count"] and not c["possible_matches_check"]:
            w.writerow([c["company"], "none"] + [""] * (len(cols) - 2))
    return buf.getvalue()


def main(argv=None):
    ap = argparse.ArgumentParser(description="Find first-degree LinkedIn paths into target companies.")
    ap.add_argument("connections", help="LinkedIn Connections.csv export")
    ap.add_argument("targets", help="text file, one company per line (aliases after |)")
    ap.add_argument("--format", choices=["markdown", "csv", "json"], default="markdown")
    ap.add_argument("--since", help="only connections made on/after YYYY-MM-DD")
    ap.add_argument("--top", type=int, default=5, help="max rows per company (default 5)")
    ap.add_argument("--include-email", action="store_true", help="show email addresses (hidden by default)")
    args = ap.parse_args(argv)
    conns = load_connections(args.connections)
    if args.since:
        since = datetime.strptime(args.since, "%Y-%m-%d").date()
        conns = [c for c in conns if c["connected_on"] and c["connected_on"] >= since]
    rep = build_report(match(conns, load_targets(args.targets)), args.top, args.include_email)
    if args.format == "json":
        print(json.dumps(rep, indent=2))
    elif args.format == "csv":
        print(render_csv(rep, args.include_email), end="")
    else:
        print(render_markdown(rep, args.include_email), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
