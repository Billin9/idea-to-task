<!-- GSD:project-start source:PROJECT.md -->
## Project

**idea-to-task Skill 输出质量优化**

对现有 idea-to-task skill 的输出质量进行定向优化。这个 skill 把 CEO 的碎片想法整理成结构化任务树，当前问题是输出缺乏「向上归纳」能力——会把本该是父子关系的任务平铺成并列主题，核心判断也直接铺主线而不是先抓住统一的顶层意图。优化目标是让 skill 在输出时先找到一个统一的顶层意图，再向下展开子任务线。

**Core Value:** 输出必须先归纳出 CEO 真正想做的那一件事，再往下展开，而不是一上来就横向铺开。

### Constraints

- **范围**: 只修改 skills/idea-to-task/ 目录下的四个文件，不改目录结构
- **兼容**: 优化不能破坏现有的非战略型输入处理逻辑
- **风格**: 代码注释和输出内容必须使用中文
<!-- GSD:project-end -->

<!-- GSD:stack-start source:codebase/STACK.md -->
## Technology Stack

## Languages
- Python 3.x - Skill validation script (`skills/idea-to-task/scripts/validate_skill.py`)
- Markdown - All skill definition, reference, and fixture content
- YAML - OpenAI agent interface definition (`skills/idea-to-task/agents/openai.yaml`)
- JavaScript (CommonJS) - GSD framework hooks and tooling (`.agent/hooks/*.js`, `.agent/get-shit-done/bin/gsd-tools.cjs`)
- Shell (bash) - GSD lifecycle hooks (`.agent/hooks/*.sh`)
- TOML - Codex agent configuration (`.codex/config.toml`, `.codex/agents/*.toml`)
## Runtime
- Python: `uv` runtime via PEP 723 inline script metadata
- JavaScript: Node.js (CommonJS, no package.json dependencies beyond `{"type":"commonjs"}`)
- Python: `uv` — script dependencies declared inline in `validate_skill.py`
- Lockfile: Not present (inline metadata only, no `uv.lock`)
## Frameworks
- None — this is a prompt-engineering skill package, not a software application
- Python standard library + `pyyaml<7` (declared in `validate_skill.py` inline metadata)
- GSD (get-shit-done) framework v1.34.2 — agent orchestration, hooks, workflow runner
## Key Dependencies
- `pyyaml<7` - YAML frontmatter parsing in skill validator (`skills/idea-to-task/scripts/validate_skill.py`)
- GSD framework v1.34.2 - Multi-platform agent framework (Claude, Codex, generic `.agent`)
- Node.js - Required for GSD hooks execution at session start and tool boundaries
## Configuration
- No `.env` files detected
- No secrets or API keys required for the skill itself
- GSD settings declared in `.agent/settings.json` and `.codex/config.toml`
- No build step required
- Skill validation: `uv run skills/idea-to-task/scripts/validate_skill.py <skill_dir> [--strict]`
## Platform Requirements
- `uv` for running `validate_skill.py`
- Node.js for GSD hooks
- Git (project is a git repository)
- Skill is consumed by AI agents (Claude, OpenAI Codex) — no server deployment required
- Platform adapters present: `.agent/` (generic), `.claude/` (Claude Code), `.codex/` (OpenAI Codex)
<!-- GSD:stack-end -->

<!-- GSD:conventions-start source:CONVENTIONS.md -->
## Conventions

