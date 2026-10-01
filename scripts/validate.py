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

try:
    from PIL import Image
except ImportError:  # Pillow is optional; icon checks degrade to existence + suffix
    Image = None
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

# Skills that discover skills by directory.
#
# `.opencode/skills` and `.gemini/skills` must be relative symlinks into
# skills/ so the skills cannot drift out of sync.
#
# `.agents/skills` is the exception: it is a real directory, because the skills
# CLI (`npx skills`) and Codex CLI both install third-party skills there. When it
# was a symlink to skills/, any `npx skills add` wrote foreign skills into
# NovelForge's canonical source tree. It must stay a real directory.
DISCOVERY_LINKS = {
    ".opencode/skills": "OpenCode V2 (native)",
    ".gemini/skills": "Gemini CLI",
}

# Install target for the skills CLI and Codex CLI. Must exist, must be a real
# directory, and must not be a symlink into the canonical tree.
INSTALL_TARGET = ".agents/skills"

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

    # The install target must stay a real directory so third-party skills
    # installed by the skills CLI cannot land in the canonical tree.
    install = ROOT / INSTALL_TARGET
    if install.is_symlink():
        r.fail(section, f"{INSTALL_TARGET} is a symlink to {os.readlink(install)!r}; "
                        f"it must be a real directory so `npx skills add` cannot "
                        f"write into skills/")
    elif not install.is_dir():
        r.fail(section, f"{INSTALL_TARGET} missing (skills CLI and Codex CLI install target)")
    else:
        foreign = sorted(
            d.name for d in install.iterdir()
            if d.is_dir() and (d / "SKILL.md").is_file() and d.name not in skills
        )
        if foreign:
            r.ok(section, f"{INSTALL_TARGET} is a real directory "
                         f"({len(foreign)} third-party skill(s) installed: {', '.join(foreign)})")
        else:
            r.ok(section, f"{INSTALL_TARGET} is a real directory (no third-party skills installed)")

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


def check_routing(r: Report, skills: dict[str, str]) -> None:
    section = "Orchestrator routing"
    if ORCHESTRATOR not in skills:
        r.fail(section, f"{ORCHESTRATOR} missing")
        return
    orchestrator = skills[ORCHESTRATOR]
    mentioned = set(re.findall(r"`([a-z][a-z0-9-]+)`", orchestrator))
    unrouted = sorted(s for s in skills if s not in mentioned and s != ORCHESTRATOR)
    if unrouted:
        r.fail(section, f"skills absent from the routing table: {unrouted}")
    else:
        r.ok(section, f"all {len(skills) - 1} skills routed from {ORCHESTRATOR}")


def check_references(r: Report, skills: dict[str, str], templates: set[str]) -> None:
    section = "Cross-references"
    known = set(skills)
    project_templates = {t[len("project/"):] for t in templates if t.startswith("project/")}

    dangling_skills: list[str] = []
    dangling_templates: list[str] = []
    dangling_local: list[str] = []

    # Per-skill payload directories defined by the Agent Skills spec. Paths
    # written inside a skill are relative to that skill's own directory, so
    # these are checked against the filesystem rather than the template tree.
    LOCAL_DIRS = ("references/", "scripts/", "assets/")

    for skill_id, text in skills.items():
        for ref in set(re.findall(r"`([a-z][a-z0-9]+(?:-[a-z0-9]+)+)`", text)):
            if ref not in known:
                dangling_skills.append(f"{skill_id} -> skill {ref}")

        for ref in sorted(set(re.findall(r"`([A-Za-z_][A-Za-z0-9_-]*(?:/[A-Za-z0-9_.-]+)*\.(?:md|py|sh|ts|js|json))`", text))):
            if ref.startswith(LOCAL_DIRS):
                target = ROOT / "skills" / skill_id / ref
                if not target.is_file():
                    dangling_local.append(f"{skill_id} -> {ref} (file does not exist)")
                elif target.stat().st_size == 0:
                    dangling_local.append(f"{skill_id} -> {ref} (file is empty)")
                continue
            # Accept paths written relative to templates/, to project/, or to the
            # plugin root (a leading `templates/` is the repo-root form).
            if not ref.endswith(".md"):
                continue
            candidates = {ref, ref[len("templates/"):] if ref.startswith("templates/") else ref}
            if candidates & templates or candidates & project_templates or {f"project/{c}" for c in candidates} & templates:
                continue
            dangling_templates.append(f"{skill_id} -> template {ref}")

    if dangling_skills:
        for item in sorted(dangling_skills):
            r.fail(section, f"dangling {item}")
    else:
        r.ok(section, "no dangling skill references")

    if dangling_local:
        for item in sorted(dangling_local):
            r.fail(section, f"bad skill-local reference {item}")
    else:
        payload = sorted(
            p.parent.name
            for s in skills
            for p in (ROOT / "skills" / s).rglob("*")
            if p.is_file() and p.parent.name in {"references", "scripts", "assets"}
        )
        if payload:
            r.ok(section, f"all skill-local payload references resolve ({len(payload)} files)")
        else:
            r.ok(section, "no skill-local payload references")

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


