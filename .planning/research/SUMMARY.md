# Project Research Summary

**Project:** idea-to-task v2.0 -- 咨询方法论集成
**Domain:** AI Prompt Skill Engineering (Markdown-based LLM system prompt optimization)
**Researched:** 2026-04-14
**Confidence:** MEDIUM-HIGH

## Executive Summary

idea-to-task v2.0 的核心任务是将四套咨询方法论（SCQA、金字塔原理、MECE、So-what 测试）嵌入现有的 Markdown 系统提示中，解决 v1.0 输出"横向铺开而非纵向归纳"的根本问题。这不是传统软件开发，而是 prompt engineering -- "代码"是 Markdown 指令文件，"架构"是处理管线的步骤编排，"技术栈"是 prompting 技术模式的选择。研究表明，最佳方案是将四套方法论融合为一条统一的处理管线（SCQA 推演 -> 金字塔构建 -> MECE 校验 -> So-what 过滤），而非作为独立规则堆叠。

推荐的技术组合是三层叠加：Procedural CoT（在工作流步骤中编码方法论流程）+ XML-Tagged Scratchpad（用 `<analysis>` 标签分离内部推理）+ Contrastive Few-Shot（正反对比示例校准行为）。这三层分别解决"步骤不被跳过""推理有结构可调试""输出质量有上下界"三个问题。所有变更限制在现有 4 个文件内（SKILL.md、decision-rules.md、output-template.md、examples.md），不改目录结构。

最大风险是**指令过载**和**回归退化**。四套方法论各自 3-5 条规则，如果平铺为 12-20 条并行指令，LLM 会选择性忽略。同时，新增方法论框架可能导致对简单输入也强行走战略分析流程，破坏 v1.0 已验证的处理能力。缓解策略是：方法论融合为顺序管线而非并行规则，方法论仅在战略型路径激活，v1.0 fixture 作为回归基线持续验证。

## Key Findings

### Recommended Stack

本项目的"技术栈"是 prompt engineering 技术模式，不涉及传统软件依赖。详见 [STACK.md](./STACK.md)。

**核心技术模式（三层叠加）：**
- **Procedural CoT**: 将 SCQA/MECE/Pyramid 编码为工作流有序步骤 -- 确保步骤不被跳过，与现有 SKILL.md 工作流结构天然兼容 (HIGH confidence)
- **XML-Tagged Scratchpad**: 用 `<analysis>` 标签包裹内部推理 -- Anthropic 官方推荐，Claude 原生支持，可隐藏中间推理过程 (HIGH confidence)
- **Contrastive Few-Shot**: 2-3 组正例/反例对比 -- 最可靠的输出控制手段，展示金字塔结构 vs 扁平铺开的差异 (HIGH confidence)

**辅助但不推荐的技术：**
- Step-Back Prompting / Least-to-Most: 有价值但需实验验证效果 (MEDIUM confidence)
- Self-Consistency / Tree-of-Thoughts / Auto-CoT: 不适合单次 skill prompt 场景 (LOW -- 明确不推荐)

### Expected Features

详见 [FEATURES.md](./FEATURES.md)。7 个 table stakes + 6 个 differentiators，关键路径为 T1 -> T3 -> (T4+T5+T6) -> T7。

**Must have (table stakes):**
- **T1: SCQA 输入解析层** -- 从碎片输入推演 S/C/Q/A 四要素，是所有后续功能的前提
- **T3: 金字塔原理输出结构** -- Answer 作为顶点向下分层展开，v2.0 的定义性特征
- **T4: 弹性 3x3 层级** -- 每层最多 3 个支撑点，深度根据证据强度弹性伸缩
- **T5: MECE 内部校验** -- 同层节点不重叠不遗漏，纯内部逻辑不暴露
- **T6: So-what 内部过滤** -- 剔除"加强沟通""提升效率"等空洞描述
- **T2: SCQA 追问融合** -- 信息不足时定向追问，与现有补问规则兼容
- **T7: v1.0 兼容性** -- 非战略型输入处理逻辑不被破坏

**Should have (differentiators):**
- **D6: 正反对比案例（方法论版）** -- 校准模型行为最有效手段
- **D4: MECE 缺口标注** -- 变沉默遗漏为显式风险提醒
- **D1: 垂直问答关系检查** -- 防止空洞分组

**Defer (v2+):**
- D2 归纳/演绎标记、D3 SCQA 变体适配、D5 证据联动 -- 收益不明确或需实践验证

**Anti-features (明确不做):**
- 向用户暴露 SCQA/MECE 推理过程
- 四要素逐一追问、僵硬 3x3 硬约束
- 方法论术语进入用户输出

