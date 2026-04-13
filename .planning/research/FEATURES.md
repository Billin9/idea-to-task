# Feature Landscape: 咨询方法论集成

**Domain:** AI Prompt Skill — 咨询方法论（金字塔原理 / SCQA / MECE / So-what）集成到 idea-to-task skill
**Researched:** 2026-04-14
**Overall confidence:** MEDIUM-HIGH（方法论本身成熟且文档充分，但 LLM prompt 中的实现模式仍在演进中）

## Table Stakes

用户（项目负责人）明确要求的功能，缺失则 v2.0 不成立。

| # | Feature | Why Expected | Complexity | Notes |
|---|---------|--------------|------------|-------|
| T1 | **SCQA 输入解析层** — AI 从碎片输入中推演 Situation / Complication / Question / Answer 四要素 | PROJECT.md 明确列为 Active requirement；SCQA 是金字塔原理的入口，没有它后续结构无锚点 | Medium | 核心难点：CEO 碎片输入通常只有 S 和部分 C，Q/A 需要 AI 推演补全 |
| T2 | **SCQA 信息不足时的定向追问** — 当 S/C/Q/A 中某要素完全缺失且影响方向判断时，触发最少量追问 | PROJECT.md 要求"信息不足时追问补全"；与现有补问规则（decision-rules.md 第 5 节）需融合 | Medium | 必须与现有"只补会显著改变方向的问题"原则兼容，不能变成四要素逐一追问 |
| T3 | **金字塔原理输出结构** — 输出从顶层结论（Answer）出发，向下分层展开战略支柱和关键任务 | PROJECT.md 核心价值："从顶层结论出发，向下分层展开"；这是 v2.0 的定义性特征 | High | 需要替换 output-template.md 的核心结构，同时保持与战略型/归纳型/常规型三种模板的兼容 |
| T4 | **弹性 3x3 层级结构** — 每层最多 3 个支撑点，层级深度根据证据强度弹性伸缩（2-4 层） | PROJECT.md 明确提出"弹性 3x3 结构"；金字塔原理的 Rule of Three 是核心约束 | Medium | "3" 是指导值不是硬限；证据弱时 2 层（项目→里程碑），证据强时 4 层（结论→支柱→里程碑→执行项） |
| T5 | **MECE 内部校验** — AI 在输出前内部检查任务分支不重叠、不遗漏 | PROJECT.md 明确列为 Active requirement；MECE 是金字塔原理水平关系的质量保证 | Medium | 作为内部逻辑运行，不在输出中暴露。需要定义可操作的检查规则而非抽象原则 |
| T6 | **So-what 内部过滤** — AI 在输出前内部剔除无行动意义的空洞描述 | PROJECT.md 明确列为 Active requirement；防止输出中出现"加强沟通""提升效率"等空话 | Low-Medium | 作为内部逻辑运行。核心规则：每个任务项必须能回答"做了这个，具体会改变什么？" |
| T7 | **v1.0 兼容性保持** — 现有非战略型输入处理逻辑不被破坏，能复用的 fixture/example 保留 | PROJECT.md 明确列为 Active requirement 和 Constraint | Medium | 需要评估 7 个现有案例和 5 个 fixture 哪些兼容新框架 |

## Differentiators

非必需但能显著提升输出质量的功能。建议在 table stakes 完成后选择性实现。

| # | Feature | Value Proposition | Complexity | Notes |
|---|---------|-------------------|------------|-------|
| D1 | **垂直问答关系检查** — 金字塔每一层的父节点必须是子节点的"所以呢"总结，不能只是分类标签 | 防止输出变成"三个方面"式的空洞分组；确保每层真正回答上一层的 why/how | Medium | 实现方式：在 decision-rules.md 中加入垂直关系检查步骤，类似现有的向上归纳检查 |
| D2 | **归纳 vs 演绎分组标记** — 水平支撑点标明是归纳型（同类事物的共性推出结论）还是演绎型（大前提→小前提→结论） | 帮助 AI 选择正确的分组逻辑，减少"硬拼"不相关任务的问题 | Low-Medium | 内部逻辑标记，不暴露给用户。归纳型用于多相关主题，演绎型用于因果链条 |
| D3 | **SCQA 变体适配** — 支持 SCA（省略显式 Question）和 CSA（从 Complication 切入）两种简化变体 | CEO 碎片输入很少完整包含四要素；僵硬要求完整 SCQA 会导致过度追问 | Low | 在 decision-rules.md 中定义：当 Q 可从 C 直接推导时省略显式 Q；当 S 是常识时从 C 切入 |
| D4 | **MECE 缺口标注** — 当检测到任务分支可能遗漏某方向时，在输出中用风险提醒方式标注 | 变"沉默遗漏"为"显式提醒"，让用户知道哪些方向可能没覆盖到 | Low | 复用现有"风险与高风险推断"输出区块，不需要新增输出节 |
| D5 | **证据强度与 SCQA 联动** — 将现有证据强度规则（decision-rules.md 第 6 节）与 SCQA 完整度关联 | 当前证据强度规则偏主观；SCQA 四要素的完整度提供了更可操作的判断标准 | Medium | S+C+Q+A 全有 = 强证据；S+C 有但 Q/A 需推演 = 中等；只有 S = 弱证据 |
| D6 | **正反对比案例（方法论版）** — 为每个方法论特征提供 before/after 对比示例 | v1.0 的正反对比案例（案例 7）效果好，同样模式应用到方法论特征上 | Medium | 需要为 SCQA 解析、金字塔结构、MECE 检查各提供至少 1 组正反对比 |

