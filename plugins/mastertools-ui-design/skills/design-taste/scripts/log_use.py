"""Log one real use of the skill to DT/usage.jsonl and print its id.

One line per real brief: the job, device and dial, each option shown (label, dial, the
build-rule ids from the user's profile it leans on, the judge's rank), the check results and the
skill version. The user's reaction is logged later with log_choice.py --use <id>.

The project is stored as a short hash of its folder, never its name. Text fields go through
log_choice.py's filter (no emails, links, money, phone numbers or long passages).
When the evidence folder can't be reached (Cowork sandbox, the web), nothing is logged and
the script says so in one line; the reply to the user stays clean.

usage: log_use.py [--text 0.7] --job docs-home --device both --mode design --judge agent \
         --option "Fit:2:A1,D1,D2:1"  (rule ids split by commas or spaces; may be empty) --option "Proven:1:F1,D1:2" \
         [--checks pass | --checks "fixed: small targets"] [--asked "docs serif?"] [--project-dir PATH]
"""
import argparse, hashlib, json, os, re, secrets, sys
from datetime import datetime, timezone
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dt import DT, SKILL, ready, profile_files
from log_choice import check

JOBS = ["homepage", "product-page", "docs-home", "docs-article", "app-flow", "settings-dashboard", "studio", "other"]
MODES = ["design", "critique", "pick", "steer"]


def rule_ids():
    """Build-rule ids defined in the user's profile pages (first table column)."""
    ids = set()
    for path in profile_files():
        with open(path, encoding="utf-8") as fh:
            ids |= set(re.findall(r"^\| ([A-Z]\d+) \|", fh.read(), re.M))
    return ids


def version():
    """Short hash of the user's profile pages, so a result ties to the rules it ran with,
    whether the skill runs from git or from an installed copy."""
    h = hashlib.sha256()
    for path in profile_files():
        with open(path, "rb") as fh:
            h.update(fh.read())
    return h.hexdigest()[:8]


def installed_version():
    """The VERSION file shipped next to this script, or None for a copy older than v0.7."""
    try:
        with open(os.path.join(SKILL, "VERSION"), encoding="utf-8") as fh:
            return fh.read().strip()
    except OSError:
        return None


def project_hash(path):
    """Salted with a random value kept in DT, so a guessed folder path can't be confirmed from the log."""
    salt_file = os.path.join(DT, ".project-salt")
    if not os.path.exists(salt_file):
        with open(salt_file, "w") as fh:
            fh.write(secrets.token_hex(16))
    with open(salt_file) as fh:
        salt = fh.read().strip()
    return hashlib.sha256((salt + os.path.realpath(path)).encode()).hexdigest()[:8]


def parse_option(text, known):
    parts = text.split(":")
    if len(parts) != 4:
        sys.exit(f'refused: option "{text}" must be LABEL:DIAL:RULES:RANK, e.g. "Fit:2:A1,H1:1"')
    label, dial, rules, rank = parts
    check("option label", label)
    if not dial.isdigit() or not 1 <= int(dial) <= 5:
        sys.exit(f'refused: option "{label}" dial must be 1-5')
    ids = [r for r in re.split(r"[,\s]+", rules) if r]
    bad = [r for r in ids if r not in known]
    if bad:
        sys.exit(f"refused: unknown rule ids {bad}; use ids from the build rules in the user's taste profile")
    if not rank.isdigit():
        sys.exit(f'refused: option "{label}" rank must be a number (1 = judge\'s top pick)')
    return {"label": label, "dial": int(dial), "rules": ids, "rank": int(rank)}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--job", required=True, choices=JOBS)
    ap.add_argument("--device", required=True, choices=["desktop", "phone", "both"])
    ap.add_argument("--mode", required=True, choices=MODES)
    ap.add_argument("--judge", required=True, choices=["agent", "self", "none"],
                    help="agent = fresh judge agent ranked the options; self = Claude in its own context")
    ap.add_argument("--option", action="append", default=[], help="LABEL:DIAL:RULES:RANK, once per option")
    ap.add_argument("--checks", default="not run", help='"pass", or a few words on what failed or was fixed')
    ap.add_argument("--asked", help="where the profile was unsure and the user was asked, in a few words")
    ap.add_argument("--surface", default="code", choices=["code", "cowork", "chat"])
    ap.add_argument("--project-dir", default=os.getcwd())
    ap.add_argument("--text", help="the version in the SKILL.md title Claude is following, e.g. 0.7")
    a = ap.parse_args(argv)

    for f in ("checks", "asked"):
        check(f, getattr(a, f))
    if a.text is not None:
        a.text = a.text.strip().lstrip("vV")
        if not re.fullmatch(r"\d+(\.\d+)*", a.text):
            sys.exit('refused: --text must be a version number, e.g. 0.7')
    # Before the folder check: a stale text matters even where nothing can be logged.
    if a.text and installed_version() and a.text != installed_version():
        print(f"stale text: following v{a.text}, installed v{installed_version()}. Re-read SKILL.md in {SKILL}")
    known = rule_ids()
    options = [parse_option(o, known) for o in a.option]
    if a.mode == "design" and not options:
        sys.exit("refused: a design use needs at least one --option")
    if len({o["label"] for o in options}) != len(options):
        sys.exit("refused: option labels must be unique")
    if len({o["rank"] for o in options}) != len(options):
        sys.exit("refused: option ranks must be unique (1 = judge's top pick)")

    if not ready():
        print("not logged: the Design Taste folder is not reachable from here")
        return None
    uid = "u-" + datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S") + "-" + secrets.token_hex(2)
    row = {"id": uid, "at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "surface": a.surface,
           "project": project_hash(a.project_dir), "job": a.job, "device": a.device, "mode": a.mode,
           "judge": a.judge, "options": options, "checks": a.checks, "version": version(),
           "skill": installed_version(), "text": a.text}
    if a.asked:
        row["asked"] = a.asked
    path = os.path.join(DT, "usage.jsonl")
    with open(path, "a") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(uid)
    return uid


if __name__ == "__main__":
    main()
