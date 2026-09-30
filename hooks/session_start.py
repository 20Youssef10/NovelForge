#!/usr/bin/env python3
"""
SessionStart hook for NovelForge.

Runs when a supported agent opens a session and, if the working directory is
part of a NovelForge project, emits a short context block describing where the
novel stands. This is what makes cross-session continuity real rather than
aspirational: the agent learns the project position without being told.

Never fails a session. If anything at all goes wrong it exits 0 silently,
because a broken context hook must never block the author's work.

Hook protocol: expects a JSON event on stdin. Emits plain text on stdout, which
the host injects as session context. Supports the ${PLUGIN_ROOT} convention used
by both Codex and Claude Code.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

MARKER = "NOVEL_BIBLE.md"
MAX_LIST = 8


def find_project(start: Path) -> Path | None:
    """Walk upward looking for a project root containing NOVEL_BIBLE.md."""
    for candidate in [start, *start.parents]:
        if (candidate / MARKER).is_file():
            return candidate
    return None


def read_text(path: Path, limit: int = 2000) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")[:limit]
    except OSError:
        return ""


def is_placeholder(value: str | None) -> bool:
    """Reject unfilled template values.

    An empty project template contains values like 'PLANNING / DRAFTING /
    REVISING / COMPLETE' and 'MAIN / branch name'. Reporting those as if they
    were real would be worse than reporting nothing, so treat anything with a
    slash-separated option list, or that reads as an unfilled placeholder, as
    absent.
    """
    if value is None:
        return True
    text = value.strip()
    if not text or text.endswith("..."):
        return True
    lowered = text.lower()
    if lowered in {"tbc", "todo", "n/a", "none", "unset", "branch name", "id"}:
        return True
    # An unfilled option list looks like 'MAIN / branch name' or
    # 'PLANNING / DRAFTING / REVISING / COMPLETE'. Real values rarely contain a
    # spaced slash with uniformly short segments, so require both.
    if " / " in text:
        segments = [s.strip() for s in text.split(" / ")]
        if len(segments) >= 2 and all(len(s) <= 30 for s in segments):
            return True
    if lowered.startswith(("see ", "path:", "id:")):
        return True
    return False


def read_value(text: str, key: str) -> str | None:
    """Pull a '- Key: value' or 'Key: value' value, ignoring placeholders."""
    for line in text.splitlines():
        stripped = line.strip().lstrip("-").strip()
        if stripped.lower().startswith(key.lower() + ":"):
            value = stripped.split(":", 1)[1].strip()
            return None if is_placeholder(value) else value
    return None


def count_lines(path: Path, pattern: str) -> int:
    if not path.is_file():
        return 0
    try:
        return sum(1 for line in path.read_text(encoding="utf-8", errors="replace").splitlines()
                   if line.strip().startswith(pattern))
    except OSError:
        return 0


def parse_frontmatter_field(text: str, field: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 3)
    if end == -1:
        return None
    for line in text[4:end].splitlines():
        if line.lower().startswith(field.lower() + ":"):
            return line.split(":", 1)[1].strip()
    return None


def main() -> int:
    try:
        # Consume the event without requiring a particular shape.
        try:
            json.loads(sys.stdin.read() or "{}")
        except (json.JSONDecodeError, ValueError):
            pass

        cwd = Path(os.environ.get("NF_PROJECT_DIR") or os.getcwd()).resolve()
        project = find_project(cwd)
        if project is None:
            return 0

        bible = read_text(project / MARKER)
        if not bible:
            return 0

        title = read_value(bible, "Title") or project.name
        status = read_value(bible, "Status")
        branch = read_value(bible, "Canon branch")
        pov = read_value(bible, "POV model")
        tense = read_value(bible, "Tense")

        obligations = count_lines(project / "obligations" / "INDEX.md", "| F-") + \
            count_lines(project / "obligations" / "OBLIGATION.md", "- ID:")

        lines = [
            "",
            "## NovelForge project detected",
            "",
            f"Project root: `{project}`",
            f"Novel: **{title}**",
        ]
        if status:
            lines.append(f"Status: {status}")
        if branch:
            lines.append(f"Canon branch: {branch}")
        if pov or tense:
            lines.append(f"POV / tense: {pov or 'unstated'} / {tense or 'unstated'}")

        series = project / "series" / "BOOK.md"
        if series.is_file():
            order = read_value(read_text(series), "Book order")
            if order:
                lines.append(f"Series volume: {order}")

        findings = project / "quality" / "FINDINGS.md"
        if findings.is_file():
            ftext = read_text(findings, 4000)
            open_rows = sum(1 for line in ftext.splitlines()
                            if line.strip().startswith("| F-") and "Critical" in line)
            if open_rows:
                lines.append(f"Open Critical findings: {open_rows} (see `quality/FINDINGS.md`)")

        lines += [
            "",
            f"Open narrative obligations: {obligations} (see `obligations/INDEX.md`)",
            "",
            "Load `novel-orchestrator` before acting, and `context-manager` for any multi-file task. "
            "Resolve WORKSPACE, NOVEL, and BRANCH before reading or writing. Project files are canonical; "
            "memory never overrides them. HIGH-risk changes need author approval before execution.",
            "",
        ]

        sys.stdout.write("\n".join(lines))
        return 0
    except Exception:
        # A context hook must never break a session.
        return 0


if __name__ == "__main__":
    sys.exit(main())