## Anti-Features

明确不应构建的功能。

| # | Anti-Feature | Why Avoid | What to Do Instead |
|---|--------------|-----------|-------------------|
| A1 | **向用户暴露 SCQA 解析过程** — 在输出中展示"S=...，C=...，Q=...，A=..." | PROJECT.md 明确要求 MECE/So-what 不暴露；SCQA 同理。暴露内部推理违反 SKILL.md 核心原则"不暴露内部推理" | SCQA 作为 AI 内部思维框架运行，输出直接呈现 Answer（核心判断）和结构化结果 |
| A2 | **向用户暴露 MECE/So-what 检查结果** — 在输出中写"经 MECE 检查，以下任务不重叠不遗漏" | PROJECT.md 明确要求"不向用户暴露"；用户只关心结果质量，不关心生产过程 | 检查结果体现在输出质量中：任务分支清晰不重叠、无空话 |
| A3 | **Action Items 表格输出** — 在任务树之外增加表格式行动项 | PROJECT.md Out of Scope 明确排除；会破坏现有树形输出的一致性 | 保持树形结构，执行建议整合在现有第 4 节 |
| A4 | **四要素逐一追问** — 当 SCQA 不完整时，逐个追问 S/C/Q/A | 违反现有"只补会显著改变方向的问题"原则；CEO 不会配合填表式追问 | 只追问真正缺失且影响方向的要素（通常是 C 或隐含的 Q），其余 AI 自行推演 |
| A5 | **僵硬的 3x3 硬约束** — 强制每层恰好 3 个支撑点，不允许 2 或 4 | 现实输入的复杂度不均匀；硬约束会导致凑数或砍掉重要内容 | "3" 作为指导值（2-4 皆可），超过 4 时强制重新分组 |
| A6 | **方法论术语进入用户输出** — 在输出中使用"金字塔原理""MECE""SCQA"等术语 | 用户是 CEO/团队，不是咨询顾问；术语增加认知负担 | 方法论只影响输出结构和质量，不出现在文本中 |
| A7 | **新增输入类型支持** — 趁方法论重构扩展输入类型 | PROJECT.md Out of Scope 明确排除 | 只改工作流和输出逻辑，不扩展输入边界 |

## Feature Dependencies

```
T1 (SCQA 解析) → T2 (SCQA 追问)    — 追问基于解析结果中的缺失要素
T1 (SCQA 解析) → T3 (金字塔输出)    — Answer 成为金字塔顶点
T3 (金字塔输出) → T4 (弹性 3x3)     — 3x3 约束作用于金字塔的水平展开
T3 (金字塔输出) → T5 (MECE 校验)    — MECE 检查金字塔同层节点的互斥完备性
T3 (金字塔输出) → T6 (So-what 过滤) — So-what 过滤金字塔叶子节点的空洞内容
T5 (MECE 校验) → D4 (缺口标注)      — 缺口标注是 MECE 检查的可选输出
T1 (SCQA 解析) → D5 (证据联动)      — 证据强度与 SCQA 完整度关联
D1 (垂直关系)  → D6 (正反案例)      — 正反案例需要覆盖垂直关系检查

T7 (v1.0 兼容) — 独立约束，贯穿所有 feature 的实现
```

**关键路径：** T1 → T3 → (T4 + T5 + T6) → T7 验证

## MVP Recommendation

**Phase 1（核心框架）优先：**

1. **T1: SCQA 输入解析层** — 所有后续功能的前提，没有结构化输入解析就没有结构化输出
2. **T3: 金字塔原理输出结构** — v2.0 的定义性特征，直接改变输出质量
3. **T4: 弹性 3x3 层级** — 与 T3 紧密耦合，一起实现最自然

**Phase 2（质量保障）其次：**

4. **T5: MECE 内部校验** — 保证金字塔水平关系的质量
5. **T6: So-what 内部过滤** — 保证金字塔叶子节点的质量
6. **T2: SCQA 追问融合** — 将 SCQA 缺失要素与现有补问规则整合

**Phase 3（兼容与打磨）最后：**

7. **T7: v1.0 兼容性** — 贯穿但最终验证放在最后
8. **D6: 正反对比案例** — 校准模型行为的最有效手段

