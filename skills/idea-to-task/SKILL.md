---
name: idea-to-task
description: Use when the user wants to turn messy CEO or founder chat fragments, meeting notes, voice transcripts, brain dumps, or strategy thoughts into structured themes, task trees, execution suggestions, and minimal follow-up questions.
---

# CEO 想法整理与任务化

把 CEO 的凌乱表达整理成可推进的任务树。目标不是生成会议纪要，而是输出下一步可执行结果。

## 适用场景

- 会议记录、聊天原文、语音转文字、碎片短句
- 多个主题混在一起，需要拆主线和次线
- 需要把模糊方向整理成项目级、里程碑级、执行项级任务
- 需要判断是直接输出结果，还是先补少量关键问题

## 核心原则

- 先给结论，再给结构，最后给动作
- 所有输入统一经过 SCQA 推演，从推演结果自然导出处理方式，不做前置分类
- 默认先产出，只有高风险歧义时才补问
- 细化层级不能超过证据强度
- 只提醒真正会影响方向的高风险推断
- 输出重点是任务推进，不是复述原话
- 内部推理使用 `<scqa_analysis>` 标签隔离，推理过程和方法论术语不暴露给用户
- 不暴露内部推理，不输出 `<thinking>` 或方法说明

## 工作流

1. 识别输入类型：长文本、碎片短句或混合输入
2. **SCQA 推演（内部）**：在 `<scqa_analysis>` 中从输入推演 S（背景）→ C（矛盾）→ Q（核心问题）→ A（核心判断），详见 [decision-rules.md](./references/decision-rules.md)（decision-rules.md 第 1 节）
3. 评估 SCQA 完整度：根据四项信息齐全程度确定证据强度（强 / 中 / 弱），详见 [decision-rules.md](./references/decision-rules.md)（decision-rules.md 第 3 节）
4. 追问判断：当 SCQA 关键要素缺失且影响方向时，触发 2 到 3 个定向追问；若信息足够则跳过，详见 [decision-rules.md](./references/decision-rules.md)（decision-rules.md 第 2 节）
5. 主题识别与组织：基于 SCQA 推演结果识别主题结构；当多个主题服务于同一核心判断时，收敛为单顶层主题，确实独立时分别处理；每个主题作为同一核心判断下的分层支撑点，同层主题数量保持在 2 到 4 个，保持内部组织规则对用户透明，详见 [output-template.md](./references/output-template.md) 第 3 节
6. **内部质量校验（内部）**：在输出渲染之前串行执行两块对用户透明的校验：先在 `<mece_check>` 中校验同层互斥 / 同层完备 / 数量 2-4 / 分组一致性并处理 cardinality underflow / overflow，详见 [decision-rules.md](./references/decision-rules.md) 第 6 节；再在 `<sowhat_filter>` 中按 5 类空洞模式做字面扫描 + 语义自问双道过滤，详见 [decision-rules.md](./references/decision-rules.md) 第 7 节；两块推理产生的内部标签、字段和分组标记绝对不得进入最终输出
7. 输出核心判断、主题拆分、任务树、执行建议、风险提醒、下一步动作

遇到边界不清的输入时：

- 如果 SCQA 推演中背景和矛盾清楚，但对核心判断的把握不足：先给基于最可能方向的初版任务树，再标注不确定性
- 如果同一组背景和矛盾可以导出两条相反方向：明确给出双路径，不偷偷选边
- 如果证据强度为弱：只输出到项目级

## 补问规则

- 只补会显著改变任务方向的问题
- 问题数量尽量控制在 2 到 5 个
- 如果输入已经足够推进，不要为了“更稳”而过度追问
- 如果多个主题彼此独立，先拆主题再判断是否需要补问
- SCQA 定向追问（见 [decision-rules.md](./references/decision-rules.md) 第 2 节）与通用补问合并计数，总问题数不超过 5 个

详细判定规则见 [decision-rules.md](./references/decision-rules.md) 第 2 节和第 3 节。

## 输出结构

默认按以下顺序输出：

1. 核心判断
2. 主题拆分
3. 分层任务树
4. 执行建议
5. 风险与高风险推断
6. 下一步动作

具体模板见 [output-template.md](./references/output-template.md)。

## 何时读取参考文件

- 当你需要执行 SCQA 推演、判断是否触发定向追问，或确认证据强度时，读取 [decision-rules.md](./references/decision-rules.md) 第 1-3 节
- 当你进入工作流步骤 6「内部质量校验」并启动 `<mece_check>` 时，读取 [decision-rules.md](./references/decision-rules.md) 第 6 节
- 当你在内部质量校验中启动 `<sowhat_filter>` 时，读取 [decision-rules.md](./references/decision-rules.md) 第 7 节
- 当你需要稳定输出格式时，读取 [output-template.md](./references/output-template.md)
- 当你需要校准风格或边界时，读取 [examples.md](./references/examples.md)

## 明确禁止

- 不把所有模糊表达都包装成确定结论
- 不把多个无关主题硬拼成同一个项目
- 不在证据不足时伪造细执行项
- 不把输出写成长篇会议纪要
- 不把时间节点、验证动作、交付约束误写成主题
- 不在输出中暴露 SCQA、Situation、Complication、Question、Answer 等方法论术语
- 不在输出中使用「支柱」「金字塔」「pillar」「MECE」「So-what」等内部方法论术语
- 不跳过 SCQA 推演直接输出任务树
- 不在输出中使用或暴露 `<mece_check>`、`<sowhat_filter>` 等内部校验标签及其字段
- 不在用户可见输出中使用「分组」「grouping」「inductive」「deductive」等内部分组标记术语（属 QUAL-03 内部推理，对用户透明）