def check_version_agreement(r: Report, manifests: dict[str, dict], skills: dict[str, str]) -> None:
    """The version must agree everywhere it is written, not just in the manifests.

    `plugin.json` is not the only place a version is recorded. The README title
    and the Claude marketplace metadata both carry one, and both drifted during
    2.3.1 because only the four plugin manifests were being compared.
    """
    section = "Version agreement"
    versions = {label: d.get("version") for label, d in manifests.items() if d}
    if not versions:
        r.fail(section, "no manifests loaded")
        return
    canonical = next(iter(set(versions.values()))) if len(set(versions.values())) == 1 else None
    if canonical is None:
        r.fail(section, f"manifests disagree: {versions}")
        return
    r.ok(section, f"manifests agree on {canonical}")

    readme = ROOT / "README.md"
    if readme.is_file():
        first = readme.read_text(encoding="utf-8").split("\n", 1)[0]
        found = re.search(r"\bv?(\d+\.\d+\.\d+)\b", first)
        if not found:
            r.fail(section, f"README title carries no version: {first!r}")
        elif found.group(1) != canonical:
            r.fail(section, f"README title says {found.group(1)} but manifests say {canonical}")

    for rel in (".claude-plugin/marketplace.json", ".agents/plugins/marketplace.json"):
        path = ROOT / rel
        if not path.is_file():
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            r.fail(section, f"{rel} invalid JSON: {exc}")
            continue
        declared = (data.get("metadata") or {}).get("version")
        if declared and declared != canonical:
            r.fail(section, f"{rel} metadata.version is {declared}, manifests say {canonical}")

    # Engine counts quoted in prose go stale as skills are added or removed.
    engines = len(skills) - 1  # every skill except the orchestrator
    for rel in (".claude-plugin/marketplace.json", "plugin.json", ".codex-plugin/plugin.json"):
        path = ROOT / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for quoted in re.findall(r"\b(\d+)\s+(?:specialist\s+)?(?:novel-writing\s+)?engines\b", text):
            if int(quoted) != engines:
                r.fail(section, f"{rel} claims {quoted} engines, there are {engines}")


