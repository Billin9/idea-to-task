# Phase 1: 判断与输出重构 - Context

**Gathered:** 2026-04-12
**Status:** Ready for planning

<domain>
## Phase Boundary

在 decision-rules.md 和 output-template.md 中实现向上归纳逻辑，使 skill 在主题拆分后能识别父子包含关系并收敛为统一顶层意图，输出结构支持「一句话顶层意图 + 子任务线展开」。同步更新 SKILL.md 的工作流描述和核心原则。

</domain>

<decisions>
## Implementation Decisions

### 归纳触发条件
- **D-01:** 向上归纳适用于所有多主题输入，不限于战略型输入。只要拆出多个主题，都先尝试归纳
- **D-02:** 归纳判断标准是「目标从属关系」— 当多个主题服务于同一个更高层目标时，收敛为单顶层主题
- **D-03:** 归纳步骤位于主题拆分之后、输出之前（先发散再收敛的思维过程）

### 归纳后输出结构
- **D-04:** 新增「归纳型」输出模板，与现有战略型模板并存两套。战略型走「总体方案设计 + 诊断线/落地线」，归纳型走「顶层意图 + 子任务线（里程碑级）」
- **D-05:** 核心判断部分显式说明归纳过程 — 先写顶层意图，再用一句话说明「原始 N 个主题均服务于此目标，归纳为单主题���
- **D-06:** 主题拆分部分标记为「单主题（归纳）」，说明是由多个方向收敛而来，区别于天然单主题
- **D-07:** 任务树中，原来的并列主题降级为顶层主题下的里程碑，在单主题内分层展开

### 归纳失败回��
- **D-08:** 当多个主题确实独立、无法归纳时，静默回退走现有的平铺多主题逻辑，不向读者暴露「尝试归纳但失败」的内部过程（符合现有原则「不暴露内部推理」）

### SKILL.md 工作流与原则
- **D-09:** 在 SKILL.md 工作流中，在拆主题（步骤 6）和输出（步骤 7）之间新增独立步骤「向上归纳检查」
- **D-10:** 核心原则中，将现有的「战略型输入必须先出顶层方案」扩展为更通用的「多主题输��先尝试向上归纳，找到统一顶层意图后再展开」。战略型规则作为其特例保留

### Claude's Discretion
- 归纳型模板中里程碑的具体排列顺序和展开深度
- decision-rules.md 中归纳判断步骤的具体措辞和示例选择
- SKILL.md 新步骤的具体措辞

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Skill 核心文件（Phase 1 修改目标）
- `skills/idea-to-task/SKILL.md` — Skill 入口，工作流和核心原则定义
- `skills/idea-to-task/references/decision-rules.md` — 分流与风险判断规则，需新增向上归纳步骤
- `skills/idea-to-task/references/output-template.md` — 输出模板，需新增归纳型模板

### 项目规格
- `docs/superpowers/specs/2026-04-11-idea-to-task-design.md` — 原始设计规格，包含目标用户、输入协议、输出协议等完整定义
- `.planning/REQUIREMENTS.md` — v1 需求定义，Phase 1 覆盖 JUDGE-01/02, OUT-01/02/03

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `decision-rules.md` 第 1 节：已有战略型输入三条件检测逻辑，归纳判断步骤可参照此格式编写
- `output-template.md` 第 3 节：已有战略型固定模板结构（总体方案设计 + 诊断线/落地线），归纳型模板可参考其层级组织方式

### Established Patterns
- 判断规则采用条件列表 + 场景说明 + 反例的组织方式
- 输出模板采用 Markdown 代码块展示结构示例
- SKILL.md 工作流以编号列表描述，每步一句话
- 核心原则以 bullet list + 加粗要点组织

### Integration Points
- SKILL.md 工作流步骤 2（战略型前置判断）和步骤 6（拆主题）之间需要协调新归纳步骤的位置
- decision-rules.md 第 2 节（主题密度判断）是归纳步骤的上游输入——先判密度，再尝试归纳
- output-template.md 第 1 节（核心判断）和第 2 节（主题拆分）的格式需要适配归纳型输出

</code_context>

<specifics>
## Specific Ideas

- 归纳型核心判断的格式示例：「CEO 真正在推动的是：『产品X上线』。原始拆出的技术实现、运营策略、团队搭建三条线均服务于这一顶层目标，归纳为单主题。」
- 主题拆分标记格式：「单主题（归纳）」，区别于天然单主题的「单主题」
- 归纳失败时的行为应与现有「不暴露内部推理」原则保持一致

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope

</deferred>

---

*Phase: 01-judgment-output-refactor*
*Context gathered: 2026-04-12*
