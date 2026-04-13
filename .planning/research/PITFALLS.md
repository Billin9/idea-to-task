# 领域陷阱：将咨询方法论集成到 LLM Prompt 系统

**领域:** AI Skill Prompt + 咨询方法论（金字塔原理、SCQA、MECE、So-what 测试）
**研究日期:** 2026-04-14
**置信度:** HIGH（多源交叉验证）

---

## 关键陷阱（Critical）

导致重写或重大回退的错误。

### 陷阱 1：指令过载——规则堆叠导致模型选择性忽略

**问题描述:** 将金字塔原理、SCQA、MECE、So-what 测试四套方法论的规则全部写入 prompt，导致指令总量超过模型的有效遵循能力（研究表明超过 5-6 条并行规则时，LLM 开始选择性丢弃规则）。

**为什么会发生:** 开发者试图"一次性教会"模型所有咨询方法论，把每个方法论的原则都列为独立规则。四套方法论各自 3-5 条规则 = 12-20 条并行指令，远超有效阈值。

**后果:**
- 模型在某些输入上遵循 MECE 但忽略金字塔原理的"结论先行"
- 不同运行之间行为不一致——有时走 SCQA 流程，有时跳过
- 调试极其困难，因为不知道模型丢弃了哪条规则

**预防策略:**
- **不要平铺方法论规则**——将四套方法论融合为一个统一的工作流步骤序列，每步最多 2-3 条约束
- **分层加载**：核心流程写在 SKILL.md，方法论细节放在 references/ 按需引用
- **优先级排序**：明确告诉模型"当规则冲突时，金字塔原理的结论先行 > MECE 的完备性 > SCQA 的叙事结构"

**检测信号:**
- 同一输入多次运行，输出结构不稳定
- 模型输出中某个方法论的痕迹消失
- 输出变长但质量下降（模型试图满足所有规则导致啰嗦）

**对应阶段:** 方法论融合阶段（应最先解决，是架构级决策）

