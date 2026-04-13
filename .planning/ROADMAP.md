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

- [ ] **Phase 3: SCQA 输入解析层** - 从碎片输入推演 SCQA 框架，为金字塔构建提供顶点
- [ ] **Phase 4: 金字塔原理输出结构** - 用统一金字塔模板替代三套模板，从顶层结论分层展开
- [ ] **Phase 5: MECE + So-what 内部质量校验** - 内部逻辑保障输出不重不漏、无空洞描述
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
**Plans**: 1 plan
Plans:
- [ ] 03-01-PLAN.md — 重构 decision-rules.md 和 SKILL.md，嵌入 SCQA 推演规则与管线工作流

### Phase 4: 金字塔原理输出结构
**Goal**: 输出从顶层结论（SCQA 的 Answer）出发，按金字塔原理向下分层展开为战略支柱和关键任务
**Depends on**: Phase 3
**Requirements**: PYMD-01, PYMD-02, PYMD-03, PYMD-04
**Success Criteria** (what must be TRUE):
  1. 输出第一层是核心判断（Answer），第二层是 2-4 个战略支柱，第三层及以下是关键任务
  2. 弹性层级生效：弱证据输入产出 2 层结构，强证据输入产出 3-4 层结构
  3. 只有一套金字塔模板在运行，不再出现战略型/归纳型/常规型的分叉选择
  4. 输出保持现有六段式格式（核心判断 -> 主题拆分 -> 分层任务树 -> 执行建议 -> 风险 -> 下一步）
**Plans**: 1 plan
Plans:
- [ ] 03-01-PLAN.md — 重构 decision-rules.md 和 SKILL.md，嵌入 SCQA 推演规则与管线工作流

### Phase 5: MECE + So-what 内部质量校验
**Goal**: AI 内部执行 MECE 互斥完备检查和 So-what 空洞过滤，输出质量可观测提升但过程不暴露
**Depends on**: Phase 4
**Requirements**: QUAL-01, QUAL-02, QUAL-03
**Success Criteria** (what must be TRUE):
  1. 同层任务分支之间不出现明显重叠（如"提升效率"和"优化流程"不并列出现）
  2. 输出中不包含五类空洞模式：无主语口号、无对象动作、无验收里程碑、父子重复、无法行动描述
  3. 每层分支数量稳定在 2-4 个，不出现单分支或 5+ 分支的情况
**Plans**: 1 plan
Plans:
- [ ] 03-01-PLAN.md — 重构 decision-rules.md 和 SKILL.md，嵌入 SCQA 推演规则与管线工作流

### Phase 6: 示例校准与兼容性验证
**Goal**: 用正反对比案例锚定完整管线行为，同时确保 v1.0 能力不退化
**Depends on**: Phase 5
**Requirements**: COMP-01, COMP-02, EXAM-01, EXAM-02, EXAM-03
**Success Criteria** (what must be TRUE):
  1. examples.md 包含 SCQA 解析、金字塔结构、MECE 检查各至少 1 组正反对比案例
  2. v1.0 已有的非战略型 fixture（简单任务、清晰指令类输入）通过回归验证，输出质量不退化
  3. 不兼容新方法论的旧 fixture/examples 已按金字塔框架重写，无残留的旧模板痕迹
  4. 端到端验证：一段真实 CEO 碎片输入经过完整管线（SCQA -> 金字塔 -> MECE -> So-what）产出结构化输出
**Plans**: 1 plan
Plans:
- [ ] 03-01-PLAN.md — 重构 decision-rules.md 和 SKILL.md，嵌入 SCQA 推演规则与管线工作流

## Progress

**Execution Order:**
Phases execute in numeric order: 3 -> 4 -> 5 -> 6

| Phase | Milestone | Plans Complete | Status | Completed |
|-------|-----------|----------------|--------|-----------|
| 1. 判断与输出重构 | v1.0 | 2/2 | Complete | 2026-04-13 |
| 2. 示例校准 | v1.0 | 1/1 | Complete | 2026-04-13 |
| 3. SCQA 输入解析层 | v2.0 | 0/1 | Planning | - |
| 4. 金字塔原理输出结构 | v2.0 | 0/TBD | Not started | - |
| 5. MECE + So-what 内部质量校验 | v2.0 | 0/TBD | Not started | - |
| 6. 示例校准与兼容性验证 | v2.0 | 0/TBD | Not started | - |
