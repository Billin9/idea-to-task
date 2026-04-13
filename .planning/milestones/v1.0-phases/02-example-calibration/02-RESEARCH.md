# Phase 2: 示例校准 - Research

**Researched:** 2026-04-13
**Domain:** Prompt engineering — few-shot 示例设计（Markdown 内容编辑）
**Confidence:** HIGH

## Summary

本阶段的工作域是纯 Markdown 内容编写：在 `examples.md` 中新增一组正反对比案例（案例 7），并修复现有案例 2 使其与 Phase 1 引入的归纳检查逻辑对齐。不涉及任何代码变更、外部依赖或运行时操作。

所有修改均限定在 `skills/idea-to-task/references/examples.md` 单文件内。核心挑战不是技术实现，而是确保新增内容与 Phase 1 产出的 `decision-rules.md` 第 3 节和 `output-template.md` 归纳型模板在逻辑和格式上完全一致。

**Primary recommendation:** 以 fixture 04 的产品发布场景为素材，按现有案例 5/6 的格式范式编写对比案例，同时修复案例 2 的流程描述以体现归纳检查步骤。

<user_constraints>

## User Constraints (from CONTEXT.md)

### Locked Decisions
- **D-01:** 只新增一组正反对比案例，最小满足 EX-01 要求
- **D-02:** 复用 fixture 04（04-induction-success.md）的产品发布场景（技术实现 + 运营策略 + 团队搭建 → 归纳为「产品X发布」），保持 examples.md 与 fixture 的一致性
- **D-03:** 使用前后分段对比格式：先展示「❌ 错误示例（平铺）」，再展示「✅ 正确示例（归纳）」，用明确的视觉标记区分
- **D-04:** 每个示例展示三个关键节点的对比：核心判断 + 主题拆分 + 任务树摘要（里程碑级），不展开到执行项级
- **D-05:** 对比案例末尾附「检查点」列表，与现有案例 5/6 的格式保持一致
- **D-06:** 修改案例 2 的处理方式描述，加入「拆分后经过向上归纳检查」的步骤。因为案例 2 的「产品 AI 化、组织提效、商业化」属于多不相关主题，归纳检查后应走静默回退，最终结果仍为平铺，但流程描述需要体现归纳检查的存在

### Claude's Discretion
- 对比案例中错误示例和正确示例的具体文案措辞
- 检查点的具体条目数量
- 案例 2 修复后的具体措辞

### Deferred Ideas (OUT OF SCOPE)
None — discussion stayed within phase scope

</user_constraints>

<phase_requirements>

## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| EX-01 | 补充正反对比案例 — 同一输入分别展示「平铺输出」（错误）和「归纳输出」（正确），让模型对齐期望行为 | 案例 7 的正反对比设计直接满足此需求；fixture 04 提供现成素材；output-template.md 归纳型模板提供正确示例的格式规范 |

</phase_requirements>

## Architecture Patterns

### 现有 examples.md 结构模式

当前文件包含 6 个案例，按编号递增排列。每个案例的结构模式如下：

**基础案例（案例 1-4）：**
```markdown
## 案例 N：[标题]

输入[描述]。
处理方式：[处理说明]。
```

**带检查点的正反例（案例 5-6）：**
```markdown
## 案例 N：[标题]（正例/反例）

输入："[具体输入文本]"

判定依据：[判定说明]。
处理方式：[详细处理说明]。

检查点：
- [检查项 1]
- [检查项 2]
- [检查项 3]
```

### 新增对比案例的目标结构（案例 7） [VERIFIED: CONTEXT.md D-03/D-04/D-05]

```markdown
## 案例 7：归纳型输入——正反对比

输入："[复用 fixture 04 的输入文本]"

### ❌ 错误示例（平铺）

**核心判断：** [将三条线平铺为并列主线的错误写法]
**主题拆分：** [拆为三个并列主题的错误写法]
**任务树摘要：** [三个并列主题各自独立的里程碑]

### ✅ 正确示例（归纳）

**核心判断：** [以顶层意图开头，说明三个方向归纳为单主题]
**主题拆分：** 单主题（归纳）
**任务树摘要：** [单顶层主题 + 三个方向降级为里程碑]

检查点：
- [检查项]
```

### 案例 2 修复模式 [VERIFIED: CONTEXT.md D-06]

修复前：
```markdown
处理方式：先拆主题，再分别给任务树，可附 1 到 3 个关键问题。
```

修复后需体现的流程：
```markdown
处理方式：先拆主题，经向上归纳检查（产品 AI 化、组织提效、商业化属于不同方向，无法归纳为单一目标，静默回退），再分别给任务树，可附 1 到 3 个关键问题。
```

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| 归纳型核心判断措辞 | 自行编造格式 | 复用 output-template.md 归纳型核心判断模板 | 保持与 Phase 1 产出的一致性 |
| 正确示例的任务树结构 | 自行设计层级 | 复用 output-template.md 归纳型任务树模板 | D-04 要求与模板一致 |
| 对比案例的输入文本 | 编造新场景 | 复用 fixture 04 的原始输入 | D-02 明确锁定 |

