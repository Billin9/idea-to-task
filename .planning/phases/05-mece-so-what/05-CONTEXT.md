# Phase 5: MECE + So-what 内部质量校验 - Context

**Gathered:** 2026-04-15
**Status:** Ready for planning

<domain>
## Phase Boundary

在 SKILL.md 工作流中引入两块内部推理（MECE 互斥完备校验 + So-what 空洞过滤），位于 Phase 3 的 `<scqa_analysis>` 与 Phase 4 的金字塔输出之间。两块推理对用户透明，不暴露方法论术语；目标是消除同层重叠/空洞、强制分组一致、兜底 cardinality 边界。本 phase 只改 SKILL.md 和 decision-rules.md；output-template.md 与 examples.md 零改动。

</domain>

<decisions>
## Implementation Decisions

### 内部推理结构
- **D-01:** 两块独立 XML 串行：`<mece_check>` 先执行，`<sowhat_filter>` 后执行，均位于 `<scqa_analysis>` 下游、金字塔输出生成之前。延续 Phase 3 的「XML 隔离」模式，便于 Phase 6 的行为 spot-check 分别命中某一阶段的缺陷

### MECE 互斥完备校验
- **D-02:** 中等粒度校验——覆盖 QUAL-01 全四维（同层互斥 / 同层完备 / 数量 2-4 / 分组一致性），对齐 REQUIREMENTS 全覆盖
- **D-03:** 所有输入强制触发 MECE；弱证据场景（只输出到主题层）自动退化为「同层 2-4 数量检查」，避免对无分层的输出过度校验
- **D-04:** QUAL-03 归纳/演绎分组标记在本 phase 落地，作为 MECE 分组一致性维度的必要前提：`<mece_check>` 内对每层同层分支显式标 `grouping: inductive | deductive`；归纳组后续校验「分类标准一致性」，演绎组后续校验「因果推导链完整性」；标记对用户不暴露

### So-what 空洞过滤
- **D-05:** 混合机制——模式库（5 类：无主语口号 / 无对象动作 / 无验收里程碑 / 父子重复 / 无法行动描述）先做字面黑名单扫描；存活项再走语义自问（「是否具体到可指派负责人 + 可验收里程碑」），两道过滤互为冗余保障

### Cardinality 边界规则
- **D-06:** Underflow（同层 <2 个稳定候选）处理：视为「输入过窄」，由 Phase 3 的 SCQA 追问机制优先捕获；若漏到 `<mece_check>` 则兜底退化为 2 层结构（核心判断→里程碑），并在「风险与高风险推断」段标注「输入不足以支撑多主题」。MECE 不越权接管补问
- **D-07:** Overflow（同层 >4 个候选）处理：优先触发归纳聚类（复用 v1.0 向上归纳能力，已在 decision-rules.md §1 第 4 步定义）尝试合并为 2-4 个主题；若无法自然合并，则选 top 3 作为主题，其余降级为里程碑或归入「需补问」清单

### 混合信号优先级（Phase 4 评审 carryover）
- **D-08:** 战略型 + 归纳型信号同时命中时，战略型优先。写入方式：decision-rules.md §1 末尾追加一句「当战略型与归纳型信号同时命中时，优先按战略型组织，归纳收敛融入总体方案」；本 phase 不新增 fixture（严格归 Phase 6 范围）

### 证据强度机制
- **D-09:** 维持 Phase 3 的定性描述（D-08/09），不在本 phase 补充「强=3+业务维度+资源约束 / 弱=单句口号」等量化准则。量化判别感交由 Phase 6 的 fixture/examples 校准间接锚定，避免模型机械套用

### 文件改动范围
- **D-10:** `SKILL.md`：工作流步骤 6 之前新增一步「内部质量校验」，明确 `<mece_check>` + `<sowhat_filter>` 职责且对用户透明；「明确禁止」段扩展禁词，禁止在用户可见输出中出现 `mece_check / sowhat_filter / 分组 / grouping / inductive / deductive` 等术语
- **D-11:** `decision-rules.md`：§1 末尾追加混合信号优先级句；新增 §6「MECE 互斥完备校验」（四维规则 + 归纳/演绎分组标记 + cardinality under/overflow 规则）；新增 §7「So-what 空洞过滤」（5 类模式库 + 语义自问指令）
- **D-12:** `output-template.md`：零改动（Phase 4 已定型）
- **D-13:** `examples.md`：零改动（案例重写与 fixture 归 Phase 6）

### 行为验证（Phase 4 评审 carryover）
- **D-14:** Phase 5 VERIFICATION 阶段以 UAT 脚本形式覆盖 5 类代表性输入（战略型 / 归纳型 / 常规型 / 中等证据 3 层 / 极弱证据 2 层），人工对输出做行为断言（MECE 是否触发、是否仍有空洞任务、战略优先是否生效、cardinality 兜底是否按 D-06/D-07 执行）；结果写入 `05-VERIFICATION.md`。不新增 fixture 文件（归 Phase 6）

### Claude's Discretion
- `<mece_check>` / `<sowhat_filter>` XML 标签内部的字段命名与嵌套结构细节
- decision-rules.md §6 / §7 的小节切分粒度与排版顺序
- 5 类空洞模式在 §7 的具体措辞与正反对照
- SKILL.md 新增「内部质量校验」步骤的具体措辞（步骤编号衔接方式）

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### 项目级约束
- `.planning/PROJECT.md` — v2.0 核心价值、Out of Scope 清单（禁止术语泄漏、只改 4 文件）
- `.planning/REQUIREMENTS.md` §v2.0 / 内部质量校验 — QUAL-01、QUAL-02、QUAL-03 三条验收标准
- `.planning/ROADMAP.md` §Phase 5 — Success Criteria 三条 + Upstream Carryover 四条（Phase 4 评审承接项）

