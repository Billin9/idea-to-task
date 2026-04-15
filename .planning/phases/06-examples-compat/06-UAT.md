# Phase 6 UAT — 示例校准与兼容性验证行为脚本

**Purpose:** Phase 6 验收主文档。在 Phase 5 UAT 基础上新增三段：v1.0 回归、端到端管线、四文件术语扫清最终断言。
**执行方式:** 按段顺序执行，任一 HIGH 级失败即 Phase 6 未达成。
**术语黑名单:** 所有运行时输出正文不得出现以下术语：
- SCQA / Situation / Complication / Question / Answer
- 支柱 / 金字塔 / pillar / MECE / So-what
- mece_check / sowhat_filter / grouping / inductive / deductive / 分组

---

## 第一部分：Phase 5 UAT 5 类行为复核（继承）

本段直接引用 [`../05-mece-so-what/05-UAT.md`](../05-mece-so-what/05-UAT.md) 的类别 1-8 全部断言。Phase 6 执行时需重新跑一遍 5 类主测 + 3 类对抗测，记录结论到 `06-VERIFICATION.md`。

### 行为断言清单

- [ ] Phase 5 类别 1：战略型输入仍以总体方案相关主题先行，且正文无术语黑名单命中。
- [ ] Phase 5 类别 2：归纳型输入仍标注「单主题（归纳）」，原方向降级为里程碑。
- [ ] Phase 5 类别 3：常规型输入仍输出 2-4 个并列主题，不强拼总体方案。
- [ ] Phase 5 类别 4：中等证据输入仍只展开到里程碑层，不强造执行项层。
- [ ] Phase 5 类别 5：极弱证据输入仍停在主题层，并在风险段说明输入不足。
- [ ] Phase 5 类别 6-8：优先级、overflow、underflow 三类对抗断言仍通过。

### 失败判定

- Phase 5 任一 HIGH 级断言失败，判定为 Phase 6 对上游行为造成回归。
- 若失败由 examples.md 作者侧术语误报导致，先检查术语边界声明是否被测试脚本正确排除。

## 第二部分：v1.0 回归段（COMP-01）

将 `tests/fixtures/idea-to-task/` 下三个 v1.0 fixture 重新喂给 v2.0 skill，按 D-11 三维断言检查：结构完整性、禁词无泄漏、输入类型未被硬扣。三个类别全部通过方可视为 v1.0 不退化；任一失败视为 COMP-01 未达成。

### 类别 R1：清晰指令型（01-clear-direction.md）

**输入:** [`tests/fixtures/idea-to-task/01-clear-direction.md`](../../../tests/fixtures/idea-to-task/01-clear-direction.md)

### 三维断言清单

- [ ] 维度 1 结构完整性：输出保留六段式：核心判断 → 主题拆分 → 分层任务树 → 执行建议 → 风险与高风险推断 → 下一步动作。
- [ ] 维度 2 禁词无泄漏：对输出文本运行黑名单扫描，正文零命中。
- [ ] 维度 3 输入类型未被硬扣：不应被施加「总体方案设计」主题 I；主线应保持为销售跟进 AI 化的单一清晰方向。
- [ ] 角色建议仍至少覆盖产品、研发、销售运营，不因 v2.0 结构重写而丢失原基线能力。

### 失败判定

- 三维任一失败即记该类别「回归未通过」。
- 若清晰指令型被错误包装为公司级治理或跨部门战略结构，判定为输入类型硬扣失败。

### 类别 R2：混合主题型（02-mixed-topics.md）

**输入:** [`tests/fixtures/idea-to-task/02-mixed-topics.md`](../../../tests/fixtures/idea-to-task/02-mixed-topics.md)

### 三维断言清单

- [ ] 维度 1 结构完整性：输出保留六段式：核心判断 → 主题拆分 → 分层任务树 → 执行建议 → 风险与高风险推断 → 下一步动作。
- [ ] 维度 2 禁词无泄漏：对输出文本运行黑名单扫描，正文零命中。
- [ ] 维度 3 输入类型未被硬扣：产品 AI 化、组织协作提效、商业化试点应保持为可区分方向，不应被错压为「单主题（归纳）」。
- [ ] 如果触发补问，问题数控制在 1-3 个，且只问会改变推进方向的问题。

### 失败判定

- 三维任一失败即记该类别「回归未通过」。
- 若组织提效和商业化被混成同一个主题，判定为多主题拆分回归。

### 类别 R3：高风险模糊型（03-high-risk-ambiguity.md）

**输入:** [`tests/fixtures/idea-to-task/03-high-risk-ambiguity.md`](../../../tests/fixtures/idea-to-task/03-high-risk-ambiguity.md)

### 三维断言清单