## Common Pitfalls

### Pitfall 1: 正确示例与 output-template.md 格式不一致
**What goes wrong:** 正确示例的核心判断没有按 output-template.md 的归纳型格式写（第一句顶层意图、第二句归纳来源）
**Why it happens:** 写示例时凭感觉而非对照模板
**How to avoid:** 逐句对照 output-template.md 第 1 节「归纳型核心判断」的三条规则
**Warning signs:** 正确示例的第一句不是「CEO 真正在推动的是：...」

### Pitfall 2: 错误示例不够典型
**What goes wrong:** 错误示例写得太离谱，模型无法从中学到「微妙但关键」的区别
**Why it happens:** 为了突出对比把错误示例写成明显错误
**How to avoid:** 错误示例应该是「看起来合理但缺少归纳步骤」的平铺输出，而非胡说八道
**Warning signs:** 错误示例和正确示例在信息量上差异过大，而非在结构上差异

### Pitfall 3: 案例 2 修复后暗示归纳失败是负面结果
**What goes wrong:** 措辞让人觉得「归纳失败」是错误，实际上对于不相关主题，归纳失败是正确行为
**Why it happens:** 没有理解 decision-rules.md 第 3 节「静默回退」的设计意图
**How to avoid:** 措辞应中性，体现「经过检查 → 确认不可归纳 → 正确回退」的判断流程
**Warning signs:** 出现「失败」「无法」等负面措辞

### Pitfall 4: 对比案例的三个节点展示深度不一致
**What goes wrong:** D-04 要求展示核心判断 + 主题拆分 + 任务树摘要三个节点，但任务树摘要只到里程碑级。如果错误示例展示了执行项而正确示例没有，对比失焦
**Why it happens:** 错误示例和正确示例的展示粒度未对齐
**How to avoid:** 两个示例都严格只到里程碑级
**Warning signs:** 任一示例出现执行项级 checkbox

## Code Examples

### 归纳型核心判断格式（来自 output-template.md）

```markdown
CEO 真正在推动的是：[顶层意图]。原始拆出的 [主题A]、[主题B]、[主题C] 均服务于这一顶层目标，归纳为单主题。
```
[VERIFIED: output-template.md 第 1 节]

### 归纳型任务树格式（来自 output-template.md）

```markdown
### 主题：[顶层意图名称]
*由 [原主题A]、[原主题B]、[原主题C] 归纳而来。*

- **里程碑 1：[原主题A 方向]**
  - [ ] [执行项]
- **里程碑 2：[原主题B 方向]**
  - [ ] [执行项]
- **里程碑 3：[原主题C 方向]**
  - [ ] [执行项]
```
[VERIFIED: output-template.md 第 3 节]

### fixture 04 的原始输入（对比案例素材）

```markdown
CEO 说：我们的新产品 X 下个季度要上线。技术那边得把核心功能跑通，运营要准备好用户增长方案，市场部配合做一波发布前的预热传播。三条线各自推，但别脱节。
```
[VERIFIED: tests/fixtures/idea-to-task/04-induction-success.md]

### fixture 04 的期望行为要点

- 核心判断第一句必须是顶层意图：「CEO 真正在推动的是：产品 X 下季度上线」
- 主题拆分标记为「单主题（归纳）」
- 任务树只有一个顶层主题，技术、运营、市场降级为里程碑
- 不触发战略型模板
[VERIFIED: tests/fixtures/idea-to-task/04-induction-success.md]

### 向上归纳检查流程（来自 decision-rules.md 第 3 节）

```
1. 对已拆出的所有主题，问：「这些方向是否都在服务同一个更大的目标？」
2. 如果存在一个目标能覆盖全部主题 → 归纳成功 → 走归纳型模板
3. 如果主题之间确实独立 → 归纳失败 → 静默回退，按原有多主题逻辑输出
```
[VERIFIED: decision-rules.md 第 3 节]

## Assumptions Log

> 本研究中所有声明均已通过直接读取项目文件验证，无需用户确认。

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| (empty) | — | — | — |

**此表为空：** 所有声明均来自项目文件直接验证。

## Open Questions

无。所有实现细节已在 CONTEXT.md 中锁定或留给 Claude 自行决定。

## Environment Availability

Step 2.6: SKIPPED — 本阶段为纯 Markdown 内容编辑，无外部依赖。

## Sources

### Primary (HIGH confidence)
- `skills/idea-to-task/references/examples.md` — 现有案例结构和格式
- `skills/idea-to-task/references/output-template.md` — 归纳型模板定义
- `skills/idea-to-task/references/decision-rules.md` — 向上归纳检查逻辑
- `tests/fixtures/idea-to-task/04-induction-success.md` — 对比案例素材
- `.planning/phases/02-example-calibration/02-CONTEXT.md` — 用户锁定决策

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH — 无技术栈，纯内容编辑
- Architecture: HIGH — 现有文件结构清晰，模式已验证
- Pitfalls: HIGH — 基于对 Phase 1 产出的直接分析

**Research date:** 2026-04-13
**Valid until:** 2026-05-13（内容稳定，无版本依赖）
