# Repository Guidelines

## Project Structure & Module Organization
This repository is a registry of agent skills, not a single application. Most top-level directories are Git submodules, including `agent-workflow-audit/`, `odds-api-io/`, `tfl-journey-disruption/`, and `sentry-cli/`. Each skill usually keeps its implementation at `submodule-name/skills/<skill-name>/SKILL.md`, for example `agent-workflow-audit/skills/agent-workflow-audit/SKILL.md`.

The root `README.md` is the catalog of included skills. Submodule mappings live in `.gitmodules`.

Use `RELEASING.md` as the checklist when adding or editing a skill, marketplace entry, or plugin release metadata.

## Build, Test, and Development Commands
There is no repo-wide build or test pipeline at the root. The core maintenance commands are:

- `git submodule update --init --recursive` to fetch all skills after clone.
- `git submodule status` to verify pinned submodule SHAs.
- `git status --short` to review root changes before committing.

Run skill-specific checks from inside the relevant submodule when that project defines them.

## Coding Style & Naming Conventions
Keep new skill directories and skill identifiers in hyphen-case, such as `my-new-skill`. Match the directory name to the `name` field in `SKILL.md`. Use Markdown for documentation, concise imperative prose, and short sections optimized for agent consumption.

## Testing Guidelines
Validation is lightweight and primarily document-driven. For new or edited skills, run `quick_validate.py` against the skill folder and confirm examples, paths, and referenced scripts still resolve. At the root of this registry, there is no need to validate or run the scripts inside the individual skill repos themselves. If a submodule has its own tests or linters, run them in that submodule only when you are intentionally changing that submodule and updating its pinned commit here.

## Commit & Pull Request Guidelines
Recent history uses short, imperative commit subjects such as `Convert sentry-cli to submodule and update README` and `add pr-comments-triage`. Keep subjects specific to one change. For pull requests, include:

- a brief summary of the skill added or updated
- any submodule additions or SHA bumps
- matching `README.md` updates when the catalog changes
- linked issues or upstream repos when relevant

## Security & Configuration Tips
Do not commit secrets, API keys, or local config files. Skills that integrate with external services should document environment variables in their own repo or `SKILL.md`, not store credentials here.

## Memory

At the start of any task, run `gn help plan` and follow its instructions.
After finishing a task, run `gn help review`.
