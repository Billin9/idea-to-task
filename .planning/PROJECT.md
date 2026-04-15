# idea-to-task Skill 输出质量优化

## What This Is

idea-to-task skill 的输出质量优化。该 skill 把 CEO 的碎片想法整理成结构化任务树。v1.0 已完成「向上归纳」能力；v2.0 将用咨询方法论（金字塔原理 + SCQA + MECE）全面重构工作流和输出逻辑，使输出从简单的归纳升级为结构化的战略落地方案。

## Core Value

输出必须用金字塔原理从顶层结论出发，向下分层展开战略支柱和关键任务，确保逻辑严密、不重不漏。

## Current State

v2.0 咨询方法论重构已发布（2026-04-15）。idea-to-task skill 现已具备完整的咨询方法论管线：输入经 SCQA 内部推演 → 证据强度映射 → 金字塔分层任务树 → MECE 四维校验 → So-what 空洞过滤 → 六段式结构化输出。四个 skill 文件（SKILL.md / decision-rules.md / output-template.md / examples.md）实现旧术语清零、作者侧与正文侧双重禁词边界、v1.0 回归三维断言。

**Next milestone:** 未规划。可能方向：v2.1 补跑 05-UAT.md 8 类行为断言（tech debt 回收），或 v3.0 新增高级功能（垂直问答关系检查、SCA/CSA 变体、MECE 缺口标注）。

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

### Validated (v2.0)

- ✓ SCQA 输入解析：AI 基于输入推演 S/C/Q/A 框架，信息不足时追问补全 — v2.0 Phase 3
- ✓ 金字塔原理输出：从顶层结论分层展开主题→里程碑→执行项，弹性 2-4 层深度随证据强度伸缩 — v2.0 Phase 4
- ✓ MECE 内部校验：AI 内部四维校验（互斥 / 完备 / 数量 2-4 / 分组一致性）+ underflow/overflow 兜底 — v2.0 Phase 5
- ✓ So-what 内部过滤：AI 内部剔除 5 类空洞模式（字面黑名单 + 语义自问双道机制） — v2.0 Phase 5
- ✓ 示例校准与 v1.0 兼容：8 个 v2.0 案例全量重写，v1.0 三 fixture 三维回归门禁建立 — v2.0 Phase 6

### Active

（暂无新增需求）

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
| v2.0 全面重构而非增量改进 | 咨询方法论需要替换底层逻辑，增量会导致新旧框架冲突 | ✓ Good (v2.0) |
| SCQA 先推演后追问 | 减少用户负担，只在信息确实不足时才追问 | ✓ Good (v2.0 Phase 3) |
| MECE/So-what 作为内部逻辑 | 避免输出暴露处理过程，用户只需看结果 | ✓ Good (v2.0 Phase 5) |
| 弹性 2-4 层结构而非硬 3x3 约束 | 不同复杂度的输入需要不同层级深度 | ✓ Good (v2.0 Phase 4) |
| 统一金字塔模板替换三模板分叉 | 消除战略型/归纳型/常规型的前置分流，由 SCQA 推演统一驱动 | ✓ Good (v2.0 Phase 4) |
| Phase 5 VERIFICATION.md 回填 | milestone audit 发现形式化 gap；规则已落地，Phase 6 E2E 已间接验证，回填即可闭环 | ✓ Good (v2.0 audit) |
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
*Last updated: 2026-04-15 after v2.0 milestone close*
