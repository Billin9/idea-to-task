# Phase 4: 金字塔原理输出结构 - Context

**Gathered:** 2026-04-14
**Status:** Ready for planning

<domain>
## Phase Boundary

把 idea-to-task skill 的输出层重构为统一金字塔结构：从 SCQA 推演得到的 Answer（核心判断）作为顶点，向下分层展开为战略支柱（2-4 个）和关键任务，替代现有战略型/归纳型/常规三套分叉模板。保持六段式输出格式（核心判断→主题拆分→分层任务树→执行建议→风险→下一步）。MECE/So-what 内部校验属于 Phase 5 范围，不在本 phase 引入。

</domain>

<decisions>
## Implementation Decisions

### 模板统一策略
- **D-01:** 彻底合并三套模板为单一金字塔。删除 output-template.md 第 3 节的「模板选择优先级」分流，只保留一套金字塔模板；战略型/归纳型作为 SCQA 推演的内部分支标记，不再在模板层分叉
- **D-02:** 单模板必须弹性表达三种原有输出形态：战略型（总体方案+诊断线+落地线）、归纳型（单顶层主题+多里程碑）、常规（多主题并列）——通过条件字段和弹性层级实现

### 战略型条件规则
- **D-03:** 「总体方案设计」必含规则保留，作为金字塔第一支柱的条件性约束：当 SCQA 推演识别出跨部门协同、资源竞争、治理节奏、多业务线对齐等战略级信号时，第一支柱强制为「总体方案设计」，包含目标边界/现状诊断/治理机制/推进路线等里程碑
- **D-04:** 条件规则内容保留在 decision-rules.md 第 1 节「特殊输入类型处理」，不下移到 output-template.md，确保规则单一事实源

### 金字塔层级与术语
- **D-05:** 用户可见输出保持「主题拆分」术语不变。主题在金字塔结构中等同于战略支柱，对用户透明；SKILL.md 工作流步骤 5「主题识别与组织」不改名，仅补充「主题按金字塔支柱规则组织」的内部约束
- **D-06:** 层级弹性采用软规则：同层支撑点数量 2-4 个；层级深度与证据强度联动（弱证据=2 层：核心判断+主题；中证据=3 层：+里程碑；强证据=4 层：+执行项），但允许 ±1 弹性，不强制

### 弹性层级与证据强度衔接
- **D-07:** 替换 decision-rules.md 第 3 节临时的「弱=项目级/中=里程碑级/强=执行项级」映射表述，改为金字塔弹性层级术语；保留「完整度→证据强度」映射部分不动（Phase 3 已决策）
- **D-08:** 当输入天然只能支撑 2 层时（极弱证据）不强造第三层，允许金字塔停在战略支柱层并标注不确定性

### 示例校准分工
- **D-09:** 本 phase 同步在 examples.md 新增 1 组金字塔正反对比案例（对应 EXAM-02：非金字塔平铺 vs 金字塔分层），锚定本 phase 行为；其余 6 个案例中不兼容新模板的改造留给 Phase 6
- **D-10:** v1.0 已有的非战略型案例（清晰指令、简单任务）须按新模板检查是否兼容，若表层结构仍能承载不改动，若模板字段显著冲突则在 Phase 6 重写

### 文件修改范围
- **D-11:** 本 phase 修改四个文件：SKILL.md（微调步骤 5 说明与支柱约束）、decision-rules.md（更新第 3 节层级描述）、output-template.md（第 3 节彻底重写）、examples.md（新增 1 组对比）
- **D-12:** 不新增文件、不改目录结构，遵守 PROJECT.md 约束

### Claude's Discretion
- output-template.md 第 3 节金字塔模板的具体字段命名和视觉编排
- 战略型/归纳型/常规三种输出形态在单模板中的条件字段命名
- examples.md 新增案例的输入素材选择和输出长度
- SKILL.md 步骤 5 补充说明的措辞

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### 项目级约束
- `.planning/PROJECT.md` — v2.0 核心价值、Out of Scope 清单（禁止 3x3 硬约束、禁止 Action Items 表格、禁止暴露方法论术语）
- `.planning/REQUIREMENTS.md` §v2.0 Requirements / 金字塔输出 — PYMD-01..PYMD-04 四条验收标准
- `.planning/ROADMAP.md` §Phase 4 — Success Criteria 四条