## Overview
## File Naming Patterns
- Skill root directory uses `kebab-case`: `skills/idea-to-task/`
- Main skill definition file is always `SKILL.md` (UPPERCASE)
- Reference documents use `kebab-case.md`: `decision-rules.md`, `output-template.md`, `examples.md`
- Agent definition files use `kebab-case` with `gsd-` prefix: `gsd-codebase-mapper.md`, `gsd-executor.md`
- Hook scripts use `kebab-case` with `gsd-` prefix: `gsd-validate-commit.sh`, `gsd-workflow-guard.js`
- Fixture files use zero-padded numeric prefix + descriptive name: `01-clear-direction.md`, `02-mixed-topics.md`, `03-high-risk-ambiguity.md`
- Use `snake_case`: `validate_skill.py`
- Design/spec docs use date prefix + topic: `2026-04-11-idea-to-task-design.md`
## Markdown Document Structure
- `## 适用场景`
- `## 核心原则`
- `## 工作流`
- `## 补问规则`
- `## 输出结构`
## Language Conventions
- All `.md` content: Chinese (中文), including headings, body, and explanations
- YAML `name` and `description` fields: English
- `openai.yaml` display fields: English
- Python source code: English identifiers, Chinese string literals and error messages
- Shell/JS hook code: English comments in file headers, Chinese in user-facing error messages
- Imperative and prescriptive ("先给结论", "不暴露内部推理")
- No hedging language in rule documents
- Numbered lists for ordered steps, bullet lists for unordered rules
## Python Code Style
#!/usr/bin/env -S uv run
- Pure functions with explicit return types
- Validation functions return `list[str]` (error messages), not raise exceptions
- `main()` returns `int` exit code, called via `raise SystemExit(main())`
## YAML Conventions
## Skill Directory Layout Convention
## Output / Behavior Conventions (Skill Instructions)
- Six-section fixed structure: 核心判断 → 主题拆分 → 分层任务树 → 执行建议 → 风险与高风险推断 → 下一步动作
- Short sentences preferred
- No `<thinking>` tags or meta-commentary in output
- Default to producing output; only ask follow-up questions when ambiguity would fundamentally change task direction
- Follow-up question count: 2–5 maximum
- Task depth governed by evidence strength: weak → project level only; medium → milestone level; strong → execution item level
## Git Conventions
- Subject line ≤ 72 characters
- Lowercase, imperative mood, no trailing period
## Comments
<!-- GSD:conventions-end -->

<!-- GSD:architecture-start source:ARCHITECTURE.md -->
## Architecture

