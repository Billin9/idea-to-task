# idea-to-task Skill 输出质量优化

## What This Is

idea-to-task skill 的输出质量优化。该 skill 把 CEO 的碎片想法整理成结构化任务树。v1.0 已完成「向上归纳」能力；v2.0 将用咨询方法论（金字塔原理 + SCQA + MECE）全面重构工作流和输出逻辑，使输出从简单的归纳升级为结构化的战略落地方案。

## Core Value

输出必须用金字塔原理从顶层结论出发，向下分层展开战略支柱和关键任务，确保逻辑严密、不重不漏。

## Current Milestone: v2.0 咨询方法论重构

**Goal:** 用金字塔原理 + SCQA + MECE 等咨询方法论全面重构 idea-to-task skill 的工作流和输出逻辑

**Target features:**
- SCQA 输入解析层 — AI 先基于输入推演 S/C/Q/A 背景框架，信息不足时再追问补全
- 金字塔原理输出结构 — 输出从顶层结论出发，向下分层为战略支柱→关键任务，弹性 3x3 结构
- MECE 内部检查 — AI 内部执行任务不重叠、不遗漏的逻辑校验（不向用户暴露）
- So-what 内部过滤 — AI 内部剔除无行动意义的空洞描述（不向用户暴露）
- 保持任务树输出格式 — 不加 Action Items 表格，保持现有的树形输出

## Requirements

### Validated

- [x] 核心判断能识别并归纳出统一的顶层意图，而不是直接列出多条并列主线 — v1.0 Phase 1
- [x] 主题拆分能检测父子包含关系，当一个主题逻辑上包含其他主题时，收敛为一个顶层主题 — v1.0 Phase 1
- [x] 被包含的子主题降级为顶层主题下的里程碑或子任务线 — v1.0 Phase 1
- [x] 输出模板支持「单顶层主题 + 多子任务线」的结构 — v1.0 Phase 1
- [x] decision-rules 增加「向上归纳」判断步骤 — v1.0 Phase 1
- ✓ examples 补充正反对比案例（平铺 vs 归纳） — v1.0 Phase 2
- [x] v1.0 fixture/examples 兼容性保持：能复用的保留，不兼容的按新方法论重写 — v2.0 Phase 6
- [x] examples 全量重写为 8 个 v2.0 行为案例，覆盖 SCQA / 金字塔 / MECE 三类正反对比封闭点 — v2.0 Phase 6
- [x] Phase 6 UAT 主文档建立 v1.0 三 fixture 回归、端到端管线和四文件术语扫清门禁 — v2.0 Phase 6

### Active

- [ ] SCQA 输入解析：AI 基于输入推演 S/C/Q/A 框架，信息不足时追问补全
- [ ] 金字塔原理输出：从顶层结论分层展开战略支柱→关键任务，弹性 3x3 结构
- [ ] MECE 内部校验：AI 内部检查任务不重叠、不遗漏
- [ ] So-what 内部过滤：AI 内部剔除无行动意义的空洞任务描述

### Out of Scope

- 新增输入类型支持 — 本次只改工作流和输出逻辑
- 交互式追问流程改造 — SCQA 追问已覆盖必要场景，不做更大的追问流程变更
- 与其他工具的联动集成 — 不在本次范围
- skill 触发条件或描述优化 — 不在本次范围
- Action Items 表格输出 — 保持任务树格式，不引入表格

## Context

- 项目是一个 Claude Code skill，位于 `skills/idea-to-task/`
- 核心文件：SKILL.md（主指令）、references/decision-rules.md（判断规则）、references/output-template.md（输出模板）、references/examples.md（示例）
- v1.0 已完成：383 行 Markdown，3 个文件修改，2 个 fixture 新增，7 个案例
- v2.0 方法论来源：金字塔原理（芭芭拉·明托）、SCQA 模型、MECE/议题树、So-what 测试
- MECE 和 So-what 作为 AI 内部逻辑运行，不在输出中暴露给用户

## Constraints

- **范围**: 只修改 skills/idea-to-task/ 目录下的四个文件，不改目录结构
- **兼容**: 优化不能破坏现有的非战略型输入处理逻辑
- **风格**: 代码注释和输出内容必须使用中文

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| 只优化输出质量，不加新能力 | 用户明确要求聚焦输出质量 | ✓ Good |
| 核心改动是增加「向上归纳」步骤 | 这是平铺问题的根因——缺少识别包含关系的逻辑 | ✓ Good |
| 归纳检查放在主题拆分之后 | 先拆后归比先归后拆更灵活 | ✓ Good |
| 用正反对比案例而非纯规则校准 | 规则 + 示例双锚定降低模型偏差 | ✓ Good |
| 案例中避免暴露内部术语 | 防止模型在输出中泄漏处理过程 | ✓ Good |
| v2.0 全面重构而非增量改进 | 咨询方法论需要替换底层逻辑，增量会导致新旧框架冲突 | — Pending |
| SCQA 先推演后追问 | 减少用户负担，只在信息确实不足时才追问 | — Pending |
| MECE/So-what 作为内部逻辑 | 避免输出暴露处理过程，用户只需看结果 | — Pending |
| 弹性 3x3 结构而非硬约束 | 不同复杂度的输入需要不同层级深度 | — Pending |
| examples 作者侧 / 案例正文术语边界双重声明 | 避免作者侧方法论说明被模型模仿或被 grep 误判为运行时泄漏 | ✓ Validated in Phase 6 |
| v1.0 回归用 UAT 三维断言承接，不新增 skill 侧 fixture | 保持 fixture 基线不漂移，同时让后续人工 / 自动验证可执行 | ✓ Validated in Phase 6 |

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
*Last updated: 2026-04-15 after Phase 6 verification*
