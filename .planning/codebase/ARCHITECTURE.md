# Architecture

**Analysis Date:** 2026-04-12

## Pattern Overview

**Overall:** Skill-based prompt engineering framework with agent orchestration

**Key Characteristics:**
- This is not a traditional software application — it is a collection of AI agent skills, workflow definitions, and prompt templates that run inside an LLM runtime (Claude Code, OpenAI, Codex)
- The primary "code" is Markdown instruction files consumed by LLMs as system prompts
- A thin JavaScript runtime (`gsd-tools.cjs`) handles file I/O, state management, and context assembly
- Skills are self-contained prompt bundles: a `SKILL.md` entry point referencing `references/` documents loaded on demand
- The GSD (Get-Shit-Done) framework is a versioned sub-system installed at `.agent/get-shit-done/`, `.claude/get-shit-done/`, and `.codex/get-shit-done/` for different runtimes

## Layers

**Skill Layer:**
- Purpose: Domain-specific behavior definition for a single capability (e.g., idea-to-task)
- Location: `skills/<skill-name>/`
- Contains: `SKILL.md` (main prompt), `agents/` (platform-specific UI metadata), `references/` (lazy-loaded sub-documents), `scripts/` (validation utilities)
- Depends on: Nothing at runtime — self-contained prompt bundle
- Used by: LLM runtime when user invokes the skill

**GSD Framework Layer:**
- Purpose: Orchestration engine for project management workflows (plan, execute, verify phases)
- Location: `.agent/get-shit-done/`, `.claude/get-shit-done/`, `.codex/get-shit-done/`
- Contains: `bin/` (JS CLI tools), `workflows/` (orchestrator prompts), `agents/` (subagent definitions), `references/` (shared knowledge), `templates/` (project scaffolding), `contexts/` (agent context presets)
- Depends on: Node.js runtime for `gsd-tools.cjs`
- Used by: Claude Code commands in `.claude/commands/gsd/`

**CLI Tool Layer:**
- Purpose: State management, context assembly, config resolution
- Location: `.agent/get-shit-done/bin/gsd-tools.cjs` (main entry), `.agent/get-shit-done/bin/lib/` (modules)
- Contains: `core.cjs`, `state.cjs`, `phase.cjs`, `milestone.cjs`, `roadmap.cjs`, `template.cjs`, `config.cjs`, `intel.cjs`, `verify.cjs`, and others
- Depends on: Node.js, `pyyaml` (Python scripts only)
- Used by: Workflow `.md` files via `node ".agent/get-shit-done/bin/gsd-tools.cjs" <command> <args>`

**Command Dispatch Layer:**
- Purpose: Maps user slash-commands to workflow execution
- Location: `.claude/commands/gsd/` (Claude Code), `.agent/skills/gsd-*/` (generic agent runtime), `.codex/skills/gsd-*/` (Codex runtime)
- Contains: One `.md` file per command (e.g., `execute-phase.md`, `plan-phase.md`)
- Depends on: GSD Framework Layer
- Used by: LLM runtime command invocation

**Test / Validation Layer:**
- Purpose: Structural validation of skill correctness
- Location: `skills/<skill-name>/scripts/`, `tests/fixtures/<skill-name>/`
- Contains: Python validation script (`validate_skill.py`), fixture `.md` files describing input/expected behavior
- Depends on: `uv`, `pyyaml`
- Used by: Developers verifying skill structure before publishing

## Data Flow

**Skill Invocation Flow:**

1. User invokes skill (e.g., pastes CEO notes into chat with `idea-to-task` active)
2. LLM runtime loads `skills/idea-to-task/SKILL.md` as system prompt
3. LLM applies the workflow defined in SKILL.md (identify input type → judge topic density → assess taskability)
4. LLM optionally reads `references/decision-rules.md` to resolve ambiguity
5. LLM optionally reads `references/output-template.md` to stabilize output format
6. LLM produces structured output: core judgment → topic split → task tree → execution advice → risks → next actions

**GSD Phase Execution Flow:**

1. User runs `/gsd-execute-phase` command
2. Command `.md` file is loaded by Claude Code
3. Workflow calls `node ".agent/get-shit-done/bin/gsd-tools.cjs" init execute-phase "$PHASE"` to assemble context
4. Orchestrator reads `STATE.md` and referenced plan files
5. Orchestrator spawns `gsd-executor` subagents per plan (wave-based parallelism)
6. Each subagent executes tasks, commits changes, creates `SUMMARY.md`
7. Orchestrator collects results, verifies via filesystem/git state

**GSD Phase Planning Flow:**

1. User runs `/gsd-plan-phase` command
2. Workflow optionally spawns `gsd-phase-researcher` for technical research
3. `gsd-planner` subagent creates `PLAN.md` files from phase scope
4. `gsd-plan-checker` subagent reviews plan quality
5. Revision loop runs up to 3 iterations until plan passes gates