**Defer:**
- D1 (垂直关系检查): 可在后续版本加入，当前金字塔结构已隐含此要求
- D2 (归纳/演绎标记): 增加复杂度但收益不明显，v1.0 的向上归纳已部分覆盖
- D3 (SCQA 变体): 当追问过多时再考虑，初始实现中 AI 自行推演已足够
- D5 (证据联动): 好想法但需要实践验证，不确定 SCQA 完整度能否可靠映射证据强度

## SCQA 解析层的具体子特征

由于 T1 是关键路径起点且复杂度需要细化：

| Sub-feature | Description | Priority |
|-------------|-------------|----------|
| T1.1 从输入推演 S（背景） | 识别输入中的已知背景和上下文 | Must |
| T1.2 从输入推演 C（矛盾/变化） | 识别打破现状的矛盾点或变化 | Must |
| T1.3 从 S+C 推导隐含 Q | 当输入没有显式问题时，从背景和矛盾推导核心问题 | Must |
| T1.4 从全局推演 A（核心判断） | 基于 S/C/Q 形成顶层结论，成为金字塔顶点 | Must |
| T1.5 SCQA 与战略型判断的交互 | 战略型输入的 SCQA 解析有特殊规则（S 通常是公司现状，C 是变革需求） | Should |
| T1.6 SCQA 与归纳型判断的交互 | 归纳型输入的多主题共享同一 SCQA 框架 | Should |

## 金字塔输出结构的具体子特征

T3 需要与现有三种模板（战略型/归纳型/常规型）融合：

| Sub-feature | Description | Priority |
|-------------|-------------|----------|
| T3.1 核心判断 = Answer | 现有"核心判断"区块改为金字塔顶点（Answer），从 SCQA 推演而来 | Must |
| T3.2 战略支柱 = 第二层 | 主题/里程碑级别作为支撑 Answer 的战略支柱 | Must |
| T3.3 关键任务 = 第三层 | 执行项级别作为支撑支柱的关键任务 | Must |
| T3.4 战略型模板适配 | 现有战略型模板的"总体方案设计→诊断线/落地线"结构映射到金字塔 | Must |
| T3.5 归纳型模板适配 | 现有归纳型模板的"顶层意图→降级里程碑"结构天然契合金字塔 | Should |
| T3.6 常规型模板适配 | 单主题/多主题常规输出的金字塔化 | Should |

## MECE 校验的具体检查规则

T5 需要从抽象原则转化为可操作的 prompt 指令：

| Check | Rule | Failure Action |
|-------|------|----------------|
| 互斥性 | 同层任意两个分支的执行范围不应重叠 — 如果做了 A 的工作内容会部分完成 B，则 A/B 重叠 | 合并或重新划分边界 |
| 完备性 | 所有分支合在一起应覆盖父节点的全部范围 — 反问"还有什么方向没覆盖？" | 补充缺失分支或在风险区标注 |
| 分组数量 | 同层分支 2-4 个为佳，超过 4 个需重新分组 | 归类后降层级 |
| 分组逻辑 | 同层分支必须基于同一维度切分（按职能/按阶段/按对象），不能混合维度 | 统一切分维度 |

## So-what 过滤的具体判断标准

T6 需要定义"空洞"的可操作定义：

| Pattern | Example | Disposition |
|---------|---------|-------------|
| 无主语无动词的口号 | "加强数据治理" | 改写为具体动作："指定数据负责人，完成数据资产盘点清单" |
| 无对象的动作 | "推进实施" | 追问：推进什么的实施？补全对象 |
| 无验收标准的里程碑 | "完成系统优化" | 补充：优化什么指标，达到什么水平 |
| 与父节点重复的子节点 | 父："提升用户体验"，子："改善用户体验" | 删除或替换为具体举措 |
| 任何人看了都不知道下一步该做什么的描述 | "建立完善的机制" | 拆解为具体的机制要素和建立步骤 |

## Sources

- [ModelThinkers - Minto Pyramid & SCQA](https://modelthinkers.com/mental-model/minto-pyramid-scqa) — MEDIUM confidence
- [The Pyramid Principle - Consulting Toolbox](https://slideworks.io/resources/the-pyramid-principle-mckinsey-toolbox-with-examples) — MEDIUM confidence
- [StrategyU - Pyramid Principle Part 2](https://strategyu.co/pyramid-principle-2/) — MEDIUM confidence
- [MECE Framework - Hacking the Case Interview](https://www.hackingthecaseinterview.com/pages/mece) — HIGH confidence
- [Issue Trees - Crafting Cases](https://www.craftingcases.com/issue-tree-guide/) — MEDIUM confidence
- [MECE for AI Task Decomposition - Towards AI](https://pub.towardsai.net/mece-the-ai-principle-youll-never-stop-using-after-reading-this-1edd335c794a) — LOW confidence
- [SCQA Framework - SlideModel](https://slidemodel.com/scqa-framework-guide/) — MEDIUM confidence
- [FunBlocks AI - Pyramid Principle](https://www.funblocks.net/thinking-matters/classic-mental-models/the-pyramid-principle) — MEDIUM confidence
