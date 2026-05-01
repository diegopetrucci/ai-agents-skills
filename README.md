# AI agents skills

A collection of agent skills I made:

- [Agent workflow audit](https://github.com/diegopetrucci/agent-workflow-audit): stress-test a repo's agent-facing workflow and report where instructions, commands, or context are wasteful, ambiguous, or missing
- [GitHub librarian](https://github.com/diegopetrucci/github-librarian): GitHub code research via `gh` that returns concise path-first findings with line-ranged evidence
- [iOS](https://github.com/diegopetrucci/ios-agents-skills): skills for developing on Apple platforms
- [Odds API](https://github.com/diegopetrucci/odds-api-io): I do not personally bet, but odds are a good way to gauge the likelihood of something happening
- [PR comments triage](https://github.com/diegopetrucci/pr-comments-triage): critically evaluate PR review comments against actual code, investigating each for validity before implementing
- [PRD interviewer](https://github.com/diegopetrucci/prd-interviewer): builds a detailed PRD through a focused, one-question-at-a-time interview
- [Remove AI code slop](https://github.com/diegopetrucci/remove-ai-code-slop): scans your branch's diff and removes telltale signs of AI-generated code
- [Sentry CLI](https://github.com/diegopetrucci/sentry-cli): giving agents tools to interface with Sentry's error reporting
- [Starting from scratch](https://github.com/diegopetrucci/starting-from-scratch): reviews a codebase and says what should change if you were starting again from scratch
- [Tfl-journey-disruption](https://github.com/diegopetrucci/tfl-journey-disruption): used with personal agents to be notified of delays in London

## Installation

### As skills

```bash
npx skills add https://github.com/diegopetrucci/agent-workflow-audit --skill agent-workflow-audit
```

Replace `agent-workflow-audit` with any of the above.

### As Claude Code plugins

Add this repo to the available marketplaces:

```bash
/plugin marketplace add diegopetrucci/ai-agents-skills
```

And then install your desired plugin, eg:

```bash
/plugin install agent-workflow-audit@diegopetrucci-claude-plugins
```

### As Codex plugins

Add this repo to Codex marketplaces:

```bash
codex plugin marketplace add diegopetrucci/ai-agents-skills
```

Restart Codex, then install plugins from the "Diego Petrucci Agent Skills" marketplace in the plugin directory.

## Validation

Validate the Codex marketplace and plugin manifests with:

```bash
python3 scripts/validate_codex_plugins.py
```
