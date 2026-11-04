"""Shared paths: the evidence folder (DT) and the user's taste profile.

DT is per user. By default it is ~/.config/mastertools/design-taste/, created on the first write.
To keep it somewhere else (a synced folder, so several accounts on one machine share one log),
put that folder's path on the first line of ~/.config/mastertools/design-taste.dir. DESIGN_TASTE_DIR
overrides both (tests use a temp folder). A folder named by the pointer file or the variable is
never created: when it can't be reached, the scripts report "not reachable" instead of writing
somewhere new.

The user's profile (taste-profile.md and any rule pages beside it) is read from the first of:
DESIGN_TASTE_PROFILE_DIR, the overlay ~/.claude/overlays/design-taste/, DT, and last this skill's
own empty template.
"""
import glob
import os

DEFAULT = os.path.expanduser("~/.config/mastertools/design-taste")
POINTER = os.path.expanduser("~/.config/mastertools/design-taste.dir")
OVERLAY = os.path.expanduser("~/.claude/overlays/design-taste")
SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def find():
    env = os.environ.get("DESIGN_TASTE_DIR")
    if env:
        return env
    try:
        with open(POINTER, encoding="utf-8") as f:
            path = f.readline().strip()
        if path:
            return os.path.expanduser(path)
    except OSError:
        pass
    return DEFAULT


DT = find()


def ready():
    """True when DT can be written. Creates the default folder on first use; never creates another."""
    if os.path.isdir(DT):
        return True
    if DT == DEFAULT:
        try:
            os.makedirs(DT, exist_ok=True)
            return True
        except OSError:
            return False
    return False


def profile_dir():
    for d in (os.environ.get("DESIGN_TASTE_PROFILE_DIR"), OVERLAY, DT):
        if d and os.path.isfile(os.path.join(d, "taste-profile.md")):
            return d
    return SKILL


def profile_files():
    """taste-profile.md plus any other rule pages beside it, sorted; README and ROADMAP excluded."""
    d = profile_dir()
    if d == SKILL:
        return [os.path.join(SKILL, "taste-profile.md")]
    skip = {"README.md", "ROADMAP.md"}
    return sorted(p for p in glob.glob(os.path.join(d, "*.md")) if os.path.basename(p) not in skip)