def check_openai_listing(r: Report, manifests: dict[str, dict]) -> None:
    """Enforce the documented OpenAI listing-metadata limits.

    `category` must be a "required category title from the dashboard", so it
    has to be one of the published titles rather than an arbitrary string. The
    character limits below are hard submission limits; exceeding one is a
    packaging error, not a style preference.
    """
    section = "OpenAI listing"
    valid_categories = {
        "Productivity", "Creativity", "Developer Tools", "Business",
        "Education", "Finance", "Health", "Data", "Communication", "Utilities",
    }
    limits = {
        "displayName": 30, "shortDescription": 30, "longDescription": 4000,
        "developerName": 80,
    }
    prompt_max, prompt_count = 128, 3
    caps_count, cap_len, desc_max = 20, 120, 4000

    sources = [
        ("plugin.json", manifests.get("root (Agent Plugins / Codex)")),
        (".codex-plugin/plugin.json", manifests.get("codex (.codex-plugin)")),
    ]
    checked = 0
    for label, data in sources:
        if not data:
            continue
        if label.startswith(".codex"):
            iface = data.get("interface")
        else:
            iface = (data.get("extensions", {}).get("com.openai", {}) or {}).get("interface")
        if not isinstance(iface, dict):
            r.warn(section, f"{label}: no interface object to check")
            continue
        checked += 1

        for field, limit in limits.items():
            value = iface.get(field)
            if value is None:
                r.warn(section, f"{label}: interface.{field} missing")
            elif len(value) > limit:
                r.fail(section, f"{label}: interface.{field} is {len(value)} chars, limit {limit}")

        category = iface.get("category")
        if category is None:
            r.fail(section, f"{label}: interface.category missing")
        elif category not in valid_categories:
            r.fail(section, f"{label}: category {category!r} is not a dashboard category "
                            f"({', '.join(sorted(valid_categories))})")

        prompts = iface.get("defaultPrompt") or []
        if isinstance(prompts, str):
            prompts = [prompts]
        if len(prompts) > prompt_count:
            r.fail(section, f"{label}: {len(prompts)} defaultPrompt entries, limit {prompt_count}")
        for i, prompt in enumerate(prompts, 1):
            if len(prompt) > prompt_max:
                r.fail(section, f"{label}: defaultPrompt {i} is {len(prompt)} chars, limit {prompt_max}")

        caps = iface.get("capabilities") or []
        if len(caps) > caps_count:
            r.fail(section, f"{label}: {len(caps)} capabilities, limit {caps_count}")
        for c in caps:
            if len(c) > cap_len:
                r.fail(section, f"{label}: capability {c!r} is {len(c)} chars, limit {cap_len}")

        description = data.get("description", "")
        if len(description) > desc_max:
            r.fail(section, f"{label}: description is {len(description)} chars, limit {desc_max}")

    mk = ROOT / ".agents" / "plugins" / "marketplace.json"
    if mk.is_file():
        try:
            entries = json.loads(mk.read_text(encoding="utf-8")).get("plugins", [])
        except json.JSONDecodeError as exc:
            r.fail(section, f"marketplace.json invalid JSON: {exc}")
            entries = []
        for entry in entries:
            name = entry.get("name")
            if "category" not in entry:
                r.fail(section, f"marketplace entry {name!r} missing category")
            policy = entry.get("policy")
            if not isinstance(policy, dict):
                r.fail(section, f"marketplace entry {name!r} missing policy")
            else:
                for key in ("installation", "authentication"):
                    if key not in policy:
                        r.fail(section, f"marketplace entry {name!r} missing policy.{key}")
            cat = entry.get("category")
            if cat is not None and cat not in valid_categories:
                r.fail(section, f"marketplace entry {name!r} category {cat!r} "
                                f"is not a dashboard category")

    if checked and not any(lv == "FAIL" and sec == section for lv, sec, _ in r.rows):
        r.ok(section, f"listing metadata within limits for {checked} manifest(s)")


def check_icons(r: Report, manifests: dict[str, dict]) -> None:
    """Icons must satisfy the documented submission constraints.

    Square, at least 48x48, PNG/JPEG/WebP/SVG, at most 5 MiB, and referenced by a
    ./ prefixed path that resolves from the plugin root. Codex package validation
    requires both logo and composerIcon; without them the package is public on
    GitHub but cannot be submitted to the ChatGPT/Codex directory.
    """
    section = "Icons"
    supported = {".png", ".jpg", ".jpeg", ".webp", ".svg"}
    max_bytes = 5 * 1024 * 1024

    def check_image(path: Path) -> str | None:
        if not path.is_file():
            return "file does not exist"
        if path.suffix.lower() not in supported:
            return f"unsupported format {path.suffix}"
        size = path.stat().st_size
        if size > max_bytes:
            return f"{size / 1024 / 1024:.1f} MiB exceeds the 5 MiB limit"
        if path.suffix.lower() != ".svg":
            try:
                with Image.open(path) as im:
                    w, h = im.size
                if w != h:
                    return f"not square ({w}x{h})"
                if w < 48:
                    return f"{w}x{h} is below the 48x48 minimum"
            except Exception as exc:  # unreadable image
                return f"could not be read: {exc}"
        else:
            head = path.read_text(encoding="utf-8", errors="replace")[:2000]
            if "viewBox" not in head:
                return "SVG has no viewBox, so it has no defined square size"
        return None

    for label, data in manifests.items():
        if not data:
            continue
        iface = data.get("interface")
        if iface is None:
            iface = (data.get("extensions", {}).get("com.openai", {}) or {}).get("interface")
        if not isinstance(iface, dict):
            continue
        for field in ("logo", "composerIcon"):
            ref = iface.get(field)
            if not ref:
                r.fail(section, f"{label}: interface.{field} missing; Codex validation requires it")
                continue
            if not ref.startswith("./"):
                r.fail(section, f"{label}: interface.{field} must start with './', got {ref!r}")
                continue
            problem = check_image(ROOT / ref[2:])
            if problem:
                r.fail(section, f"{label}: interface.{field} -> {ref}: {problem}")
        for field in ("logoDark", "composerIconDark"):
            ref = iface.get(field)
            if ref and ref.startswith("./"):
                problem = check_image(ROOT / ref[2:])
                if problem:
                    r.fail(section, f"{label}: interface.{field} -> {ref}: {problem}")

    # Listing URLs the manifest advertises must resolve to a real file.
    for label, data in manifests.items():
        if not data:
            continue
        iface = data.get("interface") or (data.get("extensions", {}).get("com.openai", {}) or {}).get("interface")
        if not isinstance(iface, dict):
            continue
        for field in ("privacyPolicyURL", "termsOfServiceURL", "supportURL"):
            url = iface.get(field)
            if not url:
                continue
            if "github.com" in url and "/blob/" in url:
                name = url.rsplit("/", 1)[-1]
                if not (ROOT / name).is_file():
                    r.fail(section, f"{label}: interface.{field} points at {name}, which does not exist")

    if not any(lv == "FAIL" and sec == section for lv, sec, _ in r.rows):
        r.ok(section, "logo and composerIcon present, square, >=48x48, within size limit")