- [ ] 维度 1 结构完整性：输出保留六段式：核心判断 → 主题拆分 → 分层任务树 → 执行建议 → 风险与高风险推断 → 下一步动作；若输出双路径，每条路径也要有任务方向。
- [ ] 维度 2 禁词无泄漏：对输出文本运行黑名单扫描，正文零命中。
- [ ] 维度 3 输入类型未被硬扣：必须显式保留「高端客户」与「中小客户」两条可能路径，不默认替 CEO 选边站。
- [ ] 风险段应标注这是方向选择级别的高风险歧义，而不是把歧义降级为普通执行风险。

### 失败判定

- 三维任一失败即记该类别「回归未通过」。
- 若输出只保留单一路径且未说明假设，判定为高风险歧义处理回归。

## 第三部分：端到端管线段（Success Criteria 4）

本段锚定 `examples.md` 中标记为「完整管线演示」的战略型 Case，验证 SCQA → 金字塔 → MECE → So-what 四段内部推理在模型运行时能完整串联。

**定位命令:** `rg -n '完整管线演示' skills/idea-to-task/references/examples.md`

### 行为断言清单

- [ ] 战略型 Case 的作者侧注释显式列出 SCQA 四字段（S/C/Q/A）推演内容。
- [ ] 核心判断段直接呼应 SCQA 推演的 Answer 字段。
- [ ] 主题 I 以「总体方案设计」或等价措辞开头。
- [ ] 同层主题分组标准一致，作者侧注释中 MECE 校验要点可追溯。
- [ ] So-what 过滤痕迹可追溯，降级或合并的候选在注释中有记录。
- [ ] 案例正文（「### 输出」段）无术语黑名单命中。

### 失败判定

- 任一断言未命中记「端到端管线不完整」。
- 若作者侧注释完整但案例正文无法体现 Answer 到核心判断的连接，判定为运行时样板不足。

## 第四部分：四文件术语扫清最终断言（COMP-02 收尾）

Phase 6 收尾 gate 对四个 skill 文件跑一次 grep，确保旧层级和旧模板术语零残留，或全部伴随「历史语言」注释。

```bash
rg -n '项目级|里程碑级|执行项级|战略型模板|归纳型模板|常规型模板|三套模板|模板选择优先级|模板分流' \
   skills/idea-to-task/SKILL.md \
   skills/idea-to-task/references/decision-rules.md \
   skills/idea-to-task/references/output-template.md \
   skills/idea-to-task/references/examples.md
```

### 行为断言清单

- [ ] rg 扫描命中数为 0，或所有命中行紧邻「历史语言」注释块。
- [ ] SKILL.md「## 明确禁止」段包含 examples.md 作者侧边界句：`rg -n 'examples\.md' skills/idea-to-task/SKILL.md | rg '作者侧|双重'`。
- [ ] examples.md 顶部存在「术语边界声明」二级标题段：`rg -n '^## 术语边界声明' skills/idea-to-task/references/examples.md`。
- [ ] examples.md 案例数量等于 8：`rg -c '^## 案例' skills/idea-to-task/references/examples.md`。
- [ ] examples.md 存在战略型端到端锚点：`rg -n '完整管线演示' skills/idea-to-task/references/examples.md`。

### 失败判定

- 任一断言未命中记「跨文件一致性未达成」。
- 旧术语若出现在运行时正文或运行时规则中，即使有其他断言通过，也判定为 COMP-02 未达成。

## 执行与记录

跑完以上四段后，在 `.planning/phases/06-examples-compat/06-VERIFICATION.md` 记录通过 / 失败 / 部分通过。

HIGH 级失败包括：
- v1.0 回归维度 2 禁词泄漏。
- 端到端管线核心判断断链。
- 四文件术语扫清 zero 断言失败。

人工 UAT 可记录为 partial，但静态断言必须在 Phase 6 收尾前给出 PASS / FAIL 结论。

### 静态断言预执行记录（2026-04-15）

| 步骤 | 断言 | 结果 | 证据 |
|------|------|------|------|
| A | 四文件旧术语终扫 | PASS | `rg` 命中 0 行 |
| B | SKILL.md examples 作者侧边界句 | PASS | `skills/idea-to-task/SKILL.md:87` 命中 `examples.md`、`作者侧`、`双重` |
| C | examples.md 顶部术语边界声明 | PASS | `skills/idea-to-task/references/examples.md:3` |
| D | examples.md 案例数量 | PASS | `rg -c '^## 案例'` 返回 `8` |
| E | 战略型 Case 管线锚点 | PASS | `完整管线演示` 命中 2 行 |

结论：Phase 6 静态门禁达成。动态回归（v1.0 fixture 运行时输出复核）交由 `06-VERIFICATION.md` 验证阶段记录。
