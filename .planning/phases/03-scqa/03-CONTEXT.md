# Phase 3: SCQA 输入解析层 - Context

**Gathered:** 2026-04-14
**Status:** Ready for planning

<domain>
## Phase Boundary

从 CEO 碎片输入中推演完整的 SCQA 框架（Situation / Complication / Question / Answer），产出明确的 Answer 作为后续金字塔结构的顶点。修改范围限于 SKILL.md 和 decision-rules.md，不涉及 output-template.md 和 examples.md。

</domain>

<decisions>
## Implementation Decisions

### 工作流重构策略
- **D-01:** 完全重构 SKILL.md 工作流，不保留 v1.0 的步骤编号和分流结构，为咨询方法论设计最优 SOP
- **D-02:** SCQA 推演覆盖所有输入类型（战略型、归纳型、常规型），战略型/归纳型分流由 SCQA 推演结果自然导出，不再作为前置判断
- **D-03:** v1.0 的向上归纳检查（原步骤 7）合并进 SCQA 推演流程，不再作为独立步骤存在

### SCQA 内部推理格式
- **D-04:** 使用 XML 标签（`<scqa_analysis>`）隔离内部推演过程，为 Phase 5 的 MECE/So-what 校验建立统一的内部推理模式
- **D-05:** SCQA 四要素（S/C/Q/A）全部隐藏在内部推理中，仅 Answer 以"核心判断"的自然语言形式呈现给用户，不暴露任何方法论术语

### 追问触发机制
- **D-06:** 追问触发条件：当 Situation 或 Complication 中任一关键要素缺失且无法从上下文推演时，触发定向追问
- **D-07:** SCQA 追问独立于后续通用补问，最多 2-3 个精简定向问题，与通用补问分开计数

### 证据强度机制
- **D-08:** 证据强度机制不受 v1.0 三档（弱/中/强）束缚，完全按 SCQA + 金字塔方法论的最佳实践重构——如果方法论不需要三档映射，可以推翻重建
- **D-09:** Phase 3 只负责建立 SCQA 完整度→证据强度的映射关系，具体的层级深度控制留给 Phase 4（金字塔输出结构）

### Claude's Discretion
- decision-rules.md 中 SCQA 追问规则的章节结构和位置
- SCQA 推演步骤的具体内部编排顺序
- XML 标签的具体命名和嵌套结构（`<scqa_analysis>` 为基础，细节可调）

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### 核心修改文件
- `skills/idea-to-task/SKILL.md` — 主工作流定义，Phase 3 需要完全重构其工作流步骤
- `skills/idea-to-task/references/decision-rules.md` — 判断规则，需新增 SCQA 推演规则章节

### 不修改但需理解的文件
- `skills/idea-to-task/references/output-template.md` — 输出模板，Phase 3 不改但需理解 Answer 如何映射到"核心判断"
- `skills/idea-to-task/references/examples.md` — 现有 7 个案例，Phase 3 不改但需理解行为基线

### 方法论研究
- `.planning/research/SUMMARY.md` — v2.0 研究总结，含技术栈推荐和管线架构
- `.planning/research/ARCHITECTURE.md` — 四层管线架构设计，SCQA 为 Stage 1
- `.planning/research/PITFALLS.md` — 8 个风险陷阱，Phase 3 重点关注 #1 指令过载、#5 方法论冲突

### 需求定义
- `.planning/REQUIREMENTS.md` — SCQA-01 至 SCQA-04 需求定义
- `.planning/PROJECT.md` — 项目约束（只改 4 文件、中文输出、不暴露术语）

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `SKILL.md` 现有工作流结构（8 步流程）：虽然步骤会重构，但"先给结论再给结构"的核心原则、补问规则入口、参考文件懒加载模式可沿用
- `decision-rules.md` 现有判断框架：战略型三条件判断、信号词辅助、证据强度分级的设计模式可参考

### Established Patterns
- **Procedural CoT 模式：** 工作流步骤即思维链，SKILL.md 用有序步骤编码处理流程，SCQA 推演应延续此模式
- **禁止列表模式：** "明确禁止"章节定义负面约束，SCQA 术语泄漏禁令应放在此处
- **懒加载参考：** "何时读取参考文件"章节控制上下文预算，新增 SCQA 规则的加载条件需在此注册

### Integration Points
- `SKILL.md` → `decision-rules.md`：通过"详见 decision-rules.md"链接引用，SCQA 规则需要在此建立连接
- `decision-rules.md` 第 6 节"证据强度与下钻深度"：Phase 3 重建的 SCQA→证据强度映射需要替换或重构此节
- `output-template.md` 第 1 节"核心判断"：SCQA 的 Answer 将映射到此处，Phase 3 需确保接口对齐但不修改模板

</code_context>

<specifics>
## Specific Ideas

- 用户明确表示"可以完全推翻现有工作流"，不需要向后兼容 v1.0 步骤结构
- 用户明确表示证据强度机制"完全看方法论是否需要，如果不需要可以推翻"
- 设计理念：为方法论设定最佳 SOP，不被现有实现束缚

</specifics>

<deferred>
## Deferred Ideas

None — 讨论严格限制在 Phase 3 范围内

</deferred>

---

*Phase: 03-scqa*
*Context gathered: 2026-04-14*
