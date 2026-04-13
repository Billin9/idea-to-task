# Phase 2: 示例校准 - Context

**Gathered:** 2026-04-13
**Status:** Ready for planning

<domain>
## Phase Boundary

在 examples.md 中补充正反对比案例，让模型能直接参照「平铺输出（错误）」和「归纳输出（正确）」的差异来对齐期望行为。同时修复现有案例 2 使其与 Phase 1 新增的归纳逻辑保持一致。

</domain>

<decisions>
## Implementation Decisions

### 对比案例数量与场景
- **D-01:** 只新增一组正反对比案例，最小满足 EX-01 要求
- **D-02:** 复用 fixture 04（04-induction-success.md）的产品发布场景（技术实现 + 运营策略 + 团队搭建 → 归纳为「产品X发布」），保持 examples.md 与 fixture 的一致性

### 对比案例展示格式
- **D-03:** 使用前后分段对比格式：先展示「❌ 错误示例（平铺）」，再展示「✅ 正确示例（归纳）」，用明确的视觉标记区分
- **D-04:** 每个示例展示三个关键节点的对比：核心判断 + 主题拆分 + 任务树摘要（里程碑级），不展开到执行项级
- **D-05:** 对比案例末尾附「检查点」列表，与现有案例 5/6 的格式保持一致

### 现有案例 2 修复
- **D-06:** 修改案例 2 的处理方式描述，加入「拆分后经过向上归纳检查」的步骤。因为案例 2 的「产品 AI 化、组织提效、商业化」属于多不相关主题，归纳检查后应走静默回退，最终结果仍为平铺，但流程描述需要体现归纳检查的存在

### Claude's Discretion
- 对比案例中错误示例和正确示例的具体文案措辞
- 检查点的具体条目数量
- 案例 2 修复后的具体措辞

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Skill 核心文件（Phase 2 修改目标）
- `skills/idea-to-task/references/examples.md` — 示例案例文件，Phase 2 的主要修改目标

### Phase 1 产出（归纳逻辑定义）
- `skills/idea-to-task/references/decision-rules.md` — 第 3 节「向上归纳检查」定义了归纳判断逻辑，对比案例的正确示例必须与此一致
- `skills/idea-to-task/references/output-template.md` — 归纳型输出模板和三级优先级规则，对比案例的正确示例必须遵循此模板

### 行为级 Fixture（对比案例素材）
- `tests/fixtures/idea-to-task/04-induction-success.md` — 归纳成功场景的输入和期望行为，对比案例复用此场景

### 项目规格
- `.planning/REQUIREMENTS.md` — EX-01 需求定义

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `tests/fixtures/idea-to-task/04-induction-success.md`：已有归纳成功场景的完整输入和期望行为描述，可直接作为对比案例的素材来源
- `examples.md` 案例 5/6：已有正例/反例的格式范式（输入 → 判定依据 → 处理方式 → 检查点），可参照此格式编写对比案例

### Established Patterns
- examples.md 的案例编号从 1 开始递增，新增案例应为案例 7
- 每个案例包含：标题、输入描述、处理方式、检查点
- 战略型正例/反例已建立了「同一决策维度的正反示例」模式

### Integration Points
- 新增的对比案例需要与 output-template.md 的归纳型模板结构完全对齐
- 案例 2 的修复需要与 decision-rules.md 第 3 节的归纳检查流程一致
- 对比案例的「正确示例」格式需要与 output-template.md 的归纳型核心判断格式一致

</code_context>

<specifics>
## Specific Ideas

- 对比案例标题格式：「案例 7：归纳型输入——正反对比」
- 错误示例用 `### ❌ 错误示例（平铺）` 标记
- 正确示例用 `### ✅ 正确示例（归纳）` 标记
- 正确示例的核心判断格式参照 output-template.md：「CEO 真正在推动的是：『产品X发布』。原始拆出的技术实现、运营策略、团队搭建三条线均服务于这一顶层目标，归纳为单主题。」
- 正确示例的主题拆分标记为「单主题（归纳）」

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope

</deferred>

---

*Phase: 02-example-calibration*
*Context gathered: 2026-04-13*
