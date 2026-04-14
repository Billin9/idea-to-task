# Phase 5: MECE + So-what 内部质量校验 - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions captured in `05-CONTEXT.md` — this log preserves the Q&A process.

**Date:** 2026-04-15
**Phase:** 05-mece-so-what
**Mode:** discuss (--batch)
**Areas selected:** all 8 (用户回复 `all`)

## 灰色决策区（用户选定）

| # | 区域 | 状态 |
|---|------|------|
| 1 | 内部推理结构整合 | 讨论 |
| 2 | MECE 校验粒度与触发条件 | 讨论 |
| 3 | So-what 空洞过滤机制 | 讨论 |
| 4 | Cardinality under/overflow 边界规则 | 讨论 |
| 5 | 混合信号优先级矩阵 | 讨论 |
| 6 | 归纳/演绎分组标记（QUAL-03） | 讨论 |
| 7 | 证据强度量化准则 | 讨论 |
| 8 | 文件改动范围划分 | 讨论 |

## Batch 1 / 4 — 结构与骨架

### Q1：内部 XML 结构选型
- **选项：** A. 两块独立 XML（`<mece_check>` + `<sowhat_filter>`）/ B. 统一 `<quality_check>` 块 / C. 内嵌到 `<scqa_analysis>` 末尾
- **用户选择：** A
- **记录：** 延续 Phase 3 XML 隔离纪律，便于 Phase 6 行为 spot-check 分别定位缺陷

### Q2：MECE 校验粒度
- **选项：** A. 轻量（cardinality + 明显重叠） / B. 中等（QUAL-01 四维）/ C. 深度（B + QUAL-03 分组标记）
- **用户选择：** B（后在 Q8 扩展包含 QUAL-03 分组标记）
- **记录：** 对齐 QUAL-01 全覆盖，QUAL-03 拆到独立问题讨论

### Q3：MECE 触发条件
- **选项：** A. 所有输入强制触发 / B. 按证据强度触发 / C. 按层级数触发
- **用户选择：** A
- **记录：** 统一触发降低模型决策负担；弱证据自动退化为 cardinality 检查

## Batch 2 / 4 — So-what + Cardinality

### Q4：So-what 空洞过滤机制
- **选项：** A. 纯模式库 / B. 纯语义重写 / C. 混合
- **用户选择：** C
- **记录：** 5 类模式库做字面黑名单 + 语义自问兜底未登记变种

### Q5：Cardinality underflow（同层 <2）
- **选项：** A. 强制上浮 / B. 追问 + 兜底退化 / C. 允许单主题通过
- **用户选择：** B
- **记录：** 与 Phase 3 追问机制咬合，MECE 不越权接管补问

### Q6：Cardinality overflow（同层 >4）
- **选项：** A. 强制归纳聚类 / B. 全部降级里程碑 / C. 在风险段列被删减
- **用户选择：** A
- **记录：** 复用 v1.0 归纳能力（decision-rules.md §1 第 4 步）

## Batch 3 / 4 — Carryover 分配与 QUAL-03

### Q7：混合信号优先级矩阵写入位置
- **选项：** A. 仅规则（§1 追加一句）/ B. 规则 + 本 phase 内嵌 fixture / C. 不写入本 phase
- **用户回复：** 「都按你的推荐来」→ A
- **记录：** 严格范围控制，fixture 归 Phase 6

### Q8：QUAL-03 归纳/演绎分组标记是否本 phase 落地
- **选项：** A. 本 phase 落地为内部标记 / B. 只写规则不强制 / C. 推迟
- **用户回复：** 「都按你的推荐来」→ A
- **记录：** QUAL-03 在 REQUIREMENTS 中锁定为 Phase 5 Active，不落地则本 phase 未闭环；Q2 的 B 粒度扩展包含此标记

### Q9：证据强度量化准则
- **选项：** A. 本 phase 补充量化 / B. 维持定性描述 / C. 参考准则
- **用户回复：** 「都按你的推荐来」→ B
- **记录：** 尊重 Phase 3 决策 D-08/09，量化判别感交给 Phase 6 fixture 锚定

## Batch 4 / 4 — 文件改动范围 + 行为验证

### Q10：四文件改动范围确认
- **选项：** A. 认可 / B. 有调整
- **用户回复：** 「都按你的推荐来」→ A
- **记录：** SKILL.md + decision-rules.md 各改动范围已 spec；output-template.md 与 examples.md 零改动

### Q11：Phase 4 carryover 行为 spot-check 承接方式
- **选项：** A. 新建 5 个 fixture / B. VERIFICATION UAT 脚本 / C. 完全推迟
- **用户回复：** 「都按你的推荐来」→ B
- **记录：** 对抗 Codex HIGH 关切（文本对 ≠ 行为对），但不越界创建 fixture；5 类 UAT 结果写入 05-VERIFICATION.md

## 无对应修正

全部 11 题首次即按推荐或用户明示选项达成共识，无返工。

## 范围蠕变抵御

| 用户未提起的越界可能 | 本 phase 处理 |
|---------------------|--------------|
| 新增 fixture 文件 | 拒绝（D-14 转为 UAT 脚本） |
| examples.md 重写 | 拒绝（Deferred → Phase 6） |
| 证据强度量化硬准则 | 拒绝（Deferred → Phase 6 间接锚定） |
| output-template.md 补充 MECE/So-what 说明 | 拒绝（D-12 零改动；规则单一事实源在 decision-rules.md） |

---

*Discussion completed: 2026-04-15*
