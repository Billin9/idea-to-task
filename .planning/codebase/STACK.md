# Technology Stack

**Analysis Date:** 2026-04-12

## Languages

**Primary:**
- Python 3.x - Skill validation script (`skills/idea-to-task/scripts/validate_skill.py`)
- Markdown - All skill definition, reference, and fixture content
- YAML - OpenAI agent interface definition (`skills/idea-to-task/agents/openai.yaml`)

**Secondary:**
- JavaScript (CommonJS) - GSD framework hooks and tooling (`.agent/hooks/*.js`, `.agent/get-shit-done/bin/gsd-tools.cjs`)
- Shell (bash) - GSD lifecycle hooks (`.agent/hooks/*.sh`)
- TOML - Codex agent configuration (`.codex/config.toml`, `.codex/agents/*.toml`)

## Runtime

**Environment:**
- Python: `uv` runtime via PEP 723 inline script metadata
- JavaScript: Node.js (CommonJS, no package.json dependencies beyond `{"type":"commonjs"}`)

**Package Manager:**
- Python: `uv` — script dependencies declared inline in `validate_skill.py`
- Lockfile: Not present (inline metadata only, no `uv.lock`)

## Frameworks

**Core:**
- None — this is a prompt-engineering skill package, not a software application

**Validation:**
- Python standard library + `pyyaml<7` (declared in `validate_skill.py` inline metadata)

**Build/Dev:**
- GSD (get-shit-done) framework v1.34.2 — agent orchestration, hooks, workflow runner
  - Installed at `.agent/get-shit-done/`, `.claude/get-shit-done/`, `.codex/get-shit-done/`

## Key Dependencies

**Critical:**
- `pyyaml<7` - YAML frontmatter parsing in skill validator (`skills/idea-to-task/scripts/validate_skill.py`)

**Infrastructure:**
- GSD framework v1.34.2 - Multi-platform agent framework (Claude, Codex, generic `.agent`)
- Node.js - Required for GSD hooks execution at session start and tool boundaries

## Configuration

**Environment:**
- No `.env` files detected
- No secrets or API keys required for the skill itself
- GSD settings declared in `.agent/settings.json` and `.codex/config.toml`

**Build:**
- No build step required
- Skill validation: `uv run skills/idea-to-task/scripts/validate_skill.py <skill_dir> [--strict]`

## Platform Requirements

**Development:**
- `uv` for running `validate_skill.py`
- Node.js for GSD hooks
- Git (project is a git repository)

**Production:**
- Skill is consumed by AI agents (Claude, OpenAI Codex) — no server deployment required
- Platform adapters present: `.agent/` (generic), `.claude/` (Claude Code), `.codex/` (OpenAI Codex)

---

*Stack analysis: 2026-04-12*
