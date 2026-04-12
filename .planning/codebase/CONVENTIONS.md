# Coding Conventions

**Analysis Date:** 2026-04-12

## Overview

This project is a **Claude skill** (prompt-driven AI agent), not a traditional software codebase. The primary "code" consists of Markdown instruction files, YAML metadata, and Python utility scripts. Conventions reflect this nature.

---

## File Naming Patterns

**Skills:**
- Skill root directory uses `kebab-case`: `skills/idea-to-task/`
- Main skill definition file is always `SKILL.md` (UPPERCASE)
- Reference documents use `kebab-case.md`: `decision-rules.md`, `output-template.md`, `examples.md`

**Agents/Hooks:**
- Agent definition files use `kebab-case` with `gsd-` prefix: `gsd-codebase-mapper.md`, `gsd-executor.md`
- Hook scripts use `kebab-case` with `gsd-` prefix: `gsd-validate-commit.sh`, `gsd-workflow-guard.js`

**Tests:**
- Fixture files use zero-padded numeric prefix + descriptive name: `01-clear-direction.md`, `02-mixed-topics.md`, `03-high-risk-ambiguity.md`

**Python scripts:**
- Use `snake_case`: `validate_skill.py`

**Docs:**
- Design/spec docs use date prefix + topic: `2026-04-11-idea-to-task-design.md`

---

## Markdown Document Structure

**SKILL.md frontmatter** (mandatory):
```yaml
---
name: skill-name
description: One-sentence English description of when to use this skill.
---
```

**Required sections** in `SKILL.md` (enforced by `validate_skill.py`):
- `## 适用场景`
- `## 核心原则`
- `## 工作流`
- `## 补问规则`
- `## 输出结构`

**Section order convention** in SKILL.md:
1. YAML frontmatter
2. H1 title (Chinese)
3. One-line purpose statement
4. `## 适用场景`
5. `## 核心原则`
6. `## 工作流`
7. `## 补问规则`
8. `## 输出结构`
9. `## 何时读取参考文件`
10. `## 明确禁止`

**Reference links** in SKILL.md must be relative paths to files that actually exist (validated by `validate_skill.py`):
```markdown
详细判定规则见 [decision-rules.md](./references/decision-rules.md)。
```

---

## Language Conventions

**Document language:**
- All `.md` content: Chinese (中文), including headings, body, and explanations
- YAML `name` and `description` fields: English
- `openai.yaml` display fields: English
- Python source code: English identifiers, Chinese string literals and error messages
- Shell/JS hook code: English comments in file headers, Chinese in user-facing error messages

**Tone in Markdown:**
- Imperative and prescriptive ("先给结论", "不暴露内部推理")
- No hedging language in rule documents
- Numbered lists for ordered steps, bullet lists for unordered rules

---

## Python Code Style

**File header** (mandatory for standalone scripts):
```python
#!/usr/bin/env -S uv run
# /// script
# dependencies = ["pyyaml<7"]
# ///
from __future__ import annotations
```

**Imports:** stdlib first, then third-party. One blank line between groups.

**Type annotations:** Always use type hints. Use `list[str]` (lowercase, PEP 585 style), not `List[str]`.

**Function design:**
- Pure functions with explicit return types
- Validation functions return `list[str]` (error messages), not raise exceptions
- `main()` returns `int` exit code, called via `raise SystemExit(main())`

**Error messages:** Chinese strings, e.g. `"SKILL.md 缺少合法的 YAML frontmatter"`

**Naming:** `snake_case` for functions and variables, `UPPER_SNAKE_CASE` for module-level constants:
```python
REQUIRED_SECTIONS = [
    "## 适用场景",
    ...
]
```

---

## YAML Conventions

**openai.yaml** structure (in `agents/` subdir of each skill):
```yaml
interface:
  display_name: "Human-Readable Name"
  short_description: "Single sentence."
  default_prompt: "Use $skill-name to..."
```

---

## Skill Directory Layout Convention

Every skill must follow this layout:
```
skills/<skill-name>/
├── SKILL.md              # Main skill definition (required)
├── agents/
│   └── openai.yaml       # UI metadata (required in strict mode)
├── references/
│   ├── decision-rules.md # Routing/decision logic
│   ├── output-template.md# Output format spec
│   └── examples.md       # Annotated examples
└── scripts/
    └── validate_skill.py # Validation script
```

---

## Output / Behavior Conventions (Skill Instructions)

These conventions govern what the AI skill outputs, not the code itself:

**Output format:**
- Six-section fixed structure: 核心判断 → 主题拆分 → 分层任务树 → 执行建议 → 风险与高风险推断 → 下一步动作
- Short sentences preferred
- No `<thinking>` tags or meta-commentary in output

**Decision conventions:**
- Default to producing output; only ask follow-up questions when ambiguity would fundamentally change task direction
- Follow-up question count: 2–5 maximum
- Task depth governed by evidence strength: weak → project level only; medium → milestone level; strong → execution item level

---

## Git Conventions

**Commit format:** Conventional Commits (enforced by `.claude/hooks/gsd-validate-commit.sh`):
```
<type>(<scope>): <subject>
```
Valid types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`

**Constraints:**
- Subject line ≤ 72 characters
- Lowercase, imperative mood, no trailing period

---

## Comments

**Python:** Chinese comments for business logic explanation; English for technical implementation notes in hook files.

**Shell/JS hooks:** English block comment at file top explaining purpose and behavior; inline logic uncommented unless complex.

---

*Convention analysis: 2026-04-12*
