# AI agents' skills

Skills I tend to use.

### Skills I created

- [Agent workflow audit](https://github.com/diegopetrucci/agent-workflow-audit): stress-test a repo's agent-facing workflow and report where instructions, commands, or context are wasteful, ambiguous, or missing
- [iOS](https://github.com/diegopetrucci/ios-agents-skills): skills for developing on Apple platforms
- [Odds API](https://github.com/diegopetrucci/odds-api-io): I do not personally bet, but odds are a good way to gauge the likelihood of something happening
- [PRD interviewer](https://github.com/diegopetrucci/prd-interviewer): builds a detailed PRD through a focused, one-question-at-a-time interview
- [PR comments triage](https://github.com/diegopetrucci/pr-comments-triage): critically evaluate PR review comments against actual code, investigating each for validity before implementing
- [Remove AI code slop](https://github.com/diegopetrucci/remove-ai-code-slop): scans your branch's diff and removes telltale signs of AI-generated code
- [Starting from scratch](https://github.com/diegopetrucci/starting-from-scratch): reviews a codebase and says what should change if you were starting again from scratch
- [Sentry CLI](https://github.com/diegopetrucci/sentry-cli): giving agents tools to interface with Sentry's error reporting
- [Tfl-journey-disruption](https://github.com/diegopetrucci/tfl-journey-disruption): used with personal agents to be notified of delays in London

### Skills from 3rd parties
- [Skills creator](https://github.com/diegopetrucci/ai-agents-skills/tree/main/skill-creator): Anthropic's skill to create ad-hoc skills. [Source](https://github.com/anthropics/skills/tree/main/skills/skill-creator)
- [Visual explainer](https://github.com/nicobailon/visual-explainer/): fantastic tool to visualise repos, changes, and flows

## Installation

### As skills

```bash
npx skills add https://github.com/diegopetrucci/pr-comments-triage --skill pr-comments-triage
npx skills add https://github.com/diegopetrucci/agent-workflow-audit --skill agent-workflow-audit
npx skills add https://github.com/diegopetrucci/odds-api-io --skill odds-api-io
npx skills add https://github.com/diegopetrucci/tfl-journey-disruption --skill tfl-journey-disruption
npx skills add https://github.com/diegopetrucci/sentry-cli --skill sentry-cli
npx skills add https://github.com/diegopetrucci/prd-interviewer --skill prd-interviewer
npx skills add https://github.com/diegopetrucci/remove-ai-code-slop --skill remove-ai-code-slop
npx skills add https://github.com/diegopetrucci/starting-from-scratch --skill starting-from-scratch
```

### As Claude Code plugins

This repo is a [Claude Code plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces). Add it once, then install whichever plugins you want:

```shell
/plugin marketplace add diegopetrucci/ai-agents-skills
/plugin install pr-comments-triage@diegopetrucci-claude-plugins
```

Available plugins:
- `agent-workflow-audit`
- `odds-api-io`
- `pr-comments-triage`
- `prd-interviewer`
- `remove-ai-code-slop`
- `sentry-cli`
- `starting-from-scratch`
- `tfl-journey-disruption`
