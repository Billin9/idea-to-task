# External Integrations

**Analysis Date:** 2026-04-12

## APIs & External Services

**AI Agent Platforms:**
- Claude Code (Anthropic) - Skill consumed via `.claude/` directory structure
  - SDK/Client: Claude Code agent runner
  - Auth: Handled by the Claude Code environment; no key managed in this repo
  - Agents registered in: `.claude/agents/*.md`
  - Commands registered in: `.claude/commands/gsd/`

- OpenAI Codex - Skill consumed via `.codex/` directory structure
  - SDK/Client: Codex agent runner
  - Auth: Handled by Codex environment; no key managed in this repo
  - Agent interface defined in: `skills/idea-to-task/agents/openai.yaml`
  - Agents registered in: `.codex/agents/*.md` + `.codex/agents/*.toml`
  - Config: `.codex/config.toml`

- Generic Agent Runtime - Skill consumed via `.agent/` directory structure
  - Agents registered in: `.agent/agents/*.md`
  - Settings: `.agent/settings.json`

## Data Storage

**Databases:**
- None - No database used. All state is file-based (Markdown files in `.planning/`)

**File Storage:**
- Local filesystem only
  - Planning artifacts: `.planning/`
  - Skill definitions: `skills/`
  - Test fixtures: `tests/fixtures/`

**Caching:**
- None

## Authentication & Identity

**Auth Provider:**
- None — this is a skill/prompt package, not a web application
- All auth is delegated to the consuming AI platform (Claude, Codex)

## Monitoring & Observability

**Error Tracking:**
- None

**Logs:**
- GSD hooks produce session state via `.agent/hooks/gsd-session-state.sh`
- Context monitoring via `.agent/hooks/gsd-context-monitor.js` (fires after Bash/Edit/Write/Agent tool calls)
- Update check via `.agent/hooks/gsd-check-update.js` (fires at SessionStart)

## CI/CD & Deployment

**Hosting:**
- Not applicable — skill package distributed via git repository

**CI Pipeline:**
- None detected (no `.github/`, no CI config files)

**Skill Validation (manual):**
- Run `uv run skills/idea-to-task/scripts/validate_skill.py skills/idea-to-task` for basic checks
- Run with `--strict` flag for additional checks (requires `agents/openai.yaml` and 3+ test fixtures)

## Environment Configuration

**Required env vars:**
- None — no environment variables required

**Secrets location:**
- No secrets present in repository

## Webhooks & Callbacks

**Incoming:**
- None

**Outgoing:**
- GSD framework checks for updates at session start via `.agent/hooks/gsd-check-update.js`
  - Likely calls a remote version endpoint to compare against local `VERSION` file (v1.34.2)

---

*Integration audit: 2026-04-12*