### Architecture Approach

采用四层处理管线嵌入现有四文件结构。详见 [ARCHITECTURE.md](./ARCHITECTURE.md)。

**核心设计决策：** 不新增文件，不改目录结构。四套方法论按职责分配到现有文件中：SKILL.md 负责管线编排，decision-rules.md 负责判断逻辑（SCQA 规则 + MECE 规则 + So-what 规则），output-template.md 负责金字塔模板，examples.md 负责行为锚定。

**处理管线（5 个 Stage）：**
1. **Stage 0: 输入类型识别** -- 保留现有，判断长文本/碎片/混合
2. **Stage 1: SCQA 推演** -- 新增，替换原步骤 2-4，提取 S/C/Q/A 四要素
3. **Stage 2: 金字塔构建** -- 重构，从 Answer 出发向下分层展开
4. **Stage 3: MECE 校验** -- 新增内部逻辑，检查同层节点互斥完备
5. **Stage 4: So-what 过滤** -- 新增内部逻辑，剔除空洞描述

**关键架构决策：** 用金字塔模板统一替代现有的战略型/归纳型/常规型三套模板，消除分叉逻辑。

### Critical Pitfalls

详见 [PITFALLS.md](./PITFALLS.md)。3 个 Critical + 3 个 Moderate + 2 个 Minor。

1. **指令过载（Critical）** -- 四套方法论平铺为 12-20 条并行规则会导致 LLM 选择性忽略。**预防：** 融合为统一顺序管线，每步最多 2-3 条约束，分层加载
2. **MECE 刚性（Critical）** -- CEO 碎片输入天然重叠交叉，强制 MECE 分类会破坏自然关联。**预防：** MECE 仅用于输出验证而非输入分类，允许"软 MECE"
3. **回归退化（Critical）** -- 新增方法论破坏 v1.0 已验证的非战略型处理能力。**预防：** 保留分流机制，方法论仅战略型路径激活，v1.0 fixture 持续回归
4. **术语泄漏（Moderate）** -- SCQA/MECE 等咨询术语渗入用户输出。**预防：** 输出模板明确禁用术语列表
5. **方法论冲突（Moderate）** -- 金字塔"结论先行"与 SCQA"叙事铺垫"矛盾。**预防：** 明确分工：SCQA 用于理解输入，金字塔用于组织输出

## Implications for Roadmap

基于依赖关系和风险分布，建议 4 个阶段：

### Phase 1: SCQA 输入解析层

**Rationale:** SCQA 是管线入口，所有后续阶段依赖其输出。SCQA 的 Answer 是金字塔顶点 -- 没有 Answer 就无法构建金字塔。独立性强，可单独开发验证。
**Delivers:** decision-rules.md 新增「SCQA 推演规则」章节 + SKILL.md 工作流步骤重构（原步骤 2-4 合并为 SCQA 推演）+ 1-2 个验证 fixture
**Addresses:** T1 (SCQA 解析), T2 (SCQA 追问融合)
**Avoids:** #1 指令过载（通过将 SCQA 编码为顺序步骤而非并行规则）, #5 方法论冲突（明确 SCQA 仅用于输入理解阶段）

### Phase 2: 金字塔原理输出结构

**Rationale:** 依赖 Phase 1 的 SCQA Answer 作为顶点。是用户可感知的最大变化（输出格式重构），也是 v2.0 的定义性特征。
**Delivers:** output-template.md 用金字塔模板替换三套模板 + SKILL.md 工作流步骤更新 + 弹性 3x3 深度控制
**Addresses:** T3 (金字塔输出), T4 (弹性 3x3)
**Avoids:** #6 结构化幻觉（通过允许信息不足状态 + 弹性深度）, #7 过度递归（通过明确层级上限）

### Phase 3: MECE + So-what 内部校验

**Rationale:** 质量保障层，必须在金字塔构建完成后才有意义。两者都是内部逻辑对用户不可见，可一起实现。
**Delivers:** decision-rules.md 新增「MECE 校验规则」和「So-what 过滤规则」两章节 + SKILL.md 步骤更新
**Addresses:** T5 (MECE 校验), T6 (So-what 过滤)
**Avoids:** #2 MECE 刚性（通过定义"软 MECE" -- 用于验证而非分类）, #4 术语泄漏（通过校验结果仅影响输出质量不暴露过程）

### Phase 4: 示例校准与兼容性验证

