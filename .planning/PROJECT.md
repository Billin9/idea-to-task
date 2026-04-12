# idea-to-task Skill 输出质量优化

## What This Is

对现有 idea-to-task skill 的输出质量进行定向优化。这个 skill 把 CEO 的碎片想法整理成结构化任务树，当前问题是输出缺乏「向上归纳」能力——会把本该是父子关系的任务平铺成并列主题，核心判断也直接铺主线而不是先抓住统一的顶层意图。优化目标是让 skill 在输出时先找到一个统一的顶层意图，再向下展开子任务线。

## Core Value

输出必须先归纳出 CEO 真正想做的那一件事，再往下展开，而不是一上来就横向铺开。

## Requirements

### Validated

- [x] 核心判断能识别并归纳出统一的顶层意图，而不是直接列出多条并列主线 — Validated in Phase 1: 判断与输出重构
- [x] 主题拆分能检测父子包含关系，当一个主题逻辑上包含其他主题时，收敛为一个顶层主题 — Validated in Phase 1: 判断与输出重构
- [x] 被包含的子主题降级为顶层主题下的里程碑或子任务线 — Validated in Phase 1: 判断与输出重构
- [x] 输出模板支持「单顶层主题 + 多子任务线」的结构 — Validated in Phase 1: 判断与输出重构
- [x] decision-rules 增加「向上归纳」判断步骤 — Validated in Phase 1: 判断与输出重构

### Active

- [ ] examples 补充正反对比案例（平铺 vs 归纳）

### Out of Scope

- 新增输入类型支持 — 本次只改输出质量
- 交互式追问流程改造 — 不在本次范围
- 与其他工具的联动集成 — 不在本次范围
- skill 触发条件或描述优化 — 不在本次范围

## Context

- 项目是一个 Claude Code skill，位于 `skills/idea-to-task/`
- 核心文件：SKILL.md（主指令）、references/decision-rules.md（判断规则）、references/output-template.md（输出模板）、references/examples.md（示例）
- 已有战略型输入检测逻辑（三条件 AND 判断），但问题出在检测之后的输出组织方式
- 用户反馈的典型问题：一个"全公司 AI 转型"输入被拆成 6 个并列主题，实际上应该是 1 个顶层主题 + 5 条子任务线

## Constraints

- **范围**: 只修改 skills/idea-to-task/ 目录下的四个文件，不改目录结构
- **兼容**: 优化不能破坏现有的非战略型输入处理逻辑
- **风格**: 代码注释和输出内容必须使用中文

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| 只优化输出质量，不加新能力 | 用户明确要求聚焦输出质量 | — Pending |
| 核心改动是增加「向上归纳」步骤 | 这是平铺问题的根因——缺少识别包含关系的逻辑 | — Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd-transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-04-12 after initialization*