### 上游 Phase 决策
- `.planning/phases/03-scqa/03-CONTEXT.md` — Phase 3 已决策：XML 内部推理隔离模式（D-04/D-05）、证据强度机制不做量化（D-08/D-09）、SCQA 追问独立于通用补问（D-07）
- `.planning/phases/04-pyramid/04-CONTEXT.md` — Phase 4 已决策：战略型/归纳型作为内部条件字段（D-01/D-02）、同层 2-4 支撑点（D-06）、弹性层级（D-07）
- `.planning/phases/04-pyramid/04-REVIEWS.md` — Phase 4 跨 AI 评审共识项，Phase 5 承接 HIGH 级关切（行为 spot-check、混合信号优先级、cardinality 规则）

### 需修改的 skill 文件
- `skills/idea-to-task/SKILL.md` — 当前工作流步骤 1-6，内部质量校验步骤插入在步骤 5 与步骤 6 之间；「明确禁止」段在文件末尾
- `skills/idea-to-task/references/decision-rules.md` — 当前 §1-5，Phase 5 新增 §6（MECE）、§7（So-what），§1 末尾追加一句

### 不修改但需理解的文件
- `skills/idea-to-task/references/output-template.md` — Phase 4 定型的金字塔模板；`<mece_check>` 的分层结构必须与其骨架对齐（核心判断→主题→里程碑→执行项）
- `skills/idea-to-task/references/examples.md` — v1.0 的 7 个案例 + Phase 4 新增案例 8；Phase 5 行为验证使用独立 UAT 输入，不改此文件

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **`<scqa_analysis>` XML 内部推理模式**（Phase 3 D-04/D-05）：`<mece_check>` / `<sowhat_filter>` 直接沿用同一隔离纪律，标签嵌入位置一致（内部推理，不进最终输出）
- **向上归纳逻辑**（decision-rules.md §1 第 4 步）：D-07 overflow 聚类规则直接复用此能力，无需重建
- **术语泄漏禁令模式**（SKILL.md 明确禁止段 + Phase 4 扩展）：D-10 扩展禁词表沿用此模式
- **层级规则三处一致纪律**（Phase 3 REVIEWS takeaway 1）：MECE 的 cardinality 规则需与 SKILL.md step 5（同层 2-4）、output-template.md §3（同层 2-4）、decision-rules.md §3（弹性 2/3/4 层）字面一致

### Established Patterns
- **Procedural CoT**：SKILL.md 工作流以有序步骤编码处理流程；`<mece_check>` / `<sowhat_filter>` 作为步骤内推理，不作为新步骤暴露给用户
- **规则单一事实源**（Phase 4 D-04）：触发规则集中在 decision-rules.md，SKILL.md 只写流程约束不复写规则；本 phase MECE/So-what 规则只写在 §6/§7，SKILL.md 通过「详见 decision-rules.md 第 6/7 节」引用
- **懒加载参考**（SKILL.md「何时读取参考文件」段）：新增 §6/§7 需注册加载条件——`<mece_check>` 启动时读 §6、`<sowhat_filter>` 启动时读 §7

### Integration Points
- **SKILL.md 步骤 5 → 新增「内部质量校验」 → 步骤 6**：插入点清晰，编号可保留（用 5.5 或让原步骤 6 后移为 7）
- **decision-rules.md §1 末尾**：混合信号优先级单句插入；保留现有 5 节结构不改
- **decision-rules.md §5「常见基线偏差」后追加 §6/§7**：不打断现有 §1-§5 的逻辑流

</code_context>

<specifics>
## Specific Ideas

- QUAL-03 的 `grouping: inductive | deductive` 标记必须出现在 `<mece_check>` 内部，但不得出现在用户可见输出——Phase 5 的「明确禁止」禁词表须显式覆盖 `grouping / inductive / deductive`
- Phase 4 评审 Codex 的 HIGH 关切（「文本正确 ≠ 行为正确」）通过 D-14 的 5 类 UAT 直接回应，这是 Phase 5 风险等级能否从 HIGH 降到 MEDIUM 的关键点
- 5 类 UAT 输入应故意覆盖 Phase 4 未测场景，如「战略型 + 单顶层意图混合信号」「overflow 6 个候选方向」「underflow 单主题」——确保兜底规则真的触发

</specifics>

<deferred>
## Deferred Ideas

- 新增 fixture 文件（5 类行为 spot-check）—— Phase 6 范围，本 phase 只用 UAT 脚本一次性验证
- examples.md 中混合信号正反案例 —— Phase 6 范围（EXAM-03 对应 MECE 正反对比）
- 证据强度量化准则（强=3+业务维度；弱=单句口号）—— Phase 6 通过 fixture 间接锚定，不以规则形式落地
- v1.0 案例 1-7 系统性重写 —— Phase 6 最高优先级，本 phase 不处理
- 垂直问答关系检查（D1）、SCQA 变体适配（D3）、MECE 缺口标注（D4）—— REQUIREMENTS.md Future Requirements，v2.0 范围外

</deferred>

---

*Phase: 05-mece-so-what*
*Context gathered: 2026-04-15*