### 上游 Phase 3 决策
- `.planning/phases/03-scqa/03-CONTEXT.md` — SCQA 工作流已决策（D-01..D-09），特别是 D-04/D-05（XML 推理隔离）、D-09（层级控制留给 Phase 4）
- `.planning/phases/03-scqa/03-REVIEWS.md` — Gemini + 内部评审纪律，输出接口要求字面可 grep

### 需修改的 skill 文件
- `skills/idea-to-task/SKILL.md` — 当前工作流入口，步骤 5 是主题识别环节
- `skills/idea-to-task/references/decision-rules.md` — 第 1 节 SCQA 推演与特殊输入规则、第 3 节证据强度映射
- `skills/idea-to-task/references/output-template.md` — 第 3 节分层任务树（本 phase 重写重心）
- `skills/idea-to-task/references/examples.md` — 7 个现有案例，新增 1 组金字塔对比

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **SCQA 内部推理框架**（decision-rules.md 第 1 节）：Answer 作为推演终点可直接作为金字塔顶点复用
- **向上归纳逻辑**（decision-rules.md 第 1 节第 4 步）：多主题收敛为单顶层的规则可复用为金字塔支柱合并规则
- **战略型特殊输入处理**（decision-rules.md 第 1 节末尾）：跨部门/治理节奏识别已写好，作为第一支柱条件规则的触发器
- **证据强度三档映射**（decision-rules.md 第 3 节）：弱/中/强分级框架保留，只替换层级深度表述
- **六段式输出结构**（SKILL.md 输出结构段）：作为外层容器不动，只重构第 3 段内部
- **v1.0 归纳型模板**（output-template.md 第 3 节「归纳型输入」示例）：已接近金字塔形态（单顶层+多里程碑），可作为新模板的原型

### Established Patterns
- **XML 标签内部推理隔离**（`<scqa_analysis>`）：Phase 4 可沿用此模式为内部支柱规划增加 `<pyramid_construction>` 或内联进 scqa_analysis
- **术语泄漏负面示例清单**（decision-rules.md 第 1 节末尾，Phase 3 review fix 新加）：金字塔模板中新增约束须遵循此规范
- **规则三处一致**（Phase 3 takeaway）：PLAN.md / SKILL.md / decision-rules.md 边界契约必须字面一致

### Integration Points
- **SKILL.md 步骤 5**：当前写「基于 SCQA 推演结果识别主题结构；当多个主题服务于同一核心判断时，收敛为单顶层主题」——Phase 4 需补充「每个主题即金字塔支柱，同层 2-4 个，向上支撑核心判断」
- **decision-rules.md §3 末尾「暂时保留深度接口」段**：明确标注「Phase 4 用金字塔弹性结构替代」——本 phase 兑现该接口替换
- **output-template.md §3 模板选择优先级**：本 phase 要删除的主分流点
- **examples.md §案例 5（战略型正例）+ §案例 7（归纳型正反对比）**：现有两个战略/归纳案例需在 Phase 4 末尾 spot-check 是否兼容新模板

</code_context>

<specifics>
## Specific Ideas

- 新模板要能在同一个金字塔骨架下同时容纳「总体方案+诊断线+落地线」「单顶层+多里程碑」「多主题并列」三种形态，核心手段是用条件字段（是否触发战略条件、是否触发归纳收敛）而非分叉模板
- 新增对比案例风格参考现有 §案例 7（归纳型正反对比）：先展示平铺版（同层支撑点无明显逻辑关系），再展示金字塔版（同层 2-4 个支柱，每个支柱向上支撑 Answer）
- 「主题即支柱」对用户透明：用户看到的仍是「主题拆分 / 主题 I / 主题 II」，内部按金字塔规则组织——不在输出中引入「支柱」术语

</specifics>

<deferred>
## Deferred Ideas

- MECE 互斥完备校验 / So-what 空洞过滤 — Phase 5 范围，本 phase 不引入校验逻辑，但模板要为 Phase 5 留好插入点
- 其余 6 个 fixture/examples 案例的金字塔化改造 — Phase 6 范围
- v1.0 已有非战略型 fixture 的回归验证 — Phase 6 范围
- 垂直问答关系检查（D1）、SCQA 变体适配（D3）、MECE 缺口标注（D4） — REQUIREMENTS.md Future Requirements，不在 v2.0 本次范围
- 金字塔支柱的归纳/演绎分组标记（QUAL-03） — Phase 5 范围

</deferred>

---

*Phase: 04-pyramid*
*Context gathered: 2026-04-14*