**Rationale:** 示例必须展示完整管线行为，需要前三个 Phase 全部完成。正反对比案例是最终行为锚定，先写会因后续调整失效。同时做 v1.0 回归验证。
**Delivers:** examples.md 全面重写（5-7 个案例含正反对比）+ fixture 更新 + 端到端验证
**Addresses:** T7 (v1.0 兼容), D6 (正反对比案例)
**Avoids:** #3 回归退化（通过 v1.0 fixture 基线验证）, #8 示例-规则不一致（示例在规则之后编写）

### Phase Ordering Rationale

- **依赖链驱动：** T1(SCQA) -> T3(金字塔) -> T5+T6(校验) -> examples，每个阶段依赖前一阶段输出
- **风险前置：** Phase 1 解决最大架构风险（指令过载、方法论冲突），失败时影响范围最小
- **用户价值递增：** Phase 2 产出用户可感知的最大变化，Phase 3-4 逐步提升质量
- **回归保护：** Phase 4 作为最终兜底，确保所有变更不破坏 v1.0 能力

### Research Flags

**需要更深入研究的阶段：**
- **Phase 1:** SCQA 推演的追问触发条件需要通过实际输入测试确定边界 -- CEO 碎片输入的 SCQA 四要素完整度分布未知
- **Phase 2:** 金字塔模板统一替代三套模板后的边界情况需要实验 -- 归纳型和常规型输入在金字塔框架下的表现未验证

**可用标准模式的阶段（跳过 research-phase）：**
- **Phase 3:** MECE 和 So-what 是成熟方法论，校验规则可直接从咨询标准文献翻译为 prompt 指令
- **Phase 4:** 对比示例是 Anthropic 官方推荐的标准 prompt 技术，模式成熟

## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Stack | MEDIUM-HIGH | 核心三层技术模式有 Anthropic 官方文档支撑；辅助技术（Step-Back 等）证据较弱 |
| Features | HIGH | PROJECT.md 需求明确，feature 与需求对齐清晰，依赖关系分析完整 |
| Architecture | HIGH | 基于实际文件分析，四层管线映射到现有四文件结构自然且符合项目约束 |
| Pitfalls | HIGH | 多源交叉验证，8 个陷阱覆盖了从架构到实施的全链路风险 |

**Overall confidence:** MEDIUM-HIGH

### Gaps to Address

- **SCQA 推演在真实 CEO 输入上的效果未验证：** 研究基于方法论文献，但 CEO 碎片输入的真实分布可能与咨询场景差异大。Phase 1 需要用现有 fixture + 新增真实输入测试
- **金字塔统一模板能否覆盖所有场景未验证：** 用金字塔替代三套模板是大胆的架构简化。Phase 2 需要分别用战略型、归纳型、常规型输入验证不退化
- **MECE "软约束"的具体边界未定义：** "允许关联但任务只归属一个主题线"的操作定义需要在 Phase 3 通过案例迭代确定
- **Token 预算影响未量化：** 新增 SCQA/MECE 步骤和对比示例预计增加 500-1000 tokens，需要验证不超出上下文限制

## Sources

### Primary (HIGH confidence)
- [Anthropic Claude Prompting Best Practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) -- XML 标签、few-shot、CoT 官方指南
- [Anthropic: Use XML tags to structure prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/use-xml-tags)
- 项目实际文件分析（SKILL.md, decision-rules.md, output-template.md, examples.md）
- PROJECT.md 项目约束和需求定义

### Secondary (MEDIUM confidence)
- [Chain-of-Thought Prompting (Wei et al., 2022)](https://arxiv.org/abs/2201.11903)
- [The Prompt Report: Systematic Survey (2024-2025)](https://arxiv.org/abs/2406.06608)
- [ModelThinkers - Minto Pyramid & SCQA](https://modelthinkers.com/mental-model/minto-pyramid-scqa)
- [MECE Framework - Hacking the Case Interview](https://www.hackingthecaseinterview.com/pages/mece)
- [Lakera - Prompt Engineering Guide 2026](https://www.lakera.ai/blog/prompt-engineering-guide)
- [Prompt Regression Testing 101](https://www.breakthebuild.org/prompt-regression-testing-101-how-to-keep-your-llm-apps-from-quietly-breaking/)

### Tertiary (LOW confidence)
- [Wharton: Decreasing Value of CoT (2025)](https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought/) -- 现代 LLM 对显式 CoT 依赖度下降，需持续关注
- [Medium: XML Tags for LLM Prompts](https://medium.com/@nikhilpmarihal9/unlocking-llm-superpowers-the-secret-language-of-xml-for-perfect-prompts-d11cd9a71d22)

---
*Research completed: 2026-04-14*
*Ready for roadmap: yes*
