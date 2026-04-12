# Testing Patterns

**Analysis Date:** 2026-04-12

## Overview

This project uses a **fixture-based behavioral testing** approach rather than a unit test framework. Tests are Markdown scenario files that specify inputs and expected behaviors for the AI skill. The single Python utility script (`validate_skill.py`) is a structural validator, not a test runner in the traditional sense.

---

## Test Framework

**Runner:**
- No automated test runner (pytest, jest, etc.) is configured
- `.gitignore` includes `.pytest_cache/` and `*.pyc`, suggesting pytest was considered or used during development but no `pytest.ini` / `pyproject.toml` / `conftest.py` is present
- Structural validation is run manually via `validate_skill.py`

**Assertion Library:**
- Not applicable — tests are Markdown behavioral specs, not executable assertions

**Run Commands:**
```bash
# Validate skill structure (non-strict)
uv run skills/idea-to-task/scripts/validate_skill.py skills/idea-to-task

# Validate skill structure (strict — also checks agents/openai.yaml and fixture count)
uv run skills/idea-to-task/scripts/validate_skill.py skills/idea-to-task --strict
```

---

## Test File Organization

**Location:**
- `tests/fixtures/<skill-name>/` — one subdirectory per skill
- Current fixture directory: `tests/fixtures/idea-to-task/`

**Naming:**
- Zero-padded numeric prefix + descriptive scenario name
- Pattern: `NN-scenario-name.md`
- Examples:
  - `tests/fixtures/idea-to-task/01-clear-direction.md`
  - `tests/fixtures/idea-to-task/02-mixed-topics.md`
  - `tests/fixtures/idea-to-task/03-high-risk-ambiguity.md`

**Minimum count:**
- Strict validation requires ≥ 3 fixture files per skill (enforced by `validate_skill.py --strict`)

---

## Test (Fixture) Structure

Each fixture file follows a two-section Markdown structure:

```markdown
# 场景 N：场景名称

## 输入

<用于测试的原始输入文本>

## 期望行为

- <期望行为条目 1>
- <期望行为条目 2>
- <期望行为条目 3>
```

**Actual examples:**

`tests/fixtures/idea-to-task/01-clear-direction.md`:
- Input: Clear CEO directive with explicit scope, timeline, and target users
- Expected: No follow-up questions; explicit main theme; full three-level task tree; role recommendations covering product, engineering, sales ops

`tests/fixtures/idea-to-task/02-mixed-topics.md`:
- Input: CEO mentioning three unrelated topics (AI product, org efficiency, commercialization)
- Expected: Split into ≥ 3 themes; initial task trees; ≤ 3 follow-up questions; no merging of unrelated topics

`tests/fixtures/idea-to-task/03-high-risk-ambiguity.md`:
- Input: CEO expressing conflicting directions (high-end vs. SMB market)
- Expected: Two explicit paths; explicit high-risk ambiguity label; task directions for both paths; no implicit side-taking

---

## Structural Validation

`skills/idea-to-task/scripts/validate_skill.py` performs these checks:

**Non-strict mode:**
1. `SKILL.md` exists
2. Valid YAML frontmatter present
3. `frontmatter.name` is non-empty string
4. `frontmatter.description` is non-empty string
5. All five required sections present (`## 适用场景`, `## 核心原则`, `## 工作流`, `## 补问规则`, `## 输出结构`)
6. All relative file links in `SKILL.md` resolve to existing files

**Strict mode (adds):**
7. `agents/openai.yaml` exists in skill directory
8. `tests/fixtures/<skill-name>/` directory exists
9. At least 3 `.md` files in the fixtures directory

**Exit codes:**
- `0` — validation passed
- `1` — validation failed (errors printed to stdout)

---

## Fixture Coverage

**Scenarios covered (3 of 3 minimum):**

| Fixture | Scenario Type | Key Behavior Tested |
|---------|--------------|---------------------|
| `01-clear-direction.md` | Clear input | Direct output, no follow-up questions, full 3-level task tree |
| `02-mixed-topics.md` | Mixed/multi-topic | Topic splitting, controlled follow-up (≤3 questions), no topic merging |
| `03-high-risk-ambiguity.md` | High-risk ambiguity | Dual-path output, explicit ambiguity labeling, no implicit decision |

**Coverage gaps:**
- No fixture for "evidence too weak" scenario (only project-level output)
- No fixture for extremely short/fragment input
- No fixture testing follow-up question count boundary (2–5 range)
- No automated execution of fixtures against a live model

---

## Mocking

Not applicable — this project has no backend services, databases, or external API calls to mock.

---

## What to Test When Adding a New Skill

When creating a new skill under `skills/<new-skill>/`:

1. Create `tests/fixtures/<new-skill>/` directory
2. Add at minimum 3 fixture files covering:
   - **Clear input** → direct output, no follow-up
   - **Ambiguous input** → follow-up questions or dual path
   - **Edge case** → scenario specific to the skill's domain
3. Run structural validation:
   ```bash
   uv run skills/<new-skill>/scripts/validate_skill.py skills/<new-skill> --strict
   ```
4. Verify all reference links in `SKILL.md` resolve

---

## Notes on pytest Artifacts

The `.gitignore` includes `.pytest_cache/` and `*.pyc`, indicating pytest infrastructure was considered. If unit tests are added to `validate_skill.py` or future Python scripts, use:

```bash
uv run pytest tests/
```

No `conftest.py`, `pytest.ini`, or `pyproject.toml` currently exists — these would need to be created before pytest tests can run.

---

*Testing analysis: 2026-04-12*
