#!/usr/bin/env python3
"""Advance upstream.json to upstream main HEAD.

Fetches each tracked upstream repo's HEAD commit, re-enumerates its proto
directory (so brand-new upstream files are picked up), and rewrites
upstream.json with the new commit, fetch date and per-file sha256 hashes.
Used by the weekly upstream-drift workflow to prepare a reconcile PR; the PR's
own CI (pinned-mode coverage gate) then lists exactly which symbols the human
must merge into proto/ before it can go green.
"""

from __future__ import annotations

import datetime
import hashlib
import json
import sys
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def gh_json(url: str):
    with urllib.request.urlopen(url) as resp:
        return json.load(resp)


def main() -> int:
    pin_path = REPO_ROOT / "upstream.json"
    pins = json.loads(pin_path.read_text())
    today = datetime.date.today().isoformat()
    changed = False

    for name, cfg in pins["upstreams"].items():
        head = gh_json(
            f"https://api.github.com/repos/{cfg['repo']}/branches/main"
        )["commit"]["sha"]
        if head == cfg["commit"]:
            print(f"{name}: already at {head[:12]}")
            continue
        listing = gh_json(
            f"https://api.github.com/repos/{cfg['repo']}/contents/"
            f"{cfg['pathPrefix']}?ref={head}"
        )
        files = {}
        for entry in sorted(listing, key=lambda e: e["name"]):
            if not entry["name"].endswith(".proto"):
                continue
            url = (
                f"https://raw.githubusercontent.com/{cfg['repo']}/{head}/"
                f"{cfg['pathPrefix']}/{entry['name']}"
            )
            with urllib.request.urlopen(url) as resp:
                files[entry["name"]] = hashlib.sha256(resp.read()).hexdigest()
        print(f"{name}: {cfg['commit'][:12]} -> {head[:12]} ({len(files)} files)")
        cfg.update(commit=head, fetched=today, files=files)
        changed = True

    if changed:
        pin_path.write_text(json.dumps(pins, indent=2) + "\n")
    print("changed" if changed else "up-to-date")
    return 0


if __name__ == "__main__":
    sys.exit(main())
