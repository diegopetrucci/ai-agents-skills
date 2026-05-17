# Releasing Skills

Use this checklist when adding a new skill, updating an existing skill, or changing Claude/Codex plugin metadata.

## Skill Content

- Keep skill names and directories in hyphen-case.
- Ensure every `skills/<skill-name>/SKILL.md` starts with frontmatter containing at least `name` and `description`.
- Match the frontmatter `name` to the skill directory name.
- Document required environment variables in the skill repo; do not store secrets or local config.
- Run the local validator against every changed skill:

```bash
python3 <skill-creator>/scripts/quick_validate.py <submodule>/skills/<skill-name>
```

## Registry Updates

- Add or update the submodule entry in `.gitmodules`.
- Update `README.md` whenever a skill is added, removed, renamed, or materially repositioned.
- Do not list unfinished skills in marketplaces. A skill can stay as a submodule without being offered as a Claude or Codex plugin.
- Run `git submodule status` and confirm the pinned SHA is intentional.

## Codex Plugin Checklist

- Include `.codex-plugin/plugin.json` in any repo that is ready for Codex plugin installation.
- Keep the plugin `name` aligned with the marketplace entry name.
- Keep `skills` as `./skills/` when the repo exposes skills from the standard root folder.
- Populate `interface.displayName`, `interface.shortDescription`, `interface.developerName`, and `interface.category`.
- Add or update `.agents/plugins/marketplace.json` only when the plugin is ready for Codex users.
- Marketplace entries must include `policy.installation`, `policy.authentication`, and `category`.
- Smoke-test marketplace parsing with a temporary Codex home:

```bash
tmp_home=$(mktemp -d)
mkdir -p "$tmp_home/.codex"
CODEX_HOME="$tmp_home/.codex" HOME="$tmp_home" codex plugin marketplace add "$(pwd)"
rc=$?
rm -rf "$tmp_home"
exit "$rc"
```

## Claude Plugin Checklist

- Include `.claude-plugin/plugin.json` in any repo that is ready for Claude plugin installation.
- Add or update `.claude-plugin/marketplace.json` when a Claude-ready plugin should be discoverable.
- Keep `source.repo` pointed at the skill repo, not this registry repo.
- If `plugin.json` includes a `version`, bump it for every released plugin change. Claude uses explicit versions for update resolution.
- After bumping a Claude plugin version, create the matching release tag with:

```bash
claude plugin tag <submodule>
```

- Validate the marketplace and changed plugins before release:

```bash
claude plugin validate .
claude plugin validate <submodule>
```

## Commit Checklist

- Review `git diff --stat` and `git diff --submodule`.
- Keep commits scoped to one registry change.
- Use short imperative commit subjects, for example `Add prd-interviewer to Claude marketplace`.
- Push only after validation passes.
