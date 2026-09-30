#!/usr/bin/env python3
"""
NovelForge repository validator.

Checks the structural, cross-reference, manifest, and language invariants that
this repository depends on. Run locally or in CI:

    python3 scripts/validate.py            # standard checks, offline
    python3 scripts/validate.py --strict   # also fail on warnings
    python3 scripts/validate.py --schema   # additionally fetch and validate
                                           # the live Agent Plugins schema

Exit code is 0 when every check passes, 1 otherwise.

The v1.0 -> v1.5 regression, where twelve skills were silently replaced with
one-line pointers, shipped through two releases undetected. These checks exist
so that class of change cannot pass unnoticed again.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Plugins that read a manifest, and where each expects to find it.
MANIFESTS = {
    "root (Agent Plugins / Codex)": "plugin.json",
    "codex (.codex-plugin)": ".codex-plugin/plugin.json",
    "claude (.claude-plugin)": ".claude-plugin/plugin.json",
    "github (Copilot)": ".github/plugin.json",
}

# Plugins that discover skills by directory. Each must be a relative symlink
# into skills/ so the skills cannot drift out of sync.
DISCOVERY_LINKS = {
    ".opencode/skills": "OpenCode V2 (native)",
    ".agents/skills": "Codex CLI, OpenCode (compatibility)",
    ".gemini/skills": "Gemini CLI",
}

# Compatibility aliases. Each is a thin routing shim with no behaviour of its
# own; `alias_targets` records what it defers to so the mapping stays honest.
ALIASES = {
    "trope-management": "trope-manager",
    "versioning": "version-control",
    "memory-governance": "memory-manager",
    "workspace-isolation": "workspace-manager",
    "prose-style": "narrative-style",
}

# The orchestrator does not need to route to itself.
ORCHESTRATOR = "novel-orchestrator"

AGENT_SKILLS_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"

# Agent Skills specification limits.
MAX_NAME = 64
MAX_DESCRIPTION = 1024
MAX_LINES = 500

# Substance floors. These exist because two regressions in this repository's
# history were spec-VALID and so passed every format check: in v1.5 twelve
# skills were replaced with "use the existing v1.0 specialist" pointers, and in
# v2.0.1 forty-seven were replaced with a restatement of their own description.
# Both were 87-byte bodies with no vocabulary beyond the description.
#
# Measured across the current tree: legitimate bodies run 632-5620 bytes with
# 0.797-1.0 new vocabulary, against 87 bytes and 0.000 for the historical stubs.
# The thresholds below sit with wide margins on both sides.
MIN_BODY_BYTES = 400
MIN_NEW_VOCAB_RATIO = 0.35

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ALLOWED_FRONTMATTER = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}

# en-US spellings that must not appear. Matched on word boundaries only, so
# British forms such as FULFILLED, LABELLED, MODELLING, SIGNALLING pass.
US_SPELLINGS = [
    "analyze", "analyzed", "analyzing", "analyzer", "analyzes",
    "organize", "organized", "organizing", "organization", "organizational",
    "recognize", "recognized", "recognizing", "recognizable",
    "behavior", "behaviors", "behavioral",
    "color", "colors", "colored", "coloring", "colorful",
    "favor", "favors", "favored", "favorite", "favorites",
    "honor", "honors", "honored", "honorable",
    "center", "centers", "centered", "centering",
    "defense", "offense", "license", "licensed", "practicing",
    "judgment", "acknowledgment", "fulfillment",
    "traveling", "traveled", "canceled", "canceling",
    "modeling", "labeled", "labeling", "signaling", "fueling",
    "artifact", "artifacts", "specialty", "specialties", "personalized",
    "utilize", "utilized", "utilizing", "utilization",
    "finalize", "finalized", "minimize", "minimized",
    "maximize", "maximized", "summarize", "summarized",
    "prioritize", "prioritized", "categorize", "categorized",
    "standardize", "emphasize", "emphasized", "apologize",
    "realize", "realized", "realization", "skeptical", "esthetic",
    "focalized", "focalizing", "generalization", "symbolize",
]


class Report:
    """Collects pass/fail/warn results and prints a grouped summary."""

    def __init__(self) -> None:
        self.rows: list[tuple[str, str, str]] = []  # (level, section, message)

    def add(self, level: str, section: str, message: str) -> None:
        self.rows.append((level, section, message))

    def ok(self, section: str, message: str) -> None:
        self.add("ok", section, message)

    def fail(self, section: str, message: str) -> None:
        self.add("FAIL", section, message)

    def warn(self, section: str, message: str) -> None:
        self.add("warn", section, message)

    @property
    def failures(self) -> int:
        return sum(1 for level, _, _ in self.rows if level == "FAIL")

    @property
    def warnings(self) -> int:
        return sum(1 for level, _, _ in self.rows if level == "warn")

    def render(self) -> str:
        symbols = {"ok": "  ok  ", "warn": " warn ", "FAIL": " FAIL "}
        current = None
        out: list[str] = []
        for level, section, message in self.rows:
            if section != current:
                current = section
                out.append("")
                out.append(section)
                out.append("-" * len(section))
            out.append(f"[{symbols[level]}] {message}")
        return "\n".join(out)


# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------

def load_skills() -> dict[str, str]:
    """Return {skill_id: SKILL.md text}."""
    skills_dir = ROOT / "skills"
    out: dict[str, str] = {}
    if not skills_dir.is_dir():
        return out
    for entry in sorted(skills_dir.iterdir()):
        if not entry.is_dir():
            continue
        path = entry / "SKILL.md"
        if path.is_file():
            out[entry.name] = path.read_text(encoding="utf-8")
    return out


def load_templates() -> set[str]:
    """Return template paths relative to templates/, POSIX style."""
    out: set[str] = set()
    base = ROOT / "templates"
    if not base.is_dir():
        return out
    for dirpath, _, filenames in os.walk(base):
        for name in filenames:
            rel = Path(dirpath, name).relative_to(base)
            out.add(rel.as_posix())
    return out


def parse_frontmatter(text: str) -> tuple[dict[str, str], str] | None:
    """Parse the leading YAML frontmatter block into flat key/value pairs.

    Only the flat scalar form this repository uses is supported. Returns
    (fields, body), or None when there is no frontmatter.
    """
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 3)
    if end == -1:
        return None
    block = text[4:end]
    body = text[end + 5:]
    fields: dict[str, str] = {}
    for line in block.split("\n"):
        if not line.strip() or line.startswith((" ", "\t", "#")):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return fields, body


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def check_layout(r: Report, skills: dict[str, str], templates: set[str]) -> None:
    section = "Layout"
    if not skills:
        r.fail(section, "no skills found under skills/")
        return
    r.ok(section, f"{len(skills)} skills, {len(templates)} templates")

    for link, label in DISCOVERY_LINKS.items():
        path = ROOT / link
        if not path.is_symlink():
            r.fail(section, f"{link} missing or not a symlink ({label})")
            continue
        target = os.readlink(path)
        if target != "../skills":
            r.fail(section, f"{link} points to {target!r}, expected '../skills'")
            continue
        if not path.is_dir():
            r.fail(section, f"{link} does not resolve to a directory")
            continue
        found = len([d for d in path.iterdir() if (d / "SKILL.md").is_file()])
        if found != len(skills):
            r.fail(section, f"{link} resolves to {found} skills, expected {len(skills)}")
        else:
            r.ok(section, f"{link} -> {target} ({found} skills, {label})")

    for name in ("LICENSE", "README.md"):
        if (ROOT / name).is_file():
            r.ok(section, f"{name} present")
        else:
            r.fail(section, f"{name} missing")


def check_skill_spec(r: Report, skills: dict[str, str]) -> None:
    section = "Agent Skills spec"
    for skill_id, text in skills.items():
        parsed = parse_frontmatter(text)
        if parsed is None:
            r.fail(section, f"{skill_id}: missing or malformed frontmatter")
            continue
        fields, body = parsed

        unknown = set(fields) - ALLOWED_FRONTMATTER
        if unknown:
            r.fail(section, f"{skill_id}: unknown frontmatter keys {sorted(unknown)}")

        name = fields.get("name", "")
        if not NAME_RE.match(name):
            r.fail(section, f"{skill_id}: name {name!r} is not lowercase kebab-case")
        elif len(name) > MAX_NAME:
            r.fail(section, f"{skill_id}: name is {len(name)} chars, limit {MAX_NAME}")
        elif name != skill_id:
            r.fail(section, f"{skill_id}: name {name!r} does not match directory")

        description = fields.get("description", "")
        if not description:
            r.fail(section, f"{skill_id}: description missing (skill would not be advertised)")
        elif len(description) > MAX_DESCRIPTION:
            r.fail(section, f"{skill_id}: description is {len(description)} chars, limit {MAX_DESCRIPTION}")

        lines = text.count("\n") + 1
        if lines > MAX_LINES:
            r.fail(section, f"{skill_id}: {lines} lines, limit {MAX_LINES}")

        if not body.strip().startswith("# "):
            r.fail(section, f"{skill_id}: body does not begin with a level-1 heading")

    if not any(level == "FAIL" for level, sec, _ in r.rows if sec == section):
        longest = max(skills, key=lambda s: skills[s].count("\n") + 1)
        r.ok(section, f"all {len(skills)} skills compliant (longest: {longest}, {skills[longest].count(chr(10)) + 1} lines)")


def check_substance(r: Report, skills: dict[str, str]) -> None:
    """Guard against the two regressions that were spec-valid and so invisible.

    A skill may satisfy every Agent Skills rule and still be worthless. Both
    regressions in this repository's history were well-formed files that simply
    carried no instructions.
    """
    section = "Skill substance"

    def tokens(text: str) -> set[str]:
        return set(re.sub(r"[^a-z0-9 ]", " ", text.lower()).split())

    thin: list[str] = []
    restated: list[str] = []
    for skill_id, text in skills.items():
        parsed = parse_frontmatter(text)
        if parsed is None:
            continue
        fields, body = parsed
        body = body.strip()
        description = fields.get("description", "")

        if len(body) < MIN_BODY_BYTES:
            thin.append(f"{skill_id}: body is {len(body)} bytes, floor {MIN_BODY_BYTES}")
            continue

        body_tokens = tokens(body)
        if not body_tokens:
            thin.append(f"{skill_id}: body has no readable content")
            continue
        new_ratio = len(body_tokens - tokens(description)) / len(body_tokens)
        if new_ratio < MIN_NEW_VOCAB_RATIO:
            restated.append(
                f"{skill_id}: body adds only {new_ratio:.0%} vocabulary beyond its "
                f"description (floor {MIN_NEW_VOCAB_RATIO:.0%})"
            )

    for item in thin:
        r.fail(section, f"gutted skill -- {item}")
    for item in restated:
        r.fail(section, f"restates its own description -- {item}")

    if not thin and not restated:
        sizes = sorted(
            (len(parse_frontmatter(t)[1].strip()), s) for s, t in skills.items() if parse_frontmatter(t)
        )
        r.ok(section, f"all {len(skills)} skills carry instructions (thinnest: {sizes[0][1]}, {sizes[0][0]} bytes)")


def check_aliases(r: Report, skills: dict[str, str]) -> None:
    section = "Compatibility aliases"
    for alias, target in ALIASES.items():
        if alias not in skills:
            r.fail(section, f"{alias}: declared alias is missing from skills/")
            continue
        if target not in skills:
            r.fail(section, f"{alias}: target {target} does not exist")
            continue
        text = skills[alias].lower()
        if target not in text:
            r.fail(section, f"{alias}: does not name its target {target}")
            continue
        if alias in ALIASES and target in ALIASES:
            r.fail(section, f"{alias}: points at another alias ({target}) rather than a working engine")
            continue
        r.ok(section, f"{alias} -> {target}")


def check_routing(r: Report, skills: dict[str, str]) -> None:
    section = "Orchestrator routing"
    if ORCHESTRATOR not in skills:
        r.fail(section, f"{ORCHESTRATOR} missing")
        return
    orchestrator = skills[ORCHESTRATOR]
    mentioned = set(re.findall(r"`([a-z][a-z0-9-]+)`", orchestrator))
    unrouted = sorted(
        s for s in skills
        if s not in mentioned and s != ORCHESTRATOR and s not in ALIASES
    )
    if unrouted:
        r.fail(section, f"engines absent from the routing table: {unrouted}")
    else:
        engines = len(skills) - len(ALIASES) - 1
        r.ok(section, f"all {engines} engines routed from {ORCHESTRATOR}")


def check_references(r: Report, skills: dict[str, str], templates: set[str]) -> None:
    section = "Cross-references"
    known = set(skills)
    project_templates = {t[len("project/"):] for t in templates if t.startswith("project/")}

    dangling_skills: list[str] = []
    dangling_templates: list[str] = []

    for skill_id, text in skills.items():
        for ref in set(re.findall(r"`([a-z][a-z0-9]+(?:-[a-z0-9]+)+)`", text)):
            if ref not in known:
                dangling_skills.append(f"{skill_id} -> skill {ref}")

        for ref in set(re.findall(r"`([A-Za-z_][A-Za-z0-9_-]*(?:/[A-Za-z0-9_.-]+)*\.md)`", text)):
            # Accept paths written relative to templates/, to project/, or to the
            # plugin root (a leading `templates/` is the repo-root form).
            candidates = {ref, ref[len("templates/"):] if ref.startswith("templates/") else ref}
            if candidates & templates or candidates & project_templates or {f"project/{c}" for c in candidates} & templates:
                continue
            dangling_templates.append(f"{skill_id} -> template {ref}")

    if dangling_skills:
        for item in sorted(dangling_skills):
            r.fail(section, f"dangling {item}")
    else:
        r.ok(section, "no dangling skill references")

    if dangling_templates:
        for item in sorted(dangling_templates):
            r.fail(section, f"dangling {item}")
    else:
        r.ok(section, "no dangling template references")

    referenced: set[str] = set()
    for text in skills.values():
        for ref in re.findall(r"`([A-Za-z_][A-Za-z0-9_-]*(?:/[A-Za-z0-9_.-]+)*\.md)`", text):
            referenced.add(ref)
            referenced.add(f"project/{ref}")
            if ref.startswith("templates/"):
                referenced.add(ref[len("templates/"):])
    # Human entry points are not skill targets.
    entry_points = {"project/PROJECT_README.md", "COMMANDS.md"}
    orphans = sorted(t for t in templates if t not in referenced and t not in entry_points)
    if orphans:
        r.warn(section, f"templates not referenced by any skill: {orphans}")
    else:
        r.ok(section, "every domain template is referenced by a skill")


def check_manifests(r: Report) -> dict[str, dict]:
    section = "Manifests"
    loaded: dict[str, dict] = {}
    for label, rel in MANIFESTS.items():
        path = ROOT / rel
        if not path.is_file():
            r.fail(section, f"{rel} missing ({label})")
            continue
        try:
            loaded[label] = json.loads(path.read_text(encoding="utf-8"))
            r.ok(section, f"{rel} valid JSON")
        except json.JSONDecodeError as exc:
            r.fail(section, f"{rel} invalid JSON: {exc}")

    if len(loaded) != len(MANIFESTS):
        return loaded

    for field in ("name", "version", "license"):
        values = {label: data.get(field) for label, data in loaded.items()}
        if len(set(values.values())) > 1:
            r.fail(section, f"{field} differs across manifests: {values}")
        else:
            r.ok(section, f"{field} consistent: {next(iter(values.values()))!r}")

    root = loaded.get("root (Agent Plugins / Codex)")
    if root:
        for key in ("$schema", "name", "version", "description", "author"):
            if key not in root:
                r.fail(section, f"plugin.json missing required key {key!r}")
        if not NAME_RE.match(str(root.get("name", ""))):
            r.fail(section, f"plugin.json name {root.get('name')!r} is not lowercase kebab-case")
        if root.get("$schema") != AGENT_SKILLS_SCHEMA:
            r.fail(section, f"plugin.json $schema does not point at {AGENT_SKILLS_SCHEMA}")

    claude = loaded.get("claude (.claude-plugin)")
    if claude and not claude.get("displayName"):
        r.warn(section, ".claude-plugin/plugin.json has no displayName")

    return loaded


def check_schema(r: Report, manifests: dict[str, dict]) -> None:
    section = "Agent Plugins schema (live)"
    root = manifests.get("root (Agent Plugins / Codex)")
    if not root:
        return
    try:
        with urllib.request.urlopen(AGENT_SKILLS_SCHEMA, timeout=20) as response:
            schema = json.load(response)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as exc:
        r.warn(section, f"could not fetch schema ({exc}); skipped")
        return

    allowed = set(schema.get("properties", {}))
    unknown = sorted(set(root) - allowed)
    if unknown:
        r.fail(section, f"plugin.json has fields the schema forbids: {unknown}")
    else:
        r.ok(section, "no schema-forbidden fields in plugin.json")

    for key in schema.get("required", []):
        if key not in root:
            r.fail(section, f"plugin.json missing required field {key!r}")

    author_schema = schema.get("properties", {}).get("author", {})
    if author_schema.get("additionalProperties") is False:
        allowed_author = set(author_schema.get("properties", {}))
        bad = sorted(set(root.get("author", {})) - allowed_author)
        if bad:
            r.fail(section, f"plugin.json author has forbidden keys: {bad}")


def check_license(r: Report, manifests: dict[str, dict]) -> None:
    section = "Licence"
    path = ROOT / "LICENSE"
    if not path.is_file():
        r.fail(section, "LICENSE missing")
        return
    text = path.read_text(encoding="utf-8")
    if "MIT License" not in text:
        r.fail(section, "LICENSE is not MIT")
        return
    copyright_line = next((l for l in text.split("\n") if l.startswith("Copyright")), "")
    root = manifests.get("root (Agent Plugins / Codex)", {})
    author = root.get("author", {}).get("name")
    if author and author not in copyright_line:
        r.fail(section, f"LICENSE copyright {copyright_line.strip()!r} does not match manifest author {author!r}")
    else:
        r.ok(section, f"MIT, copyright holder matches manifest author ({author})")
    if root.get("license") and root["license"] != "MIT":
        r.fail(section, f"plugin.json declares licence {root['license']!r} but LICENSE is MIT")


def check_language(r: Report, skills: dict[str, str], templates: set[str]) -> None:
    section = "Language (en-GB)"
    pattern = re.compile(r"\b(" + "|".join(US_SPELLINGS) + r")\b", re.IGNORECASE)
    hits: list[str] = []
    for skill_id, text in skills.items():
        for match in set(pattern.findall(text)):
            hits.append(f"skills/{skill_id}: {match}")
    for rel in sorted(templates):
        text = (ROOT / "templates" / rel).read_text(encoding="utf-8")
        for match in set(pattern.findall(text)):
            hits.append(f"templates/{rel}: {match}")
    if hits:
        for hit in sorted(hits):
            r.fail(section, f"en-US spelling {hit}")
    else:
        r.ok(section, "no en-US spellings in skills or templates")


def check_no_stale_version_labels(r: Report, skills: dict[str, str]) -> None:
    section = "Version labels"
    pattern = re.compile(r"\bv?(1\.[0-9](?:\.[0-9])?)\b")
    stale: list[str] = []
    for scope, text in list(skills.items()):
        for match in set(pattern.findall(text)):
            stale.append(f"skills/{scope}: {match}")
    base = ROOT / "templates"
    for dirpath, _, filenames in os.walk(base):
        for name in filenames:
            path = Path(dirpath, name)
            text = path.read_text(encoding="utf-8")
            for match in set(pattern.findall(text)):
                stale.append(f"templates/{path.relative_to(base)}: {match}")
    if stale:
        for item in sorted(stale):
            r.fail(section, f"stale version label {item}")
    else:
        r.ok(section, "no pre-2.0 version labels in skills or templates")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the NovelForge repository.")
    parser.add_argument("--strict", action="store_true", help="treat warnings as failures")
    parser.add_argument("--schema", action="store_true", help="also validate against the live Agent Plugins schema")
    args = parser.parse_args()

    skills = load_skills()
    templates = load_templates()
    report = Report()

    print("NovelForge validator")
    print("===================")

    check_layout(report, skills, templates)
    check_skill_spec(report, skills)
    check_substance(report, skills)
    check_aliases(report, skills)
    check_routing(report, skills)
    check_references(report, skills, templates)
    manifests = check_manifests(report)
    if args.schema:
        check_schema(report, manifests)
    check_license(report, manifests)
    check_language(report, skills, templates)
    check_no_stale_version_labels(report, skills)

    print(report.render())
    print()
    print("=" * 40)
    if report.failures:
        print(f"FAILED  {report.failures} failure(s), {report.warnings} warning(s)")
        return 1
    if report.warnings and args.strict:
        print(f"FAILED  {report.warnings} warning(s) under --strict")
        return 1
    print(f"PASSED  {report.warnings} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
