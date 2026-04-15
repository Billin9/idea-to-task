# Roadmap: idea-to-task 输出质量优化

## Milestones

- ✅ **v1.0 输出质量优化** — Phases 1-2 (shipped 2026-04-13)
- 🚧 **v2.0 咨询方法论重构** — Phases 3-6 (in progress)

## Phases

<details>
<summary>✅ v1.0 输出质量优化 (Phases 1-2) — SHIPPED 2026-04-13</summary>

- [x] Phase 1: 判断与输出重构 (2/2 plans) — completed 2026-04-13
- [x] Phase 2: 示例校准 (1/1 plan) — completed 2026-04-13

</details>

### 🚧 v2.0 咨询方法论重构 (In Progress)

**Milestone Goal:** 用金字塔原理 + SCQA + MECE 等咨询方法论全面重构 idea-to-task skill 的工作流和输出逻辑

- [x] **Phase 3: SCQA 输入解析层** - 从碎片输入推演 SCQA 框架，为金字塔构建提供顶点 — completed 2026-04-14
- [x] **Phase 4: 金字塔原理输出结构** - 用统一金字塔模板替代三套模板，从顶层结论分层展开 — completed 2026-04-14
- [x] **Phase 5: MECE + So-what 内部质量校验** - 内部逻辑保障输出不重不漏、无空洞描述 — completed 2026-04-15
- [ ] **Phase 6: 示例校准与兼容性验证** - 正反对比案例锚定行为，v1.0 回归保障

## Phase Details

### Phase 3: SCQA 输入解析层
**Goal**: AI 能从 CEO 碎片输入中推演出完整的 SCQA 框架，产出明确的 Answer 作为后续金字塔的顶点
**Depends on**: Phase 2 (v1.0 已完成的归纳能力)
**Requirements**: SCQA-01, SCQA-02, SCQA-03, SCQA-04
**Success Criteria** (what must be TRUE):
  1. 给定一段碎片输入，AI 能在内部推演出 Situation 和 Complication，不在输出中暴露 SCQA 术语
  2. AI 能从 S+C 推导出隐含 Question 并给出 Answer，Answer 作为输出的核心判断呈现
  3. 当输入信息严重不足（仅有模糊 Situation）时，AI 触发 2-3 个定向追问而非强行输出
  4. SCQA 完整度自动关联证据强度：四要素齐全输出到执行项层级，仅有 S 则只输出到项目层级
**Plans**: 3 plans
Plans:
- [ ] 06-01-PLAN.md — examples.md 全量重写 8 个新案例 + 顶部术语边界声明，锚定 Phase 5 UAT 5 类 + EXAM-01/02/03 三个正反对比封闭点
- [ ] 06-02-PLAN.md — SKILL.md 禁词段扩展 examples 作者侧边界句 + SKILL/decision-rules/output-template 三文件旧术语一致性扫清
- [ ] 06-03-PLAN.md — 新建 06-UAT.md 承接 Phase 5 框架，新增 v1.0 三 fixture 三维回归段 + 端到端管线段 + 四文件术语终扫断言

### Phase 4: 金字塔原理输出结构
**Goal**: 输出从顶层结论（SCQA 的 Answer）出发，按金字塔原理向下分层展开为战略支柱和关键任务
**Depends on**: Phase 3
**Requirements**: PYMD-01, PYMD-02, PYMD-03, PYMD-04
**Success Criteria** (what must be TRUE):
  1. 输出第一层是核心判断（Answer），第二层是 2-4 个战略支柱，第三层及以下是关键任务
  2. 弹性层级生效：弱证据输入产出 2 层结构，强证据输入产出 3-4 层结构
  3. 只有一套金字塔模板在运行，不再出现战略型/归纳型/常规型的分叉选择
  4. 输出保持现有六段式格式（核心判断 -> 主题拆分 -> 分层任务树 -> 执行建议 -> 风险 -> 下一步）
**Plans**: 3 plans
Plans:
- [x] 04-01-PLAN.md — 重写 output-template.md §3 为统一金字塔任务树模板（删除三模板分叉，引入弹性层级与条件分支）
- [x] 04-02-PLAN.md — SKILL.md 步骤 5 金字塔支撑约束 + decision-rules.md §3 层级术语替换 + §1 衔接引用
- [x] 04-03-PLAN.md — examples.md 新增案例 8「非金字塔平铺 vs 金字塔分层」正反对比 + v1.0 案例兼容性 spot-check

### Phase 5: MECE + So-what 内部质量校验
**Goal**: AI 内部执行 MECE 互斥完备检查和 So-what 空洞过滤，输出质量可观测提升但过程不暴露
**Depends on**: Phase 4
**Requirements**: QUAL-01, QUAL-02, QUAL-03
**Success Criteria** (what must be TRUE):
  1. 同层任务分支之间不出现明显重叠（如"提升效率"和"优化流程"不并列出现）
  2. 输出中不包含五类空洞模式：无主语口号、无对象动作、无验收里程碑、父子重复、无法行动描述
  3. 每层分支数量稳定在 2-4 个，不出现单分支或 5+ 分支的情况
