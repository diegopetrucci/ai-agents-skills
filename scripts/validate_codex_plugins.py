#!/usr/bin/env python3
"""Validate Codex plugin manifests and the root marketplace."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"

LOCAL_PLUGIN_DIRS = {
    "agent-workflow-audit": ROOT / "agent-workflow-audit",
    "github-librarian": ROOT / "github-librarian",
    "ios-agents-skills": ROOT / "ios",
    "odds-api-io": ROOT / "odds-api-io",
    "pr-comments-triage": ROOT / "pr-comments-triage",
    "prd-interviewer": ROOT / "prd-interviewer",
    "remove-ai-code-slop": ROOT / "remove-ai-code-slop",
    "sentry-cli": ROOT / "sentry-cli",
    "starting-from-scratch": ROOT / "starting-from-scratch",
    "tfl-journey-disruption": ROOT / "tfl-journey-disruption",
}

REQUIRED_POLICY = {
    "installation": {"AVAILABLE", "INSTALLED_BY_DEFAULT", "NOT_AVAILABLE"},
    "authentication": {"ON_INSTALL", "ON_USE"},
}


def load_json(path: Path) -> dict:
    try:
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        fail(f"missing file: {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate_manifest(plugin_name: str, plugin_dir: Path) -> dict:
    manifest_path = plugin_dir / ".codex-plugin" / "plugin.json"
    manifest = load_json(manifest_path)

    for field in ("name", "version", "description", "skills", "interface"):
        if field not in manifest:
            fail(f"{plugin_name}: manifest missing {field}")

    if manifest["name"] != plugin_name:
        fail(f"{plugin_name}: manifest name is {manifest['name']!r}")

    if manifest["skills"] != "./skills/":
        fail(f"{plugin_name}: manifest skills must be ./skills/")

    skills_dir = plugin_dir / "skills"
    if not skills_dir.is_dir():
        fail(f"{plugin_name}: missing skills directory")

    if not list(skills_dir.glob("*/SKILL.md")):
        fail(f"{plugin_name}: missing skills/*/SKILL.md")

    interface = manifest["interface"]
    for field in ("displayName", "shortDescription", "developerName", "category"):
        if field not in interface:
            fail(f"{plugin_name}: interface missing {field}")

    return manifest


def validate_marketplace(manifests: dict[str, dict]) -> None:
    marketplace = load_json(MARKETPLACE)

    for field in ("name", "interface", "plugins"):
        if field not in marketplace:
            fail(f"marketplace missing {field}")

    display_name = marketplace["interface"].get("displayName")
    if not display_name:
        fail("marketplace missing interface.displayName")

    plugins = marketplace["plugins"]
    if not isinstance(plugins, list) or not plugins:
        fail("marketplace plugins must be a non-empty list")

    seen = set()
    expected = set(LOCAL_PLUGIN_DIRS)

    for entry in plugins:
        name = entry.get("name")
        if not name:
            fail("marketplace entry missing name")
        if name in seen:
            fail(f"{name}: duplicate marketplace entry")
        seen.add(name)
        if name not in expected:
            fail(f"{name}: marketplace entry has no local plugin mapping")

        source = entry.get("source")
        if not isinstance(source, dict):
            fail(f"{name}: source must be an object")
        if source.get("source") not in {"url", "git-subdir", "local"}:
            fail(f"{name}: unsupported source type {source.get('source')!r}")
        if source.get("source") == "url":
            if not source.get("url"):
                fail(f"{name}: url source missing url")
            if source.get("ref") != "main":
                fail(f"{name}: url source should pin ref main")

        policy = entry.get("policy")
        if not isinstance(policy, dict):
            fail(f"{name}: policy must be an object")
        for field, allowed in REQUIRED_POLICY.items():
            value = policy.get(field)
            if value not in allowed:
                fail(f"{name}: invalid policy.{field} {value!r}")

        if not entry.get("category"):
            fail(f"{name}: missing category")

        manifest = manifests[name]
        if entry["category"] != manifest["interface"]["category"]:
            fail(f"{name}: marketplace category does not match manifest interface.category")

    missing = expected - seen
    if missing:
        fail(f"marketplace missing entries: {', '.join(sorted(missing))}")


def main() -> int:
    manifests = {
        name: validate_manifest(name, plugin_dir)
        for name, plugin_dir in LOCAL_PLUGIN_DIRS.items()
    }
    validate_marketplace(manifests)
    print(f"validated {len(manifests)} Codex plugins")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