def check_examples(r: Report) -> None:
    """The worked example must stay consistent with the skills it demonstrates."""
    section = "Worked example"
    base = ROOT / "examples" / "salt-and-ember"
    if not base.is_dir():
        r.warn(section, "examples/salt-and-ember missing")
        return

    required = [
        "NOVEL_BIBLE.md", "PROJECT_SETTINGS.md", "README.md",
        "canon/facts.md", "canon/retcons.md", "canon/unresolved.md",
        "characters/CHARACTER.md", "characters/RELATIONSHIP.md",
        "power_system/POWER_SYSTEM.md", "obligations/INDEX.md",
        "mysteries/MYSTERY.md", "timeline/EVENT.md",
        "quality/FINDINGS.md", "quality-check.md",
        "context/BUDGET.md", "audit/AUDIT_RUN.md",
    ]
    missing = [f for f in required if not (base / f).is_file()]
    if missing:
        r.fail(section, f"example missing files: {missing}")
    else:
        r.ok(section, f"all {len(required)} example files present")

    # The example is a demonstration, not a second source of truth. It must not
    # contain skills, which would be picked up by the discovery symlinks.
    stray = sorted(p.name for p in (base / "skills").glob("*")) if (base / "skills").is_dir() else []
    if stray:
        r.fail(section, f"example contains a skills/ directory: {stray}")

    # Settings that the example claims must match the vocabulary the
    # project-settings skill defines.
    settings = (base / "PROJECT_SETTINGS.md")
    if settings.is_file():
        text = settings.read_text(encoding="utf-8")
        for level in ("strict", "standard", "permissive"):
            if f"`{level}`" not in text:
                r.warn(section, f"PROJECT_SETTINGS.md does not document the `{level}` level")
        if "UNRESOLVED" not in text:
            r.fail(section, "PROJECT_SETTINGS.md has no UNRESOLVED field; "
                            "an example must show unset decisions as unset")

    # The example advertises open questions; they must actually be marked open,
    # or the example teaches that leaving things undecided is carelessness.
    for rel in ("canon/unresolved.md", "mysteries/MYSTERY.md"):
        path = base / rel
        if path.is_file() and "UNRESOLVED" not in path.read_text(encoding="utf-8"):
            r.warn(section, f"{rel} records open questions but never marks them UNRESOLVED")


def check_catalog(r: Report) -> None:
    """The OpenCode HTTP catalog must match the canonical skills."""
    section = "OpenCode catalog"
    script = ROOT / "scripts" / "build_catalog.py"
    if not script.is_file():
        r.warn(section, "scripts/build_catalog.py missing; catalog not verified")
        return
    import subprocess
    try:
        result = subprocess.run(
            [sys.executable, str(script), "--check"],
            capture_output=True, text=True, timeout=60, cwd=str(ROOT),
        )
    except (OSError, subprocess.SubprocessError) as exc:
        r.warn(section, f"could not run catalog check ({exc})")
        return
    if result.returncode == 0:
        r.ok(section, result.stdout.strip() or "catalog is up to date")
    else:
        detail = (result.stderr or result.stdout).strip().splitlines()
        r.fail(section, detail[0] if detail else "catalog check failed")


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
    check_routing(report, skills)
    check_references(report, skills, templates)
    manifests = check_manifests(report)
    check_version_agreement(report, manifests, skills)
    if args.schema:
        check_schema(report, manifests)
    check_license(report, manifests)
    check_openai_listing(report, manifests)
    check_icons(report, manifests)
    check_language(report, skills, templates)
    check_no_stale_version_labels(report, skills)
    check_examples(report)
    check_catalog(report)

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
