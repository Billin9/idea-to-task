# Technology Stack: Consulting Methodology Prompt Engineering

**Project:** idea-to-task v2.0 — 咨询方法论集成
**Researched:** 2026-04-14
**Overall confidence:** MEDIUM-HIGH

## Recommended Stack

本项目不涉及传统软件依赖，"技术栈"指的是 prompt engineering 技术模式的选择。以下是将 Pyramid Principle / SCQA / MECE 嵌入 Markdown 系统提示的具体技术方案。

### 核心技术模式

| 技术 | 用途 | 为什么选它 | 置信度 |
|------|------|-----------|--------|
| **XML-Tagged Scratchpad** | 内部推理与最终输出分离 | Anthropic 官方推荐，Claude 原生支持 `<thinking>` / `<answer>` 标签分离；可隐藏中间推理过程 | HIGH |
| **Procedural Chain-of-Thought** | SCQA/MECE 作为固定推理步骤 | 在 system prompt 中编码为有序步骤列表，LLM 按步执行比自由推理更稳定 | HIGH |
| **Contrastive Few-Shot** | 展示正确 vs 错误的结构化分析 | 3-5 个对比示例（用 `<example>` 标签包裹）是 Claude 最可靠的输出控制手段 | HIGH |
| **Least-to-Most Decomposition** | 金字塔结构的自底向上构建 | 先识别碎片 → 归类 → 提炼顶层意图，天然匹配 Pyramid Principle 的归纳逻辑 | MEDIUM |
| **Step-Back Prompting** | 强制 CEO 意图抽象 | 先问"这些碎片背后的统一目标是什么？"再做细分，防止横向铺开 | MEDIUM |

### 辅助技术模式

| 技术 | 用途 | 使用条件 | 置信度 |
|------|------|---------|--------|
| **Self-Consistency (多路径投票)** | 验证 MECE 分类质量 | 仅在 API 调用场景有意义，skill prompt 内不适用 | LOW — 不推荐 |
| **Tree-of-Thoughts** | 探索多种分类方案 | 过于复杂，增加 token 消耗，对本场景收益不明确 | LOW — 不推荐 |
| **Auto-CoT** | 自动生成推理示例 | 需要大量样本聚类，不适合手工 skill prompt | LOW — 不推荐 |

## 具体实现方案

### 方案 1: XML-Tagged 内部推理（推荐）

**原理：** 在 system prompt 中指示 LLM 先在 `<analysis>` 标签内完成结构化推理，再在标签外输出最终结果。下游可以选择展示或隐藏 `<analysis>` 内容。

**为什么有效：**
- Anthropic 官方文档明确推荐使用 XML 标签分离推理与输出
- Claude 对 XML 标签的解析极其可靠，比 JSON 或自然语言分隔符更稳定
- 2025 Wharton 研究指出，现代 LLM 内部已默认执行 CoT 推理，显式 XML 标签的作用是约束推理结构而非激活推理能力

**实现模式：**
```markdown
## 内部分析步骤（不输出给用户）

在生成输出前，先在 <analysis> 标签内完成以下推理：

<analysis>
第一步 — SCQA 定位：
- Situation: CEO 当前面对什么局面？
- Complication: 什么问题/变化打破了现状？
- Question: 这引出了什么核心问题？
- Answer: CEO 真正想做的那一件事是什么？

第二步 — MECE 分类：
- 将所有输入碎片归入互斥类别
- 检验：任意两个类别是否有重叠？是否有碎片无法归入任何类别？
- 如果不满足 MECE，重新分类

第三步 — 金字塔构建：
- 顶层：第一步的 Answer（统一意图）
- 中层：第二步的 MECE 类别（主题线）
- 底层：每个类别下的具体任务项
</analysis>

然后按照输出模板生成最终结果。
```

### 方案 2: Procedural CoT（有序步骤列表）

**原理：** 不使用 XML 标签，而是将分析步骤编码为 system prompt 中的工作流有序步骤。

**为什么有效：**
- 当前 SKILL.md 已使用有序步骤的工作流结构，新方法论可自然嵌入
- Anthropic 文档建议"提供按顺序执行的步骤时使用编号列表"
- 比自由形式 CoT 更可预测

**实现模式：**
```markdown
## 工作流

### 第零步：意图归纳（新增）
1. 通读全部输入
2. 用一句话回答：CEO 真正想做的那一件事是什么？
3. 如果无法归纳为一件事 → 标记为"多意图"，分别处理

### 第一步：结构化分类
1. 将碎片按 MECE 原则分入互斥类别
2. 自检：是否有遗漏？是否有重叠？
3. 不满足则重新分类
```

### 方案 3: Contrastive Few-Shot（对比示例）