**置信度:** HIGH
**来源:** [Lakera Prompt Engineering Guide](https://www.lakera.ai/blog/prompt-engineering-guide), [Prompt Hygiene for Engineers](https://medium.com/@2nick2patel2/prompt-hygiene-for-engineers-edc4cabdbc28), [OpenAI Community Discussion](https://community.openai.com/t/impact-of-pre-structured-reasoning-in-llm-prompts/594827)

---

### 陷阱 2：MECE 刚性——对 CEO 碎片输入强制互斥分类

**问题描述:** MECE 要求分类"互不重叠、完全穷尽"，但 CEO 的碎片想法天然是重叠的、不完整的、多维度交叉的。强制 MECE 会导致模型要么人为切割本该关联的想法，要么生成空洞的"其他"类别来凑完备性。

**为什么会发生:** 咨询场景中 MECE 处理的是已经半结构化的商业问题（市场细分、成本结构），而 CEO 的碎片想法是原始的、情绪化的、前后矛盾的。两者的输入质量差距被忽视。

**后果:**
- 本该聚合的关联想法被拆散到不同类别（"招人"和"团队文化"被强制分开）
- 出现空洞的兜底类别（"其他战略事项"）
- 输出看起来"干净"但丢失了输入中的真实关联

**预防策略:**
- **MECE 用于输出验证，不用于输入分类**——先让模型自由聚类，然后用 MECE 检查结果是否有明显遗漏或重叠
- **允许"软 MECE"**：在 prompt 中明确说"主题之间允许存在关联，但每个任务只归属一个主题线"
- **用 So-what 测试替代 CE（完全穷尽）**：不要求覆盖所有可能性，而是确保每个分类都有实际行动价值

**检测信号:**
- 输出中出现"其他"或"杂项"类别
- 明显相关的想法被分到不同主题
- 用户反馈"这两件事应该放在一起"

**对应阶段:** 决策规则更新阶段（修改 decision-rules.md 的分类逻辑）

**置信度:** HIGH
**来源:** [MECE Wikipedia](https://en.wikipedia.org/wiki/MECE_principle), [RocketBlocks MECE Deep Dive](https://www.rocketblocks.me/blog/the-mece-principle.php), [StrategyU MECE Explained](https://strategyu.co/wtf-is-mece-mutually-exclusive-collectively-exhaustive/)

---

### 陷阱 3：回归风险——新增方法论层破坏现有的非战略型处理能力

**问题描述:** 当前 skill 已经能正确处理"明确方向型"和"混合主题型"输入（v1.0 已验证）。新增咨询方法论框架后，这些已验证的能力可能静默退化——模型对简单输入也强行走金字塔分析流程，导致过度解读或输出膨胀。

**为什么会发生:** 新增的方法论指令没有作用域限定，模型无法判断"什么时候该用咨询框架，什么时候该用原有的简单处理路径"。

**后果:**
- 简单的"帮我整理这三件事"也被包装成战略分析
- 输出从简洁变为冗长
- v1.0 的 fixture 测试不再通过

**预防策略:**
- **保留并强化现有的分流机制**：decision-rules.md 中的"战略型 vs 非战略型"判断必须在方法论介入之前执行
- **方法论只在战略型路径上激活**：在 SKILL.md 工作流中明确标注"以下步骤仅当判断为战略型输入时执行"
- **v1.0 fixture 作为回归基线**：每次修改后用现有的 01/02/03 fixture 验证基本行为未变

**检测信号:**
- 对 fixture 01（clear-direction）的输出变复杂了
- 简单输入的输出长度显著增加
- 用户说"以前很简洁，现在怎么这么长"

**对应阶段:** 所有阶段（持续回归检查），但在工作流重构阶段最为关键

**置信度:** HIGH
**来源:** [Prompt Regression Testing 101](https://www.breakthebuild.org/prompt-regression-testing-101-how-to-keep-your-llm-apps-from-quietly-breaking/), [IEEE/ACM Prompt Regression Research](https://doi.org/10.1145/3644815.3644950)

---

## 中等陷阱（Moderate）

### 陷阱 4：咨询术语泄漏——SCQA、MECE 等术语出现在用户面向的输出中

**问题描述:** prompt 中大量使用"SCQA 框架"、"MECE 检查"、"金字塔结构"等术语，模型在输出中也开始使用这些术语。CEO 用户看到"经过 MECE 验证的任务分解"会感到困惑或反感。

**为什么会发生:** LLM 倾向于镜像 prompt 中的语言风格。当 prompt 充满咨询术语时，模型会"学到"这是预期的输出风格。

**后果:**
- 输出看起来像咨询报告而不是可执行的任务清单
- CEO 用户觉得工具"装腔作势"
- 真正有用的结构被术语噪音淹没

**预防策略:**
- **prompt 中使用术语，output-template 中禁止术语**：在输出模板的注释中明确写"禁止在输出中出现以下词汇：MECE、SCQA、金字塔原理、So-what 测试"
- **用动作语言替代方法论语言**："确保无遗漏" 而非 "MECE 检验"；"先给结论" 而非 "金字塔顶端"
- **在 examples.md 中展示无术语的正确输出**：让模型从示例中学到输出风格

**检测信号:**
- 输出中出现"MECE"、"SCQA"、"Pyramid"等词
- 输出语气从务实变为学术/咨询

**对应阶段:** 输出模板更新阶段

**置信度:** HIGH

---

### 陷阱 5：方法论冲突——金字塔原理与 SCQA 的叙事方向矛盾

**问题描述:** 金字塔原理要求"结论先行"（Answer First），而 SCQA 要求按"情境-冲突-问题-答案"的叙事顺序铺开。两者同时出现在 prompt 中时，模型不知道该先给结论还是先讲故事。

**为什么会发生:** 这两个框架在咨询实践中适用于不同场景（金字塔用于汇报，SCQA 用于说服），但在 prompt 中它们被并列为通用规则。

**后果:**
- 输出结构在"结论先行"和"情境铺垫"之间摇摆不定
- 同一份输出的不同部分用不同的叙事逻辑，读起来混乱
- 模型为了两头讨好，先给结论又重新从情境讲一遍，造成重复

**预防策略:**
- **明确分工**：SCQA 仅用于 skill 内部的"理解输入"阶段（帮模型理解 CEO 想法的情境和冲突），金字塔原理仅用于"组织输出"阶段（确保输出结论先行）
- **不要让两个框架同时作用于同一步骤**
- **在 decision-rules.md 中画清边界**："分析阶段用 SCQA 思考，输出阶段用金字塔呈现"

**检测信号:**
- 输出开头既有"核心判断"又有"背景分析"
- 结论被重复表述两次（一次在开头，一次在 SCQA 的 A 环节）

**对应阶段:** 工作流设计阶段

**置信度:** MEDIUM（基于方法论本身的矛盾推断，非直接实验证据）

---

### 陷阱 6：结构化幻觉——模型伪造结构完整性

**问题描述:** 当 prompt 要求输出必须包含固定的六段式结构（核心判断、主题拆分、分层任务树等），且同时要求 MECE 完备性时，模型会为了"凑齐格式"而编造内容——在信息不足时也不留空，而是生成看似合理但无依据的分析。

**为什么会发生:** 结构化框架 + 完备性要求给模型强烈的"每个格子都要填满"的压力。LLM 的本性是生成而非拒绝——在"输出完整结构"和"承认信息不足"之间，模型几乎总是选择前者。

**后果:**
- 输出的"风险分析"部分充满泛泛而谈的万能风险（"执行力不足"、"资源受限"）
- 看起来专业但实际没有可操作价值
- 用户对工具建立虚假信任，基于编造的分析做决策

**预防策略:**
- **允许并鼓励"信息不足"状态**：在 prompt 中明确写"如果输入信息不足以支撑某个输出段落，用'信息不足，建议补充 XX'替代，不要编造"
- **用 So-what 测试作为自检**："每个输出项都必须能回答'所以呢？下一步做什么？'——如果回答不了，删除该项"
- **弱化 CE（完全穷尽）要求**：从"必须覆盖所有可能"改为"覆盖输入中明确提及的维度"

**检测信号:**
- 风险部分出现"执行风险"、"沟通风险"等通用话术
- 任务树中出现与输入无关的填充任务
- 输出长度与输入复杂度不成比例（简单输入产生复杂输出）

**对应阶段:** 输出模板更新阶段 + So-what 测试集成阶段

**置信度:** HIGH

---

## 轻微陷阱（Minor）

### 陷阱 7：过度递归分解——金字塔原理驱动的无限向下展开

**问题描述:** 金字塔原理鼓励"支撑论据下面还有子论据"的层层展开。当 prompt 要求"分层任务树"并结合金字塔原理时，模型可能将 2 层就够的任务展开到 4-5 层，每层都"有理有据"但实际粒度过细。

**预防策略:**
- 在 prompt 中明确层级上限："任务树最多 3 层：项目 > 里程碑 > 执行项"
- 结合 decision-rules.md 中已有的"证据强度决定展开深度"规则——弱证据只展开到项目级

**检测信号:** 出现"子子任务"或第四层缩进

**对应阶段:** 工作流约束阶段

---

### 陷阱 8：示例-规则不一致——examples.md 与新规则脱节

**问题描述:** 修改了 SKILL.md 和 decision-rules.md 的规则，但 examples.md 和 output-template.md 中的示例仍然是旧格式。模型在"遵循规则"和"模仿示例"之间产生冲突，通常示例的影响力更大。

**预防策略:**
- **规则和示例同步更新**：每修改一条规则，必须同步更新对应示例
- **示例优先原则**：先写出理想的输出示例，再从中提炼规则（而非反过来）
- **用 fixture 测试覆盖新旧场景**

**检测信号:** 输出更像旧示例而非新规则

**对应阶段:** 示例校准阶段（必须安排在规则修改之后）

---

## 阶段风险映射

| 阶段主题 | 最可能触发的陷阱 | 缓解策略 |
|----------|-----------------|---------|
| 方法论融合设计 | #1 指令过载, #5 方法论冲突 | 统一工作流而非堆叠规则；明确分工 |
| 决策规则更新 | #2 MECE 刚性, #3 回归风险 | MECE 用于验证而非分类；保留分流机制 |
| 工作流重构 | #3 回归风险, #7 过度递归 | v1.0 fixture 作为基线；限制层级深度 |
| 输出模板更新 | #4 术语泄漏, #6 结构化幻觉 | 禁用术语列表；允许信息不足状态 |
| 示例校准 | #8 示例-规则不一致 | 示例先行，规则后行 |
| 全程持续 | #3 回归风险 | 每次修改后运行 fixture 回归 |

---

## 来源

- [Lakera - Ultimate Guide to Prompt Engineering 2026](https://www.lakera.ai/blog/prompt-engineering-guide)
- [OpenAI Community - Impact of Pre-Structured Reasoning](https://community.openai.com/t/impact-of-pre-structured-reasoning-in-llm-prompts/594827)
- [Prompt Regression Testing 101](https://www.breakthebuild.org/prompt-regression-testing-101-how-to-keep-your-llm-apps-from-quietly-breaking/)
- [IEEE/ACM - Rethinking Regression Testing for Evolving LLM APIs](https://doi.org/10.1145/3644815.3644950)
- [MECE Principle - Wikipedia](https://en.wikipedia.org/wiki/MECE_principle)
- [RocketBlocks - The MECE Principle](https://www.rocketblocks.me/blog/the-mece-principle.php)
- [StrategyU - WTF is MECE](https://strategyu.co/wtf-is-mece-mutually-exclusive-collectively-exhaustive/)
- [Prompt Hygiene for Engineers](https://medium.com/@2nick2patel2/prompt-hygiene-for-engineers-edc4cabdbc28)
- [Arxiv - Taxonomy of Prompt Defects](https://arxiv.org/html/2509.14404v1)
- [Tavoq - Minto Pyramid Principle](https://tavoq.com/blog/minto-pyramid-principle)