## Pattern Overview
- This is not a traditional software application — it is a collection of AI agent skills, workflow definitions, and prompt templates that run inside an LLM runtime (Claude Code, OpenAI, Codex)
- The primary "code" is Markdown instruction files consumed by LLMs as system prompts
- A thin JavaScript runtime (`gsd-tools.cjs`) handles file I/O, state management, and context assembly
- Skills are self-contained prompt bundles: a `SKILL.md` entry point referencing `references/` documents loaded on demand
- The GSD (Get-Shit-Done) framework is a versioned sub-system installed at `.agent/get-shit-done/`, `.claude/get-shit-done/`, and `.codex/get-shit-done/` for different runtimes
## Layers
- Purpose: Domain-specific behavior definition for a single capability (e.g., idea-to-task)
- Location: `skills/<skill-name>/`
- Contains: `SKILL.md` (main prompt), `agents/` (platform-specific UI metadata), `references/` (lazy-loaded sub-documents), `scripts/` (validation utilities)
- Depends on: Nothing at runtime — self-contained prompt bundle
- Used by: LLM runtime when user invokes the skill
- Purpose: Orchestration engine for project management workflows (plan, execute, verify phases)
- Location: `.agent/get-shit-done/`, `.claude/get-shit-done/`, `.codex/get-shit-done/`
- Contains: `bin/` (JS CLI tools), `workflows/` (orchestrator prompts), `agents/` (subagent definitions), `references/` (shared knowledge), `templates/` (project scaffolding), `contexts/` (agent context presets)
- Depends on: Node.js runtime for `gsd-tools.cjs`
- Used by: Claude Code commands in `.claude/commands/gsd/`
- Purpose: State management, context assembly, config resolution
- Location: `.agent/get-shit-done/bin/gsd-tools.cjs` (main entry), `.agent/get-shit-done/bin/lib/` (modules)
- Contains: `core.cjs`, `state.cjs`, `phase.cjs`, `milestone.cjs`, `roadmap.cjs`, `template.cjs`, `config.cjs`, `intel.cjs`, `verify.cjs`, and others
- Depends on: Node.js, `pyyaml` (Python scripts only)
- Used by: Workflow `.md` files via `node ".agent/get-shit-done/bin/gsd-tools.cjs" <command> <args>`
- Purpose: Maps user slash-commands to workflow execution
- Location: `.claude/commands/gsd/` (Claude Code), `.agent/skills/gsd-*/` (generic agent runtime), `.codex/skills/gsd-*/` (Codex runtime)
- Contains: One `.md` file per command (e.g., `execute-phase.md`, `plan-phase.md`)
- Depends on: GSD Framework Layer
- Used by: LLM runtime command invocation
- Purpose: Structural validation of skill correctness
- Location: `skills/<skill-name>/scripts/`, `tests/fixtures/<skill-name>/`
- Contains: Python validation script (`validate_skill.py`), fixture `.md` files describing input/expected behavior
- Depends on: `uv`, `pyyaml`
- Used by: Developers verifying skill structure before publishing
## Data Flow
- Project state is persisted in filesystem files (`STATE.md`, `ROADMAP.md`, `PLAN.md`, `SUMMARY.md`, `CONTEXT.md`)
- `gsd-tools.cjs` reads/writes these files and emits JSON context for workflows
- No in-memory or database state — all state is git-tracked Markdown
## Key Abstractions
- Purpose: A self-contained, single-purpose prompt bundle that teaches the LLM a specific behavior
- Examples: `skills/idea-to-task/SKILL.md`
- Pattern: YAML frontmatter (`name`, `description`) + Markdown sections (`适用场景`, `核心原则`, `工作流`, `补问规则`, `输出结构`) + inline references to `references/*.md`
- Purpose: An orchestrator prompt defining how an LLM should coordinate multi-step, multi-agent tasks
- Examples: `.agent/get-shit-done/workflows/execute-phase.md`, `.agent/get-shit-done/workflows/plan-phase.md`
- Pattern: XML-tagged sections (`<purpose>`, `<required_reading>`, `<process>`) with bash snippets calling `gsd-tools.cjs`
- Purpose: A detailed system prompt defining a specialized subagent's responsibilities, tools, and behavior
- Examples: `.agent/agents/gsd-executor.md`, `.agent/agents/gsd-planner.md`, `.agent/agents/gsd-codebase-mapper.md`
- Pattern: Long-form Markdown system prompt, invoked via `Task(subagent_type="<name>", ...)`
- Purpose: Supplementary knowledge loaded on demand within a skill or workflow
- Examples: `skills/idea-to-task/references/decision-rules.md`, `skills/idea-to-task/references/output-template.md`
- Pattern: Short, focused Markdown — loaded only when the LLM needs to resolve a specific decision
- Purpose: Behavioral test case defining input + expected output behavior for a skill
- Examples: `tests/fixtures/idea-to-task/01-clear-direction.md`, `02-mixed-topics.md`, `03-high-risk-ambiguity.md`
- Pattern: `## 输入` section with raw input, `## 期望行为` section with bullet-list expected behaviors
## Entry Points
- Location: `skills/idea-to-task/SKILL.md`
- Triggers: LLM runtime loads this when user invokes the `idea-to-task` skill
- Responsibilities: Defines the complete behavior contract for turning messy CEO notes into structured task trees
- Location: `skills/idea-to-task/agents/openai.yaml`
- Triggers: OpenAI platform reads this for UI display metadata
- Responsibilities: Provides `display_name`, `short_description`, `default_prompt` for platform integration
- Location: `.agent/skills/gsd-<command-name>/SKILL.md`
- Triggers: Generic agent runtime invokes this per command
- Responsibilities: Routes to the appropriate GSD workflow
- Location: `.claude/commands/gsd/<command>.md`
- Triggers: Claude Code slash-command invocation (e.g., `/gsd-execute-phase`)
- Responsibilities: Bootstraps workflow execution with runtime-specific context
- Location: `skills/idea-to-task/scripts/validate_skill.py`
- Triggers: `uv run validate_skill.py <skill_dir> [--strict]`
- Responsibilities: Validates SKILL.md frontmatter, required sections, referenced file existence; in `--strict` mode also checks `agents/openai.yaml` and test fixtures
## Error Handling
- Workflow files specify fallback behavior when subagent spawning fails (sequential inline execution)
- `validate_skill.py` returns a list of validation errors with non-zero exit code
- LLM workflows instruct the orchestrator to verify completion via filesystem/git state rather than relying on completion signals
- Ambiguous skill inputs are handled by explicit dual-path output rules rather than errors
## Cross-Cutting Concerns
<!-- GSD:architecture-end -->

<!-- GSD:skills-start source:skills/ -->
## Project Skills

No project skills found. Add skills to any of: `.claude/skills/`, `.agents/skills/`, `.cursor/skills/`, or `.github/skills/` with a `SKILL.md` index file.
<!-- GSD:skills-end -->

<!-- GSD:workflow-start source:GSD defaults -->
## GSD Workflow Enforcement

Before using Edit, Write, or other file-changing tools, start work through a GSD command so planning artifacts and execution context stay in sync.

Use these entry points:
- `/gsd-quick` for small fixes, doc updates, and ad-hoc tasks
- `/gsd-debug` for investigation and bug fixing
- `/gsd-execute-phase` for planned phase work

Do not make direct repo edits outside a GSD workflow unless the user explicitly asks to bypass it.
<!-- GSD:workflow-end -->



<!-- GSD:profile-start -->
## Developer Profile

> Profile not yet configured. Run `/gsd-profile-user` to generate your developer profile.
> This section is managed by `generate-claude-profile` -- do not edit manually.
<!-- GSD:profile-end -->