**Plans**: 4 plans
Plans:
- [x] 05-01-PLAN.md — decision-rules.md 新增 §6 MECE 四维校验 + cardinality underflow/overflow 兜底规则
- [x] 05-02-PLAN.md — decision-rules.md 新增 §7 So-what 空洞过滤 + §1 末尾混合信号优先级句
- [x] 05-03-PLAN.md — SKILL.md 工作流插入「内部质量校验」步骤 + 扩展禁词 + §6/§7 懒加载注册
- [x] 05-04-PLAN.md — 05-UAT.md 行为验证脚本：5 类基础 + 3 类对抗（混合信号 / Overflow / Underflow）

**Upstream Carryover** — 源自 [`.planning/phases/04-pyramid/04-REVIEWS.md`](./phases/04-pyramid/04-REVIEWS.md)（Phase 4 跨 AI 评审共识项）：
- [HIGH] 新增行为 spot-check 验收框架：至少覆盖 5 类输入（战略型 / 归纳型 / 常规型 / 中等证据 3 层 / 极弱证据停 2 层）——本 phase 的 MECE/So-what 内部校验规则必须可通过这组输入验证，不能只依赖 grep
- [HIGH] 增加混合信号优先级对抗样例：明确「战略型 > 归纳型 > 常规型」优先级矩阵，附 1 组「公司级治理信号 + 单顶层意图」的正反例，证明不会被错误压成「单主题（归纳）」
- [MEDIUM] 补充 cardinality underflow/overflow 规则：同层候选 <2 或 >4 时的聚类/降级/补问策略（MECE 天然边界，纳入本 phase）
- [MEDIUM] 量化证据强度判别准则：强证据 = 明确阶段性目标 + 具体资源约束 + 3+ 业务维度；弱证据 = 单句或单一行动意向（Gemini 建议）——避免层级抖动

### Phase 6: 示例校准与兼容性验证
**Goal**: 用正反对比案例锚定完整管线行为，同时确保 v1.0 能力不退化
**Depends on**: Phase 5
**Requirements**: COMP-01, COMP-02, EXAM-01, EXAM-02, EXAM-03
**Success Criteria** (what must be TRUE):
  1. examples.md 包含 SCQA 解析、金字塔结构、MECE 检查各至少 1 组正反对比案例
  2. v1.0 已有的非战略型 fixture（简单任务、清晰指令类输入）通过回归验证，输出质量不退化
  3. 不兼容新方法论的旧 fixture/examples 已按金字塔框架重写，无残留的旧模板痕迹
  4. 端到端验证：一段真实 CEO 碎片输入经过完整管线（SCQA -> 金字塔 -> MECE -> So-what）产出结构化输出
**Plans**: 3 plans
Plans:
- [ ] 06-01-PLAN.md — examples.md 全量重写 8 个新案例 + 顶部术语边界声明，锚定 Phase 5 UAT 5 类 + EXAM-01/02/03 三个正反对比封闭点
- [ ] 06-02-PLAN.md — SKILL.md 禁词段扩展 examples 作者侧边界句 + SKILL/decision-rules/output-template 三文件旧术语一致性扫清
- [ ] 06-03-PLAN.md — 新建 06-UAT.md 承接 Phase 5 框架，新增 v1.0 三 fixture 三维回归段 + 端到端管线段 + 四文件术语终扫断言

**Upstream Carryover** — 源自 [`.planning/phases/04-pyramid/04-REVIEWS.md`](./phases/04-pyramid/04-REVIEWS.md)（Phase 4 跨 AI 评审共识项）：
- [HIGH] Case 1-7 系统性重写为最高优先级：Phase 4 已确认新增 Case 8 + 旧 Case 1-7 的 1:7 比例会导致 Few-shot 污染，模型可能忽略新规则沿用旧格式——这是 v1.0→v2.0 最大的回归风险
- [HIGH] 作为过渡缓冲，考虑在本 phase 起始阶段先给 Case 1-7 统一加 `(Legacy Context - Pending Update)` 前缀标记，或在 SKILL.md 中明确指示模型「优先参考 Case 8 的金字塔结构」（Gemini 建议）
- [MEDIUM] 「案例正文禁术语」边界须显式声明：examples.md 作者侧标题含「金字塔」是允许的；黑名单针对的是「模型最终输出」而非「参考文件文本」本身——避免验收自撞
- [MEDIUM] 扩大跨文件一致性扫清范围：04-02 只改了 SKILL.md step 5 和禁止词，四个文件里残留的旧「项目级 / 里程碑级 / 执行项级」表述（若有）需要在本 phase 一次性统一，或明确列出允许保留的历史文本白名单
- [MEDIUM] Phase 4 deferred 的 v1.0 非战略型 fixture 回归验证：本 phase 的端到端 SCQA→金字塔→MECE→So-what 验证必须覆盖 v1.0 的清晰指令、简单任务类输入，确保新管线不退化

## Progress

**Execution Order:**
Phases execute in numeric order: 3 -> 4 -> 5 -> 6

| Phase | Milestone | Plans Complete | Status | Completed |
|-------|-----------|----------------|--------|-----------|
| 1. 判断与输出重构 | v1.0 | 2/2 | Complete | 2026-04-13 |
| 2. 示例校准 | v1.0 | 1/1 | Complete | 2026-04-13 |
| 3. SCQA 输入解析层 | v2.0 | 1/1 | Complete | 2026-04-14 |
| 4. 金字塔原理输出结构 | v2.0 | 3/3 | Complete | 2026-04-14 |
| 5. MECE + So-what 内部质量校验 | v2.0 | 4/4 | Complete | 2026-04-15 |
| 6. 示例校准与兼容性验证 | v2.0 | 0/1 | Not started | - |
