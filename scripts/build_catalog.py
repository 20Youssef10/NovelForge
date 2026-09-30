#!/usr/bin/env python3
"""
Build the OpenCode HTTP skill catalog.

OpenCode can install skills from an HTTP catalog: a base URL serving an
index.json, from which it downloads each skill into a private directory. That
lets users install NovelForge without cloning.

The layout matters. From the OpenCode V2 docs:

    "<base>/<name>/<file>"   for each file in files[]
    "Each downloaded skill directory becomes a source root"
    "A root-level SKILL.md currently has the literal ID SKILL in V2"

So a catalog that ships `SKILL.md` would collapse every skill onto the single
ID `SKILL`. The fix is to ship `<name>.md` instead, which yields the ID
`<name>`. That is why this script flattens each SKILL.md into `<name>.md`
rather than copying the directory tree.

Generated output is never hand-edited. Run:

    python3 scripts/build_catalog.py           # write catalog/
    python3 scripts/build_catalog.py --check   # exit 1 if catalog/ is stale
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
CATALOG = ROOT / "catalog"

# Bump when skill content changes so OpenCode refreshes its cache.
CATALOG_VERSION = "3"


def strip_frontmatter(text: str) -> str:
    """OpenCode tolerates frontmatter, but the flattened file is cleaner without it."""
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 3)
    return text[end + 5:] if end != -1 else text


def payload_for(skill_dir: Path) -> list[Path]:
    """Support files shipped alongside SKILL.md, excluding it."""
    out: list[Path] = []
    for sub in ("references", "scripts", "assets"):
        d = skill_dir / sub
        if d.is_dir():
            out.extend(sorted(p for p in d.rglob("*") if p.is_file()))
    return out


def build() -> dict:
    entries = []
    for skill_dir in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            continue
        name = skill_dir.name
        files = [f"{name}.md"]
        for extra in payload_for(skill_dir):
            files.append(extra.relative_to(skill_dir).as_posix())
        entries.append({"name": name, "version": CATALOG_VERSION, "files": files})
    return {"skills": entries}


def write(plan: dict) -> None:
    if CATALOG.exists():
        shutil.rmtree(CATALOG)
    for entry in plan["skills"]:
        skill_dir = SKILLS / entry["name"]
        out_dir = CATALOG / entry["name"]
        out_dir.mkdir(parents=True, exist_ok=True)

        # The entry file, named so OpenCode derives the ID from the name.
        body = strip_frontmatter((skill_dir / "SKILL.md").read_text(encoding="utf-8"))
        (out_dir / f"{entry['name']}.md").write_text(body, encoding="utf-8")

        # Preserve the frontmatter separately so nothing is lost in flattening.
        raw = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        if raw.startswith("---\n"):
            end = raw.find("\n---\n", 3)
            (out_dir / "SKILL.original.md").write_text(raw[4:end], encoding="utf-8")

        for rel in entry["files"][1:]:
            dest = out_dir / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(skill_dir / rel, dest)

    (CATALOG / "index.json").write_text(
        json.dumps(plan, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the OpenCode HTTP skill catalog.")
    parser.add_argument("--check", action="store_true",
                        help="exit 1 if catalog/ is missing or stale instead of writing it")
    args = parser.parse_args()

    plan = build()
    if not plan["skills"]:
        print("error: no skills found", file=sys.stderr)
        return 1

    if args.check:
        index = CATALOG / "index.json"
        if not index.is_file():
            print("catalog/ is missing; run scripts/build_catalog.py", file=sys.stderr)
            return 1
        current = json.loads(index.read_text(encoding="utf-8"))
        if current != plan:
            print("catalog/ is stale; run scripts/build_catalog.py", file=sys.stderr)
            return 1
        for entry in plan["skills"]:
            d = CATALOG / entry["name"]
            for rel in entry["files"]:
                if not (d / rel).is_file():
                    print(f"catalog missing file: {entry['name']}/{rel}", file=sys.stderr)
                    return 1
            original = SKILLS / entry["name"] / "SKILL.md"
            flattened = d / f"{entry['name']}.md"
            if original.read_text(encoding="utf-8") != \
                    "---\n" + (d / "SKILL.original.md").read_text(encoding="utf-8") + "\n---\n" + \
                    flattened.read_text(encoding="utf-8"):
                print(f"catalog content drifted: {entry['name']}", file=sys.stderr)
                return 1
        print(f"catalog is up to date ({len(plan['skills'])} skills)")
        return 0

    write(plan)
    total = sum(len(e["files"]) for e in plan["skills"])
    print(f"wrote catalog/ with {len(plan['skills'])} skills, {total} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