**原理：** 通过正例/反例对比，教会 LLM 什么是好的金字塔结构，什么是扁平铺开。

**为什么有效：**
- Anthropic 官方文档强调 3-5 个 few-shot 示例是最可靠的输出控制手段
- 对比示例（好 vs 坏）比纯正例更能让模型理解边界
- 当前 examples.md 已有示例框架，可扩展

**实现模式：**
```markdown
<examples>
<example type="正确 — 金字塔结构">
输入：[CEO 碎片]
分析：统一意图 = "扩大东南亚市场份额"
输出：
  核心判断：扩大东南亚市场份额
  ├─ 主题 1：市场进入策略
  ├─ 主题 2：本地化运营
  └─ 主题 3：合规与风险
</example>

<example type="错误 — 扁平铺开">
输入：[同样的 CEO 碎片]
输出：
  主题 1：印尼市场调研
  主题 2：泰国合作伙伴
  主题 3：翻译团队
  主题 4：法律合规
  → 问题：缺少统一意图，4 个主题是并列的而非层级的
</example>
</examples>
```

## 推荐组合策略

**不要只用一种技术。** 最佳实践是三层叠加：

1. **Procedural CoT** — 在工作流步骤中编码 SCQA → MECE → Pyramid 流程（骨架）
2. **XML-Tagged Scratchpad** — 用 `<analysis>` 标签包裹内部推理步骤（执行层）
3. **Contrastive Few-Shot** — 在 examples.md 中提供 2-3 组对比案例（校准层）

这三层分别解决不同问题：
- Procedural CoT 确保步骤不被跳过
- XML Scratchpad 确保推理过程有结构、可调试
- Contrastive Few-Shot 确保输出质量的上下界

## Alternatives Considered

| 类别 | 推荐方案 | 替代方案 | 为什么不选 |
|------|---------|---------|-----------|
| 推理框架 | Procedural CoT | Zero-Shot CoT ("Let's think step by step") | 太宽泛，不能保证 SCQA/MECE 结构 |
| 输出控制 | Contrastive Few-Shot | 纯规则描述 | 规则描述容易被忽略，示例更可靠 |
| 推理隐藏 | XML Tagged Scratchpad | 后处理裁剪 | XML 标签更精确，且 Claude 原生支持 |
| 分解策略 | Least-to-Most | Tree-of-Thoughts | ToT 需要多次采样，不适合单次 prompt |
| 抽象策略 | Step-Back Prompting | 直接指令"先归纳" | Step-Back 有研究支撑，效果更稳定 |

## 关键约束与注意事项

### Token 预算
- 当前 SKILL.md + references 的总 token 量需要控制
- 新增的 SCQA/MECE 步骤和对比示例会增加约 500-1000 tokens
- 控制方法：将详细方法论放入 references/ 按需加载，SKILL.md 只放精简步骤

### 与现有架构的兼容
- 当前 skill 已有 `工作流` 有序步骤 → Procedural CoT 可直接嵌入
- 当前 `examples.md` 已有示例框架 → Contrastive Few-Shot 可扩展
- 当前 `decision-rules.md` 已有决策规则 → SCQA/MECE 规则可添加新章节
- 当前 `output-template.md` 已有输出模板 → 金字塔结构约束可嵌入

### 不改变的部分
- 目录结构不变（4 个文件）
- 非战略型输入的处理逻辑不变
- 输出的六段固定结构不变（核心判断 → 主题拆分 → 分层任务树 → 执行建议 → 风险 → 下一步）

## Sources

### HIGH confidence（官方文档）
- [Anthropic Claude Prompting Best Practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) — XML 标签、few-shot、CoT 官方指南
- [Anthropic: Use XML tags to structure prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/use-xml-tags)

### MEDIUM confidence（学术研究/综合评测）
- [Chain-of-Thought Prompting Elicits Reasoning (Wei et al., 2022)](https://arxiv.org/abs/2201.11903) — CoT 原始论文
- [The Prompt Report: Systematic Survey (2024-2025)](https://arxiv.org/abs/2406.06608) — 58 种 prompting 技术分类
- [Wharton: Decreasing Value of CoT in Prompting (2025)](https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought/) — 现代 LLM 对显式 CoT 的依赖度下降
- [Galileo: 8 Chain-of-Thought Techniques](https://galileo.ai/blog/chain-of-thought-prompting-techniques) — 技术对比

### LOW confidence（社区实践/单一来源）
- [Medium: XML Tags for LLM Prompts](https://medium.com/@nikhilpmarihal9/unlocking-llm-superpowers-the-secret-language-of-xml-for-perfect-prompts-d11cd9a71d22) — XML 标签实践经验