**State Management:**
- Project state is persisted in filesystem files (`STATE.md`, `ROADMAP.md`, `PLAN.md`, `SUMMARY.md`, `CONTEXT.md`)
- `gsd-tools.cjs` reads/writes these files and emits JSON context for workflows
- No in-memory or database state — all state is git-tracked Markdown

## Key Abstractions

**Skill:**
- Purpose: A self-contained, single-purpose prompt bundle that teaches the LLM a specific behavior
- Examples: `skills/idea-to-task/SKILL.md`
- Pattern: YAML frontmatter (`name`, `description`) + Markdown sections (`适用场景`, `核心原则`, `工作流`, `补问规则`, `输出结构`) + inline references to `references/*.md`

**Workflow:**
- Purpose: An orchestrator prompt defining how an LLM should coordinate multi-step, multi-agent tasks
- Examples: `.agent/get-shit-done/workflows/execute-phase.md`, `.agent/get-shit-done/workflows/plan-phase.md`
- Pattern: XML-tagged sections (`<purpose>`, `<required_reading>`, `<process>`) with bash snippets calling `gsd-tools.cjs`

**Agent Definition:**
- Purpose: A detailed system prompt defining a specialized subagent's responsibilities, tools, and behavior
- Examples: `.agent/agents/gsd-executor.md`, `.agent/agents/gsd-planner.md`, `.agent/agents/gsd-codebase-mapper.md`
- Pattern: Long-form Markdown system prompt, invoked via `Task(subagent_type="<name>", ...)`

**Reference Document:**
- Purpose: Supplementary knowledge loaded on demand within a skill or workflow
- Examples: `skills/idea-to-task/references/decision-rules.md`, `skills/idea-to-task/references/output-template.md`
- Pattern: Short, focused Markdown — loaded only when the LLM needs to resolve a specific decision

**Fixture:**
- Purpose: Behavioral test case defining input + expected output behavior for a skill
- Examples: `tests/fixtures/idea-to-task/01-clear-direction.md`, `02-mixed-topics.md`, `03-high-risk-ambiguity.md`
- Pattern: `## 输入` section with raw input, `## 期望行为` section with bullet-list expected behaviors

## Entry Points

**`skills/idea-to-task/SKILL.md`:**
- Location: `skills/idea-to-task/SKILL.md`
- Triggers: LLM runtime loads this when user invokes the `idea-to-task` skill
- Responsibilities: Defines the complete behavior contract for turning messy CEO notes into structured task trees

**`skills/idea-to-task/agents/openai.yaml`:**
- Location: `skills/idea-to-task/agents/openai.yaml`
- Triggers: OpenAI platform reads this for UI display metadata
- Responsibilities: Provides `display_name`, `short_description`, `default_prompt` for platform integration

**`.agent/skills/gsd-*/SKILL.md`:**
- Location: `.agent/skills/gsd-<command-name>/SKILL.md`
- Triggers: Generic agent runtime invokes this per command
- Responsibilities: Routes to the appropriate GSD workflow

**`.claude/commands/gsd/*.md`:**
- Location: `.claude/commands/gsd/<command>.md`
- Triggers: Claude Code slash-command invocation (e.g., `/gsd-execute-phase`)
- Responsibilities: Bootstraps workflow execution with runtime-specific context

**`skills/idea-to-task/scripts/validate_skill.py`:**
- Location: `skills/idea-to-task/scripts/validate_skill.py`
- Triggers: `uv run validate_skill.py <skill_dir> [--strict]`
- Responsibilities: Validates SKILL.md frontmatter, required sections, referenced file existence; in `--strict` mode also checks `agents/openai.yaml` and test fixtures

## Error Handling

**Strategy:** Explicit fallback rules embedded in workflow prose; no exception handling in the traditional sense

**Patterns:**
- Workflow files specify fallback behavior when subagent spawning fails (sequential inline execution)
- `validate_skill.py` returns a list of validation errors with non-zero exit code
- LLM workflows instruct the orchestrator to verify completion via filesystem/git state rather than relying on completion signals
- Ambiguous skill inputs are handled by explicit dual-path output rules rather than errors

## Cross-Cutting Concerns

**Logging:** Runtime output printed to stdout in Chinese (per project conventions); `validate_skill.py` prints `校验通过` or `校验失败：` + error list

**Validation:** `validate_skill.py` enforces structural contracts on skill bundles (frontmatter schema, required sections, file references, fixture count)

**Multi-runtime Support:** The GSD framework is replicated across three runtime namespaces — `.agent/` (generic), `.claude/` (Claude Code), `.codex/` (Codex) — with identical internal structure but runtime-specific command dispatch

---

*Architecture analysis: 2026-04-12*
